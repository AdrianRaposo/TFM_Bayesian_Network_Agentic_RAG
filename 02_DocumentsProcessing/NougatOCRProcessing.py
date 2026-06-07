import os
import subprocess
from pathlib import Path
from LoggerSetUp import setup_logger
from config import(
    RAW_DATA_PATH_PDF,
    RAW_DATA_PATH_MD_NOUGAT,
    CHECKPOINT_PATH,
    LOGS_BASE_PATH,
    LOG_LEVEL
)

# Configure logging
logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='NougatOCRProcessing.log',
    error_log_filename='NougatOCRProcessing_error.log',
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
        # Read lines, strip whitespace, and filter out empty lines
        return set(line.strip() for line in f if line.strip())
    

# Process PDFs with Nougat using the checklist
def process_with_nougat(input_folder: Path, output_folder: Path, checkpoint_path: Path) -> None:
    """
    Processes PDF files in the input folder using Nougat OCR.
    Skips files that are already in the checklist or have been processed before.
    Saves the processed files in the output folder and updates the checklist.

    :param input_folder: Folder containing the input PDF files.
    :param output_folder: Folder where processed files will be saved.   
    :param checkpoint_path: Path to the checkpoint file.
    :raises FileNotFoundError: If the input folder does not exist.
    :raises Exception: If there is an error during the Nougat processing command.
    :return: None
    """
    # Check if input and output folders exist, create output folder if not
    if not os.path.exists(input_folder):
        logger.error(f"Input folder not found: {input_folder}")
        raise FileNotFoundError(f"Input folder not found: {input_folder}")
    if not os.path.exists(output_folder):
        logger.info(f"Output folder does not exist. Creating: {output_folder}")
        os.makedirs(output_folder)

    checklist = load_checklist(checkpoint_path) # Load the checklist
    logger.info(f"Loaded checklist with {len(checklist)} entries.")
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")] # Get all PDF files in the input folder
    logger.info(f"Found {len(pdf_files)} PDF files to process in {input_folder}.")

    if not pdf_files:
        logger.info("No PDF files found to process.")
        return
    # Process each PDF file
    logger.info("Starting PDF processing with Nougat...")
    for pdf_file in pdf_files:
        
        logger.info(f"Processing file: {pdf_file}")
        raw_file_name = os.path.splitext(pdf_file)[0] # Get the file name without extension
        
        # Check if the file is in the checklist
        if raw_file_name in checklist:
            logger.info(f"[PASS] Skipping (in checklist): {pdf_file}")
            continue
        # Construct paths for the PDF and output file
        pdf_path = os.path.join(input_folder, pdf_file)
        output_file = os.path.join(output_folder, raw_file_name + ".mmd")

        # Check if the output file already exists
        if os.path.exists(output_file):
            logger.info(f"[OK] Already processed (by file): {pdf_file}, skipping.")
            continue

        command = [
            "nougat",
            pdf_path,
            "--no-skipping",
            "--batchsize", "4",
            "-m", "0.1.0-base",
            "--markdown",
            "-o", output_folder
        ]

        logger.info(f">>> Processing : {pdf_file}")
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"[ERROR] Error in {pdf_file}:\n{result.stderr}")
        else:
            # Save to checkpoint
            with open(checkpoint_path, "a", encoding="utf-8") as f:
                f.write(raw_file_name + "\n")
            logger.info(f"[OK] Finished: {pdf_file}")

#
if __name__ == "__main__":
    # Use paths from config
    logger.info("Starting Nougat OCR processing script.")
    logger.info(f"Raw PDF data path: {RAW_DATA_PATH_PDF}")
    logger.info(f"Raw MD data path: {RAW_DATA_PATH_MD_NOUGAT}")
    input_folder = Path(RAW_DATA_PATH_PDF)
    output_folder = Path(RAW_DATA_PATH_MD_NOUGAT)
    checkpoint_path = Path(CHECKPOINT_PATH)
    logger.info(f"Checkpoint path: {checkpoint_path}")
    
    # Call the processing function
    logger.info("Processing PDFs with Nougat...")  
    process_with_nougat(input_folder, output_folder, checkpoint_path)
    logger.info("Processing completed.")
    logger.info("Nougat OCR processing script finished.")