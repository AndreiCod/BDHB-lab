# Week 8 — Supervised Learning for Cancer Classification Notes

# Authors
- Student: rbals (@rbals)

## Task 1 — Data Exploration and Preprocessing
- Loaded GSE50081 Non-Small Cell Lung Cancer (NSCLC) dataset from Lab 7 (181 samples, 2001 genes).
- Used **real clinical metadata** from GEO to classify **Adenocarcinoma vs Squamous Cell Carcinoma** (169 samples after filtering).
- Applied **ANOVA F-test feature selection** to reduce from 2001 to 100 most informative genes.
- Normalized features using `StandardScaler` and split 80/20 with stratification.
- Output: `data/task1_preprocessed_expression.csv`, `data/GSE50081_metadata.csv`.

| Parameter | Value |
|-----------|-------|
| Dataset | GSE50081 (NSCLC) |
| Classification | Adenocarcinoma (1) vs Squamous (0) |
| Total samples | 169 |
| Features (genes) | 100 (after selection) |
| Train/Test split | 80/20 |

## Task 2 — Logistic Regression Implementation
- **Note**: Assignment specified "cancer vs normal" classification, but GSE50081 contains only tumor samples. We use a clinically meaningful alternative: **Adenocarcinoma (1) vs Squamous Cell Carcinoma (0)** - two NSCLC subtypes requiring different treatments.
- **Logistic Regression Equation**:
  ```
  P(y=1|X) = 1 / (1 + exp(-(W·X + b)))
  ```
  Where:
  - **X**: Input feature vector (gene expression values)
  - **W**: Weight vector (learned coefficients for each gene)
  - **b**: Bias term (learned intercept)
  - **W·X + b**: Linear combination (decision function)
  - **Sigmoid function** (1/(1+exp(-z))): Maps linear output to probability [0,1]
  - Weights indicate gene importance: positive weights favor class 1 (Adenocarcinoma), negative favor class 0 (Squamous)
  
- Trained Logistic Regression model on NSCLC histological subtype classification:
  | Metric | Value |
  |--------|-------|
  | Accuracy | 0.8529 |
  | Precision | 0.8621 |
  | Recall | 0.9615 |
  | F1 | 0.9091 |
- Interpretation: High recall (96%) means the model correctly identifies most adenocarcinoma cases.
- Top contributing gene features exported to `artifacts/task2_logistic_regression_weights.csv`.

## Task 3 — SVM Classification
- Compared Linear and RBF kernels against Logistic Regression baseline:
  | Model | Kernel | Accuracy | F1 |
  |-------|--------|----------|--------|
  | Logistic Regression | N/A | 0.8529 | 0.9091 |
  | SVM | Linear | 0.7647 | 0.8519 |
  | SVM | RBF | 0.8824 | 0.9259 |
- Observations: SVM with RBF kernel achieves best performance (88% accuracy), indicating non-linear gene expression patterns distinguish the two cancer subtypes.

## Task 4 — Model Optimization
- Performed hyperparameter tuning using Grid Search with 5-fold cross-validation.
- Best parameters for RBF kernel:
  | Parameter | Value |
  |-----------|-------|
  | C | 1 |
  | gamma | 0.01 |
- Reference to full results: `artifacts/task4_svm_cv_results.csv`.

## Task 5 — Interpret Results
- Visualized decision boundaries using PCA (100 genes → 2 dimensions).
- Clear separation between Adenocarcinoma and Squamous Cell Carcinoma visible in PCA space.
- **Biological interpretation**: Gene expression profiles effectively distinguish NSCLC histological subtypes, which has clinical relevance for treatment selection.
- Visualization saved to: `artifacts/task5_decision_boundary.png`.
