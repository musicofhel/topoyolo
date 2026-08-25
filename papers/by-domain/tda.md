# Topological Data Analysis

Papers from the TDA community, indexed by which abstract machines they instantiate. Cross-references to `by-structure/` files are given per paper.

---

## Mollers, Immer, Fortuin, Isufi (2023)
**"Hodge-Aware Contrastive Learning"**
arXiv: 2309.07364

**Domain(s)**: TDA, machine learning

**Abstract machines instantiated**:
- **Chain complex**: The paper's foundation is the simplicial complex X_2 with incidence matrices B_1 (node-to-edge) and B_2 (edge-to-triangle). The Hodge Laplacians L_0 = B_1 B_1^T, L_1 = B_1^T B_1 + B_2 B_2^T, L_2 = B_2^T B_2 are explicitly constructed from boundary operators. The condition B_1^T B_1 and B_2 B_2^T decomposing the 1-Hodge Laplacian into lower and upper parts encodes the chain complex structure: ∂^2 = 0 is implicit in the fact that im(B_1^T) ⊥ im(B_2) in the Hodge decomposition.
- **Parameterized homology**: The Hodge decomposition R^{N_1} = im(B_1^T) ⊕ im(B_2) ⊕ ker(L_1) decomposes edge signals into gradient, curl, and harmonic components. The harmonic space ker(L_1) IS the first homology of the complex — this is the Hodge theorem made computational. The SCNN filters H_t(L_1) act on these spectral subspaces, and the learned representations are parameterized by filter coefficients that weight gradient vs. curl vs. harmonic content.
- **Stability**: The augmentation design aims to preserve spectral properties: positive examples should have similar Hodge component proportions to the anchor. The reweighting of negative samples by Hodge-aware distance creates an embedding space where nearby points share spectral structure. This is an engineered stability — the embedding is constructed to be robust to augmentations that preserve spectral character.

**What is genuinely new (not reducible to shared abstraction)**:
- The key novelty is using the Hodge decomposition as inductive bias for contrastive learning. The three Hodge subspaces (gradient, curl, harmonic) provide interpretable structure that most graph contrastive methods ignore entirely. This is domain-specific to simplicial complexes — graphs lack the B_2 operator and therefore have no curl space.
- Spectral augmentation optimization: the augmentation parameters are tuned to preserve the Hodge decomposition of positive examples. This is a novel constraint on data augmentation with no analogue in standard CL.
- Hodge-aware negative reweighting in InfoNCE: negatives that are spectrally similar to the anchor are penalized more heavily. This creates embedding geometries that reflect the algebraic structure of the underlying complex.
- Outperforms fully supervised methods in label-scarce settings — demonstrating that the Hodge structure alone provides enough signal for downstream classification.

