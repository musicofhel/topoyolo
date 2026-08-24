# Inbox — Archive (Waves 1-3)

Archived annotations from sessions 1-3. For current annotations (Waves 4+), see [inbox.md](inbox.md).

Full-depth annotations of papers in the topo-rosetta corpus. Each paper is cross-referenced in the dual index (by-domain + by-structure) and relevant atlas files.

---

## Wave 1-2 annotations — migrated to per-paper files

Each annotation below is verbatim-migrated to `papers/annotations/` (A3 slice 1):

- [de la Fuente et al. (2025) — non-Pauli decoding](annotations/2604.02033.md) — `annotations/2604.02033.md`
- [Takens (1981)](annotations/takens-1981.md) — `annotations/takens-1981.md`
- [Sauer, Yorke, Casdagli (1991)](annotations/sauer-1991.md) — `annotations/sauer-1991.md`
- [Bauer (2021) — Ripser](annotations/2108.03831.md) — `annotations/2108.03831.md`
- [Peek et al. (2025) — TE + directed PH](annotations/2508.19048.md) — `annotations/2508.19048.md`
- [Schreiber (2000) — transfer entropy](annotations/schreiber-2000.md) — `annotations/schreiber-2000.md`
- [Tort et al. (2010) — PAC modulation index](annotations/tort-2010.md) — `annotations/tort-2010.md`
- [Giusti et al. (2015) — clique topology](annotations/1502.06172.md) — `annotations/1502.06172.md`
- [Reimann et al. (2017) — directed cliques/cavities](annotations/10.3389-fncom.2017.00048.md) — `annotations/10.3389-fncom.2017.00048.md`
- [Dabaghian et al. (2012) — hippocampal PH](annotations/10.1371-journal.pcbi.1002581.md) — `annotations/10.1371-journal.pcbi.1002581.md`
- [Curto & Itskov (2008) — cell groups](annotations/10.1371-journal.pcbi.1000205.md) — `annotations/10.1371-journal.pcbi.1000205.md`
- [Divol & Lacombe (2019) — PD space as OT](annotations/1901.03048.md) — `annotations/1901.03048.md`
- [Vejdemo-Johansson & Mukherjee (2018)](annotations/1812.06491.md) — `annotations/1812.06491.md`
- [Harrington et al. (2017) — multiparameter PH](annotations/1708.07390.md) — `annotations/1708.07390.md`
- [Wong & Yang (2019) — info geometry ↔ OT](annotations/1906.00030.md) — `annotations/1906.00030.md`

## Core ATT papers (annotated)

### Cohen-Steiner, Edelsbrunner, Harer (2007) — "Stability of persistence diagrams"
**Domain**: TDA. **Machines**: Stability (bottleneck ≤ Hausdorff), parameterized homology. **Full annotation**: [annotations/math-0604068.md](annotations/math-0604068.md).

### Adams et al. (2017) — "Persistence images"
**Domain**: TDA. **Machines**: Parameterized homology (vectorized), stability (W_1 Lipschitz bounds, Theorems 1-4), matching (implicit via Wasserstein optimal bijection), chain complex (implicit, Appendix A). **Full annotation below** (arXiv: 1507.06217).

### Giusti, Curto et al. (2015) — "Clique topology reveals intrinsic geometric structure"
**Domain**: Neuroscience + TDA. **Machines**: Chain complex (clique complex on correlations), parameterized homology, null hypothesis. **Full annotation**: [annotations/1502.06172.md](annotations/1502.06172.md).

### Gardner et al. (2022) — "Toroidal topology of population activity in grid cells"
**Domain**: Neuroscience, TDA. **Machines**: Chain complex, parameterized homology, stability, null hypothesis, joint-vs-marginal. The torus IS the neural manifold — same object as the toric code's base space, different interpretation. **Full annotation below** (DOI: 10.1038/s41586-021-04268-7). **See also**: `cross_domain_bridges.md` (neuro ↔ QEC via shared T²).

### Sugihara et al. (2012) — CCM (Science, DOI: 10.1126/science.1227079)
**Domain**: Dynamical systems + causal inference. **Machines**: Joint-vs-marginal (manifold cross-prediction), stability (convergence criterion), null hypothesis (no-coupling null + surrogates), parameterized homology (weak — library size L as filtration). **Full annotation below** (DOI: 10.1126/science.1227079).

### Tsuda (2001) — "Chaotic itinerancy"
**Domain**: Neuroscience + dynamical systems. **Machines**: Parameterized homology (attractor switching = path through topology space), stability (quasi-stability via attractor ruins), null hypothesis (fixed-point/limit-cycle as non-itinerant null), chain complex (weak — sequence of ruins with heteroclinic connections). **Fully annotated below** (DOI: 10.1017/S0140525X01000097).

## Found and annotated (Wave 4b)

Each annotation below is verbatim-migrated to `papers/annotations/` (A3 slice 2):

- [Kitaev (1997) — fault-tolerant quantum computation by anyons](annotations/quant-ph-9707021.md)
- [Dennis, Kitaev, Landahl, Preskill (2002) — topological quantum memory](annotations/quant-ph-0110143.md)
- [Perea & Harer (2013) — SW1PerS sliding-window persistence](annotations/1307.6188.md)
- [Cohen-Steiner, Edelsbrunner, Harer (2007) — stability of persistence diagrams](annotations/math-0604068.md)

## Wave 3 triage annotations

Migrated verbatim to `papers/annotations/` (A3 slice 2):

- [Baudot & Bennequin (2015) — the homological nature of entropy](annotations/baudot-2015.md)
- [Bradley (2021) — entropy as a topological operad derivation](annotations/2107.09581.md)
- [Kolchinsky (2024) — PID redundancy as information bottleneck](annotations/2405.07665.md)

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
