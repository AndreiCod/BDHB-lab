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
from Bio import AlignIO, Phylo, SeqIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for saving figures
import matplotlib.pyplot as plt


def create_simple_alignment(records):
    """
    Create a simple alignment by padding sequences to the same length.
    For a proper phylogenetic analysis, you would use a tool like MUSCLE or ClustalW.
    This is a simplified approach for demonstration purposes.
    """
    # Find the maximum sequence length
    max_len = max(len(rec.seq) for rec in records)
    
    # Pad sequences with gaps to make them equal length
    aligned_records = []
    for rec in records:
        seq_str = str(rec.seq)
        # Pad with gaps at the end
        padded_seq = seq_str + '-' * (max_len - len(seq_str))
        aligned_rec = SeqRecord(
            Seq(padded_seq),
            id=rec.id,
            description=rec.description
        )
        aligned_records.append(aligned_rec)
    
    return MultipleSeqAlignment(aligned_records)


if __name__ == "__main__":
    # TODO 1: Load your multi-FASTA file
    fasta = Path("data/sample/tp53_dna_multi.fasta")
    
    print(f"Loading sequences from: {fasta}")
    records = list(SeqIO.parse(fasta, "fasta"))
    print(f"Loaded {len(records)} sequences:")
    for rec in records:
        print(f"  - {rec.id}: {len(rec.seq)} bp")
    
    # Create alignment (padding sequences to equal length)
    # Note: For proper phylogenetics, use a real alignment tool like MUSCLE/ClustalW
    alignment = create_simple_alignment(records)
    print(f"\nAlignment created with {len(alignment)} sequences, length {alignment.get_alignment_length()} bp")

    # TODO 2: Compute the distance matrix
    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)
    print("\nDistance Matrix:")
    print(distance_matrix)

    # TODO 3: Build the NJ tree
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(distance_matrix)
    print("\nNeighbor-Joining Tree:")
    Phylo.draw_ascii(tree)

    # TODO 4: Save the tree in Newick format
    output_dir = Path("labs/04_phylogenetics/submissions/AndreiCod")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    tree_file = output_dir / "tree_AndreiCod.nwk"
    Phylo.write(tree, tree_file, "newick")
    print(f"\nTree saved to: {tree_file}")

    # TODO 5: Visualize the tree
    fig, ax = plt.subplots(figsize=(12, 8))
    Phylo.draw(tree, axes=ax, do_show=False)
    ax.set_title("Neighbor-Joining Phylogenetic Tree of TP53 Sequences")
    
    tree_image = output_dir / "tree_AndreiCod.png"
    plt.savefig(tree_image, dpi=150, bbox_inches='tight')
    print(f"Tree visualization saved to: {tree_image}")
    
    print("\nDone!")