**Connections the authors acknowledge**: Cite simplicial signal processing (Barbarossa & Sardellitti, 2020), SCNN (Yang et al., 2022), and graph contrastive learning. Explicitly position against GNN-based CL which cannot handle edge flows. No citations to QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Incidence matrix B_k | Boundary operator ∂_k |
| Hodge Laplacian L_1 | ∂^T∂ + ∂∂^T (the Laplacian of the chain complex) |
| Harmonic space ker(L_1) | Homology H_1 (by Hodge theorem) |
| Gradient space im(B_1^T) | Coboundary image (exact 1-forms) |
| Curl space im(B_2) | Boundary image (2-chain boundaries) |
| Hodge decomposition | Cycle-boundary-harmonic splitting |
| Simplicial complex X_2 | 2-dimensional chain complex |
| SCNN filter H_t(L_1) | Linear operator parameterized by spectral weights |
| Spectral augmentation | Perturbation within a spectral subspace |
| Hodge-aware distance | Distance respecting the chain complex decomposition |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`

---

## Di Rocco, Eklund, Weinstein (2019)
**"The Bottleneck Degree of Algebraic Varieties"**
arXiv: 1904.04502

**Domain(s)**: TDA (algebraic geometry interface), computational geometry

**Abstract machines instantiated**:
- **Matching**: Bottlenecks are pairs (x, y) of distinct points on an algebraic variety X where the connecting line is normal to X at both points. This is an optimal assignment problem: find the critical points of the squared distance function ||x - y||^2 subject to x, y in X. The bottleneck degree counts these critical points — it is the algebraic complexity of the matching problem on the variety.
- **Stability**: The reach tau_X = min(rho, b) where rho is minimal geodesic curvature radius and b is half the narrowest bottleneck width. The reach controls persistent homology: it determines the sample density needed to recover correct homology from point clouds. By computing bottleneck degree, one bounds the computational complexity of estimating the reach, which in turn controls the stability of topological inference.
- **Parameterized homology**: The connection to persistent homology is explicit: the reach determines the scale parameter at which the Rips/Cech complex of a sample correctly recovers the homology of the underlying manifold. The bottleneck degree bounds how many critical parameter values (scale parameters) exist where the topology might change.

**What is genuinely new (not reducible to shared abstraction)**:
- The bottleneck degree as an algebraic invariant: expressed in terms of Chern classes and polar classes of the variety. This connects computational TDA (reach estimation) to classical intersection theory in algebraic geometry — a bridge that goes beyond the standard TDA toolkit.
- Explicit formulas in low dimension: for curves in R^n, the bottleneck degree is 2(delta^2 - delta) where delta is the algebraic degree. For surfaces, the formula involves both degree and Euler characteristic.
- The algorithm to compute bottleneck degree in general dimension via numerical algebraic geometry (homotopy continuation). This provides a concrete computational pathway from algebraic invariants to topological inference guarantees.
- The observation that bottleneck pairs connect distinct connected components — the narrowest bottleneck bounds the minimum inter-component distance.

**Connections the authors acknowledge**: Explicit connection to persistent homology and the reach (Niyogi, Smale, Weinberger, 2008; Aamari & Levrard). Cite Johnson-Lindenstrauss dimensionality reduction and manifold triangulation as downstream applications. Situated at the algebraic geometry / data science interface. No connections to QEC, dynamical systems, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Bottleneck pair (x, y) | Matched feature pair (critical pairing) |
| Bottleneck degree | Algebraic complexity of the matching |
| Reach tau_X | Stability radius for topological inference |
| Normal line at x | Orthogonal complement to tangent (gradient direction) |
| Squared distance critical points | Optimal assignment solutions |
| Chern classes | Intrinsic algebraic invariants of the variety |
| Polar classes | Projective invariants (intersection-theoretic) |
| Homotopy continuation | Numerical path-following to enumerate solutions |
| Hausdorff distance | Perturbation metric between point sets |
| Bottleneck width | Minimum cost in the matching |

**See also**: `by-structure/optimal_transport.md`, `by-structure/filtrations.md`

---

## de Jesus Jr., Fernandez-Navarro, Carbonero-Ruz (2025)
**"Enhancing Financial Time Series Forecasting through Topological Data Analysis"**
DOI: 10.1007/s00521-024-10787-x | Neural Computing and Applications 37:6527-6545

Full annotation: `annotations/10.1007-s00521-024-10787-x.md` (promoted from this prose block, B2 pass 20).

---

## Kanjamapornkul, Pincak, Bartos (2020)
**"Cohomology Theory for Financial Time Series"**
DOI: 10.1016/j.physa.2019.122212 | Physica A 546:122212

**Domain(s)**: TDA (algebraic topology applied to finance), mathematical physics

**Abstract machines instantiated**:
- **Chain complex**: The paper constructs Khovanov cohomology on financial time series data. The chain and cochain groups are built from market microstructure states (bid-ask interactions). The coboundary operators arise from the knot/link structure of figure-eight hyperbolic knots in the time series phase space. The condition delta^2 = 0 is inherited from the standard Khovanov cohomology construction. The cohomology groups classify market states.
- **Parameterized homology**: The market phase transitions are parameterized: the paper proves the existence of 8 market states (Theorem 2) and 16 physiological cones classifying all possible endpoint states. As the Wilson loop parameter varies, the cohomological invariants change — this is a parameterized cohomology over the space of trader interactions.
- **Joint-vs-marginal excess**: Chern-Simons currents arise from the interaction of trader behavior fields. The current measures a geometric phase that is absent from individual trader actions but emerges from their joint interaction — the arbitrage opportunity in the bid-ask spread is a joint-vs-marginal excess phenomenon.

**What is genuinely new (not reducible to shared abstraction)**:
- Application of Khovanov cohomology (a categorification of the Jones polynomial from knot theory) to financial data. This is an unusual bridge — Khovanov cohomology was developed for low-dimensional topology, and its application to time series is highly non-standard.
- The Yang-Mills field interpretation of trader behavior, with Chern-Simons currents representing arbitrage opportunities. This imports gauge theory into financial modeling.
- The proof that market microstructure has exactly 8 or 16 fundamental states, derived from the knot/link structure of the time series. The connection between tick sizes and topological invariants of the phase space is novel.
- Path integral formulation of market phase transitions using Wilson loops — treating the market as a quantum field theory on the time series manifold.

**Connections the authors acknowledge**: Explicitly draw from mathematical physics (Chern-Simons theory, Yang-Mills fields, Wilson loops, spinor fields). Cite econophysics literature. The paper IS a cross-domain bridge between gauge theory/knot theory and finance. No connections to TDA community proper (persistent homology, stability), dynamical systems, or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Khovanov cohomology | Cohomology of the chain complex (categorified) |
| Cochain/chain | Elements of the chain complex |
| Coboundary operator delta | Dual of boundary operator ∂ |
| Chern-Simons current | Geometric phase (joint-vs-marginal excess) |
| Wilson loop | Path integral over the chain complex |
| Market 8 states | Homology classes (classification) |
| Figure-eight knot | Topology of the time series phase space |
| Bid-ask spread | Boundary between market states |
| Yang-Mills field | Connection on the chain complex (gauge field) |
| Arbitrage opportunity | Non-trivial cohomology class (exploitable structure) |
| Phase transition | Critical parameter value (topology change) |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-structure/composite_systems.md`

---

## Adams, Chepushtanova, Emerson, Hanson, Kirby, Motta, Neville, Peterson, Shipman, Ziegelmeier (2017)
**"Persistence Images: A Stable Vector Representation of Persistent Homology"**
arXiv: 1507.06217

**Domain(s)**: TDA

**Abstract machines instantiated**:
- **Parameterized homology**: Persistence images vectorize the output of parameterized homology. Pipeline: PD -> birth-persistence coordinates -> weighted Gaussian sum (persistence surface) -> pixel grid integration -> R^n vector. Concatenation across homological dimensions (H_0, H_1, ...) into a single vector. Three user choices: resolution, distribution variance, weighting function.
- **Stability**: Central contribution. Persistence surface is Lipschitz w.r.t. 1-Wasserstein: ||rho_B - rho_{B'}||_inf <= C * W_1(B, B'). Extends to discretized PI vectors (L_inf, L_1, L_2 bounds). Tighter constants for Gaussians (Theorems 3-4). Impossibility: PI kernel NOT stable for W_p with p > 1.
- **Matching**: The Wasserstein distance used in stability bounds IS an optimal matching (bijection between diagram points minimizing total displacement). Stability proofs bound PI differences via the matching that achieves the Wasserstein infimum.
- **Chain complex**: Implicit. Input PDs come from Vietoris-Rips (simplicial) or sublevel set (cubical) chain complexes. Appendix A defines the full chain complex machinery (C_k, partial_k, Z_k, B_k, H_k).

