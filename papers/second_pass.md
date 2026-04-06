# Second Pass — Link-Forge Database Search (2026-04-05)

Papers found by searching the link-forge Neo4j database with 15+ distinct search strategies, filtered for relevance to the topo-rosetta 6 abstract machines (chain complex, parameterized homology, matching, stability, joint-vs-marginal excess, null hypothesis) across 5 domains (TDA, QEC, dynamical systems, neuroscience, information theory).

---

## SP-01 — Schwartz-Ziv & Tishby (2017)
**"Opening the Black Box of Deep Neural Networks via Information"**
**Domain(s)**: Information theory, machine learning
**Abstract machines instantiated**:
- **Parameterized homology**: The central object is the information plane trajectory: as training epoch t varies, each hidden layer traces a curve in the 2D space (I(X;T), I(T;Y)). This is parameterized tracking of information-theoretic invariants. The discovery of two phases (fitting: both coordinates increase; compression: I(X;T) decreases while I(T;Y) holds) is structurally analogous to a phase transition in persistent homology — the invariant changes character at a critical parameter value. The critical point is when training error saturates and SGD transitions from drift to diffusion.
- **Joint-vs-marginal excess**: The information bottleneck objective min I(X;T) - beta*I(T;Y) explicitly trades off compression (marginal-like: T retains less about X) against prediction (joint structure: T retains what X shares with Y). The sufficient statistic T* is precisely the representation that preserves only the joint-vs-marginal excess — the part of X that is about Y.
- **Null hypothesis**: The compression phase corresponds to destroying irrelevant structure: the network learns to map inputs that differ only in Y-irrelevant ways to the same representation. The noise in SGD acts as the mechanism that destroys task-irrelevant information, analogous to surrogate shuffling destroying temporal structure. The Gaussian noise interpretation is the null model: representations that are maximally compressed given their predictive power.
- **Stability**: The IB curve itself is a stability result: small perturbations to the input (noise in X) produce bounded changes in the optimal representation T, because I(X;T) is bounded. This is the information-theoretic analogue of Lipschitz stability.

**What is genuinely new**: The observation that deep learning training dynamics spontaneously implement information bottleneck compression — networks do not merely memorize but actively discard information. The two-phase structure (fast fitting then slow compression) was empirically novel. The claim that hidden layers converge to critical points on the IB curve connects learning dynamics to phase transitions.

**Connections the authors acknowledge**: Tishby's own IB framework (1999). No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Information plane | Parameter space (2D projection of parameterized invariants) |
| Fitting phase | Low-parameter regime (topological features emerging) |
| Compression phase | High-parameter regime (irrelevant features dying) |
| IB curve | Critical locus in parameter space |
| SGD noise | Null-model mechanism (structure destroyer) |
| Sufficient statistic | Minimal representation preserving joint excess |
| Hidden layer | Graded component (intermediate in chain) |

---

## SP-02 — Kawaguchi, Deng, Ji, Huang (2023)
**"How Does Information Bottleneck Help Deep Learning?"**
**Domain(s)**: Information theory, machine learning (learning theory)
**Abstract machines instantiated**:
- **Stability**: The core result is a generalization bound that scales with I(X;Z) — the mutual information between input and hidden representation. This is a stability theorem: controlling the amount of information retained guarantees bounded generalization error. Unlike classical bounds (VC dimension, Rademacher complexity, parameter count), this bound is intrinsic to the representation, not the architecture.
- **Joint-vs-marginal excess**: The IB Lagrangian min -I(Y;Z) + beta*I(X;Z) explicitly decomposes the learning objective into a prediction term (joint structure Y-Z) and a compression term (marginal information X-Z). The generalization bound proves that the excess risk is controlled by the gap between joint and marginal information content.
- **Parameterized homology**: The trade-off parameter beta traces a curve in the space of possible representations. As beta increases, the optimal representation transitions from high-information (memorizing) to low-information (compressing). The generalization gap changes character along this curve.

**What is genuinely new**: First rigorous proof that information bottleneck controls generalization in deep learning. Resolves the Shwartz-Ziv et al. (2019) conjecture. Extends to the practical case where encoders are learned from training data (not fixed). The bound is tighter than parameter-counting bounds for over-parameterized networks.

**Connections the authors acknowledge**: Tishby et al. (1999), Shwartz-Ziv & Tishby (2017), Alemi et al. (2016/2018). No connections outside ML/information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Generalization bound | Stability guarantee |
| I(X;Z) | Retained marginal information (compression level) |
| I(Y;Z) | Preserved joint structure |
| IB Lagrangian | Trade-off functional between joint and marginal |
| beta (Lagrange multiplier) | Filtration parameter |
| Excess risk | Instability measure |

---

