# Week 7 — Network Visualization & Diseasome Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Data and Preprocessing
- Loaded **GSE50081** Non-Small Cell Lung Cancer (NSCLC) dataset (Der et al., PLoS ONE 2014) from Lab 6 per `Task1_preprocessing.ipynb`.
- Dataset contains 181 tumor samples (adenocarcinoma + squamous cell carcinoma).
- Data already RMA-normalized (log2 scale) from Affymetrix platform.
- Applied variance filtering to retain top 2000 most variable genes.
- **TP53 confirmed present** in the final gene set for tumor-relevant analysis.
- Output: `artifacts/task1_preprocessed_expression.csv`, `artifacts/task1_variance_stats.csv`, `artifacts/task1_tp53_expression.csv`.

| Parameter | Value |
|-----------|-------|
| Dataset | GSE50081 (NSCLC Lung Cancer) |
| Platform | Affymetrix GPL570 |
| Total samples | 181 tumor samples |
| Genes after filtering | 2001 |
| Target gene | **TP53 ✓** |

## Task 2 — Network and Modules (Louvain)
- Constructed gene-gene **Pearson** correlation matrix per `Task2_network_modules.ipynb`.
- Applied absolute correlation threshold (0.4) to build adjacency matrix.
- Built NetworkX graph and detected modules using **Louvain community detection**.
- **Key difference from Lab 6**: Louvain algorithm instead of WGCNA (TOM + Dynamic Tree Cut).
- Identified **11 modules** with TP53 assigned to **Module 4** (268 genes).
- Output: `artifacts/task2_modules.csv`, `artifacts/task2_hub_genes.csv`, `artifacts/task2_correlation_matrix.csv`, `artifacts/task2_network.gml`.

| Parameter | Value |
|-----------|-------|
| Correlation method | Pearson |
| Adjacency threshold | 0.4 |
| Module detection | **Louvain algorithm** |
| Resolution | 1.0 |
| Network nodes | 1948 |
| Network edges | 148,240 |
| Modules detected | **11** |
| TP53 module | **Module 4** (268 genes) |

## Task 3 — Visualization and Hub Genes
- Visualized network using Spring Layout (Fruchterman-Reingold) with `seed=42` per `Task3_visualization.ipynb`.
- Nodes colored by **Louvain module** membership using tab20 colormap.
- Hub genes identified by **degree centrality** within each module (top 10 per module).
- **TP53 specially highlighted** with red circle border.
- Created module size distribution and degree distribution plots.
- Generated TP53 ego network (local neighborhood) visualization.
- Output: `artifacts/task3_network.png`, `artifacts/task3_statistics.png`, `artifacts/task3_ego_network.png`.

## Task 4 — Biological Interpretation and Diseasome
- Selected **TP53's module (Module 4)** for enrichment analysis per `Task4_enrichment.ipynb`.
- Performed functional enrichment using **g:Profiler** API.
- Queried GO (Biological Process, Molecular Function, Cellular Component) databases.
- Identified **45 enriched terms** for TP53's module.
- Output: `artifacts/task4_enrichment.csv`, `artifacts/task4_enrichment.png`, `artifacts/task4_tp53_module_genes.txt`.

### Top Enriched GO Terms (TP53 Module 4)

| Term | p-value | Genes |
|------|---------|-------|
| Extracellular vesicle | 4e-6 | 46 |
| Cytoplasm | 6e-6 | 150 |
| Membrane | 4e-5 | 125 |
| Protein binding | 2e-4 | 179 |
| Apical part of cell | 1e-3 | 15 |

### Diseasome Context

The **human diseasome** (Goh et al., PNAS 2007; Barabási et al., Nature Reviews Genetics 2011) maps diseases to shared genes. Key insights:

1. **TP53 is a diseasome hub**: One of the most connected genes, linking cancer, aging, metabolic disorders, and neurodegenerative diseases.

2. **Module interpretation**: Genes co-expressed with TP53 in NSCLC may participate in:
   - Cell cycle regulation and checkpoint control
   - DNA damage response and repair
   - Apoptosis and senescence pathways
   - Metabolic reprogramming (Warburg effect)

3. **Clinical relevance**: Hub genes in TP53's module represent potential:
   - Therapeutic targets
   - Diagnostic/prognostic biomarkers
   - Indicators of disease comorbidity

4. **Integration with diseasome**: The TP53 co-expression module connects to multiple disease pathways, reflecting TP53's role as a "guardian of the genome" that integrates diverse stress signals.

## Visualization Advantages
Visualization provides several key advantages over pure numeric analysis:
- **Pattern Recognition**: Network topology reveals module clustering and inter-module connections not obvious from correlation matrices.
- **Hub Identification**: Visual emphasis on high-degree nodes (hub genes) makes their central role immediately apparent.
- **Communication**: Network figures effectively communicate complex relationships to collaborators.
- **Quality Control**: Visual inspection can reveal unexpected structures or artifacts in the data.
- **TP53 Context**: Seeing TP53's position in the network illustrates its connectivity and module membership.

## Comparison: WGCNA (Lab 6) vs Louvain (Lab 7)

| Aspect | WGCNA | Louvain |
|--------|-------|---------|
| Approach | Hierarchical clustering on TOM | Modularity optimization |
| Adjacency | Soft-thresholding (power) | Hard threshold |
| Module detection | Dynamic Tree Cut | Iterative community detection |
| Unassigned genes | "grey" module | All genes assigned |
| Computational complexity | O(n²) for TOM | O(n log n) |
| Module names | Colors (darkgrey, black, etc.) | Numeric IDs (0, 1, 2, ...) |

Both methods identify functionally coherent gene modules, but may produce different boundaries. The biological interpretation should be consistent for core module members.

## Reflection

### Challenges Encountered
The primary challenge was adapting the Lab 6 GSE50081 dataset workflow for Louvain-based analysis. Unlike WGCNA which uses TOM-based dissimilarity, Louvain works directly on the correlation graph, requiring different threshold selection. We chose a 0.4 correlation threshold to balance network density with meaningful co-expression relationships while maintaining sufficient connectivity for module detection.

### Insights Gained
Comparing WGCNA (Lab 6) and Louvain (Lab 7) on the same NSCLC dataset reveals:
- **Louvain finds fewer, larger modules** compared to WGCNA's color-named modules
- **Hub genes are consistent** across both methods within overlapping modules
- **TP53's co-expression partners** are largely preserved regardless of algorithm
- **Visualization is crucial** for understanding module structure and hub positions

The diseasome perspective adds clinical context: TP53's module likely contains genes involved in tumor suppression, DNA repair, and cell cycle control—pathways frequently disrupted across multiple cancer types.