**What is genuinely new (not reducible to shared abstraction)**:
- The vectorization pipeline itself: weighting function + Gaussian smoothing + grid integration simultaneously achieves stability, interpretability, and fixed-dimensionality.
- Domain-adaptable weighting function f (zero on diagonal, continuous, piecewise differentiable) — standard choice weights by persistence, but non-standard weightings also covered.
- Impossibility result: stability only achievable for W_1, not W_p (p > 1).
- Dynamical systems applications: linked twist map (82.5%) and anisotropic Kuramoto-Sivashinsky PDE (97.3%) parameter classification via PIs.
- Sparse SVM pixel selection: 10 out of 400 pixels achieve 100% accuracy, with interpretable correspondence to PD regions.

**Connections the authors acknowledge**: Persistence landscapes (Bubenik 2015), kernel methods (Reininghaus et al. 2015), PH stability (Cohen-Steiner et al. 2007). No connections to QEC, information theory, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Persistence diagram | Output of parameterized homology |
| Persistence image | Fixed-size vector featurization of parameterized homology |
| Persistence surface rho_B | Continuous featurization (pre-discretization) |
| Weighting function f | Importance modulation on diagram features |
| 1-Wasserstein distance W_1 | Optimal matching cost (L1 transport) |
| Bottleneck distance W_inf | Optimal matching cost (minimax transport) |
| Gaussian phi_u | Smoothing kernel (localization in feature space) |
| Vietoris-Rips complex | Chain complex from point cloud |
| Sublevel set filtration | Chain complex from function |
| SSVM pixel selection | Discriminatory feature identification |

**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`

---

## Bauer (2021)
**"Ripser: efficient computation of Vietoris-Rips persistence barcodes"**
arXiv: 2108.03831 | Journal of Applied and Computational Topology 5:391-423

THE standard computational tool for PH. Implicit coboundary matrix representation (never materializes full matrix). Three optimizations: apparent pairs, emergent pairs, clearing -- identify most persistence pairs without full column reduction. 40-1000x speedups over GUDHI/Dionysus/DIPHA. De facto standard for VR persistent homology. Full annotation: `annotations/2108.03831.md`.
**Machines**: chain complex (VR complex with coboundary matrix), parameterized homology (persistence algorithm computes birth-death pairs across filtration).
**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`

---

## Cross-listed from Dynamical Systems

- **Zhou, Chu, Xu, Liu, Yu (2020)** — "Detecting Predictable Segments of Chaotic Financial Time Series via Neural Network." Phase space reconstruction + SOM clustering to detect predictable vs. chaotic segments. Full annotation: `annotations/10.3390-electronics9050823.md` (promoted B2 pass 19). Machines: parameterized homology, null hypothesis.

---

## Cross-listed from Machine Learning / Optimal Transport

- **Bunne, Alvarez-Melis, Krause, Jegelka (2019)** — "Learning Generative Models across Incomparable Spaces." Gromov-Wasserstein GANs for cross-domain generative modeling. Full annotation in `by-domain/dynamical_systems.md` (cross-domain). Machines: matching, stability.

---

## Cross-listed from Second Pass + Bridges

- **Niroomand & Wales (2023)** — "Physics-Inspired Interpretability." Disconnectivity graphs = H₀ persistence diagrams, independently invented by energy landscape theory. Conserved weights = persistent features. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, stability, null hypothesis, joint-vs-marginal (weak). **KEY FINDING: same mathematical object, zero cross-citation.**

- **Gallicchio & Micheli (2020)** — "Fast and Deep Graph Neural Networks." Layer depth = scale parameter (Rips-like). Banach contraction = stability. Untrained random weights suffice — topology carries the information. Full annotation: `cross_domain_bridges.md`. Machines: stability, parameterized homology, null hypothesis, chain complex. **Bridge: dynamics + TDA.**

---

## Wave 2 (2026-04-06) — Thin Cell Papers

### Divol & Lacombe (2019) — OT for Persistence Diagrams
**"Understanding the Topology and the Geometry of the Space of Persistence Diagrams via Optimal Partial Transport"**
arXiv: 1901.03048
PD distances = optimal partial transport (exact theorem). Radon measure extension. Fréchet means. All continuous linear representations characterized.
**Machines**: matching, stability. **See also**: `by-structure/optimal_transport.md`.

### Vejdemo-Johansson & Mukherjee (2018) — Multiple Testing with PH
**"Multiple testing with persistent homology"**
arXiv: 1812.06491
Universal empirical null distribution for PH features. FWER and FDR control for rejecting acyclicity. Grounded in limit theorems for PH of point processes.
**Machines**: null hypothesis, stability. **See also**: `by-structure/phase_transitions.md`.

### Harrington, Otter, Schenck, Tillmann (2017) — Stratifying Multiparameter PH
**"Stratifying multiparameter persistent homology"**
arXiv: 1708.07390
Joint bifiltration captures structure invisible to single-parameter PH. Multigraded associated primes, Hilbert series, local cohomology as partial invariants. No complete discrete invariant exists (unlike 1-parameter barcode).
**Machines**: joint-vs-marginal, parameterized homology, chain complex. **See also**: `by-structure/composite_systems.md`, `by-structure/filtrations.md`.