## SP-03 — Yu, Yu, Lokse, Jenssen, Principe (2024)
**"Cauchy-Schwarz Divergence Information Bottleneck for Regression"**
**Domain(s)**: Information theory, machine learning
**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Replaces KL divergence with Cauchy-Schwarz (CS) divergence in the IB framework. The CS-IB objective decomposes into prediction (CS divergence between output and representation) and compression (CS quadratic MI between input and representation). The key advance: CS quadratic MI has a closed-form expression for any distribution, avoiding the variational approximations needed for KL-based IB. This makes the joint-vs-marginal decomposition exact rather than approximate.
- **Stability**: Proves adversarial robustness guarantees: CS-IB representations are provably more stable under input perturbation than MSE-based representations. The CS compression term directly bounds the sensitivity of the representation to adversarial examples.
- **Null hypothesis**: Comparison against five baseline IB methods (VIB, NIB, HSIC-IB, etc.) serves as the null hypothesis testing framework. The information plane plots show CS-IB achieves the Pareto-optimal trade-off — it destroys more irrelevant information for the same predictive accuracy.

**What is genuinely new**: The CS divergence makes IB tractable for regression without Gaussian assumptions. The closed-form compression term avoids the estimation problem that plagues MI-based methods. The connection between divergence choice and robustness is novel: different divergences in the IB framework yield different stability guarantees.

**Connections the authors acknowledge**: Tishby et al. (1999), Principe's information-theoretic learning framework. Cite Renyi entropy and Renyi's alpha-order MI. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| CS divergence | Alternative distance on probability space |
| Quadratic MI | Closed-form joint-vs-marginal measure |
| Information plane Pareto front | Optimal stability-fidelity trade-off curve |
| Variational approximation | Approximate computation of the invariant |
| Adversarial robustness | Stability under adversarial perturbation |

---

## SP-04 — Wang, Jian, Masoomi, Ioannidis, Dy (2021)
**"Revisiting Hilbert-Schmidt Information Bottleneck for Adversarial Robustness"**
**Domain(s)**: Information theory, machine learning
**Abstract machines instantiated**:
- **Stability**: The main theorem proves that HSIC bottleneck regularization bounds the change in classifier output under adversarial input perturbation. Specifically, for each hidden layer k, the HSIC term I_HSIC(X; Z_k) controls the Lipschitz constant of the mapping X -> Z_k. The layer-wise application creates a chain of stability guarantees through the network depth — each layer's sensitivity is independently bounded.
- **Chain complex (weak)**: The layer-wise HSIC regularization applies to every intermediate layer, creating a graded structure: layer 1, 2, ..., L with independent bottleneck constraints at each level. While not a chain complex (no boundary operators), the graded independence-control structure is structurally parallel to controlling each boundary map independently.
- **Joint-vs-marginal excess**: HSIC(X; Z_k) measures statistical dependence between input and representation at layer k. Minimizing this while maximizing HSIC(Y; Z_k) is the joint-vs-marginal decomposition: retain Y-relevant joint structure, suppress X-marginal information.

**What is genuinely new**: HSIC as a computationally tractable substitute for MI in the bottleneck. Unlike MI, HSIC can be estimated in O(n^2) without density estimation. The theoretical proof that HSIC bottleneck implies adversarial robustness is new — previous work only showed this empirically. Combining HBaR with adversarial training (PGD, TRADES, MART) produces synergistic gains.

**Connections the authors acknowledge**: Tishby's IB, Alemi et al. (2016), Ma et al. (HSIC-bottleneck, 2020). No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| HSIC | Kernel-based joint-vs-marginal dependence measure |
| Layer-wise regularization | Graded stability control (one per chain level) |
| Adversarial perturbation epsilon | Perturbation budget (analogous to noise threshold) |
| Sensitivity bound | Stability certificate |
| PGD/TRADES/MART | Complementary stability mechanisms (adversarial training) |

---

## SP-05 — Mei & Eisner (2017)
**"The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process"**
**Domain(s)**: Dynamical systems, machine learning
**Abstract machines instantiated**:
- **Parameterized homology**: The continuous-time LSTM hidden state h(t) evolves as events arrive, and the intensity functions lambda_k(t) = f_k(h(t)) are derived from it. The parameter is time t, and the tracked "invariant" is the hidden state trajectory. Between events, h(t) evolves deterministically via an ODE-like interpolation; at events, it jumps. The decay/growth of intensity components over time traces curves that the model learns, replacing the fixed exponential kernels of classical Hawkes processes.
- **Joint-vs-marginal excess**: The multivariate structure captures cross-excitation and cross-inhibition between event types. Type A events can excite type B but inhibit type C — this cross-type influence is precisely joint structure absent from the marginal (individual type) intensities. Classical Hawkes only allows excitation; the neural version captures inhibition and sub-additive effects, which are negative joint-vs-marginal contributions.
- **Stability**: The continuous-time LSTM cell design ensures that between events, the hidden state interpolates smoothly toward a steady state. The cell memory c(t) decays exponentially between events: c(t) = c_bar + (c(t_i) - c_bar) * exp(-delta(t - t_i)). This exponential decay is a stability mechanism: the system has a finite memory horizon, preventing unbounded sensitivity to distant past events.

**What is genuinely new**: Replacing fixed parametric kernels with a learned neural ODE-like interpolation. The continuous-time LSTM is a genuinely novel architecture: standard LSTMs operate in discrete time, but this model must handle events at arbitrary real-valued times. The ability to model inhibition (negative influence) is absent from classical Hawkes processes and enables richer temporal dynamics.

