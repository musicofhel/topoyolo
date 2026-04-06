# Information Theory

Papers from the information theory community, indexed by which abstract machines they instantiate. Cross-references to `by-structure/` files are given per paper.

---

## Belghazi et al. (2018)
**"Mutual Information Neural Estimation (MINE)"**
arXiv: 1801.04062 | ICML 2018

**Domain(s)**: Information theory, machine learning

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The paper's core object IS the joint-vs-marginal gap. MI is defined as I(X;Z) = D_KL(P_XZ || P_X ⊗ P_Z) — the KL divergence between the joint distribution and the product of marginals. MINE estimates this divergence via the Donsker-Varadhan dual representation: I(X;Z) = sup_T E_joint[T] - log(E_product[e^T]), where T is parameterized by a neural network. The entire method is a machine for measuring excess structure in the joint relative to independent marginals.
- **Null hypothesis**: The product of marginals P_X ⊗ P_Z serves as the explicit null distribution — it is what you get when you "destroy" the dependence between X and Z while preserving each variable's marginal statistics. MINE samples from both joint and product distributions; the gap between them is the signal.
- **Stability**: The paper proves strong consistency — as sample size → ∞, the MINE estimate converges to the true MI. They also prove the estimator is Lipschitz-bounded with respect to network parameters, providing perturbation guarantees.

**What is genuinely new (not reducible to shared abstraction)**:
- The use of neural networks as the function class for the dual representation. Previous dual estimators (Nguyen et al., 2010) used fixed function classes; parameterizing with deep networks makes the estimator scalable to high-dimensional continuous variables.
- The "exponential moving average" trick to reduce bias in the gradient of the Donsker-Varadhan bound — this is a practical optimization technique with no analogue in the other domains.
- Application to the Information Bottleneck method, using MINE as a differentiable MI layer within a deep network. This makes MI a loss function rather than just a diagnostic, which is a distinctly ML contribution.
- Applies MINE to improve mode coverage in GANs — uses MI maximization between generator input noise Z and generated output G(Z) to prevent mode dropping.

**Connections the authors acknowledge**: Cite the information bottleneck (Tishby et al., 2000) extensively. Acknowledge KL divergence estimation literature (Nguyen, Wainwright, Jordan 2010). No citations to TDA, QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Joint distribution P_XZ | Joint object |
| Product of marginals P_X ⊗ P_Z | Independence (null model) |
| Mutual information I(X;Z) | Excess (joint-vs-marginal gap) |
| KL divergence D_KL | Detection method for excess |
| Donsker-Varadhan representation | Dual formulation of excess detection |
| Strong consistency | Stability guarantee |
| Information bottleneck | Parameterized compression (related to parameterized homology) |

**See also**: `by-structure/composite_systems.md`

---

## Wickstrøm, Løkse, Kampffmeyer, Yu, Principe, Jenssen (2019)
**"Information Plane Analysis of Deep Neural Networks via Matrix-Based Rényi's Entropy and Tensor Kernels"**
arXiv: 1909.11396

**Domain(s)**: Information theory, machine learning

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The paper measures I(X;T) and I(T;Y) — mutual information between input X, hidden layer representation T, and output Y. Each MI quantity measures how much joint structure exists between a layer and input/output beyond what marginals would predict.
- **Parameterized homology**: The core contribution is tracking how these MI values change as a parameter varies — here the parameter is training epoch, not a filtration scale or error rate. The "information plane" plots I(X;T) vs I(T;Y) across training, revealing two phases: a fitting phase (both increase) and a compression phase (I(X;T) decreases while I(T;Y) stays high). This is structurally analogous to tracking Betti numbers across a filtration, or tracking logical error rate across error threshold — an invariant changes character at critical parameter values.
- **Null hypothesis**: The compression phase corresponds to the network destroying information about X that is not needed for Y — a selective destruction of structure while preserving task-relevant structure. This is the null-model logic inverted: instead of destroying coupling to test significance, the network learns to destroy irrelevant coupling.

**What is genuinely new (not reducible to shared abstraction)**:
- Matrix-based Rényi's entropy with tensor kernels: replaces Shannon entropy with Rényi's α-entropy computed via eigenvalues of a Gram matrix. This avoids density estimation entirely — a fundamentally different computational approach from bin-based or KNN MI estimators.
- Scales to VGG-16 — first information plane analysis of a production-scale deep CNN. Prior work was limited to small networks.
- Finding that compression phase correlates with overfitting: early stopping typically halts training before compression occurs. This challenges the Tishby-Shwartz-Ziv narrative that compression is beneficial.
- Tensor kernel construction for convolutional layers — respects the spatial structure of feature maps rather than flattening.

