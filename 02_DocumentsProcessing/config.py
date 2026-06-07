import re
import os

from dotenv import load_dotenv

# Load environment variables from .env 
load_dotenv()

#PATHS
RAW_DATA_PATH_PDF = r"../00_Data/RAW_PDF" # Path to the folder containing raw PDF files
RAW_DATA_PATH_MD_MISTRAL = r"../00_Data/MISTRAL_RAW_MD" # Path to the folder containing raw MD files processed by MISTRAL OCR
RAW_DATA_PATH_MD_NOUGAT = r"../00_Data/NOUGAT_RAW_MD" # Path to the folder containing raw MD files processed by NOUGAT OCR
ABSTRACTS_PATH = r"../00_Data/ABSTRACTS" # Path to the folder containing abstract files
NOT_FOUND_ABSTRACT_FILE = r"../00_Data/FILES_LISTS/abstract_no_found.txt"
CLEANED_DATA_PATH = r"../00_Data/CLEANED" # Path to the folder containing cleaned data files
CLEANED_DATA_PATH_MD =r"../00_Data/CLEANED/CLEANED_MD" # Path to the folder containing cleaned MD files
CHUNKING_IMPROVED_OUTPUT_DIR=os.path.join(CLEANED_DATA_PATH, "CHUNKED", "IMPROVED_JSON") # Path to the folder for improved chunked JSON output

# ABSTRACTS_PATH = r"../00_Data/TEST/TEST_ABSTRACT" # Path to the folder containing abstract files
# CLEANED_DATA_PATH_MD =r"../00_Data/TEST/TEST_MD" # Path to the folder containing cleaned MD files
# CLEANED_DATA_PATH = r"../00_Data/TEST/" # Path to the folder containing cleaned data files
# CHUNKING_IMPROVED_OUTPUT_DIR=os.path.join(CLEANED_DATA_PATH, "TEST_CHUNK") # Path to the folder for improved chunked JSON output
# PDF_METADATA_PATH = r"../00_Data/TEST/TEST_METADATA" # Path to the folder containing PDF metadata files
# JSON_BIBLIOGRAPHY_AND_TABLES_PATH = os.path.join(CLEANED_DATA_PATH, "TEST_BIB") # Path to the folder containing JSON bibliography and tables files

#LOGS
LOGS_BASE_PATH = r"../00_Logs/DocumentsProcessing" # Base path for logs
LOG_LEVEL = "INFO" # Log level for the application

#CHECKPOINT
CHECKPOINT_PATH = r"../00_Data/FILE_LISTS/checkpoint.txt" # Path to the checkpoint file used

#MISTRAL OCR
MISTRAL_OCR_API_KEY = os.getenv("MISTRAL_OCR_API_KEY")  # API key for Mistral OCR, loaded from environment variables
MISTRAL_MODEL_NAME = "mistral-ocr-latest" # Model name for Mistral OCR, can be changed to a specific version if needed

#MODELS FOR TOKEN COUNTING
TIKTOKEN_MODEL_FOR_COUNT = "gpt-3.5-turbo"  # Model name for token counting using tiktoken

#MD PROCESSING
HEADER_SPLIT_RE = re.compile(r"(?m)^\s{0,3}(#{1,3})\s+")
SENTENCE_SPLIT_RE = r".*?(?:[.!?;\n](?!\d)(?=\s+[A-Z]|$)|$)"
FORMULA_BLOCK_PATTERN = r'\$\$(?:.|\n)*?\$\$'
FORMULA_INLINE_PATTERN = r'\$(?:\\.|[^$])+\$'
CODE_BLOCK_FENCE_PATTERN = r'```.*?```'
CODE_INLINE_PATTERN = r'`([^`]+)`'
IMAGE_MD_PATTERN = r'!\[.*?\]\(.*?\)'
TABLE_PATTERN = re.compile(
    r'(?m)'
    r'^\|(?:[^|\n]+\|?)+\s*\r?\n'         # encabezado
    r'^\|(?:\s*:?-+:?\s*\|?)+\s*\r?\n'    # separadores
    r'(?:^\|(?:[^|\n]+\|?)+\s*\r?\n?)+'   # filas de datos
) # Markdown table pattern (supports multiple rows/columns, with or without trailing |)
DATA_BLOCK_PATTERN = re.compile(
    r'(?m)(?:^(?:\S+\s*\|\s*){2,}\S*\s*$\r?\n){2,}'
)

# CHUNKING PARAMETERS
CHUNK_MIN_TOKENS = 350
CHUNK_MAX_TOKENS = 512
CHUNK_OVERLAP_FRAC = 0.10

# LIST AND DICTS FOR PROCESSING
# Map of special Unicode symbols to their ASCII equivalents or descriptions
SYMBOL_MAP = {
    "\u2018": "'", "\u2019": "'", "\u201A": "'", "\u2032": "'",  # single quotes / prime
    "\u201C": '"', "\u201D": '"', "\u201E": '"', "\u2033": '"',  # double quotes / double prime
    "\u2026": "...",  # ellipsis
    "\u2013": "-", "\u2014": "--", "\u2212": "-", "\u2010": "-", "\u2011": "-",  # dashes/minus
    "\u00A0": " ", "\u2009": " ", "\u200A": " ", "\u202F": " ", "\u2002": " ", "\u2003": " ",  # spaces
    "\u00AD": "", "\u200B": "", "\u200C": "", "\u200D": "", "\u2060": "",  # soft/zero-width
    "\u00B0": " deg", "\u00D7": "x", "\u00F7": "/", "\u00B1": "+/-",
    "\u2192": "->", "\u2190": "<-", "\u21D2": "=>",
    "\u00A9": "(c)", "\u00AE": "(R)", "\u2122": "(TM)",
    "\u00BD": "1/2", "\u00BC": "1/4", "\u00BE": "3/4",
    "•": "-", "·": "-", "∙": "-",
}
# Patterns indicating low-value content to be removed from documents
LOW_VALUE_PATTERNS = [ 
    r"corresponding author",
    r"affiliation",
    r"\bemail\b|\b@[\w\.-]+",
    r"acknowledg(e)?ments?",
    r"figure\s+\d+|table\s+\d+|caption",
    r"copyright",
    r"\babstract\b",
    r"\bkeywords?\b",
    r"\bindex terms?\b",
    r"\bconflict(s)? of interest\b",
    r"\bfunding\b|\bgrant\b|\bsponsor(ed)?\b",
    r"\bhow to cite\b|\bcitation\b",
    r"\breferences\b",
    r"\bbibliograph(y|ies)\b",
    r"\bdoi\b",
    r"\bissn\b",
    r"\bisbn\b",
    r"\blicense\b",
    r"\bcreative commons\b",
    r"\ball rights reserved\b",
    r"\bfootnote\b",
    r"\bmanuscript\b",
    r"\bsubmitted\b|\baccepted\b|\breceived\b",
    r"\bpeer[- ]review(ed)?\b",
    r"\bappendix\b",
    r"\bsee (figure|table|section)\b",
    r"\babbreviation(s)?\b",
    r"\bglossary\b",
]
