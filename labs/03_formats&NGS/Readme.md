# Week 3 — Formats and Next-Generation Sequencing (NGS)

## Goals
- Understanding the formats used in bioinformatics: **FASTA, FASTQ, SAM, VCF**.  
- Practicing NGS data quality control (QC: read count, length, N-rate, Phred).  
- Becoming familiar with the steps in an NGS analysis workflow.  
- Strengthening the connection between biological data and scientific literature.  

---

## Context
After studying sequence alignment (global and local) in Week 2, we now move to **NGS data**, where we work with millions of short reads stored in FASTQ format. We will learn how to verify data quality and connect the results to scientific articles.

---

## Part 1 — File formats & NGS
**Run**  
- `demo01_fastq_qc.py` — reading a FASTQ file and computing basic statistics (read count, mean length, N-rate, mean Phred score).  
- `demo02_mapping_toy.py` — simplified example of mapping reads to a reference sequence (exact string matching).  

**Complete and run**  
- `ex01_fetch_fastq.py` — short exercise: download **your own FASTQ** (TP53-related) using the ENA API and save it to  
  `data/work/<handle>/lab03/your_reads.fastq.gz`.  
- `ex02_fastq_stats.py` — compute QC on your FASTQ file (accepts `.fastq` or `.fastq.gz`) and save the report in  
  `labs/03_formats&NGS/submissions/<handle>/qc_report_<handle>.txt`.

## Deliverables
Your PR must contain:
1. File `labs/03_formats&NGS/submissions/<github_handle>_notes.md` with:  
   - which FASTQ you used (link or SRA accession),  
   - a short reflection: **Why is data quality verification essential before variant analysis?**  
2. The completed exercise, saved in:  
   ```bash
   labs/03_formats&NGS/submissions/<github_handle>/ex04_fastq_stats.py
   labs/03_formats&NGS/submissions/<github_handle>/qc_report_<handle>.txt
   ```
3. Completion of the PR checklist template.

## Next week

- Phylogenetic trees using sequence distances and multiple alignments.
- From variant analysis to evolutionary relationships.
- [See Week 4 — Phylogenetics](../04_phylogenetics/README.md)

## Skills

- Understanding the difference between FASTA, FASTQ, SAM, VCF.
- Using Biopython to read and process FASTQ files.
- Implementing basic QC checks.
- Connecting NGS data to information from scientific literature.

## Resources

- [Lab handout](../../docs/lab_onepagers/02_alignment.md)
- [FASTQ (Illumina)](https://support.illumina.com/bulletins/2016/04/fastq-files-explained.html)
- [Biopython SeqIO](https://biopython.org/wiki/SeqIO)
- [SAM/VCF format (htslib)](http://samtools.github.io/hts-specs/)
- [SRA Run Selector](https://www.ncbi.nlm.nih.gov/Traces/study/) — search and filter SRA runs.  
- [Entrez Programming Utilities (E-utilities)](https://www.ncbi.nlm.nih.gov/books/NBK25501/) — interface for metadata and links.  
- [NCBI Datasets API](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/) — modern API for sequences and runs.

### **ENA (European Nucleotide Archive)**
- [ENA Browser](https://www.ebi.ac.uk/ena/browser/home) — web interface for genomes and runs.  
- [ENA Portal API (filereport)](https://www.ebi.ac.uk/ena/portal/api/) — programmatic access to FASTQ links.  
- [Biopython Entrez](https://biopython.org/docs/1.75/api/Bio.Entrez.html) — for access to NCBI.
