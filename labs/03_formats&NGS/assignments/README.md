# Week 3 Assignment Workbooks

This folder hosts Jupyter notebooks that implement the Week 3 Formats & NGS assignment without touching the `submissions/` exercises. Each notebook focuses on one deliverable so they can be executed independently and exported into the Moodle ZIP bundle.

## Notebooks

- `Task1_pubmed.ipynb` — queries PubMed for "TP53 AND cancer" (max 5 articles), saves title, authors, and abstract to `task1_pubmed_results.txt`.
- `Task2_fasta.ipynb` — reuses the TP53 FASTA from Lab 1 and saves a copy as `task2_tp53_sequence.fasta`.
- `Task3_fastq_qc.ipynb` — computes FASTQ QC statistics (reads, mean length, N-rate, mean Phred) and saves to `task3_fastq_qc_report.txt`.
- `Task4_vcf_pubmed.ipynb` — parses `data/work/<handle>/lab03/tp53_variants.vcf` (curated TP53 variants) and searches PubMed for each, saving results to `task4_vcf_pubmed_results.txt`.

All notebooks assume the Lab data lives under `data/work/<handle>/`. Run them from the repo root so relative paths stay consistent.

# AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.
