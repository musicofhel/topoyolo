# Chain Complex

## The Abstract Machine

A chain complex is a sequence of abelian groups (or vector spaces) connected by boundary operators ∂ satisfying ∂² = 0:

```
... → C_{n+1} → C_n → C_{n-1} → ...
           ∂_{n+1}    ∂_n
```

The key derived objects:
- **Cycles**: ker(∂_n) — elements with zero boundary
- **Boundaries**: im(∂_{n+1}) — elements that are boundaries of something
- **Homology**: H_n = ker(∂_n) / im(∂_{n+1}) — cycles that are not boundaries

The condition ∂² = 0 guarantees that every boundary is a cycle, making the quotient well-defined. Homology classes are the topological invariants — features that survive modding out by trivial structure.

## Where It Appears

### TDA
The simplicial complex is the prototypical chain complex. Simplices (vertices, edges, triangles, ...) form the chain groups C_n. The boundary operator maps each n-simplex to its (n-1)-faces with alternating signs. Persistent homology tracks how these homology classes appear and disappear across a filtration.

**Papers**: Hodge-Aware CL (Mollers et al., 2023) — incidence matrices B_1, B_2 as boundary operators; Hodge Laplacian L_1 = B_1^T B_1 + B_2 B_2^T; Hodge decomposition = cycle-boundary-harmonic splitting. Khovanov Cohomology for Finance (Kanjamapornkul et al., 2020) — cochain complex from market microstructure.

### QEC
The code complex on a surface or cellulation. Stabilizers are images of ∂ (trivial syndromes). Logical qubits are non-trivial homology classes. The error syndrome pattern is an element of ker(∂).

**Papers**: de la Fuente et al. (2025) — toric code as cellular homology on T²; Oreshkov (2013) — subsystem decomposition H_S = H_A ⊗ H_B ⊕ K as Hilbert-space chain complex, correctability condition as ∂² = 0 analogue.

### Information Theory
Two distinct instantiations discovered:

1. **LDPC codes** (Mézard & Mora, 2008): Parity-check matrix H is literally a boundary operator over GF(2). Codewords = ker(H). Factor graphs generalize the structure but lose the strict ∂² = 0 property for general CSPs.

2. **Posets** (Sugiyama et al., 2016): Information decomposition on partially ordered sets. Möbius function as boundary operator. Principal ideals and filters as ∂ and δ supports. The event hierarchy (1-way, 2-way, ..., n-way interactions) forms a graded structure where the Möbius inversion formula plays the role of ∂² = 0.

### Dynamical Systems
Periodic orbits correspond to 1-cycles in the attractor's topology, but this is a weaker instantiation — see ANTISYNONYMS.md on "cycle" as false cognate.

### Neuroscience
Clique complexes on correlation matrices (Giusti et al., 2015 — in inbox). Population topology on neural manifolds (Gardner et al., 2022 — in inbox).

## Key Divergences

- **Coefficient fields**: TDA uses ℝ or ℤ/2; QEC uses ℤ/2 or ℤ/p; information theory uses ℝ. Same machine, different arithmetic.
- **Factor graphs vs. chain complexes**: factor graphs lack ∂² = 0 in general.
- **Möbius function vs. ∂**: works on posets (more general than simplicial complexes).
- See `glossary/ANTISYNONYMS.md` for full list.
