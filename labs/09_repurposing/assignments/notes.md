# Week 9 — Drug Repurposing & Network-based Approaches Notes

# Authors
- Student: Andrei Codrin Daha (AndreiCod)
- Student: Bals Radu (BalsRadu)


## Task 1 — Dataset Preparation
- Parsed full DrugBank XML (v5.1.11) to extract drug-target and drug-disease relationships per `Task1_dataset_preparation.ipynb`.
- Used iterative XML parsing for memory-efficient processing of the 1.5GB DrugBank file.
- Improved disease extraction with keyword-based filtering and artifact removal (reference markers, newlines).
- **Note on gene-disease associations**: DrugBank does not provide explicit gene-disease relationships. While we extracted gene associations for network completeness, our repurposing analysis deliberately uses only direct DrugBank relationships (drug-target, drug-disease) to avoid circular inference.
- Output: `artifacts/task1_drugs.csv`, `artifacts/task1_drug_targets.csv`, `artifacts/task1_drug_diseases.csv`, `artifacts/task1_gene_diseases.csv`.

| Parameter | Value |
|-----------|-------|
| Dataset | DrugBank XML v5.1.11 (full) |
| Drugs processed | 16,575 |
| Drug-target relationships | 14,802 |
| Drug-disease relationships | 5,983 |
| Gene-disease associations | 14,571 |
| Unique targets | 3,553 |
| Unique genes | 3,545 |
| Unique diseases | 4,030 |


## Task 2 — Network Construction
- Constructed drug-disease network using NetworkX per `Task2_network_construction.ipynb`.
- Built network with 4 node types as required: Drug, Target (protein), Gene, and Disease.
- Implemented 4 edge types: drug-target, protein-gene, gene-disease, drug-disease.
- The network structure supports multiple analysis approaches, though our repurposing strategy focuses on direct drug-target-disease paths.
- Generated network visualization highlighting all node types with distinct colors.
- Output: `artifacts/task2_network.gml`, `artifacts/task2_network_viz.png`, `artifacts/task2_network_summary.csv`.

| Parameter | Value |
|-----------|-------|
| Network library | NetworkX |
| Node types | Drug, Target, Gene, Disease |
| Total nodes | 26,616 |
| Total edges | 38,150 |
| Drug nodes | 16,575 |
| Target nodes | 2,887 |
| Gene nodes | 2,794 |
| Disease nodes | 4,360 |
| Drug-target edges | 14,802 |
| Gene-disease edges | 14,571 |
| Drug-disease edges | 5,983 |
| Protein-gene edges | 2,794 |


## Task 3 — Metric Calculations
- Computed network centrality metrics per `Task3_metric_calculations.ipynb`.
- Calculated degree centrality to identify highly connected nodes (hubs).
- Calculated betweenness centrality to identify bottleneck nodes (critical connectors).
- Calculated clustering coefficient to measure local connectivity.
- Computed shortest paths between drug-disease pairs with intermediate node type tracking.
- Identified paths with gene/target intermediates for mechanistic repurposing candidates.
- Output: `artifacts/task3_centrality_metrics.csv`, `artifacts/task3_drug_disease_paths.csv`, `artifacts/task3_hub_targets.csv`.

### Top Hub Drugs (Polypharmacological Compounds)

| Drug | Degree | Betweenness | Interpretation |
|------|--------|-------------|----------------|
| Fostamatinib | 298 | 0.0379 | Multi-kinase inhibitor targeting many proteins |
| NADH | 146 | 0.0150 | Cofactor involved in many metabolic pathways |
| Copper | 145 | 0.0172 | Essential mineral with multiple protein interactions |
| Zinc | 126 | 0.0048 | Enzyme cofactor with broad target profile |

### Top Hub Targets (Most Druggable Proteins)

| Target | Degree | Betweenness | Interpretation |
|--------|--------|-------------|----------------|
| Cyclin-dependent kinase 2 | 137 | 0.0051 | Key cell cycle regulator, oncology target |
| Estrogen receptor alpha | 120 | 0.0107 | Major hormone receptor, breast cancer target |
| Histamine H1 receptor | 111 | 0.0022 | Antihistamine target for allergies |
| Dopamine D2 receptor | 110 | 0.0012 | CNS target for antipsychotics |
| 5-HT2A receptor | 108 | 0.0016 | Serotonin receptor for CNS drugs |


## Task 4 — Biological Interpretation
- Analyzed overall network structure per `Task4_biological_interpretation.ipynb`.
- Interpreted hub nodes: polypharmacological drugs, highly druggable protein targets.
- Interpreted bottleneck nodes: critical regulators in drug-disease pathways.
- Implemented **shared-target mechanism** for drug repurposing — a methodologically sound approach that avoids circular reasoning.
- Proposed diverse drug repurposing candidates based on shared protein targets between drugs.
- Output: `artifacts/task4_network_summary.txt`, `artifacts/task4_repurposing_candidates.csv`, `artifacts/task4_network_properties.csv`.

### Network Properties Summary

| Property | Value | Interpretation |
|----------|-------|----------------|
| Nodes | 26,616 | 4 entity types: Drug, Target, Gene, Disease |
| Edges | 38,150 | 4 relationship types as required |
| Density | 0.0001 | Very sparse - selective drug-target binding |
| Avg clustering | ~0 | Expected for bipartite-like network structure |
| Connected components | ~10,366 | Many isolated drug-disease clusters |
| Largest component | ~54.7% | Majority of nodes interconnected |
| Avg degree | ~2.87 | Each node has ~3 connections on average |

### Drug Repurposing Candidates (Shared Target Mechanism)

| Candidate Drug | Target Disease | Shared Target | Approved Drug |
|----------------|---------------|---------------|---------------|
| Fostamatinib | Diabetic Retinopathy | Focal adhesion kinase 1 | Endostatin |
| Copper | Major Depressive Disorder | Brain-derived neurotrophic factor | Esketamine |
| Quercetin | Osteoporosis (Postmenopausal) | Estrogen receptor beta | Raloxifene |
| Artenimol | Recurrent Ovarian Cancer | Tubulin beta chain | Vinorelbine |
| Glutamic acid | Schizophrenia | NMDA receptor 2B | Lumateperone |

**Methodology**: If Drug A and Drug B both bind Target T, and Drug A is approved for Disease D, then Drug B may also treat Disease D via the same mechanism. This approach leverages **native DrugBank relationships** (drug-target and drug-disease) to identify mechanistically plausible repurposing candidates.

### Biological Insights
- **Very sparse network (density=0.0001)**: Reflects highly selective drug-target binding typical of pharmaceutical compounds.
- **Hub drugs (Fostamatinib, NADH, Copper)**: Polypharmacological compounds that interact with many targets, either by design (kinase inhibitors) or biology (cofactors).
- **Hub targets (CDK2, ER-alpha, H1R, D2R)**: Major druggable proteins representing key therapeutic areas (oncology, hormone therapy, allergy, psychiatry).
- **Shared-target repurposing rationale**: Drugs binding the same protein target as approved therapeutics offer mechanistically justified repurposing candidates. Examples:
  - **Quercetin** (phytoestrogen) shares Estrogen receptor β with **Raloxifene** (osteoporosis drug) — biologically plausible given their common receptor binding.
  - **Artenimol** (antimalarial) shares Tubulin β with **Vinorelbine** (cancer drug) — tubulin inhibition is a well-established anticancer mechanism.
- **Methodological soundness**: By using only direct drug-target and drug-disease relationships from DrugBank, this approach ensures biologically meaningful repurposing hypotheses without relying on inferred associations.
