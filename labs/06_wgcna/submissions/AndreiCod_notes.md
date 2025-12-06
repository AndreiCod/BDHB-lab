# Lab 06 — Gene Co-Expression Networks Notes

**Author**: AndreiCod  
**Date**: December 2024

## Configuration Used

### Correlation Metric
- **Method**: Spearman correlation
- **Reasoning**: Spearman correlation is rank-based and robust to outliers, making it more suitable for gene expression data which often has non-linear relationships and can contain outliers.

### Threshold
- **Adjacency threshold**: 0.85
- **Reasoning**: A high threshold (0.85) ensures that only strongly correlated gene pairs are connected in the network. This helps create clear module separation by keeping only the most reliable co-expression relationships.

### Other Parameters
- **Variance filtering threshold**: 0.1 (log2 scale)
- **Use absolute correlation**: False (using signed correlation to distinguish positive from negative co-expression)
- **Network type**: Undirected (co-expression relationships are symmetric)

## Results Summary
- **Total genes analyzed**: 80
- **Genes after filtering**: 80
- **Network edges**: 593
- **Modules detected**: 4
- **Module sizes**: [20, 20, 20, 20]

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