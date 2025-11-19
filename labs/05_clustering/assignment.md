# Assignment 5 — Clustering and Phylogenetics

## Objective
This assignment extends the lab exercise and challenges you to combine **clustering** with the **phylogenetic analysis** performed in Lab 4.  
You will reuse your dataset and the phylogenetic tree previously created, in order to compare statistical clusters with evolutionary branches.  

---

## Instructions

### Step 1 — Dataset and Phylogenetic Tree
- Reuse the **multi-FASTA dataset** built in Lab 4.  
- Use the saved phylogenetic tree (`tree_<handle>.nwk`) as reference.  

### Step 2 — Clustering
- Preprocess the data: transform it into a **distance/similarity matrix** or feature vectors.  
- Apply at least **two clustering methods**:  
  - Hierarchical (average linkage or another method of your choice)  
  - K-means (test several K values)  
  - DBSCAN (vary eps / min_samples)  
- Evaluate cluster quality using an index (e.g., Silhouette Score).  

### Step 3 — Integration with Phylogenetics
- Compare clusters with tree branches.  
- Analyze whether genes/sequences in the same cluster also appear in the same clade.  
- Discuss observed differences:  
  - overlaps,  
  - discrepancies,  
  - biological hypotheses (e.g., convergent evolution, functional diversification).  

---

## Deliverables
1. **Python code** used for clustering and comparison with the tree.  
2. **Visualizations**:  
   - dendrogram,  
   - PCA plots for clustering,  
   - phylogenetic tree annotated with clusters.  
3. **Short report (`notes.pdf`, max 2 pages)** including:  
   - clustering results,  
   - comparison with the phylogenetic tree,  
   - biological/functional interpretation (see reflection questions).  

---

## Grading
- **Dataset and tree correctly reused** — 1p  
- **Correct application of two clustering methods** — 3p  
- **Clear visualizations (dendrogram, PCA, annotated tree)** — 3p  
- **Comparative analysis: clustering vs phylogenetics** — 2p  
- **Report quality (structure, clarity, critical reflection)** — 1p  
- **Bonus (+1p):** Use 3 clustering methods and discuss differences.  

---

## Reflection Questions
- How do the clustering results align with the phylogenetic tree?  
- What explains the differences observed between methods, and between the tree vs. clustering?  
- How can combining clustering and phylogenetics be useful in other applications (e.g., disease subtype identification, gene families, functional evolution)?
