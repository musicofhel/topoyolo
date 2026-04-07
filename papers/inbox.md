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

## Core ATT papers (annotated)

## Takens (1981)
**"Detecting strange attractors in turbulence"**
Lecture Notes in Mathematics, vol. 898, Springer, pp. 366-381

**Domain(s)**: Dynamical systems

**Abstract machines instantiated**:
- **Chain complex (implicit)**: The delay embedding theorem guarantees that for a generic pair (diffeomorphism phi, observation function y) on a compact manifold M, the delay map F(x) = (y(x), y(phi(x)), ..., y(phi^{2d}(x))) is an embedding of M into R^{2d+1}. The reconstructed manifold F(M) is diffeomorphic to M and therefore has identical homology: H_k(F(M)) = H_k(M) for all k. The chain complex of M is preserved under embedding, though it is never explicitly constructed -- the theorem guarantees existence, not computation. This is the foundational result that makes topological analysis of time series possible: you can recover the topology of an unknown attractor from a single scalar observable.
- **Stability**: The embedding is GENERIC: it holds for a residual (topologically generic) set of pairs (phi, y) in the C^2 topology. This is a topological robustness result -- the embedding persists under small perturbations of both the dynamics and the observation function. Generic = open and dense, so the set of "bad" pairs (where embedding fails) is meager (first Baire category). This is structural stability in the sense of dynamical systems: the qualitative (topological) properties of the reconstruction are robust.
- **Parameterized homology (weak)**: The embedding dimension d serves as a parameter. For d < dim(M), the delay map generically fails to be injective (self-intersections in the reconstruction). For d > 2·dim(M), it generically succeeds. The transition from unfaithful to faithful reconstruction as d increases is a discrete analogue of a filtration: the topology of the reconstructed object changes at a critical parameter value. However, Takens does not track this parametric dependence explicitly.

**What is genuinely new (not reducible to shared abstraction)**:
- The delay embedding construction itself: a SINGLE scalar time series y(x(t)) suffices to reconstruct the full topology of the attractor, provided the observation is generic. No other domain has this property -- in TDA you start with point clouds, in QEC you have direct access to the code space.
- The genericity condition is C^2-topological, not measure-theoretic. This is weaker than Sauer et al.'s later prevalence result but historically came first and shaped the field.
- The theorem applies to diffeomorphisms (discrete dynamics). The continuous-time extension (flows) requires one additional embedding dimension due to the trivial direction along the trajectory.
- No algorithm is given for determining the correct embedding dimension d or delay tau from data -- the theorem is purely existential. Practical methods (false nearest neighbors, mutual information) came later.

**Connections the authors acknowledge**: Situated in the dynamical systems / ergodic theory tradition (Smale, Ruelle). The "turbulence" in the title connects to fluid dynamics. No connections to TDA (which did not exist in 1981), QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Delay map F | Topology-preserving embedding |
| Observation function y | Observable (analogous to cochain) |
| Diffeomorphism phi | Dynamics (discrete time map) |
| Embedding dimension 2d+1 | Sufficient parameter for faithful reconstruction |
| Generic pair (phi, y) | Structurally stable configuration |
| Compact manifold M | The space (attractor) |
| Strange attractor | Invariant topological object with non-integer dimension |
| Residual set | Topologically generic (open dense) |

## Sauer, Yorke, Casdagli (1991)
**"Embedology"**
Journal of Statistical Physics 65(3-4):579-616

**Domain(s)**: Dynamical systems

**Abstract machines instantiated**:
- **Stability**: The central contribution is replacing Takens' topological genericity (residual sets) with PREVALENCE -- a measure-theoretic notion of "almost every." A property holds for prevalent pairs (phi, y) if the set of exceptions has measure zero in a probe sense (analogous to "Lebesgue almost every" in infinite dimensions). This is strictly stronger than genericity: prevalent sets are always residual, but not vice versa. The embedding theorem holds for almost every delay map in the measure-theoretic sense, not merely the topological sense.
- **Parameterized homology (weak)**: The box-counting dimension d_B(A) of the attractor A determines the minimal embedding dimension: 2·d_B(A) + 1 suffices for prevalent embeddings. Since d_B can be non-integer (fractal attractors), the critical embedding dimension is no longer tied to the integer manifold dimension as in Takens. This extends the parametric dependence: the transition from unfaithful to faithful embedding occurs at d > 2·d_B(A), which can be any real number, making the "filtration" finer-grained than Takens' integer threshold.

**What is genuinely new (not reducible to shared abstraction)**:
- Extension to FRACTAL ATTRACTORS: Takens required a smooth compact manifold. Sauer-Yorke-Casdagli prove embedding for sets of arbitrary (possibly non-integer) box-counting dimension, including fractal attractors, products of fractals, and sets with zero Lebesgue measure.
- Prevalence replaces genericity: this is the measure-theoretic analogue of "open and dense." It avoids pathologies of the topological notion (e.g., meager sets can have full measure). Prevalence later became a standard tool across dynamical systems.
- The box-counting dimension d_B(A) is the operative quantity, not the topological or Hausdorff dimension. This is practically important because d_B is computable from data (Grassberger-Procaccia algorithm) while topological dimension is not.
- The result applies to delay embeddings, projections, and more general observation maps -- unifying several embedding results under one framework.

**Connections the authors acknowledge**: Extends Takens (1981) and Whitney (1936). Cite Grassberger-Procaccia for dimension estimation. No connections to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Prevalence | Measure-theoretic robustness (stability in the measure-zero complement sense) |
| Box-counting dimension d_B | Effective dimension of the attractor (fractal analogue of manifold dimension) |
| Delay embedding | Topology-preserving map (Takens) |
| Fractal attractor | Invariant set with non-integer dimension |
| 2·d_B + 1 | Critical embedding dimension (parameter threshold) |
| Whitney embedding | Smooth manifold case (predecessor) |
| Probe measure | Reference measure for prevalence (infinite-dimensional Lebesgue analogue) |

### Cohen-Steiner, Edelsbrunner, Harer (2007) — "Stability of persistence diagrams"
**Domain**: TDA. **Machines**: Stability (bottleneck ≤ Hausdorff), parameterized homology. **Full annotation below** (arXiv: math/0604068).

### Adams et al. (2017) — "Persistence images"
**Domain**: TDA. **Machines**: Parameterized homology (vectorized), stability (W_1 Lipschitz bounds, Theorems 1-4), matching (implicit via Wasserstein optimal bijection), chain complex (implicit, Appendix A). **Full annotation below** (arXiv: 1507.06217).

## 2108.03831 --- Bauer (2021)
**"Ripser: efficient computation of Vietoris-Rips persistence barcodes"**
Journal of Applied and Computational Topology 5:391-423

**Domain(s)**: TDA (computational)

**Abstract machines instantiated**:
- **Chain complex**: The Vietoris-Rips complex is the chain complex: given a finite metric space (X, d), the VR complex at scale epsilon includes a k-simplex [v_0, ..., v_k] whenever all pairwise distances d(v_i, v_j) <= epsilon. The boundary operators are standard simplicial partial. Ripser works with the COBOUNDARY matrix (the transpose/dual of partial) rather than the boundary matrix -- this is the key algorithmic insight. The coboundary matrix is sparse (each simplex has few cofaces) while the boundary matrix is dense (each simplex has many faces in high dimensions). By working with coboundary, the matrix representation is implicit: Ripser never stores the full matrix, instead computing coboundary entries on-the-fly from the combinatorial structure.
- **Parameterized homology**: The persistence algorithm IS the parameterized homology machine: it tracks births and deaths of homology classes as the filtration parameter epsilon varies from 0 to infinity. The output is the persistence barcode -- a multiset of intervals [b_i, d_i) recording when each feature appears and disappears. Three algorithmic optimizations accelerate this: (1) APPARENT PAIRS: if a simplex sigma and its youngest cofacet tau satisfy a certain clearing criterion, they form a persistence pair immediately without matrix reduction. (2) EMERGENT PAIRS: detected during coboundary enumeration, before the full column is assembled. (3) CLEARING: once a simplex is identified as a "death" simplex, its column can be zeroed, reducing future work.

**What is genuinely new (not reducible to shared abstraction)**:
- The implicit coboundary matrix representation: Ripser never materializes the full boundary/coboundary matrix. Instead, it computes entries on-demand using the combinatorial encoding of simplices (lexicographic ordering). This reduces memory from O(n^k) to O(n) for k-simplices.
- Apparent and emergent pair optimizations: these identify persistence pairs WITHOUT performing column reduction, short-circuiting the standard persistence algorithm. In practice, the vast majority of pairs are apparent/emergent, making the algorithm orders of magnitude faster than naive implementations.
- The clearing optimization (from Chen-Kerber 2011, but integrated and optimized here): uses the duality between homology and cohomology to skip redundant computations.
- Benchmarks show 40-1000x speedups over previous implementations (GUDHI, Dionysus, DIPHA) on standard datasets, making VR persistent homology tractable for point clouds of thousands of points.
- Ripser has become the de facto standard computational tool for PH -- virtually all subsequent TDA papers use it or cite it.

**Connections the authors acknowledge**: Cite Edelsbrunner-Letscher-Zomorodian (2002) for the persistence algorithm, Chen-Kerber (2011) for clearing, de Silva-Morozov (2011) for the duality between homology and cohomology persistence. Situated entirely within computational TDA. No connections to QEC, dynamical systems, neuroscience, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Vietoris-Rips complex | Chain complex (simplicial, from metric data) |
| Coboundary matrix | Dual of boundary operator (transpose of partial) |
| Filtration value epsilon | The parameter (scale) |
| Persistence barcode | Output of parameterized homology (birth-death intervals) |
| Apparent pair | Trivially determined persistence pair (immediate matching) |
| Emergent pair | Early-detected persistence pair (partial computation) |
| Clearing | Optimization exploiting homology-cohomology duality |
| Implicit representation | Memory-efficient encoding (on-demand computation) |
| Lexicographic simplex ordering | Combinatorial encoding of chain complex generators |

### Giusti, Curto et al. (2015) — "Clique topology reveals intrinsic geometric structure"
**Domain**: Neuroscience + TDA. **Machines**: Chain complex (clique complex on correlations), parameterized homology, null hypothesis. **Full annotation below** (arXiv: 1502.06172).

### Gardner et al. (2022) — "Toroidal topology of population activity in grid cells"
**Domain**: Neuroscience, TDA. **Machines**: Chain complex, parameterized homology, stability, null hypothesis, joint-vs-marginal. The torus IS the neural manifold — same object as the toric code's base space, different interpretation. **Full annotation below** (DOI: 10.1038/s41586-021-04268-7). **See also**: `cross_domain_bridges.md` (neuro ↔ QEC via shared T²).

## 2508.19048 --- Peek, Pritam, Skerritt, Chalup (2025)
**"Time Series Analysis of Spiking Neural Systems via Transfer Entropy and Directed Persistent Homology"**
arXiv: 2508.19048

**Domain(s)**: Neuroscience, TDA, information theory

**Abstract machines instantiated**:
- **Chain complex**: Transfer entropy (TE) between all neuron pairs produces a weighted, directed adjacency matrix. This is converted to a directed flag complex via Flagser: a directed k-simplex is included when all directed edges between (k+1) vertices exist in a consistent orientation. The boundary operators are standard simplicial partial on the oriented simplices. The construction is: spike trains -> TE estimation (pairwise) -> directed weighted graph -> asymmetry enforcement (retain only stronger direction per pair) -> directed flag complex. This is the same directed simplicial complex construction as Reimann et al. (2017), but built from INFORMATION-THEORETIC (TE) coupling rather than synaptic connectivity.
- **Parameterized homology**: The filtration is by inverted TE values: edges with highest TE (strongest information transfer) appear first, weakest last. As the filtration parameter increases, weaker connections are added, and topological features (connected components, directed loops, higher-dimensional cavities) are born and die. Persistence diagrams record (birth, death, dimension) tuples. Betti curves beta_d(epsilon) track feature counts per dimension across the filtration. Area Under Betti Curve (AUBC) provides scalar summaries. The paper also uses Wasserstein distances between persistence diagrams to measure topological distances between experimental conditions, recovering meaningful geometry in task space (e.g., ordered transitions across noise levels).
- **Null hypothesis (implicit/structural)**: Three levels of comparison serve as implicit nulls: (1) In the logic gate experiment, AND/OR tasks serve as simple baselines against which XOR's richer topology is measured. (2) In the image classification experiment, clean images serve as the baseline; noise (bit-flipping) and spatial perturbation (bit-moving) systematically degrade structure. Bit-moving preserves total spike energy, isolating topological changes from input intensity changes. (3) In the biological experiment, baseline epochs (pre-stimulus) provide the null against which stimulus/feedback epochs are compared, with metrics including delta-to-baseline, ratio-to-baseline, Cohen's d, and mutual information.

**What is genuinely new (not reducible to shared abstraction)**:
- The TE+PH pipeline is the first to apply directed persistent homology to NEURON-LEVEL transfer entropy networks in spiking systems. Xi et al. (2025) combined TE+PH at the EEG regional scale; Peek et al. extend this to fine-grained spiking data.
- Triple-domain bridge: the paper explicitly connects information theory (TE as the coupling measure), TDA (directed PH as the topological analysis), and neuroscience (both artificial SNNs and biological mouse cortical recordings). This is one of very few papers that operates simultaneously in all three domains.
- Higher-dimensional homology (dimensions 2-3) discriminates task complexity even when dimensions 0-1 do not. XOR produces richer higher-dimensional topology than AND/OR, consistent with its non-linear separability. This extends the Reimann et al. finding that high-dimensional directed simplices matter.
- The bit-moving experiment controls for spike energy while varying spatial structure, cleanly isolating topological effects from amplitude effects.
- Wasserstein distances between PDs recover graded structure in task space: noise levels map to an ordered topological trajectory.

**Connections the authors acknowledge**: Cite Schreiber (2000) for TE, Edelsbrunner-Harer and Carlsson for PH, Reimann et al. (2017) and Sizemore et al. (2019) for directed TDA in neuroscience, Dabaghian et al. (2012) and Giusti et al. (2015) for TDA in neuroscience. Cite Xi et al. (2025) as the only prior TE+PH work (EEG scale). Explicitly positioned as a cross-disciplinary bridge between computational topology, information theory, and neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transfer entropy T_{X->Y} | Directed joint-vs-marginal excess (Schreiber) |
| Directed flag complex | Chain complex (directed simplicial, from TE graph) |
| Flagser | Computational tool for directed PH (analogous to Ripser for undirected) |
| Inverted TE filtration | Parameterization (strongest connections first) |
| Persistence diagram | Output of parameterized homology |
| Betti curve beta_d(epsilon) | Feature count per dimension across filtration |
| AUBC (Area Under Betti Curve) | Scalar summary of parameterized homology |
| Wasserstein distance between PDs | Optimal matching distance between topological signatures |
| Directed k-simplex | Generator of chain group (oriented, from information flow) |
| Baseline epoch | Null model (pre-stimulus reference) |
| Spike train | Binary time series (input to TE estimation) |

**Note**: The inbox originally listed this as "Xi et al." Xi et al. (2025) is a related precursor that applied TE+directed PH to EEG data at regional scale (Neurocomputing 637:130086). Peek et al. (2025) extends this to neuron-level spiking systems, which is the more precise match for "TE + directed PH in spiking systems."

### Sugihara et al. (2012) — CCM (Science, DOI: 10.1126/science.1227079)
**Domain**: Dynamical systems + causal inference. **Machines**: Joint-vs-marginal (manifold cross-prediction), stability (convergence criterion), null hypothesis (no-coupling null + surrogates), parameterized homology (weak — library size L as filtration). **Full annotation below** (DOI: 10.1126/science.1227079).

### Tsuda (2001) — "Chaotic itinerancy"
**Domain**: Neuroscience + dynamical systems. **Machines**: Parameterized homology (attractor switching = path through topology space), stability (quasi-stability via attractor ruins), null hypothesis (fixed-point/limit-cycle as non-itinerant null), chain complex (weak — sequence of ruins with heteroclinic connections). **Fully annotated below** (DOI: 10.1017/S0140525X01000097).

### PRL 85:461 — Schreiber (2000)
**"Measuring information transfer"**

**Domain(s)**: Information theory, dynamical systems

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Transfer entropy T_{Y→X} = H(X_{t+1} | X_t^(k)) - H(X_{t+1} | X_t^(k), Y_t^(l)). This IS conditional mutual information: how much does the joint history (X,Y) improve prediction of X's future beyond the marginal history (X alone)? The excess quantifies directed information flow from Y to X.
- **Null hypothesis**: Shuffled surrogates destroy the temporal coupling between X and Y while preserving marginal statistics. TE under the null should be zero (up to finite-sample bias). Significance = observed TE exceeds null distribution.
- **Parameterized homology** (weak): The embedding dimensions k, l and prediction horizon parameterize the TE estimate. Different parameter choices reveal different timescales of information transfer.

**What is genuinely new (not reducible to shared abstraction)**:
- Asymmetry: unlike MI, TE is inherently directional. T_{Y→X} ≠ T_{X→Y} in general. This distinguishes it from symmetric measures and connects to causality.
- Non-parametric: unlike Granger causality, TE makes no model assumptions (linear, Gaussian). It measures information transfer in arbitrary nonlinear systems.
- The connection to dynamical systems: TE is defined on state-space reconstructions, linking naturally to Takens embedding and attractor geometry.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transfer entropy | Directed joint-vs-marginal excess |
| Conditional MI | Excess prediction from joint history |
| Shuffled surrogate | Null model (destroys temporal coupling) |
| Embedding dimension k, l | Parameterization of estimator |
| Information flow direction | Asymmetry of joint-vs-marginal |

