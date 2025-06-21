from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def train_decision_tree(X_train, y_train, depth=None):
    """
    Train a decision tree classifier with entropy criterion
    
    Parameters:
    X_train: Features for training
    y_train: Target labels for training
    depth: Maximum depth of the tree (None for unlimited)
    
    Returns:
    A trained DecisionTreeClassifier model
    """
    model = DecisionTreeClassifier(criterion='entropy', 
                                   max_depth=depth, 
                                   random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, split_id=None, output_dir='../results'):
    """
    Evaluate a model and save the classification report and confusion matrix
    
    Parameters:
    model: Trained model
    X_test: Test features
    y_test: True test labels
    split_id: Identifier for the train/test split being evaluated
    output_dir: Directory to save the evaluation results
    
    Returns:
    Dictionary with accuracy and classification report
    """
    # Create directories if they don't exist
    os.makedirs(f"{output_dir}/classification_reports", exist_ok=True)
    os.makedirs(f"{output_dir}/confusion_matrices", exist_ok=True)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    
    # Save classification report
    split_info = f"_split_{split_id}" if split_id is not None else ""
    with open(f"{output_dir}/classification_reports/report{split_info}.txt", "w") as f:
        f.write(report + "\n")
        f.write("Confusion Matrix:\n" + np.array2string(matrix))
    
    return {
        "accuracy": accuracy,
        "report": report,
        "matrix": matrix
    }

def analyze_tree_depth(X_train, X_test, y_train, y_test, 
                       depths=None, output_dir='../results'):
    """
    Analyze model performance across different tree depths
    
    Parameters:
    X_train, X_test, y_train, y_test: Train and test data
    depths: List of depths to test (default is None, 2-7)
    output_dir: Directory to save the results
    
    Returns:
    DataFrame with accuracy results for each depth
    """
    if depths is None:
        depths = [None, 2, 3, 4, 5, 6, 7]
    
    # Create directory if it doesn't exist
    os.makedirs(f"{output_dir}/accuracy_tables", exist_ok=True)
    
    accuracies = []
    
    for d in depths:
        model = train_decision_tree(X_train, y_train, depth=d)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        depth_label = 'Unlimited' if d is None else d
        accuracies.append({'max_depth': depth_label, 'accuracy': acc})
    
    # Save results to CSV
    df = pd.DataFrame(accuracies)
    df.to_csv(f"{output_dir}/accuracy_tables/accuracy_by_depth.csv", index=False)
    
    return df

def visualize_tree(model, feature_names, class_names, output_path=None, figsize=(20, 10)):
    """
    Visualize a decision tree model
    
    Parameters:
    model: Trained DecisionTreeClassifier
    feature_names: List of feature names
    class_names: List of class names
    output_path: Path to save the visualization
    figsize: Size of the figure
    """
    plt.figure(figsize=figsize)
    plot_tree(model, 
              feature_names=feature_names, 
              class_names=class_names, 
              filled=True, 
              rounded=True, 
              fontsize=10)
    
    plt.tight_layout()
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()
    
