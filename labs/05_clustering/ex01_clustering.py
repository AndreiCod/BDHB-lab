"""
Exercise 6 — Clustering on breast cancer data (toy dataset)

Instructions:
1. Load the WDBC breast cancer dataset from the UCI Repository.
2. Preprocess the data: remove irrelevant columns and convert diagnosis to numeric values.
3. Standardize the data.
4. Implement and visualize clustering using:
   - Hierarchical clustering (dendrogram),
   - K-means (K=2, PCA visualization),
   - DBSCAN (PCA visualization).
5. Save results in submissions/<handle>/:
   - clusters_<handle>.csv
   - hierarchical_<handle>.png
   - kmeans_<handle>.png
   - dbscan_<handle>.png
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# Optional: you may import necessary functions now
# from scipy.cluster.hierarchy import dendrogram, linkage
# from sklearn.cluster import KMeans, DBSCAN
# from sklearn.decomposition import PCA

if __name__ == "__main__":
    # TODO 1: Load dataset

    # TODO 2: Preprocessing
    # - remove the ID column

    # TODO 3: Standardization
    X = df.drop(columns=["Diagnosis"])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Directory for results
    output_dir = Path("labs/05_clustering/submissions/<handle>")
    output_dir.mkdir(parents=True, exist_ok=True)

    # TODO 4: Hierarchical Clustering
    # - use linkage(X_scaled, method="average")
    # - visualize with dendrogram()
    # - save figure as hierarchical_<handle>.png

    # TODO 5: K-means Clustering
    # - apply KMeans with K=2
    # - add labels in df["KMeans_Cluster"]
    # - reduce dimensionality with PCA(n_components=2)
    # - visualize and save plot kmeans_<handle>.png

    # TODO 6: DBSCAN Clustering
    # - apply DBSCAN (e.g., eps=1.5, min_samples=5)
    # - add labels in df["DBSCAN_Cluster"]
    # - visualize and save plot dbscan_<handle>.png

    # TODO 7: Save results
    # save a CSV with columns ["Diagnosis", "KMeans_Cluster", "DBSCAN_Cluster"]
    # to clusters_<handle>.csv