**Connections the authors acknowledge**: Extensive engagement with the Shwartz-Ziv & Tishby (2017) information bottleneck debate. Cite Saxe et al. (2018) who linked compression to activation saturation. No citations outside ML/information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Information plane | Parameter space (2D projection of parameterized information invariants) |
| I(X;T), I(T;Y) | Joint-vs-marginal excess at each layer |
| Training epoch | The parameter (analogous to filtration scale ε) |
| Fitting phase | Birth of features (analogous to feature appearance in persistence) |
| Compression phase | Death of features (analogous to feature disappearance; selective structure destruction) |
| Matrix-based Rényi's entropy | Spectral invariant of the data distribution |
| Tensor kernel | Local structure encoder for convolutional layers |

**See also**: `by-structure/composite_systems.md`, `by-structure/filtrations.md`

---

## Mézard & Mora (2008)
**"Constraint satisfaction problems and neural networks: a statistical physics perspective"**
arXiv: 0803.3061

**Domain(s)**: Statistical physics, information theory, neuroscience

**Abstract machines instantiated**:
- **Chain complex**: LDPC (Low-Density Parity-Check) codes are explicitly chain complexes over GF(2). The parity-check matrix H defines a boundary operator: a codeword c is valid iff Hc = 0 (mod 2), i.e., c ∈ ker(H). Syndromes are the images s = He for error vectors e. The paper treats LDPC decoding, random k-SAT, and perceptron learning as instances of the same graphical model structure — factor graphs where variables and constraints interact through local compatibility functions.
- **Parameterized homology**: The random k-SAT phase transition at α_c ≈ 4.267 is a critical parameter value where the structure of the solution space changes qualitatively. Below α_c, solutions form a connected cluster; above, the solution space shatters into exponentially many disconnected clusters. This is a genuine topological phase transition in the solution landscape, parameterized by the constraint density α = M/N.
- **Matching**: Belief Propagation and Survey Propagation are message-passing algorithms that solve an approximate matching problem on the factor graph — assigning values to variables to satisfy constraints. For LDPC codes, this reduces to syndrome decoding (matching errors to syndromes). The paper notes that BP achieves near-optimal decoding for sparse codes.
- **Stability**: The paper discusses the distinction between the "easy-SAT" regime (α < α_d, BP converges), the "hard-SAT" regime (α_d < α < α_c, BP fails but Survey Propagation works), and the UNSAT regime (α > α_c). Each transition marks a change in the stability of the message-passing fixed point.
- **Null hypothesis**: Random k-SAT instances serve as the null model for typical-case complexity — random structure with controlled density, against which algorithmic performance is benchmarked.

**What is genuinely new (not reducible to shared abstraction)**:
- The unification of satisfiability, error correction, and neural network inference under a single graphical-model formalism. This is itself a Rosetta-like move — the paper explicitly maps between domains.
- Survey Propagation: operates on the space of "surveys" (probability distributions over messages), capturing the full complexity of the clustered solution space. This is a meta-level message-passing algorithm with no direct analogue in TDA or dynamical systems.
- The proposed message-passing algorithm for inferring neural interactions from multi-electrode correlation data. This is a neuroscience application of the inverse problem (given correlations, reconstruct the interaction graph), cast as a constraint-satisfaction problem.
- The connection between replica symmetry breaking in spin glasses and the clustering of solutions in SAT. This statistical physics concept (the Parisi order parameter) describes the hierarchical organization of solution space — it is richer than a simple Betti number count.

