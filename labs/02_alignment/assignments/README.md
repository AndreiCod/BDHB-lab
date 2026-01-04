# Week 2 Assignment Workbooks

This folder hosts Jupyter notebooks that implement the Week 2 Sequence Alignment assignment. Each notebook focuses on one deliverable so they can be executed independently and exported into the Moodle ZIP bundle.

## Dataset
Uses TP53 transcript sequences from three species:
- Human: `NM_000546.6` (Homo sapiens TP53 mRNA)
- Mouse: `NM_011640.3` (Mus musculus Trp53 mRNA)
- Zebrafish: `NM_131327.2` (Danio rerio tp53 mRNA)

## Notebooks

- `Task1_distances.ipynb` — computes p-distance for all pairs, outputs distance matrix to `artifacts/task1_*.csv`.
- `Task2_pairwise_alignments.ipynb` — runs Biopython global vs local alignments on Human–Mouse pair, outputs to `artifacts/task2_*.txt`.
- `Task3_msa_semiglobal.ipynb` — exports sequences for Clustal Omega MSA and runs semiglobal alignment demo, outputs to `artifacts/task3_*`.

## Running
Execute from the `labs/02_alignment/assignments/` directory:
```bash
jupyter execute Task1_distances.ipynb
jupyter execute Task2_pairwise_alignments.ipynb
jupyter execute Task3_msa_semiglobal.ipynb
```

**Note**: Task 3 automatically submits sequences to the EBI Clustal Omega REST API and retrieves the MSA result. No manual upload required.

All notebooks assume Lab 1 FASTA files live under `data/work/<handle>/lab01/`.

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
