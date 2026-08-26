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

**Papers**: Bottleneck Degree (Di Rocco et al., 2019) — bottleneck pairs as critical points of the squared distance function on a variety; algebraic complexity of the matching. Divol & Lacombe (2019, arXiv: 1901.03048) — persistence diagram distances ARE optimal partial transport distances (exact identification, not analogy); Wasserstein-p distance on PDs = p-th root of optimal partial transport cost. Adams et al. (2017) — Wasserstein matching is implicit in the stability proofs for persistence images; the W_1 Lipschitz bound means small changes in the matching produce small changes in the vectorized output. Bubenik & Elchesen (2019, arXiv: 1912.02563) — proves bottleneck and Wasserstein distances are UNIVERSAL constructions on persistence diagrams; 1-Wasserstein satisfies Kantorovich-Rubinstein duality; any metric on PDs factors through these distances. Chen & Wang (2021, arXiv: 2104.07710) — near-linear time approximation algorithms for 1-Wasserstein on PDs via randomly shifted quadtrees; diagonal handled as infinite zero-cost reservoir; 100-1000x speedup over Hungarian/auction. Peyré (2026, arXiv: 2604.04891) — Spectral Wasserstein distances: family of transport costs W_γ parameterized by Schatten norm p, where the cost acts on the global displacement covariance matrix. Trace norm (p=1) recovers W2; operator norm (p=∞) gives Muon geometry. Generalizes scalar matching (sum of individual costs) to matrix-aware matching (global covariance penalty). Kantorovich = Benamou-Brenier for monotone norms.

### QEC — Syndrome Decoding
Syndrome defects (endpoints of error chains) are matched to identify the most likely error. MWPM (Minimum-Weight Perfect Matching) on the syndrome graph. Union-Find as a faster alternative.

**Papers**: Kitaev (1997, arXiv: quant-ph/9707021) — anyon fusion rules define matching on quasiparticle pairs; braiding statistics give the computation. Dennis et al. (2002, arXiv: quant-ph/0110143) — MWPM as the standard syndrome decoder for surface codes; matching syndrome defects to identify most likely error chain. de la Fuente et al. (2025) — JIT decoder uses MWPM with causal constraint (partial syndrome history). Oreshkov (2013) — continuous correction as streaming matching (implicit). Hastings & Haah (2021) — spacetime MWPM syndrome decoder for Floquet codes: syndromes are matched across both space and time, since the stabilizer group changes each period; the decoder must match defects that may span multiple time steps. Berry et al. (2023) — quantum algorithms for matching-related computations in TDA; Betti number estimation requires solving a matching-like problem on chain complex generators.

### Information Theory — Multiple Instances

1. **Belief Propagation** (Mézard & Mora, 2008): Approximate matching on factor graphs. For LDPC codes, equivalent to syndrome decoding. Survey Propagation as meta-level matching on the space of surveys.
2. **Blahut-Arimoto** (Blahut 1972, Arimoto 1972): THE foundational IT matching. Channel capacity C = max_{P(x)} I(X;Y) is optimal assignment of source symbols to channel inputs. Rate-distortion R(D) = min I(X;Y) s.t. E[d] ≤ D is minimum-cost soft matching between source and reproduction alphabets. Alternating minimization (fix one marginal, optimize the other) predates EM by 5 years. R(D) curve parameterized by D; slope = -s. 3000+ citations.
3. **Optimal transport**: Wasserstein distances between distributions (shared with TDA).
4. **Information geometry embeds in OT** (Wong & Yang, 2019, arXiv: 1906.00030): Fisher-Rao metric embeds in Wasserstein space via pseudo-Riemannian framework. The statistical manifold of distributions has a natural transport structure — information-geometric distances are a special case of optimal transport distances.

### Dynamical Systems (updated — third pass + Wave 9)
Previously marked as "rarely used." Third pass and Wave 9 found several instances:
1. **Ensemble control on Lie groups**: Single broadcast control must simultaneously steer all systems to respective targets — infinite-dimensional matching reduced to finite-dimensional via Cartan covering.
2. **IC-PINN coupling functions**: Basis-free inference = function-level matching from infinite-dimensional space to observed dynamics.
3. **Ordinal networks**: Hurst exponent estimation = matching to parameterized family of fractional processes.
4. **Spectral Wasserstein gradient flows** (Peyré, 2026): Muon optimizer dynamics = gradient flow on Spectral Wasserstein space. The Benamou-Brenier formulation makes optimization a continuous matching problem: the velocity field at each instant defines how mass is re-assigned. The dynamic and static (Kantorovich) formulations coincide for monotone norms — dynamics IS matching.