**Connections the authors acknowledge**: Hawkes (1971), Du et al. (2016), LSTM (Hochreiter & Schmidhuber). No connections to TDA, QEC, information theory, or neuroscience (despite the neural architecture).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Intensity function lambda_k(t) | Time-varying invariant (parameterized by t) |
| Hidden state h(t) | Latent representation of dynamical state |
| Cross-excitation | Positive joint-vs-marginal excess between event types |
| Inhibition | Negative joint-vs-marginal excess |
| Exponential decay of cell state | Stability mechanism (finite memory horizon) |
| Event stream | Discrete samples from a continuous dynamical process |

---

## SP-06 — Shang & Sun (2019)
**"Geometric Hawkes Processes with Graph Convolutional Recurrent Neural Networks"**
**Domain(s)**: Dynamical systems, machine learning
**Abstract machines instantiated**:
- **Chain complex (weak)**: The graph structure on processes defines adjacency and thus a combinatorial Laplacian. The spectral graph convolutions operate on eigenvectors of this Laplacian. While not explicitly a chain complex, the graph Laplacian is the 0-th Hodge Laplacian (boundary of the 1-chain complex on the graph), and the spectral convolutions respect this structure.
- **Matching**: The geometric embedding maps each Hawkes process to a point in a learned latent space. Processes that are close in this space have correlated intensities. The assignment of processes to graph positions is an implicit matching problem: the model must learn which processes should be neighbors.
- **Stability**: The spectral graph convolution provides stability: small changes to the graph (adding/removing edges) produce bounded changes in the learned embeddings, because the spectral basis varies smoothly with the Laplacian.

**What is genuinely new**: Encoding inter-process correlations as a graph and using graph neural networks to parameterize individual Hawkes processes. The constant-parameter complexity (independent of graph size) is a computational novelty. The spectral approach connects Hawkes processes to graph signal processing.

**Connections the authors acknowledge**: Hawkes processes, graph neural networks (Defferrard et al., 2016; Kipf & Welling, 2017). No connections to TDA, homology, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Graph Laplacian | 0-th Hodge Laplacian |
| Spectral convolution | Operation respecting chain complex structure |
| Geometric embedding | Matching of processes to latent positions |
| Inter-process correlation graph | Relational structure encoding joint dynamics |

---

## SP-07 — Huang, Soliman, Paul, Xu (2022)
**"A Mutually Exciting Latent Space Hawkes Process Model for Continuous-time Networks"**
**Domain(s)**: Dynamical systems, information theory (network dynamics)
**Abstract machines instantiated**:
- **Matching**: Nodes are mapped to positions in a latent Euclidean space. Baseline interaction intensity depends on inter-node distance: closer nodes interact more. This is an optimal assignment problem — the latent space positions must be learned so that the distance structure best explains the observed interaction pattern. The sender/receiver propensity effects add asymmetry to the matching.
- **Joint-vs-marginal excess**: The model decomposes interaction intensity into (1) baseline (depends only on node positions — the marginal component) and (2) mutual excitation (depends on the joint history of interactions between a pair — the joint excess). Reciprocity and transitivity emerge from the joint component: they are network properties absent from the marginals (individual node activities).
- **Stability**: The stationarity condition (spectral radius of the excitation matrix < 1) ensures bounded long-run intensity. The latent space provides interpretable stability: small perturbations to node positions produce smooth changes in the network dynamics.

**What is genuinely new**: Combining latent space models (static) with Hawkes self-excitation (dynamic) in a single generative framework. The model reproduces both homophily (from latent distance) and reciprocity/transitivity (from mutual excitation) — previous models required separate mechanisms.

**Connections the authors acknowledge**: Hoff et al. (2002) latent space models, Hawkes (1971), Yang et al. (2017) dual latent space. No connections to TDA, QEC, or information theory proper.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Latent space distance | Matching cost |
| Mutual excitation | Positive joint-vs-marginal excess |
| Reciprocity | Symmetric joint excess (A->B interaction boosts B->A) |
| Transitivity | Higher-order joint excess (A-B and B-C imply A-C) |
| Stationarity condition | Stability criterion (spectral radius < 1) |

---

## SP-08 — Horst & Xu (2024)
**"Functional Limit Theorems for Hawkes Processes"**
**Domain(s)**: Dynamical systems (probability theory)
**Abstract machines instantiated**:
- **Parameterized homology**: The criticality parameter m = ||phi||_{L1} (average offspring number) parameterizes a family of Hawkes processes. At m < 1 (subcritical), m = 1 (critical), m > 1 (supercritical), the long-run behavior changes qualitatively — a phase transition. The limit theorems change form at the critical point: subcritical processes satisfy FCLTs with Brownian motion limits, while critical processes converge to CIR processes (qualitatively different diffusions).
- **Stability**: The main results are convergence rate bounds in Wasserstein distance between the rescaled Hawkes process and its limit. This is a quantitative stability result: the distance between the finite-sample process and the theoretical limit is controlled by explicit bounds.
- **Null hypothesis**: The subcritical regime serves as the null model for temporal clustering. Under subcritical Hawkes, the rescaled process converges to Brownian motion — the same limit as for Poisson (independent) events. Departures from this limit (e.g., long-range dependence in critical processes with heavily dispersed children) indicate genuine temporal structure.