**Connections the authors acknowledge**: This paper IS a bridge paper. It explicitly connects: (1) random k-SAT and computational complexity, (2) LDPC error correction and information theory, (3) perceptron learning and neural networks, (4) statistical physics phase transitions and spin glasses. One of the rare papers that sees across multiple domains simultaneously. Does NOT cite TDA or persistent homology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Parity-check matrix H | Boundary operator ∂ |
| Codeword (Hc = 0) | Cycle (element of ker ∂) |
| Syndrome (s = He) | Image of ∂ applied to error |
| Factor graph | Chain complex (generalized) |
| Constraint density α = M/N | The parameter (filtration/error rate/bifurcation) |
| SAT/UNSAT phase transition | Critical value (topological change) |
| Belief Propagation | Approximate matching on factor graph |
| Survey Propagation | Matching on the space of surveys (meta-level) |
| Solution cluster shattering | Topological phase transition in solution space |
| Random k-SAT ensemble | Null model (random structure, controlled density) |
| Replica symmetry breaking | Hierarchical organization of solution space |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-structure/composite_systems.md`, `by-domain/neuroscience.md`

---

## Tax, Mediano & Shanahan (2017)
**"The Partial Information Decomposition of Generative Neural Network Models"**
DOI: 10.3390/e19090474 | Entropy 19(9), 474

**Domain(s)**: Information theory, neuroscience (computational), machine learning

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: PID decomposes the mutual information I({S1, S2, ...}; Y) between multiple source neurons Si and a target Y into redundant, unique, and synergistic atoms. Synergy is the quintessential joint-vs-marginal excess: information that is present in the joint set of sources but absent from any individual source. The paper tracks how synergy, redundancy, and unique information evolve during RBM training.
- **Parameterized homology**: Training epoch serves as the parameter. The paper discovers two phases: (1) an initial phase where neurons acquire redundant information (all neurons learn the same coarse features), followed by (2) a specialization phase where neurons differentiate and acquire unique/synergistic information. The transition between phases is a qualitative change in the information-theoretic "topology" of the representation.
- **Null hypothesis**: Implicit — the paper compares actual PID atoms against what would be expected from independent neurons (zero synergy, zero redundancy). The deviation from independence is the signal.

**What is genuinely new (not reducible to shared abstraction)**:
- Applying PID to track the internal dynamics of learning in a restricted Boltzmann machine (RBM). This is one of the first papers to use PID as a lens on representation learning.
- The discovery of the redundancy-then-specialization pattern in training. This two-phase structure is reminiscent of the fitting-compression narrative (Tishby) but described in PID terms, which gives finer-grained decomposition.
- The finding that smaller networks produce more disentangled representations (higher unique information per neuron) — learning pressure from capacity constraints forces specialization.
- Uses the Williams-Beer PID framework (I_min measure of redundancy), acknowledging its limitations but arguing it suffices for qualitative analysis.

**Connections the authors acknowledge**: Explicit bridge between information theory and machine learning. Cite neuroscience literature on neural coding (comparing artificial and biological neural codes). Acknowledge PID literature (Williams & Beer, 2010; Bertschinger et al., 2014). No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Redundant information | Shared structure across components (opposite of excess) |
| Unique information | Component-specific structure |
| Synergistic information | Joint-vs-marginal excess |
| PID atoms | Decomposition of the composite-system signal |
| Training epoch | The parameter |
| Redundancy → specialization transition | Phase transition / critical parameter value |
| Restricted Boltzmann machine | The system under study |
| I_min (Williams-Beer) | Redundancy measure (specific operationalization) |

**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`

---

## Chwilka & Karbowski (2024)
**"Explicit mutual information for simple networks and neurons with lognormal activities"**
arXiv: 2307.00017v2

**Domain(s)**: Information theory, neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The paper derives exact analytical formulas for MI between correlated lognormally distributed variables. MI = I(X;Y) measures the excess information in the joint distribution (X,Y) beyond what the marginals provide. The key result is that for lognormal variables, MI can diverge at finite variances — meaning the joint-vs-marginal excess can become infinite, unlike the Gaussian case where MI is always finite for finite correlations.
- **Stability**: The divergence result is an anti-stability finding: small changes in the variance parameter can push MI from finite to infinite. This marks a phase boundary in parameter space — a qualitative change in the information-theoretic invariant as the distribution parameter crosses a critical threshold. The contrast with Gaussian MI (which is smooth and bounded) is itself informative about where the stability analogy holds and where it breaks.

**What is genuinely new (not reducible to shared abstraction)**:
- Closed-form MI for multivariate lognormal distributions. Prior exact results existed only for Gaussian and a handful of other distributions. The lognormal case is important because empirical neural firing rates and synaptic weights are approximately lognormal.
- The divergence phenomenon: MI between lognormal variables can blow up at finite variance. This has no Gaussian analogue and suggests that heavy-tailed neural statistics carry fundamentally more information than light-tailed ones.
- Evolutionary argument: the authors suggest that the ubiquity of lognormal distributions in neural systems may reflect selection pressure for information-processing capacity — brains may have evolved heavy-tailed dynamics because they maximize MI.
- Application to cortical circuits with many correlated synaptic inputs — derives MI for a realistic presynaptic fan-in model.

