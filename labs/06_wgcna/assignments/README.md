# Week 6 Assignment Workbooks — Gene Co-Expression Networks

This folder hosts Jupyter notebooks that implement the Week 6 Gene Co-Expression Networks assignment. Each notebook focuses on one deliverable so they can be executed independently.

## Dataset

Uses **GSE50081** — Non-Small Cell Lung Cancer (NSCLC) Expression Dataset (Der et al., PLoS ONE 2014):
- **181 tumor samples** (adenocarcinoma + squamous cell carcinoma)
- Affymetrix Human Genome U133 Plus 2.0 Array (GPL570)
- Downloaded from GEO, probe IDs mapped to HUGO gene symbols
- Variance-filtered to top 2000 genes
- **TP53 present** ✓ for tumor-relevant analysis

## Dependencies

```bash
pip install PyWGCNA gseapy GEOparse
```

| Package | Version | Purpose |
|---------|---------|---------|
| **PyWGCNA** | ≥2.0 | Authentic WGCNA implementation (TOM, Dynamic Tree Cut, module eigengenes) |
| **gseapy** | ≥1.0 | Online enrichment via Enrichr (KEGG, GO, Reactome databases) |
| **GEOparse** | ≥2.0 | Download GEO datasets |

## Notebooks

- `Task1_data_preparation.ipynb` — loads GSE50081 NSCLC microarray data, maps probes to gene symbols, applies variance filtering, exports preprocessed matrix.
- `Task2_network_construction.ipynb` — computes Pearson correlation matrix and constructs adjacency matrix using soft-thresholding (power=5).
- `Task3_module_detection.ipynb` — detects gene modules using **PyWGCNA** (authentic WGCNA with TOM + Dynamic Tree Cut), identifies hub genes.
- `Task4_visualization.ipynb` — visualizes the network with WGCNA color-based module coloring, creates dendrograms and correlation heatmaps.
- `Task5_enrichment.ipynb` — performs functional enrichment using **gseapy/Enrichr** (online KEGG/GO/Reactome).

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
| 1 | `task1_expression_preprocessed.csv` | Variance-filtered expression matrix (2001 genes × 181 samples) |
| 1 | `GSE50081_gene_expression.csv` | Downloaded expression data with gene symbols |
| 2 | `task2_correlation_matrix.csv` | Gene-gene Pearson correlation matrix |
| 2 | `task2_adjacency_matrix.csv` | Soft-thresholded adjacency matrix (power=5) |
| 2 | `task2_network_params.csv` | Network construction parameters |
| 3 | `task3_module_assignments.csv` | PyWGCNA module assignments (6 modules, color-named) |
| 3 | `task3_hub_genes.csv` | Hub gene analysis with connectivity scores (60 hubs) |
| 3 | `task3_summary.csv` | Module detection summary statistics |
| 4 | `task4_network_full.png` | Full network visualization with WGCNA module colors |
| 4 | `task4_module_*.png` | Individual module visualizations |
| 4 | `task4_dendrogram.png` | Hierarchical clustering dendrogram |
| 4 | `task4_correlation_heatmap.png` | Module-ordered correlation heatmap |
| 5 | `task5_enrichment_*.csv` | Enrichr results per module (KEGG/GO/Reactome) |
| 5 | `task5_module_summary.csv` | Module characterization summary |

## Key Results

| Module | Size | Function | Key Genes |
|--------|------|----------|-----------|
| **darkgrey** | 625 | Lung adenocarcinoma markers, surfactant metabolism | **TP53**, NKX2-1, SFTPA1, HOPX |
| lightgrey | 600 | Squamous cell markers, epidermis development | TP63, KRT5, DSG3, SPRR1B |
| black | 230 | B-cell signaling, cell cycle | CD19, CD79A, MS4A1 |
| gainsboro | 224 | Chemokine signaling, T-cell activation | CCL5, CXCL9, CD8A |
| whitesmoke | 162 | Inflammatory response, ECM | COL1A1, COL3A1, MMP2 |
| silver | 160 | Coagulation, type I interferon | C3, SERPINA1, F13A1 |

### TP53 Analysis
**TP53 is in the darkgrey module** — the largest module (625 genes) containing lung adenocarcinoma differentiation markers. This makes biological sense:
- TP53 mutations occur in ~50% of NSCLC cases
- Co-expression with surfactant genes (SFTPA1, SFTPB) reflects alveolar type II cell origin
- Module enriched for tight junctions, consistent with TP53's role in epithelial integrity

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
