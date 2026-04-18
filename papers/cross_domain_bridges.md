# Cross-Domain Bridges

Papers that explicitly or structurally bridge two or more of the five topo-rosetta domains (TDA, QEC, dynamical systems, neuroscience, information theory). These are the highest-value papers for the Rosetta project because they instantiate abstract machines in ways that connect communities that typically do not cite each other.

Each annotation notes which domains are bridged and whether the authors themselves acknowledge the connection.

---

## Fasoli, Coletta, Gutierrez-Barragan, Gini, Gozzi, Panzeri (2026)
**"Attractor dynamics of a whole-cortex network model predicts emergence and structure of fMRI co-activation patterns in the mouse brain"**
DOI: 10.1371/journal.pcbi.1013995 | PLoS Computational Biology 22(2)

**Domains bridged**: Neuroscience + Dynamical systems

**Domain(s)**: Computational neuroscience, dynamical systems theory

**Abstract machines instantiated**:
- **Parameterized homology**: The model's attractor landscape is parameterized by inter-hemispheric connectivity strength. As this parameter is varied (decreased or increased from real anatomical values), the number of attractors changes — fewer attractors emerge, and their ability to predict empirical co-activation patterns (CAPs) degrades. This is a bifurcation diagram: a parameterized family of dynamical systems whose invariants (number and type of attractors: stationary vs. oscillatory) change at critical parameter values. The attractor count IS the topological invariant being tracked.
- **Stability**: The model parameters are fitted only to static fMRI properties (mean, variance, covariance on the timescale of minutes), yet the model predicts rich frame-by-frame dynamics on the timescale of seconds. This is a stability result: the dynamical structure (attractor topology) is robust — it emerges from the fitted static properties without being explicitly optimized for. The attractors recapitulate empirical CAPs, meaning the topological organization of the attractor landscape is stable under the perturbation of going from fitted static constraints to emergent dynamics.
- **Null hypothesis**: Neglecting fiber directionality (replacing directed anatomical connectivity with undirected) serves as the structural null. This null severely reduces the number of attractors and their explanatory power for CAPs. The gap between directed and undirected connectivity models quantifies the contribution of directionality to the dynamical repertoire — a structure-removal null.
- **Joint-vs-marginal excess**: The model reveals that CAPs are not independent patterns but emerge from the joint interaction of excitatory-inhibitory populations across cortical regions via directed connectivity. The attractor structure is absent from any individual region's dynamics and emerges only from the coupled system — genuine composite structure.

**What is genuinely new (not reducible to shared abstraction)**:
- The key finding is that a model fitted only to static correlations spontaneously generates the correct dynamic repertoire (CAPs). This means the attractor topology is fully determined by the static statistical structure — a striking constraint that has no direct analogue in TDA (where persistence diagrams require explicit scale parameterization) or QEC (where dynamic error correction requires explicit decoder design).
- Directionality of anatomical connectivity is essential: undirected connectivity produces far fewer attractors. This shows that the boundary operator's orientation matters — not just whether connections exist, but their direction. Analogous to the difference between chain complexes over Z (which track orientation) vs. Z/2 (which do not).
- The excitatory-inhibitory balance within regions creates the nonlinearity needed for multiple attractors. Without this balance (e.g., purely excitatory networks), the system has only one attractor. This is a domain-specific mechanism with no direct analogue in TDA or information theory.

**Connections the authors acknowledge**: Cite dynamical systems theory (bifurcation, attractor landscapes) and computational neuroscience (CAPs, resting-state fMRI). Explicitly note the connection between attractor dynamics and neural manifold geometry. Do NOT cite TDA, QEC, or information theory — the bridge to dynamical systems is acknowledged, but not to other Rosetta domains.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Attractor (stationary/oscillatory) | Topological invariant (fixed point/limit cycle) |
| Co-activation pattern (CAP) | Empirical signature of an attractor basin |
| Inter-hemispheric connectivity strength | Parameterization variable |
| Number of attractors | Betti-like count (topological complexity of the landscape) |
| Directed anatomical connectivity | Oriented boundary operator (chain complex over Z) |
| Undirected connectivity null | Chain complex over Z/2 (orientation removed) |
| Excitatory-inhibitory balance | Nonlinearity enabling multiple invariants |
| Static fMRI properties | Constraints that determine the filtration |
| Frame-by-frame dynamics | Emergent trajectory in the parameterized space |
| Allen mouse brain atlas | Ground-truth chain complex (the anatomical wiring) |

**Rosetta significance**: This paper demonstrates that attractor topology (dynamical systems) predicts neural activity patterns (neuroscience) and that the topological complexity depends on the oriented structure of the connectivity graph. The analogy to chain complexes over Z vs. Z/2 is structural and deep: directed vs. undirected connectivity is exactly the difference between tracking orientation or not in homology. The paper does not make this connection.

---

## Niroomand & Wales (2023)
**"Physics-Inspired Interpretability of Machine Learning Models"**
arXiv: 2304.02381 | ICLR 2023 Workshop on Physics for Machine Learning

**Domains bridged**: Dynamical systems (energy landscape theory) + Information theory (feature importance / interpretability)

**Domain(s)**: Machine learning, physical chemistry (energy landscapes), interpretability

**Abstract machines instantiated**:
- **Parameterized homology**: The loss landscape of a neural network is explored via basin-hopping and transition state search, producing a disconnectivity graph. The disconnectivity graph IS a parameterized view of the landscape: at each energy threshold (the parameter), connected components of sub-level sets are tracked. As the threshold rises, components merge — this is precisely the persistence diagram construction in 0-dimensional persistent homology (H_0). The authors compute this for ML loss landscapes, though they do not use TDA terminology.
- **Stability**: Conserved weights are identified across groups of minima in the disconnectivity graph. These are weights that remain approximately constant across multiple local minima connected by low-barrier transition states. The conservation is a stability statement: these weights are robust to perturbation of the loss landscape minimum (moving between nearby minima preserves their values).
- **Null hypothesis**: Random weight permutation serves as the null. Permuting conserved weights reduces AUC from 0.95 to 0.76, far exceeding the impact of permuting random weights. The gap quantifies the information content of the conserved weights — they carry the decision-relevant structure.
- **Joint-vs-marginal excess (weak)**: The conserved weights collectively determine model behavior in a way that individual weight magnitudes do not. The gradient-based methods (which look at individual input-output derivatives) miss the conserved structure that emerges from the joint landscape topology. The conservation is a composite property of the weight space, not reducible to single-weight analysis.

**What is genuinely new (not reducible to shared abstraction)**:
- Direct application of energy landscape methods (basin-hopping, transition state theory, disconnectivity graphs) from molecular science to ML loss landscapes. The disconnectivity graph is equivalent to a 0-dimensional persistence barcode, but the authors develop it independently from the physical chemistry tradition rather than from TDA.
- The conserved-weight concept: analogous to order parameters or reaction coordinates in chemistry. In a molecule, certain coordinates remain constant across conformational changes (e.g., bond lengths in a rotation). In a neural network, certain weights remain constant across loss landscape minima. This is a novel interpretability method with no analogue in standard ML interpretability (SHAP, LIME, integrated gradients).
- The observation that conserved weights are more informative than gradient-based feature importance. Permuting conserved weights causes much larger performance drops than permuting high-gradient weights.

**Connections the authors acknowledge**: Explicitly draw from energy landscape theory in physical chemistry (Wales, 1998, 2003). Cite molecular order parameters and coordinate invariants. The paper IS an acknowledged bridge between physical sciences and ML. They do NOT cite TDA or persistent homology — the disconnectivity graph is developed from the energy landscape tradition, not the computational topology tradition, despite being the same mathematical object (sub-level set persistence for H_0).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Disconnectivity graph | H_0 persistence diagram / dendrogram |
| Energy barrier between minima | Death time of a connected component |
| Basin of attraction | Sublevel set connected component |
| Transition state | Saddle point (merger event in persistence) |
| Conserved weight | Persistent feature (stable across the filtration) |
| Random weight permutation | Null model (structure destruction) |
| Loss landscape | Function whose sublevel sets define the filtration |
| Basin-hopping | Exploration of the persistence landscape |
| Order parameter | Topological invariant (persistent feature) |