### Perea & Harer (2013) — Sliding Windows and Persistence (SW1PerS)
**"Sliding Windows and Persistence: An Application of Topological Methods to Signal Analysis"**
arXiv: 1307.6188. Full annotation: `annotations/1307.6188.md`.
Sliding window embedding → point cloud → Rips complex → PH. Maximum H₁ persistence = periodicity score. Convergence theorems + dependency estimates for window size / embedding dimension. Formal bridge between Takens (dynamical systems) and persistence (TDA).
**Machines**: chain complex, parameterized homology, stability. **See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`. **Bridge: TDA + dynamical systems.**

### Cohen-Steiner, Edelsbrunner, Harer (2007) — Stability of Persistence Diagrams
**"Stability of Persistence Diagrams"**
arXiv: math/0604068. Full annotation: `annotations/math-0604068.md`.
THE foundational stability theorem. d_B(Dgm(f), Dgm(g)) ≤ ||f - g||∞. Bottleneck distance = optimal matching between diagram points. Made TDA rigorous. Proof via interleaving of filtrations — template for all subsequent stability results.
**Machines**: stability, matching, parameterized homology. **See also**: `by-structure/phase_transitions.md`, `by-structure/optimal_transport.md`.

### Barannikov, Trofimov, Sotnikov et al. (2021) — Manifold Topology Divergence (Cross-Barcode)
**"Manifold Topology Divergence: a Framework for Comparing Data Manifolds"**
arXiv: 2106.04024
Cross-Barcode(P,Q) tracks multiscale topological discrepancies between two manifold-supported distributions. MTop-Divergence detects mode-dropping, mode-collapse, mode-invention. Scales linearly with dimension. Domain-agnostic (images, 3D shapes, time series). Conceptually distinct from comparing two PDs via Wasserstein — builds a SINGLE barcode from the pair.
**Machines**: joint-vs-marginal, parameterized homology, matching, null hypothesis. **See also**: `by-structure/composite_systems.md`.

---

## Cross-listed from Neuroscience + Information Theory

- **Peek, Pritam, Skerritt, Chalup (2025)** — "Time Series Analysis of Spiking Neural Systems via Transfer Entropy and Directed Persistent Homology." Directed flag complexes from TE-derived weighted directed graphs, analyzed via Flagser. Inverted TE filtration. Applied to synthetic SNNs and mouse cortical recordings. Triple-domain bridge. Full annotation: `annotations/2508.19048.md` (arXiv: 2508.19048). Machines: chain complex, parameterized homology, null hypothesis.

---

## Third Pass (2026-04-05)

### Structure-Preserving Contrastive Learning for Spatial Time Series
**Domain(s)**: TDA, dynamical systems, machine learning
First use of persistent homology as regularizer for contrastive learning of time series. Wasserstein metric on persistence diagrams bounds topological distortion. Dual-scale: global PH + local graph geometry.
**Machines**: parameterized homology, joint-vs-marginal, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-01).

### Thai Stock Market de Rham Cohomology
**Domain(s)**: TDA (algebraic topology), dynamical systems
Full de Rham cohomology + gauge theory (Wilson loops, Chern-Simons currents) applied to financial correlation matrices. Novel import from mathematical physics — standard in gauge field theory, new in finance.
**Machines**: chain complex, parameterized homology, null hypothesis, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-02).
**See also**: `by-structure/boundary_operators.md`

### Higher-Order Network Compression (PRL) — Bravo Abad
**Domain(s)**: TDA (higher-order networks), information theory
Information-theoretic criterion for which interaction orders in a hypergraph carry genuinely new information. k-body interactions predictable from (k-1)-body = no excess → compress away. Genuinely new information at order k = non-trivial homology at grade k.
**Machines**: chain complex, joint-vs-marginal, null hypothesis.
Full annotation: `third_pass_dynamics_tda.md` (TP-10).
**See also**: `by-structure/boundary_operators.md`, `by-structure/composite_systems.md`

### Hom-Lie Algebra Cochain Complexes
**Domain(s)**: Pure mathematics (algebra), TDA (cohomological structures)
Cochain complexes for hom-Lie algebras with twisted Jacobi identity. δ²=0 explicitly constructed. Twisting map α parameterizes family of algebraic structures; α=id recovers Chevalley-Eilenberg cohomology. H² controls deformations, H³ gives obstructions.
**Machines**: chain complex, parameterized homology, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-14).
**See also**: `by-structure/boundary_operators.md`

### Deep Arbitrary Polynomial Chaos Neural Networks (DaPC NN)
**Domain(s)**: Machine learning, dynamical systems (UQ)
Reinterprets DNN layers via data-driven polynomial chaos expansion. Polynomial order p as filtration parameter. Layer-wise orthonormal bases create graded functional decomposition analogous to Hodge theory. Conventional DNN as null.
**Machines**: chain complex (weak), parameterized homology, null hypothesis.
Full annotation: `third_pass_dynamics_tda.md` (TP-13).

---

## Cross-listed from QEC (Wave 5)

- **Berry et al. (2023)** — "Analyzing Prospects for Quantum Advantage in Topological Data Analysis." PRX Quantum 4, 040349. Quantum algorithm for Betti number estimation via chain complex (boundary operators, combinatorial Laplacian, Dirac operator). Super-quadratic speedup requires growing Betti number + multiplicative error. Dequantization via Monte Carlo on k-simplices. DIRECT TDA-QEC bridge. Full annotation: `annotations/2508.19048.md`. Machines: chain complex, parameterized homology, stability, null hypothesis. **See also**: `cross_domain_bridges.md`, `by-domain/qec.md`.

---

## Cross-listed from Information Theory + Neuroscience (Wave 7)

- **Varley, Mediano, Patania & Bongard (2025)** — "The topology of synergy." PLoS Comput. Biol., DOI: 10.1371/journal.pcbi.1013649, arXiv: 2504.10140. 4 citations. First empirical demonstration that H2 persistent homology features (three-dimensional cavities in Rips filtration) correspond to synergistic information (O < 0), while knots correspond to redundancy (O > 0). Chebyshev distance for both TDA (Ripser) and KNN information estimation (JIDT). In fMRI: avg H2 persistence vs normalized O-information rho = -0.55 to -0.65. PCA systematically destroys synergy while preserving redundancy. EXPLICIT TDA-information theory bridge. Full annotation: `annotations/2508.19048.md` (Wave 7). Machines: chain complex, parameterized homology, joint-vs-marginal, null hypothesis, stability. **See also**: `cross_domain_bridges.md`, `by-domain/information_theory.md`, `by-domain/neuroscience.md`, `by-structure/composite_systems.md`, `by-structure/filtrations.md`.

- **Hamilton & Leditzky (2023/2024)** — "Probing Multipartite Entanglement Through Persistent Homology." Commun. Math. Phys. 405, article 125. arXiv: 2307.07492. 8 citations. PH applied to multipartite quantum entanglement. Filtration driven by q-deformed total correlation (multipartite, not pairwise). Main theorem: integrated Euler characteristic = n-tangle (standard entanglement monotone at q=2). Barcodes strictly finer than n-tangle — distinguish SLOCC orbits with identical τ_n. Relative PH connects to strong subadditivity. DIRECT TDA-QEC bridge. Full annotation: `annotations/2508.19048.md` (Wave 7). Machines: joint-vs-marginal, chain complex, parameterized homology, stability, matching, null hypothesis. **See also**: `by-domain/qec.md`, `by-structure/composite_systems.md`, `by-structure/boundary_operators.md`.

- **Natarajan, Chaplin, Bull et al. (2026)** — "Topology of Multi-species Localization." arXiv: 2603.03237. M2S2 framework: kernel/image/cokernel persistence of k-chromatic gluing map decomposes multi-species point cloud PH into four categories — features common to subsets, destroyed by composition, ONLY visible in joint, and formed by some persisting with others. Cokernel = pure topological joint-vs-marginal excess. Chromatic Delaunay-Cech filtration solves functoriality problem. Applied to tumor microenvironment: recovers immunoediting regimes, identifies higher-order spatial interactions (periostin-macrophage, trichromatic T-cell triples). Full annotation: `annotations/2508.19048.md` (Wave 7). Machines: joint-vs-marginal, chain complex, parameterized homology, null hypothesis, stability. **See also**: `by-structure/composite_systems.md`, `by-structure/boundary_operators.md`.

---

## Wave 8 — Matching in TDA (2026-04-07)

- **Bubenik & Elchesen (2019)** — "Universality of persistence diagrams and the bottleneck and Wasserstein distances." Computational Geometry, arXiv: 1912.02563. 15 citations. Proves bottleneck and Wasserstein distances on PDs arise from universal constructions — they are THE canonical optimal matching metrics. 1-Wasserstein satisfies Kantorovich-Rubinstein duality. Universality: for any metric space with basepoint, these distances are unique satisfying the universal property. Extends to multiparameter persistence. Full annotation: `annotations/2508.19048.md` (Wave 8). Machines: matching, stability. **See also**: `by-structure/optimal_transport.md`, `atlas/MATCHING.md`.

- **Chen & Wang (2021)** — "Approximation algorithms for 1-Wasserstein distance between persistence diagrams." JMLR, arXiv: 2104.07710. 9 citations. Near-linear time approximation algorithms for 1-Wasserstein on PDs via randomly shifted quadtrees. Key technical novelty: handling the diagonal as infinite reservoir of zero-cost points (standard OT assumes finite discrete measures). 100-1000x speedup over Hungarian/auction with <1% approximation error. Full annotation: `annotations/2508.19048.md` (Wave 8). Machines: matching, stability. **See also**: `by-structure/optimal_transport.md`, `atlas/MATCHING.md`.

---

## Wave 9 — Spectral Wasserstein (2026-04-07)

- **Peyré (2026)** — "Muon Dynamics as a Spectral Wasserstein Flow." arXiv: 2604.04891. Gabriel Peyré (CNRS/ENS). Family of Spectral Wasserstein distances W_γ on measures, parameterized by Schatten norm index p: trace norm (p=1) → classical W2, operator norm (p=∞) → Muon geometry. Cost depends on global displacement covariance matrix, not per-particle scalar costs. Kantorovich (static matching) = Benamou-Brenier (dynamic gradient flow) for monotone norms. Metric equivalence with W2: √c_γ · W2 ≤ W_γ ≤ √C_γ · W2. Geodesic convexity. Gaussian closed form extends Bures metric. Full annotation: `annotations/2508.19048.md` (Wave 9). Machines: matching, parameterized homology, stability, chain complex (weak). **See also**: `by-domain/dynamical_systems.md`, `by-structure/optimal_transport.md`, `atlas/MATCHING.md`, `atlas/STABILITY.md`.

---

## Wave 10 — link-forge update (2026-04-17)

- **Baudot, Tapia, Bennequin & Goaillard (2019)** — "Topological Information Data Analysis." arXiv: 1907.04242. I_k co-chains on simplicial complex of variables, coboundary δH = I_2. Bridges TDA and information theory via topos cohomology. Full annotation: `annotations/2508.19048.md` (Wave 10a). Machines: chain complex, joint-vs-marginal, null hypothesis, parameterized homology, stability. **See also**: `by-domain/information_theory.md`, `papers/cross_domain_bridges.md`.

- **Ghorbanchian, Restrepo, Torres & Bianconi (2020)** — "Higher-order simplicial synchronization of coupled topological signals." Nature Comms Physics, DOI: 10.1038/s42005-021-00605-4. Hodge Laplacian dynamics on simplicial complexes. Topological signals on k-simplices. Explosive synchronization at critical coupling. Hysteresis. Full annotation: `annotations/2508.19048.md` (Wave 10a). Machines: chain complex, parameterized homology, stability. **See also**: `by-domain/dynamical_systems.md`, `papers/cross_domain_bridges.md`.

- **Dey, Mrozek & Slechta (2021)** — "Persistence of Conley-Morse Graphs in Combinatorial Dynamical Systems." arXiv: 2107.02115. Zigzag persistence on Conley-Morse graphs. Conley index as relative homology. Noise-resilient index pairs. Full annotation: `annotations/2508.19048.md` (Wave 10a). Machines: chain complex, parameterized homology, stability. **See also**: `by-domain/dynamical_systems.md`, `papers/cross_domain_bridges.md`.

- **Petri, Expert, Turkheimer, Carhart-Harris, Nutt, Hellyer & Vaccarino (2014)** — "Homological scaffolds of brain functional networks." J. R. Soc. Interface, DOI: 10.1098/rsif.2014.0873. 657 citations. Homological scaffold: network encoding which edges carry persistent cycles in brain fMRI. Psilocybin vs placebo. Full annotation: `annotations/2508.19048.md` (Wave 10a). Machines: chain complex, parameterized homology, null hypothesis. **See also**: `by-domain/neuroscience.md`, `papers/cross_domain_bridges.md`.

- **Lord, Expert, Fernandes, Petri, Van Hartevelt, Vaccarino, Deco, Turkheimer & Kringelbach (2016)** — "Insights into Brain Architectures from the Homological Scaffolds of the Structural Connectome." DOI: fnsys.2016.00085. Extends Petri et al. 2014 scaffold method to resting-state fMRI. Homological scaffold from weighted clique complex tracks which edges carry persistent cycles. Chain complex with weight filtration; parameterized homology across correlation threshold. Full annotation: `annotations/2508.19048.md` (Wave 10c). Machines: chain complex, parameterized homology. **See also**: `by-domain/neuroscience.md`, `by-structure/boundary_operators.md`, `by-structure/filtrations.md`.

- **Chung, El-Yaagoubi, Qiu & Ombao (2025)** — "From Density to Void." arXiv: 2503.14700. Simplicial complexes from fMRI with explicit ∂_k. Null result: higher-order brain topology fails FDR and cross-subject replication. Anti-stability. Methodological critique of TDA applied to brain networks. Full annotation: `annotations/2508.19048.md` (Wave 10b). Machines: chain complex, null hypothesis, stability (anti). **See also**: `by-domain/neuroscience.md`, `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`.

- **Donato et al. (2016)** — "Persistent Homology analysis of Phase Transitions." arXiv: 1601.03641. PH detects topological phase transitions in configuration space. Rips complex on sampled points; energy density ε as parameter. MFXY model (positive) vs φ^4 (negative control). Persistence landscapes with confidence bands. Full annotation: `annotations/2508.19048.md` (Wave 10b). Machines: chain complex, parameterized homology, stability, null hypothesis. **See also**: `by-domain/dynamical_systems.md`, `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-structure/phase_transitions.md`, `papers/cross_domain_bridges.md`.

- **Batko, Mischaikow, Mrozek & Przybylski (2019)** — "Conley Index Approach to Sampled Dynamics." arXiv: 1904.03757. Cohomological Conley index from weak index pairs. Sunflower enclosure: data → multivalued map → Conley index → semiconjugacy to symbolic dynamics. Binning scale δ as filtration parameter. Isolating neighborhoods persist under ε-perturbation. Full annotation: `annotations/2508.19048.md` (Wave 10b). Machines: chain complex, parameterized homology, stability. **See also**: `by-domain/dynamical_systems.md`, `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-structure/phase_transitions.md`.

- **Jost & Zhang (2023)** — "Cheeger inequalities on simplicial complexes." arXiv: 2302.01069. Higher-order Cheeger constants for simplicial complexes. Spectral gap of k-Hodge Laplacian bounded by Cheeger constant h_k: explicit two-sided inequality. Connects combinatorial topology (chain complex boundary operators) to spectral stability of simplicial signals. Full annotation: `annotations/2508.19048.md` (Wave 10c). Machines: chain complex, stability. **See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`.

