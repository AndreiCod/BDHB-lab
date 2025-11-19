"""
Demo 01 — FASTQ Quality Control (QC)

This script demonstrates how we can read a FASTQ file and compute simple statistics:
- total number of reads
- mean read length
- proportion of 'N' bases
- approximate mean Phred score

Input data: a small FASTQ file from data/sample/ (e.g., sample.fastq)
"""

from Bio import SeqIO

fastq_file = "data/sample/sample.fastq"  # replace with the path to your FASTQ file

num_reads = 0
total_length = 0
total_n = 0
total_phred = 0
total_bases = 0

for record in SeqIO.parse(fastq_file, "fastq"):
    num_reads += 1
    seq = str(record.seq)
    total_length += len(seq)
    total_n += seq.count("N")
    # quality scores
    phred_scores = record.letter_annotations["phred_quality"]
    total_phred += sum(phred_scores)
    total_bases += len(phred_scores)

len_mean = total_length / num_reads if num_reads > 0 else 0
n_rate = total_n / total_length if total_length > 0 else 0
phred_mean = total_phred / total_bases if total_bases > 0 else 0

print(f"Reads: {num_reads}")
print(f"Mean length: {len_mean:.2f}")
print(f"N rate: {n_rate:.4f}")
print(f"Mean Phred: {phred_mean:.2f}")
