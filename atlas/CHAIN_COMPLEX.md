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

3. **Polynomial chaos** (Oladyshkin et al., 2023): Orthogonal polynomial expansion of neural signals graded by interaction order. kth-order terms capture k-way interactions. The orthogonality condition parallels the Hodge decomposition — three independent mathematical traditions (Hodge, KL-Pythagoras on posets, polynomial chaos) have developed isomorphic orthogonal decomposition machinery with zero cross-citation.

4. **PID lattice** (Williams-Beer, 2010; multiple PID papers): The redundancy lattice of source combinations, with Möbius inversion decomposing MI into atoms. The lattice structure + Möbius function creates a near-chain complex. See PID core annotations in `by-domain/information_theory.md`.

### QEC (extended)
**Papers**: Pati & Sanders (2005) — The Bloch sphere S² has H₂(S²) = ℤ, and no CPTP map can reduce this topological dimension. The no-partial-erasure theorem is a homological conservation law. Tarnowski et al. (2019) — Chern number as fiber bundle invariant measured dynamically via linking number.

### Dynamical Systems
Periodic orbits correspond to 1-cycles in the attractor's topology, but this is a weaker instantiation — see ANTISYNONYMS.md on "cycle" as false cognate. Graph Laplacians on Hawkes process networks (Shang & Sun, 2019) and lead-lag networks (Bennett et al., 2022) are 0th Hodge Laplacians. Reservoir GNN message-passing aggregation (Gallicchio & Micheli, 2020) acts as a boundary-like operator.

### Neuroscience
Clique complexes on correlation matrices (Giusti et al., 2015 — in inbox). Population topology on neural manifolds (Gardner et al., 2022 — in inbox). Brain network graph Laplacians (Simpson et al., 2013).

## Key Divergences

- **Coefficient fields**: TDA uses ℝ or ℤ/2; QEC uses ℤ/2 or ℤ/p; information theory uses ℝ. Same machine, different arithmetic.
- **Factor graphs vs. chain complexes**: factor graphs lack ∂² = 0 in general.
- **Möbius function vs. ∂**: works on posets (more general than simplicial complexes).
- See `glossary/ANTISYNONYMS.md` for full list.