- **Curry, DeSha, Hoff, Limberger, Luo & Qin (2022)** — "Decorated merge trees for persistent topology." DOI: s41468-022-00089-3. Decorated merge trees (DMTs) as algebraic invariant for persistent homology. Functorial: PH module → DMT via R[x]-module interleaving. Gromov-Wasserstein coupling between DMTs defines a stable metric. Connects chain complex (boundary operators on merge tree edges), matching (GW coupling), and stability (interleaving distance bounds). Full annotation: `annotations/2508.19048.md` (Wave 10c). Machines: chain complex, matching, stability. **See also**: `by-structure/boundary_operators.md`, `by-structure/optimal_transport.md`, `by-structure/phase_transitions.md`.

- **Méndez & Sánchez-García (2020)** — "A Directed Persistent Homology Theory for Dissimilarity Functions." arXiv: 2008.00711. Extends PH to directed spaces via pre-ordered Rips complex and asymmetric dissimilarity functions. Directed boundary operators on oriented simplices. Parameterized homology over directed filtration — captures asymmetric relationships invisible to standard (symmetric) PH. Full annotation: `annotations/2508.19048.md` (Wave 10c). Machines: chain complex, parameterized homology. **See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`.

- **Panaretos & Zemel (2019)** — "Statistical Aspects of Wasserstein Distances." DOI: annurev-statistics-030718-104938. 913 citations. Comprehensive review of W_p family as statistical tools. Bottleneck distance on PDs IS W_∞. Otto calculus gives Riemannian geometry of Wasserstein space. Full annotation: `annotations/2508.19048.md` (Wave 10b). Machines: matching, stability, parameterized homology. **See also**: `by-domain/information_theory.md`, `by-structure/optimal_transport.md`.

- **Grande & Schaub (2023)** — "Topological Point Cloud Clustering." arXiv: 2303.16716. Clusters point-cloud points by their contribution to global topological features: sparse eigenvectors of the full family of Hodge Laplacians {L_k} on a complex built from the cloud, instead of L_0 of the pairwise graph alone. Pushes homological structure down to per-point labels; no filtration/persistence machinery. Full annotation: `annotations/2303.16716.md` (pass 15, batch-002). Machines: chain complex, matching, stability. **See also**: `by-structure/boundary_operators.md`.

## B2 batch-005 — ph-stability foundations (2026-08-25)

- **Bubenik & Scott (2012)** — "Categorification of persistent homology." arXiv: 1205.3669. Persistence modules as diagrams indexed by (ℝ, ≤) in an arbitrary target category; interleaving distance generalizes the bottleneck distance; stability theorems greatly generalized, and a category of interleavings constructed (abelian when the target is). Categorical backbone upstream of every applied-PH entry in this atlas. Machines: parameterized homology, stability, matching. Full annotation: `annotations/1205.3669.md` (B2 pass 32). **See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`.

