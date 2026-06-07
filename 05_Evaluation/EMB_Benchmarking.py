import sys
import os
import json
import psycopg
import numpy as np
from typing import List, Dict, Any, Tuple

from psycopg.rows import dict_row
from ranx import Qrels, Run, compare, evaluate

# Libraries for advanced data visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. Path Routing & Configuration
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
agentic_rag_dir = os.path.join(root_dir, "04_AgenticRAG")
services_dir = os.path.join(agentic_rag_dir, "services") 

sys.path.append(agentic_rag_dir)
sys.path.append(services_dir)

# Import RAG modules and configurations
import retrieval # type: ignore
from eval_config import (
    DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, 
    DB_SCHEMA,
    DB_CHUNKS_TABLE, EVALUATION_DATA_PATH,
    DB_SCHEMA_TEST_1, TEST_EMBEDDING_MODEL_NAME_1,
    DB_SCHEMA_TEST_2, TEST_EMBEDDING_MODEL_NAME_2,
    DB_SCHEMA_TEST_3, TEST_EMBEDDING_MODEL_NAME_3
)

# ==========================================
# 2. Database & Qrels (Ground Truth) Logic
# ==========================================
def connect_to_db(schema_name: str) -> psycopg.Connection:
    """
    Establishes a connection to the PostgreSQL database and sets the search path 
    to strictly include the target schema, base schema, and public (for pgvector).
    
    Args:
        schema_name (str): The specific target schema for the evaluation run.
        
    Returns:
        psycopg.Connection: Configured database connection object.
    """
    conn = psycopg.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
        user=DB_USER, password=DB_PASSWORD,
        row_factory=dict_row
    )
    # Include 'public' to ensure pgvector operators are accessible
    conn.execute(f"""SET search_path TO "{schema_name}", "{DB_SCHEMA}", public""")
    
    return conn

def get_sibling_chunks(conn: psycopg.Connection, doc_id: str) -> List[str]:
    """
    Retrieves all chunk primary keys (PKs) belonging to a specific document 
    to establish Document-Level Graded Relevance.
    
    Args:
        conn (psycopg.Connection): Active database connection.
        doc_id (str): The parent document's unique identifier.
        
    Returns:
        List[str]: A list of sibling chunk primary keys.
    """
    query = f"""SELECT chunk_pk FROM "{DB_SCHEMA}"."{DB_CHUNKS_TABLE}" WHERE doc_id = %s"""
    with conn.cursor() as cur:
        cur.execute(query, (doc_id,))
        return [str(row['chunk_pk']) for row in cur.fetchall()]

def build_graded_qrels(benchmark_data: List[Dict[str, Any]], conn: psycopg.Connection) -> Qrels:
    """
    Constructs the Ground Truth (Qrels) object using a graded relevance approach:
    - 2 Points: Exact target chunk match.
    - 1 Point: Sibling chunk match (same parent document).
    
    Args:
        benchmark_data (List[Dict]): The parsed JSON benchmark dataset.
        conn (psycopg.Connection): Active database connection.
        
    Returns:
        Qrels: A ranx-compatible Qrels object containing the relevance judgements.
    """
    qrels_dict = {}
    print("\n[PROCESS] Building Graded Qrels (Ground Truth Matrix)...")
    
    for item in benchmark_data:
        query_id = item['query_id']
        target_chunk_pk = str(item['chunk_pk'])
        doc_id = str(item['doc_id'])
        
        sibling_chunks = get_sibling_chunks(conn, doc_id)
        
        query_qrels = {}
        for chunk in sibling_chunks:
            if chunk == target_chunk_pk:
                query_qrels[chunk] = 2  # Optimal Context
            else:
                query_qrels[chunk] = 1  # Thematic/Sibling Context
                
        qrels_dict[query_id] = query_qrels
        
    return Qrels(qrels_dict)

