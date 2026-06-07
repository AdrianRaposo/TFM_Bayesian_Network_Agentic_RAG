# tools/metadata.py
'''
Docstring for 04_AgenticRAG.tools.metadata
This module contains the metadata tool for handling natural language to SQL conversion
and interpreting results in the Agentic RAG system.
It defines a node that processes metadata queries by generating SQL, executing it,
and returning natural language responses.
'''
from typing import Optional
from LoggerSetUp import setup_logger

from services.llm import generate_sql_from_nl, generate_response_from_results
from services.retrieval import connect_db

from config import (
    TABLE_SCHEMAS,
    MAX_RETRIES,
    NOT_FOUND_PHRASE,
    MAX_ROWS,
    LOGS_BASE_PATH,
    LOG_LEVEL 
)

logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='AgenticRAG.log',
    error_log_filename='AgenticRAG_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='w',
    error_mode='w'
)


def metadata_node(state: dict) -> dict:
    """
    Node that processes metadata queries using NL-to-SQL generation and execution.
    
    Expects in state:
      - CorrectedQuery: str
      - relevant_tables: list[str] (from router)
    
    Returns in state:
      - answer: str (response to user)
    
    Args:
        state (dict): Current graph state.
    
    Returns:
        dict: Updated state with answer.
    """

    question = state.get("CorrectedQuery", "")
    relevant_tables = state.get("relevant_tables", [])
    user_language = state.get("user_language", "English")
    
    #Variabke to store results or error messages to be used in response generation
    results = [] 
    
    if not relevant_tables:
        logger.warning("No relevant tables specified for metadata query")
        results = [{"Error": "I could not process your query well because no tables were provided."}]
    else:
        # Filter table schemas to only requested tables
        table_schemas = {
            table: TABLE_SCHEMAS[table] 
            for table in relevant_tables 
            if table in TABLE_SCHEMAS
        }
        
        if not table_schemas:
            logger.warning(f"Requested tables not found in schema: {relevant_tables}")
            results = [{"Error": "I could not process your query well because requested tables don't exist."}]
        else:
            logger.info(f"Processing metadata query with tables: {list(table_schemas.keys())}")
            
            # Step 1: Generate SQL from natural language
            sql_query = generate_sql_from_nl(question, table_schemas, max_retries=MAX_RETRIES)
            
            if sql_query is None:
                logger.warning(f"Failed to generate valid SQL for question: {question}")
                results = [{"Error": "I could not generate a valid query for your request."}]
            
            # Check if it's a decline message (starts with "I cannot" or NOT_FOUND_PHRASE)
            elif sql_query.startswith("I cannot") or sql_query.startswith(NOT_FOUND_PHRASE):
                logger.info(f"SQL generation declined: {sql_query}")
                results = [{"Notice": sql_query}] # Lo guardamos como resultado para el LLM final
            
            else:
                logger.info(f"Generated SQL: {sql_query}")
                # Step 2: Execute SQL and get results
                try:
                    conn = connect_db()
                    with conn.cursor() as cur:
                        cur.execute(sql_query)
                        db_results = cur.fetchall()
                    conn.close()
                    
                    if db_results and not isinstance(db_results[0], dict):
                        db_results = [dict(row) for row in db_results]
                    
                    results = db_results[:MAX_ROWS]
                    logger.info(f"Query executed successfully. Retrieved {len(results)} rows.")
                    
                    if not results:
                        logger.info("Query returned no results")
                        results = [{"Notice": "No results found for your query. Please try a different question."}]
                        
                except Exception as e:
                    error_msg = str(e)
                    logger.error(f"SQL execution failed: {error_msg}")
                    results = [{"Error": f"Database error: {error_msg}"}]
    
    # Step 3: Generate natural language response from results
    try:
        response = generate_response_from_results(question, results, user_language=user_language)
        logger.info("Generated natural language response")
        return {
            **state,
            "answer": response
        }
        
    except Exception as e:
        logger.error(f"Failed to generate response: {str(e)}")
        results_str = "\n".join([str(row) for row in results])
        return {
            **state,
            "answer": f"Query results:\n{results_str}"
        }