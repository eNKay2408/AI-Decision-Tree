import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def load_and_preprocess(path):
    df = pd.read_csv(path)
    imp = IterativeImputer(max_iter=10, random_state=42)
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = imp.fit_transform(df[numeric_cols])

    df['sex'].fillna(df['sex'].mode()[0], inplace=True)

    df = pd.get_dummies(df, columns=['sex','island'], drop_first=True)
    X = df.drop('species',axis=1)
    y = df['species']
    return X, y

# The function will be imported and called from the notebook
# Removing the example call
# load_and_preprocess('data/penguins.csv')