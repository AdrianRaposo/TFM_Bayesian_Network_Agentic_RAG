import psycopg
import os
import json
import uuid
import unicodedata
import datetime

from psycopg.rows import TupleRow
from psycopg.types import json as pg_json
from psycopg import Cursor, rows
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from DBConnectionTest import connect_db, check_extension, check_tables

#from psycopg import json
from sentence_transformers import SentenceTransformer
import torch

from psycopg.rows import dict_row
from LoggerSetUp import setup_logger
from config import(
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_SCHEMA,
    ABSTRACTS_PATH,
    CLEANED_DATA_PATH_MD,
    CLEANED_DATA_PATH,
    CHUNKING_IMPROVED_OUTPUT_DIR,
    PDF_METADATA_PATH,
    JSON_BIBLIOGRAPHY_AND_TABLES_PATH,
    OCR_USED,
    LOGS_BASE_PATH,
    LOG_LEVEL,
    EMBEDDING_MODEL_NAME
)

# Configure logger
logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='DataIngestion.log',
    error_log_filename='DataIngestion_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='w',
    error_mode='w'
)

# AUX functions
def get_document_stems(abstracts_path: str, cleaned_md_path: str, biblio_path: str, chunks_path: str, metadata_path: str) -> List[str]:
    """
    Retrieves the list of 'stems' (file names without extension) of documents 
    that have all the required files (abstract, markdown, bibliography, chunks).

    Args:
        abstracts_path (str): Path to the abstracts directory.
        cleaned_md_path (str): Path to the cleaned markdown files directory.
        biblio_path (str): Path to the bibliography and tables JSON files directory.
        chunks_path (str): Path to the chunks JSON files directory.
        metadata_path (str): Path to the PDF metadata files directory.
    Returns:
        List[str]: List of document stems that have all required files.
    """
    #  List Markdown files
    md_files = [f for f in os.listdir(cleaned_md_path) if f.endswith('.md')]
    md_stems = {os.path.splitext(f)[0] for f in md_files}
    # List plain text abstracts
    abstract_stems = {os.path.splitext(f)[0] for f in os.listdir(abstracts_path) if f.endswith('.md')}
    # List JSON files for bibliography/tables
    biblio_stems = {os.path.splitext(f)[0] for f in os.listdir(biblio_path) if f.endswith('.json')}
    # List JSON files for chunks
    chunks_stems = {os.path.splitext(f)[0] for f in os.listdir(chunks_path) if f.endswith('.json')}
    # List PDF metadata files
    metadata_stems = {os.path.splitext(f)[0] for f in os.listdir(metadata_path) if f.endswith('.json')}
    # Find common stems
    common_stems = md_stems & abstract_stems & biblio_stems & chunks_stems & metadata_stems

    # Report documents with missing files
    all_stems = md_stems  # Start with MD stems
    missing_reports = []
    for stem in sorted(all_stems):
        missing = []
        if stem not in abstract_stems:
            missing.append("abstract")
        if stem not in biblio_stems:
            missing.append("bibliografía/tablas")
        if stem not in chunks_stems:
            missing.append("chunks")
        if stem not in metadata_stems:
            missing.append("metadatos")
        if missing:
            missing_reports.append(f"{stem}: falta {', '.join(missing)}")
    if missing_reports:
        logger.warning("Documentos con archivos faltantes:")
        for report in missing_reports:
            logger.warning(" - %s", report)

    # Return sorted list of stems with all required files
    return sorted(common_stems)

def normalize_author_name(name: Optional[str]) -> Optional[str]:
    """Normalize author names by removing accents and converting to lowercase.
    Args:
        name (Optional[str]): The author's name.

    Returns:
        Optional[str]: The normalized author name.
    """
    if name is None:
        return None
    # Remove accents and convert to lowercase
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('utf-8')
    return name

def vector_literal(vec) -> str:
    """Convert a vector (list or numpy array) to PostgreSQL vector literal format.
    Args:
        vec (Union[list, np.ndarray]): The input vector to convert.

    Returns:
        str: The PostgreSQL vector literal representation of the input vector.
    """
    try:
        arr = vec.tolist()
    except Exception:
        arr = vec
    return "[" + ",".join(f"{float(x):.6f}" for x in arr) + "]"

