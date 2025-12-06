# Lab 07 - Network Visualization Notes

**Author**: AndreiCod

## Layout Method Used

I used the **Spring Layout** (`nx.spring_layout`) with the Fruchterman-Reingold force-directed algorithm. This layout treats edges as springs that attract connected nodes, while all nodes repel each other. The result is a natural separation of densely connected clusters (modules) while maintaining visibility of the overall network structure.

Parameters used:
- `seed=42` for reproducibility
- `k=1.5` to increase spacing between nodes

## Reflection: What advantages does visualization provide compared to the numeric analysis from Lab 6?

Visualization provides several key advantages over pure numeric analysis:

1. **Intuitive Pattern Recognition**: While Lab 6 gave us numeric metrics like module assignments and correlation thresholds, the visualization immediately reveals the network's topology - we can see how modules cluster together and which genes bridge different modules.

2. **Hub Gene Identification**: Although we computed degree centrality numerically, seeing hub genes as larger nodes in context of their connections makes their importance tangible. We can observe that high-degree nodes (like Gene_55) truly sit at the center of densely connected regions.

3. **Module Validation**: The coloring by module confirms that our clustering from Lab 6 captured real structure - genes in the same module (same color) tend to cluster spatially in the layout, validating the biological relevance of our module detection.

4. **Communication Tool**: A network figure is far more effective for communicating findings to collaborators or in publications than a table of correlation coefficients. Biologists can immediately grasp the overall structure and identify genes of interest.

5. **Quality Control**: Visualization can reveal potential issues like disconnected components or unexpected connections that might not be obvious from summary statistics alone.

In summary, visualization transforms abstract numeric relationships into a spatial representation that leverages human pattern recognition abilities, making complex co-expression networks interpretable and actionable.