**Rosetta significance**: This paper independently reinvents 0-dimensional persistent homology in the guise of disconnectivity graphs from physical chemistry. The two communities (TDA and energy landscape theory) have developed equivalent mathematical machinery for analyzing sub-level sets of real-valued functions, but neither cites the other. The conserved-weight concept adds a new invariant: not just the topology of the landscape, but which coordinates are fixed across its components.

---

## Kawaguchi, Deng, Ji, Huang (2023)
**"How Does Information Bottleneck Help Deep Learning?"**
arXiv: 2305.18887 | ICML 2023

**Domains bridged**: Information theory + Machine learning (statistical learning theory)

**Domain(s)**: Information theory, statistical learning theory, deep learning

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The information bottleneck principle is fundamentally a joint-vs-marginal comparison. I(X;Z) measures the mutual information between input X and hidden representation Z. The bottleneck goal is to minimize I(X;Z) (compress — remove marginal information about X that is irrelevant to Y) while maximizing I(Y;Z) (preserve — retain joint structure between Y and the representation). The excess I(X;Z) - I(Y;Z) quantifies the amount of task-irrelevant information retained in the representation.
- **Stability**: The main theoretical contribution is a generalization bound: Delta(s) <= sqrt((2 I(X;Z_l) + log(2/delta)) / (2n)). This bound says that generalization error is controlled by the mutual information I(X;Z_l) at layer l. This is a stability result: small I(X;Z) implies that the learned function is insensitive to the specific training sample (the representation discards sample-specific information), which bounds generalization. The bound scales with information content, NOT with parameter count, VC dimension, or Rademacher complexity.
- **Parameterized homology**: The information plane tracks I(X;Z_l) and I(Y;Z_l) at each layer l as training progresses. The trajectory through the information plane IS a parameterized curve (parameterized by training time and layer index) whose shape characterizes the learning dynamics. The paper proves that this trajectory's endpoint (the degree of information bottleneck) controls performance.
- **Null hypothesis**: The training data s = {(x_i, y_i)} drawn from the distribution (X,Y) is the finite sample. The generalization error Delta(s) measures the gap between the empirical loss (on the sample) and the true loss (on the distribution). The distribution is the reference; the sample is the perturbation. The bound quantifies how much the finite-sample perturbation affects the learned function.

**What is genuinely new (not reducible to shared abstraction)**:
- First rigorous proof that the information bottleneck principle provides generalization bounds for learned representations. Previous work (Shwartz-Ziv & Tishby, 2017) conjectured this; this paper proves it. The key technical contribution is handling the case where the encoder is learned from data (not fixed a priori), which requires a novel analysis combining mutual information with PAC-Bayes-like arguments.
- The bound is strictly tighter than parameter-count bounds for networks with strong information bottlenecks. This means that for networks that compress representations effectively, the information-theoretic bound is the right characterization of generalization, not the combinatorial (VC/Rademacher) one.
- Resolution of the open conjecture from Shwartz-Ziv et al. (2019), extending it to the practical setting.

**Connections the authors acknowledge**: Explicitly cite the information bottleneck literature (Tishby, Shwartz-Ziv, Alemi). Cite PAC-Bayes bounds and compression-based generalization theory. The paper IS a bridge between information theory and statistical learning theory. No connections to TDA, QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| I(X;Z) (input-representation MI) | Joint-vs-marginal excess (full) |
| I(Y;Z) (label-representation MI) | Joint-vs-marginal excess (task-relevant) |
| Information bottleneck | Compression of excess information |
| Generalization bound Delta(s) | Stability guarantee (perturbation bound) |
| Training data s (finite sample) | Perturbation of the true distribution |
| Information plane trajectory | Parameterized curve (layer x epoch) |
| Learned encoder phi | Map from input space to representation |
| Parameter-count bound (VC, etc.) | Alternative stability guarantee (combinatorial) |
| Compression phase | Death of unnecessary features |

**Rosetta significance**: This paper provides the first rigorous link between information compression (killing unnecessary joint-vs-marginal structure) and stability (generalization). The bound sqrt(I(X;Z)/n) has the same form as persistence stability bounds (perturbation / sample_size), with mutual information playing the role of the perturbation magnitude. Networks that compress more are more stable — directly analogous to the TDA principle that simpler persistence diagrams (fewer features) are more robust.

---

## Ma, Lewis, Kleijn (2020)
**"The HSIC Bottleneck: Deep Learning without Back-Propagation"**
AAAI 2020

**Domains bridged**: Information theory (independence criterion) + Machine learning (training without backpropagation)

**Domain(s)**: Information theory, kernel methods, deep learning

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The HSIC (Hilbert-Schmidt Independence Criterion) measures statistical dependence between random variables via cross-covariance operators in RKHS. HSIC(X,Y) = ||C_XY||^2_HS where C_XY is the cross-covariance operator. HSIC = 0 iff X and Y are independent (marginal product). The training objective maximizes HSIC(Z_l, Y) (representation should be dependent on labels — joint structure) while minimizing HSIC(Z_l, X) (representation should be independent of input — marginal product). This IS the information bottleneck, but implemented via kernel independence rather than mutual information.
- **Null hypothesis**: The marginal product (independence) is the null. HSIC measures departure from this null. When HSIC(Z_l, X) is minimized, the representation Z_l approaches statistical independence from X — the null model where no input information is retained. The residual HSIC(Z_l, Y) quantifies the task-relevant structure that survives compression.
- **Stability**: The method eliminates vanishing/exploding gradients because each layer is trained independently (no backpropagation). This is a stability guarantee on the training process: layer-wise HSIC objectives decouple the optimization, preventing the exponential amplification/attenuation that makes deep backpropagation unstable. The training process is stable by construction.
- **Chain complex (weak)**: The layer-wise training creates a structure where each layer l has a well-defined input (Z_{l-1}) and output (Z_l), and the objectives at each layer are independent. The information flows from X through Z_1, Z_2, ..., Z_L to Y. The HSIC objectives define a graded structure: at each grade (layer), information is compressed (HSIC with X decreases) and task-relevance is preserved (HSIC with Y maintained). This is not a chain complex in the strict boundary-operator sense, but the graded, direction-respecting structure is analogous.

**What is genuinely new (not reducible to shared abstraction)**:
- Training deep networks without backpropagation by optimizing layer-wise kernel independence criteria. This is biologically more plausible than backpropagation (no weight transport, no update locking) and eliminates gradient instability by design.
- The HSIC as a practical replacement for mutual information in the information bottleneck. MI is hard to estimate in high dimensions; HSIC is computed from kernel matrices and is tractable for any kernel.
- The surprising finding that HSIC-bottleneck training sometimes produces nearly one-hot output representations without ever being told to match classification labels — the information bottleneck principle alone drives the representation toward discrete class structure.
- Competitive with backpropagation+cross-entropy on MNIST/FashionMNIST/CIFAR10, demonstrating that the information bottleneck is sufficient for learning, not merely a regularizer.

**Connections the authors acknowledge**: Cite the information bottleneck (Tishby), MINE (Belghazi et al.), Shwartz-Ziv & Tishby on the information plane. Cite HSIC and kernel independence testing literature. The paper IS a bridge between kernel methods/information theory and deep learning training. No connections to TDA, QEC, dynamical systems, or neuroscience (though the biological plausibility angle connects to neuroscience implicitly).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| HSIC(Z, Y) | Joint-vs-marginal excess (task-relevant dependence) |
| HSIC(Z, X) | Joint-vs-marginal excess (unnecessary dependence) |
| Cross-covariance operator C_XY | Joint structure in RKHS |
| Independence (HSIC = 0) | Marginal product (null model) |
| Layer-wise training | Graded decomposition (each grade optimized independently) |
| No backpropagation | Stability by decoupling (no exponential amplification) |
| Nearly one-hot outputs | Emergent discrete structure from continuous optimization |
| Kernel matrix K | Gram matrix (similarity structure in RKHS) |