# ==========================================
# 3. Model Evaluation Logic
# ==========================================
def get_uuid_translator(conn: psycopg.Connection, base_schema: str, target_schema: str) -> Dict[str, str]:
    """
    Maps UUIDs from the target schema back to the base schema using exact MD5 hashes 
    of the text content, ensuring cross-schema evaluation consistency.
    """
    if base_schema == target_schema:
        return {} 
        
    print(f"  -> Building cross-schema UUID translator mapping for [{target_schema}]...")
    
    base_hashes = {}
    with conn.cursor() as cur:
        cur.execute(f'SELECT chunk_pk, md5(page_content) as hash FROM "{base_schema}"."{DB_CHUNKS_TABLE}"')
        for r in cur.fetchall():
            base_hashes[r['hash']] = str(r['chunk_pk'])
            
    translator = {}
    with conn.cursor() as cur:
        cur.execute(f'SELECT chunk_pk, md5(page_content) as hash FROM "{target_schema}"."{DB_CHUNKS_TABLE}"')
        for r in cur.fetchall():
            if r['hash'] in base_hashes:
                translator[str(r['chunk_pk'])] = base_hashes[r['hash']]
                
    return translator

def build_model_run(schema_name: str, model_name: str, benchmark_data: List[Dict[str, Any]], base_schema: str) -> Run:
    """
    Executes the hybrid retrieval pipeline for a designated embedding model and builds 
    a ranking Run object for evaluation.
    """
    run_dict = {}
    print(f"\n[EVALUATING] Model: {model_name} | Target Schema: {schema_name}")
    
    retrieval.DB_SCHEMA = schema_name
    retrieval.EMBEDDING_MODEL_NAME = model_name
    retrieval.get_embedding_model.cache_clear()

    conn = connect_to_db(schema_name)
    uuid_translator = get_uuid_translator(conn, base_schema, schema_name)
    
    try:
        total_queries = len(benchmark_data)
        for idx, item in enumerate(benchmark_data):
            query_id = item['query_id']
            user_question = item['generated_query']
            
            if (idx + 1) % 50 == 0:
                print(f"  -> Processed {idx + 1}/{total_queries} queries...")
            
            # Retrieve Top 20 context chunks
            top_results = retrieval.hybrid_retrieval_pipeline(
                query=user_question, 
                conn=conn, 
                keywords=[], 
                top_k=20, 
                model_name=model_name 
            )
            
            query_results = {}
            for rank, result in enumerate(top_results):
                score = float(result.get('final_score', 20 - rank))
                raw_pk = str(result['chunk_pk'])

                # Translate UUID to base baseline UUID if schemas differ
                translated_pk = uuid_translator.get(raw_pk, raw_pk) 
                query_results[translated_pk] = score
                
            run_dict[query_id] = query_results
            
    finally:
        conn.close()
        
    return Run(run_dict, name=model_name)

# ==========================================
# 4. Statistical Tests & Visualization
# ==========================================

def fisher_randomization_test(scores_a: List[float], scores_b: List[float], n_permutations: int = 1000, seed: int = 42) -> float:
    """
    Computes the exact p-value using Fisher's Randomization Test.
    Strict mathematical implementation recommended by Smucker et al. (2007) for Information Retrieval metrics.
    """
    arr_a = np.array(scores_a)
    arr_b = np.array(scores_b)
    diffs = arr_a - arr_b
    
    # Absolute observed mean difference
    obs_diff = np.abs(np.mean(diffs))
    
    # Identical performance yields p-value 1.0
    if obs_diff == 0:
        return 1.0
        
    np.random.seed(seed)
    
    # Generate random sign flips (+1 or -1)
    signs = np.random.choice([1, -1], size=(n_permutations, len(diffs)))
    permuted_diffs = signs * diffs
    permuted_mean_diffs = np.abs(np.mean(permuted_diffs, axis=1))
    
    # Calculate proportion of permutations exceeding observed difference
    p_value = np.sum(permuted_mean_diffs >= obs_diff) / n_permutations
    
    return float(p_value)

