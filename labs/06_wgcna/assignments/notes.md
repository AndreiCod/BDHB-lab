# Week 6 — TP53 Co-Expression Networks Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Dataset Preparation
- Generated synthetic TP53-associated RNA-Seq dataset with 200 genes and 30 samples (15 tumor, 15 normal) per `Task1_data_preparation.ipynb`.
- Applied log2(x+1) transformation and filtered genes with variance < 0.1.
- Created 5 biologically-inspired gene modules: TP53 pathway (apoptosis), Cell cycle regulators, DNA damage response, Metabolic genes, and Housekeeping genes.
- Output: `artifacts/task1_expression_preprocessed.csv` with 67 genes after filtering.

## Task 2 — Network Construction
- Computed Pearson correlation matrix across all gene pairs per `Task2_network_construction.ipynb`.
- Applied WGCNA-style soft-thresholding with power=6 to create weighted adjacency matrix.
- Evaluated soft-threshold powers using scale-free topology criterion.
- Output: `artifacts/task2_adjacency_matrix.csv` and `artifacts/task2_correlation_matrix.csv`.

| Parameter | Value |
|-----------|-------|
| Correlation method | Pearson |
| Soft-threshold power | 6 |
| Network type | Unsigned (absolute correlation) |

## Task 3 — Module Detection
- Computed Topological Overlap Matrix (TOM) to capture network topology per `Task3_module_detection.ipynb`.
- Applied both hierarchical clustering (average linkage on TOM dissimilarity) and Louvain community detection.
- Identified hub genes as top 10% intramodular connectivity within each module.
- Output: `artifacts/task3_module_assignments.csv` and `artifacts/task3_hub_genes.csv`.

| Metric | Value |
|--------|-------|
| Modules detected (Louvain) | 4 |
| Hub genes identified | 7 |
| Largest module size | 20 genes |

## Task 4 — Network Visualization
- Visualized full co-expression network with nodes colored by module and hub genes labeled per `Task4_visualization.ipynb`.
- Created hierarchical clustering dendrogram with module color bar.
- Generated correlation heatmap ordered by module membership.
- Output: PNG visualizations in `artifacts/task4_*.png`.

## Task 5 — Biological Interpretation
- Performed Fisher's exact test enrichment against curated pathway gene sets per `Task5_enrichment.ipynb`.
- Analyzed pathways: Apoptosis, Cell Cycle, DNA Damage Response, p53 Signaling, Metabolism.
- Characterized TP53's position in Module 1 (Apoptosis).
- Output: `artifacts/task5_enrichment_results.csv` and `artifacts/task5_interpretation.json`.

### Key Findings:

| Module | Size | Top Pathway | Hub Genes | P-value |
|--------|------|-------------|-----------|---------|
| 1 | 20 | Apoptosis | APAF1, NOXA | 2.03e-14 |
| 2 | 20 | Cell Cycle | CDKN1A, E2F2 | 1.73e-17 |
| 3 | 20 | DNA Damage Response | XRCC1, ERCC2 | 3.62e-16 |
| 4 | 7 | Metabolism | AMPK | 1.15e-09 |

1. **TP53 pathway module (Module 1)**: Strongly enriched for apoptosis genes (BAX, PUMA, CASP3, CASP9). TP53 is positioned in this module with high connectivity.
2. **Cell cycle module (Module 2)**: Enriched for CDK/cyclin genes (CDK2, CDK4, CCND1, CCNE1) and checkpoint regulators (CHEK1, CHEK2).
3. **DNA damage response module (Module 3)**: Contains DNA repair genes (BRCA1, BRCA2, ATM, ATR, RAD51).
4. **Metabolic module (Module 4)**: Smaller module with TP53-regulated metabolic genes (TIGAR, GLS2, SCO2).

## Reflection

### Challenges Encountered
The main challenge was balancing network sparsity with biological signal. Initial variance filtering (threshold=0.5) was too aggressive, leaving only 21 genes and collapsing all into one module. Lowering to 0.1 retained 67 genes with distinct expression patterns, enabling meaningful module detection. The TOM-based approach helped by emphasizing shared neighbors rather than direct correlations alone.

### Insights Gained
Co-expression networks reveal functional relationships beyond individual gene expression levels. The modular structure mirrors known TP53 biology: apoptosis genes cluster together, cell cycle regulators form a distinct module, and metabolic genes show coordinated expression changes in tumors. Hub genes like NOXA, E2F2, and XRCC1 represent central regulators within their respective modules.

### Biological Interpretation
TP53's position in the apoptosis module reflects its role as "guardian of the genome." The strong connections to BAX, PUMA, and caspases represent the transcriptional program TP53 activates during DNA damage-induced apoptosis. The separation of cell cycle genes into Module 2 suggests these represent a different facet of TP53 function (cell cycle arrest vs. apoptosis), which may be context-dependent in cancer. The distinct DNA damage response module highlights the repair machinery that works upstream of TP53 activation.