**Rosetta significance**: HSIC provides a kernel-space implementation of the joint-vs-marginal machine that is computationally tractable where MI is not. The layer-wise training eliminates the stability problems of backpropagation, achieving stability by decomposition — analogous to how chain complexes decompose global structure into local (grade-by-grade) computations. The emergence of discrete class structure from the continuous HSIC objective is reminiscent of how discrete topological invariants (Betti numbers) emerge from continuous filtrations.

---

## Pati & Sanders (2005)
**"No partial erasure of quantum information"**
arXiv: quant-ph/0503138 | Physical Review A 74, 010301(R)

**Domains bridged**: QEC (quantum information) + Information theory (erasure/compression)

**Domain(s)**: Quantum information theory, quantum error correction

**Abstract machines instantiated**:
- **Stability (as impossibility)**: The no-partial-erasure theorem is a stability result in the strongest possible sense: quantum information cannot be partially degraded by any quantum operation. You can erase ALL the information (map to a fixed state) or NONE of it (preserve the full parameter space), but you cannot reduce the parameter space dimension. This is anti-compression: unlike classical information, which can be compressed (rate-distortion theory), quantum information is indivisible. The parameter space (theta, phi) of a qubit is a topological object (S^2, the Bloch sphere), and you cannot reduce its dimension by any CPTP map.
- **Chain complex (topological)**: The Bloch sphere S^2 parameterizing qubit states is a 2-dimensional manifold. Partial erasure would correspond to projecting this manifold to a lower-dimensional subspace (e.g., reducing S^2 to S^1 by erasing phi). The theorem proves this is impossible — the topological dimension of the quantum state space is an invariant under all physical operations. This is a homological statement: H_2(S^2) = Z is non-trivial, and no CPTP map can reduce it.
- **Joint-vs-marginal excess**: Quantum information stored in the full parameter (theta, phi) cannot be split into independent "theta-information" and "phi-information" and then selectively erased. The theta and phi parameters are entangled in the quantum state structure — they form a joint object (the Bloch sphere) that cannot be decomposed into marginal components. This indivisibility IS a joint-vs-marginal statement: the joint parameter space has structure absent from any attempt to decompose it into marginal subspaces.

**What is genuinely new (not reducible to shared abstraction)**:
- The no-flipping theorem (impossibility of a universal NOT gate) emerges as a corollary. This connects to QEC: you cannot universally flip a qubit because that would require partial erasure (erasing one coordinate and reconstructing it negated).
- Extension to continuous-variable quantum information (bosonic coherent states on the phase space), proving that the indivisibility of quantum information is not specific to finite-dimensional systems.
- The connection to the no-cloning and no-deletion theorems: together, these establish a conservation law for quantum information. Information cannot be created (no-cloning), destroyed partially (no-partial-erasure), or fully destroyed while preserving a copy (no-deletion). This is a topological conservation law — the dimension of the parameter manifold is a topological invariant.
- The "integrity principle": quantum information must be treated as a whole entity. This has a direct category-theoretic interpretation: the functor from quantum states to their parameter spaces does not admit factorizations.

**Connections the authors acknowledge**: Cite no-cloning (Wootters-Zurek), no-deletion, and no-flipping theorems. Explicitly state the conservation-of-quantum-information principle. Situated at the QEC/quantum information interface. No connections to TDA, dynamical systems, or neuroscience, though the topological structure (Bloch sphere) is the same object studied in algebraic topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Qubit parameter space (theta, phi) | Manifold S^2 (Bloch sphere) |
| Partial erasure | Dimension reduction of the parameter manifold |
| CPTP map | Morphism (structure-preserving operation) |
| No partial erasure | Topological invariance of dimension under CPTP maps |
| Full erasure (to fixed state) | Projection to a point (trivial homology) |
| No-flipping | Impossibility of orientation reversal on S^2 by CPTP |
| Conservation of quantum information | Topological conservation law (H_2(S^2) invariant) |
| Indivisibility | Joint-vs-marginal: parameter space is not decomposable |
| Spin coherent states | Points on S^2 (classical-quantum boundary) |
| Bosonic coherent states | Points on phase space (continuous-variable extension) |

**Rosetta significance**: This paper reveals that quantum information has topological protection built into the laws of physics: the parameter manifold of a quantum state cannot be dimensionally reduced by any physical operation. This is the deepest possible stability theorem — it is not a bound (like PH stability or QEC thresholds) but an absolute impossibility. The Bloch sphere S^2 appears in both QEC (as the qubit state space) and TDA (as the simplest manifold with non-trivial H_2). The paper does not make this connection, but the abstract machine (topological invariance of the parameter space) is the same.

---

## Garbaczewski (2005)
**"Differential entropy and time"**
arXiv: quant-ph/0408192 | Entropy 7(4):253-299

**Domains bridged**: Information theory + Dynamical systems + QEC (quantum information)

**Domain(s)**: Information theory, quantum mechanics, statistical mechanics, dynamical systems

**Abstract machines instantiated**:
- **Parameterized homology**: The paper tracks how entropy functionals evolve under dynamical evolution. For Smoluchowski processes, the Shannon entropy H(t) = -integral p(x,t) log p(x,t) dx changes over time. For Schrodinger picture evolution, the Gibbs entropy of the probability density |psi|^2 tracks the wave packet delocalization. The parameter is time, and the invariant is the entropy value. The temporal behavior reveals physically meaningful transitions: entropy increase (delocalization/mixing), entropy decrease (localization/ordering), and entropy stationarity (invariant measures).
- **Joint-vs-marginal excess**: The paper carefully distinguishes three entropy notions applied to the SAME physical system: (1) von Neumann entropy S(rho) for the quantum density matrix, (2) Shannon/Gibbs entropy H(p) for the position probability density |psi|^2, and (3) Kullback-Leibler divergence D_KL(p||p_*) relative to a reference measure. For pure quantum states, S(rho) = 0 (zero uncertainty at the quantum level) but H(p) is non-zero and dynamical (non-zero uncertainty at the probability level). The gap between these measures quantifies different layers of information content in the same system — a multi-level joint-vs-marginal decomposition.
- **Stability**: The Kullback-Leibler entropy D_KL(p||p_*) relative to an invariant density p_* is monotonically non-increasing for dissipative Markov processes (H-theorem). This is a Lyapunov stability result: D_KL serves as a Lyapunov function for the dynamics, guaranteeing convergence to the invariant measure. The Shannon entropy, by contrast, can be non-monotone — it provides a different (less stable) view of the same dynamics.
- **Null hypothesis**: The invariant density p_* serves as the null/reference distribution. The Kullback-Leibler divergence measures departure from this equilibrium. The temporal decay of D_KL quantifies relaxation to the null. For quantum systems, the thermal state serves a similar role.

**What is genuinely new (not reducible to shared abstraction)**:
- The systematic comparison of Shannon, Kullback-Leibler, and von Neumann entropies as dynamical quantities applied to the same physical system. Previous work treated these as alternatives; this paper shows they reveal different dynamical information that cannot be substituted for each other.
- The Fisher information functional I(t) = integral (grad log p)^2 p dx appears as a quantifier of power transfer in the mean for both quantum (Schrodinger) and classical (Smoluchowski) dynamics. Fisher information is related to the Cramer-Rao bound and hence to statistical estimation — bridging information theory and dynamics via estimation theory.
- The observation that Shannon entropy dynamics captures non-equilibrium phenomena (power transfer, localization changes) that Kullback-Leibler entropy misses entirely, because D_KL is monotone while H is not. The non-monotonicity of H is physically informative.
- Extension to quantum wave-packet spreading, where the Gibbs entropy of |psi(x,t)|^2 captures the spatial delocalization that the von Neumann entropy (which is constant for pure-state unitary evolution) cannot detect.

