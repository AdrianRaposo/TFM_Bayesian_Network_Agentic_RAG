import os
from mistralai import Mistral
from pathlib import Path
from LoggerSetUp import setup_logger

from config import(
    RAW_DATA_PATH_PDF,
    RAW_DATA_PATH_MD_MISTRAL,
    CHECKPOINT_PATH,
    LOGS_BASE_PATH,
    LOG_LEVEL,
    MISTRAL_OCR_API_KEY,
    MISTRAL_MODEL_NAME
)

# Initialize Mistral OCR client
mistral_client = Mistral(api_key=MISTRAL_OCR_API_KEY)

# Configure logging
logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='MistralOCRProcessing.log',
    error_log_filename='MistralOCRProcessing_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='w',
    error_mode='w'
)

# Load checklist from a file
def load_checklist(path_checkpoint: str) -> set:
    """
    Loads a checklist from a file.
    Each line in the file is treated as an entry in the checklist.
    If the file does not exist, returns an empty set.

    :param path_checkpoint: Path to the checkpoint file.
    :return: A set of entries from the checklist.
    """
    if not os.path.exists(path_checkpoint):
        logger.warning(f"Checkpoint file not found: {path_checkpoint}. Returning empty checklist.")
        return set()
    with open(path_checkpoint, "r", encoding="utf-8") as f:
        logger.info(f"Loading checklist from: {path_checkpoint}")
        return set(line.strip() for line in f if line.strip())
    
# Load porcessed files from the directory
def load_processed_files(directory: Path) -> set:
    """
    Loads the names of processed files from a directory.
    Returns a set of file names without extensions.

    :param directory: Path to the directory containing processed files.
    :return: A set of processed file names without extensions.
    """
    if not directory.exists():
        logger.warning(f"Directory does not exist: {directory}. Returning empty set.")
        return set()
    
    return {file.stem for file in directory.glob("*") if file.is_file()}

# Get the list of files to process
def get_files_to_process(input_folder: Path, checklist: set, processed_files: set) -> set:
    """
    Gets the list of files to process based on the input folder, checklist, and processed files.

    :param input_folder: Path to the folder containing input files.
    :param checklist: Set of files to be processed.
    :param processed_files: Set of already processed files.
    :return: A set of files to be processed.
    """
    if not input_folder.exists():
        logger.warning(f"Input folder does not exist: {input_folder}. Returning empty set.")
        return set()
    # Get all PDF files in the input folder
    pdf_files = {file.stem for file in input_folder.glob("*.pdf") if file.is_file()}
    files_to_process =  pdf_files - (checklist | processed_files)
    
    return files_to_process

#Append the processed file to the checklist
def append_to_checklist(file_name: str, path_checkpoint: str) -> None:
    """
    Appends a file name to the checklist file.

    :param file_name: Name of the file to append.
    :param path_checkpoint: Path to the checkpoint file.
    """
    with open(path_checkpoint, "a", encoding="utf-8") as f:
        f.write(f"{file_name}\n")
    logger.info(f"Appended {file_name} to checklist.")



# Process a single file with Mistral OCR
def process_file(file_name: str) -> None:
    """
    Processes a single file with Mistral OCR.

    :param file_name: Name of the file to process.
    """
    input_file_path = Path(RAW_DATA_PATH_PDF) / f"{file_name}.pdf"
    output_file_path = Path(RAW_DATA_PATH_MD_MISTRAL) / f"{file_name}.md"

    if not input_file_path.exists():
        logger.error(f"Input file does not exist: {input_file_path}")
        return

    # Upload the file to Mistral OCR
    logger.info(f"Uploading file: {input_file_path.name} to Mistral OCR.")
    document_uploaded = mistral_client.files.upload(
        file={"file_name": input_file_path.name, "content": open(input_file_path, "rb")},
        purpose="ocr"
    )
    #Get signed URL for the uploaded file
    signed_url = mistral_client.files.get_signed_url(file_id=document_uploaded.id)
  
    # Process the file with Mistral OCR
    try:   
        logger.info(f"Processing file: {input_file_path.name} with Mistral OCR.")
        response = mistral_client.ocr.process(
            document={"type": "document_url", "document_url": signed_url.url},
            model=MISTRAL_MODEL_NAME
        )
        markdown = "\n\n".join(page.markdown for page in response.pages)
        # Save the processed data to a MD file from response
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        # Append the processed file name to the checklist
        append_to_checklist(file_name, CHECKPOINT_PATH)
    except Exception as e:
        logger.error(f"Error processing file {input_file_path.name}: {e}")

def main():
    # Load the checklist
    checklist = load_checklist(CHECKPOINT_PATH)
    logger.info(f"Loaded checklist with {len(checklist)} entries.")
    # Load the processed files
    processed_files = load_processed_files(Path(RAW_DATA_PATH_MD_MISTRAL))
    logger.info(f"Loaded {len(processed_files)} processed files from {RAW_DATA_PATH_MD_MISTRAL}.")
    # Get the files to process
    files_to_process = get_files_to_process(Path(RAW_DATA_PATH_PDF), checklist, processed_files)
    if not files_to_process:
        logger.info("No new files to process.")
    else:
        logger.info(f"Found {len(files_to_process)} files to process.")

    for file in files_to_process:
        process_file(file)

if __name__ == "__main__":
    main()

