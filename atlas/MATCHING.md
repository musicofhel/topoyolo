# Matching

## The Abstract Machine

Two sets of features and a cost function. Find the optimal assignment that minimizes total cost. The minimum cost defines a distance (between diagrams, between codes, between distributions). The assignment itself defines a correction or a transport plan.

```
Features A:  {a₁, a₂, ..., aₘ}
Features B:  {b₁, b₂, ..., bₙ}
Cost:        c(aᵢ, bⱼ)
Solution:    π* = argmin_π Σ c(aᵢ, π(aᵢ))
```

## Where It Appears

### TDA — Diagram Distances
Persistence diagram points (birth, death) are matched between two diagrams. Bottleneck distance uses L∞ cost (minimax); Wasserstein distance uses Lp cost (sum). Points can be matched to the diagonal (feature present in one diagram but not the other, at cost = lifetime/2). Algorithms: Hungarian, auction.

**Papers**: Bottleneck Degree (Di Rocco et al., 2019) — bottleneck pairs as critical points of the squared distance function on a variety; algebraic complexity of the matching.

### QEC — Syndrome Decoding
Syndrome defects (endpoints of error chains) are matched to identify the most likely error. MWPM (Minimum-Weight Perfect Matching) on the syndrome graph. Union-Find as a faster alternative.

**Papers**: de la Fuente et al. (2025) — JIT decoder uses MWPM with causal constraint (partial syndrome history). Oreshkov (2013) — continuous correction as streaming matching (implicit).

### Information Theory — Multiple Instances

1. **Belief Propagation** (Mézard & Mora, 2008): Approximate matching on factor graphs. For LDPC codes, equivalent to syndrome decoding. Survey Propagation as meta-level matching on the space of surveys.
2. **Blahut-Arimoto**: Optimal source-channel matching for rate-distortion.
3. **Optimal transport**: Wasserstein distances between distributions (shared with TDA).

### Dynamical Systems (updated — third pass fills the gap)
Previously marked as "rarely used." Third pass found several instances:
1. **Ensemble control on Lie groups**: Single broadcast control must simultaneously steer all systems to respective targets — infinite-dimensional matching reduced to finite-dimensional via Cartan covering.
2. **IC-PINN coupling functions**: Basis-free inference = function-level matching from infinite-dimensional space to observed dynamics.
3. **Ordinal networks**: Hurst exponent estimation = matching to parameterized family of fractional processes.

### Neuroscience (updated — third pass fills the gap)
Previously marked as "rarely used." Third pass found:
1. **Opponent striatal circuit**: D1/D2 opponent pairing — each D1 neuron encoding quantile tau implicitly paired with D2 neuron encoding 1-tau.
2. **ConformalHDC**: Nearest-centroid matching in high-dimensional space for hippocampal decoding.
3. **Driver fatigue GC**: Assigning causal roles (driver vs driven) to EEG channels is an implicit matching problem.

## Key Divergences

- **Causal vs. batch**: Syndrome decoding (JIT) must commit before seeing future data. Diagram matching is batch. This is a genuine structural difference — see ANTISYNONYMS.md.
- **Cost function semantics**: Bottleneck = worst-case pairing cost. Wasserstein = total pairing cost. Syndrome graph = edge weight. These different cost functions produce different distances with different mathematical properties.
- **Matching to diagonal**: In TDA, unmatched points can be paired with the diagonal. In QEC, unmatched syndromes indicate an uncorrectable error. In information theory, unmatched symbols indicate a capacity violation.
