# Week 6 — Gene Co-Expression Networks Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Dataset Preparation
- Loaded GSE50081 Non-Small Cell Lung Cancer (NSCLC) microarray dataset (Der et al., PLoS ONE 2014) per `Task1_data_preparation.ipynb`.
- Dataset contains 181 tumor samples (adenocarcinoma + squamous cell carcinoma) with expression profiles.
- Downloaded via GEOparse and mapped Affymetrix probe IDs (GPL570) to HUGO gene symbols.
- Applied variance filtering to retain top 2000 most variable genes for WGCNA analysis.
- **TP53 confirmed present** in the final gene set for tumor-relevant analysis.
- Output: `artifacts/task1_expression_preprocessed.csv` with 2001 genes after filtering.

| Parameter | Value |
|-----------|-------|
| Dataset | GSE50081 (NSCLC Lung Cancer) |
| Platform | Affymetrix GPL570 |
| Total samples | 181 tumor samples |
| Cancer types | Adenocarcinoma + Squamous Cell |
| Genes after filtering | 2001 |
| Target gene | **TP53 ✓** |

## Task 2 — Network Construction
- Computed Pearson correlation matrix across all 2001 gene pairs per `Task2_network_construction.ipynb`.
- Applied WGCNA-style soft-thresholding with optimal power=5 (R² = 0.91 scale-free fit).
- Evaluated soft-threshold powers 1-20 using scale-free topology criterion.
- Output: `artifacts/task2_adjacency_matrix.csv` and `artifacts/task2_correlation_matrix.csv`.

| Parameter | Value |
|-----------|-------|
| Correlation method | Pearson |
| Soft-threshold power | 5 |
| Scale-free R² | 0.91 |
| Network type | Unsigned (absolute correlation) |

## Task 3 — Module Detection
- Applied **PyWGCNA** (authentic R WGCNA implementation in Python) per `Task3_module_detection.ipynb`.
- Computed Topological Overlap Matrix (TOM) with hierarchical clustering.
- Used **Dynamic Tree Cut** algorithm for module detection (WGCNA standard method).
- Identified 6 co-expression modules using color-based naming convention.
- **TP53 assigned to darkgrey module** (largest module, 625 genes).
- Output: `artifacts/task3_module_assignments.csv` and `artifacts/task3_hub_genes.csv`.

| Metric | Value |
|--------|-------|
| WGCNA method | PyWGCNA (TOM + Dynamic Tree Cut) |
| Modules detected | **6** |
| Hub genes identified | 60 (top 10 per module) |
| Largest module | darkgrey (625 genes) |
| TP53 module | **darkgrey** |

## Task 4 — Network Visualization
- Visualized co-expression network with nodes colored by WGCNA module colors per `Task4_visualization.ipynb`.
- Created hierarchical clustering dendrogram with module color bar.
- Generated correlation heatmap ordered by module membership showing clear block-diagonal structure.
- Output: PNG visualizations in `artifacts/task4_*.png`.

## Task 5 — Biological Interpretation
- Performed functional enrichment using **gseapy/Enrichr** API per `Task5_enrichment.ipynb`.
- Queried KEGG_2021_Human, GO_Biological_Process_2023, and Reactome_2022 databases.
- Generated module summaries with hub gene characterization.
- Output: `artifacts/task5_enrichment_*.csv` for each module.

### Key Findings:

| Module | Size | Biological Function | Key Pathways |
|--------|------|---------------------|--------------|
| **darkgrey** (TP53) | 625 | Lung adenocarcinoma markers | Surfactant metabolism, tight junctions, drug metabolism |
| lightgrey | 600 | Squamous cell markers | Epidermis development, keratinization, cornification |
| black | 230 | Immune/cell cycle | B-cell receptor signaling, cell cycle, DNA replication |
| gainsboro | 224 | Immune signaling | Chemokine signaling, cytokine-cytokine interaction |
| whitesmoke | 162 | Inflammatory/ECM | Inflammatory response, ECM-receptor interaction |
| silver | 160 | Coagulation/interferon | Complement/coagulation cascades, type I interferon |

### Module Characterization:

