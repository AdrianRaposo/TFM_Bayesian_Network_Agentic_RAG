# config.py
'''
Docstring for 04_AgenticRAG.config
This module contains configuration settings for the Agentic RAG system.
'''
import os

from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env 
load_dotenv()

# JSON_BIBLIOGRAPHY_AND_TABLES_PATH = os.path.join(CLEANED_DATA_PATH, "TEST_BIB") # Path to the folder containing JSON bibliography and tables files

# DB CONFIGURATION
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SCHEMA = os.getenv("DB_SCHEMA")

# DB TABLES
DB_CHUNKS_TABLE = "chunk" 
DB_ABSTRACTS_TABLE = "doc_abstract"
DB_DOC_METADATA_TABLE = "doc_metadata"
DB_DOC_AUTHORS_TABLE = "doc_author"


#  PROJECT PATHS
BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"

# EMBEDDING CONFIGURATION
EMBEDDING_MODEL_NAME = "intfloat/e5-base-v2" # Name of the embedding model

# LOGS
LOGS_BASE_PATH = r"../00_Logs/AgenticRAG" # Base path for logs
LOG_LEVEL = "INFO" # Log level for the application

#LLM CONFIGURATION
LLM_PROVIDER = "openai" # Name of the LLM model
LLM_PROVIDER_RAG = "openai" # Name of the LLM model for RAG (puede ser diferente al general para tener un modelo más potente solo en RAG)

#OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")
OPENAI_API_MODEL_ROUTER = os.getenv("OPENAI_API_MODEL_ROUTER")

# Google Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_API_MODEL = os.getenv("GEMINI_API_MODEL")
GEMINI_API_MODEL_ROUTER = os.getenv("GEMINI_API_MODEL_ROUTER")

# Local (Ollama) - Por si quieres usar Llama3 localmente
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3") # Nombre amigable para los logs y outputs
OLLAMA_MODEL_ROUTER = os.getenv("OLLAMA_MODEL_ROUTER", "llama3")

MAX_TOKENS_RAG_RESPONSE = 10000 # Max tokens for LLM responses in RAG
MAX_TOKEN_LLM = 5000 # Max tokens for LLM in general


# RETRIEVAL CONFIGURATION
MAX_RESULTS_RETRIEVED = 10 # Number of top documents to retrieve
N_MAX_DOC_REPETITION =  5 # Penalty for document repetition in retrieval
PONDERTATION_ALPHA = 0.75 # Weighting factor for combining BM25 and Dense retrieval scores
PONDERTATION_BETA = 0.15 # Weighting factor for combining BM25 and Dense retrieval scores
PONDERTATION_GAMMA = 0.10 # Weighting factor for combining BM25 and Dense retrieval scores

GET_DOC_METADATA_QUERY_RAG = """
    SELECT 
        dm.doc_id
        ,dm.title
        ,dm."year"
        ,dm.journal_name
        ,dm.doi_url
        ,STRING_AGG(DISTINCT (da.given || ' ' || da.family), ', ') AS authors
    FROM "{schema}"."{meta_table}" dm
    LEFT JOIN "{schema}"."{auth_table}" da ON dm.doc_id = da.doc_id
    WHERE dm.doc_id = %s
    GROUP BY dm.doc_id, dm.title, dm.year, dm.journal_name, dm.doi_url;
"""
SEARCH_CHUNKS_QUERY_BM25_RAG = """
    SELECT 
        chunk_pk
        , doc_id
        , page_content
        , ts_rank_cd(content_ft, to_tsquery('english', %s)) AS rank
        , embedding <#> %s AS dist
    FROM "{schema}"."{table}"
    WHERE content_ft @@ to_tsquery('english', %s)
    ORDER BY rank DESC
    LIMIT %s;
"""

SEARCH_ABSTRACTS_QUERY_RAG = """
    SELECT 
        doc_id
        , abstract
        , embedding <#> %s AS dist
    FROM "{schema}"."{table}"
    ORDER BY embedding <#> %s
    LIMIT %s;
"""

GET_TOP_CHUNKS_PER_DOC_QUERY_RAG = """
    WITH ranked AS (
        SELECT 
            chunk_pk,
            doc_id,
            page_content,
            embedding <#> %s AS dist,
            ROW_NUMBER() OVER (
                PARTITION BY doc_id 
                ORDER BY embedding <#> %s
            ) AS rn
        FROM "{schema}"."{table}"
        WHERE doc_id = ANY(%s)
    )
    SELECT *
    FROM ranked
    WHERE rn <= %s
    ORDER BY dist;
"""

GET_TOP_DENSE_CHUNKS_QUERY_RAG = """
    SELECT 
        chunk_pk
        , doc_id
        , page_content
        , embedding <#> %s AS dist
    FROM "{schema}"."{table}"
    ORDER BY embedding <#> %s
    LIMIT %s;
"""

# METADATA CONFIGURATION

TABLE_SCHEMAS = {

    "doc_abstract": """
    CREATE TABLE doc_abstract (
        doc_id uuid PRIMARY KEY REFERENCES doc(doc_id) ON DELETE CASCADE,
        abstract text NOT NULL,
        has_abstract bool NOT NULL DEFAULT true,
        embedding vector
    );
    """,
    
    "doc_author": """
    CREATE TABLE doc_author (
        doc_id uuid NOT NULL REFERENCES doc(doc_id),
        "sequence" int NOT NULL,
        given text,
        "family" text,
        normalized_given text,
        normalized_family text,
        PRIMARY KEY (doc_id, "sequence")
    );
    """,
    
    "doc_metadata": """
    CREATE TABLE doc_metadata (
        doc_id uuid PRIMARY KEY REFERENCES doc(doc_id),
        doi varchar(255),
        title text,
        "year" int,
        journal_name text,
        publisher text,
        genre varchar(50),
        doi_url text
    );

    """,
}

MAX_RETRIES = 1
NOT_FOUND_PHRASE = "I cannot"
MAX_ROWS = 10

