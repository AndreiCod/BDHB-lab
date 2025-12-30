# Week 6 Assignment Workbooks — TP53 Co-Expression Networks

This folder hosts Jupyter notebooks that implement the Week 6 Gene Co-Expression Networks assignment. Each notebook focuses on one deliverable so they can be executed independently.

## Notebooks

- `Task1_data_preparation.ipynb` — loads TP53-associated RNA-Seq data, applies log2 transformation and variance filtering, exports preprocessed matrix.
- `Task2_network_construction.ipynb` — computes Pearson correlation matrix and constructs adjacency matrix using soft-thresholding (WGCNA-style).
- `Task3_module_detection.ipynb` — detects gene modules using TOM-based hierarchical clustering and Louvain algorithm, identifies hub genes.
- `Task4_visualization.ipynb` — visualizes the network with module coloring, creates dendrograms and correlation heatmaps.
- `Task5_enrichment.ipynb` — performs functional enrichment analysis on modules using Fisher's exact test against curated pathway gene sets.

All notebooks assume artifacts are stored in `artifacts/`. Run them sequentially from Task1 to Task5 as each depends on previous outputs.

## Running the Notebooks

```bash
# From the assignments directory
cd labs/06_wgcna/assignments

# Run all notebooks in sequence
for nb in Task*.ipynb; do
    uv run jupyter execute "$nb"
done
```

## Artifacts Generated

| Task | File | Description |
|------|------|-------------|
| 1 | `task1_expression_preprocessed.csv` | Log-transformed, variance-filtered expression matrix |
| 1 | `task1_sample_metadata.csv` | Sample conditions (Tumor/Normal) |
| 1 | `task1_true_modules.csv` | Ground truth module assignments |
| 2 | `task2_correlation_matrix.csv` | Gene-gene Pearson correlation matrix |
| 2 | `task2_adjacency_matrix.csv` | Soft-thresholded adjacency matrix |
| 3 | `task3_module_assignments.csv` | Detected module assignments |
| 3 | `task3_hub_genes.csv` | Hub gene analysis with connectivity scores |
| 3 | `task3_tom_matrix.csv` | Topological Overlap Matrix |
| 4 | `task4_network_full.png` | Full network visualization |
| 4 | `task4_dendrogram.png` | Hierarchical clustering dendrogram |
| 4 | `task4_correlation_heatmap.png` | Module-ordered correlation heatmap |
| 5 | `task5_enrichment_results.csv` | Full enrichment analysis results |
| 5 | `task5_module_summary.csv` | Module characterization summary |
| 5 | `task5_interpretation.json` | Structured biological interpretation |

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
