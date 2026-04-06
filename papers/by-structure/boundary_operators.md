# Boundary Operators (Chain Complex)

Papers instantiating the **chain complex** abstract machine: boundary operators with ∂²=0, cycles as kernel of ∂, boundaries as image of ∂, homology as ker/im.

The shared pattern: there is a graded algebraic object (simplicial complex, code complex, factor graph) with maps between grades satisfying ∂² = 0. The kernel of ∂ (cycles/syndromes/periodic orbits) and the image of ∂ (boundaries/trivial syndromes) define homology classes that carry topological meaning.

---

## Statistical Physics / Information Theory

### Mézard & Mora (2008) — Constraint Satisfaction
LDPC parity-check matrix H as boundary operator over GF(2). Codewords are ker(H), syndromes are im(H). Factor graphs generalize the chain complex structure. Full annotation: `by-domain/information_theory.md`.

### Sugiyama, Nakahara & Tsuda (2016) — Information Decomposition on Structured Space
Dual θ/η coordinates on posets as order-theoretic chain complex. Möbius function as boundary operator. Principal ideals (↓x) and filters (↑x) as ∂ and δ supports. Pythagorean theorem for KL divergence decomposes interactions by level. Full annotation: `by-domain/information_theory.md`.

---

## TDA

### Mollers, Immer, Fortuin, Isufi (2023) — Hodge-Aware Contrastive Learning
Full chain complex on simplicial complexes of order 2. Incidence matrices B_1 (node-to-edge) and B_2 (edge-to-triangle) ARE the boundary operators. Hodge Laplacians L_k built from ∂ and ∂^T. The Hodge decomposition R^{N_1} = im(B_1^T) + im(B_2) + ker(L_1) is the chain complex decomposition into coboundaries + boundaries + homology. The contrastive learning objective preserves this decomposition in the embedding space. Full annotation: `by-domain/tda.md`.

### Kanjamapornkul, Pincak, Bartos (2020) — Cohomology Theory for Financial Time Series
Khovanov cohomology (categorification of Jones polynomial) on financial time series. Cochain groups from market microstructure states. Coboundary operators from knot/link structure of figure-eight hyperbolic knots. delta^2 = 0 from standard Khovanov construction. Cohomology classifies 8 fundamental market states. Full annotation: `by-domain/tda.md`.

*(See also inbox for Bauer/Ripser, Cohen-Steiner)*

## QEC

### Oreshkov (2013) — Continuous-time quantum error correction
Subsystem decomposition H_S = H_A ⊗ H_B ⊕ K as Hilbert-space chain complex. Code subsystem H_A = protected information (cycles); gauge subsystem H_B = correctable errors (boundaries); K = uncorrectable states. Error-correcting map R projects onto code space (projection to ker/im). Correctability condition = functional ∂^2 = 0. Full annotation: `by-domain/qec.md`.

*(See also inbox for de la Fuente toric code, Kitaev)*

## Neuroscience

*(Clique complexes on correlation matrices — see inbox for Giusti)*

---

## Cross-domain observation

The chain complex machine appears in four distinct incarnations across these papers:

1. **Geometric (TDA — Mollers et al.)**: Incidence matrices B_k on simplicial complexes. ∂ maps k-simplices to (k-1)-simplices. Homology = topological features of the data. Hodge decomposition = gradient + curl + harmonic.

2. **Algebraic (QEC — Oreshkov)**: Subsystem decomposition of Hilbert space. The "boundary" is the error map; "cycles" are code states; "homology" = logical qubits (protected information).

3. **Categorified (TDA/Finance — Kanjamapornkul et al.)**: Khovanov cohomology on knot diagrams derived from time series. Coboundary from knot crossings. Cohomology classifies market states.

4. **Combinatorial (Information theory — Sugiyama et al.)**: Mobius function on posets. ∂ is inclusion-exclusion. Orthogonal decomposition of D_KL mirrors Hodge orthogonality.

The Hodge decomposition appears in both the TDA and information theory contexts with the same orthogonality structure.
