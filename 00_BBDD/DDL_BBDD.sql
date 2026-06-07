-- =========================
-- Extensions
-- =========================
CREATE EXTENSION IF NOT EXISTS unaccent; -- Enables removal of accents from text
CREATE EXTENSION IF NOT EXISTS vector; -- Provides vector data type for embeddings
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- Enables UUID generation
CREATE EXTENSION IF NOT EXISTS pg_trgm; -- Provides trigram similarity functions and indexes

-- =========================
-- Schema
-- =========================
CREATE SCHEMA IF NOT EXISTS "BNAR_Chunk_Simp_v1" ; -- Create schema if it doesn't exist

-- =========================
-- Table: doc
-- =========================
CREATE TABLE IF NOT EXISTS doc (
    doc_id           uuid PRIMARY KEY DEFAULT uuid_generate_v4(), -- Unique document ID
    source_file      text NOT NULL, -- Name of the source file
    source_path_md   text, -- Path to the source file (Markdown)
    ocr_engine       text, -- OCR engine used for text extraction
    extraction_date  timestamptz -- Date and time of extraction
);
CREATE UNIQUE INDEX IF NOT EXISTS doc_source_file_uq ON doc (source_file); -- Ensure unique source file names



-- =========================
-- Table: chunk
-- =========================
CREATE TABLE IF NOT EXISTS chunk (
    chunk_pk         uuid PRIMARY KEY DEFAULT uuid_generate_v4(), -- Unique chunk ID
    doc_id           uuid NOT NULL REFERENCES doc(doc_id) ON DELETE CASCADE, -- Associated document ID
    chunk_id         int  NOT NULL, -- Chunk number within the document
    page_content     text NOT NULL, -- Content of the chunk
    token_count      int, -- Number of tokens in the chunk
    contains_formula bool, -- Indicates if the chunk contains formulas
    contains_code    bool, -- Indicates if the chunk contains code
    contains_table   bool, -- Indicates if the chunk contains tables
    formulas_json    jsonb, -- JSON representation of formulas
    code_json        jsonb, -- JSON representation of code
    tables_json      jsonb, -- JSON representation of tables
    content_ft       tsvector, -- Full-text search vector
    embedding        vector -- Embedding vector for the chunk
);

CREATE UNIQUE INDEX IF NOT EXISTS chunk_doc_chunkid_uq ON chunk (doc_id, chunk_id); -- Ensure unique chunk IDs per document
CREATE INDEX IF NOT EXISTS chunk_doc_id_idx ON chunk (doc_id); -- Index for document ID
CREATE INDEX IF NOT EXISTS chunk_ft_idx ON chunk USING gin (content_ft); -- Full-text search index
CREATE INDEX IF NOT EXISTS chunk_embedding_ivfflat_idx
    ON chunk USING ivfflat (embedding vector_cosine_ops) WITH (lists = 200); -- Index for vector similarity search

-- =========================
-- Trigger Function for Full-Text Search
-- =========================
CREATE OR REPLACE FUNCTION chunk_ft_refresh()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.content_ft := to_tsvector(
            'english',
            unaccent(coalesce(NEW.page_content, '')) -- Generate full-text search vector
    );
    RETURN NEW;
END;
$$;

-- Create the trigger
CREATE TRIGGER trg_chunk_ft_refresh
BEFORE INSERT OR UPDATE OF page_content
ON chunk
FOR EACH ROW
EXECUTE FUNCTION chunk_ft_refresh(); -- Refresh full-text search vector on content change

-- =========================
-- Table: doc_abstract
-- =========================
CREATE TABLE IF NOT EXISTS doc_abstract (
    doc_id    uuid PRIMARY KEY REFERENCES doc(doc_id) ON DELETE CASCADE, -- Associated document ID
    abstract  text NOT NULL, -- Document abstract
    has_abstract bool NOT NULL DEFAULT true, -- Indicates if the document has an abstract
    embedding vector -- Embedding vector for the abstract
);

-- =========================
-- Table: doc_author
-- =========================
CREATE TABLE IF NOT EXISTS doc_author (
    doc_id            uuid NOT NULL REFERENCES doc(doc_id), -- Associated document ID
    "sequence"        int  NOT NULL, -- Author sequence number
    given             text, -- Author's given name
    "family"          text, -- Author's family name
    normalized_given  text, -- Normalized given name
    normalized_family text, -- Normalized family name
    PRIMARY KEY (doc_id, "sequence") -- Composite primary key
);

-- =========================
-- Table: doc_metadata
-- =========================
CREATE TABLE IF NOT EXISTS doc_metadata (
    doc_id       uuid PRIMARY KEY REFERENCES doc(doc_id), -- Associated document ID
    doi          varchar(255), -- Document DOI
    title        text, -- Document title
    "year"       int, -- Publication year
    journal_name text, -- Journal name
    publisher    text, -- Publisher name
    genre        varchar(50), -- Document genre
    doi_url      text -- DOI URL
);

-- =========================
-- Table: doc_reference
-- =========================
CREATE TABLE IF NOT EXISTS doc_reference (
    ref_id     uuid PRIMARY KEY DEFAULT uuid_generate_v4(), -- Unique reference ID
    doc_id     uuid NOT NULL REFERENCES doc(doc_id) ON DELETE CASCADE, -- Associated document ID
    ordinal    int, -- Reference ordinal number
    raw_text   text NOT NULL, -- Raw reference text
    block_json jsonb -- JSON representation of the reference block
);
CREATE INDEX IF NOT EXISTS doc_reference_doc_id_idx ON doc_reference (doc_id); -- Index for document ID

-- =========================
-- Table: doc_table
-- =========================
CREATE TABLE IF NOT EXISTS doc_table (
    table_id     uuid PRIMARY KEY DEFAULT uuid_generate_v4(), -- Unique table ID
    doc_id       uuid NOT NULL REFERENCES doc(doc_id) ON DELETE CASCADE, -- Associated document ID
    table_number text, -- Table number
    table_title  text, -- Table title
    headers      text[] NOT NULL, -- Table headers
    "rows"       jsonb  NOT NULL, -- Table rows in JSON format
    row_count    int, -- Number of rows
    column_count int -- Number of columns
);
CREATE INDEX IF NOT EXISTS doc_table_doc_id_idx ON doc_table (doc_id); -- Index for document ID