### J Neurophysiol 104:1195 — Tort, Komorowski, Eichenbaum, Kopell (2010)
**"Measuring Phase-Amplitude Coupling Between Neuronal Oscillations of Different Frequencies"**

**Domain(s)**: Neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The Modulation Index (MI) measures how much gamma amplitude depends on theta phase. MI = D_KL(observed phase-amplitude distribution || uniform distribution) / log(N). If theta phase and gamma amplitude are independent (marginal), the distribution is uniform. The KL divergence from uniform IS the joint-vs-marginal excess.
- **Null hypothesis**: Surrogate distributions from time-shifted data: shift the amplitude time series relative to the phase time series, destroying the temporal coupling while preserving spectral properties. The surrogate MI distribution provides the null.
- **Parameterized homology** (weak): Frequency band pairs (theta-gamma, theta-high-gamma, etc.) parameterize the family of PAC measurements. Different frequency combinations reveal different coupling structures.

**What is genuinely new (not reducible to shared abstraction)**:
- Cross-frequency coupling is a NEURAL-SPECIFIC phenomenon — it arises from the multi-scale oscillatory structure of brain dynamics. No analogue in QEC or standard dynamical systems.
- The KL-from-uniform formulation makes the measure truly information-theoretic, connecting directly to the joint-vs-marginal framework.
- The time-shift surrogate specifically destroys phase-amplitude coupling while preserving within-band spectral structure — a more targeted null than generic shuffling.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Modulation Index | Joint-vs-marginal excess (KL from uniform) |
| Phase-amplitude distribution | Joint distribution |
| Uniform distribution | Independence null (product of marginals) |
| Time-shifted surrogate | Null model (destroys cross-frequency coupling) |
| Frequency band pair | Parameterization |
| Cross-frequency coupling | Multi-scale joint structure |

---

## 1502.06172 — Giusti, Pastalkova, Curto, Itskov (2015)
**"Clique topology reveals intrinsic geometric structure in neural correlations"**

**Domain(s)**: Neuroscience, TDA

**Abstract machines instantiated**:
- **Chain complex**: Constructs clique complex from pairwise correlation matrix of hippocampal pyramidal neurons. Vertices = neurons; k-cliques in the thresholded graph become (k-1)-simplices. The boundary operators are standard simplicial ∂. The key innovation is that topological features (Betti numbers) are extracted from the ORDER COMPLEX — only the rank ordering of correlations matters, not magnitudes. This makes the chain complex invariant under monotone nonlinear transformations of the correlation matrix.
- **Parameterized homology**: The filtration parameter is the threshold on correlation values. As threshold varies, simplices appear/disappear, yielding a persistence-like signature. Geometric matrices produce specific Betti number patterns distinct from random matrices.
- **Null hypothesis**: Random matrices (iid entries) serve as the null model. Geometric matrices (derived from point configurations) are the alternative. Clique topology distinguishes the two where eigenvalue methods fail.

**What is genuinely new (not reducible to shared abstraction)**:
- The invariance under monotone transformations is specific to the order complex construction — standard PH on Rips/Čech complexes does not have this property.
- Geometric structure persists during non-spatial behaviors (wheel running, REM sleep), suggesting circuit architecture rather than stimulus encoding shapes the topology. This is a biological finding with no algebraic analogue.
- The method detects structure that eigenvalue-based methods (PCA, spectral) miss entirely — the nonlinearity of neural coding hides geometric structure from linear tools.

**Connections the authors acknowledge**: Explicit connection to persistent homology and algebraic topology. No connection to QEC, dynamical systems, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Clique complex | Chain complex (simplicial) |
| Order complex | Parameterized chain complex (filtration by rank) |
| Betti number | Feature count per dimension |
| Correlation matrix threshold | Filtration parameter |
| Random matrix | Null model |
| Geometric matrix | Structured signal |
| Monotone invariance | Stability under nonlinear perturbation |

---

## 10.3389/fncom.2017.00048 — Reimann, Nolte, Scolamiero, Turner, Perin, Chindemi, Dłotko, Levi, Hess, Markram (2017)
**"Cliques of Neurons Bound into Cavities Provide a Missing Link between Structure and Function"**

**Domain(s)**: Neuroscience, TDA

**Abstract machines instantiated**:
- **Chain complex**: Constructs DIRECTED simplicial complexes from synaptic connectivity in reconstructed rat neocortical microcircuitry (~31,000 neurons, ~8 million connections). A directed k-simplex is a clique of (k+1) neurons with a single source and single sink, reflecting information flow direction. Boundary operators are the standard simplicial ∂ on these directed simplices. Finds directed simplices up to dimension 6-7, with ~80 million directed 3-simplices — vastly exceeding null models.
- **Parameterized homology**: Stimulus response triggers hierarchical activation: correlated activity evolves through increasingly complex simplices and cavities in a stereotypical temporal sequence. The parameter is time after stimulus onset.
- **Null hypothesis**: Erdős-Rényi random graphs with same neuron count and connection probability. The biological network has orders of magnitude more high-dimensional directed cliques than the null.

**What is genuinely new (not reducible to shared abstraction)**:
- DIRECTED simplicial complexes: the direction of information flow (source→sink) is encoded in the simplex orientation. Standard TDA simplicial complexes are undirected. This is closer to the oriented chain complexes in algebraic topology but motivated by biological directionality.
- The temporal sequence of cavity formation during stimulus response has no analogue in static TDA or QEC. The chain complex is dynamic — it grows as neural activity unfolds.
- Scale: the reconstruction contains structures up to dimension 7, far exceeding anything in typical TDA point cloud analyses.

**Connections the authors acknowledge**: Explicit connection to algebraic topology (Hess, Levi are topologists). No connection to QEC or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Directed simplex | Oriented simplex in chain complex |
| Directed clique | Generator of chain group |
| Cavity | Non-trivial homology class (cycle not bounding) |
| Synaptic connectivity graph | 1-skeleton of chain complex |
| Source/sink neuron | Orientation of simplex |
| Betti number | Feature count per dimension |
| Erdős-Rényi null | Null model (destroys directed structure) |

---

## 10.1371/journal.pcbi.1002581 — Dabaghian, Mémoli, Frank, Carlsson (2012)
**"A Topological Paradigm for Hippocampal Spatial Map Formation Using Persistent Homology"**

**Domain(s)**: Neuroscience, TDA

**Abstract machines instantiated**:
- **Chain complex**: Builds temporal nerve complex T(t) from place cell co-firing. Vertices = place cells. When k cells co-fire within a theta cycle, they span a (k-1)-simplex. The complex grows as the animal explores and accumulates co-firing observations. Standard simplicial boundary operators ∂.
- **Parameterized homology**: Persistent homology tracks Betti numbers (b₀ = connected components, b₁ = loops) as the complex grows over time. Long-lived features correspond to genuine topological features of the environment (e.g., obstacles creating loops). Short-lived features are topological noise from incomplete sampling.
- **Stability**: The method identifies a "learning region" in parameter space (firing rate × place field size × neuron count) where correct topology is recovered. Outside this region, PH fails — either too sparse (false negatives) or too noisy (false positives). This is a biological analogue of the sampling density requirements in topological inference.

**What is genuinely new (not reducible to shared abstraction)**:
- The complex is built from TEMPORAL co-activity, not spatial proximity or correlation magnitude. The filtration parameter is time (exploration duration), not a distance threshold.
- Map formation takes 2-5 minutes with biologically realistic parameters — this temporal constraint has no analogue in static TDA.
- The "learning region" bounds relate biological parameters (firing rate, field size) to topological recovery — a domain-specific stability result.

**Connections the authors acknowledge**: Carlsson and Mémoli are TDA researchers. Explicit connection to persistent homology methodology. No connection to QEC, dynamical systems theory, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Nerve complex | Chain complex (Nerve theorem) |
| Place cell co-firing | Simplex generator |
| Theta cycle | Temporal resolution for simplex construction |
| Betti number b₁ | Loop count = obstacle count |
| Persistent barcode | Persistence diagram |
| Learning region | Stability region in parameter space |
| Topological noise | Short-lived features (near diagonal) |

---

## 10.1371/journal.pcbi.1000205 — Curto, Itskov (2008)
**"Cell Groups Reveal Structure of Stimulus Space"**

**Domain(s)**: Neuroscience, TDA

**Abstract machines instantiated**:
- **Chain complex**: Constructs simplicial complex from place cell co-firing groups. Cell groups (cells co-firing within a 250ms window) define simplices: 2 co-firing cells = edge, 3 = triangle, etc. This is the nerve of the receptive field cover. The Nerve Theorem guarantees that the homology of this complex equals the homology of the stimulus space (up to homotopy equivalence), provided the receptive fields are convex.
- **Matching**: Cell groups become spatial locations. A graph connects neighboring groups (differing by one cell), with edge weights from a dissimilarity index μ_k. Shortest-path distances yield a metric reconstruction of the environment with ~3% accuracy using 120-140 cells. This is an implicit optimal assignment: matching neural patterns to spatial locations.
- **Stability**: Topology recovery is robust to 10% spike-timing noise and 11% multipeaked place fields. Geometric reconstruction degrades gracefully with noise.

**What is genuinely new (not reducible to shared abstraction)**:
- The Nerve Theorem provides an EXACT theoretical guarantee (not just empirical stability) that neural co-firing topology = stimulus space topology, given convex receptive fields.
- No external information is needed — neither stimuli, position, receptive field maps, nor spike timing precision. The topology is intrinsic to the co-firing pattern.
- The geometric reconstruction (not just topological) from purely combinatorial data — going beyond homology to metric structure.

**Connections the authors acknowledge**: Explicit use of the Nerve Theorem from algebraic topology. No connections to QEC, dynamical systems, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Cell group | Simplex (face of nerve complex) |
| Co-firing pattern | Combinatorial data for chain complex |
| Nerve of covering | Chain complex (Nerve Theorem) |
| H₁ | First homology = loop/obstacle count |
| Receptive field overlap | Non-empty intersection (nerve condition) |
| Dissimilarity index μ_k | Cost function for matching |
| Spike-timing noise tolerance | Stability bound |

---

## 1901.03048 — Divol, Lacombe (2019)
**"Understanding the Topology and the Geometry of the Space of Persistence Diagrams via Optimal Partial Transport"**

**Domain(s)**: TDA

**Abstract machines instantiated**:
- **Matching**: The paper's core insight: Wasserstein and bottleneck distances on persistence diagrams ARE optimal partial transport problems. Extends persistence diagrams to Radon measures on the upper half-plane, unifying discrete diagrams and continuous representations (persistence surfaces). Provides geometric description of barycenters (Fréchet means) for distributions of diagrams. Characterizes convergence under Wasserstein metrics.
- **Stability**: Reformulating PD distances as OT distances inherits stability results from both fields. The Radon measure extension is continuous in the Wasserstein topology.

**What is genuinely new (not reducible to shared abstraction)**:
- The identification PD distance = optimal partial transport is exact, not analogical. This is a theorem, not a metaphor.
- Extension to Radon measures solves a practical problem: persistence diagrams are discrete but many operations (means, limits) naturally live in continuous spaces.
- Exhaustive description of continuous linear representations of persistence diagrams — characterizes ALL possible vectorizations.

**Connections the authors acknowledge**: Explicit bridge between TDA (persistence diagrams) and optimal transport theory. No connections to QEC, dynamics, neuroscience, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Persistence diagram | Topological signature |
| Wasserstein distance on PDs | Matching cost (Lp) |
| Bottleneck distance | Matching cost (L∞) |
| Optimal partial transport | Matching with unmatched points (diagonal) |
| Radon measure on half-plane | Continuous extension of matching space |
| Fréchet mean | Barycenter under matching metric |

---

## 1812.06491 — Vejdemo-Johansson, Mukherjee (2018)
**"Multiple testing with persistent homology"**

**Domain(s)**: TDA

**Abstract machines instantiated**:
- **Null hypothesis**: Develops universal empirical null distribution for persistent homology features. Rather than computing null distributions per application, simulates a null based on a few data summaries that generalizes across diverse PH applications. Two multiple testing procedures: FWER control and FDR control for rejecting acyclicity (i.e., testing whether topological features are significant).
- **Stability**: The empirical null is grounded in limit theorems for PH of point processes, providing asymptotic guarantees.

**What is genuinely new (not reducible to shared abstraction)**:
- UNIVERSAL null distribution for PH — analogous to chi-squared or F-distribution tables in classical statistics. Previous approaches required per-application null simulation.
- Formal multiple testing framework (FWER/FDR) adapted specifically to topological features — addresses the multiple comparisons problem when many homology generators are tested simultaneously.

**Connections the authors acknowledge**: Pure TDA methodology. No cross-domain connections.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Empirical null distribution | Null model (universal for PH) |
| Rejecting acyclicity | Significance of topological feature |
| FWER/FDR control | Multiple testing correction |
| Persistence of feature | Feature lifetime (birth-death) |
| Limit theorems for PH | Stability guarantee (asymptotic) |

---

## 1708.07390 — Harrington, Otter, Schenck, Tillmann (2017)
**"Stratifying multiparameter persistent homology"**

**Domain(s)**: TDA

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Multiparameter PH studies topological invariants as MULTIPLE parameters vary simultaneously (e.g., spatial scale AND density threshold). The joint bifiltration captures structure invisible to either single-parameter filtration alone. This IS joint-vs-marginal: the joint persistent homology contains information absent from the marginal (single-parameter) persistence diagrams.
- **Parameterized homology**: The fundamental object is a multigraded module over a polynomial ring. Three invariants track its structure: multigraded associated primes (stratification of support), multigraded Hilbert series (size measure), and local cohomology (strata-level detail).
- **Chain complex**: The underlying object is still a chain complex, but now parameterized by a poset (product of total orders) rather than a single linear filtration.

**What is genuinely new (not reducible to shared abstraction)**:
- Multiparameter PH has no complete discrete invariant (unlike 1-parameter, which has the barcode). The paper provides PARTIAL invariants via commutative algebra that capture essential structure.
- The stratification approach — decomposing by support regions — is imported from algebraic geometry (associated primes of modules) and has no direct analogue in the other domains.
- Generalizes the 1-parameter persistence → barcode correspondence to the multiparameter case, but the generalization is fundamentally incomplete (no barcode theorem exists).

**Connections the authors acknowledge**: Bridge between TDA and commutative algebra/algebraic geometry. No connections to QEC, dynamics, neuroscience, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Multiparameter filtration | Joint parameterization (product poset) |
| Bifiltration | Two-parameter family of chain complexes |
| Multigraded module | Parameterized homology over product |
| Associated primes | Support stratification |
| Single-parameter barcode | Marginal persistence diagram |
| Multiparameter structure absent from marginals | Joint-vs-marginal excess |

---

## 1906.00030 — Wong, Yang (2019)
**"Pseudo-Riemannian geometry embeds information geometry in optimal transport"**

**Domain(s)**: Information theory, TDA (optimal transport)

**Abstract machines instantiated**:
- **Matching**: Shows that information geometry (Fisher metric, Bregman divergence) EMBEDS into optimal transport geometry (Wasserstein metric) via pseudo-Riemannian framework of Kim-McCann. The Ma-Trudinger-Wang condition from OT regularity theory corresponds to information-geometric curvature. Bregman divergence's dually flat geometry ↔ quadratic OT cost. L^(α)-divergence ↔ constant sectional curvature.
- **Stability**: The embedding is structure-preserving: dualistic structure of statistical manifold maps to cross-curvature in OT. Information-geometric curvature gains interpretation via "divergence between primal-dual pair of geodesics."

**What is genuinely new (not reducible to shared abstraction)**:
- The embedding result is EXACT and FUNCTORIAL — information geometry is literally a substructure of OT geometry, not merely analogous.
- Connects two independently developed fields (Amari/Chentsov vs Villani/Brenier) through a third (pseudo-Riemannian geometry).
- The MTW condition — a regularity condition for OT — gets reinterpreted as an information-geometric invariant. This is a genuine discovery, not a relabeling.

**Connections the authors acknowledge**: Explicit bridge between information geometry and optimal transport. Cites both Amari (information geometry) and Villani (OT). No connections to QEC, neuroscience, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Fisher metric | Local cost structure on statistical manifold |
| Bregman divergence | Matching cost (information-geometric) |
| Wasserstein distance | Matching cost (transport) |
| MTW condition | Regularity/stability of optimal matching |
| Dually flat geometry | Special case of matching structure |
| Pseudo-Riemannian embedding | Functor from InfoGeo to OT |

---

## Found and annotated (Wave 4b)

### quant-ph/9707021 — Kitaev (1997)
**"Fault-tolerant quantum computation by anyons"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: The toric code IS a chain complex on a 2D lattice (cellulation of a torus). Qubits live on edges (1-cells). X-stabilizers = ∂ (boundary of faces/2-cells). Z-stabilizers = δ (coboundary of vertices/0-cells). Logical operators = non-trivial homology classes of H₁(T², ℤ/2). The number of logical qubits = rank H₁ = 2 for the torus.
- **Matching**: Anyonic excitations come in pairs. Error correction = fusing (matching) anyon pairs back to vacuum. The fusion rules define which pairs can annihilate.
- **Stability**: Fault tolerance is TOPOLOGICAL — errors must create a non-trivial homology cycle to cause a logical error. This requires O(d) local errors where d = code distance = min-weight non-trivial cycle. Exponential suppression below threshold.

