# Assignment Gene Co-Expression Networks, Visualization & Diseasome

## Objectives
- building gene co-expression networks (GCEs),  
- detecting modules,  
- visualizing and identifying hub genes,  
- biological validation through enrichment analysis,  

---

## Tasks

### 1. Data and Preprocessing (2p)
- Reuse the TP53-associated dataset from **Lab 3**.  
- Preprocess the data:
  - log2(x+1),  
  - filter genes with low variance.  

### 2. Network and Modules (3p)
- Construct the correlation matrix (Pearson or Spearman).  
- Apply a threshold to obtain the adjacency matrix.  
- Build the graph and detect modules using the **Louvain** algorithm.  
- Export `modules_tp53_<handle>.csv` (gene → module).  

### 3. Visualization and Hub Genes (3p)
- Visualize the network using **NetworkX** or an external tool (Cytoscape/Gephi).  
- Color nodes by module.  
- Highlight hub genes.  
- Export `network_tp53_<handle>.png`.  
- Export `hubs_tp53_<handle>.csv`.  

### 4. Biological Interpretation and Diseasome (2p)
- Choose **one module** and perform enrichment analysis (GO/KEGG) using g:Profiler or DAVID.  
- Write a short report (max 2 pages PDF) that includes:
  - a description of the module and its hub genes,  
  - the enrichment results,  
  - a reflection: *How might this module integrate into a diseasome context?*  

### Bonus (+1p)
- Compare the visualizations between NetworkX and Cytoscape/Gephi (screenshot + observations).  

---

## Deliverables
Upload in a PR a `.zip` file containing:
- `modules_tp53_<handle>.csv`  
- `network_tp53_<handle>.png`  
- `hubs_tp53_<handle>.csv`  
- The code used (`.py` or `.ipynb`)  
- `report_<handle>.pdf` (max 2 pages, with interpretation and diseasome discussion)  
