## Eurographics-2004 (witness complexes) --- de Silva & Carlsson (2004)
**"Topological Estimation Using Witness Complexes"**
Eurographics Symposium on Point-Based Graphics 2004, pp. 157–166 (queue file: "157-166.pdf")

**Domain(s)**: TDA

**Abstract machines instantiated**:

- **Chain complex**: simplicial approximation of an unknown space X from point clouds — Betti numbers b_k computed from a simplicial complex as proxies for b_k(X); the witness construction is a Delaunay-motivated rule deciding which landmark-spanned simplices enter the chain complex.

- **Parameterized homology**: three families W(D; R, ν), ν=0,1,2, parameterized by feature-size R, each a *nested family* of complexes explicitly built to feed persistent homology (ELZ00/ZC04) — persistence interval graphs ("richer and more robust than a single Betti number") as the output invariant.

- **Stability / denoising** (empirical): shrinking the vertex set to landmarks yields "a better picture of the homology, with less noise, than the full scale constructions" — subsampling as a robustness mechanism rather than a mere compression; validated against Rips on the 2-sphere benchmark.

**What is genuinely new (not reducible to shared abstraction)**:
1. The witness principle: non-vertex data points certify simplices among landmarks — decoupling *who the vertices are* from *what evidence admits a simplex*, breaking the size coupling of Čech/Rips/α-shape vertex sets with the data.
2. Generalizes Martinetz–Schulten topology-preserving graphs along two axes at once: graph → simplicial complex, single scale → nested family (hence PH-ready).
3. Foundational infrastructure: this is the landmark-subsampling tool that later large-scale TDA quietly presupposes; no new invariants, but a change in what the chain-complex machine is allowed to be built on.

**Connections the authors acknowledge**: Delaunay complexes, Martinetz–Schulten neural-gas graphs, ELZ/ZC persistence lineage, Mumford natural-image-patch data. No cross-domain awareness.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Witness complex W(D;R,ν) | Chain complex with evidence-certified simplices |
| Landmark points | Vertex set of the approximation |
| Witnesses | Non-vertex data certifying simplices |
| Nested family over feature size R | Filtration |
| Persistence interval graph | Parameterized homology barcode |
| Less-noisy homology from landmarks | Subsampling-induced stability |

---
*Provenance: annotated from queue batch-002 candidate-36 (abstract + content extract). Depth-limited accordingly.* (B2 pass 39)

**See also**: `by-domain/tda.md`, `by-structure/filtrations.md`
