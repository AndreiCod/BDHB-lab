# Week 8 Assignment Workbooks

This folder hosts Jupyter notebooks that implement the Week 8 Supervised Learning assignment without touching the `submissions/` exercises. Each notebook focuses on one deliverable so they can be executed independently and exported into the Moodle ZIP bundle.

## Notebooks

- `Task1_preprocessing.ipynb` — load GSE50081 NSCLC dataset, merge with clinical metadata for Adeno vs Squamous classification, apply feature selection (100 genes), and split.
- `Task2_logistic_regression.ipynb` — train logistic regression model and evaluate performance metrics.
- `Task3_svm_classification.ipynb` — compare SVM linear and RBF kernels against the logistic regression baseline.
- `Task4_optimization.ipynb` — perform hyperparameter tuning (C and gamma) using GridSearchCV.
- `Task5_interpretation.ipynb` — visualize decision boundaries and synthesize final results.

## Data

The `data/` folder contains:
- `task1_preprocessed_expression.csv` — Lab 7 preprocessed gene expression data
- `GSE50081_metadata.csv` — Clinical metadata with histology labels

All notebooks should be run from the `labs/08_ML_flower/assignments/` directory so relative paths stay consistent.

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
