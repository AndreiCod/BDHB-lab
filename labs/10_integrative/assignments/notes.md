# Week 10 — Integrative Genomics Workflow Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Data Acquisition and Preprocessing
- **Downloaded real TCGA-BRCA data** from cBioPortal (Breast Invasive Carcinoma, Pan-Cancer Atlas 2018) per `Task1_data_acquisition.ipynb`.
- Used cBioPortal REST API (free, no authentication required) to fetch multi-omics data.
- All 277 samples have matched patient IDs across SNP, expression, proteomics, and phenotype data types.
- Expression data from RNA-seq (1000 genes by variance), proteomics from RPPA (208 proteins), mutations from whole-exome sequencing (100 most frequently mutated genes).
- **Phenotype definition**: We use **molecular subtype** as a proxy for clinical phenotype classification:
  - **Basal-like** (labeled "responder" in code) — Triple-negative breast cancer (TNBC), aggressive subtype
  - **Non-Basal** (labeled "non_responder" in code) — Her2-enriched, Luminal A/B, Normal-like subtypes
- Output: `artifacts/task1_snp_data.csv`, `artifacts/task1_expression_data.csv`, `artifacts/task1_proteomics_data.csv`, `artifacts/task1_phenotypes.csv`.

> **Note on Phenotype Terminology**: The labels "responder/non_responder" in the code represent **molecular subtype classification** (Basal-like vs Non-Basal), NOT actual drug treatment response. This is a common approach when treatment response data is unavailable, as molecular subtypes are strongly predictive of clinical behavior and treatment sensitivity.

| Parameter | Value |
|-----------|-------|
| Samples | 277 |
| Genes | 1000 |
| Proteins | 208 |
| SNPs/Mutations | 100 (top mutated genes) |
| Molecular Subtypes | 5 (Basal-like, Her2-enriched, LumA, LumB, Normal-like) |
| Basal-like (coded as "responder") | 55 samples (~20%) |
| Non-Basal (coded as "non_responder") | 222 samples (~80%) |
| Data Source | TCGA-BRCA (brca_tcga_pan_can_atlas_2018) |

## Task 2 — Parameter Experiments

### Part A: Feature Threshold Comparison
- Tested 16 combinations of gene (100/200/500/800) and protein (50/100/150/200) thresholds per `Task2_parameter_experiments.ipynb`.
- Evaluated using 5-fold cross-validation with Random Forest classifier.
- Higher feature counts significantly improved accuracy on real TCGA-BRCA data.
- **Best performance: 800 genes + 50 proteins → 98.55% accuracy**.

| Genes | Proteins | CV Accuracy |
|-------|----------|-------------|
| 100 | 50 | 0.978 |
| 200 | 50 | 0.982 |
| 500 | 150 | 0.982 |
| **800** | **50** | **0.986** |

### Part B: Clustering Algorithm Comparison
- Compared K-Means, Hierarchical (Ward), and DBSCAN on PCA-transformed features.
- **DBSCAN achieved best performance** (ARI=0.925, NMI=0.858) on real data by identifying natural clusters.
- K-Means and Hierarchical also performed excellently with the real multi-omics data.

| Method | ARI | NMI |
|--------|-----|-----|
| K-Means | 0.904 | 0.834 |
| Hierarchical | 0.903 | 0.805 |
| **DBSCAN** | **0.925** | **0.858** |

### Part C: ML Model Comparison
- Tested 5 classifiers: Random Forest, SVM (RBF/Linear), Gradient Boosting, MLP.
- **All models achieved excellent performance** (>96% accuracy) on real TCGA-BRCA data.
- Random Forest and MLP tied for highest accuracy (97.5%).

| Model | Accuracy | F1-Score |
|-------|----------|----------|
| **RandomForest** | **0.975 ± 0.014** | **0.938 ± 0.036** |
| SVM (RBF) | 0.975 ± 0.018 | 0.938 ± 0.045 |
| SVM (Linear) | 0.964 ± 0.028 | 0.909 ± 0.075 |
| GradientBoosting | 0.964 ± 0.016 | 0.908 ± 0.042 |
| **MLP** | **0.975 ± 0.018** | **0.936 ± 0.049** |

## Task 3 — Biological and Clinical Interpretation
- Performed differential expression analysis using t-test with Benjamini-Hochberg correction per `Task3_biological_interpretation.ipynb`.
- Identified differentially expressed genes (FDR < 0.05) between **Basal-like** and **Non-Basal** subtypes.
- **TP53 and PIK3CA mutations** significantly associated with molecular subtype (FDR < 0.05).
- SNP-subtype associations tested with chi-square test.

### Statistical Analysis Results
- Differential expression: **1001 genes analyzed**, top genes by fold-change identified.
- SNP associations: **2 significant mutations** after FDR correction - TP53 and PIK3CA.
- Feature importance: Top features include genes 10551, 79083, 25803 (Entrez IDs).

### Significant Mutation-Subtype Associations
| Gene | Chi-Square | P-Value | Odds Ratio | Biological Interpretation |
|------|------------|---------|------------|---------------------------|
| **TP53** | **71.18** | **3.27e-17** | **19.21** | Enriched in Basal-like (expected: ~80% in TNBC) |
| **PIK3CA** | **20.43** | **6.17e-06** | **0.09** | Enriched in Luminal subtypes (expected: ~40%) |