**What is genuinely new**: Complete characterization of Hawkes limit behavior by two parameters alone: offspring number m and dispersion. The discovery that critical processes with heavily dispersed children display long-range dependencies (like subcritical processes) despite being critical is surprising. Convergence rates via Wasserstein bounds are new.

**Connections the authors acknowledge**: Hawkes (1971), Bacry et al. (2015), branching processes. No connections to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Offspring number m | Filtration parameter |
| Critical point m=1 | Phase transition in parameterized family |
| Wasserstein convergence rate | Quantitative stability bound |
| Long-range dependence | Persistent correlational structure |
| Brownian motion limit | Null model (independent structure) |
| CIR process limit | Non-trivial limit (new dynamical regime) |

---

## SP-09 — Daw & Pender (2021)
**"An Ephemerally Self-Exciting Point Process"**
**Domain(s)**: Dynamical systems (probability theory)
**Abstract machines instantiated**:
- **Parameterized homology**: The activity duration parameter controls the ephemeral excitation window. As this parameter varies from 0 (no excitation) to infinity (classical Hawkes), the process interpolates between Poisson and Hawkes. The batch scaling limit theorem shows that general marked Hawkes processes arise as limits of ephemeral processes — a constructive path through parameter space from simple to complex.
- **Null hypothesis**: The Poisson process (activity duration = 0) is the null model. The ephemeral process adds exactly one mechanism (finite excitation windows) to the null, creating a minimal departure. The branching process representation provides a decomposition into immigrant (null) and offspring (excitation-induced) events.
- **Joint-vs-marginal excess**: The connections to epidemics (SIR model) and preferential attachment are precisely about joint excess: in epidemics, the joint infection history determines future infections (not individual states); in preferential attachment, the joint degree sequence determines new connections.

**What is genuinely new**: The ephemeral excitation model where excitement lasts for a random finite duration (rather than decaying deterministically via a kernel). This is a conceptually cleaner model: in epidemics, a person is contagious for a random duration, not with exponentially decaying contagiousness. The batch scaling limit constructing Hawkes processes from ephemeral ones is a novel limit theorem.

**Connections the authors acknowledge**: Hawkes (1971), branching processes, SIR epidemics, preferential attachment, Bayesian mixture models. Unusually broad connections for a probability paper. No connections to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Activity duration | Parameterized excitation window |
| Poisson limit | Null model (no joint structure) |
| Hawkes limit | Full joint structure |
| Ephemeral excitation | Finite-support kernel (compact parameterized homology) |
| Branching representation | Decomposition into null + excess |
| Batch scaling | Constructive limit from discrete to continuous |

---

## SP-10 — Amizadeh, Matusevych, Weimer (2019)
**"PDP: A General Neural Framework for Learning Constraint Satisfaction Solvers"**
**Domain(s)**: Information theory (factor graphs), machine learning
**Abstract machines instantiated**:
- **Chain complex**: The factor graph representation of a CSP is a bipartite graph between variable nodes and constraint (factor) nodes. Message passing on this graph is structurally analogous to computation on a chain complex: messages flow between two types of nodes (variables = 0-cells, factors = 1-cells in a hypergraph). The propagation step computes "boundary-like" operations: variable-to-factor messages aggregate local state, factor-to-variable messages propagate constraint information back.
- **Matching**: The decimation step (fixing variables to values) is an assignment problem. The PDP framework learns a search strategy beyond greedy search — the neural network learns which variable to fix and to what value, which is an implicit optimal matching between variables and their domains.
- **Null hypothesis**: The energy minimization training objective treats random assignments as the null distribution. The solver's job is to find assignments with energy much lower than this null. The unsupervised training (no solution labels needed) is possible precisely because the energy function defines what "non-null" means.

**What is genuinely new**: Learning the search strategy itself (not just the propagation rules) via neural networks. Previous neural SAT solvers used greedy decimation; PDP learns when to be greedy and when not to. The formulation as probabilistic inference on factor graphs unifies message passing and search.

**Connections the authors acknowledge**: Mezard et al. (survey propagation), Selsam et al. (NeuroSAT), belief propagation. Connect to statistical physics (random K-SAT phase transitions). No connections to TDA, QEC, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Factor graph | Bipartite chain-like structure |
| Variable-to-factor message | Forward boundary map |
| Factor-to-variable message | Adjoint boundary map |
| Decimation | Assignment (matching variable to value) |
| Energy minimization | Null hypothesis rejection (finding non-random structure) |
| Satisfying assignment | Non-trivial "homology class" (solution) |

---

