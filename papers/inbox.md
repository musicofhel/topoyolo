# Inbox

Papers to be sorted into the dual index (by-domain + by-structure).

---

## 2604.02033 — Magdalena de la Fuente, Feldman, Eisert, Bauer (2025)
**"High-threshold decoding of non-Pauli codes for 2D universality"**

**Domain**: Quantum error correction

**Abstract machines instantiated**:
- **Chain complex**: Toric/surface code defined by cellular homology of a torus. Logical qubits = H₁(T², ℤ/2). Non-Pauli stabilizers extend the complex beyond the standard CSS construction.
- **Matching**: JIT decoder uses minimum-weight perfect matching on a syndrome graph to decide mid-circuit X corrections. The matching is causal (partial syndrome history), which is a constraint absent from PH matching.
- **Parameterized homology**: Error threshold at ~2.5% is a phase transition in the parameterized family of noisy complexes. Below threshold, homological information (logical qubits) is preserved; above, it is destroyed.
- **Stability**: Threshold close to the ~2.9% of a decoder with full syndrome history. The gap (2.5 vs 2.9) quantifies the cost of causal (JIT) vs batch decoding — analogous to asking how much stability you lose by computing persistence on a sliding window vs the full point cloud.
- **Null model**: Phenomenological error model with equally likely physical and measurement errors serves as the noise channel against which the decoder is benchmarked.

**What is genuinely new (not reducible to shared abstraction)**:
- Non-Pauli stabilizers require mid-circuit corrections, meaning the complex itself changes during the computation. This is a *dynamic* chain complex — the boundary operators are modified by the decoder's actions. No direct analogue in PH (where the complex is built once from data) or dynamical systems.
- JIT constraint: the decoder must commit to corrections before seeing future syndromes. This causality constraint has no analogue in batch PH computation.

**Connections the authors acknowledge**: None to TDA or dynamical systems. Situated entirely within the QEC literature.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Toric code | Chain complex on T² |
| Stabilizer | Image of ∂ (or δ) |
| Logical operator | Non-trivial homology class |
| Syndrome | Cycle (element of ker ∂) |
| Matching decoder | Optimal assignment on features |
| Error threshold | Critical parameter in parameterized homology |
| Code distance | Robustness guarantee (min-weight non-trivial cycle) |

---

## Core ATT papers (to be individually annotated)

### Takens (1981) — "Detecting strange attractors in turbulence"
**Domain**: Dynamical systems. **Machines**: Chain complex (implicit — the reconstructed manifold has homology), stability (embedding is generically diffeomorphic → topology preserved).

### Sauer, Yorke, Casdagli (1991) — "Embedology"
**Domain**: Dynamical systems. **Machines**: Stability (measure-theoretic genericity of faithful embedding).

### Cohen-Steiner, Edelsbrunner, Harer (2007) — "Stability of persistence diagrams"
**Domain**: TDA. **Machines**: Stability (bottleneck ≤ Hausdorff), parameterized homology.

### Adams et al. (2017) — "Persistence images"
**Domain**: TDA. **Machines**: Parameterized homology (vectorized), matching (implicit in the weighting function).

### Bauer (2021) — "Ripser"
**Domain**: TDA (computational). **Machines**: Chain complex (VR), parameterized homology (persistence algorithm).

### Giusti, Curto et al. (2015) — "Clique topology reveals intrinsic geometric structure"
**Domain**: Neuroscience + TDA. **Machines**: Chain complex (clique complex on correlations), parameterized homology.

### Gardner et al. (2022) — "Toroidal topology of population activity in grid cells"
**Domain**: Neuroscience. **Machines**: Chain complex (the torus IS the neural manifold — same object as the toric code's base space, different interpretation).

### Xi et al. — "TE + directed PH in spiking systems"
**Domain**: Neuroscience + TDA + information theory. **Machines**: Chain complex (on TE-derived network), parameterized homology, null model.

### Sugihara et al. — CCM
**Domain**: Dynamical systems + causal inference. **Machines**: Joint-vs-marginal (manifold cross-prediction), stability (convergence criterion).

### Tsuda (2001) — "Chaotic itinerancy"
**Domain**: Neuroscience + dynamical systems. **Machines**: Parameterized homology (implicit — attractor switching = topology change over time).

### Schreiber (2000) — "Measuring information transfer"
**Domain**: Information theory + dynamical systems. **Machines**: Joint-vs-marginal (conditional mutual information), null model (shuffled surrogates).

### Tort et al. (2010) — PAC modulation index
**Domain**: Neuroscience. **Machines**: Joint-vs-marginal (cross-frequency coupling), null model (surrogate distributions).

---

## To find and annotate

- Kitaev (2003) — original toric code paper. Map the homological construction explicitly.
- Dennis et al. (2002) — "Topological quantum memory." Threshold as phase transition in random-bond Ising model — connects to statistical mechanics.
- Bombin & Martin-Delgado — color codes. Different cellulation, same homological machinery.
- Perea & Harer — sliding-window PH. Parameterized homology on time series.
- R-Cross-Barcode / RTD-Lite — cross-filtration features. Closest to joint-vs-marginal in TDA proper.
- Freedman, Kitaev, Wang — topological quantum computation. Homology as computational resource.
- Tononi — Integrated Information Theory (Φ). Joint-vs-marginal excess as consciousness measure. Controversial but structurally parallel to binding.
- Ay, Polani — information decomposition (PID). Synergy/redundancy as joint-vs-marginal. Directly comparable to binding residual.
- Riehl — "Category Theory in Context." The abstract machines here are functors. Worth formalizing?