- **Gulen & McCleary (2022)** — "Galois Connections in Persistent Homology." arXiv: 2201.06650. Interleavings and matchings unified as one Galois-connection structure; Rota's theorem yields a substantially easier proof of bottleneck stability; multiparameter persistence diagram notions related. Order-theoretic proof-technology transfer into a stability proof. Machines: parameterized homology, matching, stability. Full annotation: `annotations/2201.06650.md` (B2 pass 32). **See also**: `by-structure/filtrations.md`, `by-structure/optimal_transport.md`, `by-structure/phase_transitions.md`.

- **Perez (2020)** — "On C0-persistent homology and trees." arXiv: 2012.02634. Metric tree construction faithfully identifying superlevel-set connected components of R-valued continuous functions; H0 persistence diagram retrievable from the tree; quantitative Wasserstein stability for α-Hölder functions on regular X; homological dimension bounded by upper-box dimension (partial answer to Schweinhart). Applications to random fields' superlevel-set topology. Machines: parameterized homology, stability, matching (weak). Full annotation: `annotations/2012.02634.md` (B2 pass 33). **See also**: `by-structure/filtrations.md`.

- **Broomhead & Pirashvili (2025)** — "An isometry theorem for persistent homology of circle-valued functions." arXiv: 2506.02999. Persistence modules over circle-valued functions: barcodes generalised to arcs on a derived-category-of-quivers geometric model; extended interleaving and bottleneck distances defined; ISOMETRY theorem equating the two exactly. Upgrades the Matching↔Stability duality from inequality to equality, and extends the apparatus past the monotone (ℝ, ≤) index to a cyclic one. Machines: parameterized homology, stability, matching. Full annotation: `annotations/2506.02999.md` (B2 pass 33). **See also**: `by-structure/filtrations.md`.

