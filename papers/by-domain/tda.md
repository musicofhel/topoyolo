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

**Domain(s)**: TDA, finance (applied)

**Abstract machines instantiated**:
- **Parameterized homology**: The core methodology is sliding-window persistent homology on financial time series. For each window, a Vietoris-Rips filtration is constructed from time-delay embedded points, and persistence diagrams are computed. The paper extracts three scalar summaries from each diagram: persistent entropy (information content of the barcode), amplitude (spread of the diagram), and point count (number of topological features). These are tracked as the window slides — parameterized homology over time.
- **Stability**: The paper implicitly relies on the stability of persistence diagrams (Cohen-Steiner, Edelsbrunner, Harer, 2007): small perturbations in the input time series produce bounded changes in the persistence diagram, and hence bounded changes in the extracted features. This stability is what makes the TDA features meaningful as forecasting inputs — they are robust summaries rather than noise-sensitive statistics.
- **Null hypothesis**: The experimental design compares N-BEATS+TDA against baselines: (1) univariate N-BEATS without additional features, (2) N-BEATS with temporal decomposition features, and (3) N-BEATS with time-delay embedding features. The baselines serve as null models that lack topological information, isolating the contribution of TDA features.

**What is genuinely new (not reducible to shared abstraction)**:
- First paper to use TDA-derived features (persistent entropy, amplitude, point count) specifically for time series forecasting rather than classification or exploratory analysis. Prior TDA-finance work focused on crash detection (Gidea et al.) or risk indicators, not forecasting.
- The integration with N-BEATS architecture: TDA features are fed as exogenous inputs to a neural forecasting model, letting the network learn how topological structure relates to future price movement.
- Evaluation across 32 datasets (6 cryptocurrencies x 4 scenarios + 4 traditional instruments x 2 scenarios) with statistical significance testing (alpha = 0.10).
- Finding that TDA features outperform both temporal decomposition and time-delay embedding as supplementary features — topological summaries capture information that purely temporal or geometric features miss.

**Connections the authors acknowledge**: Cite TDA-finance literature (Gidea et al. 2020 on crypto crashes, persistent landscapes for market turbulence). Cite persistent homology foundations. No connections to QEC, dynamical systems theory, or information theory beyond standard TDA references.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Persistence diagram | Output of parameterized homology |
| Sliding window | Parameterization over time |
| Persistent entropy | Scalar summary of the barcode (information-theoretic) |
| Amplitude | Scalar summary of the barcode (geometric spread) |
| Point count | Betti number at a given scale |
| Vietoris-Rips filtration | The parameterization (scale parameter epsilon) |
| Time-delay embedding | Phase space reconstruction (Takens embedding) |
| N-BEATS model | Downstream consumer of topological features |
| Baseline without TDA | Null model (no topological information) |

**See also**: `by-structure/filtrations.md`

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

## Cross-listed from Dynamical Systems

- **Zhou, Chu, Xu, Liu, Yu (2020)** — "Detecting Predictable Segments of Chaotic Financial Time Series via Neural Network." Phase space reconstruction + SOM clustering to detect predictable vs. chaotic segments. Full annotation in `by-domain/dynamical_systems.md`. Machines: parameterized homology, null hypothesis.

---

## Cross-listed from Machine Learning / Optimal Transport

- **Bunne, Alvarez-Melis, Krause, Jegelka (2019)** — "Learning Generative Models across Incomparable Spaces." Gromov-Wasserstein GANs for cross-domain generative modeling. Full annotation in `by-domain/dynamical_systems.md` (cross-domain). Machines: matching, stability.

---

## Cross-listed from Second Pass + Bridges

- **Niroomand & Wales (2023)** — "Physics-Inspired Interpretability." Disconnectivity graphs = H₀ persistence diagrams, independently invented by energy landscape theory. Conserved weights = persistent features. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, stability, null hypothesis, joint-vs-marginal (weak). **KEY FINDING: same mathematical object, zero cross-citation.**

- **Gallicchio & Micheli (2020)** — "Fast and Deep Graph Neural Networks." Layer depth = scale parameter (Rips-like). Banach contraction = stability. Untrained random weights suffice — topology carries the information. Full annotation: `cross_domain_bridges.md`. Machines: stability, parameterized homology, null hypothesis, chain complex. **Bridge: dynamics + TDA.**

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