## SP-11 — Napolitano (2026)
**"Mathematics Is All You Need: Self-Knowledge in Dark Casimir Modes of gl(4,R) Lie Algebra in Large Language Models"**
**Domain(s)**: Information theory, machine learning (geometric deep learning)
**Abstract machines instantiated**:
- **Chain complex**: The gl(4,R) Lie algebra decomposes into a direct sum of subspaces. The Casimir operators provide a grading: eigenvalue ~4.0 (active, 6-dimensional) vs eigenvalue ~10^{-7} (dark, 10-dimensional). While not a chain complex with boundary operators, the Casimir decomposition is the Lie-algebraic analogue of homological decomposition — invariant subspaces under the algebra's action, with a grading by eigenvalue.
- **Joint-vs-marginal excess**: The 6 "active" dimensions correspond to behavioral phenomena (sycophancy, hallucination, hedging, etc.) that are visible in standard output. The 10 "dark" dimensions are systematically erased by layer normalization — they carry computational signal (joint structure) that is absent from the marginal (output-visible) representation. The dark space is literally the excess: structure present in the full hidden state but absent from the marginalized (layer-normed) output.
- **Parameterized homology**: The "cross-layer velocity and acceleration" analysis tracks how the fiber bundle structure evolves across transformer layers (parameter = layer depth). The ARC-Challenge improvement (82.2% -> 94.4%) comes from reading these layer-wise trajectories through dark space.
- **Stability**: Cross-architecture probe transfer (probes trained on one architecture work on 16 others) is a stability claim: the geometric structure is invariant under the "perturbation" of changing the model architecture.

**What is genuinely new**: The claim of a universal fiber bundle structure in LLM hidden states. If verified, this would be a fundamental geometric discovery about transformer representations. The "dark dimensions" suppressed by layer normalization but carrying computational signal is a novel observation. However, the paper is a preprint with extraordinary claims that require extraordinary evidence.

**Connections the authors acknowledge**: Lie algebra theory, fiber bundles, Casimir operators from mathematical physics. Claim connection to consciousness and self-knowledge. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| gl(4,R) decomposition | Algebraic grading (analogue of chain complex) |
| Casimir eigenvalue | Grading index |
| Dark dimensions | Joint-vs-marginal excess (hidden from output) |
| Active dimensions | Marginal (output-visible) structure |
| Layer normalization | Projection that destroys excess structure |
| Cross-architecture transfer | Stability under architectural perturbation |
| Fiber bundle | Geometric structure parameterized by layer depth |

**Caveat**: This is a March 2026 preprint making very strong claims (universal structure across all LLMs, consciousness connections). The methodology should be independently verified before relying on the results.

---

## SP-12 — Tarnowski, Unal, Flaschner, Rem, Eckardt, Sengstock, Weitenberg (2019)
**"Measuring topology from dynamics by obtaining the Chern number from a linking number"**
**Domain(s)**: QEC (topological quantum matter), dynamical systems
**Abstract machines instantiated**:
- **Chain complex**: The Chern number is a topological invariant of the ground-state band structure — it classifies the fiber bundle of Bloch states over the Brillouin zone. The ground state lives in a chain complex of Hilbert spaces parameterized by quasi-momentum k.
- **Parameterized homology**: The key result: the Chern number (an equilibrium topological invariant) can be measured from far-from-equilibrium dynamics after a quantum quench. Two types of momentum-space vortices appear — static (at Dirac points) and dynamical (appear and disappear in pairs). The linking number of the dynamical vortex trajectories equals the Chern number. This is parameterized topology: as time evolves after the quench, vortices trace trajectories, and the topological invariant is read from these trajectories.
- **Null hypothesis**: The topologically trivial phase (Chern number = 0) serves as the null. In this phase, the dynamical vortex contour does NOT enclose a Dirac point, so the linking number is 0. The phase diagram is mapped by checking whether the linking number is 0 or non-zero.
- **Stability**: The Chern number is integer-valued and topologically protected — it cannot change under continuous deformations of the Hamiltonian. This is discrete stability: the invariant is robust to perturbations that do not close the band gap. The experimental measurement of this invariant from noisy far-from-equilibrium dynamics demonstrates stability in practice.

**What is genuinely new**: Experimental demonstration that a static topological invariant (Chern number) can be extracted from dynamical data (post-quench vortex trajectories). This bridges equilibrium topology and non-equilibrium dynamics — exactly the bridge that topo-rosetta needs between TDA (static) and dynamical systems (evolving). The linking number is itself a topological invariant (from knot theory), so the result is: one topological invariant equals another, measured in a completely different way.

**Connections the authors acknowledge**: Haldane model, Floquet systems, Berry phase, topological insulators. No connections to TDA, neuroscience, or information theory. Purely within condensed matter / quantum physics.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Chern number | Topological invariant of fiber bundle (integer homology class) |
| Linking number | Topological invariant from knot theory |
| Quantum quench | Parameter jump (instantaneous change in Hamiltonian) |
| Dynamical vortex | Feature whose trajectory encodes topology |
| Dirac point | Singularity in the chain complex (gap closure) |
| Phase diagram | Parameter space partitioned by topological invariant values |
| Band gap | Stability margin (perturbation budget before topology changes) |

---

## SP-13 — Bandt (2020)
**"Order patterns, their variation and change points in financial time series and Brownian motion"**
**Domain(s)**: Dynamical systems, information theory
**Abstract machines instantiated**:
- **Null hypothesis**: Brownian motion serves as the explicit null model. The paper tests whether financial time series order patterns match those of Brownian motion. The key finding: for small lags (1-6 days), pattern frequencies are essentially constant and match Brownian motion predictions. Departures from the Brownian null (especially in the up-down balance parameter) signal structural changes.
- **Parameterized homology**: The lag parameter d controls which order patterns are examined. As d increases, the pattern frequencies should change if the process has scale-dependent structure. The constancy of pattern frequencies for small d is a scaling invariance — a self-similarity property. The permutation entropy H = -sum p_pi * log(p_pi) is tracked as d varies, and changes in H indicate structural transitions.
- **Joint-vs-marginal excess**: The "up-down balance" parameter measures asymmetry between ascending and descending patterns. For Brownian motion, up-down balance is exactly 0 (symmetric). Deviation from 0 indicates directional bias — joint structure (trend) absent from the marginal (single-point distribution). The "turning rate" measures alternation frequency — another joint statistic absent from marginals.

