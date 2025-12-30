# Lab 2 — Sequence Alignment

## Datasets Used

For the sequence alignment exercises, I used the following datasets:
- TP53 gene sequence which is a well-known tumor suppressor gene represented by the p53 gene.

## Reflection

**When is global alignment preferred over local alignment?**

- Global alignment is preferred when the sequences being compared are of similar length and are expected to be homologous (sharing a common ancestor) across their entire length. This is particularly useful for comparing sequences that are closely related, such as different isoforms of a gene or sequences from closely related species. Global alignment ensures that the entire sequence is aligned, allowing for the identification of conserved regions and overall similarity.

- In contrast, local alignment is more suitable for sequences that may have regions of high similarity interspersed with regions of low similarity or gaps. This is often the case when comparing sequences from distantly related species or when searching for conserved motifs within larger sequences. Local alignment focuses on finding the best matching subsequences, which can be more informative in these scenarios.


## Completed Exercises

The completed exercise files contain the implementations of the Needleman-Wunsch algorithm for global alignment and the Smith-Waterman algorithm for local alignment, respectively.

- `labs/02_alignment/submissions/AndreiCod/ex02_global_nw.py`
- `labs/02_alignment/submissions/AndreiCod/ex03_local_sw.py`

**Note:** The sequences were truncated to a maximum length of 10,000 bases. This was done to ensure the data fits in memory. For both global and local alignments, sequence with indices 0 and 1 from the FASTA file were used.

**Results:**
- Global Alignment Score (Needleman-Wunsch): -1639
- Local Alignment Score (Smith-Waterman): 5080


## AI Methodology
Inline completitions were used to assist in code writing. In the notes file, AI was used to expand on the reflection section regarding the preference of global versus local alignment.