**What is genuinely new**: Computation via anyon braiding — the computational gate set comes from the braid group acting on the fusion space. This is computation FROM topology, not computation ON topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Toric code lattice | Chain complex on T² |
| Anyon | Localized homology defect |
| Fusion | Matching (annihilation of defect pairs) |
| Braid group | Computational gate set from topology |
| Code distance | Min-weight non-trivial cycle |
| Logical qubit | Non-trivial homology class |

---

### quant-ph/0110143 — Dennis, Kitaev, Landahl, Preskill (2002)
**"Topological quantum memory"**

**Domain(s)**: QEC, statistical physics

**Abstract machines instantiated**:
- **Chain complex**: Surface codes on surfaces of nontrivial topology. Qubits on edges, stabilizers from ∂ and δ. Encoded operations = non-trivial homology cycles. Explicit construction with recovery protocols.
- **Parameterized homology**: Error rate p parameterizes the family. Below threshold p_c: encoded information preserved. Above: destroyed. The threshold IS a phase transition.
- **Stability**: Threshold theorem: below p_c, logical error rate suppressed exponentially in code distance. The phase transition maps EXACTLY to a 3D Z₂ lattice gauge theory with quenched disorder — the accuracy threshold = critical temperature of the gauge theory.
- **Null hypothesis**: Uncorrected system (no recovery) as baseline. The gap between corrected and uncorrected logical error rates quantifies the value of error correction.
- **Matching**: Recovery = identifying and matching syndrome defects. MWPM on syndrome graph.

**What is genuinely new**: The mapping to statistical mechanics (random-bond Ising / Z₂ gauge theory) is a genuine cross-domain bridge. The threshold IS a thermodynamic phase transition, not merely analogous to one. Also: the 4D procedure that doesn't require measurement — a qualitatively different computational model.

**Connections the authors acknowledge**: Explicit bridge to statistical mechanics (Z₂ gauge theory). This is one of the rare cross-domain connections.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Surface code | Chain complex on surface |
| Accuracy threshold | Critical parameter (phase transition) |
| Z₂ gauge theory | Statistical mechanics null model |
| Recovery protocol | Matching/correction |
| Code distance | Min-weight non-trivial cycle |
| Encoded operation | Non-trivial homology class |

---

### 1307.6188 — Perea, Harer (2013)
**"Sliding Windows and Persistence: An Application of Topological Methods to Signal Analysis" (SW1PerS)**

**Domain(s)**: TDA, dynamical systems

**Abstract machines instantiated**:
- **Chain complex**: Sliding window embedding of a time series produces a point cloud in ℝ^d. Rips/Čech complex on this point cloud. Standard simplicial ∂.
- **Parameterized homology**: TWO parameters: (1) the Rips scale ε, (2) the window size/embedding dimension. Persistence diagrams track homology as ε varies. Maximum 1-dimensional persistence quantifies PERIODICITY of the original signal.
- **Stability**: Structural and convergence theorems for the persistence diagrams. Estimates for dependency on window size and embedding dimension. Connects to Takens embedding theorem guarantees.

**What is genuinely new**: The bridge between signal-level properties (periodicity) and point-cloud-level topology (persistent H₁). This is a FORMAL connection between dynamical systems (Takens) and TDA (persistence), not just an application. The SW1PerS score is a topological periodicity measure.

**Connections the authors acknowledge**: Explicit bridge between TDA and dynamical systems (Takens embedding). Cross-domain by construction.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Sliding window embedding | Takens embedding → point cloud |
| SW1PerS score | Maximum persistence in H₁ |
| Window size | Embedding parameter (Takens dimension) |
| Periodicity | Non-trivial H₁ (loop in embedding) |
| Convergence theorem | Stability of persistence under sampling |

---

### math/0604068 — Cohen-Steiner, Edelsbrunner, Harer (2007)
**"Stability of Persistence Diagrams"**

**Domain(s)**: TDA

**Abstract machines instantiated**:
- **Stability**: THE foundational stability theorem for TDA. Bottleneck distance between persistence diagrams ≤ L∞ distance between the functions inducing the filtrations. d_B(Dgm(f), Dgm(g)) ≤ ||f - g||∞. Small perturbation in input → bounded change in topological output. This is the Lipschitz stability that all downstream TDA applications rely on.
- **Matching**: The bottleneck distance IS a matching: optimal bijection between diagram points (including the diagonal) minimizing the maximum displacement. The stability theorem says this matching cost is bounded by the input perturbation.
- **Parameterized homology**: Persistence diagrams ARE the output of parameterized homology. The theorem says this output is stable.

**What is genuinely new**: This is the FOUNDATIONAL result. Before this theorem, persistent homology was a computational tool without robustness guarantees. The stability theorem made TDA a rigorous statistical methodology. The proof technique (interleaving of filtrations) became a template for all subsequent stability results.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Bottleneck distance | Matching cost (L∞) |
| Persistence diagram | Parameterized homology output |
| ||f - g||∞ | Input perturbation |
| d_B ≤ ||f - g||∞ | Lipschitz stability bound |
| Interleaving | Approximate isomorphism of filtrations |

---

## Wave 3 triage annotations

### MDPI Entropy 17(5):3253 — Baudot, Bennequin (2015)
**"The Homological Nature of Entropy"**

**Domain(s)**: Information theory, TDA (algebraic topology)

**Abstract machines instantiated**:
- **Chain complex**: Defines information structures as simplicial complexes where k-simplices correspond to k-tuples of random variables. The coboundary operator δ maps (k-1)-information functions to k-information functions. δ² = 0 holds by construction. Shannon entropy H and mutual information I emerge as COCYCLES in this complex — they satisfy the cocycle condition δH = 0 (the chain rule of entropy). Information quantities that satisfy the chain rule ARE cohomology classes.
- **Parameterized homology** (weak): The lattice of random variable subsets parameterizes the information functions. Moving up the lattice reveals higher-order interactions.

**What is genuinely new (not reducible to shared abstraction)**:
- The identification entropy = cocycle is EXACT, not analogical. Shannon's chain rule IS the cocycle condition. This is the most rigorous Chain×Info result in the literature.
- Extends to Tsallis and Rényi entropies as deformed cocycles — the deformation parameter parameterizes a family of cohomology theories.
- Negative information quantities (conditional MI can be negative) correspond to non-trivial cohomology classes — they cannot be "explained away" by lower-order terms.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Information structure | Simplicial complex of random variables |
| k-tuple of variables | k-simplex |
| Shannon entropy | 1-cocycle |
| Chain rule | Cocycle condition (δH = 0) |
| Mutual information | Derived quantity from cocycle |
| Information cohomology | Homology of information complex |

---

### 2107.09581 — Bradley (2021)
**"Entropy as a Topological Operad Derivation"**

**Domain(s)**: Information theory, TDA (category theory)

**Abstract machines instantiated**:
- **Chain complex**: The operad of topological simplices provides the algebraic structure. Shannon entropy is characterized as the unique derivation (up to scalar) of this operad. The simplicial structure IS the chain complex — the operad composition maps correspond to boundary/face maps. Faddeev's 1956 characterization of entropy (via functional equations) is shown to be equivalent to the derivation property in the operad.

**What is genuinely new (not reducible to shared abstraction)**:
- Uniqueness: Shannon entropy is the ONLY derivation of the simplicial operad (up to constant). This is a characterization theorem, not just an embedding.
- Category-theoretic framing connects to Riehl's functorial perspective (on the "to find" list).
- Strengthens Baudot-Bennequin: not only is entropy a cocycle, it is the unique one satisfying the operad derivation axioms.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Operad of simplices | Chain complex (categorified) |
| Derivation | Cocycle satisfying Leibniz rule |
| Shannon entropy | Unique derivation |
| Faddeev axioms | Cocycle conditions |

---

### 2405.07665 — Kolchinsky (2024)
**"Partial information decomposition: redundancy as information bottleneck"**

**Domain(s)**: Information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: PID IS the joint-vs-marginal machine: synergy = information in the joint that exceeds the sum of unique + redundant contributions. This paper reformulates redundancy itself as an IB problem: compress the sources while preserving target prediction but obscuring source identity.
- **Parameterized homology**: The "RB curve" traces redundancy as a function of compression level — a one-parameter family of decompositions. At different compression levels, different redundant subsets emerge. This IS parameterized homology: a parameter (compression β) indexes a family of information decompositions.
- **Matching**: The IB framework involves optimal assignment between source representations and target predictions. The redundancy bottleneck optimizes this assignment.

**What is genuinely new (not reducible to shared abstraction)**:
- The bridge PID ↔ IB is the key contribution. Redundancy (Joint machine) = compression-prediction tradeoff (Param machine). This formally connects two abstract machines that were previously instantiated independently.
- Efficient iterative algorithm replaces combinatorial PID computation — practical scalability.
- Generalizes "Blackwell redundancy" — provides operational semantics for PID atoms.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Redundancy | Joint-vs-marginal (shared component) |
| Synergy | Joint-vs-marginal (excess component) |
| RB curve | Parameterized decomposition |
| Compression β | Filtration parameter |
| Source identity obscuring | Null construction (destroy source labels) |

---

## Phase 2 Annotations (2026-04-06, session 2)

---

## quant-ph/0101025 --- Freedman, Kitaev, Larsen, Wang (2001)
**"Topological Quantum Computation"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: The theory of quantum computation constructed from anyonic systems = unitary topological modular functors. These arise in Witten-Chern-Simons theory. Braiding and fusion of anyonic excitations form a categorified chain complex: the fusion algebra on anyonic charges has composition rules generalizing boundary operators. Modular functors underlie the Jones polynomial — the same mathematical object that generates Khovanov homology.
- **Stability**: Physical error correction with error rate scaling as e^{-αℓ} where ℓ is a length scale. This is the strongest form of topological protection — exponential suppression by a geometric parameter, not a code distance. Contrasts with "qubit-model" requiring initial error rate ~10^{-4}.
- **Matching**: Anyon braiding = assignment of quasiparticle worldlines in (2+1)D spacetime. The computational gates are determined by the braiding topology, not the geometric details — a topological matching.
- **Null hypothesis**: Abelian anyons (trivial braiding statistics) as null. Non-Abelian anyons are required for universal quantum computation. The gap between Abelian and non-Abelian is the gap between trivial and computationally universal.

**What is genuinely new (not reducible to shared abstraction)**:
- Computation itself as a topological invariant. Not just using topology for error correction — the computation IS the topology. Braiding worldlines compute gate operations.
- The connection to the Jones polynomial and Witten-Chern-Simons theory provides a bridge from QEC to pure mathematics (knot invariants, 3-manifold invariants).
- The error scaling e^{-αℓ} is qualitatively different from e^{-c·d} (code distance scaling) — it's continuous, geometric, and doesn't require discrete code blocks.

**Connections the authors acknowledge**: Explicit connection to Jones polynomial, Chern-Simons theory, fractional quantum Hall effect. Bridge between QEC and condensed matter physics.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Modular functor | Chain complex (categorified) |
| Anyon braiding | Matching (topological assignment) |
| Topological protection e^{-αℓ} | Stability (exponential suppression) |
| Abelian anyons | Null (trivial braiding = no computation) |
| Fusion rules | Boundary operator (composition law) |

---

## 2106.04024 --- Barannikov, Trofimov, Sotnikov, Trimbach, Korotin, Filippov, Burnaev (2021)
**"Manifold Topology Divergence: a Framework for Comparing Data Manifolds"**

**Domain(s)**: TDA

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Cross-Barcode(P,Q) IS the joint-vs-marginal measure for topological features. Given two distributions P and Q, it tracks multiscale topological discrepancies between their support manifolds. MTop-Divergence = 0 iff manifolds are topologically equivalent; positive values quantify the excess structure in one manifold relative to the other.
- **Parameterized homology**: Multi-scale tracking of topological features across spatial scales. The Cross-Barcode records birth-death events as the comparison resolution varies — a parameterized invariant of the pair (P,Q).
- **Matching**: The Cross-Barcode implicitly matches topological features across the two manifolds. Unmatched features (present in one but not the other) are the discrepancy signal.
- **Null hypothesis**: Identical manifolds give zero divergence — this is the null. Mode-dropping, mode-collapse, mode-invention all produce non-zero MTop-Divergence in characteristic ways.

**What is genuinely new (not reducible to shared abstraction)**:
- First TDA tool that gives a PAIRWISE comparison of manifold topology, not just a feature summary of one space. Fills the gap: standard PH characterizes a single space; Cross-Barcode characterizes the relationship between two spaces.
- Scales linearly with ambient dimension — practical for high-dimensional generative model evaluation.
- Domain-agnostic: works on images, 3D shapes, time series without pretrained networks.
- The cross-barcode is conceptually distinct from comparing two persistence diagrams via Wasserstein distance (which is a Matching operation). It builds a SINGLE barcode from the pair, not two barcodes that are then compared.

**Connections the authors acknowledge**: Builds on persistent homology (Edelsbrunner, Zomorodian). No cross-domain citations.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Cross-Barcode(P,Q) | Joint-vs-marginal (topological excess between manifolds) |
| MTop-Divergence | Divergence measure (analogous to D_KL for topology) |
| Mode-dropping | Feature death in one manifold |
| Mode-invention | Feature birth in one manifold |
| Multi-scale | Parameterized (filtration scale) |

---

## 0711.0468 --- Bombin & Martin-Delgado (2007)
**"Statistical Mechanical Models and Topological Color Codes"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: Color codes on trivalent lattices (triangular, Union Jack). Different cellulation from toric code but same homological machinery. The key difference: Z₂×Z₂ gauge group (vs Z₂ for toric code), yielding richer transversality — direct implementation of quantum Clifford gates. The overlap of a color code state with a factorized state IS the partition function of a 3-body classical Ising model.
- **Stability**: Error threshold p_c = 0.109(2) (from Katzgraber-Bombin-Martin-Delgado 2009), very close to toric code threshold (~0.109). Enhanced computational capabilities does NOT imply lower noise resistance.
- **Null hypothesis**: Factorized state of qubits as null. The partition function measures the overlap between the topologically ordered state and the structureless null. Different universality classes of the associated Ising models correspond to different computational capabilities.
- **Joint-vs-marginal excess**: The color code has richer entanglement structure than the toric code (Z₂×Z₂ vs Z₂). The excess manifests as ability to perform transversal Clifford gates — structure present in the color code joint state that is absent from simpler codes.

**What is genuinely new (not reducible to shared abstraction)**:
- The mapping code state ↔ partition function is EXACT, not approximate. Different QEC codes correspond to different universality classes of classical spin models. This is the deepest QEC↔stat-mech bridge.
- 3-body interactions (vs 2-body for toric code). The cellulation matters: trivalent lattice enables different gates than square lattice.
- Classical simulatability of measurement-based computation on color codes remains open — a genuine computational complexity question that doesn't reduce to topology.

**Connections the authors acknowledge**: Explicit mapping to statistical mechanics (Ising models). References Kitaev's toric code as comparison.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Color code | Chain complex (Z₂×Z₂ cellulation) |
| Partition function overlap | Joint-vs-marginal (code vs factorized) |
| Universality class | Phase transition (stability boundary) |
| Factorized state | Null (structureless reference) |
| Trivalent lattice | Cellulation (different from square lattice) |

---

## 10.1371/journal.pcbi.1003588 --- Oizumi, Albantakis, Tononi (2014)
**"From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0"**

**Domain(s)**: neuroscience, information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: THE foundational formalization of this machine in neuroscience. Integrated information Φ measures how much the whole system's information exceeds the sum of its parts. Mathematically: Φ = D(p(X^t|X^{t-1}) || Π_i p(X_i^t|X_i^{t-1})) — the divergence between the system's transition probability and the product of its parts' transition probabilities. A conscious system has Φ > 0; higher Φ = more conscious.
- **Null hypothesis**: The "partitioned" system (parts operating independently) is the explicit null. Φ quantifies departure from this null. The minimum information partition (MIP) is the partition that makes Φ smallest — the hardest-to-destroy integration.
- **Stability**: The exclusion postulate enforces a form of stability: the complex with maximal Φ (the "main complex") is the one that exists. Perturbations that don't change which complex is maximal don't change the experience.
- **Parameterized homology**: Φ varies with the spatiotemporal grain of analysis. The exclusion postulate selects the grain that maximizes Φ — a critical value in the parameterization.

**What is genuinely new (not reducible to shared abstraction)**:
- Φ is derived from phenomenological axioms (existence, composition, information, integration, exclusion), not from physics or mathematics. The axioms constrain the form of the measure.
- The maximally irreducible conceptual structure (MICS) specifies not just the quantity but the QUALITY of experience — the shape of the structure in concept space.
- IIT predicts that simple systems can be conscious and complex ones (e.g., feed-forward networks) cannot. This is a testable, counterintuitive prediction that doesn't follow from any of the six machines alone.
- The theory addresses the "hard problem" of consciousness directly — it's not a computational theory but a physical one.

**Connections the authors acknowledge**: References Shannon information theory, Kullback-Leibler divergence, causal analysis. The PID decomposition (Williams-Beer) is related but not cited — Tononi's decomposition predates PID.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Integrated information Φ | Joint-vs-marginal excess |
| Minimum information partition | Null (optimal partition = hardest null) |
| Main complex | Stability (maximal Φ complex persists) |
| Spatiotemporal grain | Parameterization (filtration over scales) |
| Conceptual structure (MICS) | Homology class (the invariant shape) |
| Exclusion postulate | Uniqueness (one complex, one experience) |

---

## 10.1038/s41586-021-04268-7 --- Gardner, Hermansen, Pachitariu, Burak, Baas, Dunn, M. Moser, E. Moser (2022)
**"Toroidal topology of population activity in grid cells"**

