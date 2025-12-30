# Lab 03 — Formats & NGS Notes

## Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)

## FASTQ Source

- **Accession**: ERR000001
- **ENA Link**: https://www.ebi.ac.uk/ena/browser/view/ERR000001
- **Description**: Illumina Genome Analyzer sequencing run from the 1000 Genomes Project

## QC Results Summary

| Metric       | Value     |
|--------------|-----------|
| Reads        | 1,170,794 |
| Mean length  | 36.00 bp  |
| N rate       | 0.0002    |
| Mean Phred   | 38.54     |

## Reflection: Why is data quality verification essential before variant analysis?

Data quality verification is a critical step before variant analysis for several important reasons:

1. **Accuracy of variant calls**: Low-quality reads with high error rates can lead to false-positive variant calls. By filtering out or trimming poor-quality bases, we reduce the risk of calling sequencing errors as true variants.

2. **N-bases indicate ambiguity**: A high proportion of 'N' bases (unknown nucleotides) indicates regions where the sequencer could not confidently determine the base. These ambiguous positions can mask true variants or introduce artifacts.

3. **Phred scores quantify confidence**: The Phred quality score (Q = -10 × log₁₀(P_error)) directly indicates base-calling accuracy. A Phred score of 30 means 1 in 1000 chance of error, while 40 means 1 in 10,000. High mean Phred scores (like 38.54 in our data) indicate reliable sequencing.

4. **Read length affects alignment**: Short or variable-length reads may align ambiguously to multiple genomic locations, complicating variant detection. Understanding read length distribution helps in selecting appropriate alignment parameters.

5. **Resource optimization**: Filtering low-quality data early reduces computational burden in downstream analysis (alignment, variant calling, annotation) and produces cleaner results.

In summary, QC ensures that the biological signal (true variants) is distinguished from technical noise (sequencing errors), which is fundamental for any meaningful genomic analysis.

## AI usage
Github Copilot was used in agent mode to do this assignment. All code was reviewed and edited by the student to ensure correctness and understanding.