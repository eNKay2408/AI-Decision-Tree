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
