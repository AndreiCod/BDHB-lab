# Assignment 7: Supervised Learning for Cancer Classification

## Overview
Apply supervised learning techniques to classify cancer states using gene expression data and interpret model performance.

**Opened:** Tuesday, November 25, 2025, 00:00
**Due:** Thursday, December 18, 2025, 00:00

---

## Dataset
- **Source:** Use the same dataset as the previous assignment (e.g., `cancer_gene_expression.csv` or a processed RNA-Seq table).
- **Description:** Labeled gene expression data with features representing gene activity and target labels indicating cancer (1) or normal (0) samples.
- **Preprocessing:** Normalize the dataset and split into training (80%) and testing (20%) subsets.

---

## Tasks

### 1. Data Exploration and Preprocessing
- Load the dataset and explore its structure (dimensions, feature names, summary statistics).
- Perform normalization to ensure features are on a comparable scale.
- Identify and handle any missing values.

### 2. Logistic Regression Implementation
- Train a logistic regression model using the training dataset.
- Write the equation for logistic regression and explain the role of weights, bias, and the sigmoid function.
- Evaluate the model using metrics like accuracy, precision, recall, and F1-score.

### 3. Support Vector Machine (SVM) Classification
- Train an SVM with both **linear** and **RBF** kernels.
- Discuss how the kernel choice impacts performance.
- Evaluate and compare the results with logistic regression.

### 4. Model Optimization
- Perform hyperparameter tuning for SVM (e.g., `C` for regularization, `gamma` for the RBF kernel).
- Use cross-validation to select the best parameters.

### 5. Interpret Results
- Compare the performance of logistic regression and SVM models.
- Visualize the decision boundaries for the models (if feasible).
- Write a brief interpretation of the results, focusing on their implications for cancer classification.

---

## Deliverables
Submit:
- **Code notebook** (e.g., `.ipynb` or `.py`) implementing the workflow.
- **Report (1 page max)** covering:
  - dataset overview,
  - model selection and training,
  - performance comparison between logistic regression and SVM,
  - insights and interpretation of the results.
