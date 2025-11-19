# Week 5 — Clustering in Bioinformatics

## Goals
- Understanding basic clustering methods: **Hierarchical, K-means, DBSCAN**.  
- Applying clustering on real biological data.  
- Visualizing and interpreting clusters.  
- Connecting clustering to phylogenetics and advanced applications (drug repurposing, gene co-expression networks).  

---

## Context
After constructing phylogenetic trees in Week 4, we now apply **clustering** methods to discover hidden groups in biological data.  
In the presentation, we will cover both classical methods (Hierarchical, K-means, DBSCAN) and advanced ones (dimensionality reduction, cluster validity indices, probabilistic and fuzzy clustering).  
In the lab, we will implement the basic algorithms on a breast cancer dataset.  

---

## Hands-on
**Run**  
- `demo01_k_means.py` — k-means with PCA visualization  
**Run and complete**  
- `ex01_clustering.py` — clustering on gene expression data from breast cancer (toy dataset).  
  - Standardize the data.  
  - Apply **Hierarchical Clustering** and visualize the dendrogram.  
  - Apply **K-means (K=2)** and visualize results using PCA.  
  - Apply **DBSCAN** and compare the clusters.  
  - Save the generated files (CSV with labels, images with plots).  

---

## Deliverables
Your PR must contain:
1. File `labs/05_clustering/submissions/<github_handle>_notes.md` with:  
   - which method you considered most appropriate for the analyzed data,  
   - a short reflection: **How does clustering compare to phylogenetic trees in discovering biological relationships?**  
2. Completed script `ex06_clustering.py`.  
3. Generated files:  
   ```bash
   labs/05_clustering/submissions/<handle>/clusters_<handle>.csv
   labs/05_clustering/submissions/<handle>/hierarchical_<handle>.png
   labs/05_clustering/submissions/<handle>/kmeans_<handle>.png
   labs/05_clustering/submissions/<handle>/dbscan_<handle>.png
   ```
4. Completion of the PR checklist template.

---

## Next week

- Gene Co-expression Networks.  
- From classic clustering to biological modules and multi-omics integration.  
- [See Week 6 — Gene Co-expression Networks](./06_wgcna/README.md))  

---

## Skills

- Applying Hierarchical, K-means, and DBSCAN to biological data.  
- Dimensionality reduction and cluster visualization (PCA).  
- Comparing and interpreting results across methods.  
- Understanding clustering limitations and the relationship with phylogenetic analysis.  

---

## Resources

- [Lab handout](../../docs/lab_onepagers/05_clustering.md)  
- [Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)  
- [Scipy Hierarchical](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)  
- [PCA in scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)  
- [Drug repurposing with gene-network clustering](../../docs/papers/clustering_paper.pdf)
