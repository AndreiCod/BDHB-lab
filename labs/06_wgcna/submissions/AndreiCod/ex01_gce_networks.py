"""
Exercise — Gene Co-Expression Networks (GCEs) — Building the network and detecting modules

Objective:
- Build a co-expression network from an RNA-Seq expression matrix
- Detect gene modules (communities) using a Louvain-like algorithm (or alternative)

Instructions (in the lab):
1) Data preparation
   - Download and prepare the expression matrix (e.g., GSE115469) into a CSV with:
     * rows = genes (index), columns = samples (sample IDs)
   - Save the file to: data/work/<handle>/lab06/expression_matrix.csv

2) Preprocessing
   - log2(x + 1)
   - filter low-variance genes

3) Correlation → Adjacency
   - complete the `correlation_matrix` function
   - the function `adjacency_from_correlation` is already implemented

4) Graph + Modules
   - build the graph with NetworkX
   - detect modules (Louvain or alternative)
   - export the gene → module mapping to submissions/<handle>/modules_<handle>.csv

Note:
- Document in <github_handle>_notes.md: correlation metric, threshold, short observations.

Data source:
- GSE115469: Single cell RNA sequencing of human liver (MacParland et al., Nat Commun 2018)
- Downloaded from: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE115nnn/GSE115469/suppl/GSE115469_Data.csv.gz
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import networkx as nx
import numpy as np
import pandas as pd

# --------------------------
# Config — fill in as needed
# --------------------------
HANDLE = "AndreiCod"

# Use the real GSE115469 data
GEO_DATA_CSV = Path(f"data/work/{HANDLE}/lab06/GSE115469_Data.csv")
OUTPUT_DIR = Path(f"labs/06_wgcna/submissions/{HANDLE}")
OUTPUT_CSV = OUTPUT_DIR / f"modules_{HANDLE}.csv"
EXPR_MATRIX_CSV = OUTPUT_DIR / f"expression_matrix_{HANDLE}.csv"  # Processed matrix

CORR_METHOD = "spearman"  # "pearson" or "spearman"
VARIANCE_THRESHOLD = (
    0.5  # threshold for filtering genes (on log2 scale) - higher for real data
)
ADJ_THRESHOLD = 0.5  # threshold for |cor| - adjusted for real single-cell data
USE_ABS_CORR = True  # Use absolute correlation for co-expression networks
MAKE_UNDIRECTED = True  # co-expression networks are usually undirected

# Filtering parameters for single-cell data
MIN_CELLS_EXPRESSED = 100  # Gene must be expressed in at least this many cells
TOP_VARIABLE_GENES = 500  # Select top N most variable genes for network construction


def get_repo_root() -> Path:
    """Get the repository root directory."""
    # Navigate from labs/06_wgcna/submissions/AndreiCod/ to repo root
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent.parent.parent.parent


def load_and_preprocess_geo_data(
    geo_csv: Path, min_cells: int = 100, top_genes: int = 500
) -> pd.DataFrame:
    """
    Load GSE115469 single-cell RNA-seq data and preprocess for co-expression analysis.

    Since this is single-cell data, we:
    1. Filter genes expressed in too few cells
    2. Select top variable genes
    3. Return the expression matrix (genes x cells)
    """
    print(f"Loading GSE115469 data from: {geo_csv}")

    # Load data (genes as rows, cells as columns)
    df = pd.read_csv(geo_csv, index_col=0)
    print(f"  Raw data: {df.shape[0]} genes x {df.shape[1]} cells")

    # Filter genes expressed in at least min_cells
    genes_expressed = (df > 0).sum(axis=1)
    df_filtered = df[genes_expressed >= min_cells]
    print(f"  After filtering (>={min_cells} cells): {df_filtered.shape[0]} genes")

    # Calculate variance for each gene (on log scale)
    df_log = np.log2(df_filtered + 1)
    variances = df_log.var(axis=1)

    # Select top variable genes
    top_var_genes = variances.nlargest(top_genes).index
    df_top = df_filtered.loc[top_var_genes]
    print(f"  Selected top {top_genes} variable genes")

    return df_top


def read_expression_matrix(path: Path) -> pd.DataFrame:
    """Read expression matrix from CSV. Expects genes as rows, samples as columns."""
    df = pd.read_csv(path, index_col=0)
    return df


def log_and_filter(df: pd.DataFrame, variance_threshold: float) -> pd.DataFrame:
    """
    Preprocessing:
    - apply log2(x+1)
    - filter genes with low variance
    """
    # Apply log2(x+1) transformation
    df_log = np.log2(df + 1)

    # Compute variance across samples for each gene
    variances = df_log.var(axis=1)

    # Filter genes with variance above threshold
    df_filtered = df_log[variances >= variance_threshold]

    print("log2(x+1) transformation applied.")
    print(
        f"Filtered genes: {df.shape[0]} -> {df_filtered.shape[0]} (variance threshold: {variance_threshold})"
    )

    return df_filtered


def correlation_matrix(
    df: pd.DataFrame, method: str = "spearman", use_abs: bool = True
) -> pd.DataFrame:
    """
    Compute the gene–gene correlation matrix (rows).
    """
    # Transpose so we correlate genes (originally rows) across samples
    corr = df.T.corr(method=method)

    if use_abs:
        corr = corr.abs()

    print(f"Computed {method} correlation matrix: {corr.shape}")

    return corr


def adjacency_from_correlation(
    corr: pd.DataFrame, threshold: float, weighted: bool = False
) -> pd.DataFrame:
    """
    Build adjacency matrix from correlations.
    - binary: A_ij = 1 if corr_ij >= threshold, else 0
    - weighted: A_ij = corr_ij if corr_ij >= threshold, else 0
    """
    if weighted:
        adj = corr.where(corr >= threshold, 0)
    else:
        adj = (corr >= threshold).astype(int)

    # Remove self-loops
    np.fill_diagonal(adj.values, 0)

    print(f"Adjacency matrix created with threshold {threshold}")
    print(f"  Non-zero edges: {(adj.values > 0).sum() // 2}")

    return adj


def graph_from_adjacency(A: pd.DataFrame, undirected: bool = True) -> nx.Graph:
    if undirected:
        G = nx.from_pandas_adjacency(A)
    else:
        G = nx.from_pandas_adjacency(A, create_using=nx.DiGraph)
    isolates = list(nx.isolates(G))
    if isolates:
        print(f"Removed {len(isolates)} isolated nodes")
        G.remove_nodes_from(isolates)
    return G


def detect_modules_louvain_or_greedy(G: nx.Graph) -> Dict[str, int]:
    """
    Detect communities (modules) and return a dict gene -> module_id.
    Options:
      - try louvain_communities(G, seed=42) if available
      - otherwise greedy_modularity_communities(G)
    """
    try:
        # Try Louvain algorithm (available in NetworkX >= 2.6)
        communities = nx.community.louvain_communities(G, seed=42)
        method = "Louvain"
    except AttributeError:
        # Fall back to greedy modularity
        communities = nx.community.greedy_modularity_communities(G)
        method = "Greedy Modularity"

    print(f"Module detection using {method} algorithm")

    # Convert list of sets to gene -> module_id mapping
    gene_to_module = {}
    for module_id, community in enumerate(communities):
        for gene in community:
            gene_to_module[gene] = module_id

    return gene_to_module


def save_modules_csv(mapping: Dict[str, int], out_csv: Path) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df_modules = pd.DataFrame(
        {"Gene": list(mapping.keys()), "Module": list(mapping.values())}
    ).sort_values(["Module", "Gene"])
    df_modules.to_csv(out_csv, index=False)


if __name__ == "__main__":
    # Get repo root using the correct path calculation
    repo_root = get_repo_root()

    geo_csv = repo_root / GEO_DATA_CSV
    output_csv = repo_root / OUTPUT_CSV
    expr_matrix_csv = repo_root / EXPR_MATRIX_CSV

    print("=" * 60)
    print("Gene Co-Expression Network Analysis")
    print("GSE115469: Human Liver Single-Cell RNA-seq")
    print("=" * 60)

    # Step 1: Load and preprocess GEO data
    print("\nStep 1: Loading and preprocessing GSE115469 data...")
    df_expr = load_and_preprocess_geo_data(
        geo_csv, min_cells=MIN_CELLS_EXPRESSED, top_genes=TOP_VARIABLE_GENES
    )

    # Save the processed expression matrix
    expr_matrix_csv.parent.mkdir(parents=True, exist_ok=True)
    df_expr.to_csv(expr_matrix_csv)
    print(f"  Saved processed matrix to: {expr_matrix_csv}")

    # Step 2: Preprocessing - log transform and filter
    print("\nStep 2: Preprocessing (log2 transform + variance filter)...")
    df_processed = log_and_filter(df_expr, VARIANCE_THRESHOLD)

    # Step 3: Compute correlation matrix
    print("\nStep 3: Computing correlation matrix...")
    corr = correlation_matrix(df_processed, method=CORR_METHOD, use_abs=USE_ABS_CORR)

    # Step 4: Build adjacency matrix
    print("\nStep 4: Building adjacency matrix...")
    adj = adjacency_from_correlation(corr, ADJ_THRESHOLD, weighted=False)

    # Step 5: Build graph
    print("\nStep 5: Building NetworkX graph...")
    G = graph_from_adjacency(adj, undirected=MAKE_UNDIRECTED)
    print(
        f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges."
    )

    # Step 6: Detect modules
    print("\nStep 6: Detecting modules...")
    gene_to_module = detect_modules_louvain_or_greedy(G)
    print(f"Detected {len(set(gene_to_module.values()))} modules.")

    # Step 7: Save results
    print("\nStep 7: Saving results...")
    save_modules_csv(gene_to_module, output_csv)
    print(f"Saved gene→module mapping to: {output_csv}")

    # Summary
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Correlation method: {CORR_METHOD}")
    print(f"  Adjacency threshold: {ADJ_THRESHOLD}")
    print(f"  Number of modules: {len(set(gene_to_module.values()))}")
    module_sizes = {}
    for m in gene_to_module.values():
        module_sizes[m] = module_sizes.get(m, 0) + 1
    print(f"  Module sizes: {sorted(module_sizes.values(), reverse=True)}")
    print("=" * 60)
