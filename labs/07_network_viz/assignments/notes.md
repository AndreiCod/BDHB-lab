# Week 7 — Network Visualization & Diseasome Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Data and Preprocessing
- Loaded TP53-associated expression matrix (80 genes × 15 samples) from Lab 6 data per `Task1_preprocessing.ipynb`.
- Applied log2(x+1) transformation to normalize expression values.
- Filtered low-variance genes (threshold=0.5) to retain genes with meaningful expression variation.
- Output saved to `artifacts/task1_preprocessed_expression.csv`.

## Task 2 — Network and Modules
- Constructed gene-gene Spearman correlation matrix per `Task2_network_modules.ipynb`.
- Applied absolute correlation threshold (0.85) to build binary adjacency matrix.
- Built NetworkX graph and detected modules using Louvain community detection.
- Network statistics:
  | Metric | Value |
  |--------|-------|
  | Nodes | 80 |
  | Edges | 593 |
  | Modules | 4 |
  | Density | 0.188 |
- Module distribution:
  | Module | Genes |
  |--------|-------|
  | 0 | 20 |
  | 1 | 20 |
  | 2 | 20 |
  | 3 | 20 |
- Output saved to `artifacts/modules_tp53_AndreiCod.csv`.

## Task 3 — Visualization and Hub Genes
- Visualized network using Spring Layout (Fruchterman-Reingold) with `seed=42` per `Task3_visualization.ipynb`.
- Nodes colored by module membership using `tab10` colormap.
- Hub genes identified by degree centrality; top 10 hubs highlighted with larger nodes.
- Top hub genes:
  | Gene | Degree | Module |
  |------|--------|--------|
  | Gene_55 | 20 | 2 |
  | Gene_25 | 19 | 1 |
  | Gene_35 | 19 | 1 |
  | Gene_34 | 19 | 1 |
  | Gene_32 | 19 | 1 |
- Outputs saved to `artifacts/network_tp53_AndreiCod.png` and `artifacts/hubs_tp53_AndreiCod.csv`.

## Task 4 — Biological Interpretation and Diseasome
- Selected Module 0 (largest module) for enrichment analysis per `Task4_enrichment.ipynb`.
- Exported gene list for g:Profiler (GO/KEGG) to `artifacts/task4_module0_genes.txt`.
- Diseasome context: TP53 is a highly connected node in the human diseasome, linking cancer, aging, and metabolic pathways. Co-expression modules around TP53-associated genes may reveal functional gene groups involved in tumor suppression and DNA repair.

## Visualization Advantages
Visualization provides several key advantages over pure numeric analysis:
- **Pattern Recognition**: Network topology reveals module clustering and inter-module connections not obvious from correlation matrices.
- **Hub Identification**: Visual emphasis on high-degree nodes (hub genes) makes their central role immediately apparent.
- **Communication**: Network figures effectively communicate complex relationships to collaborators.
- **Quality Control**: Visual inspection can reveal unexpected structures or artifacts in the data.
