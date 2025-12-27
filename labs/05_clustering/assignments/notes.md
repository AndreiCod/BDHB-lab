# Week 5 — Clustering and Phylogenetics Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Radu Bals (BalsRadu)


## Task 1 — Clustering Methods
- Applied three clustering methods (Hierarchical, K-means, DBSCAN) on Lab 4 multi-FASTA sequences containing TP53 orthologs from multiple species per `Task1_clustering_methods.ipynb`.
- Computed pairwise p-distance matrix from 10 sequences (Human, Mouse, Zebrafish, and other species).
- Results summary:

| Method | Best Parameters | Silhouette Score |
|--------|-----------------|------------------|
| Hierarchical | average linkage, K=2,3 | N/A (dendrogram-based) |
| K-means | K=2 | 0.0096 |
| DBSCAN | eps=0.2-0.5, min_samples=2 | N/A (all noise) |

- K-means with K=2 provided the highest silhouette score (0.0096), though all scores were low due to high sequence divergence.
- DBSCAN identified all 10 sequences as noise (eps=0.2-0.5), confirming that the sequences are highly divergent with no dense clusters—expected for cross-species TP53 orthologs.

## Task 2 — Phylogenetic Integration
- Built Neighbor-Joining tree from the same Lab 4 sequences using identity-based distances per `Task2_phylo_integration.ipynb`.
- Compared statistical clusters (from Task 1) with phylogenetic clades using Adjusted Rand Index (ARI) and Normalized Mutual Information (NMI).
- Key observations:

| Metric | Value |
|--------|-------|
| Adjusted Rand Index | 0.0407 |
| Normalized Mutual Information | 0.1747 |
| Tree terminals | 10 sequences |
| Internal nodes | 8 |

- The low ARI (0.04) indicates that statistical clusters (based on p-distance) do not closely match phylogenetic clades from the NJ tree.
- This is expected because:
  1. The sequences span multiple species with high divergence
  2. Hierarchical clustering groups by overall similarity, while the NJ tree considers evolutionary models
  3. The distance-based MDS embedding for K-means may not preserve the same structure as the tree

## Reflection Questions

### How do clustering results align with the phylogenetic tree?
- Low agreement (ARI = 0.04, NMI = 0.17) indicates that statistical clusters do not closely correspond to phylogenetic clades.
- This is biologically meaningful: the sequences are highly divergent orthologs (human, mouse, zebrafish, frog, etc.), and distance-based clustering captures different aspects than evolutionary tree structure.
- The NJ tree shows a clear split between mammalian sequences (Human TP53, Mouse Trp53) and other species, but the hierarchical clustering groups based on raw sequence similarity which can be affected by sequence length differences.

### What explains the differences between methods?
- **Clustering vs. Phylogenetics**: Clustering optimizes for statistical compactness (minimum within-cluster distance), while phylogenetics models evolutionary divergence with branch lengths.
- **Method-specific differences**:
  - K-means assumes spherical clusters, which may not capture asymmetric evolutionary divergence.
  - DBSCAN's density-based approach can identify outliers (highly divergent sequences) that phylogenetics still places in the tree.
  - Hierarchical clustering most closely resembles phylogenetic trees (both produce dendrograms).

### Applications of combined clustering and phylogenetics
1. **Disease subtype identification**: Cluster patient tumor samples, then verify if subtypes have distinct evolutionary origins (clonal evolution).
2. **Gene family analysis**: Cluster paralogs by function, compare with phylogenetic ortholog/paralog assignments.
3. **Drug repurposing**: Cluster drugs by target similarity, validate with phylogenetic analysis of target genes across species.
4. **Microbial community analysis**: Cluster OTUs by sequence similarity, compare with phylogenetic placement for taxonomic assignment.

## Artifacts Generated
- `task1_hierarchical_dendrogram.png` — Hierarchical clustering visualization
- `task1_kmeans_comparison.png` — K-means results for K=2,3,4
- `task1_dbscan_comparison.png` — DBSCAN results with varying eps
- `task1_cluster_labels.csv` — All cluster assignments
- `task1_distance_matrix.csv` — Pairwise p-distance matrix
- `task1_quality_metrics.json` — Silhouette scores and parameters
- `task2_nj_tree.nwk` — Neighbor-Joining tree in Newick format
- `task2_annotated_tree.png` — Tree with cluster color annotations
- `task2_cluster_tree_comparison.png` — Side-by-side comparison visualization
- `task2_cluster_clade_comparison.csv` — Cluster vs clade assignments
- `task2_agreement_metrics.json` — ARI, NMI, and tree statistics

## AI Usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
