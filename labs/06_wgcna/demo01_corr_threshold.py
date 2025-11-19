"""
Demo — Computing correlation and thresholding on toy data

This demo shows how to compute a correlation matrix between genes
and how to apply a threshold to obtain a simple adjacency matrix.
"""

import pandas as pd
import numpy as np

# Toy expression matrix (3 genes x 5 samples)
data = {
    "Sample1": [5, 3, 8],
    "Sample2": [4, 3, 9],
    "Sample3": [6, 2, 7],
    "Sample4": [5, 4, 10],
    "Sample5": [4, 3, 8],
}
df = pd.DataFrame(data, index=["GeneA", "GeneB", "GeneC"])
print("Expression matrix (toy):")
print(df)

# Spearman correlation between genes
corr = df.T.corr(method="spearman")
print("\nCorrelation matrix (Spearman):")
print(corr)

# Threshold on correlation (e.g., 0.7)
threshold = 0.7
adjacency = (corr >= threshold).astype(int)
np.fill_diagonal(adjacency.values, 0)  # no self-loops

print(f"\nAdjacency matrix with threshold {threshold}:")
print(adjacency)