def print_win_tie_loss_matrix(qrels: Qrels, runs: List[Run], metric: str = "mrr@10") -> None:
    """
    Computes and prints the Pairwise Win/Tie/Loss matrix alongside the exact Fisher's p-value.
    """
    print(f"\n" + "="*95)
    print(f" 🏆 WIN / TIE / LOSS & EXACT P-VALUE MATRIX ({metric.upper()}) ")
    print("="*95)
    print(f"{'Comparison (A vs B)':<48} | {'Wins':<5} | {'Ties':<5} | {'Losses':<6} | {'p-value'}")
    print("-" * 95)

    # 1. Extract query-level scores per model
    query_scores = {}
    for run in runs:
        model_name = run.name
        query_scores[model_name] = {}
        for q_id in qrels.qrels.keys():
            if q_id in run.run:
                mini_run = Run({q_id: run.run[q_id]})
                mini_qrels = Qrels({q_id: qrels.qrels[q_id]})
                score = evaluate(mini_qrels, mini_run, metrics=metric)
                query_scores[model_name][q_id] = score
            else:
                query_scores[model_name][q_id] = 0.0

    model_names = [r.name for r in runs]

    # 2. Execute pairwise evaluation
    for i in range(len(model_names)):
        for j in range(i + 1, len(model_names)):
            model_a = model_names[i]
            model_b = model_names[j]
            
            wins, ties, losses = 0, 0, 0
            scores_a_list = []
            scores_b_list = []
            
            for q_id in qrels.qrels.keys():
                score_a = query_scores[model_a][q_id]
                score_b = query_scores[model_b][q_id]
                
                scores_a_list.append(score_a)
                scores_b_list.append(score_b)
                
                if score_a > score_b:
                    wins += 1
                elif score_a < score_b:
                    losses += 1
                else:
                    ties += 1
            
            # 3. Calculate mathematical p-value
            p_val = fisher_randomization_test(scores_a_list, scores_b_list, n_permutations=1000)
            p_str = "< 0.001" if p_val == 0.0 else f"{p_val:.4f}"
                
            comp_name = f"[{model_a}] vs [{model_b}]"
            print(f"{comp_name:<48} | {wins:<5} | {ties:<5} | {losses:<6} | {p_str}")
            
    print("="*95 + "\n")

