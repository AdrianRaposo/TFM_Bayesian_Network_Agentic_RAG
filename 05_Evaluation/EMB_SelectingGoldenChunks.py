import pandas as pd
import psycopg
import json
import os
import time

from psycopg.rows import dict_row
from LoggerSetUp import setup_logger
from openai import OpenAI  # <-- Make sure to run: pip install openai

from eval_config import(
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_SCHEMA,
    OPENAI_API_KEY_EVALUATION,
    OPENAI_API_MODEL_EMBEDDING_TEST,
    DB_CHUNKS_TABLE as CHUNK_TABLE,
    GET_STRATIFIED_CHUNKS_QUERY_RAG,
    EVALUATION_DATA_PATH,
    LOG_LEVEL,
    LOGS_BASE_PATH
)

logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='AgenticRAG.log',
    error_log_filename='AgenticRAG_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='a',
    error_mode='a'
)

# Initialize LLM Client 
llm_client = OpenAI(api_key=OPENAI_API_KEY_EVALUATION)

def connect_db() -> psycopg.Connection:
    """
     Establish a connection to the PostgreSQL database.
     Returns:
        psycopg.Connection: A connection object to interact with the database.
    """
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        client_encoding='utf8',
        row_factory=dict_row
    )

def extract_sample_chunks(conn: psycopg.Connection) -> list[dict]:
    """
    Extracts a stratified sample of chunks from the database (Oversampled to 3 per doc).
    Args:
        conn (psycopg.Connection): An active database connection.
        Returns:
        list[dict]: A list of dictionaries, each representing a chunk with its metadata.
    """
    sql = GET_STRATIFIED_CHUNKS_QUERY_RAG.format(
        schema=DB_SCHEMA,
        table=CHUNK_TABLE
    )

    with conn.cursor() as cur:
        logger.info("Executing SQL query to extract stratified sample chunks for RAG evaluation.")
        cur.execute(sql)
        return cur.fetchall()

def evaluate_chunk_quality(chunk_text: str) -> dict:
    """Uses an LLM to judge if a chunk is substantive academic content or noise."""
    prompt = f"""You are a highly strict data quality evaluator for an academic RAG system. 
        Your job is to filter out "low-information" or "context-dependent" text chunks extracted via OCR.

        Classify the following text into one of two categories:

        1. "NOISE": Select this if the text is primarily:
        - A list of references or a bibliography (e.g., numbered lists containing authors, years, DOIs, journal names).
        - Copyright notices, publisher metadata, author affiliations, or contact info.
        - Isolated figure captions or table legends.
        - Text that heavily relies on pointing to a Table, Figure, or Equation that is not fully explained in the text itself (e.g., "From this table...", "Table 3 shows...", "As seen in Figure 4...").
        - Incoherent OCR artifacts, heavily fragmented sentences, or raw lists of numbers.

        2. "SUBSTANTIVE": Select this ONLY if the text is a self-contained, meaningful academic paragraph. It must contain actual knowledge, methodology, theory, or results that a researcher could understand and ask a question about *without* needing to look at a chart or read the rest of the paper.

        Return ONLY a valid JSON object with two keys: "classification" (either "NOISE" or "SUBSTANTIVE") and "reason" (a 1-sentence explanation).

        Text to classify:
        {chunk_text}
    """
    
    response = llm_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.0 # Keep it deterministic
    )
    
    return json.loads(response.choices[0].message.content)

def filter_substantive_chunks(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Iterates through oversampled documents and uses the LLM to select the best chunk.
    Args:
        df_raw (pd.DataFrame): DataFrame containing the oversampled chunks with metadata.
    Returns:
        pd.DataFrame: A filtered DataFrame with one "best" chunk per document, classified as SUBSTANTIVE.
    """
    final_chunks = []
    grouped = df_raw.groupby('doc_id')
    
    total_docs = len(grouped)
    logger.info(f"Starting LLM Quality Gate for {total_docs} unique documents...")
    
    for i, (doc_id, group) in enumerate(grouped, 1):
        if i % 50 == 0:
            logger.info(f"Processed {i}/{total_docs} documents...")
            
        # Sort by token count descending (longest chunks first as a heuristic)
        group = group.sort_values(by='token_count', ascending=False)
        selected_chunk = None
        
        for _, row in group.iterrows():
            try:
                evaluation = evaluate_chunk_quality(row['page_content'])
                
                if evaluation.get('classification') == 'SUBSTANTIVE':
                    selected_chunk = row.to_dict()
                    selected_chunk['llm_quality_reason'] = evaluation.get('reason')
                    break # Success! Stop evaluating chunks for this document
                
            except Exception as e:
                logger.warning(f"LLM eval failed for chunk {row.get('chunk_pk')}: {e}")
                time.sleep(1) # Backoff if API rate limits
                
        # Fallback Strategy: If all candidates are NOISE, pick the longest one
        if selected_chunk is None:
            selected_chunk = group.iloc[0].to_dict()
            selected_chunk['llm_quality_reason'] = "FALLBACK: All candidates evaluated as NOISE."
            logger.debug(f"Document {doc_id} fell back to longest chunk.")
            
        final_chunks.append(selected_chunk)
        
    return pd.DataFrame(final_chunks)

def main():
    try:
        conn = connect_db()
        with conn:
            # 1. Extract the oversampled chunks (Expected: ~1152 chunks)
            chunks = extract_sample_chunks(conn)
            df_raw = pd.DataFrame(chunks)
            
            if df_raw.empty:
                logger.error("The extracted chunk list is empty. Check database connection and table content.")
                return
            
            logger.info(f"Successfully extracted {len(df_raw)} raw candidate chunks from database.")

            # 2. Run the LLM Quality Gate to filter down to 1 Substantive chunk per doc
            df_filtered = filter_substantive_chunks(df_raw)

            # 3. Validation Logs (proving the stratification and filtering worked)
            unique_docs = df_filtered['doc_id'].nunique()
            logger.info(f"FINAL - Unique documents represented: {unique_docs} (Expected: 384)")
            
            quartile_counts = df_filtered['quartile'].value_counts().to_dict()
            logger.info(f"FINAL - Distribution across Quartiles: {quartile_counts} (Expected: ~96 per quartile)")
            
            # 4. Save the "Gold Standard" benchmark dataset
            # Make sure EVALUATION_DATA_PATH exists
            os.makedirs(EVALUATION_DATA_PATH, exist_ok=True)
            output_path = os.path.join(EVALUATION_DATA_PATH, "gold_standard_eval_chunks_384.json")

            with open(output_path, 'w', encoding='utf-8') as file:
                df_filtered.to_json(
                    file, 
                    orient='records', 
                    indent=4, 
                    force_ascii=False
                )
            logger.info(f"Frozen benchmark dataset safely exported to: {output_path}")

    except Exception as e:
        logger.error(f"An error occurred during chunk extraction: {e}", exc_info=True)

if __name__ == "__main__":
    main()