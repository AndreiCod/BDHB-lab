# Week 6 — Gene Co-Expression Networks (GCEs) — Building Modules

## Goals
- Understanding the concept of gene co-expression networks (GCEs).  
- Preprocessing RNA-Seq data (normalization, log transformation, filtering).  
- Computing correlation matrices and building an adjacency matrix.  
- Detecting modules using community detection algorithms (e.g., Louvain).  
- Critical analysis of limitations and interpretive pitfalls.  

---

## Context
After studying clustering in Week 5, we now move to **gene co-expression networks**.  
Clustering groups samples or genes globally, while co-expression networks capture **pairwise relationships** between genes.  
In this first part we will build the network and detect modules. Interpretation and visualization will be addressed in Week 7.  

---

## Hands-on
**Run and complete**  
- `ex07_gce_networks.py` — constructing a co-expression network using RNA-Seq data from breast cancer (GSE115469).  
  - Load and normalize the data.  
  - Apply log transformation and filter low-variance genes.  
  - Compute correlation (Pearson or Spearman).  
  - Apply a threshold to build the adjacency matrix.  
  - Build the graph and detect modules with the **Louvain** algorithm.  
  - Export a `.csv` file mapping gene → module.  

---

## Deliverables
Your PR must contain:
1. File `labs/06_networks/submissions/<github_handle>_notes.md` with:  
   - which correlation metric and threshold you used,  
   - a short reflection: **How does a co-expression network differ from classical clustering?**  
2. Completed script `ex07_gce_networks.py`.  
3. The generated file:  
   ```bash
   labs/06_networks/submissions/<handle>/modules_<handle>.csv
   ```
4. Completion of the PR checklist template.

---

## Next week
- Visualization and interpretation of networks.  
- Identification of hub genes and functional analysis (enrichment).  
- Introduction to the Diseasome concept.  
- [See Week 7 — Visualization & Diseasome](./07_network_viz/README.md)

---

## Skills

- RNA-Seq data preprocessing for network analysis.  
- Building correlation and adjacency matrices.  
- Detecting modules with community detection algorithms.  
- Critical evaluation of networks.  

---

## Resources
- [Lab handout](../../docs/lab_onepagers/06_WGCNA.md)  
- [NetworkX Documentation](https://networkx.org/documentation/stable/)  
- [GEO Accession GSE115469](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE115469)  
- [van Dam et al., Brief Bioinform 2018](htt)