def plot_advanced_metrics(qrels: Qrels, runs: List[Run], output_dir: str) -> None:
    """
    Generates and exports advanced retrieval evaluation charts (Hit Rate, Rank Distribution, MRR).
    
    Args:
        qrels (Qrels): Ground truth definitions.
        runs (List[Run]): Model ranking outputs.
        output_dir (str): Destination directory for the exported PNG images.
    """
    print("\n[PROCESS] Generating and exporting advanced evaluation charts...")
    sns.set_theme(style="whitegrid")
    
    # Calculate metrics up to Top 20
    k_values = [1, 5, 10, 20]
    metrics_to_calc = [f"hit_rate@{k}" for k in k_values] + [f"mrr@{k}" for k in k_values]
    
    report = compare(qrels=qrels, runs=runs, metrics=metrics_to_calc)
    
    # ------------------------------------------
    # CHART 1: Hit Rate Evolution @ K
    # ------------------------------------------
    plot_data = []
    for model_name in report.model_names:
        for k in k_values:
            score = report.results[model_name][f"hit_rate@{k}"]
            plot_data.append({"Model": model_name, "K": k, "Hit Rate": score})
            
    df_hr = pd.DataFrame(plot_data)
    
    plt.figure(figsize=(8, 5))
    sns.lineplot(data=df_hr, x="K", y="Hit Rate", hue="Model", marker="o", linewidth=2.5, markersize=8)
    plt.title("Evolution of Hit Rate across Top-K Contexts", fontsize=14, pad=15)
    plt.xlabel("Number of retrieved chunks (Top K)", fontsize=12)
    plt.ylabel("Hit Rate (Probability of Success)", fontsize=12)
    plt.xticks(k_values)
    plt.ylim(0, 1.05)
    plt.legend(title="Embedding Model")
    plt.tight_layout()
    
    path_1 = os.path.join(output_dir, "Fig1_Hit_Rate_Evolution.png")
    plt.savefig(path_1, dpi=300)
    plt.close()
    print(f"  -> Exported: {path_1}")

    # ------------------------------------------
    # CHART 2: Rank Distribution Boxplot
    # ------------------------------------------
    ranks_data = []
    for run in runs:
        model_name = run.name
        for query_id, results in run.run.items():
            if query_id not in qrels.qrels: continue
            truth_chunks = qrels.qrels[query_id]
            
            sorted_res = sorted(results.items(), key=lambda x: x[1], reverse=True)
            for rank, (chunk_id, score) in enumerate(sorted_res, start=1):
                if chunk_id in truth_chunks and truth_chunks[chunk_id] > 0:
                    ranks_data.append({"Model": model_name, "Position": rank})
                    break

    df_ranks = pd.DataFrame(ranks_data)
    
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df_ranks, x="Model", y="Position", hue="Model", palette="Set2", showfliers=True, legend=False)
    plt.title("Distribution of the First Relevant Hit Position (Lower is Better)", fontsize=14, pad=15)
    plt.xlabel("Model", fontsize=12)
    plt.ylabel("Position (Rank)", fontsize=12)
    plt.ylim(0, 21) 
    plt.gca().invert_yaxis() # Invert Y-axis so Position 1 is at the top
    plt.tight_layout()
    
    path_2 = os.path.join(output_dir, "Fig2_Rank_Distribution.png")
    plt.savefig(path_2, dpi=300)
    plt.close()
    print(f"  -> Exported: {path_2}")

    # ------------------------------------------
    # CHART 3: Grouped Bar Chart for @10 Metrics
    # ------------------------------------------
    metrics_10 = ["hit_rate@10", "mrr@10"]
    bar_data = []
    
    for model_name in report.model_names:
        for m in metrics_10:
            score = report.results[model_name][m]
            bar_data.append({"Model": model_name, "Metric": m.upper(), "Score": score})

    df_bar = pd.DataFrame(bar_data)
    
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(data=df_bar, x="Metric", y="Score", hue="Model", palette="viridis")
    
    plt.title("Comparison of Primary Retrieval Metrics (@10)", fontsize=15, pad=15, fontweight="bold")
    plt.ylim(0, 1.05)
    plt.ylabel("Score (0.0 to 1.0)", fontsize=12)
    plt.xlabel("")
    
    # Add numbers on top of each bar
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.3f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=10)

    plt.legend(title="Embedding Model", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    path_3 = os.path.join(output_dir, "Fig3_Metrics_BarChart_10.png")
    plt.savefig(path_3, dpi=300)
    plt.close()
    print(f"  -> Exported: {path_3}")


# ==========================================
# 5. Main Execution Pipeline
# ==========================================
def main():
    try:
        input_path = os.path.join(EVALUATION_DATA_PATH, "evaluation_benchmark_final.json")
        with open(input_path, 'r', encoding='utf-8') as f:
            benchmark_data = json.load(f)

        # Map target configurations
        test_configs = [
            (DB_SCHEMA_TEST_1, TEST_EMBEDDING_MODEL_NAME_1),
            (DB_SCHEMA_TEST_2, TEST_EMBEDDING_MODEL_NAME_2),
            (DB_SCHEMA_TEST_3, TEST_EMBEDDING_MODEL_NAME_3)
        ]
        base_schema_for_json = DB_SCHEMA

        # Construct Baseline Qrels
        conn_qrels = connect_to_db(base_schema_for_json)
        qrels = build_graded_qrels(benchmark_data, conn_qrels)
        conn_qrels.close()

        # Execute Evaluation Runs
        runs = []
        for schema, model in test_configs:
            run = build_model_run(schema, model, benchmark_data, base_schema_for_json)
            runs.append(run)

        print("\n[PROCESS] Aggregating RAG Metrics (K=1, 5, 10, 20) and applying Randomization Test...")
        
        metrics_list = [
            "hit_rate@1", "hit_rate@5", "hit_rate@10", "hit_rate@20",
            "mrr@1", "mrr@5", "mrr@10", "mrr@20"
        ]
        
        report = compare(
            qrels=qrels,
            runs=runs,
            metrics=metrics_list,
            stat_test="fisher",  
            max_p=0.05           
        )
        
        print("\n" + "="*50)
        print(" --> FINAL AGGREGATE RESULTS ")
        print("="*50)
        print(report)

        print_win_tie_loss_matrix(qrels, runs, metric="mrr@10")
        print_win_tie_loss_matrix(qrels, runs, metric="hit_rate@10")
        
        print("\n" + "="*50)
        print(" --> GENERATED LATEX REPORT FOR THESIS ")
        print("="*50)
        print(report.to_latex())

        # Generate and route advanced charts to the Evaluation directory
        plot_advanced_metrics(qrels=qrels, runs=runs, output_dir=EVALUATION_DATA_PATH)
        
        print("\n[SUCCESS] Pipeline execution completed. All artifacts saved to the evaluation directory.\n")

    except Exception as e:
        print(f"\n[CRITICAL ERROR] Pipeline failed: {str(e)}")

if __name__ == "__main__":
    main()