### Known Cancer Gene Analysis — Literature Validation
Our findings align with established breast cancer biology (TCGA Network, Nature 2012):
- **TP53**: Tumor suppressor, mutated in **85% of Basal-like** vs 23% of Non-Basal. Literature reports ~80% TP53 mutations in TNBC/Basal-like subtype — **our data matches**.
- **PIK3CA**: PI3K pathway oncogene, mutated in **5% of Basal-like** vs 38% of Non-Basal. Literature reports ~40% PIK3CA mutations in Luminal subtypes — **our data matches**.
- **CDH1**: E-cadherin tumor suppressor, frequently mutated in lobular breast cancer (Luminal subtypes).
- **GATA3**: Transcription factor essential for luminal differentiation, rarely mutated in Basal-like.
- **MAP3K1**: MAPK signaling pathway, commonly mutated in Luminal A breast cancer.

## Task 4 — Visualization
- Created comprehensive visualization suite per `Task4_visualization.ipynb`.
- **PCA plots show clear separation** between Basal-like and Non-Basal subtypes.
- **Volcano plot highlights differentially expressed genes** with significant fold changes between subtypes.
- **Dimensionality reduction comparison**: PCA, t-SNE, and UMAP all show distinct cluster separation.
- **Gene correlation network**: 100 nodes with edges based on correlation threshold = 0.4.
- **Hub genes identified**: Entrez IDs 3169, 2099, 3868, 7033 (highest degree centrality).

### Generated Figures
| Figure | Description |
|--------|-------------|
| `task4_pca_phenotype.png` | PCA colored by molecular subtype (Basal vs Non-Basal) |
| `task4_pca_clusters.png` | PCA with K-means cluster assignments |
| `task4_dendrogram.png` | Hierarchical clustering dendrogram |
| `task4_volcano.png` | Differential expression volcano plot |
| `task4_ml_comparison.png` | ML model performance comparison |
| `task4_threshold_heatmap.png` | Feature threshold optimization heatmap |
| `task4_feature_importance.png` | Top 15 predictive features |
| `task4_dr_comparison.png` | PCA/t-SNE/UMAP comparison |
| `task4_hub_correlation.png` | Hub gene correlation heatmap |
| `task4_network_graph.png` | Gene correlation network graph |

### Network Analysis Results
- Built gene correlation network from top 100 high-variance genes.
- **Top Hub Genes** (by degree centrality):

| Gene (Entrez ID) | Degree | Avg Correlation |
|------------------|--------|-----------------|
| 3169 | 49 | 0.529 |
| 2099 | 43 | 0.536 |
| 3868 | 38 | 0.566 |
| 7033 | 36 | 0.530 |
| 8842 | 34 | 0.503 |

## Key Findings

### Multi-Omics Integration
- **Real TCGA-BRCA data achieves 98.55% classification accuracy** using integrated multi-omics features.
- Combining SNP, expression, and proteomics data dramatically outperforms single data types.
- PCA effectively reduces dimensionality while preserving phenotype-relevant variance (clear Basal vs non-Basal separation).
- Feature selection is critical—800 genes + 50 proteins achieved best performance.

### Biological Insights
- **TP53 mutation strongly associated with Basal-like subtype** (OR=19.21, p=3.27e-17) — consistent with ~80% TP53 mutation rate in TNBC reported in literature.
- **PIK3CA mutation enriched in Luminal/Non-Basal subtypes** (OR=0.09, p=6.17e-06) — matches literature reporting ~40% PIK3CA mutations in ER+ breast cancer.
- Differential expression analysis identifies genes distinguishing molecular subtypes with high statistical significance.
- Hub genes in correlation network may represent key regulatory nodes in breast cancer biology.

### Practical Recommendations
1. **Feature Selection**: Use variance-based filtering, ~800 genes and ~50 proteins optimal for TCGA-BRCA.
2. **Clustering**: DBSCAN achieves best ARI (0.925) on real multi-omics data.
3. **Classification**: All models achieve >96% accuracy; Random Forest and MLP tied at 97.5%.
4. **Visualization**: PCA essential for quality control; t-SNE/UMAP reveal finer structure.

## Limitations
- **Phenotype proxy**: Using molecular subtype (Basal-like vs Non-Basal) as classification target instead of actual treatment response data. While molecular subtypes are clinically meaningful and predict treatment sensitivity, they are not equivalent to measured drug response.
- **Class imbalance**: 55 Basal-like vs 222 Non-Basal samples (20% vs 80%) reflects real-world prevalence but may affect model training.
- **Feature interpretation**: Gene/protein names are Entrez IDs requiring database lookup for biological interpretation.
- **Single-center data**: TCGA-BRCA represents primarily US population; results may not generalize globally.

## Extensions Implemented
- **Real-world data**: TCGA-BRCA from cBioPortal (277 matched samples).
- **Multiple dimensionality reduction**: PCA, t-SNE, UMAP comparison.
- **Gene correlation network**: Hub gene identification (NetworkX).
- **Multiple clustering algorithms**: K-Means, Hierarchical, DBSCAN comparison.
- **Multiple ML models**: RF, SVM, GB, MLP comparison with excellent performance.
- **Statistical testing**: t-tests, chi-square, Benjamini-Hochberg correction.
- **Feature importance**: Random Forest Gini importance analysis.