**Domain(s)**: Neuroscience, TDA

**Abstract machines instantiated**:
- **Chain complex**: The central result is that the joint activity of grid cells from an individual module lies on a toroidal manifold T². The torus has homology H₀(T²,Z) = Z, H₁(T²,Z) = Z², H₂(T²,Z) = Z. The two independent 1-cycles generating H₁ correspond to the two periodic spatial dimensions encoded by the grid cell module. This is the SAME topological object as the base space of Kitaev's toric code, where H₁(T²,Z/2) = (Z/2)² defines two logical qubits. In neuroscience the two 1-cycles encode two spatial coordinates; in QEC they encode two logical qubits. The chain complex is constructed explicitly via cohomology of the point cloud (population activity vectors projected to the manifold).
- **Parameterized homology**: Persistent homology across filtration scales is the primary analytical method. The authors apply PH to the population activity point cloud and observe persistent cohomology classes in dimensions 0, 1, and 2 consistent with the torus: one component (b₀=1), two independent 1-cycles (b₁=2), one 2-cycle (b₂=1). The persistence of these classes across a range of filtration scales — rather than appearing briefly and dying — is the evidence that the toroidal topology is a genuine feature of the data, not an artifact. This is textbook parameterized homology: the topological invariant (Betti numbers of T²) is tracked as the scale parameter varies.
- **Stability**: The toroidal structure persists across multiple perturbation regimes: (1) different physical environments (open field, linear track, novel vs. familiar), (2) different brain states (active waking, REM sleep, quiet wakefulness), and (3) different recording sessions. The positions of individual cells on the torus are maintained across these conditions. This is empirical stability: the topological invariant (toroidal manifold structure and cell positions on it) is robust under perturbation of the external conditions. This stability distinguishes CAN models (which predict a fixed attractor manifold) from feedforward models (which predict environment-dependent structure).
- **Null hypothesis**: Two explicit nulls are tested. (1) Feedforward models: if grid cell firing is driven primarily by feedforward sensory input (e.g., path integration from border cells or visual landmarks), the population activity manifold would change with the environment and would not persist during sleep. The toroidal structure during sleep and across environments falsifies this null. (2) Surrogate data: shuffled spike trains and random rotations of tuning curves serve as statistical nulls against which the persistence of cohomological features is tested.
- **Joint-vs-marginal excess**: The torus is a POPULATION-level object — it emerges from the joint activity of hundreds of simultaneously recorded grid cells. No single cell's firing pattern reveals the toroidal topology. Each individual cell fires in a hexagonal grid pattern (its marginal), but the toroidal manifold structure is invisible from any collection of marginals. The joint activity vector traces out the torus; the marginal firing rate maps of individual cells are periodic functions ON the torus but do not themselves reveal it. This is the strongest neuroscience demonstration that topological structure can be purely a property of the joint, not the marginals.

**What is genuinely new (not reducible to shared abstraction)**:
- The torus is not constructed (as in QEC) but DISCOVERED in empirical neural data. In QEC, one designs a code on T² by choosing a cellulation and placing qubits on cells. Here, the torus is an emergent property of neural dynamics — nobody designed it. The same abstract object (T²) arises from two completely different generative processes.
- The correspondence between positions on the torus and positions of the animal in physical space. The torus is not just a topological invariant but a FUNCTIONAL map: it encodes the animal's allocentric position. This functional role has no analogue in QEC (where positions on the torus label stabilizer configurations, not physical locations).
- The persistence of cell positions on the torus during sleep, when there is no external spatial input. This implies the torus is maintained by internal dynamics (a continuous attractor network), not by ongoing sensory calibration. The attractor is self-sustaining — a dynamical systems result that goes beyond static topology.
- Simultaneous recording of hundreds of grid cells (Neuropixels probes) is a methodological achievement that enables the population-level analysis. Previous work on individual grid cells could not access the joint manifold.

**Connections the authors acknowledge**: The authors explicitly use persistent cohomology as their primary analytical tool, citing Carlsson, de Silva, and the computational topology literature. They acknowledge the CAN (continuous attractor network) model from dynamical systems as the theoretical framework predicting the torus. They do NOT cite or acknowledge any connection to QEC, toric codes, or Kitaev's work — despite the shared T² being the strongest cross-domain bridge in the entire Rosetta.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Grid cell module | Population of neurons encoding a single spatial scale |
| Toroidal manifold | T² — the torus as neural manifold (= base space of toric code in QEC) |
| Persistent cohomology | Parameterized homology (tracking invariants across filtration scales) |
| Betti numbers (1,2,1) | Homological signature of T²: b₀=1, b₁=2, b₂=1 |
| Two independent 1-cycles | Generators of H₁(T²,Z) = Z² (= two logical qubits in toric code) |
| Continuous attractor network (CAN) | Dynamical system whose attractor is a manifold (here T²) |
| Feedforward model | Alternative (non-attractor) hypothesis — the null |
| Cell position on torus | Preferred firing location on the attractor manifold |
| Environment stability | Topological robustness under perturbation of external conditions |
| Wake-to-sleep persistence | Stability of the attractor under state change |
| Population activity vector | Joint state (point on the neural manifold) |
| Individual grid cell firing | Marginal (periodic function on T², not revealing T² itself) |
| Neuropixels recording | Simultaneous high-density measurement enabling joint analysis |

---

## DOI: 10.1126/science.1227079 --- Sugihara, May, Ye, Hsieh, Deyle, Fogarty, Munch (2012)
**"Detecting Causality in Complex Ecosystems"**

**Domain(s)**: Dynamical systems, information theory (causal inference)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: CCM IS a joint-vs-marginal test. The method asks: does the shadow manifold reconstructed from Y contain information about X that is absent from Y's own marginal dynamics? If X causes Y, then by Takens' theorem Y's attractor embeds X's states — the joint manifold (reconstructed from both variables) contains more predictive information than either marginal manifold alone. Cross-prediction success = the excess of joint over marginal. This is the dynamical systems analogue of transfer entropy's conditional MI, but operating on reconstructed state spaces rather than probability distributions.
- **Stability**: The convergence criterion is the signature diagnostic. As library size L increases (more data from the shadow manifold is used), cross-prediction skill should converge — improve monotonically and stabilize. This convergence IS a stability property: the topological information encoded in the attractor is robust to subsampling, and recoverable as sampling density increases. Additionally, Takens' embedding theorem provides the foundational stability guarantee: for generic embedding parameters (dimension m, delay tau), the reconstructed shadow manifold is diffeomorphic to the true attractor — the topology is preserved under the reconstruction.
- **Null hypothesis**: The null is no causal coupling between X and Y. Under this null, cross-prediction does NOT converge — skill is flat or non-increasing with library size. Surrogate methods (randomized time indices, phase-shuffled series) provide the null distribution by destroying temporal coupling while preserving marginal statistics. Granger causality serves as the implicit "alternative method" null: CCM is specifically designed for cases where Granger fails — nonlinear systems with synergistic effects where causal variables appear uncorrelated.
- **Parameterized homology** (weak): Library size L parameterizes the cross-prediction skill. The convergence curve rho(L) traces how prediction accuracy improves with L — analogous to tracking a topological feature across a filtration. At small L, insufficient data yields poor reconstruction (feature not yet born); at large L, the manifold is faithfully reconstructed and prediction converges (feature stabilizes). The embedding dimension m and time delay tau are additional parameters controlling the reconstruction, directly inherited from Takens' framework.

**What is genuinely new (not reducible to shared abstraction)**:
- The convergence criterion as a CAUSAL test: the direction of prediction asymmetry identifies the direction of causation. If X causes Y but Y does not cause X, then cross-mapping from Y's manifold to X converges, but not vice versa. This directional asymmetry is specific to causality — symmetric measures (MI, correlation) cannot distinguish driver from driven.
- CCM handles the case where causal variables appear uncorrelated — separability failure. In nonlinear coupled systems, strong causation can produce ZERO correlation. Granger causality, which relies on incremental prediction improvement in linear models, fails here. CCM succeeds because it operates on the full nonlinear manifold structure.
- The distinction between CCM and Granger causality maps onto a deeper distinction: Granger tests whether Y's past helps predict X's future (a conditional probability statement); CCM tests whether Y's attractor geometry contains X's information (a topological/dynamical statement). The former is statistical; the latter is geometric.
- Mirage correlations: the paper demonstrates that purely deterministic coupled systems can exhibit spurious correlations that reverse sign depending on parameters. CCM correctly identifies the causal direction even when correlation gives the wrong sign.

**Connections the authors acknowledge**: Takens (1981) embedding theorem as the theoretical foundation. Granger causality as the comparison method (and its limitations for nonlinear systems). Ecological applications (sardine-anchovy-SST coupling). No connections to TDA, QEC, or information theory — though the relationship to transfer entropy is implicit (both test directed information flow; TE via probabilities, CCM via manifold geometry).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Convergent cross-mapping | Directed joint-vs-marginal test (manifold-based) |
| Shadow manifold | Takens reconstruction (topology-preserving embedding) |
| Cross-prediction skill rho | Joint-vs-marginal excess (prediction improvement) |
| Library size L | Parameterization (analogous to filtration scale) |
| Convergence with L | Stability (feature persistence under increasing data) |
| No convergence (flat rho) | Null hypothesis (no causal coupling) |
| Embedding dimension m | Reconstruction parameter (controls manifold dimension) |
| Time delay tau | Reconstruction parameter (controls temporal resolution) |
| Granger causality | Alternative null method (linear, separable assumption) |
| Mirage correlation | Spurious structure destroyed by proper null test |
| Causal direction asymmetry | Directed excess (rho_{Y->X} != rho_{X->Y}) |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

## 1507.06217 --- Adams, Chepushtanova, Emerson, Hanson, Kirby, Motta, Neville, Peterson, Shipman, Ziegelmeier (2017)
**"Persistence Images: A Stable Vector Representation of Persistent Homology"**

**Domain(s)**: TDA

