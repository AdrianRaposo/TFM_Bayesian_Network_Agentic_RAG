import os
import sys
import json
import pandas as pd
from datasets import Dataset

# Path Routing & Logger Setup
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
agentic_rag_dir = os.path.join(root_dir, "04_AgenticRAG")
sys.path.append(agentic_rag_dir)

from LoggerSetUp import setup_logger
from eval_config import DATASETS_TO_EVALUATE, LOG_LEVEL, LOGS_BASE_PATH, EVALUATION_DATA_PATH,OPENAI_API_MODEL_EMBEDDING, OPENAI_API_MODEL_TEST, OPENAI_API_KEY


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
# 2. Ragas Imports
# ==========================================
from ragas import evaluate
from ragas.metrics.collections import (
    faithfulness,
    answer_relevancy,
    answer_correctness
)
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings


def evaluate_dataset(file_name: str):
    """
    Loads a generated JSON dataset, evaluates it using the Ragas framework with an LLM-as-a-Judge,
    and exports the detailed results (row by row) to a separate JSON file to avoid re-running costs.

    Args:
        file_name (str): The name of the JSON dataset file to evaluate.

    Returns:
        ragas.EvaluationResult | None: The evaluation result object containing the scores,
                                       or None if the file is not found or an error occurs.
    """
    file_path = os.path.join(EVALUATION_DATA_PATH, file_name)
    
    if not os.path.exists(file_path):
        logger.error(f"Dataset file not found: {file_path}")
        return None

    logger.info(f"Starting Ragas evaluation for dataset: {file_name}")

    try:
        # 1. Load the JSON data into a HuggingFace Dataset
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Ragas strictly requires the columns: question, contexts, answer, ground_truth
        df = pd.DataFrame(data)
        hf_dataset = Dataset.from_pandas(df)
        logger.debug(f"Successfully loaded {len(df)} rows into HuggingFace Dataset.")

        # 2. Configure the LLM Judge (OpenAI)
        # Using temperature 0.0 to ensure deterministic and fair evaluations
        judge_llm = ChatOpenAI(
            model=OPENAI_API_MODEL_TEST, 
            api_key=OPENAI_API_KEY,
            temperature=0.0 
        )
        
        # Initialize embeddings model required for metrics like Answer Relevancy
        judge_embeddings = OpenAIEmbeddings(
            model=OPENAI_API_MODEL_EMBEDDING,
            api_key=OPENAI_API_KEY
        )

        # 3. Define the evaluation metrics
        metrics = [
            faithfulness,       # Measures if the answer is derived 100% from the context
            answer_relevancy,   # Measures if the answer directly addresses the query
            answer_correctness  # Measures semantic similarity with the ground_truth
        ]

        # 4. Execute the Evaluation
        logger.info(f"Executing Ragas evaluation metrics for {file_name}. This will consume OpenAI API credits...")
        result = evaluate(
            dataset=hf_dataset,
            metrics=metrics,
            llm=judge_llm,
            embeddings=judge_embeddings,
            raise_exceptions=False # Continue evaluating remaining rows even if one fails
        )
        
        # 5. Export detailed results to JSON to prevent future API costs
        # The output file will have a 'ragas_evaluated_' prefix
        output_name = f"ragas_evaluated_{file_name}"
        output_path = os.path.join(EVALUATION_DATA_PATH, output_name)
        
        # Convert Ragas result to pandas DataFrame to easily export to JSON
        df_results = result.to_pandas()
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            df_results.to_json(
                outfile,
                orient='records',
                indent=4,
                force_ascii=False
            )
        
        logger.info(f"Evaluation completed successfully. Detailed JSON saved to: {output_path}")
        return result

    except Exception as e:
        logger.error(f"Critical failure during Ragas evaluation for {file_name}: {e}")
        return None


def main():
    """
    Main execution pipeline to evaluate all generated datasets, save individual JSON files,
    and log a comparative summary.
    """
    logger.info("Initializing Generative Benchmarking Pipeline (RAGAS).")

    # Define the target datasets generated in the previous phase
    datasets_to_evaluate = DATASETS_TO_EVALUATE

    all_results = {}

    for dataset_file in datasets_to_evaluate:
        result = evaluate_dataset(dataset_file)
        if result:
            all_results[dataset_file] = result

    # Log the final comparative summary
    if all_results:
        logger.info("="*60)
        logger.info(" GENERATIVE EVALUATION SUMMARY (RAGAS) ")
        logger.info("="*60)
        
        for file_name, result in all_results.items():
            model_name = file_name.replace("ragas_dataset_generated_", "").replace(".json", "").upper()
            logger.info(f"Model Evaluated: {model_name}")
            
            # Extract and log the mean score for each evaluated metric
            # Cast result to dict to handle recent Ragas version updates
            for metric_name, score in dict(result).items():
                formatted_metric = metric_name.replace('_', ' ').title()
                logger.info(f"  -> {formatted_metric}: {score:.4f}")
                
        logger.info("="*60)
    else:
        logger.warning("No evaluation results were generated. Please check the dataset files.")

if __name__ == "__main__":
    main()