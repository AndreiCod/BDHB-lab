# Week 10 Assignment Workbooks — Integrative Genomics Workflow

This folder hosts Jupyter notebooks that implement the Week 10 Integrative Genomics assignment without touching the `submissions/` exercises. Each notebook focuses on one deliverable so they can be executed independently and exported into the Moodle ZIP bundle.

## Notebooks

- `Task1_data_acquisition.ipynb` — downloads real TCGA-BRCA multi-omics data from cBioPortal (SNP, expression, proteomics, phenotype), exports to `artifacts/task1_*.csv`.
- `Task2_parameter_experiments.ipynb` — experiments with feature thresholds, clustering algorithms (K-means, Hierarchical, DBSCAN), and ML models (Random Forest, SVM, Gradient Boosting, MLP), exports comparison results.
- `Task3_biological_interpretation.ipynb` — performs differential expression/protein analysis, SNP-phenotype association tests (chi-square), and RF feature importance analysis, exports statistical results.
- `Task4_visualization.ipynb` — creates PCA plots, dendrograms, volcano plots, model comparison charts, network graphs, and feature importance visualizations, exports figures.

All notebooks assume artifacts are stored in `artifacts/`. Run them sequentially from Task1 to Task4 as each depends on previous outputs.

## Dataset Overview

**Real TCGA-BRCA data** from cBioPortal (Breast Invasive Carcinoma, Pan-Cancer Atlas 2018):

| Data Type | Source | Features | Format |
|-----------|--------|----------|--------|
| **SNP** | TCGA whole-exome sequencing | 100 top mutated genes | Binary (0/1) |
| **Expression** | TCGA RNA-seq | 1000 genes (by variance) | Log2 RSEM |
| **Proteomics** | TCGA RPPA | 208 proteins | Z-normalized |
| **Phenotype** | Molecular subtype | Basal-like vs Non-Basal | Binary classification |

**Sample size**: 277 samples with matched multi-omics data (55 Basal-like, 222 Non-Basal)

> **Note**: We classify samples by **molecular subtype** (Basal-like = aggressive TNBC vs Non-Basal = other subtypes) as a proxy for clinical phenotype. The code labels use "responder/non_responder" terminology, but this represents subtype classification, not actual treatment response data.

## Key Experiments

### Part 2A: Feature Thresholds
- Tested: 100/200/500/800 genes × 50/100/150/200 proteins
- Metric: 5-fold CV accuracy with Random Forest
- **Best**: 800 genes + 50 proteins → 98.55% accuracy

### Part 2B: Clustering Algorithms
- K-Means (k=2)
- Hierarchical (Ward linkage)
- DBSCAN (eps auto-tuned)
- Metric: Adjusted Rand Index (ARI), Normalized Mutual Information (NMI)
- **Best**: DBSCAN (ARI=0.925, NMI=0.858)

### Part 2C: ML Models
- Random Forest (100 trees)
- SVM (RBF and Linear kernels)
- Gradient Boosting (100 estimators)
- MLP (64-32 architecture)
- Metric: Accuracy, Precision, Recall, F1-score
- **Best**: Random Forest & MLP tied at 97.5% accuracy

## Dependencies

```bash
pip install numpy pandas scikit-learn scipy matplotlib
```

| Package | Version | Purpose |
|---------|---------|---------|
| **numpy** | ≥1.20 | Numerical operations |
| **pandas** | ≥1.3 | Data manipulation |
| **scikit-learn** | ≥1.0 | ML algorithms, PCA, clustering |
| **scipy** | ≥1.7 | Statistical tests, hierarchical clustering |
| **matplotlib** | ≥3.5 | Visualization |

## Running the Notebooks

```bash
# From the repository root
cd labs/10_integrative/assignments

# Execute all notebooks in sequence
uv run jupyter execute Task1_data_acquisition.ipynb
uv run jupyter execute Task2_parameter_experiments.ipynb
uv run jupyter execute Task3_biological_interpretation.ipynb
uv run jupyter execute Task4_visualization.ipynb
```

## Output Files

All artifacts are saved to `artifacts/`:

| Task | File | Description |
|------|------|-------------|
| 1 | `task1_snp_data.csv` | SNP presence/absence matrix |
| 1 | `task1_expression_data.csv` | Gene expression matrix |
| 1 | `task1_proteomics_data.csv` | Protein abundance matrix |
| 1 | `task1_phenotypes.csv` | Clinical phenotype data |
| 2 | `task2_threshold_experiment.csv` | Feature threshold comparison |
| 2 | `task2_clustering_comparison.csv` | Clustering algorithm metrics |
| 2 | `task2_ml_comparison.csv` | ML model performance |
| 2 | `task2_integrated_features.csv` | Combined feature matrix |
| 2 | `task2_pca_features.csv` | PCA-transformed features |
| 3 | `task3_differential_expression.csv` | DE analysis results |
| 3 | `task3_differential_proteins.csv` | DP analysis results |
| 3 | `task3_snp_associations.csv` | SNP-phenotype associations |
| 3 | `task3_feature_importance.csv` | RF feature importance |
| 4 | `task4_pca_phenotype.png` | PCA by drug response |
| 4 | `task4_pca_clusters.png` | PCA with K-means clusters |
| 4 | `task4_dendrogram.png` | Hierarchical clustering |
| 4 | `task4_volcano.png` | Differential expression volcano |
| 4 | `task4_ml_comparison.png` | Model comparison chart |
| 4 | `task4_threshold_heatmap.png` | Feature threshold heatmap |
| 4 | `task4_feature_importance.png` | Top feature importance |
| 4 | `task4_dr_comparison.png` | PCA/t-SNE/UMAP comparison |
| 4 | `task4_hub_correlation.png` | Hub gene correlation heatmap |
| 4 | `task4_network_graph.png` | Gene correlation network |
| 4 | `task4_hub_genes.csv` | Hub gene statistics |
| 4 | `task4_network_edges.csv` | Network edge list |
| 4 | `task4_tsne_coordinates.csv` | t-SNE coordinates |
| 4 | `task4_umap_coordinates.csv` | UMAP coordinates |

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
