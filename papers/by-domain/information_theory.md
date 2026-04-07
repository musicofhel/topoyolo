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

---

# Partial Information Decomposition — Core Papers

The PID programme decomposes I(T; X1, ..., Xn) into redundant, unique, and synergistic atoms. The entire enterprise is an extended exercise in the **joint-vs-marginal excess** machine: synergy is precisely the information present in (X,Y) jointly that is absent from X and Y marginally. The algebraic backbone — the redundancy lattice with Mobius inversion — is a chain-complex-like structure shared by all papers below.

---

## PID-01 — Kolchinsky (2022)
**"A Novel Approach to the Partial Information Decomposition"**

**Domain(s)**: Information theory

**Abstract machines instantiated**:

- **Chain complex**: The redundancy lattice is a partially ordered set with a Mobius inversion formula that recovers partial information atoms from cumulative redundancy values. The Mobius inversion plays the role of a boundary operator: it maps cumulative (cycle-like) quantities to their differential (boundary-like) constituents. The lattice nodes are antichains of sources, and the partial ordering (one source is "more informative" than another) is the structural analogue of face inclusions in a simplicial complex. The relation I_partial = I_intersect - sum(I_intersect of sub-nodes) mirrors the alternating-sign structure of the boundary map.

- **Joint-vs-marginal excess**: This is the paper's central concern. Synergy = I(T; X1,...,Xn) - Union_information. The joint system (X1,...,Xn) provides information about T that no individual source or sub-collection provides. Kolchinsky makes the key move of defining redundancy and union information independently (not via inclusion-exclusion), which means the excess of joint over marginal is not constrained by set-theoretic identities. The Blackwell order determines when one source is "more informative" than another in a decision-theoretic sense, and the gap between the joint and the Blackwell-optimal marginal is the synergy.

- **Matching**: The Blackwell order instantiates a comparison: source X is more informative than source Y if there exists a stochastic channel kappa such that Y = kappa(X). Finding the "largest" source dominated by all input sources (redundancy) or the "smallest" source dominating all (union) is an optimization over channels — an assignment problem in the space of stochastic maps.

- **Stability**: Implicit. The Blackwell order is preserved under post-processing (data processing inequality), which is a monotonicity/stability result: no stochastic transformation can increase informativeness.

**What is genuinely new**:
- The decoupling of redundancy and union information: Kolchinsky argues the inclusion-exclusion principle (|A union B| = |A| + |B| - |A intersect B|) does NOT hold for information, violating the set-theoretic analogy that motivated the original PID. This is a structural insight: information atoms do not form a Boolean algebra. The lattice is not distributive.
- Grounding PID in the Blackwell order gives operational interpretability via decision theory (expected utility maximization), going beyond the purely axiomatic approaches of Williams-Beer or Bertschinger et al.
- Explicit extension to algorithmic information theory and quantum information theory as future directions — the framework is parametric in the choice of ordering relation.

**Connections the authors acknowledge**: Extensive engagement with prior PID work (Williams-Beer, Bertschinger et al., Griffith-Koch, Harder et al., Ince, Finn-Lizier). Acknowledges the Blackwell order's origins in statistical decision theory (Blackwell 1953, Le Cam). Does NOT acknowledge any connection to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| Source random variable X_i | Component / marginal |
| Target Y | Observable / stimulus |
| Redundancy I_cap | Marginal content (what each component preserves) |
| Union information I_cup | Joint content minus synergy |
| Synergy | Joint-vs-marginal excess |
| Partial information atom | Differential element (Mobius-inverted node) |
| Redundancy lattice | Partially ordered set of source antichains |
| Blackwell order (X > Y) | "More informative" = existence of degradation channel |
| Inclusion-exclusion failure | Non-distributivity of the information lattice |
| Stochastic channel kappa | Morphism between sources (degradation map) |

**See also**: `by-structure/composite_systems.md`

---

## PID-02 — Ince (2017)
**"The Partial Entropy Decomposition: Decomposing multivariate entropy and mutual information via pointwise common surprisal"**

**Domain(s)**: Information theory, neuroscience (application context)

**Abstract machines instantiated**:

- **Chain complex**: Applies the Williams-Beer redundancy lattice framework (Mobius inversion over antichain poset) to entropy rather than mutual information. The lattice structure and its inversion formula are identical to PID-01's algebraic skeleton. The partial entropy function H_partial is defined via Mobius inversion of cumulative entropy H_intersect, exactly paralleling how homology groups are obtained from chain groups via quotient.

- **Joint-vs-marginal excess**: Synergistic entropy — uncertainty that arises only when variables are combined but is absent from individual variables. This is the entropy-domain analogue of information synergy: H(X1, X2) contains entropy atoms not present in H(X1) or H(X2) alone. The paper's central claim is that mutual information itself mixes redundant and synergistic entropy, so the standard MI already conflates joint-vs-marginal structure.