**Connections the authors acknowledge**: Explicitly cite Boltzmann H-theorem, Fisher information, Cramer-Rao bounds, and quantum entropy. The paper IS a bridge between statistical mechanics, quantum mechanics, and information theory — the author navigates all three fluently. Does NOT cite TDA or computational topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Shannon entropy H(p) | Scalar invariant of the probability density (non-monotone) |
| Kullback-Leibler D_KL(p||p_*) | Distance from null (invariant measure) |
| von Neumann entropy S(rho) | Quantum-level invariant (constant for pure states) |
| Fisher information I(p) | Curvature of the statistical manifold (information geometry) |
| Invariant density p_* | Null model / equilibrium reference |
| Smoluchowski process | Dissipative dynamics (classical) |
| Schrodinger evolution | Unitary dynamics (quantum) |
| H-theorem (D_KL non-increasing) | Lyapunov stability toward the null |
| Wave-packet delocalization | Entropy increase = topological spreading |
| Power transfer | Energy flow quantified by Fisher information |

**Rosetta significance**: This is one of the few papers that simultaneously operates in information theory, dynamical systems, and quantum mechanics — three of the five Rosetta domains. The Fisher information connection is especially valuable: Fisher information defines the metric on statistical manifolds (information geometry), and this paper shows it quantifies power transfer in both classical and quantum dynamics. This links the information-geometric structure of probability spaces to physical energy flow — a bridge between information theory and dynamics that neither community has fully exploited.

---

## Darmon (2018)
**"Specific Differential Entropy Rate Estimation for Continuous-Valued Time Series"**
arXiv: 1606.02615

**Domains bridged**: Information theory + Dynamical systems

**Domain(s)**: Information theory, dynamical systems, nonlinear time series analysis

**Abstract machines instantiated**:
- **Parameterized homology**: The specific entropy rate h(x) is a function of the current state x of the dynamical system, rather than a single number averaged over all states. This makes the entropy rate itself a parameterized object — parameterized by the state space of the dynamics. The state-dependent unpredictability map h: M -> R (where M is the state space / attractor) is a new invariant that encodes how predictability varies across the attractor. This is richer than a single Lyapunov exponent or KS entropy, which average over the invariant measure.
- **Joint-vs-marginal excess**: The specific entropy rate h(x) = H(X_{t+1} | X_t = x) is a conditional entropy — it measures how much uncertainty remains about the next state given the current state x. The marginal entropy rate h_avg = E[h(X)] averages this over all states. The variation of h(x) around h_avg reveals state-dependent structure: some states are highly predictable (h(x) << h_avg), others are highly unpredictable (h(x) >> h_avg). This variation is joint structure absent from the marginal average.
- **Null hypothesis**: The paper connects specific entropy rate to Sample Entropy (SampEn) and Approximate Entropy (ApEn), showing that these popular complexity measures are approximations to h(x) under specific modeling choices. The standard (time-averaged) entropy rate serves as the null reference; the specific rate reveals deviations from this average that are physically meaningful.

**What is genuinely new (not reducible to shared abstraction)**:
- Lifting entropy rate from a scalar to a function on the state space. Previous work on entropy rate (Shannon, Kolmogorov-Sinai, etc.) produces a single number. The specific entropy rate produces a map h: M -> R, which can be visualized, analyzed for structure, and related to the geometry of the attractor.
- Clarification of the methodological confusion between Kolmogorov-Sinai entropy (deterministic chaos approach) and Shannon entropy rate (stochastic process approach). The paper shows these give diverging answers in opposite regimes: KS entropy is infinite for stochastic systems, Shannon entropy rate is infinite for deterministic systems. The specific entropy rate resolves this by operating within the stochastic framework but providing state-dependent resolution.
- Application to heart rate variability: the specific entropy rate reveals that certain cardiac states are much more unpredictable than others, providing a diagnostic tool that time-averaged entropy measures miss.

**Connections the authors acknowledge**: Cite Shannon entropy rate, Kolmogorov-Sinai entropy, computational mechanics (Crutchfield, Shalizi), and Approximate/Sample Entropy. The paper IS a bridge between information theory and dynamical systems analysis — the author explicitly navigates both traditions. No connections to TDA, QEC, or neuroscience (though the HRV application touches neuroscience peripherally).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Specific entropy rate h(x) | State-dependent invariant (parameterized by state space) |
| Time-averaged entropy rate h_avg | Scalar invariant (single number) |
| State space M | Attractor / manifold |
| Conditional density p(x_{t+1}|x_t) | Transition kernel (dynamics) |
| KS entropy | Deterministic dynamics invariant (topological entropy) |
| Shannon entropy rate | Stochastic process invariant |
| Sample Entropy (SampEn) | Approximation to h(x) (biased estimator) |
| Heart rate variability | Physiological dynamical system |
| State-dependent unpredictability | Local Lyapunov-like diagnostic |

**Rosetta significance**: The lift from scalar entropy rate to a function h: M -> R is structurally parallel to the lift from Betti numbers to persistence diagrams in TDA. Both replace a single summary statistic with a richer object parameterized by the state/scale space. The specific entropy rate is the information-theoretic analogue of the local Lyapunov exponent — both measure local sensitivity/unpredictability on the attractor, but from different theoretical frameworks. A Rosetta translation between h(x) and the local Lyapunov exponent lambda(x) would be valuable.

---

## Gallicchio & Micheli (2020)
**"Fast and Deep Graph Neural Networks"**
arXiv: 1911.08941 | AAAI 2020

**Domains bridged**: Dynamical systems (reservoir computing / fixed-point theory) + TDA (graph topology / GNN expressiveness)

**Domain(s)**: Graph neural networks, dynamical systems (reservoir computing), graph classification

**Abstract machines instantiated**:
- **Stability**: The core theoretical contribution is a stability condition for deep GNN layers with untrained recurrent weights. Each GNN layer implements a contractive map x_{l+1} = sigma(W_l * x_l + ...) where the spectral radius rho(W_l) < 1 ensures existence and uniqueness of a fixed point (Banach contraction principle). The fixed point IS the graph embedding — the stable representation that the graph converges to under the recurrent dynamics. This stability condition is both necessary (for the dynamics to converge) and sufficient (convergence is exponentially fast). The analogy to QEC is direct: the contractivity condition plays the same role as the error correction rate exceeding the noise rate (kappa > lambda in Oreshkov, 2013).
- **Parameterized homology**: The depth of the network is the parameter. As layers are added, the receptive field of each node grows — each layer propagates information one hop further through the graph. The representation at layer l encodes the topology of the l-hop neighborhood. Increasing l reveals progressively larger-scale graph structure, analogous to increasing the scale parameter epsilon in a Rips filtration. The sparse, untrained weights act as random projections that preserve topological features while discarding geometric details.
- **Null hypothesis**: The untrained (random) weights serve as a structural null. The fact that competitive classification accuracy is achieved WITHOUT training the recurrent weights demonstrates that the architecture alone (depth + graph topology) carries the essential structure. The trainable weights (in the output layer only) merely reformat the information. The gap between untrained and fully-trained performance quantifies the contribution of learning vs. architecture.
- **Chain complex (structural analogue)**: The stacked GNN layers form a graded structure where each layer l maps from the l-th representation space to the (l+1)-th. The message-passing aggregation at each layer IS a boundary-like operator: it combines information from the neighborhood (analogous to how boundary operators combine faces of a simplex). The fixed-point constraint ensures that the composition of layers converges — a stability condition on the "chain."

