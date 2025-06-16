# UCI Heart Disease Dataset Documentation
## Overview
The UCI Heart Disease dataset is a medical research dataset containing information about patients and their heart disease status. This dataset is commonly used in predictive analytics and classification studies related to cardiovascular diseases.

## Basic Information
- Source: UCI Machine Learning Repository
- Number of Instances: 303 patients
- Number of Attributes: 14 (including the target variable)
- Data Types: Numerical and categorical data
- Missing Values: Yes (marked with '?' character)

## Data Fields
1. **age**: Age of the patient in years
    * Data type: Integer

2. **sex**: Gender of the patient
    * Data type: Binary
    * Value:
        - 1: Male
        - 0: Female

3. **cp**: Chest pain type
    * Data type: Categorical
    * Value:
        - 1: Typical angina
        - 2: Atypical angina
        - 3: Non-anginal pain
        - 4: Asymptomatic

4. **trestbps**: Resting blood pressure
    * Unit: mm Hg
    * Data type: Float

5. **chol**: Serum cholesterol level
    * Unit: mg/dl
    * Data type: Float

6. **fbs**: Fasting Blood Sugar
    * Data type: Binary
    * Value
        - 1: > 120 mg/dl
        - 0: ≤ 120 mg/dl

7. **restecg**: Resting electrocardiographic results
    * Data type: Categorical 
    * Value:
        - 0: Normal
        - 1: Having ST-T wave abnormality
        - 2: Showing probable or definite left ventricular hypertrophy by Estes' criteria

8. **thalach**: Maximum heart rate achieved
    * Unit: beats per minute
    * Data type: Integer

9. **exang**: Exercise induced angina
    * Data type: Binary
    * Value:
        - 1: Yes
        - 0: No

10. **oldpeak**: ST depression induced by exercise relative to rest
    * Data type: Float

11. **slope**: The slope of the peak exercise ST segment
    * Data type: Categorical
    * Value:
        - 1: Upsloping
        - 2: Flat
        - 3: Downsloping

12. **ca**: Number of major vessels (0-3) colored by fluoroscopy
    * Data type: Categorical (0-3)

13. **thal**: Thallium stress test result
    * Data type: Categorical
    * Value:
        - 3: Normal
        - 6: Fixed defect
        - 7: Reversible defect

14. **target**: Diagnosis of heart disease (angiographic disease status)
    * Data type: Binary
    * Value:
        - 0: < 50% diameter narrowing (no heart disease)
        - 1: > 50% diameter narrowing (has heart disease)
    * **<ins>Note<ins>**: In some versions of the dataset, this value may range from 0-4, where 0 indicates no disease and 1-4 indicate varying degrees of heart disease.

## Missing Values
Some attributes in the dataset may have missing values marked with the '?' character. When processing the data, these missing values should be handled by replacement or removal.

## Applications
This dataset is commonly used for:
* Developing predictive models for heart disease risk
* Researching factors that influence heart disease
* Analyzing relationships between health indicators and cardiovascular conditions
* Building medical diagnostic support systems

## References
The original dataset can be found at the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)