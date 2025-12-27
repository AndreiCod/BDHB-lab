# Week 4 — Phylogenetics Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Distance Matrix
- Fetched 10 TP53 sequences from NCBI Entrez representing diverse vertebrate species: Human, Mouse, Zebrafish, Dog, Pig, Cattle, Dusky titi, Duck, Chicken, and Lion per `Task1_distances.ipynb`.
- Computed pairwise Hamming and p-distance using equal-length windows (truncated to minimum sequence length) and saved to `artifacts/task1_distance_matrix.csv`.
- Key finding: Mammalian sequences show the lowest pairwise distances (~0.27-0.58), while fish (Zebrafish) shows the highest divergence from mammals (~0.65-0.70), consistent with evolutionary timescales.

## Task 2 — Neighbor-Joining Tree
- Built NJ tree using Biopython's `DistanceTreeConstructor` with identity-based distance model per `Task2_nj_tree.ipynb`.
- Tree saved in Newick format to `artifacts/task2_nj_tree.nwk`.
- Cluster interpretation:

  | Cluster | Species | Branch Length | Interpretation |
  |---------|---------|---------------|----------------|
  | Mammalian | Human, Mouse, Dog, Pig, Cattle, Lion, Dusky titi | Short (0.11-0.35) | Recent common ancestry ~100-300 MYA |
  | Avian | Chicken, Duck | Medium (0.35-0.45) | Bird-mammal divergence ~320 MYA |
  | Fish | Zebrafish | Long (0.50+) | Fish-mammal divergence ~450 MYA |

## Task 3 — MSA Comparison
- Automated Clustal Omega alignment via EBI REST API (initially planned manual web upload, but scripted for reproducibility) per `Task3_msa_comparison.ipynb`.
- Trimmed sequences to 1500bp before alignment.
- Conservation analysis (≥90% threshold):

  | Metric | Value |
  |--------|-------|
  | Total alignment positions | 1837 bp |
  | Conserved positions (≥90%) | 69 (3.8%) |
  | Mean conservation score | 0.507 |
  | Conserved blocks (≥10bp) | 0 |

- **Key observation**: The 90% threshold is strict for divergent species spanning ~450 MY evolution. DNA-binding domain shows higher local conservation, but not long continuous blocks at this threshold.
- **Correlation with NJ tree**: Species with short tree distances show high MSA similarity; fish (longest branch) shows lowest conservation.
- Artifacts: `task3_msa_result.clustal`, `task3_conservation_scores.csv`, `task3_conservation_summary.json`.

## Task 4 — Visualization (Bonus)
- Generated publication-quality tree visualization using matplotlib per `Task4_visualization.ipynb`.
- Tree labels renamed to species common names for clarity.
- PNG (150 dpi) and PDF (vector) saved to `artifacts/task4_tree_plot.png` and `artifacts/task4_tree_plot.pdf`.

## Reflection

### What additional information does a phylogenetic tree offer compared to a simple distance matrix?

1. **Evolutionary Relationships**: While a distance matrix shows pairwise distances, a tree reveals hierarchical relationships and common ancestry—we can trace which species share more recent common ancestors.

2. **Branching Order (Topology)**: The tree shows divergence order that cannot be inferred from a matrix alone. We see that mammals diverged more recently from each other than from birds, which diverged before fish.

3. **Branch Lengths**: Trees encode evolutionary distances in branch lengths, showing relative amounts of evolutionary change along each lineage—not just "how different" but "when they diverged."

4. **Ancestral State Inference**: Trees allow inference of ancestral sequence properties at internal nodes, which is impossible with just a distance matrix.

5. **Visual Communication**: Trees provide intuitive representation of evolutionary history, making it easier to identify patterns like convergent evolution or rapid diversification.
