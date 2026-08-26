## ICCV-2021 (DOI 10.1109/ICCV48922.2021.00701) --- Wong & Vong (2021)
**"Persistent Homology based Graph Convolution Network for Fine-grained 3D Shape Segmentation"**
IEEE/CVF ICCV 2021 | DOI: 10.1109/ICCV48922.2021.00701

**Domain(s)**: TDA

**Abstract machines instantiated**:

- **Parameterized homology**: the core mechanism — complex filtration on the point cloud produces filtered complexes; persistent homology in dimensions 0, 1, 2 yields barcodes/persistence diagrams used as multi-scale topological *features* fed into a graph convolution network for segmentation.

- **Matching**: the novel Persistence Diagram Loss L_PD is a diagram-vs-diagram comparison — the network's predicted segmentation induces a topological summary that is penalized by its mismatch against the ground-truth shape's persistence diagram, i.e. matching cost between diagrams repurposed as differentiable training signal.

- **Stability** (weak): enforcing topological correctness via diagram loss presupposes that small segmentation perturbations should induce small diagram changes — stability intuition operationalized as a loss, though no formal bottleneck-distance bound is proven.

**What is genuinely new (not reducible to shared abstraction)**:
1. Persistence diagrams used not as an analysis endpoint but as a *supervisory target*: the diagram loss closes the loop so that topological summaries train downstream geometric prediction — machines composed into an optimization objective.
2. Explicit motivation that pairwise-relation GNN/GCN graphs cannot see higher-dimensional relations (handles, doorknobs, wires) — filtration/simplicial structure introduced precisely to supply what edge-only message passing misses (a joint-exceeds-marginals argument stated geometrically).
3. Application-domain engineering (fine-grained manufacturing parts); no new theory of the machines themselves.

**Connections the authors acknowledge**: standard TDA lineage (Edelsbrunner–Letscher–Zomorodian style citations); PartNet hierarchical baseline critique. No cross-domain awareness.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Complex filtration / filtered complexes | Filtration (parameterized chain complexes) |
| Persistence barcode/diagram features | Parameterized homology summaries |
| Persistence Diagram Loss | Matching cost between diagrams |
| Topology correctness | Stability prior as training constraint |
| Higher-dimensional relationships | Structure absent from pairwise (marginal) views |

---
*Provenance: annotated from queue batch-002 candidate-35 (abstract + content extract). Depth-limited accordingly.* (B2 pass 39)

**See also**: `by-domain/tda.md`, `by-structure/composite_systems.md`