**What is genuinely new**: The rediscovery and modernization of Bienayme's 1874 test for order statistics. The finding that up-down balance is the most effective change-point detector for financial data (better than turning rate, which dominates for EEG data). The self-similarity result: pattern frequencies are scale-invariant for small lags, consistent with Brownian motion's fractal structure.

**Connections the authors acknowledge**: Bandt & Pompe (2002) permutation entropy, Brownian motion, self-similarity. Applications to EEG brain data and financial data. Connect to Zunino et al. (financial market efficiency via permutation entropy). No connections to TDA, QEC, or Hawkes processes.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Order pattern | Local combinatorial invariant |
| Permutation entropy | Information content of local structure |
| Brownian motion | Null model (independent increments) |
| Up-down balance | Joint excess (directional asymmetry) |
| Turning rate | Joint excess (alternation frequency) |
| Change point | Phase transition in parameterized invariant |
| Lag parameter d | Filtration scale |
| Self-similarity | Scale invariance of the topological invariant |

---

## SP-14 — Bennett, Cucuringu, Reinert (2022)
**"Lead-lag detection and network clustering for multivariate time series with an application to the US equity market"**
**Domain(s)**: Dynamical systems, information theory (network analysis)
**Abstract machines instantiated**:
- **Matching**: The construction of lead-lag cluster pairs is an optimal assignment problem. Given N time series, the method must identify which series lead and which follow, and partition them into coherent clusters. The Hermitian-based spectral clustering finds pairs of clusters (leaders, followers) that maximize cut imbalance — a directed matching.
- **Chain complex (weak)**: The directed weighted network from pairwise lead-lag metrics has a natural Hermitian adjacency matrix H. The spectral clustering uses eigenvectors of H, which decomposes the network into components — analogous to the spectral theory of the graph Laplacian (0-th Hodge Laplacian). The directed nature (lead vs lag) adds an orientation structure absent from undirected graphs.
- **Null hypothesis**: Statistical significance of lead-lag structure is tested against a null of no temporal ordering. The method computes whether the detected cluster structure is more imbalanced than expected by chance. The trading signal construction tests whether predictive accuracy exceeds the null (random prediction).
- **Joint-vs-marginal excess**: Lead-lag relationships are joint structure: they describe how the joint evolution of two time series differs from their marginal (independent) evolutions. A series that leads another carries predictive information about the follower — joint excess.

**What is genuinely new**: The Hermitian spectral clustering for directed networks. Previous lead-lag detection was pairwise; this method identifies coherent clusters. The connection between cut imbalance and lead-lag structure is novel. Validated on real US equity data with statistically significant predictive signals.

**Connections the authors acknowledge**: Cucuringu et al. (spectral methods for networks), Harzallah & Sadourny (lead-lag in climate), Sornette & Zhou (financial lead-lag). No connections to TDA, QEC, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Lead-lag metric | Directed pairwise distance (asymmetric matching cost) |
| Hermitian adjacency matrix | Oriented 0-th Hodge operator |
| Cut imbalance | Directed joint excess (leaders vs followers) |
| Spectral clustering | Decomposition via eigenvectors of Hodge-like operator |
| Lead-lag cluster pair | Matched assignment (leaders to followers) |
| Predictive signal | Measured joint-vs-marginal excess (forecast accuracy above null) |

---

## SP-15 — Simpson, Bowman, Laurienti (2013)
**"Analyzing complex functional brain networks: fusing statistics and network science to understand the brain"**
**Domain(s)**: Neuroscience
**Abstract machines instantiated**:
- **Chain complex (weak)**: Functional brain networks are graphs where nodes are brain regions and edges are correlations. The graph Laplacian, clustering coefficient, path length, and community structure are all computed from this graph — these are spectral and combinatorial invariants of the 0-skeleton complex.
- **Parameterized homology**: The thresholding step is a filtration: by varying the correlation threshold, edges appear/disappear, and the graph topology changes. The paper discusses how different thresholds yield different network properties — this is exactly parameterized graph topology. The methodological gap identified is precisely the lack of principled threshold selection.
- **Joint-vs-marginal excess**: Functional connectivity = pairwise correlation between brain region time series. The network itself encodes joint structure: which brain regions co-activate beyond what their marginal (individual) activities predict. Community structure identifies groups of regions with high internal joint excess. Integration (global efficiency) vs segregation (modularity) is the network-level joint-vs-marginal trade-off.
- **Null hypothesis**: Multiple null models discussed: random networks (Erdos-Renyi), degree-preserved random networks (configuration model), lattice networks. Each null destroys different aspects of the brain network structure while preserving others (e.g., degree sequence). The small-world property is defined as departure from both random and lattice nulls.