# Insert Db functions

def load_pdf_metadata(metadata: Dict, md_path:str, stem: str, cur: Cursor[TupleRow]) -> uuid.UUID:
    """Load PDF metadata into the database.
    Args:
        metadata (Dict): Metadata dictionary loaded from JSON file.
        md_path (str): Path to the markdown file.
        stem (str): Document stem (file name without extension).
        cur: Database cursor for executing queries.
    Returns:
        None
    """
    query_doc = f"""INSERT INTO "{DB_SCHEMA}".doc (source_file, source_path_md, ocr_engine, extraction_date) 
                    VALUES (%s, %s, %s, %s)
                    RETURNING doc_id"""
    values = (
        stem+".pdf",
        md_path,
        OCR_USED,
        datetime.datetime.now()
    )
    logger.debug(f"Inserting metadata for document {stem} into 'doc' table.")
    cur.execute(query_doc, values)
    doc_id = cur.fetchone()['doc_id']   # <- aquí obtienes el id generado
    logger.debug(f"Inserted document ID: {doc_id} for stem: {stem}")
    query_metadata = f"""INSERT INTO "{DB_SCHEMA}".doc_metadata (doc_id, doi, title, year, journal_name, publisher, genre, doi_url) 
                         VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"""
    metadata_values = (
        doc_id,
        metadata.get("doi"),
        metadata.get("title"),
        metadata.get("year"),
        metadata.get("journal_name"),
        metadata.get("publisher"),
        metadata.get("genre"),
        metadata.get("doi_url")
    )
    logger.debug(f"Inserting metadata for document {stem} into 'doc_metadata' table.")
    cur.execute(query_metadata, metadata_values)
    
    if metadata.get("z_authors"):

        for idx, author in enumerate(metadata.get("z_authors", [])):
            query_author = f"""INSERT INTO "{DB_SCHEMA}".doc_author (doc_id, sequence, given, family, normalized_given, normalized_family)
                            VALUES (%s, %s, %s, %s, %s, %s)"""

            author_given = author.get("given") if author.get("given") else (author.get("raw_author_name").split(" ")[0] if author.get("raw_author_name") else None)
            author_family = author.get("family") if author.get("family") else (author.get("raw_author_name").split(" ")[1] if author.get("raw_author_name") and len(author.get("raw_author_name").split(" ")) > 1 else None)

            author_values = (
                doc_id,
                idx,
                author_given,
                author_family,
                normalize_author_name(author_given),
                normalize_author_name(author_family)
            )
            logger.debug(f"Inserting author {author_given} {author_family} for document {stem} into 'doc_author' table.")
            cur.execute(query_author, author_values)
    return doc_id