- **Null hypothesis**: The paper constructs diagnostic example systems (DblXor, RedDom, AndDup, XorDup, James-Crutchfield's indistinguishable-by-I-diagram systems) to test whether a decomposition can distinguish generative structures that are invisible to all classical Shannon measures. These examples function as null-vs-alternative tests: if a measure cannot distinguish two systems with identical I-diagrams, it fails the diagnostic.

**What is genuinely new**:
- Decomposing entropy (not MI) via the PID lattice. This is a conceptual shift: the PID was always about information *about a target*, but PED removes the target variable entirely and decomposes the entropy of the source variables themselves. This reveals that misinformation (negative local MI) is synergistic entropy.
- Mechanistic vs source redundancy distinction: mechanistic redundancy arises from the function mapping inputs to outputs, source redundancy arises from correlations among inputs. No prior PID framework separated these.
- The insight that univariate predictor MI is not a proper subset of joint MI *in entropy terms* — this explains a structural reason why consistent PID has been elusive.
- Pointwise common surprisal as the primitive: the entropy redundancy measure is built from pointwise (realization-level) quantities, not averages.

**Connections the authors acknowledge**: Williams-Beer (2010), Bertschinger et al. (2014), Griffith-Koch, Harder et al., the "challenge" of James and Crutchfield (2016) to distinguish systems with equal I-diagrams. Application context in neuroscience (neural coding). No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| Partial entropy atom H_partial | Differential element of entropy lattice |
| Entropy redundancy H_intersect | Shared structure across components |
| Synergistic entropy | Joint-vs-marginal excess (in entropy) |
| Misinformation | Negative local MI = synergistic entropy atom |
| Pointwise common surprisal | Local (realization-level) shared information |
| Mechanistic redundancy | Functional overlap (input-output map) |
| Source redundancy | Correlational overlap (input statistics) |
| I-diagram | Classical Shannon decomposition (insufficient) |
| PED lattice | Same poset as PID, applied to entropy |

**See also**: `by-structure/composite_systems.md`

---

## PID-03 — Venkatesh, Schamberg (2022)
**"Partial Information Decomposition via Deficiency for Multivariate Gaussians"**

**Domain(s)**: Information theory, statistics

**Abstract machines instantiated**:

- **Matching**: The core computational problem is a convex optimization over the space of joint Gaussian distributions. For the deficiency-based PID, the algorithm seeks the distribution Q that minimizes mutual information subject to marginal constraints — this is an optimal assignment in probability-distribution space. The convex relaxation reduces the search over all distributions to a search over covariance matrices satisfying Schur complement constraints.

- **Joint-vs-marginal excess**: The bivariate PID decomposes I(M; (X,Y)) into unique_X, unique_Y, redundant, and synergistic components. Synergy is information in (X,Y) jointly that is absent from X or Y marginally. The paper's main contribution is making this decomposition computationally tractable for high-dimensional Gaussian vectors.

- **Stability**: Barrett's closed-form result for scalar messages is shown to NOT extend to vector messages — a failure of stability under dimensionality increase. The paper characterizes exactly when the closed-form does extend (Blackwell sufficiency condition) and shows the approximation error of their convex relaxation is bounded, providing a quantitative stability guarantee for their algorithm.

**What is genuinely new**:
- The counterexample showing Barrett's scalar PID result breaks for vector M. If M = [M1, M2], X = M1 + Z1, Y = M2 + Z2 with independent Gaussians, the MMI-PID says X and Y have only redundant information (since I(M;X) = I(M;Y)), but the deficiency-based PID correctly assigns unique information to each — they carry information about *different components* of M.
- Blackwell sufficiency as the bridge concept: X is Blackwell sufficient for M w.r.t. Y iff the PID has zero unique-Y information. This connects PID to Le Cam's theory of statistical experiments.
- Efficient computation for tens-to-hundreds of dimensions via convex programming on covariance matrices, with provable approximation bounds.

**Connections the authors acknowledge**: Barrett (2015), Bertschinger et al. (BROJA), Blackwell (1953), Le Cam (deficiency). Applications to neural data analysis. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| Message M | Target / observable |
| Constituents X, Y | Components / sources |
| Unique information UI(M:X\Y) | Component-exclusive contribution |
| Redundant information RI | Shared marginal content |
| Synergistic information SI | Joint-vs-marginal excess |
| Blackwell sufficiency | Degradation ordering (X degrades to Y) |
| Deficiency | Distance from sufficiency (Le Cam) |
| MMI-PID | min{I(M;X), I(M;Y)} baseline |
| Covariance constraint (Schur complement) | Feasible region boundary |
| Convex relaxation | Tractable approximation of matching problem |

**See also**: `by-structure/composite_systems.md`

---

## PID-04 — Finn, Lizier (2018)
**"Pointwise Partial Information Decomposition Using the Specificity and Ambiguity Lattices"**

**Domain(s)**: Information theory

**Abstract machines instantiated**:

- **Chain complex**: The paper constructs TWO redundancy lattices — one for specificity, one for ambiguity — each with its own Mobius inversion. The dual-lattice structure means the PID is computed by combining atoms from two parallel chain-like algebraic structures. The lattice nodes are antichains of sources as in Williams-Beer, but the partial ordering operates independently on each unsigned component. This is structurally analogous to decomposing a chain complex into its positive and negative parts.

- **Joint-vs-marginal excess**: Synergistic information appears in both the specificity and ambiguity lattices. Synergistic specificity is target-reduction that only occurs when sources are combined. Synergistic ambiguity is target-confusion that only arises jointly. The full synergy atom in the recombined decomposition is their difference.

- **Null hypothesis**: The paper uses canonical examples (XOR, AND, COPY, RDN, UNIQ, two-bit-copy) as diagnostic benchmarks. Each example has known "correct" behavior that any PID measure must reproduce. These function as null-hypothesis tests: a proposed measure is rejected if it assigns wrong values on these canonical distributions.

**What is genuinely new**:
- Decomposing pointwise mutual information i(s;t) into unsigned components BEFORE applying the PID lattice. Standard PID operates on average MI. Pointwise MI can be negative (misinformation), which creates problems for non-negativity axioms. Finn-Lizier circumvent this by splitting pmi into specificity h(t) - h(t|s) (how much observing s narrows T) and ambiguity h(t|s) (residual uncertainty). Each is non-negative, so each can be decomposed over a redundancy lattice without sign issues.
- The chain rule over target variables: the pointwise decomposition satisfies i(s; t1, t2) = i(s; t1) + i(s; t2|t1), and the PID atoms respect this chain rule. This is a structural constraint that most PID proposals violate.
- The two-bit-copy resolution: the dual-lattice approach gives the "correct" answer on the contentious two-bit-copy example, interpreted via Kelly gambling in the appendix.
- Operational interpretation of redundancy via the "same information" criterion: two sources provide redundant specificity if observing either one eliminates uncertainty about the same target outcomes in the same way.

**Connections the authors acknowledge**: Williams-Beer (2010), Bertschinger et al. (2014), Griffith-Koch (2014), Harder et al. (2013), Ince (2016/2017), James-Crutchfield. The Kelly gambling interpretation in the appendix connects to decision theory / economics. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| Specificity h(t) - h(t\|s) | Information gain (target uncertainty reduction) |
| Ambiguity h(t\|s) | Residual uncertainty after observation |
| Specificity lattice | Positive-part redundancy poset |
| Ambiguity lattice | Negative-part redundancy poset |
| Pointwise mutual information i(s;t) | Local information (single realization) |
| Redundant specificity | Shared structure in information gain |
| Synergistic ambiguity | Joint-vs-marginal excess in residual uncertainty |
| Source A_i | Subset of predictor variables |
| Target T | Observable being predicted |
| Two-bit-copy | Canonical diagnostic distribution |
| Chain rule over targets | Compositional constraint on atoms |
| Kelly gambling interpretation | Decision-theoretic grounding |

**See also**: `by-structure/composite_systems.md`

---

## PID-05 — Schick-Poland, Makkeh, Gutknecht, Wollstadt, Sturm, Wibral (2021)
**"A partial information decomposition for discrete and continuous variables"**

**Domain(s)**: Information theory, measure theory

**Abstract machines instantiated**:

- **Chain complex**: The PID lattice (Williams-Beer antichain poset with Mobius inversion) is the algebraic backbone throughout. The paper's contribution is extending this lattice structure from discrete probability spaces to arbitrary measure-theoretic spaces while preserving the inversion formula.

- **Joint-vs-marginal excess**: Synergistic information — the atom at the top of the lattice — represents information about T that only manifests when sources are combined. The measure-theoretic extension ensures this concept is well-defined for continuous and mixed distributions, not just finite alphabets.

- **Stability**: The paper proves three stability-type properties: (1) invariance under invertible transformations (reparametrization does not change the PID), (2) differentiability w.r.t. the underlying probability density (small perturbations in the distribution yield small changes in PID atoms), and (3) recovery of the discrete PID as a special case under the Dirac measure. These are all perturbation-robustness results.

- **Null hypothesis**: Implicit. The shared-exclusions framework defines redundancy by what target outcomes sources *jointly exclude* — i.e., which target values become impossible given source observations. The "null" against which exclusion is measured is the prior distribution over targets before any source observation.

**What is genuinely new**:
- Extension to continuous and mixed discrete-continuous random variables. Prior PID work was restricted to finite-alphabet systems. This paper uses measure-theoretic foundations (Radon-Nikodym derivatives, sigma-algebras) to define PID atoms for arbitrary probability spaces.
- The shared-exclusions approach: redundancy is defined not by what sources say about the target, but by what they jointly rule out. This is a complementary perspective to the "same information" criterion of other approaches.
- Differentiability of PID atoms w.r.t. the underlying density — a property no prior PID measure possessed, important for gradient-based estimation and sensitivity analysis.
- Target chain rule: the decomposition respects I(T1,T2 : S1,...,Sn) = I(T1 : S1,...,Sn) + I(T2 : S1,...,Sn | T1), and PID atoms compose accordingly.

**Connections the authors acknowledge**: Williams-Beer, Bertschinger et al., Harder et al., Finn-Lizier, Ince, Makkeh et al. (their own prior work on discrete shared exclusions). Rosas et al. for synergistic information via channel optimization. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| Source S_i | Component / marginal variable |
| Target T | Observable |
| Shared exclusion | Jointly ruled-out target outcomes |
| Local PID atom Pi(alpha) | Pointwise differential lattice element |
| Antichain alpha | Node in the redundancy poset |
| Radon-Nikodym derivative | Density ratio (measure-theoretic primitive) |
| Invertible transformation invariance | Reparametrization stability |
| Differentiability | Continuity of PID under distribution perturbation |
| Target chain rule | Compositional decomposition over targets |
| Dirac measure recovery | Discrete limit as special case |

**See also**: `by-structure/composite_systems.md`

---

## PID-06 — Makkeh, Theis, Vicente (2018)
**"BROJA-2PID: A Robust Estimator for Bivariate Partial Information Decomposition"**

**Domain(s)**: Information theory, optimization, scientific computing

**Abstract machines instantiated**:

- **Matching**: The entire paper is about solving the BROJA optimization problem: minimize MI(X': Y', Z') subject to fixed (X',Y') and (X',Z') marginals. This is an optimal transport / assignment problem in distribution space — find the joint distribution Q over (X,Y,Z) that minimizes mutual information while matching prescribed 2D marginals. The feasible region is a transportation polytope. The paper proves strong duality for the exponential cone program formulation, establishing that the primal (minimization over joints) and dual (maximization over Lagrange multipliers) achieve the same value.

- **Joint-vs-marginal excess**: The BROJA synergistic information CI(X;Y,Z) = I(X;Y,Z) - min_Q I_Q(X;Y,Z) is the gap between the actual joint MI and the minimum MI achievable by any distribution sharing the same pairwise marginals. This is literally the excess of the true joint over the marginal-preserving null.

- **Stability**: The paper benchmarks robustness of different numerical solvers. The exponential cone programming approach is shown to be the most robust against boundary degeneracies (where the objective is non-smooth). This is computational stability — the algorithm reliably finds the correct answer even in ill-conditioned regimes.

**What is genuinely new**:
- Production-quality software for computing BROJA PID. The theoretical contribution is proving strong duality for the exponential cone program, which guarantees that the solver finds a global optimum (not a local minimum).
- Systematic comparison of solver approaches: projected gradient descent, interior point methods, geometric programming, and exponential cone programming. The cone approach wins on robustness because the exponential cone captures the entropy objective's geometry exactly, avoiding the non-smoothness issues that plague general-purpose convex solvers at the boundary of the feasible region.
- Extension to trivariate PID quantities using the same cone programming framework.

**Connections the authors acknowledge**: Bertschinger et al. (BROJA, 2014), Williams-Beer, the COMPUTE_UI estimator of Banerjee et al., the DIT package's IBROJA estimator. Pure optimization/information-theory context. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| CI(X;Y,Z) — synergistic information | Joint-vs-marginal excess |
| SI(X;Y,Z) — shared/redundant info | Marginal content (shared across components) |
| UI(X;Y\Z) — unique information | Component-exclusive contribution |
| Marginal constraints q_{x,y,*} = b^y_{x,y} | Prescribed pairwise structure |
| Feasible region (transportation polytope) | Space of valid joint distributions |
| Exponential cone K_exp | Geometric representation of entropy constraints |
| Strong duality | Primal = dual optimal (no gap) |
| KKT conditions / complementarity | Optimality certificate |
| min_Q I_Q(X;Y,Z) | Marginal-preserving null (minimum-MI reference) |
| Cone program (CP) | Convex relaxation of matching problem |

**See also**: `by-structure/composite_systems.md`

---

## PID-07 — Makkeh, Theis, Vicente (2017)
**"Bivariate Partial Information Decomposition: The Optimization Perspective"**

**Domain(s)**: Information theory, convex optimization

**Abstract machines instantiated**:

- **Matching**: Same optimization problem as PID-06 but examined from a theoretical convex-analysis perspective. The paper characterizes the feasible region (transportation polytope defined by marginal constraints), the objective landscape (convex, smooth in the interior, non-smooth on the boundary), and the KKT optimality conditions. Finding the minimum-MI distribution is an assignment problem: match the three-way joint distribution to a target that preserves two-way marginals while minimizing dependence.

- **Joint-vs-marginal excess**: Same as PID-06 — CI is the excess MI of the true joint over the marginal-preserving minimum.

- **Stability**: Detailed analysis of why standard numerical methods fail: the objective function MI(X:Y,Z) is convex and smooth in the interior of the feasible polyhedron, but on the boundary (where some q_{x,y,z} = 0), the gradient diverges (ln(0)). This boundary non-smoothness means naive interior-point methods and gradient descent can fail to converge. The paper identifies this as a fundamental stability issue for the computation: small perturbations to the distribution near the boundary cause large changes in the gradient.

**What is genuinely new**:
- Theoretical diagnosis of WHY computing BROJA PID is hard, despite being a convex problem. The non-smoothness at the boundary of the feasible region is not just a numerical nuisance — it reflects the information-theoretic reality that deterministic relationships (zero probabilities) create singular MI landscapes.
- Explicit KKT analysis showing when the minimum is attained in the interior vs on the boundary, and how the number of zero entries in the optimal distribution determines the difficulty.
- Comparison of barrier methods, projected gradient descent, subgradient methods, and geometric programming, with theoretical explanations for the performance differences.

**Connections the authors acknowledge**: Bertschinger et al. (2014), Williams-Beer, standard convex optimization theory (Boyd-Vandenberghe, Hiriart-Urruty-Lemarechal). No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| Convex Program (CP) | Optimization formulation of joint-vs-marginal problem |
| Feasible region | Transportation polytope (marginal-constrained distributions) |
| Objective MI(X:Y,Z) | Joint dependence measure |
| Boundary non-smoothness | Singularity at deterministic limit |
| Subgradient g | Generalized derivative at non-smooth point |
| Barrier method | Interior regularization (stay away from boundary) |
| KKT conditions | First-order optimality (complementary slackness) |
| Feasible descent direction | Improving step within constraints |
| Asphericity alpha | Condition number of feasible region |
| epsilon-approximation | Approximate matching solution |

**See also**: `by-structure/composite_systems.md`

---

## PID-08 — Tian, Shamai (2025)
**"Broadcast Channel Cooperative Gain: An Operational Interpretation of Partial Information Decomposition"**

**Domain(s)**: Information theory (network information theory, broadcast channels)

**Abstract machines instantiated**:

- **Joint-vs-marginal excess**: The central result. Synergistic information I^(S)(T; X,Y) is shown to equal (or lower-bound) the cooperative gain on the corresponding broadcast channel. The cooperative gain is defined as: how much more total information can a transmitter send to two receivers when they cooperate (decode jointly) versus when they decode independently? This is a precise operational definition of "joint exceeds marginal" — the sum-rate capacity of the broadcast channel with cooperation minus the sum-rate without cooperation. The paper establishes CI_BROJA(T; X,Y) = I_P(T; X,Y) - min_Q I_Q(T; X,Y) as a lower bound on the cooperative gain.

- **Matching**: The broadcast channel capacity problem itself involves optimization over encoding/decoding strategies. The min_Q optimization in the BROJA definition is reinterpreted as finding the worst-case channel (the one that minimizes total throughput while preserving individual receiver channels). This connects the PID matching problem to the classical channel coding optimization of information theory.

- **Null hypothesis**: The marginal-preserving distribution Q that minimizes I_Q(T; X,Y) serves as the null model: it represents the "no cooperation" baseline. The synergistic information is exactly the excess over this null. The non-cooperative broadcast channel (independent decoding at each receiver) is the reference against which cooperative gain is measured.

- **Parameterized homology**: Implicit but present. The broadcast channel capacity region is a two-dimensional set (rate pairs (R1, R2) achievable by the channel). As the signaling distribution P_T varies, the capacity region deforms. The sum-rate capacity is a single scalar extracted from this parameterized family. The cooperative gain tracks how this scalar changes when the constraint of independent decoding is relaxed — analogous to tracking how a topological invariant changes when a filtration parameter crosses a threshold.

**What is genuinely new**:
- The first rigorous operational interpretation of BROJA PID in terms of a classical information-theoretic quantity (broadcast channel capacity). Prior justifications were axiomatic or qualitative (decision-making intuitions in Bertschinger et al.). This paper shows synergy = cooperative gain, connecting PID to a quantity that communication engineers have studied for decades.
- The broadcast channel mapping: T is the channel input (transmitter), X and Y are channel outputs (receivers). The PID question "how is information about T distributed between X and Y?" becomes the channel coding question "how should T encode messages for X and Y?"
- The distinction between cooperative gain under a fixed signaling distribution vs optimized over all distributions. The BROJA synergy equals the gain under the true P_T, but may only lower-bound the gain when optimizing over all input distributions.
- Connection to Marton's inner bound and the general broadcast channel capacity problem (still open after 50+ years).

**Connections the authors acknowledge**: Bertschinger et al. (BROJA, 2014), Williams-Beer, Cover (1972, broadcast channel), Marton (1979), El Gamal-Kim (textbook). Applications in neural signal processing and multi-modality machine learning. This paper is the most "network information theory aware" of all the PID papers. No connections to TDA, QEC, or dynamical systems — but the broadcast channel IS a composite system with two outputs, making the structural parallel to entanglement (two subsystems) and binding (two brain regions) very tight.

**Vocabulary mapping**:

| Paper term | Rosetta term |
|---|---|
| Broadcast channel P_{X,Y\|T} | Composite system with shared input |
| Transmitter T | Source / joint system |
| Receivers X, Y | Components / marginals |
| Sum-rate capacity | Total throughput of composite |
| Independent decoding | Marginal processing (no cooperation) |
| Cooperative decoding | Joint processing |
| Cooperative gain | Joint-vs-marginal excess (operational) |
| BROJA synergy I^(S) | Lower bound on cooperative gain |
| Fixed signaling distribution P_T | Given input statistics (not optimized) |
| Capacity region {(R1,R2)} | Parameterized achievable-rate set |
| Marton's inner bound | Best known achievable region |
| Q in Q | Marginal-preserving null distribution |
| Non-cooperative channel | Null model (independent receivers) |

**See also**: `by-structure/composite_systems.md`

---

## PID — Cross-cutting observations

### The PID lattice IS a chain complex (almost)

The redundancy lattice in all 8 papers has the same algebraic structure: a graded poset with Mobius inversion that recovers differential atoms from cumulative quantities. This is structurally identical to computing homology via the boundary operator. The key difference: in a true chain complex, the boundary-of-a-boundary is zero (d^2 = 0). In the PID lattice, the analogue would be that the "second Mobius inversion" vanishes — and it does, trivially, because the Mobius inversion is its own inverse on the incidence algebra. So the PID lattice satisfies a d^2 = 0 analogue, but it is a lattice-theoretic identity rather than a geometric one.

### Synergy IS joint-vs-marginal excess

Every paper in this set instantiates the joint-vs-marginal machine. Synergy = CI = I^(S) is the information present in the composite (X,Y) that is absent from the components X and Y individually. This is structurally identical to:
- **Entanglement** (QEC): the quantum state of (A,B) has correlations absent from rho_A and rho_B.
- **Binding** (neuroscience/TDA): the joint point cloud has topological features absent from marginal projections.
- **Emergent dynamics** (dynamical systems): the coupled system has attractors not present in uncoupled components.

### The marginal-preserving minimum is a null model

The BROJA definition CI = I_joint - min_Q I_Q (where Q preserves pairwise marginals) is precisely a null-model construction: destroy the three-way dependence while preserving all pairwise structure, then measure the residual. This parallels:
- **Surrogate testing** in TDA: destroy phase coupling, preserve power spectra.
- **Depolarizing channel** in QEC: destroy coherence, preserve state-space dimension.
- **Shuffle surrogates** in neuroscience: destroy temporal structure, preserve firing rates.

### Stability is the PID community's weak spot

Unlike TDA (which has the stability theorem) or QEC (which has the threshold theorem), PID has no general stability result. Papers PID-05 and PID-07 make partial progress (differentiability, convexity), but there is no PID analogue of "small perturbation to the joint distribution yields bounded perturbation to all PID atoms." This is an open problem with clear structural parallels to the bottleneck stability theorem.

---

## 2506.16215 — Kirkley (2025)
**"Transfer entropy for finite data"**
arXiv: 2506.16215

**Domain(s)**: Information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Transfer entropy is defined as T_{x→y} = H_S(y⁺|Y⁻) − H_S(y⁺|Z⁻), measuring how much the joint (past-of-x, past-of-y) predicts future-of-y beyond the marginal (past-of-y alone). The reduced transfer entropy R_{x→y} replaces Shannon conditional entropies with combinatorial conditional entropies H_C, but preserves exactly this joint-vs-marginal structure. The paper's central contribution is making this excess quantity exactly zero when no genuine directional coupling exists, rather than always positive due to finite-sample bias.
- **Null hypothesis**: The MDL (Minimum Description Length) principle provides an automatic null model. When the combinatorial cost of encoding the contingency table structure (log Ω/N) exceeds the compression gain, the reduced transfer entropy is exactly zero — no permutation testing or significance threshold needed. This replaces simulation-based surrogates with an analytic null: the model complexity cost acts as an intrinsic penalty that destroys spurious structure. The paper explicitly contrasts this with standard surrogate-based null models requiring computationally expensive permutation testing.
- **Stability**: The asymptotic equivalence H_C ≈ H_S (via Stirling approximation) establishes that the reduced measure converges to the standard plug-in estimator as N → ∞ with fixed cardinality C. The finite-sample correction term log Ω/N quantifies the instability of the standard estimator — it is a stability gap that vanishes in the large-data limit but dominates for small N. The measure is thus stable under the perturbation of increasing data size.

**What is genuinely new (not reducible to shared abstraction)**:
- The combinatorial (population-based) reinterpretation of entropy avoids treating time series as realizations of random variables. The data IS the population, not a sample from one. This ontological shift has no direct analogue in TDA or QEC where data is always assumed to sample from some underlying space.
- Automatic lag selection via MDL model comparison across (k,l) pairs, integrated into the significance framework at no additional computational cost.
- The coding-theoretic construction (Alice-Bob transmission scenario) gives the combinatorial entropy an operational interpretation distinct from Shannon's axiomatic derivation. The sender-receiver framing makes the null model emerge naturally from compression theory.

**Connections the authors acknowledge**: Transfer entropy as nonlinear alternative to Granger causality (Schreiber 2000, Granger 1969). MDL principle (Rissanen). Lempel-Ziv complexity estimators. No connections to TDA, QEC, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transfer entropy T_{x→y} | Joint-vs-marginal excess (conditional MI) |
| Reduced transfer entropy R_{x→y} | Debiased joint-vs-marginal excess |
| Combinatorial conditional entropy H_C | Information content of finite population |
| Contingency table n^{(w,V)} | Joint empirical distribution |
| MDL significance test | Analytic null model (complexity as penalty) |
| Delay embedding vectors x_t^{(-k)} | State space reconstruction (cf. Takens embedding) |
| Permutation test / surrogate | Simulation-based null model |
| Lag parameters (k, l) | Scale parameter (temporal embedding dimension) |
| Positivity bias | False positive excess (finite-sample artifact) |
| Stirling asymptotic equivalence | Stability convergence (H_C → H_S) |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

## 1912.07277 — Zhang, Simeone, Cvetkovic, Abela, Richardson (2020)
**"ITENE: Intrinsic Transfer Entropy Neural Estimator"**
arXiv: 1912.07277

**Domain(s)**: Information theory, neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Standard TE measures I(X_{t-m}^{t-1}; Y_t | Y_{t-n}^{t-1}), the excess predictability from joint (past-X, past-Y) over marginal (past-Y). TE over-counts because it includes synergistic information — information about Y_t extractable from past-X only if observed jointly with past-Y, not from past-X alone. The Intrinsic TE (ITE) explicitly subtracts this synergistic excess, yielding only the intrinsic (non-synergistic) directional flow. This is a refinement of the joint-vs-marginal decomposition into intrinsic vs. synergistic components.
- **Matching**: The ITE computation involves an infimum over auxiliary random variables U that mediate the information flow. The MINE-based neural estimator solves this optimization via variational bounds on KL divergence with two-sample neural classifiers and the pathwise (reparameterization trick) gradient estimator. This is an assignment problem: find the optimal auxiliary variable that captures exactly the intrinsic information channel from X to Y.
- **Null hypothesis**: Conditioning on past-Y in the TE definition is a partial null: it removes the predictability that Y's own past provides. The ITE goes further by constructing a tighter null that also removes synergistic contributions. The intrinsic MI I_↓(X;Y|Z) is defined as the infimum over distributions Q that preserve marginals — the optimization over Q is a structured null construction where the null family consists of all distributions consistent with pairwise marginals.

**What is genuinely new (not reducible to shared abstraction)**:
- The private key agreement formulation of intrinsic information (from cryptography, via Maurer and Wolf) is imported into the causal inference setting. "Intrinsic" means "extractable without the help of the conditioning variable" — this cryptographic notion has no analogue in TDA or QEC.
- Neural estimation of a quantity defined by an infimum over conditional distributions, combining variational MI bounds with the reparameterization trick.
- The explicit distinction between synergistic and intrinsic information flow directly connects to PID (Partial Information Decomposition), bridging causal inference and information decomposition.

**Connections the authors acknowledge**: Granger causality, directed information, private key agreement (Maurer-Wolf), MINE framework (Belghazi et al.). Neuroscience motivation (neural and gene-regulatory networks). No connections to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transfer entropy TE_{X→Y} | Joint-vs-marginal excess (conditional MI) |
| Intrinsic transfer entropy ITE | Refined excess (synergy-free directional flow) |
| Synergistic information | Joint structure not decomposable to components |
| Directed information DI | Causal rate (cumulative per-step excess) |
| Auxiliary variable U | Mediating assignment variable |
| Variational bound on KL | Approximate matching (neural optimization) |
| Memory parameters (m, n) | Lag / embedding dimension |
| MINE classifier | Neural density ratio estimator |
| Private key agreement rate | Intrinsic capacity (cryptographic origin) |

**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`

---

## 2002.00208 — Amornbunchornvej, Zheleva, Berger-Wolf (2020)
**"Variable-lag Granger Causality and Transfer Entropy for Time Series Analysis"**
arXiv: 2002.00208

**Domain(s)**: Information theory, dynamical systems

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Variable-lag Granger causality generalizes the standard excess: X Granger-causes Y if including past-X (at variable, DTW-aligned delays) improves prediction of Y beyond past-Y alone. The variable-lag transfer entropy is I(X_{t-m}^{t-1}; Y_{φ(t)} | Y_{φ(t)-n}^{φ(t)-1}), where φ is an optimal warping function. The excess is computed after temporally aligning the causal influence, generalizing the fixed-lag assumption.
- **Matching**: Dynamic Time Warping (DTW) is explicitly an optimal assignment: it finds the minimum-cost alignment (warping path) between two time series under monotonicity and continuity constraints. The DTW distance serves as both the matching cost and the quality measure for the causal relation. The paper proves that fixed-lag causality is a special case where the warping path is the diagonal — rigid matching as a special case of flexible matching.
- **Stability**: The paper proves that traditional fixed-lag Granger causality and transfer entropy are special cases of their variable-lag generalizations (warping path restricted to fixed offset). This establishes that the generalization is conservative: it reduces to the standard measure under the constraint of constant delay.

**What is genuinely new (not reducible to shared abstraction)**:
- The integration of DTW (a metric geometry / time series distance tool) with Granger causality. DTW's warping path φ(t) allows causes to influence effects at dynamically changing delays. This temporal deformation is more akin to reparameterization in differential geometry than to any of the six abstract machines.
- The aggregate causal relation theorem: if multiple time series jointly initiate behavioral convergence, the aggregate cause-effect relation holds. This is a compositionality result with no direct analogue in TDA.
- Application to collective movement (inferring leaders in animal groups) and financial markets introduces spatial-temporal causality beyond standard time series.

**Connections the authors acknowledge**: Granger causality, transfer entropy, DTW clustering methods, directed information graphs. No connections to TDA, QEC, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Variable-lag Granger causality | Temporally warped joint-vs-marginal excess |
| DTW optimal warping path | Optimal matching (between time indices) |
| Warping distance | Matching cost |
| Fixed-lag causality | Rigid matching (diagonal warping path) |
| BIC-based lag selection | Model selection (parameter for excess computation) |
| Causal initiator | Source node in directed coupling |
| Aggregate cause | Composite component in joint-vs-marginal |
| VLTimeCausality R package | Implementation |

**See also**: `by-structure/composite_systems.md`, `by-structure/optimal_transport.md`

---

## 0803.2881 — Marinazzo, Pellicoro, Stramaglia (2008)
**"Kernel Granger causality and the analysis of dynamical networks"**
arXiv: 0803.2881

**Domain(s)**: Dynamical systems, information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Granger causality index δ = 1 − ⟨E'²⟩/⟨E²⟩ measures the fractional variance reduction when the joint model (including η's past) is used vs. the marginal model (only ξ's past). The kernel extension preserves this structure but lifts it into a reproducing kernel Hilbert space (RKHS), making the excess nonlinear. The geometric interpretation: δ = ||P⊥y||²/(1 − x̃ᵀx̃), where P⊥ projects onto the "additional features" subspace — the residual after removing the marginal model's contribution.
- **Null hypothesis**: Bonferroni correction on eigenvector correlations provides explicit false-positive control. The filtered causality index δ_F sums only over eigenvectors whose correlation with the residual y passes a significance threshold (π_{i'} < q/m). The entire eigenvector selection strategy is a method for distinguishing signal from null at controlled false discovery rate.
- **Stability**: The kernel function controls model nonlinearity; varying the bandwidth parametrically varies complexity. For limited data, bivariate GC (simpler model) is more stable than L1-minimization (complex model), demonstrating a bias-variance tradeoff as a form of stability analysis. The method works from purely observational data without system perturbation.
- **Parameterized homology**: The inferred network topology changes as a function of available samples N. Short recordings yield partial topology; longer recordings reveal full connectivity. This is a parameterized family of inferred networks indexed by sample size.

**What is genuinely new (not reducible to shared abstraction)**:
- The geometric interpretation of GC via Hilbert space projection. The reduced Gram matrix K̃ = K' − PK' − K'P + PK'P whose eigenvectors span the "additional features" subspace H⊥ isolates exactly the nonlinear causal contribution. This kernel-space construction has no direct TDA or QEC analogue.
- Application to gene regulatory network reconstruction from HeLa cell expression data, identifying 19 causal relationships all involving tumor-related genes.
- The bridge between kernel methods (RKHS embedding) and causal inference — kernels control the nonlinearity of the causal model rather than just serving as similarity measures.

**Connections the authors acknowledge**: Linear Granger causality (Granger 1969), kernel methods (Schölkopf), dynamical network synchronization, L1 minimization for sparse networks. No connections to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Granger causality index δ | Joint-vs-marginal excess (variance ratio) |
| Filtered index δ_F | Significance-controlled excess |
| Kernel function K(x,y) | Nonlinear embedding (cf. feature map in TDA) |
| RKHS embedding | Hilbert space representation |
| Reduced Gram matrix K̃ | Residual structure after marginal removal |
| Eigenvector selection + Bonferroni | Null hypothesis with multiple comparison correction |
| Network topology | Graph structure (adjacency matrix) |
| Dynamical network | Coupled system (joint-vs-marginal setting) |
| F-test / Levene's test | Significance test for excess |
| Preferential attachment network | Synthetic null topology |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

## 1911.09879 — Khanna, Tan (2020)
**"Economy Statistical Recurrent Units For Inferring Nonlinear Granger Causality"**
arXiv: 1911.09879 | ICLR 2020

**Domain(s)**: Information theory, dynamical systems

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The component-wise autoregressive model x_{t,i} = f_i(x_{t-p:t-1,1}, ..., x_{t-p:t-1,n}) + e_{t,i} defines Granger causality through the dependence of f_i on each component's past. Series j does not Granger-cause series i if f_i is constant in x_{t-p:t-1,j}. The excess is whether including series j's past improves prediction of series i beyond what all other series provide.
- **Null hypothesis**: Group-wise L1 regularization on the input weight matrix serves as a structured null model. When the penalty drives the input weights for series j to exactly zero, the model declares no Granger-causal relationship from j to i. The sparsity pattern of the learned weight matrix IS the null hypothesis decision: zero weights = null, nonzero weights = alternative. The causal sufficiency assumption (no unobserved confounders) is itself a structural null assumption about the system.
- **Matching**: The random projection mechanism maps the high-dimensional hidden state h_t to a low-dimensional sketch via a fixed random matrix Φ. This is a dimensionality-reducing assignment that preserves information (via Johnson-Lindenstrauss-type guarantees). Group-wise regularization then selects which input-to-hidden pathways carry genuine causal signal — sparse matching between inputs and predictive features.

**What is genuinely new (not reducible to shared abstraction)**:
- The economy-SRU architecture: random projections reduce hidden state dimensionality while maintaining the universal approximation property. The SRU's lack of sigmoid gating (unlike LSTM/GRU) makes parameters directly interpretable as causal weights — structural transparency enables topology readoff from weight matrices.
- Group-wise regularization producing "time-localized causal features": sparsity structured both across input dimensions and across time lags, mimicking the temporal locality of real causal events.
- The insight that architectural design choices (gating vs. no gating, random projections vs. full recurrence) directly affect the identifiability of causal structure from learned parameters.

**Connections the authors acknowledge**: Tank et al. (sparse-input NNs for GC), Oliva et al. (SRU architecture), linear VAR models, gene regulatory networks (Fujita), brain connectome (Seth). No connections to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Granger causality | Joint-vs-marginal excess (predictive improvement) |
| Component-wise generative function f_i | Local dynamics (cf. flow equation) |
| Granger noncausality | Null hypothesis (no excess from component j) |
| Sparse input weight matrix | Adjacency structure of causal graph |
| Group-wise L1 penalty | Null model enforcement (sparsity = no coupling) |
| Random projection Φ | Dimensionality-reducing embedding |
| Economy-SRU hidden state | Latent representation (state space) |
| Causal sufficiency | Completeness assumption (no hidden confounders) |
| Network topology | Graph structure |
| Prediction residual e_{t,i} | Unexplained variance |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

## 2101.07600 — Marcinkevics, Vogt (2021)
**"Interpretable Models for Granger Causality Using Self-explaining Neural Networks"**
arXiv: 2101.07600 | ICLR 2021

**Domain(s)**: Information theory, dynamical systems

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: GVAR defines x^i_t = g_i(x^1_{1:(t-1)}, ..., x^p_{1:(t-1)}) + ε^i_t. Granger causality x^j → x^i holds when g_i depends on x^j's past. The self-explaining structure makes this excess interpretable through generalised coefficients β^{ij}(x_t) that reveal magnitude, sign, and temporal variation of each causal contribution.
- **Stability**: Stability-based selection is a core methodological component. Spurious associations are mitigated by finding relationships stable across original and time-reversed time series. The time-reversal trick acts as a perturbation: real causal relationships survive reversal of temporal ordering, while spurious correlations do not. This is directly a stability criterion — the causal graph should be robust under time-reversal perturbation.
- **Null hypothesis**: The sparsity-inducing penalty enforces a default of no Granger-causal relationship (zero generalised coefficient); the model must overcome the penalty to assert causality. The time-reversal stability check provides a second null model: relationships present only in forward time but absent after reversal are rejected as artifacts.
- **Parameterized homology**: The generalised coefficients β^{ij}(x_t) vary as functions of time t and input state x_t. Plotting these over time reveals how causal structure evolves — positive/negative/absent interactions change dynamically. This is a parameterized family of causal graphs indexed by time, analogous to tracking topology changes as a parameter varies.

**What is genuinely new (not reducible to shared abstraction)**:
- The self-explaining neural network formulation produces generalised coefficients that decompose nonlinear prediction into interpretable, time-varying contributions from each input variable. Unlike sparse-input methods that only detect presence/absence, GVAR reveals sign and magnitude at each time step.
- Effect sign detection: distinguishing inhibitory (negative) from excitatory (positive) Granger-causal effects. Signed directionality has no direct analogue in the six abstract machines (which are unsigned). It connects naturally to excitatory/inhibitory synapses in neuroscience.
- The time-reversal stability trick exploits causal asymmetry (time's arrow) as a filter — real causation is directional, so relationships equally strong in reversed time are likely spurious.

**Connections the authors acknowledge**: Tank et al. (cMLP, cLSTM), Khanna & Tan (eSRU), Nauta et al. (TCDF), Alvarez-Melis & Jaakkola (self-explaining NNs), Meinshausen & Buhlmann (stability selection). Applications to gene regulatory networks, metabolomics. No connections to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Granger causality | Joint-vs-marginal excess |
| Generalised coefficient β^{ij}(x_t) | Time-varying excess weight |
| Summary graph G = (V, E) | Causal graph (adjacency structure) |
| Effect sign (positive/negative) | Signed coupling (excitatory/inhibitory) |
| Self-explaining neural network | Interpretable nonlinear model |
| Sparsity-inducing penalty | Null model enforcement |
| Time-reversal stability | Perturbation robustness test (stability) |
| GVAR model | Nonlinear VAR with interpretable structure |
| Adjacency matrix A | Causal topology |
| Time-smoothing penalty | Temporal regularity constraint |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

## 10.1371/journal.pone.0087636 — Zhou, Xiao, Zhang, Xu, Cai (2014)
**"Granger Causality Network Reconstruction of Conductance-Based Integrate-and-Fire Neuronal Systems"**
DOI: 10.1371/journal.pone.0087636

**Domain(s)**: Neuroscience, dynamical systems, information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: GC measures whether including neuron j's voltage history improves prediction of neuron i's voltage beyond neuron i's own past. The causality index δ = 1 − ⟨E'²⟩/⟨E²⟩ is the standard variance-ratio excess. The key result GC ∝ S² (GC quadratically related to synaptic coupling strength S) establishes a quantitative mapping from the information-theoretic excess to the physical coupling parameter.
- **Stability**: The reconstruction is "insensitive to dynamical regimes" — it works across tonic firing, bursting, and irregular spiking. This is a strong stability result: the GC-to-connectivity mapping is robust under changes in the dynamical regime (itself a bifurcation parameter). The method also works from purely observational data without system perturbation.
- **Null hypothesis**: The method works from both voltage traces AND spike rasters (binary time series). The spike raster is a severe information reduction — a null-like destruction of subthreshold dynamics — yet connectivity reconstruction still succeeds. The statistical steady state requirement ensures the null (stationary dynamics) is well-defined.
- **Parameterized homology**: The reconstructed network changes as a function of available data length and coupling strength S. Short recordings yield partial topology; longer recordings reveal full connectivity. The coupling strength S modulates how easily each connection is detected — an intrinsic parameter governing the structure-to-function mapping.

**What is genuinely new (not reducible to shared abstraction)**:
- The quantitative mapping GC ∝ S² between information-theoretic (functional) connectivity and physical (structural) connectivity. This structure-function bridging theorem is specific to conductance-based I&F dynamics and is not reducible to any of the six machines.
- The spike-triggered correlation (STC) analysis on voltage residuals (whitened signals) provides the theoretical bridge. STC on raw voltages fails (due to finite autocorrelation), but STC on regression residuals succeeds — whitening is essential. This residual-based approach is specific to the I&F model.
- Application to mixed excitatory/inhibitory networks demonstrating resolution of signed connectivity.

**Connections the authors acknowledge**: Wiener-Granger causality, Marinazzo (kernel GC), dynamic Bayesian inference, functional vs. structural connectivity debate in systems neuroscience. No connections to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| GC connectivity | Functional excess (joint-vs-marginal) |
| Synaptic connectivity | Structural coupling (ground truth) |
| Coupling strength S | Physical parameter (cf. bifurcation parameter) |
| GC ∝ S² | Structure-function mapping (quadratic) |
| Conductance-based I&F model | Dynamical system (neural) |
| Spike raster | Reduced observation (binary time series) |
| Voltage time series | Full state observation |
| Spike-triggered correlation | Cross-correlation at causal events |
| Regression residuals (whitened) | Null-removed signal |
| Adjacency matrix | Network topology |
| Dynamical regime (tonic/bursting) | Phase of dynamical system |
| Excitatory/inhibitory | Signed coupling |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`, `by-domain/neuroscience.md`

---

## 10.3390/e19090494 — Wibral, Finn, Wollstadt, Lizier, Priesemann (2017)
**"Quantifying Information Modification in Developing Neural Networks via Partial Information Decomposition"**
DOI: 10.3390/e19090494

**Domain(s)**: Neuroscience, information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The entire PID framework decomposes joint MI I(Y : X₁, X₂) into unique, shared, and synergistic contributions. Synergistic information I_syn is the quintessential joint-vs-marginal excess: information about output Y obtainable ONLY by observing BOTH inputs X₁ AND X₂ together, absent from either marginal I(Y : X₁) or I(Y : X₂). The paper's central quantity — information modification — IS the synergistic component.
- **Null hypothesis**: The BROJA measure defines synergy via optimization over distributions Q ∈ Δ_P preserving marginals p(X₁, Y) and p(X₂, Y). The set Δ_P is a structured null: all distributions consistent with pairwise marginals. Synergy is the excess of true joint MI over the maximum achievable under this null. Assumption (**) explicitly requires that synergy cannot be deduced from marginal distributions alone — it is defined as the gap between joint and null.
- **Parameterized homology**: The developmental trajectory of information modification is tracked as the neural culture matures over days in vitro (DIV). The parameter is developmental time. The information-processing topology (synergy vs. redundancy dominance) undergoes a qualitative transition: synergy rises during maturation then collapses as redundancy dominates. This is a phase transition in information-processing structure indexed by developmental stage.

**What is genuinely new (not reducible to shared abstraction)**:
- The identification of information modification (synergy) with neural computation: "the purpose of dendritic connections is not to simply relay information but to modify it." This conceptual contribution links information decomposition to a theory of neural computation.
- The developmental trajectory finding: synergy rises then falls in self-organizing neural cultures. The collapse of modification and dominance of redundancy in the absence of structured external inputs suggests complex information processing requires environmental interaction.
- The distinction between information transfer, storage, and modification as three fundamental computations (dating to Turing), with PID finally providing a formal measure for the third.
- Application of PID with the BROJA measure to real neural data (cultures in vitro), demonstrating biologically meaningful results from the abstract decomposition.

**Connections the authors acknowledge**: Williams & Beer (PID), Bertschinger/Rauh/Olbrich/Jost/Ay (BROJA), Griffith & Koch, Lizier (TE, active information storage), Schreiber (TE). No connections to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Partial information decomposition (PID) | Joint-vs-marginal decomposition |
| Synergistic mutual information I_syn | Joint-vs-marginal excess (pure synergy) |
| Unique mutual information I_unq | Marginal-specific information |
| Shared (redundant) mutual information I_shd | Common structure across components |
| Information modification | Synergistic computation (excess from joint processing) |
| BROJA measure | Optimal-transport-based decomposition |
| Δ_P (compatible distribution set) | Null model family (preserve marginals) |
| Days in vitro (DIV) | Parameterization (developmental time) |
| Neural culture | Self-organizing dynamical system |
| Transfer entropy | Directed joint-vs-marginal excess |
| Active information storage | Temporal self-information |
| Assumption (**) | Non-deducibility from marginals (structural constraint) |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`, `by-domain/neuroscience.md`

---

## 2111.05299 — Venkatesh, Dutta, Mehta, Grover (2021)
**"Can Information Flows Suggest Targets for Interventions in Neural Circuits?"**
arXiv: 2111.05299

**Domain(s)**: Information theory, neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: M-information flow quantifies how much information about a specific message flows through each edge of a network. The flow on edge (i,j) measures the excess information the edge carries about the message beyond what is available without that edge. The distinction between "desirable" (accuracy) and "undesirable" (bias) flows is a decomposition of total joint-vs-marginal excess into two competing messages.
- **Null hypothesis**: Edge pruning is an explicit intervention testing a causal null: "does removing this edge change the output?" Random pruning is the unstructured null; bias-flow-guided pruning is a structured null that selectively destroys the undesirable information pathway. The key finding — edges with larger M-information flow about the protected attribute produce larger bias reductions when pruned — validates the flow measure as a predictor of interventional effects.
- **Matching**: Comparison of pruning strategies involves matching edges to flow magnitudes and selecting the optimal subset to prune. The bias-accuracy tradeoff is an assignment problem: which edges to intervene on to maximize fairness while minimizing accuracy loss.

**What is genuinely new (not reducible to shared abstraction)**:
- The bridge between observational information flow measurement and causal intervention. The central question — can passive measurement predict the effect of active intervention? — connects information theory to causal inference (Pearl's do-calculus territory). The affirmative answer is non-trivial and is not reducible to the abstract machines.
- Multi-message information flow: tracking two different messages (accuracy and bias) simultaneously through the same network. The bias-accuracy tradeoff frontier is a novel object not present in single-message information theory.
- The explicit analogy between fairness in ML and neural circuit intervention for clinical applications (deep-brain stimulation for depression/addiction) — a rare paper deliberately bridging ML and neuroscience through a shared formal framework.
- Using ANNs as proxies for biological circuits when simultaneous multi-area recordings are unavailable.

**Connections the authors acknowledge**: Explainability literature (SHAP, LIME), lottery ticket hypothesis, information-theoretic fairness. Neuroscience motivation (reward circuits, deep-brain stimulation). The authors explicitly frame fairness-in-ML as an analogy for neuroscientific intervention. No connections to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| M-information flow | Directed joint-vs-marginal excess (per-edge) |
| Protected attribute | Undesirable message (bias source) |
| True label | Desirable message (accuracy source) |
| Edge pruning | Intervention (structured null — remove coupling) |
| Random pruning | Unstructured null model |
| Bias-accuracy tradeoff | Competing excess quantities |
| Reward circuit | Biological network (neural) |
| Deep-brain stimulation | Physical intervention (analogous to pruning) |
| ANN layers | Processing stages |
| Information flow magnitude | Coupling strength (edge weight) |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`, `by-domain/neuroscience.md`

---

## Cross-listed from Neuroscience + TDA

- **Peek, Pritam, Skerritt, Chalup (2025)** — "Time Series Analysis of Spiking Neural Systems via Transfer Entropy and Directed Persistent Homology." Transfer entropy as the information-theoretic measure driving directed flag complex construction. TE quantifies directed information flow between neuron pairs. Full annotation: `inbox.md` (arXiv: 2508.19048). Machines: chain complex, parameterized homology, null hypothesis.

---

## Cross-listed from Second Pass + Bridges

### Information Bottleneck Cluster

- **Shwartz-Ziv & Tishby (2017)** — "Opening the Black Box of Deep Neural Networks via Information." The original information plane paper. Two-phase training (fitting + compression). SGD noise as null-model mechanism. Full annotation: `second_pass.md` (SP-01). Machines: parameterized homology, joint-vs-marginal, null hypothesis, stability.

- **Kawaguchi, Deng, Ji, Huang (2023)** — "How Does Information Bottleneck Help Deep Learning?" First rigorous proof IB controls generalization. Bound sqrt(I(X;Z)/n) has same form as PH stability. Full annotation: `cross_domain_bridges.md` + `second_pass.md` (SP-02). Machines: stability, joint-vs-marginal, parameterized homology.

- **Yu, Yu, Løkse, Jenssen, Principe (2024)** — "Cauchy-Schwarz Divergence Information Bottleneck for Regression." CS divergence makes IB tractable without Gaussian assumptions. Closed-form compression + adversarial robustness. Full annotation: `second_pass.md` (SP-03). Machines: joint-vs-marginal, stability, null hypothesis.

- **Wang, Jian, Masoomi, Ioannidis, Dy (2021)** — "Revisiting HSIC Bottleneck for Adversarial Robustness." Proves HSIC bottleneck implies adversarial robustness. Layer-wise Lipschitz bounds. Full annotation: `second_pass.md` (SP-04). Machines: stability, chain complex (weak), joint-vs-marginal.

- **Ma, Lewis, Kleijn (2020)** — "The HSIC Bottleneck: Deep Learning without Back-Propagation." Kernel independence replaces MI for IB. Stability by layer-wise decoupling. Emergent discrete structure. Full annotation: `cross_domain_bridges.md`. Machines: joint-vs-marginal, null hypothesis, stability, chain complex (weak).

### Entropy Dynamics

- **Garbaczewski (2005)** — "Differential entropy and time." Three entropy notions (Shannon, KL, von Neumann) on same system reveal different dynamics. Fisher information as power transfer. H-theorem as Lyapunov stability. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, joint-vs-marginal, stability, null hypothesis. **Bridge: info theory + dynamical systems + QEC.**

- **Darmon (2018)** — "Specific Differential Entropy Rate Estimation." Lifts entropy rate from scalar to function on state space — structurally parallel to lifting Betti numbers to persistence diagrams. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, joint-vs-marginal, null hypothesis. **Bridge: info theory + dynamical systems.**

### Factor Graphs + Decomposition

- **Amizadeh, Matusevych, Weimer (2019)** — "PDP: A General Neural Framework for Learning CSP Solvers." Factor graph message passing as proto-chain complex. Neural search strategy beyond greedy decimation. Full annotation: `second_pass.md` (SP-10). Machines: chain complex, matching, null hypothesis.

- **Oladyshkin et al. (2023)** — "Deep Arbitrary Polynomial Chaos Neural Network." Polynomial chaos expansion = orthogonal decomposition of neural signals. kth-order terms = joint excess beyond lower orders. Parallel to Hodge decomposition. Full annotation: `cross_domain_bridges.md`. Machines: chain complex, joint-vs-marginal, null hypothesis, stability.

### Other

- **Napolitano (2026)** — "Fiber Bundles in LLMs (gl(4,R) Lie Algebra)." Dark Casimir dimensions hidden by layer norm carry computation. Cross-architecture transfer as stability. **Preprint — extraordinary claims, requires verification.** Full annotation: `second_pass.md` (SP-11). Machines: chain complex, joint-vs-marginal, parameterized homology, stability.

- **Liu et al. (2023)** — "FOCAL: Factorized Orthogonal Latent Space for Multimodal Time Series." Shared vs private feature decomposition = explicit joint-vs-marginal operationalization. Full annotation: `second_pass.md` (SP-16). Machines: joint-vs-marginal, null hypothesis, stability.

- **Liu et al. (2020)** — "SNGP: Distance Awareness for Uncertainty." Spectral normalization = Lipschitz constraint identical to PH stability. GP posterior = distance from training manifold. Full annotation: `cross_domain_bridges.md` + `second_pass.md` (SP-17). Machines: stability, null hypothesis, parameterized homology.

---

## Wave 2 (2026-04-06) — Thin Cell Papers

### Baudot & Bennequin (2015) — The Homological Nature of Entropy
**"The Homological Nature of Entropy"**
MDPI Entropy 17(5):3253
Shannon entropy = cocycle in information cohomology. Chain rule = cocycle condition. Information structures as simplicial complexes. Foundational Chain×Info paper.
**Machines**: chain complex, parameterized homology (weak). **See also**: `by-structure/boundary_operators.md`.

### Bradley (2021) — Entropy as Topological Operad Derivation
**"Entropy as a Topological Operad Derivation"**
arXiv: 2107.09581
Shannon entropy = unique derivation of simplicial operad. Strengthens Baudot-Bennequin. Category-theoretic.
**Machines**: chain complex. **See also**: `by-structure/boundary_operators.md`.

### Kolchinsky (2024) — PID Redundancy as Information Bottleneck
**"Partial information decomposition: redundancy as information bottleneck"**
arXiv: 2405.07665
PID redundancy = IB compression-prediction tradeoff. RB curve as parameterized decomposition. Formally bridges Joint (PID) and Param (IB) machines.
**Machines**: joint-vs-marginal, parameterized homology, matching. **See also**: `by-structure/composite_systems.md`, `by-structure/filtrations.md`.

### Schreiber (2000) — Measuring Information Transfer (Transfer Entropy)
**"Measuring information transfer"**
PRL 85:461
Transfer entropy T_{Y→X} = conditional MI measuring directed information flow. Asymmetric (unlike MI). Non-parametric (unlike Granger). Shuffled surrogates as null. Defined on state-space reconstructions (Takens link).
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology (weak). **See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`. **Bridge: info theory + dynamical systems.**

### Wong & Yang (2019) — Info Geometry Embeds in Optimal Transport
**"Pseudo-Riemannian geometry embeds information geometry in optimal transport"**
arXiv: 1906.00030
Fisher metric / Bregman divergence EMBEDS into Wasserstein via pseudo-Riemannian framework. MTW condition ↔ info-geometric curvature. Exact functorial embedding.
**Machines**: matching, stability. **See also**: `by-structure/optimal_transport.md`.

---

## Third Pass (2026-04-05)

### Graphical Mutual Information Maximization (Peng et al. 2020)
**Domain(s)**: Information theory, machine learning
GMI generalizes MI to graph-structured data: separate node-level (0-cell) and edge-level (1-cell) MI terms. Isomorphism invariant (stability under graph relabeling). Graded information measure — one MI per topological dimension.
**Machines**: joint-vs-marginal, stability, null hypothesis, chain complex (weak).
Full annotation: `third_pass_infotheo_cross.md` (TP-02).
**See also**: `by-structure/composite_systems.md`

### On Finite-Time Mutual Information (Zhu et al. 2024)
**Domain(s)**: Information theory (communication theory)
MI I(t) as function of observation window duration t. Discovers "exceed-average phenomenon": instantaneous rate can exceed time-averaged rate C. Shannon capacity recovered as stable infinite-time limit. Mercer expansion connects to functional analysis.
**Machines**: parameterized homology, stability, null hypothesis.
Full annotation: `third_pass_infotheo_cross.md` (TP-03).
**See also**: `by-structure/filtrations.md`

### Multivariate Redundancy via Max Entropy (Chicharro 2017)
**Domain(s)**: Information theory (neuroscience adjacent)
Rooted-tree decomposition of MI separating redundant, unique, synergistic atoms. Maximum entropy as null at each level. Distinguishes mechanistic redundancy (system function) from source redundancy (input dependencies). The tree IS a hierarchical chain.
**Machines**: joint-vs-marginal, chain complex (tree structure), null hypothesis.
Full annotation: `third_pass_infotheo_cross.md` (TP-04).
**See also**: `by-structure/composite_systems.md`

### Neural Entropic Estimation — MI-NEE (Chan et al. 2019)
**Domain(s)**: Information theory (MI estimation)
Estimates MI via triangulation through common uniform reference, not direct joint-vs-marginal comparison. Avoids MINE's initialization problem. Uniform distribution as common null for both joint and marginal.
**Machines**: joint-vs-marginal, null hypothesis, stability.
Full annotation: `third_pass_infotheo_cross.md` (TP-08).

### HSIC-Bottleneck Orthogonalization (Li et al. 2024, AAAI)
**Domain(s)**: Information theory, machine learning (continual learning)
Prevents catastrophic forgetting by projecting gradients onto orthogonal complement of important subspace. Layer-wise HBO creates bigraded structure (layer × task). Structurally identical to Hodge decomposition: preserving harmonic component while modifying gradient/curl. ETF classifiers fix output geometry.
**Machines**: stability, joint-vs-marginal, chain complex (graded), null hypothesis.
Full annotation: `third_pass_infotheo_cross.md` (TP-09).
**See also**: `by-structure/phase_transitions.md`

### Shwartz-Ziv & Tishby (2017) — Opening the Black Box of DNNs via Information
arXiv: 1703.00810
**Domain(s)**: Information theory, machine learning
Origin paper for the "information plane" trajectory analysis of deep learning. Training epoch parameterizes the information plane: each layer's (I(X;T), I(T;Y)) traces a path with two phases — fitting (both increase) then compression (I(X;T) decreases while I(T;Y) stays high). Converged layers lie on the IB bound. Drift-diffusion transition in SGD gradients at ~350 epochs. **Caveat**: Saxe et al. (2018) and Geiger (2021) showed compression may be an artifact of saturating activations + binning-based MI estimation; see ANTISYNONYMS.md.
**Machines**: parameterized homology (primary), joint-vs-marginal, null hypothesis, stability.
Full annotation: `inbox.md` (arXiv: 1703.00810).
**See also**: `by-structure/filtrations.md`, `by-structure/composite_systems.md`

### Cross-listed from Dynamical Systems (third pass):
- **Cross-Correlation Integral** — Joint-vs-marginal excess applied to attractor measures. Full annotation: `third_pass_dynamics_tda.md` (TP-03).
- **Entropic Symmetry Breaking** (arXiv: 2510.03572) — Entropy framework for bifurcation. Full annotation: `third_pass_dynamics_tda.md` (TP-04).
- **Ordinal Networks** — Permutation entropy meets network theory. Full annotation: `third_pass_dynamics_tda.md` (TP-05).
- **Visibility Graph Irreversibility** — KL divergence as irreversibility test. Full annotation: `third_pass_dynamics_tda.md` (TP-06).
- **Specific Entropy Rate** — State-dependent unpredictability function. Full annotation: `third_pass_dynamics_tda.md` (TP-07).

### Cross-listed from Neuroscience (third pass):
- **GC-STCL** — Granger causality + contrastive learning for EEG. Full annotation: `third_pass_infotheo_cross.md` (TP-01).
- **Driver Fatigue GC** — Frequency-band causal networks. Full annotation: `third_pass_infotheo_cross.md` (TP-05).
- **Nonparametric Brain GC** — Spectral Granger causality. Full annotation: `third_pass_infotheo_cross.md` (TP-06).
- **Dabney Distributional Code** — Quantile-indexed neuron family. Full annotation: `third_pass_neuro_qec.md` (TP-03).
- **IPWT** — Synergistic information as consciousness criterion. Full annotation: `third_pass_neuro_qec.md` (TP-01).

---

## Joint x Neuro — Consciousness / Information Dynamics (Wave 5)

### Mediano, Rosas, Carhart-Harris, Seth, Barrett (2019) — PhiID
**"Beyond integrated information: A taxonomy of information dynamics phenomena"**
arXiv: 1909.02297
**Domain(s)**: Neuroscience (consciousness), information theory
PhiID = Integrated Information Decomposition. Double-redundancy lattice (product of two PID lattices, 16 nodes) with Moebius inversion gives 16 atoms decomposing excess entropy. Six-category taxonomy: storage, copy, transfer, erasure, upward causation, downward causation. Unifies IIT and PID. Shows Phi_WMS, psi, Phi_G, CD each capture different atom subsets (Table I). Corrected Phi_WMS,c avoids negativity by adding back double-redundancy.
**Machines**: joint-vs-marginal, chain complex, parameterized homology, null hypothesis, stability.
Full annotation: `inbox.md` (arXiv: 1909.02297).
**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`

### Barrett (2015) — PID for Gaussian Systems
**"Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems"**
arXiv: 1411.2832
**Domain(s)**: Information theory, neuroscience
First PID for continuous variables. For Gaussian with univariate target: all PIDs satisfying marginal-dependence collapse to MMI (R = min{I(X;Y), I(X;Z)}). Synergy = extra info from weaker source given stronger. Net synergy positive even when sources uncorrelated (log concavity effect). Dynamical MVAR analysis: synergy decreases with lag depth, increases with weaker connection, decreases with source correlation. Proposes synergistic complexity SC as alternative to Phi.
**Machines**: joint-vs-marginal, parameterized homology, null hypothesis, stability.
Full annotation: `inbox.md` (arXiv: 1411.2832).
**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`

---

## Wave 6 — Directed Information Flow in Neural Oscillations and Spike Trains (2026-04-07)

### Lobier, Siebenhuhner, Palva, Palva (2014) — Phase Transfer Entropy
**"Phase transfer entropy: A novel phase-based measure for directed connectivity in networks coupled by oscillatory interactions"**
DOI: 10.1016/j.neuroimage.2013.08.056, NeuroImage 85(2):853-872. 281 citations.
**Domain(s)**: Neuroscience, information theory
Phase TE = transfer entropy applied to Morlet-filtered phase time series. Isolates directed oscillatory coupling: how much source phase history improves prediction of target phase updates beyond target's own history. Differential TE quantifies net directionality. Frequency band as discrete parameter yields band-specific directed connectivity graphs. Surrogate-based null hypothesis testing validated (no false positives under noise + mixing). Extends Schreiber (2000) TE to the phase domain.
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology.
Full annotation: `inbox.md` (Wave 6).
**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`, `by-domain/neuroscience.md`

### Shorten, Spinney, Lizier (2021) — Continuous-Time Transfer Entropy for Spike Trains
**"Estimating Transfer Entropy in Continuous Time Between Neural Spike Trains or Other Event-Based Data"**
DOI: 10.1371/journal.pcbi.1008054, PLOS Computational Biology 17(4):e1008054. 58 citations.
**Domain(s)**: Information theory, neuroscience
Continuous-time TE formulated via Radon-Nikodym derivatives between path measures. kNN estimator in inter-event-interval space is provably consistent (discrete-time plug-in estimators converge to wrong value for event data). Local permutation surrogates provide correct null for point processes (source-time-shift surrogates demonstrated to fail). Pathwise TE decomposes into jump contributions (at target events) and continuous contributions (between events). Captures fine-and-coarse timescale relationships simultaneously. Validated on stomatogastric ganglion pyloric circuit where previous estimators failed.
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology.
Full annotation: `inbox.md` (Wave 6).
**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`, `by-domain/neuroscience.md`

---

## Wave 7 — Causal Emergence (2026-04-07)

### Rosas, Mediano, Jensen, Seth, Barrett, Carhart-Harris, Bor (2020) — Causal Emergence via PID
**"Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data"**
PLoS Computational Biology, 16(12), e1008289. arXiv: 2004.08220. 143 citations.
**Domain(s)**: Information theory, neuroscience, dynamical systems (complex systems)
Inverted joint-vs-marginal: macro feature V has causal power exceeding sum of micro parts. Ψ^(1) = I(V_t; V_{t'}) - Σ_j I(X^j_t; V_{t'}) > 0. Theorem 1: causal emergence iff dynamical synergy Syn^(k) > 0. Decomposition: Syn^(k) = D^(k) (downward causation) + G^(k) (causal decoupling / "statistical ghosts"). Three parameters: order k, time lag, partition choice. Practical sufficiency criteria using only pairwise MI. Applied to Game of Life (Ψ=0.58, particles decoupled from cells), Reynolds flocking (emergence at edge of chaos), macaque ECoG (Ψ=1.275, motor decoding emergent up to ~0.2s). Extends Mediano PhiID; no TDA/QEC awareness.
**Machines**: joint-vs-marginal (inverted), parameterized homology, null hypothesis, chain complex (inherited from PID/PhiID).
Full annotation: `inbox.md` (Wave 7).
**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`, `atlas/JOINT_VS_MARGINAL.md`

### Varley, Mediano, Patania & Bongard (2025) — The Topology of Synergy
**"The topology of synergy: Linking topological and information-theoretic approaches to higher-order interactions in complex systems"**
PLoS Computational Biology, DOI: 10.1371/journal.pcbi.1013649. arXiv: 2504.10140. 4 citations.
**Domain(s)**: TDA, information theory, neuroscience
Head-to-head comparison of O-information (TC, DTC, O, S) with H2 persistent homology (Rips/Chebyshev/Ripser) on toy manifolds and fMRI. H2 cavities <-> synergy (O < 0), knots <-> redundancy (O > 0). Normalized O-bar vs avg H2 persistence: rho = -0.55 to -0.65 in fMRI. PCA destroys synergy (rho(O-bar, PC1 variance) = 0.91-0.95) while preserving redundancy. KNN-based O-information estimator with single neighbor search (Eq. 14). Intrinsic vs. contextual higher-order information distinction. Circular-shift null model. EXPLICIT cross-domain bridge: TDA + information theory.
**Machines**: chain complex, parameterized homology, joint-vs-marginal, null hypothesis, stability.
Full annotation: `inbox.md` (Wave 7).
**See also**: `cross_domain_bridges.md`, `by-domain/tda.md`, `by-domain/neuroscience.md`, `by-structure/composite_systems.md`, `by-structure/filtrations.md`

---

## Wave 8 — Matching in Information Theory (2026-04-07)

### Blahut (1972) + Arimoto (1972) — Channel Capacity and Rate-Distortion via Alternating Minimization
**Blahut: "Computation of channel capacity and rate-distortion functions" (IEEE Trans. IT, 18(4):460–473)**
**Arimoto: "An algorithm for computing the capacity of arbitrary discrete memoryless channels" (IEEE Trans. IT, 18(1):14–20)**
Combined citations: 3000+.
**Domain(s)**: Information theory (foundational)
Optimal assignment between source and channel/reproduction alphabets. Channel capacity: find P(x) maximizing I(X;Y) = optimal matching of source symbols to channel inputs. Rate-distortion R(D): find test channel P(y|x) minimizing I(X;Y) at distortion ≤ D = minimum-cost soft assignment. Alternating minimization predates EM (1977): fix one marginal, optimize the other. Each step is a matching update. R(D) curve parameterized by distortion D; slope = -s (Lagrange multiplier). Converges to global optimum by convexity.
**Machines**: matching, parameterized homology, null hypothesis (weak).
Full annotation: `inbox.md` (Wave 8).
**See also**: `by-structure/optimal_transport.md`, `atlas/MATCHING.md`
