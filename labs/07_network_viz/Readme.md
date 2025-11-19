# Week 7 — Visualization and Interpretation of Co-Expression Networks (GCEs) + Diseasome

## Goals
- Visualizing gene co-expression networks and identified modules.  
- Identifying hub genes (the most connected nodes in modules).  
- Validating modules using functional enrichment (GO, KEGG).  
- Understanding the concept of **Diseasome** and its connection with co-expression networks.  
- Interpreting results in biomedical context (cancer, comorbidities, drug repurposing).  

---

## Context
In Week 6 we built a co-expression network and detected modules.  
Now we go further: **visualization and interpretation**.

Networks are difficult to understand as matrices — good visualization reveals structure, modules, and hub genes.  
Furthermore, we can biologically validate modules through **functional enrichment analysis** and link them to the **diseasome** — the map of human diseases connected through shared genes and modules.

---

## Hands-on
**Run and complete**  
- `ex08_network_viz.py` — visualize the network built in Lab 6.  
  - Load `modules_<handle>.csv` and the adjacency matrix.  
  - Color nodes according to module.  
  - Highlight hub genes (those with highest degree).  
  - Export the figure to `network_<handle>.png`.  

**Optional (bonus)**  
- Try visualization in an external tool (Cytoscape or Gephi).  
- Compare appearance and interpretability with NetworkX.  

---

## Deliverables
Your PR must include:
1. File `labs/07_networkviz/<github_handle>_notes.md` with:  
   - which layout method you used (e.g., spring, kamada-kawai),  
   - a short reflection: **What advantages does visualization provide compared to the numeric analysis from Lab 6?**  
2. Completed script `ex08_network_viz.py`.  
3. Generated file:  
   ```bash
   labs/07_networkviz/submissions/<handle>/network_<handle>.png
   ```  
4. Completion of the PR checklist template.

---

## Next week
- Machine Learning in biomedical data analysis.  
- Disease state classification and model evaluation.  
- [See Week 8 — Machine Learning.](/labs/08_ML_flower)

---

## Skills
- Visualizing networks and interpreting modules.  
- Identifying and analyzing hub genes.  
- Performing functional enrichment analyses on modules.  
- Understanding and explaining the Diseasome concept.  
- Connecting results to biomedical context (cancer, comorbidities, drug repurposing).  

---

## Resources

- [Lab handout](../../docs/lab_onepagers/07_network_viz.md)  
- [NetworkX Drawing](https://networkx.org/documentation/stable/reference/drawing.html)  
- [Cytoscape — biological network visualization](https://cytoscape.org/)  
- [Gephi — general-purpose network visualization](https://gephi.org/)  
- [g:Profiler — GO/KEGG functional enrichment](https://biit.cs.ut.ee/gprofiler/)  
- [Barabási et al., Nature Genetics 2007 — The Human Diseasome](https://www.nature.com/articles/nrg2918)
