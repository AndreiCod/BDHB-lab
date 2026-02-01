# Lab 06 — Gene Co-Expression Networks Notes

**Author**: Andrei Daha, Radu Bals
**Date**: December 2024

## Data Source
- **Dataset**: GSE115469 - Single cell RNA sequencing of human liver
- **Reference**: MacParland et al., "Single cell RNA sequencing of human liver reveals distinct intrahepatic macrophage populations", Nat Commun 2018
- **Downloaded from**: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE115nnn/GSE115469/suppl/GSE115469_Data.csv.gz
- **Raw data**: 20,007 genes × 8,444 cells (single-cell RNA-seq)
- **Preprocessing**: Filtered to genes expressed in ≥100 cells, selected top 500 most variable genes

## Configuration Used

### Correlation Metric
- **Method**: Spearman correlation
- **Reasoning**: Spearman correlation is rank-based and robust to outliers, making it more suitable for gene expression data which often has non-linear relationships and can contain outliers. Particularly important for single-cell data which has high dropout rates.

### Threshold
- **Adjacency threshold**: 0.5
- **Reasoning**: A moderate threshold (0.5) balances between keeping meaningful co-expression relationships and avoiding too many isolated nodes. Single-cell data tends to have lower correlation values due to sparsity.

### Other Parameters
- **Variance filtering threshold**: 0.5 (log2 scale)
- **Use absolute correlation**: True (capturing both positive and negative co-expression)
- **Network type**: Undirected (co-expression relationships are symmetric)
- **Minimum cells for gene inclusion**: 100

## Results Summary
- **Total genes analyzed**: 500 (top variable genes)
- **Genes in network**: 255 (245 isolated nodes removed)
- **Network edges**: 13,541
- **Modules detected**: 5
- **Module sizes**: [69, 69, 66, 49, 2]

### Biological Context
The GSE115469 dataset represents the cellular landscape of human liver, including:
- Hepatocytes (parenchymal cells)
- Various immune cell populations (macrophages, T cells, B cells)
- Endothelial cells
- Stellate cells

The detected modules likely correspond to cell-type specific gene expression programs and functional pathways in liver tissue.

## Reflection: How does a co-expression network differ from classical clustering?

### Key Differences

1. **Relationship Representation**:
   - **Clustering**: Groups genes (or samples) into discrete clusters based on overall similarity. Each gene belongs to exactly one cluster, and the relationships between genes are not explicitly modeled.
   - **Co-expression Networks**: Explicitly capture pairwise relationships between genes as edges. This preserves information about which specific genes are co-expressed with each other.

2. **Granularity of Information**:
   - **Clustering**: Loses pairwise relationship information – we only know that genes are in the same cluster, not how strongly they're related.
   - **Networks**: Retain edge weights (correlation strengths), allowing identification of hub genes (highly connected genes) and peripheral genes.

3. **Module Detection vs. Cluster Assignment**:
   - **Clustering**: Uses distance/similarity metrics directly (e.g., k-means, hierarchical clustering).
   - **Networks**: First builds a graph structure, then applies community detection algorithms (e.g., Louvain) that consider network topology.

4. **Biological Interpretation**:
   - **Clustering**: Useful for grouping samples (e.g., patient subtypes) or genes with similar expression profiles.
   - **Networks**: Better suited for identifying regulatory relationships, functional modules, and hub genes that may be key regulators or drug targets.

5. **Scalability to Downstream Analysis**:
   - **Networks**: Enable graph-based analyses like centrality measures, shortest paths, and network propagation for disease gene prioritization.
   - **Clustering**: Primarily provides group membership without additional structural information.

### When to Use Each Approach
- Use **clustering** when you want a simple partition of genes/samples and don't need pairwise relationship details.
- Use **co-expression networks** when you want to study gene-gene relationships, identify hub genes, or perform network-based functional enrichment.

## AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
