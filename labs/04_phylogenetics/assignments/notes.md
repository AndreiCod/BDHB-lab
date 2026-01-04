# Week 4 — Phylogenetics Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Distance Matrix
- Fetched 10 TP53 sequences from NCBI Entrez (Human, Mouse, Zebrafish, Dog, Pig, Cattle, Chicken, Rat, Chimpanzee, Rhesus) per `Task1_distances.ipynb`.
- Ran MSA (Clustal Omega via EBI REST API) before computing distances.
- Computed p-distance from aligned sequences and saved to `artifacts/task1_distance_matrix.csv`.
- Key distances:

  | Comparison | Distance |
  |------------|----------|
  | Human-Chimpanzee | 0.002 |
  | Human-Rhesus | 0.049 |
  | Mouse-Rat | 0.118 |
  | Pig-Cattle | 0.155 |
  | Chicken-Human | 0.439 |
  | Zebrafish-Human | 0.488 |

## Task 2 — Neighbor-Joining Tree
- Built NJ tree using Biopython's `DistanceTreeConstructor` per `Task2_nj_tree.ipynb`.
- Tree saved to `artifacts/task2_nj_tree.nwk`.
- Tree statistics:

  | Metric | Value |
  |--------|-------|
  | Terminal nodes | 10 |
  | Internal nodes | 8 |
  | Total tree length | 1.531 |
  | Mean branch length | 0.090 |

## Task 3 — MSA Comparison
- Reused MSA from Task 1 per `Task3_msa_comparison.ipynb`.
- Conservation analysis (≥90% threshold):

  | Metric | Value |
  |--------|-------|
  | Total alignment positions | 1859 bp |
  | Non-gap positions | 1473 bp |
  | Conserved positions | 601 (32.3%) |
  | Mean conservation score | 0.756 |
  | Conserved blocks (≥10bp) | 5 |

- Top conserved blocks: positions 788-801 (14bp), 842-855 (14bp), 1037-1047 (11bp).

## Bonus — Visualization
- Generated tree visualization using matplotlib per `Task4_visualization.ipynb`.
- PNG and PDF saved to `artifacts/task4_tree_plot.png` and `artifacts/task4_tree_plot.pdf`.

## Reflection
A phylogenetic tree provides evolutionary relationships, branching order, and branch lengths that a distance matrix alone cannot convey. Trees allow inference of common ancestry and divergence timing.
