# Week 5 — Clustering and Phylogenetics Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Radu Bals (BalsRadu)


## Task 1 — Clustering Methods
- Applied three clustering methods on Lab 4 TP53 orthologs (10 species) per `Task1_clustering_methods.ipynb`.
- Used MSA-based distance matrix from Lab 4 (Clustal Omega alignment).

### Results Summary

| Method | Parameters | Silhouette |
|--------|-----------|------------|
| K-means | K=2 | 0.447 (best) |
| K-means | K=3 | 0.441 |
| K-means | K=4 | 0.355 |
| DBSCAN | eps=0.2, min_samples=2 | 0.443 |
| Hierarchical | average linkage, K=2 | — |

- Hierarchical K=2 separates **Zebrafish** (Cluster 2) from all mammals + Chicken (Cluster 1).
- DBSCAN with small eps identifies Zebrafish/Chicken as noise; larger eps merges all into one cluster.

## Task 2 — Phylogenetic Integration
- Loaded NJ tree from Lab 4 per `Task2_phylo_integration.ipynb`.
- Compared clusters with tree clades using ARI and NMI.

| Metric | Value |
|--------|-------|
| Adjusted Rand Index | -0.087 |
| Normalized Mutual Information | 0.111 |
| Tree terminals | 10 |
| Total tree length | 1.531 |

- Low ARI reflects that K=2 clustering doesn't capture finer tree structure (primates, rodents, ungulates).

## Reflection Questions

### How do clustering results align with the phylogenetic tree?
- K=2 captures the deepest split (mammals vs Zebrafish) but misses intermediate groupings.
- Key distances: Human-Chimp = 0.002, Human-Zebrafish = 0.488.

### What explains the differences?
- Clustering optimizes statistical compactness; phylogenetics models evolutionary divergence.
- Hierarchical clustering most resembles phylogenetic trees (both produce dendrograms).

### Applications
- Disease subtype identification via clonal evolution.
- Gene family analysis comparing paralogs with phylogenetic assignments.
- Microbial community analysis combining OTU clustering with phylogenetic placement.

## Artifacts Generated
- `task1_*.png` — Dendrogram, K-means, DBSCAN visualizations
- `task1_cluster_labels.csv` — All cluster assignments
- `task1_quality_metrics.json` — Silhouette scores for all parameter combinations
- `task2_nj_tree.nwk` — NJ tree (Newick)
- `task2_*.png` — Annotated tree and cluster-clade comparison
- `task2_agreement_metrics.json` — ARI, NMI, tree statistics

## AI Usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