**Connections the authors acknowledge**: Cite neuroscience literature on lognormal firing rates (Buzsáki & Mizuseki, 2014) and lognormal synaptic weights (Song et al., 2005). Cite information theory fundamentals (Cover & Thomas). No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Mutual information I(X;Y) | Joint-vs-marginal excess |
| Lognormal distribution | Distribution over the space (heavy-tailed) |
| Variance parameter σ² | The parameter (controls the system) |
| MI divergence at finite σ² | Phase transition / critical parameter value |
| Gaussian baseline | Null model (implicit — the well-behaved case) |
| Presynaptic fan-in | Composite system (many inputs to one neuron) |

**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`

---

## Sugiyama, Nakahara & Tsuda (2016)
**"Information Decomposition on Structured Space"**
arXiv: 1601.05533

**Domain(s)**: Information theory, information geometry

**Abstract machines instantiated**:
- **Chain complex**: The paper constructs dual coordinate systems (θ and η) on partially ordered sets (posets). The θ-coordinate is defined via principal ideals (↓x) and the η-coordinate via principal filters (↑x) — these are order-theoretic analogues of boundary and coboundary operators. The Möbius function on the poset plays the role of the boundary operator, enabling decomposition of probability distributions into contributions from each element of the poset hierarchy. The condition ∂²=0 manifests as the Möbius inversion formula: applying the Möbius function twice recovers the original distribution, which is the order-theoretic version of ∂²=0. The poset structure (complete or incomplete hierarchy of event combinations) IS a chain complex, with the grading given by the number of events in each combination.
- **Joint-vs-marginal excess**: The orthogonal decomposition of KL divergence isolates the contribution of each event combination — higher-order interactions (3-way, 4-way, ...) are precisely the joint-vs-marginal excess at each level. The Pythagorean theorem for KL divergence on posets (D_KL(p||r) = D_KL(p||q) + D_KL(q||r) for appropriate q on a sub-poset) allows clean separation of marginal vs. joint contributions. This is the most algebraically rigorous treatment of joint-vs-marginal decomposition in the entire Rosetta.
- **Null hypothesis**: The method decomposes entropy by comparing the full distribution against independence models at each level of the hierarchy. Each lower-order model (e.g., pairwise-only) serves as a null against which the next level's contribution is tested.

**What is genuinely new (not reducible to shared abstraction)**:
- The connection between order theory and information geometry. Principal ideals and filters on posets map to θ and η coordinates of the exponential family manifold. This is a genuinely new bridge — neither the information geometry literature (Amari) nor the order theory literature had made this connection explicit for incomplete hierarchies.
- Handling of incomplete hierarchies — when some event combinations are impossible (e.g., male + ovarian cancer), the poset is not a complete lattice. The paper shows the dually flat structure persists even on incomplete posets, which is non-trivial.
- Efficient algorithms (O(|S|²) time) for decomposition on arbitrary posets. Prior methods assumed complete hierarchies (2^n elements for n events).
- Application to neuroscience: analyzing higher-order firing patterns in neural ensembles, isolating genuine 3-way interactions from pairwise effects.

**Connections the authors acknowledge**: Explicitly cite Amari's information geometry and extend it. Cite neuroscience applications (firing pattern analysis). Reference combinatorics and order theory. Do NOT cite TDA, QEC, or dynamical systems — but this paper is one of the closest to a genuine algebraic bridge between information theory and chain-complex reasoning.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Poset (partially ordered set) | Chain complex (graded by combination level) |
| Principal ideal ↓x | Support of boundary operator ∂ at x |
| Principal filter ↑x | Support of coboundary operator δ at x |
| Möbius function μ | Boundary operator (on the poset) |
| θ-coordinate | Natural parameter (exponential family) |
| η-coordinate | Expectation parameter (dual coordinate) |
| Pythagorean theorem for KL | Orthogonal decomposition of joint-vs-marginal excess |
| Higher-order interaction | Joint-vs-marginal excess at level k |
| Independence model | Null hypothesis (lower-order structure only) |
| Incomplete hierarchy | Poset with missing faces (incomplete simplicial complex) |

**See also**: `by-structure/boundary_operators.md`, `by-structure/composite_systems.md`

---

## Geiger (2021)
**"On Information Plane Analyses of Neural Network Classifiers — A Review"**
arXiv: 2003.09671v3

**Domain(s)**: Information theory, machine learning

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Reviews how I(X;T) and I(T;Y) quantify dependence between layers and input/output. The core insight: MI measures joint-vs-marginal excess, and the information plane plots this excess at each layer.
- **Parameterized homology**: The review's central question is whether the fitting → compression trajectory on the information plane (parameterized by training epoch) is real or an artifact of MI estimation. The author surveys conflicting evidence: compression appears with saturating activations (tanh) but not with ReLU; some MI estimators show compression where others don't. This is itself a stability question — is the observed parameterized trajectory robust to the measurement method?
- **Null hypothesis**: The review identifies a key distinction: observed "compression" is often geometric (latent representations cluster/shrink) rather than information-theoretic (MI genuinely decreases). The geometric null model — representations that cluster but preserve full MI — explains many of the conflicting results. The paper argues that geometric compression IS useful for generalization, even if information-theoretic compression is not always present.

**What is genuinely new (not reducible to shared abstraction)**:
- The systematic survey of MI estimation methods and their artifacts. Different estimators (binning, KDE, KSG, MINE, kernel-based) give qualitatively different information planes for the same network. This is a methodological warning: the "invariant" (MI) depends on how you compute it.
- The distinction between information-theoretic and geometric compression. A network can geometrically compress representations (shrink clusters) without reducing MI. This disentangles two notions of "compression" that had been conflated.
- Proof that the data processing inequality (DPI) need not hold for MI *estimates* in deterministic networks, even though it holds for true MI. This means the information plane can show apparent DPI violations.
- The conclusion that evidence for a causal link between compression and generalization remains weak. Early stopping typically halts training before compression occurs.

**Connections the authors acknowledge**: Extensive engagement with Tishby, Shwartz-Ziv, Saxe, and the information bottleneck debate. No connections outside ML/information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Information plane | 2D projection of parameterized invariant |
| Fitting phase | Feature birth (invariant increases) |
| Compression phase | Feature death (invariant decreases) |
| MI estimator | Measurement method for the invariant |
| Geometric compression | Clustering/shrinking — distinct from information-theoretic compression |
| Data processing inequality | Monotonicity constraint on the invariant across a chain |
| Deterministic network | System where DPI holds exactly but estimates may violate it |

**See also**: `by-structure/filtrations.md`, `by-structure/composite_systems.md`

---

## Jónsson, Cherubini & Eleftheriou (2020)
**"Convergence Behavior of DNNs with Mutual-Information-Based Regularization"**
DOI: 10.3390/e22070727 | Entropy 22(7), 727

**Domain(s)**: Information theory, machine learning

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Uses MINE to estimate I(X;T) and I(T;Y) in a VGG-16 CNN on CIFAR-10. MI as the joint-vs-marginal quantity.
- **Parameterized homology**: Confirms the existence of fitting + compression phases in a production-scale CNN, extending prior results from small fully-connected networks. The parameter (training epoch) traces a trajectory on the information plane. Uses MINE as the estimator, addressing scalability issues of non-parametric methods.
- **Stability**: The paper's main contribution is MI-based regularization: adding I(X;T) as a penalty term in the loss function. This stabilizes test accuracy and reduces variance — a stability result on the training process itself. Compares MINE-based regularization with Variational Information Bottleneck (VIB).

**What is genuinely new (not reducible to shared abstraction)**:
- First confirmation of compression phase in a high-dimensional CNN (VGG-16) using neural MI estimation (MINE). Prior work was limited to small networks.
- MI-based regularization as a practical training technique: using I(X;T) estimated by MINE as an additional loss term. The regularized network shows lower variance in test accuracy across training epochs.
- Comparison of MINE vs. VIB as regularization strategies — both improve stability, with MINE showing slightly better variance reduction.

**Connections the authors acknowledge**: Cite Tishby's information bottleneck, Shwartz-Ziv (2017), Belghazi et al. (MINE). No connections outside ML/information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Information plane | Parameter space (MI tracked across epochs) |
| MINE regularization | Stability intervention (bounds the invariant) |
| Compression phase | Feature death / information destruction |
| VIB (Variational Information Bottleneck) | Alternative stability intervention |
| Test accuracy variance | Robustness measure |

**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`