**What is genuinely new (not reducible to shared abstraction)**:
- The explicit connection between reservoir computing (echo state networks, liquid state machines) and deep GNNs. Reservoir computing uses random, untrained recurrent connections with a trained readout — this paper applies the same principle to graph-structured data with deep architectures.
- The stability condition rho(W) < 1 for graph diffusion with sparse random weights. This provides a concrete, checkable criterion for when a deep GNN will converge, independent of the input graph.
- The finding that untrained deep GNNs achieve state-of-the-art or competitive performance on graph classification. This is surprising and suggests that graph topology (the structure of the input) carries more information than the learned parameters — the architecture acts as a topological feature extractor.
- Extreme computational efficiency: training only the output layer (a linear classifier on the fixed-point embeddings) is orders of magnitude faster than training all layers via backpropagation.

**Connections the authors acknowledge**: Cite reservoir computing (echo state networks, Jaeger 2001; liquid state machines, Maass et al. 2002), GNN theory (Scarselli et al., 2009; Micheli, 2009; Xu et al., 2018), and graph kernels. Explicitly position the work at the reservoir computing / GNN interface. No citations to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Spectral radius rho(W) < 1 | Contractivity condition (stability guarantee) |
| Fixed point of recurrent dynamics | Stable representation (embedding) |
| Banach contraction principle | Convergence theorem (uniqueness + exponential convergence) |
| Layer depth l | Scale parameter (controls receptive field / neighborhood size) |
| Message-passing aggregation | Boundary-like operator (neighborhood combination) |
| Untrained random weights | Null model (architecture without learning) |
| Trained output layer | Readout (reformatting the stable representation) |
| Graph diffusion | Information propagation (analogous to filtration at scale l) |
| Sparse recurrent units | Random projections preserving topological features |

**Rosetta significance**: This paper provides a concrete example where the stability machine (Banach contraction) determines whether a topological feature extractor (deep GNN) converges to a meaningful representation. The receptive field growth with depth is structurally identical to scale growth in a Rips filtration. The fact that untrained (random) weights suffice for competitive performance suggests that the graph's intrinsic topology, not the learned parameters, is the primary source of discriminative information — an empirical validation of the principle that topology carries structure.

---

## Liu, Lin, Padhy, Tran, Bedrax-Weiss, Lakshminarayanan (2020)
**"Simple and Principled Uncertainty Estimation with Deterministic Deep Learning via Distance Awareness"**
arXiv: 2006.10108 | NeurIPS 2020

**Domains bridged**: Information theory (uncertainty quantification) + Geometry (manifold distance / spectral theory)

**Domain(s)**: Machine learning, uncertainty quantification, Gaussian processes, spectral theory

