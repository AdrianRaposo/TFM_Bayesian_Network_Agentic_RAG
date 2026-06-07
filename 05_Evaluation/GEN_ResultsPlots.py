import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
from typing import List, Dict

# Import project configuration
from eval_config import EVALUATED_DATASETS_OUTPUT

def configure_plot_aesthetics() -> None:
    """
    Configures the global aesthetics for matplotlib and seaborn 
    to match scientific publication standards.
    """
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        'font.size': 12, 
        'font.family': 'sans-serif',
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight'
    })

def load_and_aggregate_data(base_path: str, file_names: List[str], target_metrics: List[str]) -> pd.DataFrame:
    """
    Loads evaluation JSON files and aggregates them into a unified, 
    melted DataFrame suitable for seaborn plotting.
    
    Args:
        base_path (str): Directory containing the evaluated JSON files.
        file_names (List[str]): List of JSON file names.
        target_metrics (List[str]): Keys of the metrics to extract.
        
    Returns:
        pd.DataFrame: Aggregated data with columns ['Model', 'Metric', 'Score'].
    """
    aggregated_data = []
    
    print("\n" + "="*75)
    print(" PHASE 1: DATA AGGREGATION FOR VISUALIZATION")
    print("="*75)

    for file_name in file_names:
        file_path = os.path.join(base_path, file_name)
        if os.path.exists(file_path):
            df = pd.read_json(file_path)
            model_name = file_name.replace("ragas_evaluated_ragas_dataset_generated_", "").replace(".json", "").upper()
            
            for metric in target_metrics:
                if metric in df.columns:
                    aggregated_data.append({
                        'Model': model_name,
                        'Metric': metric,
                        'Score': df[metric].mean()
                    })
            print(f"[INFO] Data extracted successfully for: {model_name}")
        else:
            print(f"[WARNING] File not found: {file_name}")

    return pd.DataFrame(aggregated_data)

def generate_grouped_barplot(df: pd.DataFrame, output_dir: str, palette: str = 'tab10') -> None:
    """
    Generates and exports a grouped bar chart comparing all models across metrics.
    
    Args:
        df (pd.DataFrame): Aggregated data containing 'Model', 'Metric', and 'Score'.
        output_dir (str): Directory to save the exported PNG plot.
        palette (str): Seaborn color palette to use.
    """
    print("\n[PROCESS] Generating Grouped Barplot...")
    
    # Format metric names for display
    df_plot = df.copy()
    df_plot['Metric'] = df_plot['Metric'].apply(lambda x: x.replace('_', ' ').title())

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=df_plot, 
        x='Metric', 
        y='Score', 
        hue='Model',
        palette=palette
    )

    # Scientific aesthetics
    plt.title('Average Generative Performance by Metric (Ragas Framework)', fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Score (0.0 - 1.0)', fontsize=12, fontweight='bold')
    plt.xlabel('')
    plt.ylim(0, 1.1)
    plt.legend(title='Evaluated Model', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Annotate bars with exact values
    for container in ax.containers:
        ax.bar_label(container, fmt='%.3f', padding=3, fontsize=10)

    # Export to disk
    output_path = os.path.join(output_dir, 'Fig1_Comparative_Barplot.png')
    plt.savefig(output_path)
    plt.close()
    print(f"[SUCCESS] Barplot exported to: {output_path}")

def generate_radar_chart(df: pd.DataFrame, metrics_keys: List[str], display_labels: List[str], output_dir: str, palette: str = 'tab10') -> None:
    """
    Generates and exports a multidimensional Radar (Spider) chart illustrating 
    the performance profile of each model.
    
    Args:
        df (pd.DataFrame): Aggregated data containing 'Model', 'Metric', and 'Score'.
        metrics_keys (List[str]): Exact metric names to enforce strict column ordering.
        display_labels (List[str]): Formatted labels for the chart axes.
        output_dir (str): Directory to save the exported PNG plot.
        palette (str): Seaborn color palette to use.
    """
    print("[PROCESS] Generating Multidimensional Radar Chart...")
    
    # Pivot data and enforce strict column ordering to match display_labels
    df_radar = df.pivot(index='Model', columns='Metric', values='Score')
    df_radar = df_radar[metrics_keys] # Crucial fix: prevents alphabetical reordering
    
    models = df_radar.index.tolist()
    num_vars = len(display_labels)

    # Calculate angles for each axis
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1] # Close the circular loop

    # Initialize polar plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    color_palette = sns.color_palette(palette, n_colors=len(models))

    # Plot each model's polygon
    for i, model_name in enumerate(models):
        values = df_radar.loc[model_name].values.flatten().tolist()
        values += values[:1] # Close the circular loop
        
        ax.plot(angles, values, linewidth=2.5, linestyle='solid', label=model_name, color=color_palette[i])
        # Lowered alpha to 0.10 for better visibility of overlapping polygons
        ax.fill(angles, values, color=color_palette[i], alpha=0.10) 

    # Plot aesthetics and grid
    ax.set_theta_offset(pi / 2) # Start top center
    ax.set_theta_direction(-1)  # Clockwise
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(display_labels, fontsize=11, fontweight='bold')
    
    # Y-axis scaling and ticks
    ax.set_ylim(0, 1)
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], color="grey", size=9)
    plt.ylim(0, 1.05)

    plt.title('Multidimensional Model Performance Profile', size=16, fontweight='bold', y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # Export to disk
    output_path = os.path.join(output_dir, 'Fig2_Performance_Radar_Chart.png')
    plt.savefig(output_path)
    plt.close()
    print(f"[SUCCESS] Radar Chart exported to: {output_path}")

def main():
    """
    Main execution pipeline for metric visualization.
    """
    # 1. Path routing
    current_dir = os.path.dirname(os.path.abspath(__file__))
    eval_dir = os.path.abspath(os.path.join(current_dir, "..", "00_Data", "EVALUATION"))
    
    # 2. Metric Definitions
    target_metrics = ['faithfulness', 'answer_relevancy', 'answer_correctness']
    radar_labels = ['Faithfulness', 'Answer Relevancy', 'Answer Correctness']
    
    # 3. Execution Pipeline
    try:
        configure_plot_aesthetics()
        
        df_aggregated = load_and_aggregate_data(
            base_path=eval_dir, 
            file_names=EVALUATED_DATASETS_OUTPUT, 
            target_metrics=target_metrics
        )
        
        if df_aggregated.empty:
            print("\n[CRITICAL] No data available for plotting. Terminating process.")
            return

        generate_grouped_barplot(
            df=df_aggregated, 
            output_dir=eval_dir, 
            palette='tab10'
        )
        
        generate_radar_chart(
            df=df_aggregated, 
            metrics_keys=target_metrics, 
            display_labels=radar_labels, 
            output_dir=eval_dir, 
            palette='tab10'
        )
        
        print("\n" + "="*75)
        print(" VISUALIZATION PIPELINE COMPLETED SUCCESSFULLY")
        print("="*75 + "\n")
        
    except Exception as e:
        print(f"\n[CRITICAL ERROR] The visualization pipeline failed: {str(e)}")

if __name__ == "__main__":
    main()