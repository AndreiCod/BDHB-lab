# Week 2 — Alignment Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Pairwise distances
- Computed Hamming/p-distance across `NG_017013.2`, `NC_060941.1`, and `NC_000017.11` using equal-length windows (32,772 bp for gene↔chromosome, 83,257,441 bp for chromosome↔chromosome) per `Task1_distances.ipynb`.
- The closest sequences are the two chromosome builds (`NC_060941.1` vs. `NC_000017.11`, p-distance 0.7471; see `labs/02_alignment/assignments/artifacts/task1_pairwise_distances.csv`) because both represent chromosome 17 telomere-to-telomere assemblies, so even after trimming they retain the same telomeric and subtelomeric repeat structure, whereas the shorter RefSeqGene slice shares little overlap and therefore looks maximally distant.

## Task 2 — Pairwise alignments
- Aligned the trimmed RefSeqGene slice (`NG_017013.2`) against the CHM13 chromosome sequence (`NC_060941.1`) with `match=2`, `mismatch=-1`, `gap_open=-2`, `gap_extend=-0.5`. The global alignment (score 1237.5; `artifacts/task2_global_alignment.txt`) spreads across ~3.3 kb and introduces hundreds of gaps to keep the long `CTAACC` telomeric runs in register, which obscures the biologically relevant promoter/exon blocks.
- The local alignment (score 1244; `artifacts/task2_local_alignment.txt`) collapses onto the 5' TP53 promoter, yielding a contiguous ~540 bp hit with far fewer gaps. A representative fragment lifted from `artifacts/task2_fragment.csv` shows the local match staying compact while the global run forces extra gaps around the same letters:
  ```text
  Local : CT--CCTTGGTTCAAGTAATTCT---CCTG-CCTCAGACTCCAGAGTAGCTGGGATTACAGGCGCCC
  Global: -T--CCTTGGTTCAAGTAATTCT---CCTG-CCTCAGACTCCAGAGTAGCTGGGATTACAGGCGCCC
  ```

## Task 3 — Online MSA
- Exported a TP53-focused FASTA (`artifacts/task3_subset_for_msa.fasta`) containing the RefSeqGene slice plus the reverse-complemented TP53 windows from CHM13 and GRCh38, then ran MUSCLE (`artifacts/task3_msa_result.fasta`).
- The alignment shows a perfectly conserved GC-rich promoter motif (`GGGATTACAGGCGTGAGCCACCGTGCCTGGCCCTGGAT`) across all three sequences, confirming that both chromosome assemblies retain the same regulatory sequence once oriented to the gene. Excerpt:
  ```text
  NC_000017.11  CTCCTTGGTTCAAGTAATTCTCCTGCCTCAGACTCCAGAGTAGCTGGGATTACAGGCGCC
  NC_060941.1   CTCCTTGGTTCAAGTAATTCTCCTGCCTCAGACTCCAGAGTAGCTGGGATTACAGGCGCC
  NG_017013.2   CTCCTTGGTTCAAGTAATTCTCCTGCCTCAGACTCCAGAGTAGCTGGGATTACAGGCGCC
  ```
- Seeing all three sequences stacked makes it obvious when a base differs or is unresolved; this is much faster than comparing pairwise alignments sequentially and is how I verified that the RefSeqGene annotation still matches both chromosome builds at the TP53 locus.

## Bonus — Semiglobal alignment
- The semiglobal demo (`artifacts/task3_semiglobal_alignment.txt`) reuses the TP53 slice and the chromosome window but turns off end-gap penalties so the telomeric overhangs in the chromosome and the truncated gene boundary are ignored.
- This mode is preferable whenever one sequence is an internal contig or transcript (missing leading/trailing context) while the other is a chromosome-scale scaffold—e.g., stitching cDNA back to a genome or comparing an assembly contig that still carries extra `CTAACC` repeats at its tips.
