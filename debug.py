import sys
import os

print(f"Python version: {sys.version}")
print(f"Working directory: {os.getcwd()}")

try:
    import pandas as pd
    print(f"Pandas version: {pd.__version__}")
except ImportError:
    print("Pandas not installed")
    
try:
    import numpy as np
    print(f"NumPy version: {np.__version__}")
except ImportError:
    print("NumPy not installed")
    
try:
    import matplotlib
    print(f"Matplotlib version: {matplotlib.__version__}")
except ImportError:
    print("Matplotlib not installed")
    
try:
    import sklearn
    print(f"Scikit-learn version: {sklearn.__version__}")
except ImportError:
    print("Scikit-learn not installed")
    
try:
    import seaborn as sns
    print(f"Seaborn version: {sns.__version__}")
except ImportError:
    print("Seaborn not installed")

# Check if file exists
penguins_path = "./datasets/palmer_penguins/penguins.csv"
print(f"Does penguins.csv exist? {os.path.exists(penguins_path)}")

# List directory contents
dirs = [
    "./",
    "./datasets",
    "./datasets/palmer_penguins",
    "./notebooks",
    "./src"
]

for directory in dirs:
    if os.path.exists(directory):
        print(f"\nContents of {directory}:")
        for item in os.listdir(directory):
            print(f"  {item}")
    else:
        print(f"{directory} does not exist")
