"""
Exercise 1 — Building a Neighbor-Joining tree

Instructions (to follow in the lab):
1. Reuse sequences from previous labs (FASTA from Lab 2 or FASTQ→FASTA from Lab 3).
2. If you only have single-sequence FASTA files, combine at least 3 into a multi-FASTA file.
3. Save the multi-FASTA file in: data/work/<handle>/lab04/your_sequences.fasta
4. Complete the steps below:
   - load the multi-FASTA file,
   - compute the distance matrix,
   - build the NJ tree,
   - save the result in Newick format (.nwk).
"""

from pathlib import Path
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

if __name__ == "__main__":
    # TODO 1: Load your multi-FASTA file
    fasta = Path("data/work/<handle>/lab04/your_sequences.fasta")

    # Example (uncomment after replacing <handle>):

    # TODO 2: Compute the distance matrix

    # TODO 3: Build the NJ tree

    # TODO 4: Save the tree in Newick format

    # TODO 5: Visualize the tree