**Abstract machines instantiated**:
- **Parameterized homology**: Persistence images ARE a featurization of parameterized homology. The pipeline is: data -> filtration (Vietoris-Rips or sublevel set) -> persistence diagram (birth-death pairs tracking homological features across scale) -> linear transformation T(x,y) = (x, y-x) to birth-persistence coordinates -> weighted sum of Gaussians centered at each point (persistence surface rho_B) -> integration over a pixel grid -> fixed-size vector in R^n. The entire construction takes the output of parameterized homology and converts it into a form amenable to ML. Different homological dimensions (H_0, H_1, ...) can be concatenated into a single vector.
- **Stability**: The central theoretical contribution. Theorem 1 proves the persistence surface is stable with respect to the 1-Wasserstein distance: ||rho_B - rho_{B'}||_inf <= C * W_1(B, B'), where C = sqrt(10) * (||f||_inf * |grad(phi)| + ||phi||_inf * |grad(f)|). Theorem 2 extends to persistence images (the discretized vectors) with L_inf, L_1, and L_2 bounds. Theorem 3-4 give tighter constants for Gaussian distributions specifically, including an L_1 bound on the surface itself. Remark 1 proves that PI stability is IMPOSSIBLE for p-Wasserstein with p > 1 (via Reininghaus et al. 2015 Theorem 3). The weighting function f (zero on the diagonal, continuous, piecewise differentiable) is essential for stability -- without it, points emerging from the diagonal create discontinuities.
- **Matching**: Implicit but foundational. The Wasserstein distance W_p(B, B') = inf_gamma (sum ||u - gamma(u)||^p_inf)^{1/p} over bijections gamma between diagrams IS an optimal matching problem. The stability proofs work by bounding the PI difference in terms of an optimal matching gamma that achieves the Wasserstein infimum. The weighting function f assigns importance to matched pairs based on their position (persistence value), but f itself is not a matching -- it modulates the Gaussians centered at already-matched points.
- **Chain complex**: Implicit -- the persistence diagrams that serve as input to the PI pipeline are computed from simplicial (Vietoris-Rips) or cubical chain complexes. Appendix A explicitly defines the chain complex: vector spaces C_k of k-chains, boundary operators partial_k mapping k-simplices to their (k-1)-faces, cycles Z_k = ker(partial_k), boundaries B_k = im(partial_{k+1}), and homology H_k = Z_k/B_k. The paper does not innovate on the chain complex construction; it takes persistence diagrams as given input.

**What is genuinely new (not reducible to shared abstraction)**:
- The specific vectorization pipeline (PD -> birth-persistence coordinates -> weighted Gaussian sum -> pixel grid integration) is an engineering contribution with carefully controlled mathematical properties. The combination of weighting function + Gaussian smoothing + grid integration is what simultaneously achieves stability, interpretability, and fixed-dimensionality.
- The weighting function f provides domain-adaptable importance: non-decreasing in persistence (standard: high-persistence = signal), but also allowing non-standard weightings (Bendich et al. 2015 found medium-persistence features most discriminative for brain arterial geometry). This flexibility within a stability-preserving framework is novel.
- The impossibility result (Remark 1): PI inner product kernel is not stable w.r.t. W_p for p > 1. This is a genuine negative result constraining the design space -- stability is only achievable for W_1.
- The dynamical systems applications (linked twist map parameter classification at 82.5% accuracy; anisotropic Kuramoto-Sivashinsky parameter inference at 97.3%) demonstrate that PH captures parameter-dependent structure in dynamics -- a bridge between TDA and dynamical systems that the authors exploit but do not theorize about in Rosetta terms.
- Sparse SVM pixel selection identifies 10 discriminatory pixels (out of 400) achieving 100% classification accuracy. The selected pixels are interpretable: they correspond to specific regions of the persistence diagram, connecting ML feature importance back to topological meaning.

**Connections the authors acknowledge**: Extensive comparison with persistence landscapes (Bubenik 2015), kernel methods (Reininghaus et al. 2015), complex polynomial encoding (Di Fabio & Ferri 2015), and binning approaches (Bendich et al. 2014). Use PH stability theorem of Cohen-Steiner et al. (2007) as foundation. Applications to dynamical systems (linked twist map, Kuramoto-Sivashinsky PDE) but no connection drawn to dynamical systems theory per se. No connections to QEC, information theory, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Persistence diagram | Output of parameterized homology |
| Persistence image | Fixed-size vector featurization of parameterized homology |
| Persistence surface rho_B | Continuous featurization (pre-discretization) |
| Birth-persistence coordinates | Reparameterized diagram (T(x,y) = (x, y-x)) |
| Weighting function f | Importance modulation on diagram features |
| 1-Wasserstein distance W_1 | Optimal matching cost (L1 transport) |
| Bottleneck distance W_inf | Optimal matching cost (minimax transport) |
| Gaussian phi_u | Smoothing kernel (localization in feature space) |
| Pixel grid integration | Discretization of continuous representation |
| Vietoris-Rips complex | Chain complex from point cloud (distance threshold) |
| Sublevel set filtration | Chain complex from function (level set threshold) |
| Resolution (grid size) | Discretization granularity |
| Variance sigma^2 | Smoothing bandwidth |
| SSVM feature selection | Identifying discriminatory regions of the diagram |

**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`, `by-domain/tda.md`

---

## 1703.00810 --- Shwartz-Ziv & Tishby (2017)
**"Opening the Black Box of Deep Neural Networks via Information"**

**Domain(s)**: Information theory, machine learning

**Abstract machines instantiated**:
- **Parameterized homology**: THE primary machine in this paper. Training epoch is the parameter; the invariants are the information plane coordinates (I(X;T), I(T;Y)) for each hidden layer T. As training progresses, each layer traces a path in the information plane. Two qualitative phases emerge: a *fitting* phase (both coordinates increase, ~350 epochs) and a *compression* phase (I(X;T) decreases while I(T;Y) stays high, consuming the majority of training time). The transition between phases — where gradient SNR drops from drift-dominated to diffusion-dominated — is a critical parameter value analogous to a birth/death event in persistence. The authors show that converged layers lie on or near the Information Bottleneck (IB) theoretical bound, with each layer corresponding to a different value of the Lagrange multiplier beta. The information plane trajectory across layers satisfies Data Processing Inequality chains: I(X;T_1) >= I(X;T_2) >= ... >= I(X;T_K), creating a monotonic "information path" structurally analogous to a filtration where successive layers correspond to progressively coarser scales.
- **Joint-vs-marginal excess**: Each MI quantity I(X;T) and I(T;Y) is itself a joint-vs-marginal measure: D_KL(P_{X,T} || P_X * P_T). The information plane plots how much each layer's representation T shares with input X (encoder quality) and output Y (decoder quality) beyond what independent marginals would predict. Inter-layer MI I(T_i; T_j) is implicit in the Markov chain structure — each layer is a compressed view (marginal) of the input, and the joint network captures dependencies across layers that no single layer contains.
- **Null hypothesis**: Random initialization serves as the null — the untrained network has near-zero I(T;Y) (deep layers fail to preserve relevant information). The compression phase implements a learned null: the network destroys information about X that is irrelevant for Y, converging to a maximum-entropy representation under the training error constraint. This selective destruction parallels surrogate construction: preserve task-relevant coupling (I(T;Y)), destroy everything else (minimize I(X;T) for given I(T;Y)). The diffusion phase of SGD acts as the destruction mechanism — weight updates become Wiener processes (random noise), and the Fokker-Planck stationary distribution maximizes conditional entropy H(X|T).
- **Stability**: The information plane trajectories are robust across 50 randomized initializations — different random seeds produce qualitatively similar paths that converge to nearby points. This reproducibility justifies averaging over randomizations. The converged layers satisfy the IB self-consistent equations (Eq. 9) within numerical precision, with the optimal beta found by minimizing KL divergence between the layer's encoder and the IB-optimal encoder. The IB bound itself is a stability result: the information curve is a concave boundary that no representation can exceed.

**What is genuinely new (not reducible to shared abstraction)**:
- The drift-to-diffusion phase transition in SGD gradient statistics. The shift from high gradient SNR (mean >> std) to low gradient SNR (std >> mean) at ~350 epochs is a dynamical phenomenon with no direct analogue in persistence (where the filtration parameter is externally controlled, not emergent from optimization dynamics). The parameter that drives the information plane trajectory is not prescribed — it emerges from the interaction between the loss landscape and stochastic optimization.
- The computational benefit of depth via diffusion. The paper argues that hidden layers reduce the relaxation time exponentially: compressing by Delta_IX via diffusion takes exp(Delta_IX / D) epochs, but splitting this across K layers yields sum of exp(Delta_IX^k / D), which is exponentially smaller (Eq. 11). This is an argument about parallelization of compression that has no analogue in persistence computation.
- The claim that individual neuron/weight interpretation is meaningless — the compression phase randomizes weights while preserving layer-level information, so exponentially many different weight configurations yield the same information plane point. This is a statement about the quotient structure: the equivalence class of networks under information-preserving reparameterization is enormous.
- **CRITICAL CAVEAT**: Saxe et al. (2018) showed that the compression phase disappears with ReLU activations and only appears with saturating activations (tanh, sigmoid). Geiger (2021) provided a systematic review showing that observed compression is often an artifact of binning-based MI estimation — when representations cluster geometrically, binned MI estimates decrease even if the true MI does not. This is already noted in ANTISYNONYMS.md ("Information plane compression != feature death"). The paper's experiments use tanh activations and 30-bin discretization, both of which are now known to favor the appearance of compression. The two-phase narrative remains influential but is not universally accepted as a property of deep learning per se, rather than a property of saturating-activation networks analyzed with binning estimators.

**Connections the authors acknowledge**: Cite the Information Bottleneck framework (Tishby et al., 1999) and Tishby & Zaslavsky (2015) as the direct predecessor. Reference SGD noise literature (Achille & Soatto, 2016; Balduzzi et al., 2017; Kadmon & Sompolinsky, 2016). Discuss connections to sufficient statistics and rate-distortion theory. No citations to TDA, QEC, dynamical systems (except tangentially via diffusion equations), or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Information plane | Parameter space for the invariant (I(X;T), I(T;Y)) |
| Information path | Trajectory in parameter space (analogous to barcode) |
| Fitting phase (ERM) | Birth event / feature emergence |
| Compression phase | Death event / feature destruction (but see caveats above) |
| Drift-diffusion transition | Critical parameter value |
| Data Processing Inequality chain | Monotonicity of filtration (nested representations) |
| IB bound (information curve) | Stability boundary (optimal achievable invariant) |
| Lagrange multiplier beta | Filtration scale (parameterizes the tradeoff) |
| Encoder P(T|X) | Forward map in Markov chain (representation) |
| Decoder P(Y|T) | Backward map (prediction from representation) |
| Layer T | Component in composite system (marginal view) |
| Joint network | Composite system |
| Random initialization | Null model (no learned structure) |
| Diffusion / stochastic relaxation | Entropy maximization (null construction mechanism) |
| IB self-consistent equations | Fixed-point conditions for optimal representation |

**See also**: `by-structure/filtrations.md`, `by-structure/composite_systems.md`, `by-domain/information_theory.md`

---

## 10.1017/S0140525X01000097 --- Tsuda (2001)
**"Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems"**

**Domain(s)**: Neuroscience, dynamical systems

**Abstract machines instantiated**:
- **Parameterized homology**: This is the primary machine. Chaotic itinerancy (CI) is a trajectory that wanders among "attractor ruins" (also called attractor relics or attractor ghosts) — remnants of attractors that existed before a bifurcation destroyed them. As the system evolves in time, it visits quasi-stable neighborhoods with DIFFERENT topological structure: each attractor ruin has its own basin geometry, dimensionality, and local topology. The itinerant trajectory thus traces a PATH THROUGH TOPOLOGY SPACE — a sequence of distinct topological configurations, parameterized by time. This is parameterized homology where the parameter is time itself, and the invariant being tracked is the local attractor topology (dimension, basin structure, Lyapunov spectrum). At each quasi-stable epoch, the system has an approximate topology; transitions between epochs are topology-changing events. The sequence of visited attractor ruins defines an itinerary through a discrete set of topological states — structurally analogous to a barcode where each bar represents a quasi-stable epoch and transitions are births/deaths.
- **Stability**: Quasi-stability — the system lingers near attractor ruins long enough for functional computation (perception, memory recall, decision-making), but the attractors themselves are DESTROYED. The ruins are not true attractors (they have been annihilated by parameter change or coupling), yet they retain enough of the original attractor's geometry to temporarily trap trajectories. This is anti-stability in a precise sense: the attractors that would provide permanent stability have been destroyed, but the system exploits the residual geometric structure (the "ghost" of the attractor) for transient stability. Milnor attractors — attractors whose basin of attraction has positive measure but is not open — formalize this intermediate status. The functional claim is that this quasi-stability is not a defect but a FEATURE: it allows the brain to be simultaneously stable enough for coherent processing and flexible enough to transition between states.
- **Null hypothesis**: A fixed-point attractor, limit cycle, or conventional strange attractor is the null — simple, non-itinerant dynamics where the system converges to a single invariant set and stays there. Chaotic itinerancy is the departure from this null: the system visits MULTIPLE invariant-like sets without permanently settling. The Kaplan-Yorke dimension and Lyapunov spectrum of the full trajectory exceed what any single attractor would produce — the excess is the signature of itinerancy. Tsuda explicitly contrasts CI with both fixed-point dynamics (too rigid for brain function) and fully developed chaos (too unstructured for information processing). CI occupies the dynamically interesting intermediate regime.
- **Chain complex** (weak): Each attractor ruin has its own homology — a local topological signature (dimension, number of holes, basin topology). The sequence of ruins visited by the itinerant trajectory defines a path through these homology classes. While Tsuda does not construct an explicit chain complex, the framework implies one: the state space is decomposed into neighborhoods of attractor ruins (cells), with transitions between them (analogous to boundary maps connecting cells of different dimension in a CW complex). The heteroclinic-like connections between ruins provide the "boundary" structure linking one quasi-stable state to another.

**What is genuinely new (not reducible to shared abstraction)**:
- The concept of "attractor ruins" (attractor relics/ghosts) is domain-specific and has no direct analogue in TDA, QEC, or information theory. An attractor ruin is the geometric remnant of an attractor that has been destroyed by bifurcation — it still shapes nearby trajectories but does not permanently capture them. This is a dynamical object, not a topological or information-theoretic one.
- The functional interpretation: CI is proposed as the dynamical mechanism underlying specific cognitive processes — olfactory perception (Freeman's work on olfactory bulb dynamics), episodic memory (itinerancy among memory states), and cognitive flexibility. The claim that the brain REQUIRES destroyed attractors for flexible cognition is a neuroscience-specific hypothesis.
- The distinction between Milnor attractors and standard attractors. Milnor attractors have basins of positive Lebesgue measure but are not asymptotically stable in the usual sense — trajectories may leave and return. This intermediate notion of attraction has no analogue in TDA (where features are either present or absent in a persistence diagram) or QEC (where logical information is either protected or lost).
- The connection to the "edge of chaos" hypothesis: CI provides a concrete dynamical mechanism for the informal idea that the brain operates at a critical boundary between order and chaos. Unlike generic criticality arguments, CI specifies the GEOMETRY of this boundary — it is a network of heteroclinic-like connections among attractor ruins.
- Tsuda's specific application to cortical dynamics: the proposal that transitions between attractor ruins correspond to transitions between cognitive states (e.g., different percepts in multistable perception, different memory items in free recall). This maps CI onto experimentally measurable neural phenomena.

**Connections the authors acknowledge**: Tsuda explicitly connects to Freeman's work on olfactory bulb chaos, to Kaneko's globally coupled maps (where CI was first computationally demonstrated), and to Milnor's mathematical theory of attractors. The paper bridges neuroscience and dynamical systems by construction. No connections to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Chaotic itinerancy | Path through topology space (parameterized by time) |
| Attractor ruin / relic / ghost | Destroyed invariant set retaining geometric influence |
| Quasi-stable state | Transient epoch with approximate local topology |
| Milnor attractor | Attractor with positive-measure but non-open basin |
| Itinerant trajectory | Sequence of topology-changing transitions |
| Heteroclinic connection | Transition between attractor ruins (boundary-like map) |
| Fixed-point / limit-cycle attractor | Null model (non-itinerant dynamics) |
| Kaplan-Yorke dimension | Dimensionality of the attractor (local invariant) |
| Lyapunov exponent | Stability/instability diagnostic |
| Edge of chaos | Critical regime between null (order) and full chaos |
| Olfactory bulb dynamics (Freeman) | Empirical instantiation of CI in neural tissue |

**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`, `by-domain/neuroscience.md`, `by-domain/dynamical_systems.md`

---

## Still to find

- Ay, Polani — information decomposition (PID). Synergy/redundancy as joint-vs-marginal. (May overlap with Kolchinsky 2024 already annotated.)
- Riehl — "Category Theory in Context." The abstract machines here are functors. Worth formalizing? (Low priority — textbook, not paper.)

---

## Wave 4c: Stability x QEC — Foundational Threshold Theorem Papers (2026-04-06)

---

## quant-ph/9906129 --- Aharonov & Ben-Or (1997/1999)
**"Fault-Tolerant Quantum Computation with Constant Error Rate"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: Uses Calderbank-Shor-Steane (CSS) quantum error correcting codes, which are defined by pairs of classical codes satisfying an orthogonality condition (H_Z H_X^T = 0 mod 2). This IS the chain complex condition: two boundary operators whose composition vanishes. The paper also introduces *polynomial codes* over F_p — a new class of CSS codes where codewords are superpositions of evaluations of random polynomials of degree d over a finite field. The algebraic structure of polynomial codes (degree filtration, evaluation maps) provides a graded chain complex with systematic fault-tolerant procedures derived from the algebraic properties.
- **Parameterized homology**: The error rate eta parameterizes the family. Below the threshold eta_c, the logical error rate is exponentially suppressed via concatenation: after r levels, the effective error is reduced to eta_eff ~ (c * eta)^{2^r}. The threshold eta_c is THE critical value — a phase transition between correctable and uncorrectable regimes. The paper estimates eta_c ~ 10^{-6} for polynomial codes.
- **Stability**: THE foundational stability result for quantum computation. The key theorem: if eta < eta_c, then arbitrarily long quantum computations can be performed with arbitrarily high reliability, at polylogarithmic overhead in space and time. The stability is achieved through recursive concatenation — each level of simulation improves reliability, and the improvement is exponential in the number of levels. The result holds for a very general noise model: probabilistic errors, decoherence, amplitude damping, depolarization, systematic inaccuracies, and even exponentially decaying correlations in space and time.
- **Null hypothesis**: The uncorrected quantum circuit (no error correction) as null. Without error correction, noise accumulates and ruins the computation — the error probability grows with circuit size. The threshold theorem quantifies the gap: with correction, the error can be made arbitrarily small at polylogarithmic cost; without correction, it grows without bound.

**What is genuinely new (not reducible to shared abstraction)**:
- The *constant error rate* threshold. Shor's prior result required the error rate to shrink polylogarithmically with computation size — physically unreasonable. Aharonov & Ben-Or show a CONSTANT threshold suffices. This is the quantum analogue of von Neumann's 1956 result for classical circuits.
- Polynomial codes: a new class of quantum codes where fault-tolerant procedures have a "simple and systematic structure" derived from the algebra of polynomials over finite fields. The degree-reduction step (interpolation on encoded states) has no analogue in other domains.
- No measurements or classical operations required during quantum computation. The quantum model is self-contained — it can be made fault-tolerant within itself. This eliminates the need for classical control, which itself could be noisy.
- Generality of the noise model: works with nearest-neighbor interactions on a 1D line, qupits (p > 2 states), exponentially decaying correlations — far beyond the independent stochastic model.
- The recursive concatenation proof technique: the hierarchical circuit M_r where each qubit becomes a block, each block becomes a block of blocks, etc. The analysis involves tracking "sparse fault paths" through the hierarchy — a combinatorial argument specific to the recursive structure.

**Connections the authors acknowledge**: Cite Knill, Laflamme, Zurek as independent co-discoverers of the threshold theorem. Cite Kitaev's toric code approach as an alternative (topological rather than concatenation-based). Situated entirely within QEC/quantum complexity theory. No connections to TDA, dynamical systems, neuroscience, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Error rate eta | Perturbation magnitude (parameter) |
| Threshold eta_c | Critical value (phase transition) |
| Concatenated code | Hierarchical chain complex (recursive) |
| Polynomial code | Chain complex over F_p (algebraic) |
| CSS code orthogonality H_Z H_X^T = 0 | Chain complex condition (partial^2 = 0) |
| Fault-tolerant procedure | Stability-preserving map |
| Recursive simulation M_r | Hierarchical refinement (r levels of correction) |
| Effective error (c*eta)^{2^r} | Exponential suppression (stability bound) |
| Sparse fault path | Correctable error pattern (element of boundary image) |
| Non-sparse fault path | Uncorrectable error (non-trivial homology class) |
| Block of qubits | Code space (protected subspace) |
| Logical state | Homology class (invariant under correction) |

**See also**: `by-structure/phase_transitions.md`, `by-domain/qec.md`

---

## quant-ph/9702058 --- Knill, Laflamme, Zurek (1998)
**"Resilient Quantum Computation: Error Models and Thresholds"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: Uses the 7-qubit Steane code (based on the classical [7,4,3] Hamming code) as the base code. The Hilbert space decomposes as Q^{tensor 7} = A tensor S, where A is the abstract (logical) qubit and S is the syndrome space. The six stabilizer observables S_1...S_6 (built from tensor products of Pauli operators) define the boundary operators. Syndrome measurement projects onto the code space — analogous to projection onto ker(partial)/im(partial). The normalizer group of the code provides the algebraic structure for encoded operations.
- **Parameterized homology**: Error probability p parameterizes the family. The concatenation procedure maps p to cp^2 at each level (single-error elimination). After h levels of concatenation, the effective error is c^{2^h - 1} p^{2^h}. The threshold p_c = 1/c is the critical value: below it, the doubly-exponential suppression drives the error to zero; above it, concatenation amplifies the error.
- **Stability**: The threshold theorem: if each gate in a physical implementation of a quantum network has error less than p_c, it is possible to perform encoded quantum computations with arbitrary accuracy. The paper provides explicit threshold calculations: ~10^{-6} for independent stochastic errors (p_c ~ 1/f where f ~ 10^6 is the number of minimal failure pairs in the recovery network). The stability result holds for quasi-independent stochastic and monotonic error models — substantially more general than independent errors.
- **Null hypothesis**: The unencoded, uncorrected quantum network as null. The paper explicitly frames the problem as: "the effect of noise will accumulate and ruin the entire computation, and hence the computation must be protected." The gap between encoded (error suppressed) and unencoded (error accumulates) is the value of error correction.

**What is genuinely new (not reducible to shared abstraction)**:
- The explicit construction of fault-tolerant procedures for a COMPLETE set of operations: encoded gates, state preparation, measurement, and error correction — all tolerating single faults. The paper introduces a method for obtaining fault-tolerantly encodable operations using the normalizer group and transversal gates.
- The detailed error model taxonomy: independent stochastic, quasi-independent stochastic, quasi-independent (general), and quasi-independent monotone. Each model makes different assumptions about correlations and boundedness. The threshold analysis applies to each, yielding different constants but the same qualitative result.
- The "error location" and "error expansion" framework: every noisy quantum network can be decomposed as a mixed sum of networks with linear error operators at each error location. This representation is the analytical foundation — it connects physical noise to the algebraic error model.
- The explicit counting of "minimal failure sets" to derive numerical thresholds. The recovery network for the 7-qubit code has ~190,785 operational pairs and ~415,605 total pairs that can cause failure, yielding p_c ~ 3.0 x 10^{-6}.
- The treatment of memory errors (idle qubits accumulate errors) alongside operational errors (gates introduce errors), and the explicit trade-off between parallelism and memory error accumulation.

**Connections the authors acknowledge**: Cite Shor's original fault-tolerance result, Calderbank-Shor-Steane codes, Gottesman's stabilizer formalism, and Kitaev as independent co-discoverer. Acknowledge that Aharonov and Ben-Or independently obtained threshold results. Entirely within QEC. No cross-domain connections.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Error probability p | Perturbation magnitude (parameter) |
| Threshold p_c | Critical value (phase transition) |
| Concatenation level h | Hierarchical depth (refinement scale) |
| Effective error c^{2^h-1} p^{2^h} | Doubly-exponential suppression (stability bound) |
| 7-qubit Steane code | Chain complex (Hamming-based) |
| Abstract particle A | Logical qubit (homology class) |
| Syndrome space S | Error detection space (cokernel) |
| Stabilizer observables S_1...S_6 | Boundary operators (parity checks) |
| Normalizer group | Symmetry group preserving code space |
| Error expansion | Decomposition into localized fault components |
| Error location | Localized perturbation site |
| Minimal failure set | Uncorrectable error pattern (non-trivial cycle) |
| Recovery network | Error correction circuit (projection to code space) |
| Transversal gate | Bitwise operation preserving code structure |

**See also**: `by-structure/phase_transitions.md`, `by-domain/qec.md`

---

## 2103.06309 --- Breuckmann & Eberhardt (2021)
**"Quantum Low-Density Parity-Check Codes"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: THE central organizing principle of the paper. CSS codes ARE chain complexes of length three: C_2 --partial_2--> C_1 --partial_1--> C_0, where 1-cells = physical qubits, partial_2 = H_Z (Z-stabilizer checks from faces), partial_1^T = H_X (X-stabilizer checks from vertices), and the CSS orthogonality condition H_Z H_X^T = 0 is EXACTLY partial_1 partial_2 = 0. Logical Z-operators = H_1(C) = ker(partial_1)/im(partial_2). Logical X-operators = H^1(C) = ker(partial_2^T)/im(partial_1^T). Number of logical qubits k = dim H_1. Code distance d = minimum Hamming weight of a non-trivial homology class. The paper systematically exploits this: hyperbolic codes from tessellations of hyperbolic manifolds, where k is determined by the Gauss-Bonnet-Chern theorem relating geometry to topology. Product constructions (hypergraph product, tensor product, fiber bundle, lifted product, balanced product) are ALL operations on chain complexes imported from homological algebra. The Kunneth formula gives the homology of product complexes.
- **Parameterized homology**: Multiple parameterizations. (1) Code family parameters [n, k, d]: as n grows, k and d scale according to the construction. Surface codes: k=1, d~sqrt(n). Hyperbolic surface codes: k~n, d~log(n). Fiber bundle codes: k~n^{3/5}, d~n^{3/5}. (2) The systole sys_i(M) of the underlying manifold parameterizes the distance — connecting code distance to a geometric invariant. (3) Error rate p parameterizes the decodability transition (threshold).
- **Stability**: Multiple stability results at different levels. (1) Gottesman's constant overhead theorem: LDPC codes with constant rate and sufficient error suppression enable fault-tolerant computation with only constant (not growing) overhead. This is the strongest resource-efficiency stability result. (2) Individual code thresholds: hyperbolic surface codes have thresholds under MWPM and union-find decoders; the error suppression below threshold is polynomial in n (not exponential as for concatenated codes, because d ~ log(n)). (3) The systolic geometry connection: the distance is related to the i-systole of the underlying manifold, linking code robustness to a deep geometric invariant.
- **Null hypothesis**: The surface code serves as the implicit null/baseline throughout. Every new construction is benchmarked against the surface code's parameters: k=1, d~sqrt(n), threshold ~1%. LDPC codes are judged by how far they exceed this baseline in encoding rate, distance scaling, or overhead. The "good code" question — whether quantum LDPC codes with k ~ n and d ~ n exist — is framed as the open problem of achieving what classical random LDPC codes achieve trivially.

**What is genuinely new (not reducible to shared abstraction)**:
- The taxonomy of product constructions on chain complexes IS a contribution to the Rosetta. Hypergraph product, tensor product, fiber bundle codes, lifted product, balanced product — these are all operations that take chain complexes (classical or quantum codes) and produce new chain complexes with predictable homological properties. The Kunneth formula, fiber bundle twisting, and balanced product are concrete tools for combining chain complexes across contexts.
- The systolic geometry connection: code distance = systole of the underlying manifold. The systole is the shortest non-contractible submanifold — a purely geometric quantity. This bridges QEC to Riemannian geometry in a precise, theorem-level way.
- The asymptotic gap between classical and quantum LDPC codes: random classical LDPC codes are good (k ~ n, d ~ n) but random quantum LDPC codes fail (the orthogonality constraint H_Z H_X^T = 0 cannot be satisfied randomly). This asymmetry has no classical analogue and is intrinsic to quantum mechanics.
- Gottesman's constant overhead theorem — the result that LDPC codes can reduce fault-tolerance overhead to a CONSTANT — is qualitatively different from concatenation-based thresholds (which give polylogarithmic overhead). This is a resource-efficiency result with no analogue in TDA or other domains.
- The connection to quantum gravity via holographic codes and the AdS/CFT correspondence (Section VII). Quantum LDPC codes serve as toy models for holographic quantum gravity — a bridge to fundamental physics.

**Connections the authors acknowledge**: Extensive connections to classical coding theory (Sipser-Spielman expander codes, Shannon capacity, Tanner graphs). Explicit connections to algebraic topology (homological algebra, chain complexes, Kunneth formula), differential geometry (hyperbolic manifolds, Gauss-Bonnet-Chern), systolic geometry, and even quantum gravity (holographic codes). This is one of the most cross-disciplinary papers in QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| CSS code | Chain complex of length 3 over F_2 |
| Parity check matrix H_X, H_Z | Boundary operators partial, partial^T |
| Orthogonality H_Z H_X^T = 0 | Chain complex condition (partial^2 = 0) |
| Logical operator | Non-trivial homology/cohomology class |
| Code distance d | Min-weight non-trivial cycle (systole) |
| Number of logical qubits k | dim H_1 (Betti number) |
| LDPC condition | Bounded degree (local constraint on chain complex) |
| Hypergraph/tensor product | Product of chain complexes (Kunneth) |
| Fiber bundle code | Twisted product of chain complexes |
| Systole sys_i(M) | Shortest non-contractible i-submanifold |
| Gauss-Bonnet-Chern theorem | Geometry-to-topology correspondence (k from curvature) |
| Tanner graph | Bipartite representation of chain complex |
| Surface code | Chain complex on T^2 (baseline) |
| Good code (k ~ n, d ~ n) | Optimal scaling of homological invariants |
| Constant overhead (Gottesman) | Stability with bounded resource cost |

**See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`, `by-domain/qec.md`

---

## DOI: 10.1016/0167-2789(92)90102-S --- Theiler, Eubank, Longtin, Galdrikian, Farmer (1992)
**"Testing for nonlinearity in time series: the method of surrogate data"**
Published in Physica D, vol. 58, pp. 77--94.

**Domain(s)**: Dynamical systems

**Abstract machines instantiated**:
- **Null hypothesis**: THIS is the foundational instantiation of the null machine in dynamical systems. The paper introduces a systematic framework: generate surrogate time series that satisfy a specific null hypothesis (linear stochastic process), then test whether the original data's nonlinear properties are statistically distinguishable from the surrogates. Three algorithms define three null hypotheses of increasing sophistication:
  - **Algorithm 0 (random shuffle)**: Destroys ALL temporal correlations. Preserves only the amplitude distribution (histogram). Null: the data are IID draws from a fixed distribution. This is the weakest null — rejecting it only establishes that temporal order matters at all.
  - **Algorithm 1 (phase randomization)**: Randomizes the phases of the Fourier transform while preserving the amplitudes. Preserves the power spectrum (and hence the autocorrelation function). Destroys all phase relationships between Fourier components. Null: the data are generated by a linear Gaussian process (stationary, with the observed power spectrum). Rejecting this null establishes nonlinearity in the generating process.
  - **Algorithm 2 (AAFT — Amplitude Adjusted Fourier Transform)**: Preserves BOTH the power spectrum AND the amplitude distribution of the original data. Null: the data are a static monotonic nonlinear transformation of a linear Gaussian process. This is the strongest null — rejecting it rules out the possibility that apparent nonlinearity is merely a measurement artifact (nonlinear observation function applied to linear dynamics).
  Each algorithm is a precise choice of what to destroy (phase correlations, nonlinear dynamics) and what to preserve (power spectrum, amplitude distribution). The preserved quantities define the null; the destroyed quantities are what the test is sensitive to.
- **Stability**: The properties preserved by each surrogate algorithm are stability invariants — they survive the surrogate transformation by construction. The power spectrum is invariant under Algorithm 1 (phase randomization preserves Fourier amplitudes exactly). The amplitude distribution is invariant under Algorithm 2 (the amplitude adjustment step restores the original marginal distribution). These are engineered invariances: the surrogate construction is designed so that specific statistical properties are EXACTLY preserved, making the null hypothesis precise. The robustness of the test itself is also a stability question: the rank-ordering significance test (comparing the original's test statistic to the surrogate distribution) is nonparametric and does not assume a specific distribution for the test statistic.
- **Joint-vs-marginal excess** (weak): Phase relationships between Fourier components represent joint structure — the relative timing and coherence of different frequency modes. Phase randomization (Algorithm 1) destroys this joint structure while preserving the marginal spectral properties (the power at each frequency). A significant test result means the original time series contains joint phase structure absent from the phase-randomized surrogates. This is precisely the joint-vs-marginal pattern: the marginal (power spectrum) is preserved, but the joint (phase coherence) is destroyed, and the test measures the excess.
- **Parameterized homology** (weak): The test statistic (correlation dimension, Lyapunov exponent, prediction error, or any other nonlinear measure) defines a scalar computed on both the original and each surrogate. The ensemble of surrogate values parameterizes a distribution under the null. The original's value is compared to this distribution — significance is determined by where the original falls in the null distribution's ranking. This is a parameterized family (indexed by the surrogate ensemble) where the invariant (the test statistic) is tracked to detect departure from the null.

**What is genuinely new (not reducible to shared abstraction)**:
- The METHOD itself: a principled, algorithmic framework for hypothesis testing in nonlinear dynamics. Before this paper, claims of chaos/nonlinearity in experimental data were often unfalsifiable — there was no systematic way to test whether observed nonlinear signatures were genuine or artifacts of finite data, colored noise, or nonlinear measurement functions. The surrogate data method provided the first rigorous statistical framework.
- The hierarchy of null hypotheses (Algorithm 0 < Algorithm 1 < Algorithm 2) is a taxonomy of "levels of linearity" — each successive algorithm preserves more structure, making the null harder to reject and the conclusion stronger. This graded approach to null construction has no direct analogue in other domains' null models.
- The identification that AAFT (Algorithm 2) addresses the specific pitfall of nonlinear observation functions: a linear system observed through a static nonlinearity (e.g., a diode, a saturating sensor) will appear nonlinear. Algorithm 2 accounts for this by preserving the amplitude distribution, which encodes the observation function's effect.
- The practical diagnostics: the paper demonstrates that correlation dimension and Lyapunov exponent estimates on surrogates can expose spurious claims of chaos in experimental data (sunspot numbers, measles epidemics, white noise). This had immediate impact on the field — many prior claims of low-dimensional chaos were subsequently overturned using surrogate testing.
- The connection to bootstrap and permutation testing in classical statistics, but adapted to the specific structure of time series (where temporal order is the structure being tested).

**Connections the authors acknowledge**: Cite Grassberger-Procaccia (correlation dimension), Wolf et al. (Lyapunov exponents), Takens embedding. Acknowledge the connection to classical hypothesis testing and bootstrap methods (Efron). No connections to TDA, QEC, or information theory — the paper is situated entirely within nonlinear dynamics / time series analysis.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Surrogate time series | Null realization (sample from the null distribution) |
| Algorithm 0 (random shuffle) | Strongest structure destruction (destroys all temporal order) |
| Algorithm 1 (phase randomization) | Selective structure destruction (destroys phase, preserves spectrum) |
| Algorithm 2 (AAFT) | Minimal structure destruction (preserves spectrum + amplitude distribution) |
| Power spectrum preservation | Stability invariant of the surrogate transformation |
| Amplitude distribution preservation | Stability invariant (marginal) |
| Phase relationships | Joint structure (between Fourier components) |
| Test statistic (correlation dimension, etc.) | Diagnostic scalar (compared across null ensemble) |
| Rank-ordering significance | Nonparametric p-value from surrogate ensemble |
| Null hypothesis: linear stochastic process | The reference model (what surrogates instantiate) |
| Nonlinear observation function | Static monotonic transformation (Algorithm 2 accounts for this) |
| Rejection of null | Evidence for genuine nonlinear dynamics |

---

## 2209.13581 --- Berry, Su, Gyurik, King, Basso, Del Toro Barba, Rajput, Wiebe, Dunjko, Babbush (2023)
**"Analyzing Prospects for Quantum Advantage in Topological Data Analysis"**
PRX Quantum 4, 040349 (2023)

**Domain(s)**: TDA, QEC (quantum algorithms)

**Abstract machines instantiated**:
- **Chain complex**: The paper works directly with the simplicial chain complex of the clique complex of a graph G. The boundary operator dG_k maps k-simplices to (k-1)-simplices. The combinatorial Laplacian Delta^G_{k-1} = dG^{dagger}_{k-1} dG_{k-1} + dG_k dG^{dagger}_k is the central object. The Betti number beta_{k-1} = dim(ker(Delta^G_{k-1})) is the quantity to be estimated. The Dirac operator BG = dG + dG^{dagger} is constructed; BG^2 is block-diagonal with the combinatorial Laplacian in the middle block. The quantum algorithm projects onto ker(BG) restricted to the k-chain subspace H^G_k. This is the chain complex in its purest computational form: boundary operators, their adjoints, and the kernel/image structure ARE the computation.
- **Parameterized homology**: TWO distinct parameterizations. (1) The standard TDA filtration: the distance scale epsilon determines which simplices exist in the clique complex, and Betti numbers are tracked as epsilon varies (persistent homology). The paper explicitly discusses this as the motivating application. (2) The dimension k itself is a parameter: the complexity of computing beta_k grows exponentially in k classically (the number of k-cliques can be C(n,k)), but the quantum algorithm's complexity is polynomial in k. The quantum advantage IS the ability to probe high-dimensional homology efficiently.
- **Matching**: The dequantization argument uses a random walk on k-simplices (a Markov chain whose stationary distribution is uniform over k-cliques). The mixing time of this walk is governed by the spectral gap gamma_M of the transition matrix. This spectral approach to sampling k-simplices is structurally related to matching: the random walk must find and connect cliques, which is an assignment problem between vertices. The MWPM decoder in QEC syndrome matching has a structural parallel here: both solve assignment problems on combinatorial structures derived from chain complexes.
- **Stability**: The paper establishes that quantum advantage is robust only under specific parameter regimes: (1) the Betti number must grow asymptotically for super-quadratic speedup, (2) exponentially large dimension AND Betti number are necessary but insufficient for super-polynomial advantage. The dequantization result is itself a stability analysis: it asks how robust the quantum advantage is to the existence of classical competitors. The answer is that advantage is fragile --- it requires very specific parameter regimes (large beta_k, large spectral gap lambda_min, specific graph families). This is a meta-stability result: the computational advantage is not topologically robust; it depends sensitively on problem parameters.
- **Null hypothesis**: The dequantization serves as the null. The classical random-walk algorithm (Monte Carlo sampling of k-simplices) is the "structureless" baseline. The quantum advantage is measured as the gap between quantum and classical complexity. The paper shows this gap can be superpolynomial for specifically constructed graph families (dense random graphs with parameters tuned for large Betti numbers) but may collapse for generic instances. The naive classical algorithm (enumerate all k-cliques, compute nullity) with complexity O(C(n,k)) is the strongest null; the Monte Carlo dequantization is a weaker null that narrows the advantage.

**What is genuinely new (not reducible to shared abstraction)**:
- The paper is the first to compile a quantum TDA algorithm to a fault-tolerant gate set with explicit constant factors. The Toffoli complexity (tens of billions of Toffolis for classically intractable instances) places quantum TDA in the resource landscape between quantum chemistry and Shor's algorithm. This resource estimation has no analogue in the abstract machine framework.
- The dequantization result (classical Monte Carlo algorithm for Betti number estimation) is genuinely new: it shows that the quantum advantage for TDA is NOT simply a consequence of the exponential size of the chain complex. The mixing time of the classical random walk (governed by the spectral gap of the transition matrix on k-simplices) is the key quantity that determines whether classical algorithms can compete. This creates a nuanced landscape: quantum advantage exists in a narrow regime where the chain complex is large but the classical random walk mixes slowly.
- The specific graph families constructed for super-polynomial advantage (dense random graphs with parameters n, k ~ n/2, degree ~ n/2) are novel mathematical objects. They demonstrate that the regime of quantum advantage is non-empty but highly constrained.
- Kaiser-window amplitude estimation, Chebyshev polynomial eigenvalue projectors, and Dicke state preparation via inequality testing are algorithmic innovations specific to quantum computing with no classical or topological analogue.
- The key insight that super-quadratic speedup requires MULTIPLICATIVE error estimation (relative error in beta_k) rather than additive error in the normalized Betti number. This distinction between error types is a computational refinement absent from the abstract stability concept.

**Connections the authors acknowledge**: Explicitly connect quantum algorithms (QEC/quantum computing) to TDA (simplicial homology, Betti numbers, persistent homology). This is a DIRECT TDA-QEC bridge paper: the quantum algorithm computes TDA invariants. The authors cite Lloyd et al.'s original quantum TDA algorithm, Gyurik et al.'s DQC1-hardness results, and the dequantization literature. They acknowledge that the chain complex structure is shared between TDA and the quantum algorithm. They do NOT connect to dynamical systems, neuroscience, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Clique complex of graph G | Simplicial complex (the space) |
| Boundary operator dG_k | Boundary operator ∂ |
| Combinatorial Laplacian Delta^G_{k-1} | Hodge Laplacian L_k (up/down components) |
| Dirac operator BG = dG + dG^{dagger} | ∂ + ∂^{dagger} (Dirac = boundary + coboundary) |
| Betti number beta_k | dim(ker(L_k)) = k-th homological feature count |
| Kernel projector | Projection onto harmonic space (homology representatives) |
| Distance scale epsilon | Filtration parameter |
| Persistent homology | Parameterized homology (tracking beta_k(epsilon)) |
| Dequantization | Classical null algorithm (Monte Carlo on k-simplices) |
| Spectral gap lambda_min | Gap of combinatorial Laplacian (separation of harmonic from non-harmonic) |
| Toffoli complexity | Computational resource (fault-tolerant gate count) |
| Multiplicative error in beta_k | Relative perturbation size (stability metric) |
| Dense random graph family | Specific problem instance in the advantage regime |
| Quantum walk operator | Block encoding of Dirac/boundary operator |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `cross_domain_bridges.md`

---

## 2107.02194 --- Hastings, Haah (2021)
**"Dynamically Generated Logical Qubits"**
arXiv: 2107.02194

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: The honeycomb code is defined on a hexagonal lattice with qubits on vertices and two-qubit Pauli checks on edges. When viewed as a subsystem code, the product of checks along any 1-cycle on the lattice is a stabilizer. Plaquette stabilizers correspond to homologically trivial cycles (boundaries); logical operators correspond to homologically non-trivial cycles on the torus (H_1(T^2, Z/2)). The stabilizer group has dimension n_p + 1, the gauge group 3n_p - 1, leaving n_p - 1 gauge qubits and ZERO logical qubits as a static subsystem code. The chain complex is the standard cellular chain complex of the honeycomb lattice: 0-cells (vertices/qubits), 1-cells (edges/checks), 2-cells (hexagonal plaquettes/stabilizers). The boundary operator maps edges to their endpoint vertices; the stabilizer condition (product of checks on a boundary = identity) is exactly del^2 = 0.
- **Parameterized homology**: THE key machine. Time (measurement round r) parameterizes the code. The instantaneous stabilizer group (ISG) S(r) changes with each measurement round in a period-3 cycle (r mod 3 determines which edge type is measured). But the DYNAMICS of logical operators has period 6: after one period of 3 rounds, every electric logical operator maps to a parallel magnetic operator and vice versa; after 6 rounds, they return to themselves. The ISG at each time step defines a different instantaneous code, but the logical information is encoded in the ORBIT of the ISG under the periodic measurement schedule --- not in any single snapshot. This is deeply analogous to Floquet theory in dynamical systems: the stroboscopic map (ISG after one full period) defines the "Floquet multipliers" of the code, and the logical qubits live in the persistent eigenspace of this map. The period-6 dynamics of logical operators (electric <-> magnetic automorphism with period 6 despite period-3 measurements) is a non-trivial monodromy: the codespace does not return to itself after one measurement period, only after two.
- **Stability**: Error correction is possible despite the time-varying code. The syndrome bits (eigenvalues of plaquette stabilizers) form a lattice in 2+1 dimensional spacetime with basis vectors s_1, s_2, s_3 that span a structure isomorphic to a simple cubic lattice (after bipartition into two congruent sublattices). Standard MWPM decoding on this spacetime lattice achieves fault tolerance: below a threshold error rate, logical errors are exponentially suppressed with system size. The stability result is that the dynamical code protects information as well as the static toric code despite never having a fixed codespace. Each individual measurement round has no protection (the subsystem code has zero logical qubits); protection emerges only from the SEQUENCE.
- **Null hypothesis**: The static subsystem code (ignoring measurement order) serves as the null. This null has zero logical qubits --- no information protection at all. The Floquet structure (specific periodic measurement schedule) is the structure that must be added to create protection. The gap between null (0 logical qubits) and Floquet code (2 logical qubits with distance proportional to linear system size) is maximal: the dynamical structure creates protection from nothing. A secondary null is the static toric code: it protects the same 2 logical qubits but requires 4-qubit measurements. The honeycomb Floquet code achieves the same protection with only 2-qubit measurements, at the cost of requiring a specific temporal schedule.
- **Matching**: The fault-tolerant decoder uses MWPM on the spacetime syndrome lattice. Syndrome defects (violations of plaquette stabilizer eigenvalues between consecutive rounds) are matched in the 2+1D spacetime lattice. The matching cost is the spacetime distance between defects. This is the standard QEC matching machine, but lifted to spacetime: the matching is not just spatial (as in static toric code decoding) but spatiotemporal (defects at different times and locations are matched).

**What is genuinely new (not reducible to shared abstraction)**:
- The concept of DYNAMICALLY GENERATED logical qubits: a code that has zero logical qubits as a static object but generates protected logical qubits through a specific periodic measurement schedule. This is fundamentally new --- there is no TDA analogue where a simplicial complex has trivial homology but gains non-trivial homology through a specific sequence of operations. The closest analogue would be a time-varying filtration where the complex at each time step is contractible but the periodic orbit of complexes has non-trivial topology. This does not exist in standard TDA.
- The period-6 automorphism of logical operators (electric <-> magnetic exchange): after 3 measurement rounds, the ISG returns (up to signs) but logical operators undergo a non-trivial permutation. This 6/3 period ratio is a form of monodromy --- the logical information picks up a phase (here, an operator permutation) when transported around one period of the driving schedule. This is structurally identical to Berry phase / holonomy in quantum mechanics or monodromy in dynamical systems, but applied to the codespace itself.
- The Majorana fermion perspective: the honeycomb code maps (via Jordan-Wigner) to free Majorana fermions on a honeycomb lattice, with the gauge field structure of Kitaev's honeycomb model. The inner logical operators transport FERMIONS (their commutation relations show fermionic statistics), while outer logical operators transport BOSONS (e and m anyons). This anyon content is a domain-specific structure with no analogue in TDA or information theory.
- The measurement-only quantum computation aspect: no unitary gates are applied; all dynamics come from 2-qubit Pauli measurements. The logical information is maintained purely by the pattern of measurements. This is a new computational paradigm with no classical analogue.
- The spacetime syndrome lattice structure: syndrome bits in 2+1D spacetime form a lattice spanned by vectors that, after bipartition, give two copies of the simple cubic lattice. This specific geometric structure is engineered for MWPM decoding efficiency.

**Connections the authors acknowledge**: Cite Kitaev's toric code (the static QEC chain complex they generalize), the subsystem code framework (Poulin, Bacon-Shor, Bombin-Martin-Delgado color codes), and Kitaev's honeycomb model (the condensed matter Hamiltonian whose measurement-based analogue they construct). Situated entirely within QEC. No connections to TDA, dynamical systems, or information theory. The Floquet analogy (periodic driving) is implicit but not acknowledged --- the authors do not use the term "Floquet" in the original paper (the name was given by the community).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Honeycomb lattice | The space (cellulation) |
| Two-qubit Pauli check | Local constraint (edge measurement) |
| Gauge group | Full group generated by local constraints |
| Stabilizer group | Center of gauge group (global constraints = boundaries) |
| Instantaneous stabilizer group S(r) | Snapshot of the chain complex at time r |
| Measurement round r mod 3 | Parameterization variable (discrete time) |
| Period-3 ISG cycle | Periodic orbit of the code complex |
| Period-6 logical operator dynamics | Monodromy of the parameterized family |
| Logical qubit (dynamically generated) | Homology class (emergent from periodic orbit, not from any snapshot) |
| Plaquette stabilizer | Boundary (product of checks on contractible cycle = identity) |
| Non-trivial cycle on torus | Non-trivial homology class (logical operator) |
| Syndrome bit | Cycle violation (departure from del^2 = 0) |
| Spacetime syndrome lattice | 2+1D chain complex for decoding |
| MWPM decoder | Optimal matching on syndrome defects |
| Electric/magnetic logical operators | Dual homology classes (H_1 vs cohomology) |
| Fermion (inner logical operator) | Odd element under exchange (fermionic statistics) |
| Code distance ~ L | Minimum-weight non-trivial cycle (robustness scale) |
| Zero static logical qubits | Trivial static homology (null) |
| Two dynamical logical qubits | Non-trivial dynamical homology (Floquet-generated) |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-domain/qec.md`

**See also**: `by-structure/phase_transitions.md`, `by-domain/dynamical_systems.md`

---

## 1909.02297 --- Mediano, Rosas, Carhart-Harris, Seth, Barrett (2019)
**"Beyond integrated information: A taxonomy of information dynamics phenomena"**

**Domain(s)**: neuroscience, information theory

**Abstract machines instantiated**:
- **Chain complex**: The double-redundancy lattice is a product lattice A x A with 16 nodes, ordered by the PID partial order on source/target subsets. The Moebius inversion on this lattice defines the 16 PhiID atoms, exactly as PID uses Moebius inversion on the single redundancy lattice. The lattice is the algebraic scaffold; the atoms are the "homology" of the information structure.
- **Parameterized homology**: The PhiID atoms can be computed for different time lags, system sizes, noise levels, or redundancy function choices. The paper shows that existing integration measures (Phi_WMS, psi, Phi_G, CD) are different projections of the same 16-atom lattice --- they are different "slices" of a parameterized family, analogous to how different filtration thresholds reveal different persistent features.
- **Joint-vs-marginal excess**: THE central object. PhiID decomposes the excess entropy E = I(X1,X2; Y1,Y2) into 16 atoms that distinguish HOW joint information exceeds marginal information. Synergistic atoms (those involving {12} in source or target) are the information present in the composite system but absent from any component. The paper's key insight: what IIT calls "integration" is actually an aggregate of synergy, transfer, storage, copy, erasure, upward causation, and downward causation --- all distinct modes of joint-vs-marginal excess.
- **Null hypothesis**: Independent subsystems (Phi = 0) is the explicit null. The partitioned system where X1,X2 evolve independently is the baseline against which all 16 atoms are measured. The paper also constructs specific null systems (copy-transfer, downward-XOR, parity-preserving-random) that each have Phi_WMS = 1 but with different non-zero atoms --- showing the null model is insufficient to distinguish qualitatively different integration modes.
- **Stability**: The corrected Phi_WMS,c (which adds back the double-redundancy term to avoid negativity) is more robust across noise correlation levels than the standard Phi_WMS. The paper demonstrates that Phi_WMS goes negative in highly redundant systems, while the corrected version tends to 0 --- a stability improvement.

**What is genuinely new (not reducible to shared abstraction)**:
- The 6-category taxonomy of information dynamics (storage, copy, transfer, erasure, downward causation, upward causation) is genuinely new. These are not just different names for joint-vs-marginal excess --- they are structurally distinct modes of how information moves through a multivariate process across time. No other Rosetta domain has this fine-grained temporal decomposition.
- Upward causation (individual past states determining collective future) and downward causation (collective past determining individual futures) are formally distinguished for the first time. These are directional modes of joint-vs-marginal excess that have no direct analogue in TDA, QEC, or standard dynamical systems.
- The demonstration that Phi_WMS, psi, Phi_G, and CD each capture different subsets of the 16 PhiID atoms (Table I) is a meta-result about integration measures themselves, not about any specific system.
- Synergistic storage I_partial({12}->{12}) --- information that is jointly encoded in both past variables and jointly decodable only from both future variables --- had not been reported before this paper.

**Connections the authors acknowledge**: The paper explicitly bridges IIT (Tononi) and PID (Williams & Beer), unifying them into PhiID. They cite Lizier's "information modification" as a precursor to their 6-category taxonomy. They note connections to Granger causality and causal density but do not acknowledge parallels to TDA, QEC, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Excess entropy E | Joint-vs-marginal excess (total) |
| PhiID atom | Information atom (decomposed excess) |
| Double-redundancy lattice | Chain complex (product lattice with Moebius inversion) |
| Redundancy function Red(.) | Overlap measure (common information in components) |
| Synergy Syn(X1,X2; Y1Y2) | Joint-vs-marginal excess (synergistic component) |
| Integrated information Phi | Scalar summary of joint-vs-marginal excess |
| Partitioned system (Phi=0) | Null hypothesis (independent subsystems) |
| Upward causation | Individual-to-collective information flow |
| Downward causation | Collective-to-individual information flow |
| Information storage | Self-predictive information (same variable, past to future) |
| Transfer entropy | Directed information flow (unique cross-variable prediction) |

**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`, `by-domain/information_theory.md`

---

## 1411.2832 --- Barrett (2015)
**"Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems"**

**Domain(s)**: information theory, neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The entire paper is about decomposing I(X; Y, Z) into redundancy R, unique information U, and synergy S --- and synergy IS the joint-vs-marginal excess: S(X; Y, Z) = information about X present in (Y,Z) jointly that is absent from Y alone and Z alone. The key result: for Gaussian systems with univariate target, a broad class of PIDs all reduce to the MMI (Minimum Mutual Information) PID where R = min{I(X;Y), I(X;Z)}, making synergy = extra information from the weaker source given the stronger. The paper's WMS = I(X;Y,Z) - I(X;Y) - I(X;Z) = S - R is the net joint-vs-marginal excess.
- **Parameterized homology**: The paper systematically varies three parameters: (i) correlation coefficients a, b, c between the three Gaussian variables; (ii) time lag (1-lag vs infinite-lag pasts in dynamical systems); (iii) connection strengths alpha, gamma, rho in MVAR models. For each parameter setting, the PID atoms change, creating a parameterized family. The key finding: net synergy at 1-lag is always >= net synergy at infinite lag for order-1 MVAR systems (Eq. 96), because restricted regressions on infinite pasts reduce apparent synergy.
- **Null hypothesis**: The product of marginals (Y independent of Z) is the baseline null. The paper shows the surprising result that net synergy can be positive even when the two sources are uncorrelated (b=0), violating the naive intuition that synergy requires source correlation. The "information as variance reduction" alternative (WMS_Sigma) gives zero synergy when sources are uncorrelated, highlighting that the nonlinearity of the log in Shannon information creates synergy absent from the linear (variance) measure.
- **Stability**: The MMI PID has a remarkable stability property: redundancy R_MMI = min{I(X;Y), I(X;Z)} is completely independent of the correlation between sources. Only synergy depends on the full joint distribution. This factorization is a robustness result --- redundancy is stable under perturbations to the source-source relationship. The paper also shows that synergy is a monotonically increasing function of the weaker connection strength and monotonically decreasing with source correlation (Eq. 110), giving predictable perturbation behavior.

**What is genuinely new (not reducible to shared abstraction)**:
- The proof that ALL PIDs satisfying the marginal-dependence property collapse to MMI for Gaussian systems with univariate target is a universality result specific to the Gaussian structure. This has no analogue in TDA or QEC --- it says the information-theoretic decomposition is uniquely determined by the domain's distributional assumptions.
- The distinction between Shannon information (log of variance ratio) and variance-based information (I_Sigma = variance difference) reveals that synergy in Gaussian systems is partly an artifact of the logarithm's concavity. WMS_Sigma = 0 when sources are uncorrelated, but WMS > 0. This is a genuinely domain-specific insight about how the choice of information measure affects the decomposition.
- The infinite-lag vs 1-lag comparison (synergy decreases with more history) is a temporal effect with no direct TDA or QEC analogue. It arises because restricted regressions on longer histories capture more variance, reducing the apparent excess from knowing both sources.
- The proposed "synergistic complexity" measure SC (Eq. 134) as an alternative to causal density and Phi is new, measuring the average excess synergy in a system of n variables.

**Connections the authors acknowledge**: Explicitly discusses implications for neuroscience (neural coding, EEG connectivity, epilepsy, consciousness). Cites Granger causality literature and its equivalence to transfer entropy for Gaussians. Notes that net synergy has been observed in intracranial EEG during epileptic seizures and in information transfer between neural variables. Does NOT cite TDA, QEC, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Synergy S(X; Y, Z) | Joint-vs-marginal excess (synergistic atom) |
| Redundancy R(X; Y, Z) | Common information in components |
| Whole-Minus-Sum WMS | Net joint-vs-marginal excess (synergy minus redundancy) |
| MMI PID (Minimum Mutual Information) | Canonical decomposition for Gaussian composites |
| Partial covariance Sigma(X|Y) | Conditional structure (residual after marginal removed) |
| Net synergy | Excess of joint over sum of marginals |
| Transfer entropy | Directed joint-vs-marginal excess |
| Causal density | Average pairwise transfer (double-counts synergy) |
| Synergistic complexity SC | Average joint-vs-marginal excess per triplet |
| Granger causality F | Variance-ratio directed information flow |

**See also**: `by-structure/composite_systems.md`, `by-domain/information_theory.md`, `by-domain/neuroscience.md`

---

## Wave 5 — Match x Neuro (2026-04-06)

Papers filling the weakest cell in the 6x5 coverage matrix: Matching machine instantiated in Neuroscience. All three use optimal transport as the core algorithmic mechanism applied to neural data.

---

## 2206.09398 --- Thual, Tran, Zemskova, Courty, Flamary, Dehaene, Thirion (2022)
**"Aligning individual brains with Fused Unbalanced Gromov-Wasserstein"**

**Domain(s)**: Neuroscience (neuroimaging, fMRI), TDA (optimal transport)

**Abstract machines instantiated**:
- **Matching**: The central contribution. FUGW computes an optimal transport plan P in R^{n x p} between cortical vertices of two subjects. The plan is a soft assignment matrix that matches vertices across brains. The loss has three terms: (1) Wasserstein loss L_W(P) matching vertices with similar functional features, (2) Gromov-Wasserstein loss L_GW(P) penalizing changes in pairwise geodesic distance structure (second-order matching), and (3) unbalanced KL marginal relaxation allowing functional areas to differ in size across subjects. The parameter alpha interpolates between feature-based and geometry-based matching. This is a genuine optimal assignment problem: minimize total cost of transporting mass from source cortical surface to target cortical surface, subject to structural constraints.
- **Stability**: The unbalanced feature (parameter rho) provides robustness: areas where signal or geometry differ too much between subjects simply transport less mass rather than forcing a bad match. The method is shown to be robust to noise and inter-individual anatomical variability. Alignment quality degrades gracefully as brain differences increase.
- **Parameterized homology**: The parameter alpha traces a family of alignments from pure feature matching (alpha=0) to pure geometry preservation (alpha=1). The optimal alpha (selected on validation data) reveals the relative importance of functional vs anatomical structure. The training set size (number of fMRI contrasts) also parameterizes alignment quality.
- **Null hypothesis**: Baseline alignment via FreeSurfer anatomical co-registration (fsaverage5) serves as the null. FUGW alignment significantly increases between-subject correlation of held-out functional data compared to this anatomical-only baseline. MSM (multimodal surface matching) serves as the primary competing method.

**What is genuinely new (not reducible to shared abstraction)**:
- The fusion of Wasserstein and Gromov-Wasserstein in a single objective is domain-specific: it encodes the neuroscience insight that functional alignment should respect cortical geometry (nearby cortical areas should map to nearby areas). This is not just OT; it is OT constrained by the Riemannian geometry of the cortical sheet.
- Unbalanced transport handles the biological fact that homologous functional areas differ in size across individuals. This is a neuroscience-specific constraint absent from standard OT in TDA or QEC.
- The method is landmark-free and whole-brain, unlike hyperalignment (Haxby) which requires ROI selection or stimulus-driven alignment. FUGW discovers the alignment from data geometry alone.
- Applied to the Individual Brain Charting dataset (12 subjects, 400 fMRI maps each), demonstrating that OT-based alignment captures fine-grained functional organization invisible to anatomy-based methods.

**Connections the authors acknowledge**: Cite Haxby hyperalignment and Procrustes-based methods as predecessors but note they require stimulus labels (supervised). Cite Gromov-Wasserstein literature (Memoli, Peyre, Vayer) for the mathematical framework. Do NOT cite TDA/PH literature --- the connection to persistence diagram matching is implicit but unacknowledged.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transport plan P | Optimal assignment / matching |
| Wasserstein loss L_W | Feature-based matching cost |
| Gromov-Wasserstein loss L_GW | Second-order (structure-preserving) matching cost |
| Fused loss (alpha) | Parameterized family of matchings |
| Unbalanced (rho) | Robustness / partial transport |
| Marginal relaxation (KL) | Soft constraint on matching completeness |
| Sinkhorn iterations | Matching algorithm (entropic regularization) |
| Cortical vertex | Feature point |
| Functional signature | Feature vector |
| Geodesic distance matrix D | Cost matrix |
| FreeSurfer baseline | Null model (anatomy-only alignment) |

**See also**: `by-structure/optimal_transport.md`, `by-domain/neuroscience.md`

---

## 1902.04812 --- Janati, Bazeille, Thirion, Cuturi, Gramfort (2019)
**"Group level MEG/EEG source imaging via optimal transport: minimum Wasserstein estimates"**

**Domain(s)**: Neuroscience (MEG/EEG source imaging), TDA (optimal transport)

**Abstract machines instantiated**:
- **Matching**: The core innovation. Minimum Wasserstein Estimates (MWE) define a multi-task regression penalty Omega using unbalanced optimal transport. For S subjects, the penalty is: Omega = mu * min_{x-bar} sum_s W(x^(s), x-bar) + lambda * ||x^(s)||_1, where W is the unbalanced Wasserstein distance on the cortical source space and x-bar is the Wasserstein barycenter. The cost matrix M_ij is the geodesic distance between cortical vertices i and j. The transport plan matches source activations across subjects: it finds the minimum-cost assignment of neural current dipoles from each subject to a common "average" source pattern, where cost respects cortical geometry. This is OT-as-regularizer: the matching constrains the inverse problem to prefer solutions where different subjects' sources are nearby on the cortex.
- **Stability**: MWE infers per-subject noise standard deviation sigma^(s) jointly with sources. This makes the method robust to varying signal-to-noise ratios across subjects --- a practical stability guarantee. The unbalanced formulation (KL marginal relaxation with parameter gamma) prevents forcing mass transport when source amplitudes differ. Reduces localization error from ~4 cm (Lasso) to <1 cm.
- **Null hypothesis**: Independent Lasso (L1 regularization per subject, no cross-subject coupling) serves as the baseline. Group Lasso (L21 norm forcing identical source locations) is the rigid null. MWE outperforms both, demonstrating that OT-based spatial proximity is the right prior --- neither independence nor identity.
- **Parameterized homology**: The number of subjects S parameterizes the estimation quality. As S increases from 2 to 16, MWE's AUC rises from ~0.6 to ~0.9 --- more subjects make the inverse problem better-posed. The regularization parameters (mu, lambda, gamma, epsilon) also define a multi-dimensional parameter space over which alignment quality varies.

**What is genuinely new (not reducible to shared abstraction)**:
- OT as a regularizer for an ill-posed inverse problem (MEG/EEG source imaging). This is not just computing OT distance between distributions; it is embedding OT inside a regression objective to constrain the solution space. The matching is between latent (unobserved) neural sources, not between observed signals.
- The Wasserstein barycenter x-bar emerges as a group-level neural source estimate --- an "average brain activation" that respects cortical geometry. This is the Frechet mean in Wasserstein space, a concept from OT theory applied to neural source localization.
- Concomitant noise estimation (sigma^(s) per subject) extends MTW to handle heterogeneous noise --- a practical neuroscience requirement absent from abstract OT.
- Validated on the Wakeman-Henson face perception dataset: MWE localizes sources in the fusiform face area consistent with fMRI ground truth, closing the gap between MEG temporal resolution and fMRI spatial resolution.
- Generalized Sinkhorn algorithm for unbalanced transport enables efficient computation on cortical meshes (~2500 sources per hemisphere).

**Connections the authors acknowledge**: Cite Kantorovich OT, Cuturi (Sinkhorn distances), Chizat et al. (unbalanced OT). Cite fMRI multi-subject methods (Varoquaux, Kozunov). Do NOT cite TDA or persistence diagrams --- the connection to Wasserstein distance on PDs is implicit.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transport plan P | Optimal assignment / matching |
| Unbalanced Wasserstein distance W | Matching cost with mass relaxation |
| Wasserstein barycenter x-bar | Frechet mean of matched features |
| Cost matrix M (geodesic) | Pairwise cost for matching |
| Generalized Sinkhorn | Matching algorithm (entropic, unbalanced) |
| Left marginal m = P*1 | Transported mass per source |
| Source space | Feature space (cortical vertices) |
| Leadfield matrix L | Forward model (linear constraint) |
| Current dipole amplitude x | Feature value to be matched |
| L1 penalty (lambda) | Sparsity (focal sources) |
| Noise variance sigma^(s) | Per-subject robustness parameter |
| MCE (minimum current estimates) | Independent matching baseline (null) |
| Group Lasso (L21) | Rigid matching (forced identity, null) |
| Earth mover distance (EMD) | Wasserstein-1 evaluation metric |

**See also**: `by-structure/optimal_transport.md`, `by-domain/neuroscience.md`

---

## 1906.11768 --- Lee, Dabagia, Dyer, Rozell (2019)
**"Hierarchical Optimal Transport for Multimodal Distribution Alignment"**

**Domain(s)**: Neuroscience (neural decoding, motor cortex), TDA (optimal transport)

**Abstract machines instantiated**:
- **Matching**: The central contribution. Hierarchical OT (HOT) formulates cross-domain alignment as a two-level optimal transport problem. Level 1: match clusters across domains (coarse assignment). Level 2: match individual data points within matched clusters (fine-grained assignment). The Wasserstein distance serves as the divergence measure at both levels. Applied to neural decoding: align neural population activity from macaque primary motor cortex (M1) across different recording sessions/conditions, then decode movement directions and velocities from the aligned representations. The transport plan maps neural firing patterns from one session to another, enabling cross-session generalization.
- **Stability**: Performance guarantees describe when cluster correspondences can be recovered under the hierarchical formulation. The method is robust to noise, ambiguity, and multimodality in the data distributions --- precisely the conditions encountered in neural recordings where trial-to-trial variability is high. The hierarchical structure provides stability: even if fine-grained matching fails, the coarse cluster assignment can still be correct.
- **Parameterized homology**: The hierarchy itself is a parameterization: as the number of clusters varies, the alignment transitions from fully global (one cluster = standard OT) to fully local (each point is its own cluster). The entropic regularization parameter epsilon also controls the softness of the assignment.
- **Null hypothesis**: Standard (flat) optimal transport alignment serves as the baseline null. The hierarchical formulation outperforms flat OT when data has clustered structure (as neural population activity does, with clusters corresponding to movement directions). Vanilla averaging of unaligned representations is the weakest null.

**What is genuinely new (not reducible to shared abstraction)**:
- Two-level hierarchy in OT is a structural innovation: it exploits the fact that neural population activity has meaningful clustered structure (corresponding to discrete movement directions). Standard OT treats all points equally; HOT respects the categorical structure of the neural code.
- Application to cross-session neural decoding in macaque M1 is a genuinely new use case: align neural population vectors recorded on different days/conditions so that a decoder trained on one session works on another. This is "domain adaptation" for neural data via OT.
- Distributed ADMM algorithm with Sinkhorn distance provides computational efficiency scaling quadratically with the largest cluster rather than the full dataset --- important for real-time neural decoding.
- Worst-case geometry analysis: the paper characterizes dataset geometries where hierarchical alignment fails, providing a negative result about the limits of OT-based neural alignment.
- Unitary transformation model between sessions: when the cross-session mapping is approximately orthogonal (rotation of neural population geometry), HOT provably recovers the correct alignment.

**Connections the authors acknowledge**: Cite OT literature (Villani, Cuturi, Peyre). Cite neural decoding/BCI literature (Churchland, Shenoy). Do NOT cite TDA, persistence diagrams, or hyperalignment explicitly --- the work bridges OT theory and systems neuroscience without referencing the broader Rosetta.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transport plan | Optimal assignment / matching |
| Wasserstein distance | Matching cost |
| Hierarchical OT | Two-level matching (coarse + fine) |
| Cluster correspondence | Coarse-level matching |
| Within-cluster alignment | Fine-level matching |
| Sinkhorn distance | Entropically regularized matching cost |
| ADMM solver | Matching algorithm (distributed) |
| Neural population vector | Feature vector |
| Movement direction cluster | Category in feature space |
| Cross-session alignment | Domain adaptation via matching |
| Unitary transformation | Structure-preserving map between feature spaces |

**See also**: `by-structure/optimal_transport.md`, `by-domain/neuroscience.md`

---

## Wave 6 — Directed Information Flow in Neural Oscillations and Spike Trains (2026-04-07)

### DOI: 10.1016/j.neuroimage.2013.08.056 --- Lobier, Siebenhuhner, Palva, Palva (2014)
**"Phase transfer entropy: A novel phase-based measure for directed connectivity in networks coupled by oscillatory interactions"**

**Domain(s)**: Neuroscience, information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Phase TE quantifies directed phase coupling between oscillatory neural signals. The measure computes TE on phase time series extracted via Morlet filtering, detecting directed information flow from source to target that exceeds what the target's own phase history can predict. Differential TE (dTE = TE(1->2) - TE(2->1)) isolates the net directional excess. This is joint-vs-marginal at two levels: (1) the TE itself measures how the joint (source + target) history exceeds the marginal (target-only) history for prediction, and (2) the phase extraction step takes the joint amplitude-phase signal and projects to the phase marginal, discarding amplitude to isolate oscillatory coupling.
- **Null hypothesis**: Surrogate data constructs the null distribution. The paper validates that surrogate-based null-hypothesis testing correctly identifies statistical significance of directed phase coupling. Crucially, the surrogates must destroy phase relationships while preserving spectral properties --- the same destroy-structure/preserve-statistics pattern as Theiler surrogates. Phase TE yields no false positives under mixing and noise when tested against surrogate nulls.
- **Parameterized homology**: Frequency band serves as the filtration parameter. The paper demonstrates frequency-band-specific directed connectivity: different oscillatory frequency bands (e.g., alpha, beta, gamma) yield different directed coupling patterns. The coupling strength and direction can reverse across bands. This is a discrete parameterized family of directed graphs indexed by frequency, analogous to a filtration where each frequency band reveals a different connectivity topology.

**What is genuinely new (not reducible to shared abstraction)**:
- Phase extraction as a preprocessing step before TE is domain-specific to oscillatory neural systems. The Hilbert/Morlet phase time series is a circular (S^1-valued) variable, not a real-valued one. Standard TE estimators on real-valued signals conflate amplitude and phase contributions; Phase TE isolates the phase component. This circular-variable structure has no direct analogue in standard TDA or QEC chain complexes.
- Robustness to linear mixing (volume conduction) is a uniquely neuroimaging concern. MEG/EEG signals are linear superpositions of sources, creating spurious correlations. Phase TE's demonstrated robustness to mixing is a domain-specific stability property absent from information-theoretic TE in other contexts.
- Computational efficiency: Phase TE is "considerably more efficient computationally" than real-valued TE because phase time series have lower dimensionality than the original signals. This practical advantage is specific to the oscillatory-neural-data use case.
- Bidirectional frequency-band-specific interaction patterns that confound real-valued TE are "accurately untangled" by Phase TE. The ability to resolve per-band directionality is a capability absent from broadband TE.

**Connections the authors acknowledge**: Cite Schreiber (2000) transfer entropy, Granger causality, Dynamic Causal Modeling. Situated in the MEG/EEG effective connectivity literature. Do NOT cite TDA, persistent homology, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Phase transfer entropy | Joint-vs-marginal excess (directed, on phase time series) |
| Differential TE (dTE) | Net directed excess (asymmetric joint-vs-marginal) |
| Surrogate data | Null hypothesis distribution (structure-destroying) |
| Frequency band | Parameter in parameterized family |
| Coupling strength | Excess magnitude |
| Linear mixing / volume conduction | Perturbation (domain-specific noise model) |
| Neural Mass Model | Generative model for validation |
| Effective connectivity | Directed information flow |

**See also**: `by-domain/neuroscience.md`, `by-domain/information_theory.md`, `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

### DOI: 10.1371/journal.pcbi.1008054 --- Shorten, Spinney, Lizier (2021)
**"Estimating Transfer Entropy in Continuous Time Between Neural Spike Trains or Other Event-Based Data"**

**Domain(s)**: Information theory, neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Continuous-time TE measures directed information flow: how much the joint history (source + target point processes) improves prediction of target updates beyond the target's own history. The TE is formulated via Radon-Nikodym derivatives between measures of complete path realizations --- the joint measure vs the product of conditional and marginal measures. This is the purest mathematical formulation of joint-vs-marginal excess for event-based data: the excess is literally the KL divergence between the true conditional (given full history) and the reduced conditional (given only target history).
- **Null hypothesis**: The paper develops a local permutation scheme for generating null surrogates specifically for point process data. Standard source-time-shift surrogates are shown to FAIL for continuous-time spike trains (they do not properly destroy the source-target coupling while preserving marginal statistics). The local permutation scheme correctly generates surrogates conforming to the null hypothesis of conditional independence: H_source is independent of updates in target given H_target. This is a significant methodological advance --- the paper demonstrates that naive null-generation methods produce incorrect results, and provides a principled alternative.
- **Parameterized homology**: The continuous-time framework implicitly parameterizes TE by timescale. Unlike discrete-time TE which is locked to a single bin width, the kNN estimator captures relationships occurring at both fine temporal precision and over long time intervals simultaneously. The inter-spike interval serves as a natural continuous parameter. The pathwise transfer entropy (introduced by the precursor Spinney, Prokopenko, Lizier 2016) decomposes into discontinuous jump contributions (at target spikes) and continuously varying contributions (between spikes) --- a natural two-component parameterization by event type.

**What is genuinely new (not reducible to shared abstraction)**:
- Continuous-time formulation of TE via Radon-Nikodym derivatives on path space is mathematically distinct from discrete-time MI/TE. The pathwise transfer entropy --- accumulated TE along a specific realization, analogous to work/heat along a thermodynamic path --- is a genuinely new information-theoretic object without direct parallel in TDA or QEC.
- The k-nearest-neighbours estimator in the inter-event-interval embedding space is provably consistent (converges to the true TE) while discrete-time plug-in estimators are NOT consistent for event-based data. This is not merely an engineering improvement but a fundamental mathematical distinction: the discrete approach converges to the wrong value.
- Demonstration that source-time-shift surrogates fail for continuous-time data is a negative result about null hypothesis construction. The failure mode is specific to point processes: time-shifting a source spike train changes its temporal relationship to the target in a way that does not correspond to the intended null of conditional independence.
- Application to the pyloric circuit of the crustacean stomatogastric ganglion provides a biologically grounded validation where previous related estimators (discrete-time TE, model-based approaches) failed to correctly infer the known connectivity.

**Connections the authors acknowledge**: Cite Schreiber (2000) TE, Spinney/Prokopenko/Lizier (2016) continuous-time TE theory, JIDT toolkit. Cite neuroscience spike-train analysis literature. Acknowledge connection to Granger causality and point process GLMs. Do NOT cite TDA, persistent homology, or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transfer entropy | Directed joint-vs-marginal excess |
| Conditional independence | Null hypothesis (no directed coupling) |
| Local permutation surrogate | Null hypothesis distribution (structure-destroying, preserving marginal statistics) |
| Source-time-shift surrogate | Naive null (shown to fail) |
| kNN estimator | Estimation algorithm for excess |
| Pathwise transfer entropy | Accumulated excess along a realization |
| Inter-event interval | Continuous parameter (timescale) |
| Point process | Event-based time series (domain object) |
| Radon-Nikodym derivative | Density ratio quantifying excess |
| Pyloric circuit | Biological validation system |
| Spike train | Neural event sequence |

**See also**: `by-domain/information_theory.md`, `by-domain/neuroscience.md`, `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`