- **Carlsson (2020)** — "Persistent Homology and Applied Homotopy Theory." arXiv: 2004.00738. Survey: persistence module theory, stability theorems for barcodes, generalized (multidimensional) persistence, barcode vectorization and applications. Canonical single-reference anchor for the Filtrations×Stability cell; its generalized-persistence section marks where the single-parameter machine strains. Machines: parameterized homology, stability, chain complex, matching (tooling). Full annotation: `annotations/2004.00738.md` (B2 pass 33). **See also**: `by-structure/filtrations.md`.

## B2 batch-006 — GW-theory core (2026-08-25)

The Matching machine's own mathematical literature — invariance, statistical inference, and the Kantorovich/Monge split, previously touched only through applications.

- **Weitkamp, Proksch, Tameling & Munk (2020)** — "Gromov-Wasserstein Distance based Object Matching: Asymptotic Inference." arXiv: 2006.12287. Objects as metric measure spaces; a beta-trimmed lower bound of the GW distance yields a pose-invariant discrimination test; distributional limits via weak convergence of a U-type process indexed by β ∈ [0, 1/2); applied to structural protein comparison. The Matching functional given sampling theory — null hypothesis and matching in one object. Machines: matching, null hypothesis, stability (distributional). Full annotation: `annotations/2006.12287.md` (B2 pass 35). **See also**: `by-structure/optimal_transport.md`, `by-structure/phase_transitions.md`.

