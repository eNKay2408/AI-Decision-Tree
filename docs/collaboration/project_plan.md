# DECISION TREE PROJECT PLAN
**Course:** Introduction to Artificial Intelligence - CS14003  
**Timeline:** 07/06/2025 - 26/06/2025 (20 days)  
**Group:** 4 members

## DATASET ASSIGNMENTS

| Member        | Dataset            | Description                              |
| ------------- | ------------------ | ---------------------------------------- |
| **Van Chien** | Heart Disease      | Binary classification - 303 samples      |
| **Van Khanh** | Palmer Penguins    | Multi-class classification - 344 samples |
| **Cat Huynh** | Additional Dataset | Self-selected dataset (>300 samples)     |
| **Duc Khai**  | Coordinator        | General support + Comparative Analysis   |

## MILESTONE 1: 07/06 - 12/06 (6 days)
**Objective:** Data Preparation (30% of grade)

**Task 2.1:** Prepare and preprocess data

### Member A (Heart Disease)
- Load and EDA Heart Disease data
- Split data in 4 ratios: 40/60, 60/40, 80/20, 90/10 (stratified split)
- Visualize class distributions for all splits
- Document data preparation process

### Member B (Palmer Penguins)
- Load Palmer Penguins data
- Process categorical features with one-hot encoding
- Split data in 4 ratios with stratified split
- Visualize class distributions

### Member C (Additional Dataset)
- Find and download suitable dataset (>300 samples, multi-class)
- EDA and write detailed dataset description
- Data preprocessing and cleaning
- Split data in 4 ratios and visualize distributions

### Member D (Coordinator)
- Initialize GitHub repository structure
- Create standardized visualization templates
- Quality check data preparation across all datasets
- Perform comparative analysis of preprocessing approaches

## MILESTONE 2: 13/06 - 17/06 (5 days)
**Objective:** Implement Decision Tree Classifiers (20% of grade)

**Task 2.2:** Build and visualize decision trees

### Members A, B, C (Each dataset)
- Build DecisionTreeClassifier with information gain
- Train models for all 4 train/test ratios
- Visualize decision trees using Graphviz
- Document implementation process

### Member D (Coordinator)
- Create report template
- Quality check decision tree implementations
- Prepare framework for comparative analysis

## MILESTONE 3: 18/06 - 26/06 (9 days)
**Objective:** Evaluation, Analysis & Report (50% of grade)

**Tasks 2.3, 2.4, 2.5:** Evaluation, analysis and comparison

### Week 1 (18/06 - 22/06): Performance Evaluation
**Members A, B, C (Each dataset):**
- **Task 2.3:** Performance evaluation (20% of grade)
  - Generate classification_report and confusion_matrix (10%)
  - Write insights about performance (10%)
- **Task 2.4:** Depth analysis (30% of grade)
  - Experiment with max_depth: None, 2, 3, 4, 5, 6, 7
  - Create visualizations (trees, tables, charts) (20%)
  - Analyze insights about depth-accuracy relationship (10%)

**Member D:**
- Quality check classification reports and confusion matrices
- Review insights, visualizations and depth analysis

### Week 2 (23/06 - 26/06): Final Integration
**23/06 - 24/06:**
- **Members A, B, C:** Complete individual analysis
- **Member D:** **Task 2.5:** Comparative analysis (5% of total grade)

**25/06:**
- **All:** Compile final report, format PDF
- Cross-check code and results
- Test submission files

**26/06:** 
- Final review and submission

---

## DELIVERABLES BY MILESTONE

| Milestone       | Deliverable                     | Deadline | Grade % |
| --------------- | ------------------------------- | -------- | ------- |
| **Milestone 1** | Data preparation for 3 datasets | 12/06    | 30%     |
| **Milestone 2** | Decision tree implementation    | 17/06    | 20%     |
| **Milestone 3** | Evaluation + Analysis + Report  | 26/06    | 50%     |

## DETAILED GRADE BREAKDOWN
- **Data preparation:** 30%
- **Decision tree implementation:** 20%
- **Performance evaluation:** 20% (Classification report 10% + Insights 10%)
- **Depth analysis:** 30% (Visualization 20% + Insights 10%)
- **Well-structured notebooks:** 5% (Milestone 3)
- **Comparative analysis:** 5% (Milestone 3)

## MEETING SCHEDULE
- **13/06:** Milestone 1 review
- **18/06:** Milestone 2 review 
- **25/06:** Pre-submission check

## SUBMISSION REQUIREMENTS
- **File format:** .zip/.rar/.7z
- **Naming:** StudentID1_StudentID2_StudentID3_StudentID4.zip
- **Contents:** 
  - Jupyter notebooks (.ipynb)
  - Code files (.py)
  - PDF report
  - Dataset files (if <25MB)
  - Google Drive link (if datasets >25MB)
- **AI tools declaration:** If used, must be listed in appendix