# Week 9 Assignment Workbooks

This folder hosts Jupyter notebooks that implement the Week 9 Drug Repurposing & Network-based Approaches assignment without touching the `submissions/` exercises. Each notebook focuses on one deliverable so they can be executed independently and exported into the Moodle ZIP bundle.

## Notebooks

- `Task1_dataset_preparation.ipynb` — parses full DrugBank XML v5.1.11 to extract drugs, protein targets, gene names, indications (diseases), and gene-disease associations. Exports `task1_drugs.csv`, `task1_drug_targets.csv`, `task1_drug_diseases.csv`, `task1_gene_diseases.csv`.
- `Task2_network_construction.ipynb` — constructs drug-disease network using NetworkX with 4 node types (Drug, Target, Gene, Disease) and 4 edge types (drug-target, protein-gene, gene-disease, drug-disease). Exports `task2_network.gml`, `task2_network_viz.png`, `task2_network_summary.csv`.
- `Task3_metric_calculations.ipynb` — computes degree centrality, betweenness centrality, clustering coefficient, and drug-disease shortest paths with intermediate node analysis. Exports `task3_centrality_metrics.csv`, `task3_drug_disease_paths.csv`, `task3_hub_targets.csv`.
- `Task4_biological_interpretation.ipynb` — analyzes network properties, interprets hub/bottleneck nodes biologically, proposes diverse drug repurposing candidates with mechanistic justification. Exports `task4_network_summary.txt`, `task4_repurposing_candidates.csv`, `task4_network_properties.csv`.

All notebooks assume DrugBank XML lives under `data/work/AndreiCod/lab08/drugbank.xml`. Run them from the repo root so relative paths stay consistent.

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