### Neuroscience (updated — third pass fills the gap)
Previously marked as "rarely used." Third pass found:
1. **Opponent striatal circuit**: D1/D2 opponent pairing — each D1 neuron encoding quantile tau implicitly paired with D2 neuron encoding 1-tau.
2. **ConformalHDC**: Nearest-centroid matching in high-dimensional space for hippocampal decoding.
3. **Driver fatigue GC**: Assigning causal roles (driver vs driven) to EEG channels is an implicit matching problem.
4. **Fused Unbalanced Gromov-Wasserstein** (Thual et al., 2022): Brain alignment across subjects via FUGW — simultaneously matches cortical regions by functional similarity (Wasserstein on fMRI responses) and anatomical proximity (Gromov-Wasserstein on mesh distances). Unbalanced transport allows partial matching when brain regions don't have 1-to-1 correspondences.
5. **OT for MEG/EEG source imaging** (Janati et al., 2019): Optimal transport regularizes the MEG inverse problem; the transport plan matches sensor-space measurements to source-space activations with spatial smoothness enforced by the Wasserstein cost.
6. **Hierarchical OT for neural decoding** (Lee et al., 2019): Multi-scale optimal transport matches neural population responses to stimulus categories, respecting the hierarchical structure of both neural representations and stimulus semantics.

## Two Cross-Machine Roles (updated — B3 sub-slice 3, pass 37)

### OT as proof technology (inbound to statistical physics)
Optimal transport can enter a result not as the object being studied but as the instrument that proves it: in bounded-memory belief propagation (Jain–Koehler–Liu–Mossel, arXiv: 1905.10031), Wasserstein bounds on message iterates are what force the memory-limited transition strictly below the Kesten–Stigum threshold — the Matching machine's cost geometry doing the work of a phase-transition proof (`by-structure/phase_transitions.md`). Read such instances as *matching-as-lemma*: the coupling is never the phenomenon, only the estimate carrier.

### PH → Matching bridge: filtration summary as measure
Chambers & Meng (arXiv: 2507.01171) compose the machines in the direction the atlas has few instances of: an extended persistence diagram (Parameterized homology's birth-death summary) is converted to a persistence image and used as the *probability measure* of the mm-space on which Gromov-Wasserstein matching runs — with scalar-field stability carried end-to-end. The filtration does not merely weight features for a classifier; it defines the measure over which relational matching is performed. Compare the reverse direction already catalogued (Matching metrics consuming topological descriptors) — this is Parameterized homology supplying Matching's ground data, not vice versa.

### Same theorem, two machines: Takens via conjugacy vs via pushforward (B3 sub-slice 5, pass 47)
Takens' delay embedding now exists in the corpus in two independent re-derivations that split along exactly the Lagrangian/Eulerian line the Matching machine's two roles trace:

1. **Matching-as-conjugacy** (Grigoryeva–Hart–Ortega, arXiv: 2108.05024): in driven reservoir systems, generalized synchronization *is* the embedding — the sync map is a topological conjugacy carrying the source attractor into reservoir state space, and Takens' delay coordinates fall out as the special case. Pointwise map on states, deterministic flows, fidelity certified by a conditional-Lyapunov spectral gap (`annotations/2401.00885.md`), dimension capped by pullback-attractor dimension (`annotations/2501.11357.md`).
2. **Matching-as-measure-coupling** (Botvinick-Greenhouse–Oprea–Maulik–Yang, arXiv: 2409.08768): the same theorem recast Eulerian-style — dynamics evolves a probability measure μ_t, and reconstruction becomes a pushforward Φ_#: P(M) → P(R^{2m+1}) between spaces of measures, solved with optimal-transport machinery. No trajectory is matched; only the image of the measure, which degrades continuously under sparse/noisy observation.

The pair is the cleanest corpus instance that the abstract machine survives a change of *description level* while its instances do not: what counts as "the coupling" (pointwise conjugacy vs induced measure coupling) and what counts as "reconstruction succeeds" (exact trajectory vs pushforward image) both shift, yet the Matching bookkeeping — assignment, cost, stability of the correspondence — is identical on both sides. Read them as one theorem observed from two sides of the Lagrangian/Eulerian divide, with the Stability machine supplying complementary certificates each way (spectral gap for the conjugacy side; measure-degradation robustness for the pushforward side).

## Key Divergences



- **Causal vs. batch**: Syndrome decoding (JIT) must commit before seeing future data. Diagram matching is batch. This is a genuine structural difference — see ANTISYNONYMS.md.
- **Cost function semantics**: Bottleneck = worst-case pairing cost. Wasserstein = total pairing cost. Syndrome graph = edge weight. These different cost functions produce different distances with different mathematical properties.
- **Matching to diagonal**: In TDA, unmatched points can be paired with the diagonal. In QEC, unmatched syndromes indicate an uncorrectable error. In information theory, unmatched symbols indicate a capacity violation.
