"""
Exercise 1 — Visualization of Co-Expression Networks + Hub Genes

Author: AndreiCod

This script:
- Loads the expression matrix and module mapping from Lab 6
- Rebuilds the adjacency matrix from correlations
- Constructs a NetworkX graph from adjacency
- Colors nodes by module
- Computes hub genes (top degree)
- Visualizes and exports the network figure (.png)
- Exports hub genes to CSV
"""

from __future__ import annotations
from pathlib import Path
from typing import Dict, Iterable, Optional

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# --------------------------
# Config
# --------------------------
HANDLE = "AndreiCod"

# Input files
EXPR_CSV = Path(f"data/work/{HANDLE}/lab06/expression_matrix.csv")
MODULES_CSV = Path(f"labs/06_wgcna/submissions/{HANDLE}/modules_{HANDLE}.csv")

# Optional: if you saved adjacency in Lab 6, load it here
PRECOMPUTED_ADJ_CSV: Optional[Path] = None

# Parameters for adjacency reconstruction (same as Lab 6)
CORR_METHOD = "spearman"
USE_ABS_CORR = True
ADJ_THRESHOLD = 0.85
WEIGHTED = False

# Visualization parameters
SEED = 42
TOPK_HUBS = 10
NODE_BASE_SIZE = 60
EDGE_ALPHA = 0.15

# Outputs
OUT_DIR = Path(f"labs/07_network_viz/submissions/{HANDLE}")
OUT_PNG = OUT_DIR / f"network_{HANDLE}.png"
OUT_HUBS = OUT_DIR / f"hubs_{HANDLE}.csv"


# --------------------------
# Utils
# --------------------------
def ensure_exists(path: Path) -> None:
    """Check that a file exists, raise FileNotFoundError if not."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")


def read_expression_matrix(path: Path) -> pd.DataFrame:
    """
    Read expression matrix CSV.
    - First column contains gene names (set as index)
    - Returns DataFrame with genes as rows, samples as columns
    """
    df = pd.read_csv(path, index_col=0)
    return df


def read_modules_csv(path: Path) -> Dict[str, int]:
    """
    Read CSV with columns: Gene, Module
    Returns dict: gene -> module_id
    """
    df = pd.read_csv(path)
    return dict(zip(df["Gene"], df["Module"]))


def correlation_to_adjacency(expr: pd.DataFrame,
                             method: str,
                             use_abs: bool,
                             threshold: float,
                             weighted: bool) -> pd.DataFrame:
    """
    Compute correlation matrix and apply threshold to build adjacency.
    - compute correlation matrix on expr (genes as rows)
    - optionally apply abs()
    - apply threshold to build adjacency
    - remove diagonal (no self-loops)
    """
    # Transpose so that genes are columns for correlation
    corr = expr.T.corr(method=method)
    
    # Optionally use absolute correlations
    if use_abs:
        corr = corr.abs()
    
    # Apply threshold
    if weighted:
        adj = corr.where(corr >= threshold, 0)
    else:
        adj = (corr >= threshold).astype(int)
    
    # Remove diagonal (no self-loops)
    np.fill_diagonal(adj.values, 0)
    
    return adj


def graph_from_adjacency(A: pd.DataFrame) -> nx.Graph:
    """
    Convert adjacency DataFrame to NetworkX graph.
    Remove isolated nodes (nodes with no edges).
    """
    G = nx.from_pandas_adjacency(A)
    
    # Remove isolated nodes
    isolates = list(nx.isolates(G))
    G.remove_nodes_from(isolates)
    
    return G


def color_map_from_modules(nodes: Iterable[str], gene2module: Dict[str, int]) -> list:
    """
    Assign a color to each node based on its module.
    Uses matplotlib 'tab10' colormap.
    Returns list of colors in same order as nodes.
    """
    cmap = plt.get_cmap("tab10")
    colors = []
    for node in nodes:
        module = gene2module.get(node, 0)
        colors.append(cmap(module % 10))
    return colors


def compute_hubs(G: nx.Graph, topk: int) -> pd.DataFrame:
    """
    Compute degree for every node.
    Return top-k genes as DataFrame with Gene and Degree columns.
    """
    deg = dict(G.degree())
    sorted_genes = sorted(deg.items(), key=lambda x: x[1], reverse=True)[:topk]
    df = pd.DataFrame(sorted_genes, columns=["Gene", "Degree"])
    return df


# --------------------------
# Main
# --------------------------
if __name__ == "__main__":
    # 1: Verify input files exist
    ensure_exists(EXPR_CSV)
    ensure_exists(MODULES_CSV)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 2: Load expression matrix and module mapping
    expr = read_expression_matrix(EXPR_CSV)
    gene2module = read_modules_csv(MODULES_CSV)
    print(f"Loaded expression matrix: {expr.shape[0]} genes × {expr.shape[1]} samples")
    print(f"Loaded module mapping: {len(gene2module)} genes")

    # 3: Reconstruct adjacency from correlations
    print(f"Computing {CORR_METHOD} correlation matrix (abs={USE_ABS_CORR}, threshold={ADJ_THRESHOLD})...")
    A = correlation_to_adjacency(expr, CORR_METHOD, USE_ABS_CORR, ADJ_THRESHOLD, WEIGHTED)
    print(f"Adjacency matrix shape: {A.shape}")

    # 4: Build graph
    G = graph_from_adjacency(A)
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # 5: Compute colors by module
    node_colors = color_map_from_modules(G.nodes(), gene2module)

    # 6: Compute hub genes
    hubs_df = compute_hubs(G, TOPK_HUBS)
    hub_nodes = set(hubs_df["Gene"])
    print(f"\nTop {TOPK_HUBS} hub genes:")
    print(hubs_df.to_string(index=False))

    # Node sizes: larger for hubs
    node_sizes = [NODE_BASE_SIZE * 3 if n in hub_nodes else NODE_BASE_SIZE for n in G.nodes()]

    # 7: Compute layout and draw graph
    print("\nGenerating network visualization...")
    pos = nx.spring_layout(G, seed=SEED, k=1.5)  # k controls spacing
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=EDGE_ALPHA, edge_color="gray", ax=ax)
    
    # Draw nodes (colored by module)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, ax=ax)
    
    # Draw labels only for hub genes
    hub_labels = {n: n for n in hub_nodes if n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=hub_labels, font_size=8, font_weight="bold", ax=ax)
    
    # Add title and legend info
    unique_modules = sorted(set(gene2module.values()))
    ax.set_title(f"Gene Co-Expression Network\n{G.number_of_nodes()} genes, {G.number_of_edges()} edges, {len(unique_modules)} modules", 
                 fontsize=14)
    ax.axis("off")
    plt.tight_layout()

    # 8: Save network figure
    plt.savefig(OUT_PNG, dpi=200, bbox_inches="tight")
    print(f"\nSaved network figure to: {OUT_PNG}")
    plt.close()

    # 9: Save hub genes to CSV
    hubs_df.to_csv(OUT_HUBS, index=False)
    print(f"Saved hub genes to: {OUT_HUBS}")

    print("\n✓ Network visualization complete!")