- **Mémoli & Needham (2022)** — "Comparison Results for Gromov-Wasserstein and Gromov-Monge Distances." arXiv: 2212.14123. GW (coupling) vs GM (map) formulations compared: equal exactly for non-atomic metric measure spaces; bi-Hölder equivalence between GM and an isometry-invariant Monge OT distance from shape/image analysis. The Kantorovich-vs-Monge split resolved *inside* the Matching machine — when hard assignment costs nothing over soft. Machines: matching, stability (bi-Hölder control). Full annotation: `annotations/2212.14123.md` (B2 pass 35). **See also**: `by-structure/optimal_transport.md`.

- **Lim & Mémoli (2022)** — "Classical Multidimensional Scaling on Metric Measure Spaces." arXiv: 2201.09385. cMDS generalized to arbitrary mm-spaces with a full spectral theory; sum of negative eigenvalues of the cMDS operator as a new non-flatness invariant (zero exactly on Euclidean-flat structure); stability of the cMDS output proven w.r.t. GW distance on inputs — perturbation control across two instantiations of the matching family. Machines: matching, stability, null hypothesis (weak, flatness-as-reference). Full annotation: `annotations/2201.09385.md` (B2 pass 35). **See also**: `by-structure/optimal_transport.md`, `by-structure/phase_transitions.md`.

- **Chambers & Meng (2025)** — "A Stable and Theoretically Grounded Gromov-Wasserstein Distance for Reeb Graph Comparison using Persistence Images." arXiv: 2507.01171. Reeb graphs as mm-spaces compared by GW; the probability measure built from persistence images of extended persistence diagrams; symmetric Reeb radius for geometric robustness; scalar-field-perturbation stability proven end-to-end — filtration summary → weighting → relational matching in one pipeline. Machines: matching, parameterized homology (consumed), stability. Full annotation: `annotations/2507.01171.md` (B2 pass 36). **See also**: `by-structure/optimal_transport.md`, `by-structure/filtrations.md`.

- **Hohmeier, Fraiman & Moosmueller (2026)** — "k-Nearest Neighbors in Gromov--Wasserstein Space." arXiv: 2606.10295. Universal consistency of GW-k-NN and fGW-k-NN on weak-isomorphism classes of finite mm-spaces (hence on graphs and node-attributed graphs) — a learning-theoretic guarantee living directly on Matching-space geometry, with quotient-by-isomorphism made load-bearing. Machines: matching, stability (consistency form), null hypothesis (weak, quotienting). Full annotation: `annotations/2606.10295.md` (B2 pass 36). **See also**: `by-structure/optimal_transport.md`, `by-structure/phase_transitions.md`.

- **Yachimura & Zou (2026)** — "Entropic Partial Optimal Transport and Partial Gromov--Wasserstein Distance between Gaussian Mixtures." arXiv: 2608.09265. Partial (mass-conservation-relaxed) GW between mixtures identified with finite component mm-spaces: entropic existence/uniqueness, quantitative large-penalty and zero-entropy limits, metric property — match-only-what-matches semantics inside the relational matching machine. Machines: matching, stability (relaxation-path continuity), null hypothesis (weak, limit cases). Full annotation: `annotations/2608.09265.md` (B2 pass 36). **See also**: `by-structure/optimal_transport.md`.

## B2 batch-002 re-triage — held candidates re-read machines-first (2026-08-25)

Three of the 22 orchestrator-held candidates survive a GW-core/stat-phys-informed pass; the rest rejected (<2 machines).

- **Kawamura, Majhi & Mitra (2026)** — "The Shadow of Vietoris–Rips Complexes in Limits." arXiv: 2601.01359. The geometric shadow S(R_β(X)) of the Rips complex and the projection p: R_β(X) → S(R_β(X)); p has singularities (resolved only N≤3), but shape-theoretic inverse limits over β→0 jointly with sample densification S→X behave well on homotopy/homology for ANRs — stability recovered for the *system* though individual stages fail. Hausmann/Latschev reconstruction lineage made two-parameter. Machines: parameterized homology, stability, chain complex. Full annotation: `annotations/2601.01359.md` (B2 pass 39). **See also**: `by-structure/filtrations.md`.

- **de Silva & Carlsson (2004)** — "Topological Estimation Using Witness Complexes." Eurographics PBG 2004, pp. 157–166. Landmark vertex sets with witness-certified simplices: decouples who the vertices are from what evidence admits a simplex; nested families W(D;R,ν) built explicitly for persistent homology; landmark sparsity gives less-noisy homology than full constructions — subsampling as robustness mechanism. Foundational infrastructure for large-scale TDA. Machines: chain complex, parameterized homology, stability (empirical). Full annotation: `annotations/desilva-carlsson-2004.md` (B2 pass 39). **See also**: `by-structure/filtrations.md`.

- **Wong & Vong (2021)** — "Persistent Homology based Graph Convolution Network for Fine-grained 3D Shape Segmentation." ICCV 2021, DOI 10.1109/ICCV48922.2021.00701. Filtration barcodes as GCN features plus a novel Persistence Diagram Loss: diagram-vs-diagram mismatch repurposed as differentiable training signal — topological summaries supervising downstream geometric prediction. Motivated by pairwise-only GNN message passing missing higher-dimensional structure. Machines: parameterized homology, matching (diagram loss), stability (weak). Full annotation: `annotations/wong-vong-2021.md` (B2 pass 39). **See also**: `by-structure/composite_systems.md`.