1. **Module darkgrey (TP53)**: Largest module containing **TP53** along with lung-specific genes. Enriched for surfactant metabolism (SFTPA1, SFTPB, SFTPC, SFTPD), tight junction assembly (CLDN3, CLDN7, CLDN18), and drug metabolism (CYP2B6). Hub genes include TP53, AGER, NKX2-1, and HOPX. Represents **lung adenocarcinoma** differentiation program with alveolar type II cell markers.

2. **Module lightgrey (Squamous Cell)**: Second largest module with epidermis development genes. Enriched for keratinization (KRT5, KRT6A, KRT14), cornified envelope formation, and epithelial cell differentiation. Hub genes include TP63, KRT5, DSG3, and SPRR1B. Represents **squamous cell carcinoma** differentiation markers.

3. **Module black (Immune/Cell Cycle)**: Contains B-cell receptor signaling genes (CD19, CD79A, MS4A1) and cell cycle regulators. Enriched for DNA replication, G1/S transition, and antigen processing. Reflects tumor-infiltrating lymphocytes and proliferative activity.

4. **Module gainsboro (Chemokine/Immune)**: Enriched for chemokine signaling (CCL5, CXCL9, CXCL10, CXCL11), cytokine-cytokine receptor interaction, and T-cell activation. Hub genes include CD8A, GZMK, and IFNG. Represents cytotoxic T-cell infiltration in tumor microenvironment.

5. **Module whitesmoke (Inflammatory/ECM)**: Contains inflammatory response genes and extracellular matrix components. Enriched for collagen fibril organization, ECM-receptor interaction, and complement activation. Hub genes include COL1A1, COL3A1, and MMP2. Represents tumor stroma and fibroblast activity.

6. **Module silver (Coagulation/Interferon)**: Smallest module enriched for complement and coagulation cascades (C3, C7, SERPIND1), type I interferon signaling, and acute phase response. Hub genes include C3, SERPINA1, and F13A1. Reflects systemic inflammatory response in cancer.

## Reflection

### Challenges Encountered
The primary challenge was selecting an appropriate dataset containing TP53. The initial GSE115469 liver dataset represented normal tissue where TP53 expression is low and stable. We switched to GSE50081 NSCLC lung cancer dataset where TP53 is highly relevant—TP53 mutations are common in lung cancer (~50% of cases). Another challenge was probe-to-gene mapping for Affymetrix arrays, resolved using the GPL570 annotation table with HUGO gene symbols.

### Insights Gained
The WGCNA analysis beautifully separated **adenocarcinoma vs squamous cell carcinoma** programs:
- **Darkgrey module** (TP53's module) contains lung-specific adenocarcinoma markers (NKX2-1/TTF-1, surfactant proteins)
- **Lightgrey module** contains squamous differentiation markers (TP63, keratins)

This reflects the fundamental biological distinction between these NSCLC subtypes. TP53 clustering with adenocarcinoma markers is interesting given that TP53 mutations have different prognostic implications in adenocarcinoma vs squamous cell carcinoma.

### Biological Interpretation
The NSCLC co-expression network reveals the tumor's cellular composition:
1. **Tumor cell programs**: Darkgrey (adenocarcinoma) and lightgrey (squamous) modules capture cancer cell differentiation states
2. **Immune infiltration**: Black, gainsboro, and parts of silver modules represent tumor-infiltrating lymphocytes
3. **Tumor microenvironment**: Whitesmoke module captures stromal/ECM components

The hub genes identified have clinical relevance:
- **NKX2-1** (TTF-1): Standard immunohistochemistry marker for lung adenocarcinoma
- **TP63**: Squamous cell carcinoma marker
- **CD8A, GZMK**: Cytotoxic T-cell markers predictive of immunotherapy response

### TP53 Analysis
**TP53 was successfully identified in the darkgrey module**, co-expressed with lung adenocarcinoma markers. This makes biological sense:
- TP53 is the most frequently mutated gene in lung cancer
- Wildtype TP53 co-expression with differentiation markers (surfactants, NKX2-1) reflects its role in maintaining differentiation
- The module's enrichment for tight junctions (CLDN3, CLDN7) aligns with TP53's role in epithelial integrity
