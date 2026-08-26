## simpson-2013 — Simpson, Bowman, Laurienti (2013)
**"Analyzing complex functional brain networks: fusing statistics and network science to understand the brain"**
**Domain(s)**: Neuroscience
**Abstract machines instantiated**:
- **Chain complex (weak)**: Functional brain networks are graphs where nodes are brain regions and edges are correlations. The graph Laplacian, clustering coefficient, path length, and community structure are all computed from this graph — these are spectral and combinatorial invariants of the 0-skeleton complex.
- **Parameterized homology**: The thresholding step is a filtration: by varying the correlation threshold, edges appear/disappear, and the graph topology changes. The paper discusses how different thresholds yield different network properties — this is exactly parameterized graph topology. The methodological gap identified is precisely the lack of principled threshold selection.
- **Joint-vs-marginal excess**: Functional connectivity = pairwise correlation between brain region time series. The network itself encodes joint structure: which brain regions co-activate beyond what their marginal (individual) activities predict. Community structure identifies groups of regions with high internal joint excess. Integration (global efficiency) vs segregation (modularity) is the network-level joint-vs-marginal trade-off.
- **Null hypothesis**: Multiple null models discussed: random networks (Erdos-Renyi), degree-preserved random networks (configuration model), lattice networks. Each null destroys different aspects of the brain network structure while preserving others (e.g., degree sequence). The small-world property is defined as departure from both random and lattice nulls.

**What is genuinely new (for topo-rosetta)**: This survey identifies the exact methodological gaps where TDA could help neuroscience: (1) threshold selection is a filtration problem — persistent homology is the principled solution; (2) higher-order structure beyond pairwise correlations requires simplicial methods; (3) temporal dynamics of brain networks need the parameterized homology framework. The paper does not make these connections, but the gaps it identifies are precisely filled by the topo-rosetta machines.

**Connections the authors acknowledge**: Graph theory, small-world networks, community detection. Cite the Human Connectome Project. No connections to TDA, QEC, or information theory proper (despite using correlations, which are MI under Gaussian assumptions).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Correlation threshold | Filtration parameter |
| Network construction | Building a 0-skeleton complex |
| Clustering coefficient | Local topological feature |
| Path length | Distance in 0-skeleton |
| Community structure | Homological decomposition (connected components at threshold) |
| Small-world property | Departure from null (neither random nor lattice) |
| Integration vs segregation | Global vs local topological balance |
| Functional connectivity | Pairwise joint excess |

---
