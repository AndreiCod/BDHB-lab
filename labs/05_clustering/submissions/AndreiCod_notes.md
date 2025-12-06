# Clustering Exercise Notes

**Author**: AndreiCod  
**Date**: December 6, 2025

## Dataset

Wisconsin Diagnostic Breast Cancer (WDBC) dataset from UCI Repository:
- 569 samples
- 30 features (computed from digitized images of fine needle aspirate of breast mass)
- Binary classification: Malignant (M=1) vs Benign (B=0)

## Clustering Methods Applied

### 1. Hierarchical Clustering
- Used average linkage method
- Produces a dendrogram showing the hierarchical relationship between samples
- No need to specify number of clusters beforehand

### 2. K-means Clustering (K=2)
- Partition-based clustering with K=2 clusters
- Assumes spherical clusters of similar size
- Fast and efficient for large datasets

### 3. DBSCAN (eps=1.5, min_samples=5)
- Density-based clustering
- Can identify noise points (outliers)
- Does not require specifying number of clusters

## Which Method is Most Appropriate for This Data?

**K-means (K=2)** is the most appropriate method for this dataset because:

1. **Known number of classes**: We know there are exactly 2 classes (Malignant and Benign), matching K=2.
2. **Spherical assumption reasonable**: After PCA visualization, the data shows relatively compact, roughly spherical clusters.
3. **Balanced clusters**: The dataset has a reasonable distribution between classes (~357 Benign, ~212 Malignant).
4. **Computational efficiency**: K-means is faster and more scalable than hierarchical clustering.

DBSCAN might identify noise points but requires careful tuning of epsilon and min_samples. Hierarchical clustering is useful for exploratory analysis but doesn't scale well.

## Reflection: How Does Clustering Compare to Phylogenetic Trees in Discovering Biological Relationships?

Both clustering and phylogenetic trees are methods for discovering relationships in biological data, but they differ fundamentally in their approach and interpretation:

### Similarities
- **Distance-based**: Both can use distance matrices to measure similarity between entities
- **Hierarchical structure**: Hierarchical clustering produces dendrograms similar to phylogenetic trees
- **Pattern discovery**: Both reveal underlying structure in biological data

### Key Differences

| Aspect | Clustering | Phylogenetic Trees |
|--------|------------|-------------------|
| **Purpose** | Group similar samples/features | Infer evolutionary relationships |
| **Interpretation** | Similarity grouping | Evolutionary history/ancestry |
| **Branch lengths** | May represent distance, but no evolutionary meaning | Represent evolutionary time or genetic change |
| **Root** | Often unrooted | Can be rooted to show common ancestor |
| **Data type** | Any numerical features | Typically sequence data (DNA, protein) |
| **Assumptions** | Statistical similarity | Evolutionary models (e.g., molecular clock) |

### Biological Implications

1. **Phylogenetics** assumes that similar sequences share a common ancestor and that divergence follows evolutionary models. The tree represents a hypothesis about evolutionary history.

2. **Clustering** makes no evolutionary assumptions—it simply groups samples based on feature similarity. Two samples in the same cluster may be similar due to:
   - Common ancestry (like phylogenetics)
   - Convergent evolution
   - Similar environmental pressures
   - Shared functional requirements

3. **Complementary use**: In practice, both methods are often used together. Clustering can identify groups of interest, while phylogenetic analysis can determine if those groups share evolutionary history.

### Example in Cancer Research

For the breast cancer dataset:
- **Clustering** groups tumors by their molecular features (cell morphology, size, texture)
- **Phylogenetics** could trace the clonal evolution within a single tumor, showing how cancer cell populations diverged from a common ancestor

Both approaches contribute to understanding cancer biology but answer different questions: clustering asks "which tumors are similar?" while phylogenetics asks "how did these cells evolve?"

## AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.