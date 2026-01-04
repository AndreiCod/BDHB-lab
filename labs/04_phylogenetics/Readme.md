# Week 4 — Phylogenetics

## Goals
- Understanding basic concepts in phylogenetics.
- Computing distances between sequences and constructing phylogenetic trees.
- Practicing the **Neighbor-Joining (NJ)** method with Biopython.
- Strengthening the connection between multiple alignments and evolutionary relationships.

---

## Context
After exploring formats and NGS data analysis in Week 3, we now move on to **phylogenetic trees**.
We start from a set of sequences (multi-FASTA), compute a distance matrix, and build an NJ tree.
We will compare the results with an online MSA to observe conserved regions.

---

## Hands-on — Distances and phylogenetic trees
**Run**
- `demo01_distance_matrix.py` — calculation of a distance matrix on a multi-FASTA (Hamming/p-distance).

**Complete and run**
- `ex05_phylo_tree.py` — exercise:
  - save the result as `.nwk` in `labs/04_phylogenetics/submissions/<handle>/tree_<handle>.nwk`.

---

## Deliverables
Your PR must contain:
1. File `labs/04_phylogenetics/submissions/<github_handle>_notes.md` with:
   - which FASTA sequences you used (link/description),
   - a short reflection: **What additional information does a phylogenetic tree offer compared to a simple distance matrix?**
2. The completed exercise, saved in:
   ```bash
   labs/04_phylogenetics/submissions/<github_handle>/ex05_phylo_tree.py
   labs/04_phylogenetics/submissions/<github_handle>/tree_<handle>.nwk
   ```
3. Completion of the PR checklist template.

---

## Next week
- Gene expression clustering and group analysis.
- From evolutionary trees to co-expression modules.
- [See Week 5 — Clustering](../04_phylogenetics/README.md)

---

## Skills
- Computing distance matrices from a multi-FASTA.
- Building and visualizing NJ trees with Biopython.
- Interpreting evolutionary clusters.
- Connecting multiple alignments to phylogenetic relationships.

---

## Resources
- [Lab handout](../../docs/lab_onepagers/04_phylogenetics.md)
- [Biopython Phylo](https://biopython.org/wiki/Phylo)
- [Newick format](http://evolution.genetics.washington.edu/phylip/newicktree.html)
- [Clustal Omega (online MSA)](https://www.ebi.ac.uk/Tools/msa/clustalo/)
- [Multiple Sequence Alignment in Biopython](https://biopython.org/wiki/AlignIO)
