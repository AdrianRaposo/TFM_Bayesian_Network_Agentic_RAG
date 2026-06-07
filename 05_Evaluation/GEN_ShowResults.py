import os
import itertools
import pandas as pd
import scipy.stats as stats
from typing import List, Dict, Tuple

# Importamos la configuración del proyecto
from eval_config import EVALUATED_DATASETS_OUTPUT

def load_evaluation_datasets(base_path: str, file_names: List[str]) -> Dict[str, pd.DataFrame]:
    """
    Loads JSON evaluation datasets into pandas DataFrames.
    
    Args:
        base_path (str): The directory path where the evaluation files are stored.
        file_names (List[str]): List of JSON file names to be loaded.
        
    Returns:
        Dict[str, pd.DataFrame]: A dictionary mapping the model name to its corresponding DataFrame.
    """
    dataframes = {}
    
    print("\n" + "="*75)
    print(" PHASE 1: DATA LOADING AND ABSOLUTE MEANS COMPUTATION")
    print("="*75)

    for file_name in file_names:
        file_path = os.path.join(base_path, file_name)
        if os.path.exists(file_path):
            df = pd.read_json(file_path)
            # Extract clean model name from file name
            model_name = file_name.replace("ragas_evaluated_ragas_dataset_generated_", "").replace(".json", "").upper()
            dataframes[model_name] = df
            print(f"[INFO] Successfully loaded dataset for model: {model_name}")
        else:
            print(f"[WARNING] Evaluation file not found: {file_name}")
            
    return dataframes

def compute_baseline_means(dataframes: Dict[str, pd.DataFrame], metrics: List[str]) -> None:
    """
    Calculates and prints the absolute mean scores for each model across all specified metrics.
    
    Args:
        dataframes (Dict[str, pd.DataFrame]): Dictionary containing the models' dataframes.
        metrics (List[str]): List of metric columns to evaluate.
    """
    for model_name, df in dataframes.items():
        print(f"\nModel: {model_name}")
        for metric in metrics:
            if metric in df.columns:
                mean_score = df[metric].mean()
                formatted_metric = metric.replace('_', ' ').title()
                print(f"  -> {formatted_metric}: {mean_score:.4f}")

def execute_pairwise_ttest(dataframes: Dict[str, pd.DataFrame], metrics: List[str], alpha: float = 0.05) -> Tuple[Dict, Dict]:
    """
    Executes a Two-Tailed Paired Student's t-test for all combinations of models.
    Determines if the difference in means is statistically significant (p < alpha).
    
    Args:
        dataframes (Dict[str, pd.DataFrame]): Dictionary containing the models' dataframes.
        metrics (List[str]): List of metric columns to evaluate.
        alpha (float): Significance level (default is 0.05).
        
    Returns:
        Tuple[Dict, Dict]: A tuple containing the detailed scoreboard and the total wins per model.
    """
    model_names = list(dataframes.keys())
    
    if len(model_names) < 2:
        raise ValueError("Insufficient models for comparison. At least 2 models are required.")

    # Initialize scoreboards
    scoreboard = {model: {m: 0 for m in metrics} for model in model_names}
    total_wins = {model: 0 for model in model_names}

    print("\n" + "="*75)
    print(f" PHASE 2: PAIRWISE STATISTICAL ANALYSIS (Paired T-Test, α = {alpha})")
    print("="*75)

    # Generate all possible pairwise combinations (e.g., Model A vs Model B)
    model_pairs = list(itertools.combinations(model_names, 2))

    for m1, m2 in model_pairs:
        print(f"\n--- Statistical Comparison: {m1} vs {m2} ---")
        df1 = dataframes[m1]
        df2 = dataframes[m2]
        
        for metric in metrics:
            if metric in df1.columns and metric in df2.columns:
                # Align data strictly by question index to satisfy paired test assumptions
                data_aligned = pd.concat([df1[metric], df2[metric]], axis=1).dropna()
                
                # Execute Paired T-Test
                stat, p_value = stats.ttest_rel(data_aligned.iloc[:, 0], data_aligned.iloc[:, 1])
                
                mean1 = data_aligned.iloc[:, 0].mean()
                mean2 = data_aligned.iloc[:, 1].mean()
                formatted_metric = metric.ljust(22)
                
                # Evaluate statistical significance
                if p_value < alpha:
                    winner = m1 if mean1 > mean2 else m2
                    print(f"  [{formatted_metric}] Significant Difference (p={p_value:.4f}) -> Winner: {winner}")
                    scoreboard[winner][metric] += 1
                    total_wins[winner] += 1
                else:
                    print(f"  [{formatted_metric}] No Significant Difference (p={p_value:.4f}) -> H0 Retained")

    return scoreboard, total_wins

def generate_leaderboards(scoreboard: Dict, total_wins: Dict) -> None:
    """
    Transforms the scoreboard dictionary into pandas DataFrames and prints the final
    absolute and pragmatic rankings.
    
    Args:
        scoreboard (Dict): Detailed wins per metric.
        total_wins (Dict): Total accumulated wins per model.
    """
    # Convert dictionary to DataFrame for better visualization
    df_scores = pd.DataFrame(scoreboard).T
    df_scores['TOTAL_WINS'] = pd.Series(total_wins)

    print("\n" + "="*75)
    print(" PHASE 3: ABSOLUTE LEADERBOARD (All Metrics Considered)")
    print("="*75)

    # Absolute Ranking
    df_scores_absolute = df_scores.sort_values(by='TOTAL_WINS', ascending=False)
    print(df_scores_absolute.to_string())
    print(f"\n>> OPTIMAL MODEL (Absolute): {df_scores_absolute.index[0]}")

    print("\n" + "="*75)
    print(" PHASE 4: PRAGMATIC LEADERBOARD (Excluding Answer Correctness)")
    print("="*75)

    # Pragmatic Ranking (Filtering out 'answer_correctness')
    df_scores_pragmatic = df_scores[['faithfulness', 'answer_relevancy']].copy()
    df_scores_pragmatic['PRAGMATIC_WINS'] = df_scores_pragmatic.sum(axis=1)
    df_scores_pragmatic = df_scores_pragmatic.sort_values(by='PRAGMATIC_WINS', ascending=False)
    
    print(df_scores_pragmatic.to_string())
    print(f"\n>> OPTIMAL RAG MODEL (High Faithfulness & Relevancy): {df_scores_pragmatic.index[0]}")
    print("="*75 + "\n")

def main():
    """
    Main execution pipeline for the Statistical Generative Benchmarking.
    """
    # Define paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    eval_dir = os.path.abspath(os.path.join(current_dir, "..", "00_Data", "EVALUATION"))
    
    # Define metrics to evaluate
    target_metrics = ['faithfulness', 'answer_relevancy', 'answer_correctness']
    
    # Execute Pipeline
    try:
        dataframes_dict = load_evaluation_datasets(base_path=eval_dir, file_names=EVALUATED_DATASETS_OUTPUT)
        
        if len(dataframes_dict) < 2:
            print("\n[ERROR] Execution halted: At least two datasets are required to perform the Paired T-Test.")
            return

        compute_baseline_means(dataframes=dataframes_dict, metrics=target_metrics)
        
        scoreboard, total_wins = execute_pairwise_ttest(
            dataframes=dataframes_dict, 
            metrics=target_metrics, 
            alpha=0.05
        )
        
        generate_leaderboards(scoreboard=scoreboard, total_wins=total_wins)
        
    except Exception as e:
        print(f"\n[CRITICAL ERROR] The evaluation pipeline failed: {str(e)}")

if __name__ == "__main__":
    main()