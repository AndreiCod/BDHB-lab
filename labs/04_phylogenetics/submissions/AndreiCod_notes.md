# Lab 04 - Phylogenetics Notes

**Authors:** Andrei Daha, Bals Radu
**Date:** December 6, 2025

## Reflection

### What additional information does a phylogenetic tree offer compared to a simple distance matrix?

A phylogenetic tree provides several key advantages over a simple distance matrix:

1. **Evolutionary Relationships**: While a distance matrix only shows pairwise distances between sequences, a phylogenetic tree reveals the hierarchical relationships and common ancestry. We can see which sequences are more closely related to each other and infer their evolutionary history.

2. **Branching Order (Topology)**: The tree shows the order in which lineages diverged. This topology cannot be directly inferred from a distance matrix alone - we can see which species share a more recent common ancestor.

3. **Branch Lengths**: The tree encodes evolutionary distances in branch lengths, showing not just how different sequences are, but also the relative amount of evolutionary change along each lineage.

4. **Ancestral States**: Trees allow us to infer properties of ancestral sequences (the internal nodes), which is impossible with just a distance matrix.

5. **Visual Interpretation**: Trees provide an intuitive visual representation of evolutionary history, making it easier to communicate findings and identify patterns like convergent evolution or rapid diversification events.

6. **Hypothesis Testing**: Phylogenetic trees can be used to test hypotheses about evolutionary processes, such as molecular clock models or adaptive evolution.

## Implementation Notes

- Used Biopython's `DistanceCalculator` with identity distance model
- Built the tree using the Neighbor-Joining (NJ) algorithm via `DistanceTreeConstructor`
- Sequences were padded to equal length for alignment (in production, use proper alignment tools like MUSCLE/ClustalW)
- The analysis included TP53 sequences from:
  - Human (*Homo sapiens*) - NM_000546.6
  - Mouse (*Mus musculus*) - NM_011640.3
  - Zebrafish (*Danio rerio*) - NM_131327.2

## Results

The Neighbor-Joining tree shows that the human and mouse TP53 sequences are more closely related to each other than to the zebrafish sequence, which aligns with known mammalian vs. fish evolutionary divergence.

## AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.