# Week 7 Assignment Workbooks — Gene Co-Expression Networks & Diseasome

This folder hosts Jupyter notebooks that implement the Week 7 Gene Co-Expression Networks, Visualization & Diseasome assignment. Each notebook focuses on one deliverable so they can be executed independently.

## Notebooks

- `Task1_preprocessing.ipynb` — loads GSE50081 NSCLC data (from Lab 6), applies variance filtering, ensures TP53 is included, exports `task1_preprocessed_expression.csv`.
- `Task2_network_modules.ipynb` — constructs Pearson correlation matrix, builds adjacency matrix with threshold, detects modules using **Louvain algorithm**, exports `task2_modules.csv` and `task2_hub_genes.csv`.
- `Task3_visualization.ipynb` — visualizes the network with NetworkX, colors nodes by Louvain module, highlights hub genes and TP53, exports `task3_network.png`.
- `Task4_enrichment.ipynb` — performs GO enrichment on TP53's module using g:Profiler, exports `task4_enrichment.csv`.

All notebooks assume artifacts are stored in `artifacts/`. Run them sequentially from Task1 to Task4 as each depends on previous outputs.

## Dataset

Uses **GSE50081** — Non-Small Cell Lung Cancer (NSCLC) Expression Dataset (Der et al., PLoS ONE 2014):
- **181 tumor samples** (adenocarcinoma + squamous cell carcinoma)
- Affymetrix Human Genome U133 Plus 2.0 Array (GPL570)
- Variance-filtered to top 2000 genes
- **TP53 present** ✓ for tumor-relevant analysis

This is the same dataset used in Lab 6 (WGCNA), but with **Louvain** module detection instead of WGCNA.

## Key Differences from Lab 6

| Aspect | Lab 6 (WGCNA) | Lab 7 (This) |
|--------|---------------|--------------|
| Module detection | PyWGCNA (TOM + Dynamic Tree Cut) | **Louvain algorithm** |
| Adjacency | Soft-thresholding (power=5) | Hard threshold (0.4) on correlation |
| Modules found | 6 | **11** |
| TP53 module size | 625 genes (darkgrey) | **268 genes (Module 4)** |
| Focus | WGCNA methodology | Visualization & Diseasome context |

## Dependencies

```bash
pip install networkx matplotlib gprofiler-official
```

| Package | Version | Purpose |
|---------|---------|---------|
| **networkx** | ≥3.0 | Graph construction and Louvain community detection |
| **matplotlib** | ≥3.5 | Network visualization |
| **gprofiler-official** | ≥1.0 | Enrichment via g:Profiler API |

## Running the Notebooks

```bash
# From the assignments directory
cd labs/07_network_viz/assignments

# Run all notebooks in sequence
for nb in Task*.ipynb; do
    uv run jupyter execute "$nb"
done
```

## Artifacts Generated

| Task | File | Description |
|------|------|-------------|
| 1 | `task1_preprocessed_expression.csv` | Variance-filtered expression matrix (2001 genes × 181 samples) |
| 1 | `task1_variance_stats.csv` | Gene variance statistics |
| 1 | `task1_tp53_expression.csv` | TP53 expression profile |
| 2 | `task2_modules.csv` | Gene → Module mapping (Louvain) |
| 2 | `task2_hub_genes.csv` | Hub genes per module with centrality scores |
| 2 | `task2_correlation_matrix.csv` | Gene-gene Pearson correlation |
| 2 | `task2_network.gml` | Network in GML format |
| 3 | `task3_network.png` | Main network visualization |
| 3 | `task3_statistics.png` | Module size and degree distributions |
| 3 | `task3_ego_network.png` | TP53's local neighborhood |
| 4 | `task4_enrichment.csv` | GO enrichment for TP53's module |
| 4 | `task4_enrichment.png` | Enrichment bar plot |
| 4 | `task4_tp53_module_genes.txt` | Genes in TP53's module

## Key Results

| Metric | Value |
|--------|-------|
| Correlation threshold | 0.4 |
| Network nodes | 1948 |
| Network edges | 148,240 |
| Network density | 0.078 |
| Louvain modules | 11 |
| TP53 module | **Module 4** (268 genes) |
| TP53 degree | 20 connections |
| Enriched terms | 45 (GO:CC, GO:MF, GO:BP) |

### TP53 Module Enrichment (Module 4)

Top enriched GO terms for TP53's module:
- **Extracellular vesicle** (p=4e-6) - 46 genes
- **Cytoplasm** (p=6e-6) - 150 genes
- **Membrane** (p=4e-5) - 125 genes
- **Protein binding** (p=2e-4) - 179 genes
- **Apical part of cell** (p=1e-3) - 15 genes

## Comparison: WGCNA vs Louvain

The Louvain algorithm differs from WGCNA in several ways:
- **No TOM**: Louvain works directly on the adjacency/correlation graph
- **Modularity optimization**: Maximizes modularity score rather than hierarchical clustering
- **Resolution parameter**: Controls granularity of detected communities
- **Faster**: O(n log n) vs WGCNA's O(n²) for TOM computation

Expected differences in results:
- Different number of modules (Louvain typically finds fewer, larger modules)
- Different module boundaries (no "grey" unassigned module)
- Similar hub genes within modules

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
