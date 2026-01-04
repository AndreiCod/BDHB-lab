# Week 3 — Formats and NGS Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — PubMed Parsing
- Queried PubMed with `TP53 AND cancer` to retrieve the 5 most recent articles using Biopython's `Bio.Entrez` module per `Task1_pubmed.ipynb`.
- Used `Entrez.esearch()` to find PMIDs matching the query, then `Entrez.efetch()` to retrieve article metadata (title, authors, abstract).
- Results saved to `artifacts/task1_pubmed_results.txt` containing article titles, author lists, and abstracts for downstream literature review.

## Task 2 — FASTA File
- Reused the TP53 human transcript sequence (`NM_000546.6`) from Lab 1's sample data per `Task2_fasta.ipynb`.
- This is the canonical TP53 mRNA transcript variant 1, which encodes the p53 tumor suppressor protein.
- Saved copy as `artifacts/task2_tp53_sequence.fasta` for assignment deliverables.

## Task 3 — FASTQ QC
- Used the FASTQ file downloaded from ENA (ERR000001, https://www.ebi.ac.uk/ena/browser/view/ERR000001) per `Task3_fastq_qc.ipynb`.
- Computed quality metrics using Biopython's `SeqIO.parse()` with the "fastq" format:
  | Metric       | Value     |
  |--------------|-----------|
  | Reads        | 1,170,794 |
  | Mean length  | 36.00 bp  |
  | N rate       | 0.0002    |
  | Mean Phred   | 38.54     |
- The high mean Phred score (38.54) indicates excellent sequencing quality suitable for variant calling.

## Task 4 — VCF → PubMed
- Linked VCF variants to PubMed literature per `Task4_vcf_pubmed.ipynb` using a curated VCF file `data/work/AndreiCod/lab03/tp53_variants.vcf`.
- The VCF contains 3 real TP53 variants curated from ClinVar/dbSNP:
  | Variant | rsID | Clinical Significance |
  |---------|------|----------------------|
  | Pro72Arg | rs1042522 | Benign polymorphism |
  | R175H | rs28934578 | Pathogenic hotspot |
  | Exon 7 | N/A | Position-based search |
- Query formulation strategy:
  1. **Variants with rsID** (e.g., rs1042522): Search PubMed directly with the rsID.
  2. **Variants without rsID**: Search with `chr<CHROM>:<POS> AND TP53`.

## Bonus — Reflection: Why is QC important before variant calling?
- **Accuracy of variant calls**: Low-quality reads with high error rates lead to false-positive variant calls. Filtering or trimming poor-quality bases reduces the risk of calling sequencing errors as true variants.
- **N-bases indicate ambiguity**: A high proportion of 'N' bases indicates regions where the sequencer couldn't confidently determine the base. These ambiguous positions can mask true variants or introduce artifacts.
- **Phred scores quantify confidence**: The Phred quality score (Q = -10 × log₁₀(P_error)) directly indicates base-calling accuracy. A score of 30 means 1 in 1000 chance of error, while 40 means 1 in 10,000.
- **Resource optimization**: Filtering low-quality data early reduces computational burden in downstream analysis and produces cleaner results.