def load_bibliography_and_tables_data(biblio_data: Dict, doc_id: uuid.UUID, cur: Cursor[TupleRow]) -> None:
    """Load bibliography and tables data into the database.
    Args:
        biblio_data (Dict): Bibliography and table data loaded from JSON file.
        doc_id (uuid.UUID): Document ID to associate bibliography entries with.
        cur: Database cursor for executing queries.
    Returns:
        None
    """

    logger.debug(f"Loading bibliography and tables for document ID {doc_id}.")
    if biblio_data.get("references"):
        for entry in biblio_data["references"]["references"]:
            query_biblio = f"""INSERT INTO "{DB_SCHEMA}".doc_reference (doc_id, ordinal, raw_text) 
                            VALUES (%s, %s, %s)"""
            biblio_values = (
                doc_id,
                entry['ref_id'],
                entry['text']
            )
            logger.debug(f"Inserting bibliography entry {entry.get('ref_number')} for document ID {doc_id} into 'doc_bibliography' table.")
            cur.execute(query_biblio, biblio_values)
    logger.debug(f"Finished inserting bibliography entries for document ID {doc_id}.")

    logger.debug(f"Loading tables for document ID {doc_id}.")
    if biblio_data.get("tables"):
        for entry in biblio_data["tables"]:
            query_table = f"""INSERT INTO "{DB_SCHEMA}".doc_table (doc_id, table_number, table_title, headers, rows, row_count, column_count) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            table_values = (
                doc_id,
                entry['table_number'],
                entry['table_title'],
                entry['headers'],
                pg_json.Jsonb(entry['rows']),
                entry['row_count'],
                entry['column_count']
            )
            logger.debug(f"Inserting table {entry.get('table_number')} for document ID {doc_id} into 'doc_table' table.")
            cur.execute(query_table, table_values)
    logger.debug(f"Finished inserting tables for document ID {doc_id}.")

def load_abstract(abstract_text: str, doc_id: uuid.UUID, cur: Cursor[TupleRow], model: SentenceTransformer) -> None:
    """Load abstract text into the database.
    Args:
        abstract_text (str): The abstract text.
        doc_id (uuid.UUID): Document ID to associate the abstract with.
        cur: Database cursor for executing queries.
    Returns:
        None
    """
    vlit = None
    query_abstract = f"""INSERT INTO "{DB_SCHEMA}".doc_abstract (doc_id, abstract, has_abstract, embedding) 
                         VALUES (%s, %s, %s, CAST(%s AS vector))"""
    if len(abstract_text.strip()) > 0:
        emb =  model.encode(abstract_text)
        vlit = vector_literal(emb)

    abstract_values = (
        doc_id,
        abstract_text,
        len(abstract_text.strip()) > 0,
        vlit
    )

    logger.debug(f"Inserting abstract for document ID {doc_id} into 'doc_abstract' table.")
    cur.execute(query_abstract, abstract_values)

def load_chunks(chunks_data: Dict, doc_id: uuid.UUID, cur: Cursor[TupleRow], model: SentenceTransformer) -> None:
    """Load document chunks into the database.
    Args:
        chunks_data (Dict): Chunks data loaded from JSON file.
        doc_id (uuid.UUID): Document ID to associate chunks with.
        cur: Database cursor for executing queries.
    Returns:
        None
    """

    query_chunk = f"""INSERT INTO "{DB_SCHEMA}".chunk (doc_id, chunk_id, page_content, token_count, contains_formula, contains_table, contains_code,
                    formulas_json, code_json, tables_json, embedding) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CAST(%s AS vector))"""
    
    for chunk in chunks_data['chunks']:
        chunk_text = chunk['page_content']
        if chunk['metadata'].get('contains_table'):
            for placeholder, table in chunk['metadata']['tables'].items():
                chunk_text = chunk_text.replace(placeholder, table)
        if chunk['metadata'].get('contains_formula'):
            for placeholder, formula in chunk['metadata']['formulas'].items():
                chunk_text = chunk_text.replace(placeholder, formula)
        if chunk['metadata'].get('contains_code'):
            for placeholder, code in chunk['metadata']['code'].items():
                chunk_text = chunk_text.replace(placeholder, code)

        emb = model.encode(chunk_text)
        vlit = vector_literal(emb)

        chunk_values = (
            doc_id,
            chunk['chunk_id'],
            chunk_text,
            chunk['metadata']['token_count'],
            chunk['metadata']['contains_formula'],
            chunk['metadata']['contains_table'],
            chunk['metadata']['contains_code'],
            pg_json.Jsonb(chunk['metadata']['formulas']),
            pg_json.Jsonb(chunk['metadata']['code']),
            pg_json.Jsonb(chunk['metadata']['tables']),
            vlit
        )
        logger.debug(f"Inserting chunk {chunk['chunk_id']} for document ID {doc_id} into 'doc_chunk' table.")
        cur.execute(query_chunk, chunk_values)

def verify_if_doc_exists(cur: Cursor[TupleRow], stem: str) -> bool:
    """Verify if a document already exists in the database based on its source file name.
    Args:
        cur: Database cursor for executing queries.
        stem (str): Document stem (file name without extension).
    Returns:
        bool: True if the document exists, False otherwise.
    """
    query = f"""SELECT COUNT(*) as count FROM "{DB_SCHEMA}".doc WHERE source_file = %s"""
    cur.execute(query, (stem+".pdf",))
    result = cur.fetchone()
    return result['count'] > 0

# Read files safely
def safe_load_json(file_path, description, stem):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"{description} file not found for document {stem}. Skipping.")
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from {description} file for document {stem}. Skipping.")
        except Exception as e:
            logger.error(f"Unexpected error loading {description} for document {stem}: {e}")
        return None

def safe_load_md(file_path, description, stem):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"{description} file not found for document {stem}. Skipping.")
        except Exception as e:
            logger.error(f"Unexpected error loading {description} for document {stem}: {e}")
        return None


def process_one_document(cur: Cursor[TupleRow], model: SentenceTransformer, stem: str) -> None:
    
    # Load documents files
    abstract_file_path = os.path.join(ABSTRACTS_PATH, f"{stem}.md")
    md_file_path = os.path.join(CLEANED_DATA_PATH_MD, f"{stem}.md")
    biblio_file_path = os.path.join(JSON_BIBLIOGRAPHY_AND_TABLES_PATH, f"{stem}.json")
    chunks_file_path = os.path.join(CHUNKING_IMPROVED_OUTPUT_DIR, f"{stem}.json")
    metadata_file_path = os.path.join(PDF_METADATA_PATH, f"{stem}.json")

    if verify_if_doc_exists(cur, stem):
        logger.info(f"Document {stem} already exists in the database. Skipping ingestion.")
        return
    
    metadata = safe_load_json(metadata_file_path, "Metadata", stem)
    if not metadata:
        return
    doc_id = load_pdf_metadata(metadata, md_file_path, stem, cur)

    biblio_data = safe_load_json(biblio_file_path, "Bibliography", stem)
    if biblio_data:
        load_bibliography_and_tables_data(biblio_data, doc_id, cur)

    abstract_data = safe_load_md(abstract_file_path, "Abstract", stem)
    if abstract_data:
        load_abstract(abstract_data, doc_id, cur, model)

    chunks_data = safe_load_json(chunks_file_path, "Chunks", stem)
    if chunks_data:
        load_chunks(chunks_data, doc_id, cur, model)
    else:
        logger.error(f"Chunks data is missing or invalid for document {stem}. Skipping chunk loading.")

def main():
    logger.info("Starting data ingestion process.")
    # Verification of required directories
    for p in [CLEANED_DATA_PATH_MD, JSON_BIBLIOGRAPHY_AND_TABLES_PATH, CHUNKING_IMPROVED_OUTPUT_DIR, PDF_METADATA_PATH, ABSTRACTS_PATH]:
        if not Path(p).is_dir():
            logger.error(f"Required directory not found: {p}")
            raise FileNotFoundError(f"Required directory not found: {p}")
    stems = get_document_stems(ABSTRACTS_PATH, CLEANED_DATA_PATH_MD, JSON_BIBLIOGRAPHY_AND_TABLES_PATH, CHUNKING_IMPROVED_OUTPUT_DIR, PDF_METADATA_PATH)
    if not stems:
        logger.warning("No eligible documents found (MD+Bib/Tablas+Chunks). Check paths.")
        return
    
    logger.info(f"Found {len(stems)} documents with all required files for ingestion.")

    # DB Connection
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            check_extension(cur)
            check_tables(cur)

            # Embeddings model
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
            logger.info(f"Using device for embeddings: {device}")
            model = SentenceTransformer(EMBEDDING_MODEL_NAME, device=device)
            logger.info(f"Loaded embedding model: {EMBEDDING_MODEL_NAME}")

            # Ingestion process
            for i, stem in enumerate(stems, start=1):
                logger.info(f"[{i}/{len(stems)}] Processing document: {stem}")
                try:
                    process_one_document(cur, model, stem)
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    logger.error(f"Error processing {stem}: {e}")

    except Exception as e:
        logger.error(f"Database checks failed: {e}")
        return
    finally:
        cur.close()
        conn.close()
    logger.info("Database connection and checks successful.")


if __name__ == "__main__":
    main()