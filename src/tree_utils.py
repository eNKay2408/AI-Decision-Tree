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
