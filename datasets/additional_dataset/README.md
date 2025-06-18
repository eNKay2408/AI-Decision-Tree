# Dermatology Dataset (UCI) - Detailed Description

## Summary

This dataset contains clinical and histopathological data for the differential diagnosis of erythemato-squamous diseases. The data was originally sourced from the UCI Machine Learning Repository ([link](https://archive.ics.uci.edu/dataset/33/dermatology)). The main challenge addressed by this dataset is the accurate classification of six types of erythemato-squamous diseases, which often share overlapping clinical and histopathological features.

## Problem Type

- **Classification**

## Purpose

The purpose of this dataset is to develop and evaluate machine learning models, particularly decision trees, for the classification of erythemato-squamous diseases based on patient features. The dataset is widely used for benchmarking classification algorithms in medical diagnosis tasks.

## Columns Meaning

The dataset consists of 34 columns:

### Clinical Attributes (Columns 1-10, 12, 34)

1. erythema
2. scaling
3. definite borders
4. itching
5. koebner phenomenon
6. polygonal papules
7. follicular papules
8. oral mucosal involvement
9. knee and elbow involvement
10. scalp involvement
11. family history (0 or 1)
12. age (linear, may contain missing values)

### Histopathological Attributes (Columns 12-33)

12. melanin incontinence
13. eosinophils in the infiltrate
14. PNL infiltrate
15. fibrosis of the papillary dermis
16. exocytosis
17. acanthosis
18. hyperkeratosis
19. parakeratosis
20. clubbing of the rete ridges
21. elongation of the rete ridges
22. thinning of the suprapapillary epidermis
23. spongiform pustule
24. munro microabcess
25. focal hypergranulosis
26. disappearance of the granular layer
27. vacuolisation and damage of basal layer
28. spongiosis
29. saw-tooth appearance of retes
30. follicular horn plug
31. perifollicular parakeratosis
32. inflammatory monoluclear infiltrate
33. band-like infiltrate

### Target Column

- The **last column** (35th) is the target variable, representing the disease class:
  1. Psoriasis
  2. Seboreic dermatitis
  3. Lichen planus
  4. Pityriasis rosea
  5. Chronic dermatitis
  6. Pityriasis rubra pilaris

## Features and Target

- **Features:** All columns except the last (1-34)
- **Target:** Last column (disease class)

## Method

The primary method to be used for analysis and classification is the **Decision Tree** algorithm. Decision trees are interpretable and effective for handling categorical and integer-valued features, making them suitable for medical diagnostic tasks.

## Insights from Source and Literature

- The dataset is challenging due to overlapping features among disease classes and the presence of missing values (notably in the age column).
- Both clinical and histopathological features are important for accurate diagnosis.
- Decision trees and ensemble methods (e.g., voting feature intervals, as discussed in [Güvenir et al., 1998](https://www.semanticscholar.org/paper/eb371061d34d08b01856f8fe8e66d2a689f3419c)) have been shown to perform well on this dataset.
- The dataset is widely used for benchmarking classification algorithms in medical informatics.

## References

1. UCI Machine Learning Repository: Dermatology Data Set. https://archive.ics.uci.edu/dataset/33/dermatology
2. Güvenir, H. A., Demiröz, G., & Ilter, N. (1998). Learning differential diagnosis of erythemato-squamous diseases using voting feature intervals. _Artificial Intelligence in Medicine_, 13(1), 147-165. [CORE full text](https://core.ac.uk/reader/52921850?utm_source=linkout)
3. Ilter, N. & Guvenir, H. (1998). Dermatology [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5FK5P

---

This dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode).
