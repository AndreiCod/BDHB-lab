# Week 7 Assignment Workbooks

This folder hosts Jupyter notebooks that implement the Week 7 Gene Co-Expression Networks, Visualization & Diseasome assignment without touching the `submissions/` exercises. Each notebook focuses on one deliverable so they can be executed independently and exported into the Moodle ZIP bundle.

## Notebooks

- `Task1_preprocessing.ipynb` — loads the TP53-associated expression data, applies log2(x+1) transformation, and filters low-variance genes.
- `Task2_network_modules.ipynb` — constructs the correlation matrix, builds the adjacency matrix, detects modules using Louvain, and exports `modules_tp53_AndreiCod.csv`.
- `Task3_visualization.ipynb` — visualizes the network with NetworkX, colors nodes by module, highlights hub genes, and exports `network_tp53_AndreiCod.png` and `hubs_tp53_AndreiCod.csv`.
- `Task4_enrichment.ipynb` — performs GO/KEGG enrichment analysis on one module and prepares data for the biological interpretation report.

All notebooks assume the Lab 6 data lives under `data/work/AndreiCod/lab06/`. Run them from the repo root so relative paths stay consistent.

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