**Abstract machines instantiated**:
- **Stability**: The paper's central concept is distance awareness: a model's uncertainty should reflect the distance between a test example and the training data manifold. Spectral normalization constrains the Lipschitz constant of the feature extractor: ||h(x) - h(x')||_H <= L * ||x - x'||_X, where L is bounded by the product of spectral norms. This is a bi-Lipschitz-like constraint ensuring that the feature map preserves distances — small perturbations in input produce bounded changes in representation. This is the same stability structure as PH stability (bottleneck <= Hausdorff) and the QEC threshold theorem (bounded error propagation).
- **Joint-vs-marginal excess**: The Gaussian Process output layer computes predictive uncertainty as a function of the training data kernel matrix and the test point's kernel evaluations. The posterior variance sigma^2(x*) = k(x*,x*) - k(x*,X) K^{-1} k(X,x*) measures how much the test point's covariance with the training set differs from its self-covariance — a joint-vs-marginal comparison. High uncertainty means the test point has low joint structure with the training set.
- **Null hypothesis**: Out-of-domain (OOD) inputs are the null. For OOD inputs, the model should return maximum entropy (uniform distribution over labels). The GP layer ensures this: points far from the training manifold have high posterior variance, producing near-uniform predictions. The training manifold is the structured reference; OOD inputs are the structureless null.
- **Parameterized homology (structural analogue)**: The spectral normalization constrains the Jacobian's singular values at every point in the network. As the layer index varies (the parameter), the cumulative Lipschitz constant is the product of per-layer spectral norms. This creates a parameterized family of Lipschitz bounds, one per layer, that collectively control the global distance-preservation property.

**What is genuinely new (not reducible to shared abstraction)**:
- The formalization of distance awareness as a necessary condition for minimax-optimal uncertainty estimation. Previous work (deep ensembles, MC dropout) achieved good uncertainty empirically but without identifying WHY. This paper shows the mechanism: the feature map must preserve input-space distances for the uncertainty to be meaningful.
- The SNGP method: spectral normalization (enforcing distance preservation) + Laplace-approximated GP output (providing the actual uncertainty). This is a principled two-step approach: first ensure the features are distance-aware, then use a distance-based uncertainty model.
- Competitive with deep ensembles (which require 5-10x the computation) using a single deterministic model. This makes principled uncertainty estimation practical for real-time applications.
- Demonstrated on both vision (Wide-ResNet) and language (BERT) architectures, showing generality.

**Connections the authors acknowledge**: Cite Gaussian processes, spectral normalization (Miyato et al., 2018), neural tangent kernel theory, and ensemble methods. Acknowledge the connection between distance awareness and the manifold hypothesis. No citations to TDA, QEC, or dynamical systems, though the bi-Lipschitz preservation of distances is the same mathematical structure as PH stability.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Distance awareness | Stability (feature map preserves input distances) |
| Spectral normalization | Lipschitz constraint (bounded perturbation amplification) |
| GP posterior variance | Uncertainty = distance from training manifold |
| OOD input | Null (structureless / far from training support) |
| Training data manifold | The structured reference space |
| Maximum entropy prediction | Null output (uniform distribution) |
| Bi-Lipschitz map h | Distance-preserving feature extractor |
| Singular values of Jacobian | Per-layer Lipschitz constants |
| Laplace approximation of GP | Tractable posterior for distance-based uncertainty |

**Rosetta significance**: This paper provides a direct analogy between PH stability and neural uncertainty: just as PH stability guarantees that small perturbations in the input point cloud produce small changes in the persistence diagram (bottleneck <= Hausdorff), SNGP guarantees that small perturbations in input produce bounded changes in the uncertainty estimate. The spectral normalization IS a Lipschitz constraint, which IS the same mathematical structure as the stability theorems in TDA. The paper does not make this connection explicit.

---

## ContiFormer: Chen, Ren, Wang, Fang, Sun, Li (2023)
**"ContiFormer: Continuous-Time Transformer for Irregular Time Series Modeling"**
arXiv: 2402.10635 | NeurIPS 2023

**Domains bridged**: Dynamical systems (Neural ODEs) + Information theory (attention / transformer architecture)

**Domain(s)**: Machine learning, dynamical systems, time series analysis

**Abstract machines instantiated**:
- **Parameterized homology**: The continuous-time attention mechanism defines a parameterized family of attention weights. The standard Transformer computes attention at discrete time points; ContiFormer defines attention as a continuous function of time via Neural ODE dynamics. The query Q(t), key K(t), and value V(t) evolve according to ODEs: dQ/dt = f_Q(Q,t), etc. The attention A(t_i, t_j) = softmax(Q(t_i)^T K(t_j) / sqrt(d)) is a continuous function of both time indices. As time varies, the attention pattern changes — this is parameterized attention, with the parameter being continuous time rather than discrete position.
- **Stability**: The Neural ODE formulation provides inherent stability properties. The existence and uniqueness of ODE solutions (Picard-Lindelof theorem) guarantees that the continuous-time dynamics are well-defined. The paper proves an expressive power result: ContiFormer subsumes multiple existing Transformer variants (mTAND, SeFT, SEFT, etc.) as special cases under specific function hypotheses. This is a universality/stability claim: the framework is robust to the choice of variant — they all live within a single continuous family.
- **Matching**: The attention mechanism IS a matching: each query Q(t_i) is matched to all keys K(t_j) via the softmax-weighted inner product. ContiFormer extends this matching to continuous time, where the matching cost is defined by the ODE-evolved queries and keys. The reparameterization trick (solving the ODE between observation times rather than from t=0) improves computational efficiency while preserving the matching quality.

**What is genuinely new (not reducible to shared abstraction)**:
- Embedding Neural ODE dynamics inside the attention computation itself, not just using ODEs for the latent state. Previous Neural ODE methods (Latent ODE, ODE-RNN) model the state evolution as an ODE but use standard attention. ContiFormer makes the attention mechanism itself continuous-time.
- The universality result: proving that multiple existing irregular time series methods are special cases of one continuous-time framework under specific choices of the ODE right-hand side.
- The reparameterization trick for efficient continuous-time attention computation, avoiding the need to solve ODEs from t=0 for each observation.

**Connections the authors acknowledge**: Cite Neural ODEs (Chen et al., 2018), Transformer variants for irregular time series, and state space models. Explicitly position at the Neural ODE + Transformer interface. No connections to TDA, QEC, information theory (beyond attention), or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Continuous-time attention A(t_i, t_j) | Parameterized matching (continuous parameter = time) |
| Neural ODE dQ/dt = f(Q,t) | Continuous dynamics of the matching criterion |
| Query/key/value evolution | Parameterized feature evolution |
| Reparameterization trick | Efficient computation of the parameterized family |
| Picard-Lindelof existence/uniqueness | Stability guarantee for the dynamics |
| Subsumption of existing methods | Universality (all variants = special cases) |
| Irregular time series | Data with non-uniform parameterization |

**Rosetta significance**: ContiFormer bridges two abstract machines — matching (attention) and parameterized homology (continuous-time dynamics) — by making the matching itself parameterized by continuous dynamics. This is structurally analogous to computing persistence diagrams for time-varying data: the "features" (attention weights) evolve continuously as the parameter (time) changes, and the paper tracks which features persist. The universality result (existing methods as special cases) mirrors the way persistence diagrams subsume Betti numbers: the continuous object is strictly richer than any discrete snapshot.

---

## Oladyshkin, Praditia, Kroker, Mohammadi, Nowak, Otte (2023)
**"The Deep Arbitrary Polynomial Chaos Neural Network"**
arXiv: 2306.14753

**Domains bridged**: Dynamical systems (chaos theory / polynomial chaos) + Machine learning (deep neural networks)

**Domain(s)**: Uncertainty quantification, stochastic analysis, deep learning, polynomial chaos theory

**Abstract machines instantiated**:
- **Chain complex (functional decomposition)**: The key insight is that standard neural networks perform a 1st-degree polynomial expansion of inputs on each node (linear weighted sum of monomials), which from the polynomial chaos perspective implicitly assumes Gaussian distributed signals. The DaPC NN replaces this with an arbitrary-degree orthonormal polynomial basis constructed from the empirical distribution of signals at each node. The orthonormality condition means the basis functions are mutually independent — the decomposition of the neural signal into polynomial chaos components is an orthogonal decomposition analogous to the Hodge decomposition (gradient + curl + harmonic). Each component captures a specific order of interaction: 1st order = individual neuron effects, 2nd order = pairwise interactions, kth order = k-way interactions.
- **Joint-vs-marginal excess**: The higher-order polynomial terms explicitly capture interactions between neurons that are absent from the 1st-order (linear) terms. The kth-order term represents the joint effect of k neurons that is not reducible to combinations of lower-order effects. This is multi-neuron synergy — the polynomial chaos expansion decomposes the neural signal into components of increasing interaction order, with each level representing additional joint structure beyond what lower levels capture.
- **Null hypothesis**: The standard DANN (linear weighted sum + nonlinear activation) is the null model. It uses only 1st-order polynomial chaos terms and assumes (implicitly and erroneously, as the paper argues) Gaussian signal distribution. The DaPC NN tests whether higher-order interactions and data-driven (non-Gaussian) bases improve performance. The improvement quantifies the contribution of higher-order neural interactions.
- **Stability**: The orthonormality of the polynomial basis ensures that the decomposition is stable: small perturbations in the input data produce bounded changes in the polynomial chaos coefficients. This stability is inherited from the polynomial chaos expansion theory and is proven analytically. Additionally, the sensitivity indices (Sobol-type) derived from the orthonormal expansion provide a stable attribution of variance to individual neurons and interactions.

**What is genuinely new (not reducible to shared abstraction)**:
- Reinterpreting neural network computation through the lens of polynomial chaos expansion reveals that standard architectures perform an implicit (and suboptimal) 1st-order polynomial chaos. The activation function compensates for the missing higher-order terms, but imperfectly.
- Data-driven orthonormal bases on each node: the basis functions are constructed from the empirical distribution of signals arriving at that node, not assumed a priori (Hermite for Gaussian, Legendre for uniform, etc.). This makes the architecture self-adaptive to the signal distribution.
- Analytical expressions for statistical quantities (mean, variance, sensitivity indices) at each node, inherited from polynomial chaos theory. This provides built-in interpretability that standard neural networks lack.
- The potential to eliminate activation functions entirely: higher-order polynomial interactions can provide the nonlinearity that activation functions currently supply.

**Connections the authors acknowledge**: Cite polynomial chaos expansion theory (Wiener, 1938; Xiu & Karniadakis, 2002), arbitrary polynomial chaos (Oladyshkin & Nowak, 2012), and deep learning architecture design. The paper IS a bridge between uncertainty quantification / stochastic analysis and deep learning. No citations to TDA, QEC, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Polynomial chaos expansion | Orthogonal decomposition of signals (Hodge-like) |
| 1st-order terms | Marginal contributions (individual neuron effects) |
| kth-order terms | Joint contributions (k-way interaction synergy) |
| Orthonormality condition | Independence of decomposition components |
| Sensitivity indices (Sobol) | Attribution of variance to components |
| Data-driven basis | Adaptive filtration (basis constructed from data) |
| Standard DANN (linear + activation) | 1st-order null (Gaussian assumption) |
| Activation function | Compensator for missing higher-order terms |
| Arbitrary polynomial chaos (aPC) | Data-driven generalization of classical PCE |

**Rosetta significance**: The polynomial chaos decomposition of neural signals is structurally parallel to the Hodge decomposition on simplicial complexes (cf. Mollers et al., 2023): both are orthogonal decompositions where each component captures a specific type of interaction (gradient/curl/harmonic in Hodge; 1st/2nd/.../kth order in PCE). The joint-vs-marginal structure is explicit: higher-order terms ARE the joint excess beyond lower-order marginals. The connection between polynomial chaos (stochastic analysis) and Hodge decomposition (algebraic topology) is deep and unexplored — both provide graded orthogonal decompositions of signals on structured spaces, but from completely different mathematical traditions.

---

## Cross-Domain Patterns Observed

### The stability machine appears in every domain with the same structure

All eight papers above instantiate the stability machine, but from different traditions:
- **PH stability (TDA)**: bottleneck distance <= Hausdorff distance
- **Banach contraction (FDGNN)**: spectral radius < 1 ensures convergence
- **Lipschitz constraint (SNGP)**: spectral normalization bounds perturbation amplification
- **No partial erasure (QEC)**: absolute impossibility of dimension reduction
- **H-theorem (Garbaczewski)**: D_KL monotonically non-increasing
- **Generalization bound (IB)**: Delta <= sqrt(I(X;Z)/n)
- **ODE existence (ContiFormer)**: Picard-Lindelof guarantees well-defined dynamics
- **Orthonormality (DaPC NN)**: bounded coefficient perturbation from input perturbation

The mathematical form varies (Lipschitz, contraction, monotonicity, impossibility, orthogonality), but the abstract pattern is identical: bounded input change -> bounded output change.

### The orthogonal decomposition machine bridges TDA, information theory, and chaos theory

Three separate mathematical traditions have independently developed orthogonal decomposition machinery:
1. **Hodge decomposition** (TDA): gradient + curl + harmonic on simplicial complexes
2. **KL divergence Pythagoras** (information theory, Sugiyama et al.): orthogonal decomposition on posets
3. **Polynomial chaos expansion** (stochastic analysis, DaPC NN): orthogonal polynomial components of increasing interaction order

All three decompose signals on structured spaces into independent components graded by interaction order. None of the three communities cites the others.

### Disconnectivity graphs ARE persistence diagrams

Niroomand & Wales (2023) and the TDA community have developed the same mathematical object — sub-level set persistence in H_0 — from different starting points:
- **Energy landscape tradition**: disconnectivity graphs, basins of attraction, transition states
- **TDA tradition**: persistence diagrams, connected components, merging events

The vocabulary differs completely, but the objects are isomorphic. This is perhaps the most concrete "missed bridge" in the collection.

### The information bottleneck IS a topological compression

Kawaguchi et al. (2023) prove that controlling I(X;Z) bounds generalization error. In TDA terms, this means: representations with fewer persistent features (lower information content) generalize better. The information bottleneck kills unnecessary topological features, keeping only the ones relevant to the task. This is topological simplification — the same operation that persistence thresholding performs in TDA.

---

## Phase 2 Bridges (2026-04-06, session 2)

### QEC ↔ Stat Mech (Bombin & Martin-Delgado, 2007)
Color code state overlap with factorized state = 3-body Ising model partition function. Different universality classes of the associated classical spin models correspond to different computational capabilities of the QEC codes. This extends the Dennis et al. (2002) bridge (surface codes ↔ 3D Z₂ gauge theory) to a broader class of codes. arXiv: 0711.0468.

### QEC ↔ Knot Theory / TQFT (Freedman, Kitaev, Larsen, Wang, 2001)
Anyonic computation from unitary topological modular functors = Witten-Chern-Simons theory. The Jones polynomial — the same invariant underlying Khovanov homology in TDA — arises naturally in the QEC context as the computational substrate. Bridges QEC, pure math (knot invariants), and condensed matter (FQHE). arXiv: quant-ph/0101025.

### Joint Machine ↔ Param Machine (Kolchinsky, 2024)
PID redundancy = IB compression-prediction tradeoff. This is not merely an analogy: it is a formal equivalence between two abstract machines. The "RB curve" (indexed by compression β) is a parameterized family of joint-vs-marginal decompositions. Bridges information theory with itself at the machine level. arXiv: 2405.07665.

### Info Geometry ↔ OT (Wong & Yang, 2019)
Fisher-Rao metric embeds in Wasserstein space via pseudo-Riemannian framework. Statistical manifold of distributions has a natural optimal transport structure. Bridges information theory (divergences, Fisher information) with TDA (optimal transport on persistence diagrams). arXiv: 1906.00030.

### TDA ↔ Dynamical Systems (Perea & Harer, 2013)
SW1PerS: sliding window embedding of periodic time series → point cloud → Rips complex → PH. Formal bridge between Takens embedding (dynamical systems) and persistence (TDA). Maximum H₁ persistence = periodicity score. Convergence theorems. arXiv: 1307.6188.

### Info Theory ↔ Algebraic Topology (Baudot & Bennequin, 2015; Bradley, 2021)
Information cohomology: Shannon entropy is a 1-cocycle in the cochain complex of information structures. The chain rule IS the cocycle condition δH=0. Bradley strengthens: H is the UNIQUE derivation of the simplicial operad. This is the deepest bridge between information theory and algebraic topology — not analogy, but identification.

### Neuroscience ↔ Info Theory ↔ Consciousness (Tononi/Oizumi et al., 2014)
IIT 3.0: Φ = KL divergence between joint and product-of-parts transition probabilities. Connects consciousness research to formal joint-vs-marginal measures from information theory. MICS (maximally irreducible conceptual structure) is a topological invariant of the causal architecture. DOI: 10.1371/journal.pcbi.1003588.

### Neuroscience ↔ QEC via shared T² (Gardner et al., 2022)
**"Toroidal topology of population activity in grid cells"** — Nature, DOI: 10.1038/s41586-021-04268-7.
**Domains bridged**: Neuroscience + QEC (+ TDA as method)

The strongest neuro↔QEC bridge in the Rosetta. Gardner et al. use persistent cohomology on simultaneous Neuropixels recordings of hundreds of grid cells in medial entorhinal cortex and discover that the joint population activity lies on a torus T². The torus has H₁(T²,Z) = Z² — two independent 1-cycles, each encoding one periodic spatial dimension. In Kitaev's toric code (1997), the SAME torus T² serves as the base space: qubits on edges, stabilizers from ∂/δ, and logical qubits = H₁(T²,Z/2) = (Z/2)². The two independent 1-cycles in QEC encode two logical qubits; in neuroscience they encode two spatial coordinates.

**What the bridge reveals**:
- The torus T² is not an analogy — it is the SAME mathematical object arising independently in two domains. In QEC it is DESIGNED (Kitaev chose T² for its non-trivial H₁). In neuroscience it is DISCOVERED (the brain evolved it as a spatial representation).
- The two 1-cycles serve isomorphic structural roles: they define the independent degrees of freedom of the code. In QEC: two logical qubits. In neuroscience: two spatial coordinates. Both are protected by the global topology of T².
- Stability operates differently: in QEC, topological protection means errors must form non-trivial cycles (O(d) local errors) to corrupt logical information. In neuroscience, stability means the torus persists across environments and brain states. Both are robustness statements about the topological invariant, but the perturbation model differs (local quantum errors vs. environmental/state changes).
- The authors do NOT cite or acknowledge any connection to QEC or toric codes. This bridge is invisible to both communities.

**Machines in common**: Chain complex (T² with H₁), stability (topological robustness), null hypothesis (feedforward models in neuro; uncorrected noise in QEC).
**Machines unique to Gardner**: Parameterized homology (PH as method), joint-vs-marginal (population-level torus invisible from single-cell marginals).
**Machines unique to QEC**: Matching (anyon fusion/MWPM for error correction).

Full annotation: `inbox.md`.

---

## Berry, Su, Gyurik, King, Basso, Del Toro Barba, Rajput, Wiebe, Dunjko, Babbush (2023)
**"Analyzing Prospects for Quantum Advantage in Topological Data Analysis"**
arXiv: 2209.13581 | PRX Quantum 4, 040349 (2023)

**Domains bridged**: TDA + QEC (quantum algorithms)

This is the most DIRECT TDA-QEC bridge in the Rosetta: a quantum algorithm that computes TDA invariants. The paper works with the exact same chain complex (simplicial boundary operators, combinatorial Laplacian, Betti numbers) that defines both persistent homology in TDA and the code complex in QEC. The Dirac operator BG = dG + dG^{dagger} unifies boundary and coboundary; its kernel on the k-chain subspace gives the k-th Betti number.

**What the bridge reveals**:
- The chain complex is not merely analogous between TDA and QEC --- it is the SAME mathematical object serving dual roles. In TDA, boundary operators define topological features of data. In QEC, boundary operators define the code structure (stabilizers, logical operators). This paper uses quantum error-corrected hardware to compute the TDA chain complex's kernel, making the shared structure operational.
- The combinatorial Laplacian Delta = dG^{dagger} dG + dG dG^{dagger} IS the Hodge Laplacian from TDA, and its spectral properties (gap lambda_min) determine both the topological robustness of features (in TDA) and the computational complexity of the quantum algorithm (in QEC). The spectral gap serves as a stability parameter in both domains.
- The dequantization result (classical Monte Carlo on k-simplices) connects TDA to computational complexity theory: computing Betti numbers of general chain complexes is DQC1-hard (one clean qubit model). This means the homological invariants that TDA uses for data analysis are, in general, computationally hard --- a fact rarely discussed in the TDA community.
- The authors explicitly acknowledge the TDA-quantum computing connection (it IS the paper's subject). They cite both TDA literature (persistent homology, Betti numbers) and quantum algorithm literature. This is a rare acknowledged bridge.

**Machines in common across the bridge**: Chain complex (the same boundary operators), parameterized homology (filtration scale epsilon in TDA; dimension k as computational parameter in quantum), stability (spectral gap controls both feature robustness and algorithmic efficiency).
**Machine unique to the quantum side**: Null hypothesis (dequantization as classical competitor).
**Machine unique to the TDA side**: Matching (persistence matching of birth-death pairs not addressed).

Full annotation: `inbox.md`.

---

## Varley, Mediano, Patania & Bongard (2025)
**"The topology of synergy: Linking topological and information-theoretic approaches to higher-order interactions in complex systems"**
PLoS Computational Biology, DOI: 10.1371/journal.pcbi.1013649 | arXiv: 2504.10140 | 4 citations

**Domains bridged**: TDA + Information Theory + Neuroscience

This is an EXPLICIT, acknowledged cross-domain bridge. The authors set out to compare TDA (persistent homology) and information theory (O-information family) head-to-head, noting the two fields developed "largely in parallel with limited interdisciplinary cross-talk."

**What the bridge reveals**:
- **H2 cavities ARE synergy, topologically**: Three-dimensional voids in the Vietoris-Rips filtration correspond to synergistic information (O < 0). Hollow spheres and toroids are synergy-dominated; filled versions are not. Knots (locally 1D curves requiring 3D embedding) are redundancy-dominated. This is the first result connecting a specific homological dimension to a specific information-theoretic character.
- **Common metric makes the bridge tight**: Both analyses use Chebyshev (L-infinity) distance -- the KNN information estimator and the Rips filtration see identical geometry. This is not a loose analogy; the same distance matrix feeds both machines.
- **PCA destroys the bridge's content**: Dimensionality reduction (PCA) preferentially preserves redundancy and is blind to synergy. The most synergistic fMRI triads have PC1 variance near 33% (indistinguishable from independent data). This means neural manifold learning is systematically missing the topological features that carry synergistic information -- a finding with major implications for computational neuroscience.
- **Intrinsic vs. contextual**: The paper introduces a distinction between rotation-invariant "intrinsic" higher-order information (tied to topology: cavities, knots) and rotation-dependent "contextual" information (tied to embedding orientation). Intrinsic synergy persists after PCA; contextual synergy vanishes. This distinction has no prior formalization in either field.
- **No formal proof yet**: The correspondence is empirical (correlational). The authors explicitly call this "experimental mathematics." A theorem linking H2 Betti numbers to O-information remains open -- this is a gap the Rosetta should track.

**Machines in common across the bridge**:
- Chain complex (VR simplicial complex feeds both PH and the geometric basis for KNN estimation)
- Parameterized homology (Rips filtration scale as parameter; H2 features tracked)
- Joint-vs-marginal excess (O-information = TC - DTC; synergy = information in joint absent from all proper subsets)
- Null hypothesis (circular-shift null preserving autocorrelation; both PH features and information measures tested against it)
- Stability (persistence stability for TDA; KNN estimator consistency for information theory; Chebyshev metric consistency across both)

**Machine unique to the IT side**: The O-information decomposition (TC, DTC, S-information) and the PID-adjacent interpretation of synergy vs. redundancy -- TDA has no intrinsic way to distinguish synergy from redundancy.
**Machine unique to the TDA side**: The full persistence diagram (birth-death pairs, barcodes) -- the paper only uses scalar summaries (avg persistence, void count), but the full diagram is richer than any single information measure.

**Connection to Rosas (2020)**: Same family of measures. Rosas uses O-information/PhiID to define causal emergence (Psi > 0 iff synergy at the macro level). Varley now shows that the synergy Rosas cares about has a topological interpretation: it corresponds to H2 cavities. This chain -- causal emergence via PID synergy (Rosas) -> synergy as H2 topology (Varley) -- is a two-hop bridge from information-theoretic emergence to persistent homology.

Full annotation: `inbox.md` (Wave 7).

---

## Wave 10a — link-forge Cross-Domain Bridges (2026-04-17)

### Baudot, Tapia, Bennequin & Goaillard (2019)
**"Topological Information Data Analysis"**
arXiv: 1907.04242

**Domains bridged**: Information theory + TDA

The paper constructs an explicit simplicial complex of random variables where entropy and MI are co-chains with cohomological structure (δH = I_2). The Borromean link interpretation of synergy connects combinatorial topology to information decomposition. Bethe free energy as alternating sum over simplicial faces bridges variational inference and algebraic topology. Authors explicitly cite PH (Edelsbrunner, Carlsson) and neural simplicial complexes (Reimann 2017). Application to gene expression (neuroscience/genomics).

**Bridge quality**: Explicit. Authors fully aware of bridging TDA and information theory. The topos-cohomological framework of Baudot-Bennequin (2015) is the theoretical foundation connecting these communities.

### Ghorbanchian, Restrepo, Torres & Bianconi (2020)
**"Higher-order simplicial synchronization of coupled topological signals"**
Nature Comms Physics, DOI: 10.1038/s42005-021-00605-4

**Domains bridged**: Dynamical systems + TDA

Hodge Laplacian from TDA drives synchronization dynamics on simplicial complexes. The chain complex structure (boundary operators, spectral gap) determines the phase transition. Topological signals on k-simplices are a genuinely new dynamical concept. Tested on real connectomes (neuroscience data). Authors cite both TDA foundations and Kuramoto synchronization.

**Bridge quality**: Explicit and structural. The boundary operator IS the coupling mechanism — topology dictates dynamics.

### Dey, Mrozek & Slechta (2021)
**"Persistence of Conley-Morse Graphs in Combinatorial Dynamical Systems"**
arXiv: 2107.02115

**Domains bridged**: TDA + Dynamical systems

Zigzag persistence (TDA tool) applied to Conley-Morse graphs (dynamical systems object). The Conley index (relative homology) is a chain complex invariant; persistence tracks it parametrically. Noise-resilient index pairs are a stability construction bridging computational topology and dynamical systems.

**Bridge quality**: Deep structural bridge. The paper is situated squarely at the TDA-dynamics intersection, building on zigzag persistence (Carlsson-de Silva) and Conley theory (Mischaikow-Mrozek).

### Petri, Expert, Turkheimer, Carhart-Harris, Nutt, Hellyer & Vaccarino (2014)
**"Homological scaffolds of brain functional networks"**
J. R. Soc. Interface, DOI: 10.1098/rsif.2014.0873. 657 citations.

**Domains bridged**: Neuroscience + TDA

PH applied to brain fMRI correlation networks. The homological scaffold is a novel construction that transforms PH output back into a network, bridging the TDA and network science communities. Psilocybin experiments provide empirical validation. Authors explicitly cite both Edelsbrunner/Harer/Carlsson (TDA) and Bullmore/Sporns (brain networks).

**Bridge quality**: Explicit and methodologically innovative. One of the most-cited papers bridging TDA and neuroscience. The scaffold construction operationalizes TDA for network science.

### Donato, Gori, Pettini, Petri, De Nigris, Franzosi & Vaccarino (2016)
**"Persistent Homology analysis of Phase Transitions"**
arXiv: 1601.03641

**Domains bridged**: Dynamical systems (statistical mechanics) + TDA

First application of PH to detect phase transitions via configuration space topology. Rips complex on dynamically sampled points; energy density parameterizes submanifolds. MFXY model shows H_1 topological signal at phase transition; φ^4 model serves as negative control with no signal. Persistence landscapes with statistical confidence bands. Petri (homological scaffolds) is coauthor, connecting to the neuroscience-TDA bridge. Authors cite both TDA foundations (Edelsbrunner, Carlsson) and topological theory of phase transitions (Pettini 2007).

**Bridge quality**: Explicit. Bridges computational topology and statistical mechanics at the methodological level. The dual positive/negative model benchmark is methodologically exemplary.
