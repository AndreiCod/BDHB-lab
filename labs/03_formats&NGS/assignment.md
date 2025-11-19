# Week 3 — Assignment (Formats and NGS)

## Objective
Simulate a simplified NGS analysis workflow using programmatic tools (Biopython, requests, or public APIs) and your own files.  
The assignment integrates knowledge about databases, formats, and QC, and links raw data to scientific literature.

---

## Requirements 

### 1) PubMed parsing — **2 pts**
- Write `pubmed_query.py` that:
  - Queries PubMed with `TP53 AND cancer` (max. 5 articles).  
  - Saves the title, authors, and abstract to a file `pubmed_<handle>.txt`.

### 2) FASTA (from Lab 1) — **2 pts**
- Reuse the FASTA file with the TP53 sequence downloaded in Lab 1.  
- Save a copy as `fasta_<handle>.fasta`.

### 3) FASTQ QC — **3 pts**
- Use the code from `ex04_fastq_stats.py` to compute:
  - number of reads, mean length, N proportion, mean Phred score.  
- Use the file stored in `data/work/<handle>/lab03/your_reads.fastq.gz`.  
- Save the report as `qc_report_<handle>.txt`.  
- **If you use the backup FASTQ file:** max **2 pts** (out of 3).

### 4) VCF → PubMed — **3 pts**
- Write `vcf_pubmed.py` that:
  - Reads a VCF file and extracts at least 2 variants.  
  - For each variant:
    - If it has an ID (e.g., `rs12345`) → search PubMed for that rsID.  
    - If it has no ID → search `chr<CHROM>:<POS> AND TP53`.  
  - Save the results as `variants_<handle>.txt`.  
- **If you use the sample VCF file:** max **2 pts**.

---

### Bonus (+1 pt)
- Generate a simple visualization (matplotlib) of the distribution of read lengths and Phred scores, and save it as `qc_plot_<handle>.png`.

---

## Deliverables (upload on Moodle)
Upload a `.zip` file containing:  
- `pubmed_query.py`, `vcf_pubmed.py`, `ex04_fastq_stats.py`  
- `pubmed_<handle>.txt`, `fasta_<handle>.fasta`, `qc_report_<handle>.txt`, `variants_<handle>.txt`  
- `qc_plot_<handle>.png` (optional, bonus)  
- `README.txt` and `notes.pdf`

---

### `README.txt` must include:
- Authors (1–2) + GitHub handles.  
- AI disclosure (what was used, how it was validated).  
- FASTQ source.  

### `notes.pdf` (max 1 page):
- 3–5 sentences: “Why is QC important before variant calling?”  
- 2–3 sentences: how you formulated PubMed searches for variants.
