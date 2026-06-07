from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

#PATHS
RAW_DATA_PATH_PDF = r"../00_Data/RAW_PDF" # Path to the folder containing raw PDF files
PDF_METADATA_PATH = r"../00_Data/PDF_METADATA" # Path to the folder containing PDF metadata files
CSV_DOI_PATH = r"../00_Data/WOS_DATA/CSV_DOCUMENTS_DATA/filtered_wos_data.xlsx" # Path to the folder containing CSV with DOIs
RESULTS_FOLDER = r"../00_Data/WOS_DATA/RESULTS_FILES" # Path to the folder containing results
BIBLIOGRAPHY_APA_FILE = r"../00_Data/BIBLIOGRAPHY_DATA/BIBLIOGRAPHY_FROM_BOOKS/APA_Bibliography_KollerFriedman.txt" # Path to the folder containing bibliography data
BIBLIOGRAPHY_SPRINGER_FILE = r"../00_Data/BIBLIOGRAPHY_DATA/BIBLIOGRAPHY_FROM_BOOKS/SPRINGER_Bibliography_LuisSucar.txt" # Path to the folder containing bibliography data
BIBLIOGRAPHY_TITLES_FOLDER = r"../00_Data/BIBLIOGRAPHY_DATA/BIBLIOGRAPHY_TITLES" # Path to the folder containing bibliography titles

#EMAIL
EMAIL = os.getenv("EMAIL")

#LOGS
LOGS_BASE_PATH = r"../00_Logs/DocumentsAdquisition" # Base path for logs
LOG_LEVEL = "INFO" # Log level for the application