**What is genuinely new (for topo-rosetta)**: This survey identifies the exact methodological gaps where TDA could help neuroscience: (1) threshold selection is a filtration problem — persistent homology is the principled solution; (2) higher-order structure beyond pairwise correlations requires simplicial methods; (3) temporal dynamics of brain networks need the parameterized homology framework. The paper does not make these connections, but the gaps it identifies are precisely filled by the topo-rosetta machines.

**Connections the authors acknowledge**: Graph theory, small-world networks, community detection. Cite the Human Connectome Project. No connections to TDA, QEC, or information theory proper (despite using correlations, which are MI under Gaussian assumptions).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Correlation threshold | Filtration parameter |
| Network construction | Building a 0-skeleton complex |
| Clustering coefficient | Local topological feature |
| Path length | Distance in 0-skeleton |
| Community structure | Homological decomposition (connected components at threshold) |
| Small-world property | Departure from null (neither random nor lattice) |
| Integration vs segregation | Global vs local topological balance |
| Functional connectivity | Pairwise joint excess |

---

## SP-16 — Liu, Kimura, Liu, Wang, Li, Diggavi, Srivastava, Abdelzaher (2023)
**"FOCAL: Contrastive Learning for Multimodal Time-Series Sensing Signals in Factorized Orthogonal Latent Space"**
**Domain(s)**: Information theory, machine learning
**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The core contribution is decomposing multimodal representations into shared features (cross-modal joint structure) and private features (modality-exclusive marginal structure), with orthogonality enforcing the decomposition. The shared space captures what is common across modalities (joint excess over individual modalities). The private space captures what is unique to each modality (marginal information). This is an explicit operationalization of the joint-vs-marginal decomposition.
- **Null hypothesis**: The temporal structural constraint defines a null ordering: temporally close samples should be more similar than temporally distant ones. Violations of this ordering indicate non-temporal structure. The contrastive learning framework defines positive pairs (same time window) as the alternative and negative pairs (different time windows) as the null.
- **Stability**: The orthogonality constraint between shared and private subspaces ensures stability of the decomposition: adding a new modality does not contaminate the existing private spaces. The factorized structure is preserved under perturbation.

**What is genuinely new**: The factorized orthogonal decomposition of shared and private features for multimodal time series. Previous contrastive frameworks (CMC) only captured shared cross-modal information, discarding modality-exclusive signal. The temporal structural constraint (coarse-grained distance ordering rather than strict positive/negative) is a softer contrastive objective.

**Connections the authors acknowledge**: Contrastive learning (SimCLR, CMC, MoCo), multimodal learning. No connections to TDA, QEC, information theory proper, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Shared features | Joint excess (cross-modal structure) |
| Private features | Marginal structure (modality-exclusive) |
| Orthogonality constraint | Independence of joint and marginal components |
| Temporal structural constraint | Parameterized ordering (time as filtration) |
| Factorized latent space | Decomposed representation (joint + marginal) |
| Modal-matching objective | Cross-modal joint alignment |

---

## SP-17 — Liu, Lin, Padhy, Tran, Bedrax-Weiss, Lakshminarayanan (2020)
**"Simple and Principled Uncertainty Estimation with Deterministic Deep Learning via Distance Awareness"**
**Domain(s)**: Machine learning, information theory
**Abstract machines instantiated**:
- **Stability**: The core concept is "distance awareness" — the model's ability to quantify how far a test example is from the training manifold. SNGP achieves this via spectral normalization (controlling the Lipschitz constant of each layer) combined with a GP output layer. The spectral normalization is a direct stability mechanism: it ensures that small input perturbations produce bounded changes in hidden representations, layer by layer. The Lipschitz bound is the stability certificate.
- **Null hypothesis**: Out-of-domain detection is null hypothesis testing: the training distribution is the null, and the model must identify test examples that are far from this null. The GP output layer provides a principled uncertainty measure (posterior variance) that increases with distance from training data. High uncertainty = likely null (out-of-domain).
- **Parameterized homology (weak)**: The spectral normalization parameter controls the bi-Lipschitz property of each layer. As this parameter varies, the model interpolates between unconstrained (no distance awareness) and fully constrained (isometric, distance-preserving). The optimal value balances expressiveness and distance awareness.

**What is genuinely new**: Formalization of uncertainty quantification as a minimax learning problem, with distance awareness as the necessary condition. The identification of spectral normalization + GP output as sufficient for competitive uncertainty with deep ensembles, at the cost of a single model. The distance awareness concept connects uncertainty to metric geometry.

**Connections the authors acknowledge**: Gaussian processes, Bayesian neural networks, deep ensembles (Lakshminarayanan et al., 2017). No connections to TDA (despite the manifold distance concept being related to persistent homology), QEC, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Distance awareness | Stability certificate (Lipschitz bound) |
| Spectral normalization | Layer-wise Lipschitz control |
| GP output layer | Posterior uncertainty (distance from null) |
| Out-of-domain detection | Null hypothesis testing (far from training manifold) |
| Training manifold | Support of the null distribution |
| Uncertainty | Distance from null (measured in feature space) |
| Deep ensemble | Stability through redundancy |

---

# Summary

