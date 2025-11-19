"""
Demo 02 — Toy Mapping

We check whether the reads align exactly to a reference sequence through string matching.
This example is NOT a real mapper (it does not support gaps, scoring, etc.).
"""

reference = "ATGCTAGCTAGGCTAATCGGATCGATCGTACGATCG"
reads = [
    "ATGCTAGC",   # match at beginning
    "GATCGATC",   # match in middle
    "TACGATCG",   # match at end
    "GGGGGGGG"    # no match
]

for read in reads:
    pos = reference.find(read)
    if pos != -1:
        print(f"Read {read} mapped at position {pos}")
    else:
        print(f"Read {read} did not map")
