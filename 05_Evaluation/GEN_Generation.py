import os
import sys
import json
import time
import random
from openai import max_retries
import pandas as pd

# ==========================================
# 1. Path Routing (Fixing the import issue)
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
agentic_rag_dir = os.path.join(root_dir, "04_AgenticRAG")
services_dir = os.path.join(agentic_rag_dir, "services") 

sys.path.append(agentic_rag_dir)
sys.path.append(services_dir)

# Now we can import your RAG modules safely
from LoggerSetUp import setup_logger
from eval_config import (
    LOG_LEVEL,
    LOGS_BASE_PATH,
    EVALUATION_DATA_PATH
)

from services.retrieval import retrieval_llm_context
from services.llm import get_rag_chain
from config import MAX_RESULTS_RETRIEVED, LLM_PROVIDER, OLLAMA_MODEL, OLLAMA_MODEL_NAME

# ==========================================
# 2. Logger Setup
# ==========================================
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

# ==========================================
# 3. Core Functions
# ==========================================
def generate_rag_response_and_context(question: str, rag_chain, max_retries: int = 4) -> tuple[str, str]:
    """
    Retrieves the context for a given question and generates a response using the configured RAG chain.

    Args:
        question (str): The user query to process.
        rag_chain (Runnable): The LangChain runnable object configured to generate the RAG answer.
        max_retries (int): The maximum number of retry attempts for API calls.

    Returns:
        tuple[str, str]: A tuple containing:
            - The generated answer (str).
            - The retrieved context used to generate the answer (str).
    """
    # 1. Retrieve context from the Vector Database
    context_str = retrieval_llm_context(
        query=question, 
        keywords=[], 
        top_k=MAX_RESULTS_RETRIEVED
    )
    
    # 2. Generate answer using the LLM
    for attempt in range(max_retries):
        try:
            response = rag_chain.invoke({
                "question": question,
                "context": context_str
            })
            return response, context_str
            
        except Exception as e:
            error_msg = str(e)
            
            # Check if it's a quota error (429 / RESOURCE_EXHAUSTED)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "Quota" in error_msg:
                if attempt < max_retries - 1:
                    # Calculate wait time: 60s, then 120s... + some randomness
                    sleep_time = (60 * (attempt + 1)) + random.uniform(1, 5)
                    logger.warning(f"API Rate Limit reached. Pausing script for {sleep_time:.0f} seconds before retry {attempt + 1}...")
                    print(f"   ⏳ Quota limit detected. Pausing for {sleep_time:.0f} seconds...")
                    time.sleep(sleep_time)
                    continue  # Try again
                
            # If it's another type of error or we run out of retries, raise it
            logger.error(f"Definitive failure after {max_retries} attempts: {error_msg}")
            raise e


def main():
    """
    Main execution function to load the ground truth QA dataset, generate RAG responses 
    using the configured LLM provider, and export a Ragas-compatible JSON dataset.
    """
    logger.info(f"Starting Generative Evaluation Pipeline using provider: {LLM_PROVIDER.upper()}")
    
    input_path = os.path.join(EVALUATION_DATA_PATH, "BN_100_QA.json") 
    if LLM_PROVIDER != "ollama":
        output_path = os.path.join(EVALUATION_DATA_PATH, f"ragas_dataset_generated_{LLM_PROVIDER}.json")
    else: 
        output_path = os.path.join(EVALUATION_DATA_PATH, f"ragas_dataset_generated_ollama_{OLLAMA_MODEL_NAME}.json")
    try:
        # 1. Load the Evaluation Dataset
        if not os.path.exists(input_path):
            logger.error(f"Input file not found: {input_path}")
            return

        with open(input_path, 'r', encoding='utf-8') as f:
            qa_data = json.load(f)

        logger.info(f"Successfully loaded {len(qa_data)} questions from Ground Truth.")

        # 2. Initialize the RAG Chain
        rag_chain = get_rag_chain()
        ragas_dataset = []

        # 3. Process Each Query (with Rate Limiting)
        for idx, item in enumerate(qa_data):
            question = item.get("question", "")
            # Assuming Ground Truth JSON has an 'answer' key representing the ideal response
            ground_truth = item.get("answer", "") 
            
            logger.info(f"Processing Query {idx + 1}/{len(qa_data)}: {question[:50]}...")
            
            try:
                # Generate RAG output
                generated_answer, retrieved_context = generate_rag_response_and_context(
                    question=question, 
                    rag_chain=rag_chain
                )
                
                # Append in the exact format required by the Ragas framework
                ragas_dataset.append({
                    "question": question,
                    "answer": generated_answer,
                    "contexts": [retrieved_context], # Ragas expects a list of context strings
                    "ground_truth": ground_truth
                })
                
                if (idx + 1) % 10 == 0:
                    print(f"  -> Generated {idx + 1}/{len(qa_data)} responses...")

            except Exception as e:
                logger.warning(f"Failed to generate RAG response for query '{question[:30]}': {e}")
                
                # Append empty strings to maintain dataset alignment, avoiding catastrophic failure
                ragas_dataset.append({
                    "question": question,
                    "answer": "ERROR_GENERATING_RESPONSE",
                    "contexts": ["ERROR_RETRIEVING_CONTEXT"],
                    "ground_truth": ground_truth
                })
            
            # Rate limiting for Free Tier APIs (e.g., Gemini 15 RPM limit -> 4 seconds per request)
            if idx < len(qa_data) - 1:
                time.sleep(4)
                
        # 4. Save the Final Ragas-Compatible Dataset
        df_ragas = pd.DataFrame(ragas_dataset)
        
        with open(output_path, 'w', encoding='utf-8') as file:
            df_ragas.to_json(
                file, 
                orient='records', 
                indent=4, 
                force_ascii=False
            )
            
        logger.info(f"Successfully created Ragas evaluation dataset: {output_path}")
        
        # Display a sample to verify
        print("\\n--- Sample Generated Evaluation Entry ---")
        sample = df_ragas.iloc[0]
        print(f"Q: {sample['question']}")
        print(f"RAG Answer (Snippet): {sample['answer'][:150]}...")

    except Exception as e:
        logger.error(f"Critical error in Generative Evaluation Pipeline: {e}")

if __name__ == "__main__":
    main()