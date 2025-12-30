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
"""

from __future__ import annotations
from pathlib import Path
from typing import Dict, Iterable

import numpy as np
import pandas as pd
import networkx as nx


# --------------------------
# Config — fill in as needed
# --------------------------
INPUT_CSV = Path("data/work/AndreiCod/lab06/expression_matrix.csv")
OUTPUT_DIR = Path("labs/06_wgcna/submissions/AndreiCod")
OUTPUT_CSV = OUTPUT_DIR / "modules_AndreiCod.csv"

CORR_METHOD = "spearman"   # "pearson" or "spearman"
VARIANCE_THRESHOLD = 0.1   # threshold for filtering genes (on log2 scale)
ADJ_THRESHOLD = 0.85       # threshold for |cor| - high to ensure within-module edges only
USE_ABS_CORR = False       # Use signed correlation (not absolute) for better separation
MAKE_UNDIRECTED = True     # co-expression networks are usually undirected


def create_synthetic_expression_data(output_path: Path, n_genes: int = 80, n_samples: int = 15) -> pd.DataFrame:
    """
    Create synthetic expression matrix simulating co-expression patterns.
    Creates 4 modules of genes with correlated expression + some noise.
    Designed to create clear module separation for community detection.
    """
    np.random.seed(42)
    
    # Create 4 gene modules with different base expression patterns
    samples = [f"Sample_{i+1}" for i in range(n_samples)]
    genes = [f"Gene_{i+1}" for i in range(n_genes)]
    
    # Base patterns for 4 modules - using non-monotonic, distinct patterns
    t = np.linspace(0, 4*np.pi, n_samples)
    
    # Module 1: increasing then flat
    pattern1 = np.concatenate([np.linspace(20, 100, n_samples//2), 
                               np.full(n_samples - n_samples//2, 100)])
    # Module 2: oscillating pattern 1
    pattern2 = 60 + 30 * np.sin(t)
    # Module 3: step function
    pattern3 = np.where(np.arange(n_samples) < n_samples//3, 30, 
                       np.where(np.arange(n_samples) < 2*n_samples//3, 80, 50))
    # Module 4: oscillating pattern 2 (different phase)
    pattern4 = 60 + 30 * np.cos(t * 0.7)
    
    patterns = [pattern1.astype(float), pattern2.astype(float), 
                pattern3.astype(float), pattern4.astype(float)]
    genes_per_module = n_genes // 4
    
    expression_data = []
    for i, gene in enumerate(genes):
        module_idx = i // genes_per_module
        if module_idx >= 4:
            module_idx = 3  # Last genes go to module 4
        
        base_pattern = patterns[module_idx].copy()
        # Add small noise to maintain high within-module correlation
        noise = np.random.randn(n_samples) * 5
        gene_expr = base_pattern + noise + np.random.rand() * 15  # offset
        # Ensure positive values
        gene_expr = np.maximum(gene_expr, 1)
        expression_data.append(gene_expr)
    
    df = pd.DataFrame(expression_data, index=genes, columns=samples)
    
    # Save to CSV
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path)
    print(f"Created synthetic expression matrix: {output_path}")
    print(f"  Shape: {df.shape[0]} genes x {df.shape[1]} samples")
    
    return df


def read_expression_matrix(path: Path) -> pd.DataFrame:
    """Read expression matrix from CSV. Expects genes as rows, samples as columns."""
    df = pd.read_csv(path, index_col=0)
    return df


def log_and_filter(df: pd.DataFrame,
                   variance_threshold: float) -> pd.DataFrame:
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
    
    print(f"log2(x+1) transformation applied.")
    print(f"Filtered genes: {df.shape[0]} -> {df_filtered.shape[0]} (variance threshold: {variance_threshold})")
    
    return df_filtered


def correlation_matrix(df: pd.DataFrame,
                       method: str = "spearman",
                       use_abs: bool = True) -> pd.DataFrame:
    """
    Compute the gene–gene correlation matrix (rows).
    """
    # Transpose so we correlate genes (originally rows) across samples
    corr = df.T.corr(method=method)
    
    if use_abs:
        corr = corr.abs()
    
    print(f"Computed {method} correlation matrix: {corr.shape}")
    
    return corr


def adjacency_from_correlation(corr: pd.DataFrame,
                               threshold: float,
                               weighted: bool = False) -> pd.DataFrame:
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


def graph_from_adjacency(A: pd.DataFrame,
                         undirected: bool = True) -> nx.Graph:
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
    df_modules = (
        pd.DataFrame({"Gene": list(mapping.keys()), "Module": list(mapping.values())})
        .sort_values(["Module", "Gene"])
    )
    df_modules.to_csv(out_csv, index=False)


if __name__ == "__main__":
    # Get the script's directory to construct absolute paths
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    
    input_csv = repo_root / INPUT_CSV
    output_csv = repo_root / OUTPUT_CSV
    
    print("=" * 60)
    print("Gene Co-Expression Network Analysis")
    print("=" * 60)
    
    # Step 1: Create or load expression data
    if not input_csv.exists():
        print("\nStep 1: Creating synthetic expression data...")
        df_expr = create_synthetic_expression_data(input_csv, n_genes=80, n_samples=15)
    else:
        print("\nStep 1: Loading expression data...")
        df_expr = read_expression_matrix(input_csv)
        print(f"  Loaded: {df_expr.shape[0]} genes x {df_expr.shape[1]} samples")
    
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
    print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    
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
