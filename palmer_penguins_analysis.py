import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

print("Libraries imported successfully!")

# Load dataset
data_path = "./datasets/palmer_penguins/penguins.csv"
print(f"Loading data from {data_path}")
df = pd.read_csv(data_path)
print("Data loaded successfully!")

# Print first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Print dataset info
print("\nDataset info:")
print(df.info())

# Print dataset statistics
print("\nBasic statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Preprocess data
print("\nPreprocessing data...")
# 1. Impute numeric columns
numeric_cols = df.select_dtypes(include='number').columns
imputer = IterativeImputer(random_state=42)
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

# 2. Fill missing categorical values
df['sex'].fillna(df['sex'].mode()[0], inplace=True)

# 3. One-hot encoding
df = pd.get_dummies(df, columns=['sex', 'island'], drop_first=True)

# 4. Separate features and target
X = df.drop('species', axis=1)
y = df['species']

print("Preprocessing completed!")

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"\nTrain set: {X_train.shape[0]} samples, Test set: {X_test.shape[0]} samples")

# Train decision tree
print("\nTraining decision tree...")
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)
print("Model trained!")

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nTest accuracy: {accuracy:.4f}")

# Create output directories
os.makedirs("./results/accuracy_tables", exist_ok=True)
os.makedirs("./visualizations/palmer_penguins", exist_ok=True)

# Simple visualization
plt.figure(figsize=(10, 6))
sns.countplot(x=y, palette='viridis')
plt.title("Class Distribution in Palmer Penguins Dataset")
plt.xlabel("Penguin Species")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("./visualizations/palmer_penguins/class_distribution.png")
print("\nVisualization saved to ./visualizations/palmer_penguins/class_distribution.png")

print("\nScript execution completed successfully!")
