# Week 4 Assignment Workbooks

This folder hosts Jupyter notebooks that implement the Week 4 Phylogenetics assignment without touching the `submissions/` exercises. Each notebook focuses on one deliverable so they can be executed independently and exported into the Moodle ZIP bundle.

## Notebooks

- `Task1_distances.ipynb` — fetches ≥10 TP53 sequences from NCBI, computes Hamming/p-distance matrix, and saves to `artifacts/task1_distance_matrix.csv`.
- `Task2_nj_tree.ipynb` — builds a Neighbor-Joining tree with Biopython, extracts cluster statistics, and saves tree to `artifacts/task2_nj_tree.nwk`.
- `Task3_msa_comparison.ipynb` — runs Clustal Omega via EBI REST API, analyzes conserved regions, and saves scores to `artifacts/task3_conservation_scores.csv`.
- `Task4_visualization.ipynb` — generates graphical tree visualization using matplotlib and saves to `artifacts/task4_tree_plot.png`.

All notebooks assume the Lab data lives under `data/work/<handle>/`. Run them from the repo root so relative paths stay consistent.

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
