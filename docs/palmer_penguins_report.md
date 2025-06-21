# Palmer Penguins Analysis Report

## Overview of the Palmer Penguins Dataset

The Palmer Penguins dataset contains data for three penguin species observed in the Palmer Archipelago, Antarctica:

- Adelie
- Chinstrap
- Gentoo

The dataset includes measurements of:

- Bill length (mm)
- Bill depth (mm)
- Flipper length (mm)
- Body mass (g)
- Sex (male/female)
- Island (Biscoe, Dream, Torgersen)

## Data Preprocessing

- Missing values in numeric columns were imputed using the IterativeImputer, which uses a multivariate approach to estimate missing values based on relationships between variables
- Missing values in the sex column were filled with the mode value
- Categorical variables (sex, island) were one-hot encoded with drop_first=True to avoid multicollinearity

## Model Development

We trained decision tree models to classify penguins into their respective species using various train/test splits:

- 40/60 split
- 60/40 split
- 80/20 split
- 90/10 split

We also analyzed the effect of tree depth on model performance, testing depths from 2 to 7 as well as unlimited depth.

## Findings

### Class Distribution Analysis

Each penguin species is well-represented in the dataset, ensuring balanced training across classes in all splits.

### Decision Tree Performance

- The decision trees achieved high accuracy across all train/test splits
- The 90/10 split typically yielded the highest accuracy due to having more training data
- The most important features for classification were flipper length and bill length

### Tree Depth Analysis

- Trees with depth 3-4 typically achieved the best balance between model complexity and performance
- Deeper trees showed signs of overfitting, particularly when using depths greater than 5
- Unlimited depth trees achieved high accuracy but were more complex and potentially less generalizable

## Conclusions

1. Decision trees are an effective model for classifying penguin species based on physical characteristics
2. The optimal depth for decision trees in this task is around 3-4 levels
3. The most discriminative features are flipper length and bill length
4. A reasonably high accuracy can be achieved with relatively simple models

## Future Work

- Test with other machine learning algorithms for comparison
- Perform feature importance analysis to identify the most critical measurements
- Use ensemble methods like Random Forest to potentially improve performance
- Investigate the effect of feature engineering on model performance
