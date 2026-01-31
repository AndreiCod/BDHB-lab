# Assignment 9: Integrative Genomics Workflow

## Overview
Expand the integrative genomics workflow by replacing synthetic data with real-world subsets, varying analysis parameters, and interpreting biological and clinical results.

**Opened:** Tuesday, December 9, 2025, 00:00
**Due:** Friday, January 9, 2026, 00:00

---

## Part 1: Expanding the Datasets
Replace synthetic data with real-world subsets:

- **SNP data**
  - Download a small VCF file from the 1000 Genomes Project *or* a somatic mutation file (MAF) from TCGA.
  - Convert to a simplified SNP matrix (e.g., 0/1 for absence/presence of a variant) for a selected subset of samples.

- **Gene expression data**
  - Choose a dataset from GEO or GTEx.
  - Download normalized expression data for a set of samples that overlap (or can be matched) with your SNP subset.

- **Proteomics data**
  - Select a proteomics dataset from CPTAC.
  - Extract protein abundance data for the same cohort of samples.

- **Phenotype data**
  - Obtain clinical or phenotype information (e.g., treatment response, survival) from TCGA clinical data or GEO metadata.
  - Align phenotype entries with your selected samples.

**Goal:** Assemble a consistent multi-omics dataset where SNP, expression, proteomics, and phenotype files share sample IDs.

---

## Part 2: Adjusting Analysis Parameters
Inspect the integrated feature matrix (**X**) and experiment with different settings:

### A) Change the number of top variable features
- Instead of top 200 genes and top 100 proteins, try different thresholds (e.g., top 500 genes, top 200 proteins).
- Compare effects on:
  - clustering,
  - classification accuracy,
  - computational time,
  - PCA separation.

### B) Experiment with different clustering algorithms
- Replace K-means with:
  - hierarchical clustering,
  - DBSCAN.
- Compare the resulting clusters to phenotype data.

### C) Try alternative ML models
- Replace `RandomForestClassifier` with:
  - SVM,
  - gradient boosting,
  - MLP (neural network).
- Assess accuracy, precision, recall, or F1-score across models.

---

## Part 3: Biological and Clinical Interpretation

### A) Biological relevance of features
- Identify top variable genes/proteins.
- Research their known roles in your disease context.
- Are they known oncogenes, tumor suppressors, or signaling proteins?

### B) Phenotype-feature relationships
- Investigate whether certain SNPs or expression patterns correlate with key phenotypes (e.g., responders vs non-responders).
- Use a simple statistical test (t-test or ANOVA) where appropriate.

---

## Part 4: Additional Extensions (Optional)
- **Batch correction & normalization:** apply ComBat and compare results.
- **Network-based integration:** build gene-gene or protein-protein networks; identify hub nodes.
- **Dimensionality reduction alternatives:** t-SNE or UMAP for visualization.
- **Scaling up data size:** increase samples/features and discuss runtime/performance tradeoffs.

---

## Deliverables
Submit:
- **Code updates:** revised Python scripts incorporating real-world datasets, thresholds, clustering methods, and ML models.
- **Figures & plots:** PCA plots, dendrograms, or other visualizations showing the impact of changes.
- **Short report (1-2 pages):** describe datasets, parameters, methods, and key biological/clinical insights.
