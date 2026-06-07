import pandas as pd
import json
import os
import time
from openai import OpenAI
from LoggerSetUp import setup_logger

from eval_config import (
    OPENAI_API_KEY_EVALUATION,
    OPENAI_API_MODEL_EMBEDDING_TEST,
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

# Initialize LLM Client - Recommended to use a smarter model like gpt-4o here
llm_client = OpenAI(api_key=OPENAI_API_KEY_EVALUATION) 

def generate_synthetic_query(chunk_text: str) -> str:
    """
    Uses an LLM to generate a realistic user query based on the chunk content.

    Args:
        chunk_text (str): The text content of the chunk for which to generate a query.
    Returns:
        str: A synthetic user query that could be realistically asked by a researcher.
    
    """
    
    prompt = f"""You are an expert researcher creating an evaluation benchmark for an academic RAG (Retrieval-Augmented Generation) system.

            I will provide you with a text chunk extracted from an academic paper. Your task is to generate **one** highly realistic user query that can be answered *using only the information in this specific chunk*.

            **Rules for the Query:**
            1. It must sound like a real question a researcher would type into a search bar (e.g., "What is the formula for calculating...", "How did the authors evaluate...", "What are the limitations of...").
            2. It must be highly specific to the concepts, variables, or methodology mentioned in the text.
            3. DO NOT use generic phrases like "In this text...", "According to the chunk...", or "Based on the excerpt...". The query must stand alone.
            4. Ensure the query cannot easily be answered by a different paper (use specific terminology or constraints from the chunk).

            Return ONLY a valid JSON object with the key "query" containing your generated question.

            Chunk Text:
            {chunk_text}
    """
    
    response = llm_client.chat.completions.create(
        model=OPENAI_API_MODEL_EMBEDDING_TEST, # Using a smarter model for question generation
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.4 # Slight temperature for natural phrasing, but still grounded
    )
    
    result = json.loads(response.choices[0].message.content)
    return result.get("query", "")

def main():
    input_path = os.path.join(EVALUATION_DATA_PATH, "gold_standard_eval_chunks_384.json")
    output_path = os.path.join(EVALUATION_DATA_PATH, "evaluation_benchmark_final.json")
    
    try:
        # 1. Load the frozen chunks
        logger.info(f"Loading gold standard chunks from {input_path}")
        with open(input_path, 'r', encoding='utf-8') as f:
            chunks = json.load(f)
            
        df_chunks = pd.DataFrame(chunks)
        total_chunks = len(df_chunks)
        
        logger.info(f"Starting synthetic query generation for {total_chunks} chunks...")
        
        benchmark_dataset = []
        
        # 2. Iterate and generate queries
        for idx, row in df_chunks.iterrows():
            if (idx + 1) % 50 == 0:
                logger.info(f"Generated queries for {idx + 1}/{total_chunks} chunks...")
                
            chunk_dict = row.to_dict()
            
            # Generate a unique query ID (e.g., q_001, q_002)
            query_id = f"q_{str(idx + 1).zfill(3)}"
            chunk_dict['query_id'] = query_id
            
            try:
                # Call the LLM
                generated_query = generate_synthetic_query(chunk_dict['page_content'])
                chunk_dict['generated_query'] = generated_query
            except Exception as e:
                logger.warning(f"Failed to generate query for chunk {chunk_dict.get('chunk_pk')}: {e}")
                chunk_dict['generated_query'] = "ERROR_GENERATING_QUERY"
                time.sleep(2) # Backoff
                
            benchmark_dataset.append(chunk_dict)
            
        # 3. Save the Final Benchmark Dataset
        df_benchmark = pd.DataFrame(benchmark_dataset)
        
        with open(output_path, 'w', encoding='utf-8') as file:
            df_benchmark.to_json(
                file, 
                orient='records', 
                indent=4, 
                force_ascii=False
            )
            
        logger.info(f"Successfully created final evaluation benchmark: {output_path}")
        
        # Display a sample to verify
        print("\n--- Sample Generated Query ---")
        sample = df_benchmark.iloc[0]
        print(f"Q: {sample['generated_query']}")
        print(f"Target Chunk PK: {sample['chunk_pk']}")

    except Exception as e:
        logger.error(f"An error occurred during query generation: {e}", exc_info=True)

if __name__ == "__main__":
    main()