## Search statistics
- **Total distinct search queries executed**: 62 (across 15 strategies + extra targeted searches)
- **Search strategies used**: Author-based, sheaves, spectral methods, topological ML, network neuroscience, renormalization, error-correcting codes, Morse theory, category theory, thermodynamics, algebraic topology, causal emergence, neural dynamics, point processes, compressed sensing, plus supplementary: cohomology, permutation entropy, ergodic theory, Lyapunov, bifurcation, surrogate testing, quantum codes, and more
- **Total papers with content retrieved and evaluated**: 28
- **New papers annotated**: 17

## Coverage by machine

| Machine | Papers instantiating it |
|---|---|
| **Chain complex** | SP-04 (HSIC layers), SP-06 (graph Laplacian), SP-10 (factor graph), SP-11 (Lie algebra), SP-12 (Chern number), SP-14 (Hermitian matrix), SP-15 (brain graph) |
| **Parameterized homology** | SP-01 (information plane), SP-02 (beta trade-off), SP-05 (intensity evolution), SP-08 (criticality m), SP-09 (activity duration), SP-12 (post-quench vortices), SP-13 (lag parameter), SP-15 (threshold filtration), SP-17 (spectral norm parameter) |
| **Matching** | SP-06 (geometric embedding), SP-07 (latent space positions), SP-10 (decimation), SP-14 (lead-lag clusters) |
| **Stability** | SP-01 (IB curve), SP-02 (generalization bound), SP-03 (adversarial robustness), SP-04 (HSIC sensitivity bound), SP-05 (exponential decay), SP-07 (stationarity), SP-08 (Wasserstein bound), SP-11 (cross-architecture transfer), SP-12 (topological protection), SP-14 (spectral smoothness), SP-16 (orthogonality), SP-17 (distance awareness) |
| **Joint-vs-marginal excess** | SP-01 (IB objective), SP-02 (excess risk), SP-03 (CS decomposition), SP-04 (HSIC dependence), SP-05 (cross-excitation/inhibition), SP-07 (mutual excitation), SP-13 (up-down balance), SP-14 (lead-lag), SP-15 (functional connectivity), SP-16 (shared vs private features) |
| **Null hypothesis** | SP-01 (SGD noise), SP-03 (baseline IB methods), SP-08 (Brownian limit), SP-09 (Poisson process), SP-10 (random assignment), SP-12 (trivial phase), SP-13 (Brownian motion), SP-14 (no temporal order), SP-15 (random/lattice networks), SP-16 (temporal ordering), SP-17 (training distribution) |

## Coverage by domain

| Domain | Papers |
|---|---|
| **TDA** | SP-11 (fiber bundle), SP-12 (Chern number) — both cross-domain |
| **QEC** | SP-12 (topological quantum matter) |
| **Dynamical systems** | SP-05, SP-06, SP-07, SP-08, SP-09, SP-13, SP-14 |
| **Neuroscience** | SP-15 (brain networks) |
| **Information theory** | SP-01, SP-02, SP-03, SP-04, SP-10, SP-11, SP-16, SP-17 |

## Surprising cross-domain connections

1. **Hawkes processes as parameterized homology**: The criticality parameter m in Hawkes processes (SP-08) plays the same structural role as the filtration parameter in persistent homology. The phase transition at m=1 is analogous to the birth/death of topological features at critical filtration values. This was not visible in the first pass, which did not cover Hawkes processes.

2. **Information bottleneck as stability + joint-vs-marginal**: The IB framework (SP-01, SP-02, SP-03, SP-04) instantiates BOTH stability and joint-vs-marginal excess simultaneously. The Lagrange multiplier beta parameterizes a family of representations that trade off between these two machines. This makes IB a natural two-machine composite.

3. **Chern number from dynamics** (SP-12): A static topological invariant (equilibrium Chern number) measured from dynamical data (post-quench vortex trajectories). This is the clearest bridge between static topology (TDA-like) and dynamical systems in the database. The linking number connecting knot theory to band topology echoes the Khovanov cohomology paper (already annotated) but from the physics side.

4. **Factor graphs as proto-chain complexes** (SP-10): The PDP paper's factor graph message passing is structurally parallel to boundary operations on a chain complex. Variable-to-factor messages are "forward" maps, factor-to-variable messages are "adjoint" maps. This connects constraint satisfaction (combinatorics) to homological algebra.

5. **Brain networks as filtrations awaiting TDA** (SP-15): The Simpson survey identifies correlation thresholding as a key methodological gap. This is precisely the setting where persistent homology provides a principled solution — the first pass did not find this connection because the brain network literature does not cite TDA.

6. **Fiber bundles in LLMs** (SP-11): If the Napolitano claims hold, the gl(4,R) decomposition of LLM hidden states is a Lie-algebraic chain complex with a joint-vs-marginal decomposition (active vs dark dimensions). Layer normalization acts as a projection that destroys the "excess" (dark) structure — a null-hypothesis-like operation built into the architecture.

7. **Ephemerally self-exciting processes** (SP-09): The constructive limit theorem (ephemeral -> Hawkes via batch scaling) provides a parameterized path through process space, connecting simple (Poisson null) to complex (Hawkes) via a single parameter (activity duration). This is a dynamical-systems instance of the parameterized homology machine.
