import sys
import os
import json
import asyncio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from dotenv import load_dotenv

# 1. Configure project paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
agentic_rag_path = os.path.join(project_root, '04_AgenticRAG')
sys.path.append(agentic_rag_path)
#load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# 2. Import async classification function
from services.llm import classify_query

async def evaluate_router():
    """
    Evaluates the cognitive router's classification performance.
    
    This function:
    - Loads test dataset from JSON file
    - Classifies each query using the LLM
    - Computes accuracy, precision, recall, and F1-score
    - Generates confusion matrix and metrics bar chart
    - Reports classification errors
    """
    json_path = os.path.join(os.path.dirname(__file__), 'router_eval_dataset.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    y_true = []
    y_pred = []
    queries = []

    print("========================================")
    print(" Running Router Benchmarking...")
    print("========================================\n")

    # Run LLM inference on entire dataset
    for item in dataset:
        print(f"Evaluating ID {item['id']}: {item['query'][:50]}...")
        decision = await classify_query(item["query"], item["history"])
        
        y_true.append(item["expected_category"])
        y_pred.append(decision.category)
        queries.append(item["query"])
        
    print("\n Inference completed. Generating metrics and charts...\n")

    labels = ['BN', 'MD', 'CC', 'OOC']
    
    # Calculate accuracy and detailed classification metrics
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, labels=labels, output_dict=True)
    report_text = classification_report(y_true, y_pred, labels=labels)
    
    print("--- GLOBAL RESULTS ---")
    print(f"Global Accuracy: {accuracy:.4f} ({(accuracy*100):.2f}%)\n")
    print("Classification Report:")
    print(report_text)

    # Display classification errors
    print("--- ERRORS FOUND ---")
    errors_found = False
    for t, p, q in zip(y_true, y_pred, queries):
        if t != p:
            print(f" Expected: {t} | Predicted: {p} | Query: '{q}'")
            errors_found = True
    if not errors_found:
        print("Perfect! 0 errors found.")

    # --- GENERATE VISUALIZATIONS ---
    output_dir = os.path.dirname(__file__)
    
    # 1. Confusion Matrix Heatmap
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.title('Confusion Matrix - Cognitive Router')
    plt.ylabel('True Category')
    plt.xlabel('Predicted Category')
    plt.tight_layout()
    cm_path = os.path.join(output_dir, 'Router_Confusion_Matrix.png')
    plt.savefig(cm_path, dpi=300)
    plt.close()

    # 2. Bar Chart: Precision, Recall, and F1-Score by Category
    metrics_df = pd.DataFrame({
        'Category': labels,
        'Precision': [report[label]['precision'] for label in labels],
        'Recall': [report[label]['recall'] for label in labels],
        'F1-Score': [report[label]['f1-score'] for label in labels]
    })
    
    # Transform data for Seaborn grouped bar chart
    metrics_melted = pd.melt(metrics_df, id_vars='Category', var_name='Metric', value_name='Score')
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Score', hue='Metric', data=metrics_melted, palette='viridis')
    plt.title('Performance Metrics by Category')
    plt.ylim(0, 1.05)  # Scores range from 0 to 1
    plt.legend(loc='lower right')
    plt.tight_layout()
    bar_path = os.path.join(output_dir, 'Router_Metrics_BarChart.png')
    plt.savefig(bar_path, dpi=300)
    plt.close()

    print(f"\n Charts saved successfully at:\n- {cm_path}\n- {bar_path}")

if __name__ == "__main__":
    asyncio.run(evaluate_router())