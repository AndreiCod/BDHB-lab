# Assignment 8: Drug-Disease Network Construction and Analysis

## Overview
Construct a drug-disease network from DrugBank, analyze its topology using key network metrics, and interpret the biological significance. Use your analysis to propose potential drug repurposing candidates.

**Opened:** Tuesday, December 2, 2025, 00:00
**Due:** Wednesday, January 7, 2026, 00:00

---

## Requirements

### 1. Dataset Preparation
Use DrugBank **version 5.1.11**(drive link).
- **Dataset:** https://go.drugbank.com/
- **Entities:**
  - Drugs: names of drugs with known targets.
  - Targets: proteins associated with the drugs.
  - Genes: disease-associated genes linked to the targets.
  - Diseases: diseases linked to the genes.
- **Interactions:** drug-target, protein-gene, gene-disease (and any other available relationships).

### 2. Network Construction
Using NetworkX (or another suitable tool):
- **Build the network:**
  - Nodes represent biological entities: drugs, proteins, genes, diseases.
  - Edges represent interactions provided in the dataset.
  - Use directed or undirected edges depending on interaction type.
- **Network visualization:**
  - Generate a basic visualization.
  - Highlight drugs and diseases as distinct node types (e.g., colors or shapes).
- **Node metadata:**
  - Node type (Drug, Protein, Gene, Disease).
  - Interaction type (Drug-Target, Gene-Disease, etc.).

### 3. Metric Calculations
Compute the following metrics, and interpret their biological significance:
- **Degree centrality:**
  - Identify nodes with highest degree.
  - Are these hubs (essential genes, highly connected proteins, multitarget drugs)?
- **Betweenness centrality:**
  - Identify bottleneck nodes.
  - Do they represent key regulators or critical targets?
- **Clustering coefficient:**
  - Identify tightly connected groups.
  - Are clusters linked to specific diseases or drug mechanisms?
- **Shortest path length (drug to disease):**
  - Which drugs are closest to disease-associated genes?
  - Can this suggest repurposing candidates?

### 4. Biological Interpretation
- **Network properties:**
  - Summarize overall structure (nodes, edges, connected components).
  - Is the network sparse or dense? What does this imply about interaction complexity?
- **Drug repurposing insights:**
  - Propose 1-2 drugs as candidates for repurposing.
  - Justify using metrics and network visualization.

---

## Deliverables
Submit a detailed report that includes:
- **Network visualization:** labeled figure highlighting key nodes/edges.
- **Metric results:** tables or plots, with biological interpretation.
- **Drug repurposing proposal:** 1-2 candidates with justification.
- **Code implementation:** script(s) used to construct and analyze the network.
