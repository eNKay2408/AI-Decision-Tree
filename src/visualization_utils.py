"""
Visualization utilities for Decision Tree Project
Author: Team Coordinator (Duc Khai)

All visualization functions:
- `plot_class_distribution`: Visualizes class distribution in the dataset.
- `plot_split_distributions`: Compares class distributions across different train/test splits.
- `plot_confusion_matrix_styled`: Displays a styled confusion matrix.
- `plot_accuracy_vs_depth`: Plots accuracy against tree depth.
- `create_interactive_comparison`: Generates an interactive chart comparing multiple datasets.
- `generate_summary_table`: Creates a summary table of results.
- `create_standard_plots`: Template function to create all standard plots for a dataset.

Usage example for team members:

    # Import utilities
    from src.visualization_utils import create_standard_plots, plot_class_distribution

    # Load your data
    data = pd.read_csv('your_dataset.csv')

    # Create all standard plots
    create_standard_plots(data, 'target_column', 'Your Dataset Name', 'visualizations/your_dataset/')

    # Individual plots
    plot_class_distribution(data, 'target_column', 'Your Dataset', 'path/to/save.png')
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set global style
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")


def plot_class_distribution(data, target_col, title, save_path=None):
    """
    Plot class distribution for dataset

    Args:
      data: DataFrame containing data
      target_col: Name of target column
      title: Chart title
      save_path: File save path (optional)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Count plot
    sns.countplot(data=data, x=target_col, ax=ax1)
    ax1.set_title(f"{title} - Count Distribution")
    ax1.set_xlabel("Class")
    ax1.set_ylabel("Count")

    # Pie chart
    class_counts = data[target_col].value_counts()
    ax2.pie(class_counts.values, labels=class_counts.index, autopct="%1.1f%%")
    ax2.set_title(f"{title} - Percentage Distribution")

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

    # Print statistics
    print(f"\n{title} Class Distribution:")
    print(class_counts)
    print(f"Class proportions:\n{class_counts/len(data)*100:.2f}%")


def plot_split_distributions(splits_dict, dataset_name, save_path=None):
    """
    Plot comparison of class distributions across split ratios

    Args:
      splits_dict: Dictionary containing splits {ratio: (train_data, test_data)}
      dataset_name: Dataset name
      save_path: File save path
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(
        f"{dataset_name} - Class Distributions Across Different Splits", fontsize=16
    )

    ratios = list(splits_dict.keys())

    for i, ratio in enumerate(ratios):
        row = i // 2
        col = i % 2

        train_data, test_data = splits_dict[ratio]

        # Combine train and test for comparison
        train_counts = train_data.value_counts()
        test_counts = test_data.value_counts()

        # Create comparison dataframe
        comparison_df = pd.DataFrame(
            {"Train": train_counts, "Test": test_counts}
        ).fillna(0)

        comparison_df.plot(kind="bar", ax=axes[row, col])
        axes[row, col].set_title(f"Split {ratio} (Train/Test)")
        axes[row, col].set_ylabel("Count")
        axes[row, col].legend()
        axes[row, col].tick_params(axis="x", rotation=45)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def plot_confusion_matrix_styled(cm, classes, title, save_path=None):
    """
    Plot confusion matrix with standard style

    Args:
      cm: Confusion matrix from sklearn
      classes: Class names
      title: Title
      save_path: File save path
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues", xticklabels=classes, yticklabels=classes
    )
    plt.title(f"Confusion Matrix - {title}")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def plot_accuracy_vs_depth(depths, accuracies, dataset_name, save_path=None):
    """
    Plot accuracy vs depth chart

    Args:
      depths: List of depth values
      accuracies: List of corresponding accuracy values
      dataset_name: Dataset name
      save_path: File save path
    """
    plt.figure(figsize=(10, 6))

    # Line plot
    plt.plot(depths, accuracies, marker="o", linewidth=2, markersize=8)
    plt.title(f"{dataset_name} - Accuracy vs Tree Depth")
    plt.xlabel("Max Depth")
    plt.ylabel("Accuracy")
    plt.grid(True, alpha=0.3)

    # Annotate best accuracy
    best_idx = np.argmax(accuracies)
    plt.annotate(
        f"Best: {accuracies[best_idx]:.3f}",
        xy=(depths[best_idx], accuracies[best_idx]),
        xytext=(10, 10),
        textcoords="offset points",
        bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.7),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
    )

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def create_interactive_comparison(datasets_results, save_path=None):
    """
    Create interactive chart comparing datasets

    Args:
      datasets_results: Dict containing results from datasets
      save_path: HTML file save path
    """
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Accuracy Comparison",
            "Sample Size Comparison",
            "Feature Count Comparison",
            "Class Count Comparison",
        ),
        specs=[
            [{"secondary_y": False}, {"secondary_y": False}],
            [{"secondary_y": False}, {"secondary_y": False}],
        ],
    )

    datasets = list(datasets_results.keys())

    # Accuracy comparison
    for dataset in datasets:
        fig.add_trace(
            go.Scatter(
                x=datasets_results[dataset]["depths"],
                y=datasets_results[dataset]["accuracies"],
                mode="lines+markers",
                name=f"{dataset} Accuracy",
            ),
            row=1,
            col=1,
        )

    # Add other comparisons as needed...

    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Decision Tree Analysis - Comparative Results",
    )

    if save_path:
        fig.write_html(save_path)

    fig.show()


def generate_summary_table(results_dict, save_path=None):
    """
    Create summary table of results

    Args:
      results_dict: Dictionary containing results from datasets
      save_path: File save path
    """
    summary_data = []

    for dataset_name, results in results_dict.items():
        summary_data.append(
            {
                "Dataset": dataset_name,
                "Sample Size": results.get("sample_size", "N/A"),
                "Feature Count": results.get("feature_count", "N/A"),
                "Class Count": results.get("class_count", "N/A"),
                "Best Accuracy": f"{max(results.get('accuracies', [0])):.3f}",
                "Best Depth": results.get("depths", ["N/A"])[
                    np.argmax(results.get("accuracies", [0]))
                ],
            }
        )

    summary_df = pd.DataFrame(summary_data)

    # Style the table
    styled_table = summary_df.style.set_table_styles(
        [
            {
                "selector": "thead th",
                "props": [
                    ("background-color", "#40466e"),
                    ("font-weight", "bold"),
                    ("color", "white"),
                ],
            },
            {"selector": "tbody td", "props": [("text-align", "center")]},
            {"selector": "", "props": [("border", "1px solid #ddd")]},
        ]
    )

    if save_path:
        styled_table.to_html(save_path)

    return summary_df


# Template function for team members to use
def create_standard_plots(data, target_col, dataset_name, output_dir):
    """
    Create all standard plots for a dataset

    Args:
      data: DataFrame containing data
      target_col: Name of target column
      dataset_name: Dataset name
      output_dir: Output directory
    """
    import os

    os.makedirs(output_dir, exist_ok=True)

    # 1. Original data distribution
    plot_class_distribution(
        data,
        target_col,
        f"{dataset_name} - Original Data",
        f"{output_dir}/01_original_distribution.png",
    )

    print(f"✅ Standard plots created for {dataset_name}")
    print(f"📁 Saved to: {output_dir}")
