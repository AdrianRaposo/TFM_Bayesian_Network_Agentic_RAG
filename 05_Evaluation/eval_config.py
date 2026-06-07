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

DB_SCHEMA_TEST_1 = os.getenv("DB_SCHEMA_TEST_1")
DB_SCHEMA_TEST_2 = os.getenv("DB_SCHEMA_TEST_2")
DB_SCHEMA_TEST_3 = os.getenv("DB_SCHEMA_TEST_3")

# DB TABLES
DB_CHUNKS_TABLE = "chunk" 
DB_ABSTRACTS_TABLE = "doc_abstract"
DB_DOC_METADATA_TABLE = "doc_metadata"
DB_DOC_AUTHORS_TABLE = "doc_author"


#  PROJECT PATHS
BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"
EVALUATION_DATA_PATH = r"../00_Data/EVALUATION" # Path to the folder containing raw PDF files

# EMBEDDING CONFIGURATION
TEST_EMBEDDING_MODEL_NAME_1 = "intfloat/e5-base-v2" # Name of the embedding model
TEST_EMBEDDING_MODEL_NAME_2 = "all-minilm-l6-v2" # Name of the embedding model
TEST_EMBEDDING_MODEL_NAME_3 = "BAAI/bge-base-en-v1.5"# Name of the embedding model

# LOGS
LOGS_BASE_PATH = r"../00_Logs/Evaluation" # Base path for logs
LOG_LEVEL = "INFO" # Log level for the application

#LLM CONFIGURATION
LLM_PROVIDER = "openai" # Name of the LLM model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY_EVALUATION = os.getenv("OPENAI_API_KEY_EVALUATION")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")
OPENAI_API_MODEL_ROUTER = os.getenv("OPENAI_API_MODEL_ROUTER")
OPENAI_API_MODEL_EMBEDDING_TEST = os.getenv("OPENAI_API_MODEL_EMBEDDING_TEST")
MAX_TOKENS_RAG_RESPONSE = 10000 # Max tokens for LLM responses in RAG
MAX_TOKEN_LLM = 5000 # Max tokens for LLM in general

# EVALUATION CONFIGURATION
OPENAI_API_MODEL_TEST = os.getenv("OPENAI_API_MODEL_TEST")
OPENAI_API_MODEL_EMBEDDING = os.getenv("OPENAI_API_MODEL_EMBEDDING")

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


GET_STRATIFIED_CHUNKS_QUERY_RAG = """
WITH doc_stats AS (
    -- Step 1: Count chunks per document, EXCLUDING short noise and obvious metadata
    SELECT 
        doc_id, 
        COUNT(chunk_pk) AS chunk_count
    FROM "{schema}"."{table}"
    WHERE token_count > 40
      -- NEW: Exclude chunks that mention "Figure 1", "Table 2", etc. (Escaped for Python)
      AND page_content !~* '(figure|table)\\s*\\d+'
      -- NEW: Exclude common publisher, metadata, and bibliography keywords
      AND page_content !~* '(copyright|all rights reserved|publisher|doi:|arxiv:|issn|isbn)'
    GROUP BY doc_id
),
quartiles AS (
    -- Step 2: Divide the documents into 4 equal buckets (Strata) based on length
    SELECT 
        doc_id,
        chunk_count,
        NTILE(4) OVER (ORDER BY chunk_count ASC) AS quartile
    FROM doc_stats
),
sampled_docs AS (
    -- Step 3: Randomly select exactly 96 documents from EACH quartile
    SELECT doc_id, quartile, chunk_count
    FROM (
        SELECT 
            doc_id, 
            quartile,
            chunk_count,
            ROW_NUMBER() OVER (PARTITION BY quartile ORDER BY RANDOM()) as rn
        FROM quartiles
    ) sub
    WHERE rn <= 96
),
sampled_chunks AS (
    -- Step 4: Assign a random row number to the candidate chunks
    SELECT 
        c.chunk_pk::text,
        c.doc_id::text,
        c.chunk_id,
        c.page_content,
        c.token_count,
        c.contains_formula,
        c.contains_code,
        c.contains_table,
        sd.quartile,
        sd.chunk_count,
        ROW_NUMBER() OVER (PARTITION BY c.doc_id ORDER BY RANDOM()) as chunk_rn
    FROM "{schema}"."{table}" c
    INNER JOIN sampled_docs sd ON c.doc_id = sd.doc_id
    WHERE c.token_count > 40
      -- NEW: Apply the same strict regex filters to the actual extraction (Escaped for Python)
      AND c.page_content !~* '(figure|table)\\s*\\d+'
      AND c.page_content !~* '(copyright|all rights reserved|publisher|doi:|arxiv:|issn|isbn)'
)
-- Step 5: Filter to keep exactly 3 random candidate chunks per selected document (Oversampling)
SELECT 
    chunk_pk,
    doc_id,
    chunk_id,
    page_content,
    token_count,
    contains_formula,
    contains_code,
    contains_table,
    quartile,
    chunk_count
FROM sampled_chunks
WHERE chunk_rn <= 3;
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


DATASETS_TO_EVALUATE = [
        "ragas_dataset_generated_openai.json",
        "ragas_dataset_generated_gemini.json",
        "ragas_dataset_generated_ollama_deepseek_r1.json",
        "ragas_dataset_generated_ollama_llama3_1.json",
        "ragas_dataset_generated_ollama_qwen3_5.json",
    ]

EVALUATED_DATASETS_OUTPUT = [
    "ragas_evaluated_ragas_dataset_generated_openai.json",
    "ragas_evaluated_ragas_dataset_generated_gemini.json",
    "ragas_evaluated_ragas_dataset_generated_ollama_deepseek_r1.json",
    "ragas_evaluated_ragas_dataset_generated_ollama_llama3_1.json",
    "ragas_evaluated_ragas_dataset_generated_ollama_qwen3_5.json",
]
