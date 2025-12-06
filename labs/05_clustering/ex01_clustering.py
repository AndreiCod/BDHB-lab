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
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
from pathlib import Path

# GitHub handle
HANDLE = "AndreiCod"

if __name__ == "__main__":
    # TODO 1: Load dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
    columns = ["ID", "Diagnosis"] + [f"Feature_{i}" for i in range(1, 31)]
    df = pd.read_csv(url, header=None, names=columns)
    print(f"Dataset loaded: {df.shape[0]} samples, {df.shape[1]} columns")

    # TODO 2: Preprocessing
    # - remove the ID column
    df = df.drop(columns=["ID"])
    # - convert Diagnosis to numeric (M=1, B=0)
    df["Diagnosis"] = df["Diagnosis"].apply(lambda x: 1 if x == "M" else 0)
    print(f"Preprocessing done. Diagnosis distribution:\n{df['Diagnosis'].value_counts()}")

    # TODO 3: Standardization
    X = df.drop(columns=["Diagnosis"])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Data standardized with StandardScaler")

    # Directory for results
    output_dir = Path(f"labs/05_clustering/submissions/{HANDLE}")
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    # TODO 4: Hierarchical Clustering
    # - use linkage(X_scaled, method="average")
    # - visualize with dendrogram()
    # - save figure as hierarchical_<handle>.png
    print("\nPerforming Hierarchical Clustering...")
    Z = linkage(X_scaled, method="average")
    
    plt.figure(figsize=(12, 6))
    dendrogram(Z, truncate_mode="lastp", p=30, leaf_rotation=90, leaf_font_size=10)
    plt.title("Hierarchical Clustering Dendrogram (Average Linkage)")
    plt.xlabel("Sample Index or Cluster Size")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.savefig(output_dir / f"hierarchical_{HANDLE}.png", dpi=150)
    plt.close()
    print(f"Saved: hierarchical_{HANDLE}.png")

    # TODO 5: K-means Clustering
    # - apply KMeans with K=2
    # - add labels in df["KMeans_Cluster"]
    # - reduce dimensionality with PCA(n_components=2)
    # - visualize and save plot kmeans_<handle>.png
    print("\nPerforming K-means Clustering (K=2)...")
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X_scaled)
    df["KMeans_Cluster"] = kmeans_labels
    
    # Dimensionality reduction for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    print(f"PCA explained variance ratio: {pca.explained_variance_ratio_}")
    
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels, cmap="viridis", s=50, alpha=0.7)
    plt.title("K-means Clustering (K=2) - PCA Visualization")
    plt.xlabel(f"PCA 1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
    plt.ylabel(f"PCA 2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
    plt.colorbar(scatter, label="Cluster")
    plt.tight_layout()
    plt.savefig(output_dir / f"kmeans_{HANDLE}.png", dpi=150)
    plt.close()
    print(f"Saved: kmeans_{HANDLE}.png")

    # TODO 6: DBSCAN Clustering
    # - apply DBSCAN (e.g., eps=1.5, min_samples=5)
    # - add labels in df["DBSCAN_Cluster"]
    # - visualize and save plot dbscan_<handle>.png
    print("\nPerforming DBSCAN Clustering (eps=1.5, min_samples=5)...")
    dbscan = DBSCAN(eps=1.5, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X_scaled)
    df["DBSCAN_Cluster"] = dbscan_labels
    
    n_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
    n_noise = list(dbscan_labels).count(-1)
    print(f"DBSCAN found {n_clusters} clusters and {n_noise} noise points")
    
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=dbscan_labels, cmap="viridis", s=50, alpha=0.7)
    plt.title(f"DBSCAN Clustering (eps=1.5, min_samples=5) - PCA Visualization\n{n_clusters} clusters, {n_noise} noise points")
    plt.xlabel(f"PCA 1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
    plt.ylabel(f"PCA 2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
    plt.colorbar(scatter, label="Cluster (-1 = noise)")
    plt.tight_layout()
    plt.savefig(output_dir / f"dbscan_{HANDLE}.png", dpi=150)
    plt.close()
    print(f"Saved: dbscan_{HANDLE}.png")

    # TODO 7: Save results
    # save a CSV with columns ["Diagnosis", "KMeans_Cluster", "DBSCAN_Cluster"]
    # to clusters_<handle>.csv
    result_df = df[["Diagnosis", "KMeans_Cluster", "DBSCAN_Cluster"]]
    result_df.to_csv(output_dir / f"clusters_{HANDLE}.csv", index=False)
    print(f"\nSaved: clusters_{HANDLE}.csv")
    
    print("\n=== Clustering Analysis Complete ===")
    print(f"All outputs saved to: {output_dir}")
