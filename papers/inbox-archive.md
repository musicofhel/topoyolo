# Inbox — Archive (Waves 1-3)

Archived annotations from sessions 1-3. For current annotations (Waves 4+), see [inbox.md](inbox.md).

Full-depth annotations of papers in the topo-rosetta corpus. Each paper is cross-referenced in the dual index (by-domain + by-structure) and relevant atlas files.

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

