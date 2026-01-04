# Week 2 — Alignment Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Pairwise distances
- Computed p-distance across three TP53 transcripts: Human (`NM_000546.6`), Mouse (`NM_011640.3`), and Zebrafish (`NM_131327.2`) using truncation to minimum length per `Task1_distances.ipynb`.
- Results (see `artifacts/task1_pairwise_distances.csv`):
  | Pair | used_len | p-distance |
  |------|----------|------------|
  | Human–Mouse | 1781 bp | 0.722 |
  | Human–Zebrafish | 2233 bp | 0.753 |
  | Mouse–Zebrafish | 1781 bp | 0.726 |
- The closest pair is **Human vs Mouse** (p-distance 0.722) because both are mammals sharing ~75 million years of common ancestry, while zebrafish diverged ~450 million years ago. The TP53 tumor suppressor is highly conserved across vertebrates, but mammalian sequences retain more similarity in UTR regions.

## Task 2 — Pairwise alignments
- Aligned Human (`NM_000546.6`) vs Mouse (`NM_011640.3`) TP53 transcripts (trimmed to 3000 bp) with `match=2`, `mismatch=-1`, `gap_open=-2`, `gap_extend=-0.5`.
- Global alignment (score 2010; `artifacts/task2_global_alignment.txt`) spans the full length, forcing gaps throughout to maintain end-to-end correspondence even in divergent UTR regions.
- Local alignment (score 2107.5; `artifacts/task2_local_alignment.txt`) focuses on the best-matching region, typically the conserved coding sequence.
- Fragment comparison from `artifacts/task2_fragment.csv` (first 60 bp of seq1):
  ```text
  Local : CT--CAAAAGT-CTAG-AGCCACCGTCCA--GGGAGCA...
  Global: ------AAAGT-CTAG-AGCCACCGTCCA--GGGAGCA...
  ```
  The local alignment starts at `CT--CAAAAGT` (position 1), finding the best-scoring region immediately, while global starts with `------AAAGT` (6 leading gaps) to maintain strict end-to-end positional correspondence even when the 5' UTR regions diverge significantly.

## Task 3 — Online MSA (automated via EBI REST API)
- Three TP53 transcripts submitted to Clustal Omega via EBI REST API (`https://www.ebi.ac.uk/Tools/services/rest/clustalo`).
- MSA result saved as `artifacts/task3_msa_result.clustal`; 584 fully conserved positions identified across all three species (score=1.0 in `task3_conserved_blocks.csv`).
- Conserved regions include the p53 DNA-binding domain and transactivation domain under strong purifying selection. The `task3_conserved_excerpt.fasta` contains a representative highly-conserved segment.
- MSA helps interpretation by showing conservation patterns across all three species simultaneously, making it easier to identify functionally important motifs than sequential pairwise comparisons.

## Bonus — Semiglobal alignment
- The semiglobal demo (`artifacts/task3_semiglobal_alignment.txt`, score 2257) aligns Human vs Mouse transcripts without penalizing end gaps.
- Semiglobal is preferred when sequences have different lengths or when comparing a shorter fragment (e.g., a PCR amplicon or partial transcript) against a full-length reference—the algorithm finds the best internal match without forcing artificial gaps at the termini.
