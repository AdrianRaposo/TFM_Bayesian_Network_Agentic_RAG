import re
import os

from dotenv import load_dotenv

# Load environment variables from .env 
load_dotenv()

# PATHS
ABSTRACTS_PATH = r"../00_Data/ABSTRACTS" # Path to the folder containing abstract files
CLEANED_DATA_PATH_MD =r"../00_Data/CLEANED/CLEANED_MD" # Path to the folder containing cleaned MD files
CLEANED_DATA_PATH = r"../00_Data/CLEANED" # Path to the folder containing cleaned data files
CHUNKING_IMPROVED_OUTPUT_DIR=os.path.join(CLEANED_DATA_PATH, "CHUNKED", "IMPROVED_JSON") # Path to the folder for improved chunked JSON output
PDF_METADATA_PATH = r"../00_Data/PDF_METADATA" # Path to the folder containing PDF metadata files
JSON_BIBLIOGRAPHY_AND_TABLES_PATH = os.path.join(CLEANED_DATA_PATH, "JSON_BIBLIOGRAPHY_AND_TABLES") # Path to the folder containing JSON bibliography and tables files


# DB CONFIGURATION
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SCHEMA = os.getenv("DB_SCHEMA")

REQUIRED_EXTENSIONS = ["vector", "uuid-ossp", "pg_trgm"]
REQUIRED_TABLES = [
    "doc", "doc_abstract", "doc_reference", "doc_table",
    "chunk", "chunk_link",
    "rag_query_log", "rag_retrieval_hit", "rag_feedback",
    "doc_metadata","doc_author"
]


# EMBEDDING CONFIGURATION
EMBEDDING_MODEL_NAME = "intfloat/e5-base-v2" # Name of the embedding model
#EMBEDDING_MODEL_NAME = "all-minilm-l6-v2" # Name of the embedding model
#EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"

# METADATA INFORMATION
OCR_USED = "Mistral_OCR" # OCR tool used for text extraction

# LOGS
LOGS_BASE_PATH = r"../00_Logs/DataIngestion" # Base path for logs
LOG_LEVEL = "INFO" # Log level for the application
