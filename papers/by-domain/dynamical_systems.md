# Dynamical Systems

Papers from the dynamical systems community, indexed by which abstract machines they instantiate. Cross-references to `by-structure/` files are given per paper.

---

## Dogra & Redman (2020)
**"Optimizing Neural Networks via Koopman Operator Theory"**
arXiv: 2006.02361 | NeurIPS 2020

**Domain(s)**: Dynamical systems, machine learning (optimization)

**Abstract machines instantiated**:
- **Parameterized homology**: Neural network training is cast as a discrete dynamical system: weights/biases evolve along a trajectory in weight space under the optimization algorithm. The Koopman operator K acts on observables g of the weight space, K[g](w) = g(F(w)), lifting the nonlinear weight dynamics to a linear operator on function space. As training progresses (the parameter is training step t), the Koopman eigenvalues/modes describe how the system's structure evolves — dominant eigenvalues correspond to persistent dynamical modes, decaying eigenvalues correspond to transient features. This is parameterized spectral analysis, tracking invariants (eigenvalues) as the system evolves.
- **Stability**: The paper proves that Koopman training (predicting future weights via the Koopman operator) is accurate over a "non-trivial range of training time" — the predictions remain valid for many steps before diverging. The complexity analysis shows when Koopman training provides speedup: the partition-based approach has cost O(sum d_i^2 * d_i) vs. backpropagation's O(sum d_i * d_{i+1}), making it faster when partitions are small. Stability of the Koopman approximation degrades as the training dynamics become increasingly nonlinear (loss landscape changes character).
- **Chain complex (weak)**: The Koopman operator framework decomposes the observable space into eigenspaces. The spectrum of K partitions observables into invariant subspaces — while not a chain complex in the strict boundary-operator sense, the spectral decomposition is the linear-algebraic analogue of homological decomposition, with eigenspaces playing the role of graded components.

**What is genuinely new (not reducible to shared abstraction)**:
- Koopman training as an alternative to backpropagation: using linear operator theory to bypass the nonconvexity of gradient-based optimization. The key insight is that linearity of the Koopman operator makes prediction a matrix computation, which is >10x faster than Adam/Adadelta/Adagrad in the demonstrated cases.
- Partitioned Koopman operator: instead of approximating a single high-dimensional operator, the weight space is partitioned into subspaces and separate Koopman operators are learned for each. This makes the approach tractable for deep networks.
- The functor perspective: Koopman operators are functors (mapping dynamical systems to linear operators), and the paper notes this connects to Fong et al.'s observation that backpropagation is a functor. Two independent roads to the same categorical structure.
- Demonstrated on practical networks: MNIST classifier and neural ODE solver, showing the approach generalizes across architectures and objectives.

**Connections the authors acknowledge**: Cite Koopman operator theory (Koopman 1931, Mezic, Brunton, Budisic), connection between renormalization group and Koopman operators (Dogra & Redman, 2020), and work on NNs as dynamical systems (Saxe et al., E et al.). Fong et al. (2019) on backpropagation as a functor. No connections to TDA, QEC, or neuroscience (beyond the dynamical systems lens on neural networks).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Koopman operator K | Linear representation of nonlinear dynamics (lifting) |
| Observable g | Function on the state space (analogous to cochain) |
| Koopman eigenvalue lambda_k | Persistent dynamical invariant |
| Koopman mode | Eigenfunction (spectral component) |
| Training step t | The parameter (analogous to filtration scale) |
| Weight trajectory w(t) | Path in the state space |
| Partitioned Koopman approximation | Local decomposition of the operator |
| Extended DMD (EDMD) | Data-driven operator approximation |
| Prediction window | Stability interval (range of valid approximation) |
| Loss landscape | The nonlinear structure being linearized |

**See also**: `by-structure/filtrations.md`

---

## Colbrook, Drmac, Horning (2025)
**"An Introductory Guide to Koopman Learning"**
arXiv: 2510.22002

**Domain(s)**: Dynamical systems, numerical analysis

**Abstract machines instantiated**:
- **Parameterized homology**: The paper provides a comprehensive treatment of how Koopman spectral analysis tracks dynamical invariants as the system evolves. Spectral measures mu_g of the Koopman operator decompose the dynamics into components: point spectrum (periodic/quasi-periodic modes), absolutely continuous spectrum (mixing/chaotic dynamics), and singular continuous spectrum (fractal-like dynamics). The spectral type is itself an invariant that classifies the dynamical system — and computing it from data requires tracking how approximations converge as the dictionary size (the parameter) increases.
- **Stability**: A central theme is rigorous convergence of data-driven methods. The paper unifies error control via residuals: for EDMD matrix approximation, the residual ||K*psi_j - sum_i A_ij psi_i||^2 quantifies how far the finite-dimensional approximation is from the true operator. Pseudospectra sigma_epsilon(K) = {z : ||(K - zI)^{-1}|| > 1/epsilon} provide stability bounds — points in the epsilon-pseudospectrum are eigenvalues that persist under perturbations of size epsilon. This is the spectral analogue of persistence stability.
- **Matching (spectral)**: The delay embedding approach connects to matching: given a single observable, the Krylov subspace {g, Kg, K^2 g, ...} generates a subspace from which the operator can be approximated. The generalized Laplace analysis matches observables to their spectral components via time-averaging: P_lambda[g] = lim_{N->inf} (1/N) sum_{n=0}^{N-1} e^{-i*lambda*n} K^n g. This is an optimal assignment of spectral weight to frequencies.

**What is genuinely new (not reducible to shared abstraction)**:
- Unified error control via residuals across finite and infinite-dimensional settings. The paper provides a single framework for assessing EDMD, DMD, and delay-embedded approximations — showing that residuals are the fundamental diagnostic regardless of method.
- Elementary proof that generalized Laplace analysis converges for spectral operators with continuous spectra and no spectral gaps. Previous convergence results required point spectrum; this extends to the mixing/chaotic case.
- Comprehensive comparison of three families of spectral measure computation methods: moment-based (Christoffel-Darboux kernels), eigenvalue-based (smoothed EDMD spectra), and resolvent-based (Stone's formula). This taxonomy of approaches is itself a contribution.
- The classification theory section: distinguishing pure point, absolutely continuous, and singular continuous spectra from finite data is posed as a computational challenge with rigorous algorithmic solutions.

**Connections the authors acknowledge**: Extensive survey of Koopman operator literature (Mezic, Schmid, Brunton, Budisic, Kutz). Applications in fluid dynamics, control theory. Cite Takens embedding theorem as the theoretical foundation for delay-based methods. No connections to TDA, QEC, or information theory — the paper stays within dynamical systems and numerical analysis.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Koopman operator K | Linear lifting of nonlinear dynamics |
| Spectral measure mu_g | Distribution of dynamical invariants (parameterized) |
| Point spectrum | Persistent features (discrete eigenvalues = periodic modes) |
| Continuous spectrum | Mixing/chaotic structure (no isolated eigenvalues) |
| EDMD matrix A | Finite-dimensional boundary operator approximation |
| Residual ||K*psi - A*psi|| | Error in the approximation (stability diagnostic) |
| Pseudospectrum sigma_epsilon | epsilon-perturbation set (stability under noise) |
| Generalized Laplace analysis | Spectral projection (matching observable to frequency) |
| Krylov subspace | Delay embedding (Takens reconstruction in function space) |
| DMD / Dynamic Mode Decomposition | Data-driven spectral decomposition |
| Dictionary {psi_j} | Basis for the function space (analogous to simplicial basis) |
| Coherency | Forecast reliability measure |

**See also**: `by-structure/filtrations.md`

---

## Zhou, Chu, Xu, Liu, Yu (2020)
**"Detecting Predictable Segments of Chaotic Financial Time Series via Neural Network"**
DOI: 10.3390/electronics9050823 | Electronics 9(5):823

**Domain(s)**: Dynamical systems, finance (applied), machine learning

**Abstract machines instantiated**:
- **Parameterized homology**: Phase space reconstruction (PSR) via Takens embedding is the core methodology. The time series x(t) is embedded into m-dimensional phase space as vectors X(t) = [x(t), x(t+tau), ..., x(t+(m-1)*tau)]. The embedding dimension m and time delay tau are the parameters. As these parameters vary, the topological structure of the reconstructed attractor changes. The paper uses mutual information to determine optimal tau and the Grassberger-Procaccia algorithm to determine m — both are parameter selection procedures that seek the simplest faithful topological representation.
- **Null hypothesis**: The SOM (Self-Organizing Map) clustering of phase track segments separates linear (predictable) components from nonlinear (chaotic) components. The chaotic segments serve as the null: regions where structure has been destroyed by sensitivity to initial conditions (positive Lyapunov exponent). The predictable segments are the signal — structure that persists despite the surrounding chaos. The Lyapunov exponent L itself is the diagnostic: 0 < L < 1 means short-term predictability; L > 1 means unpredictable.
- **Stability**: Takens embedding theorem guarantees that for generic m and tau, the reconstructed phase space is diffeomorphic to the true attractor — the topology is preserved under embedding. This is a stability result: the topological invariants of the attractor are robust to the choice of embedding parameters (as long as they are generic). The SOM clustering adds a second stability layer: similar phase track segments cluster together, and the prediction accuracy measures whether the learned patterns are stable enough to forecast.

**What is genuinely new (not reducible to shared abstraction)**:
- The key insight is detecting WHICH segments of a chaotic time series are predictable, rather than estimating overall predictability. Previous work computed global Lyapunov exponents; this paper provides local, time-varying predictability assessment via unsupervised clustering.
- Using SOM neural networks to cluster phase track segments by similarity. Phase tracks that recur in similar patterns (periodic or quasi-periodic segments within an otherwise chaotic series) are identified and grouped. LSTM is then applied only to the predictable clusters.
- The interpretation of intermittent chaos in financial markets: alternating between predictable (linear superposition) and unpredictable (chaotic) regimes. This provides a dynamical systems explanation for phenomena like sudden market crashes ("black swans") — they correspond to transitions from predictable to chaotic dynamics.
- Tested on multiple financial indices (Dow Jones, Nikkei, Chinese markets, gold) demonstrating generality.

**Connections the authors acknowledge**: Cite phase space reconstruction (Takens, 1981), Lyapunov exponents, Hurst index (MF-DFA). Cite LSTM and SOM neural networks. Acknowledge the tension between nonlinear model success and the "initial sensitivity law" of chaos — prediction accuracy should be impossible beyond the Lyapunov horizon. No connections to TDA (despite using topological reconstruction), QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Phase space reconstruction | Takens embedding (topology-preserving map) |
| Embedding dimension m | Parameter (controls the chain complex dimension) |
| Time delay tau | Parameter (controls the sampling resolution) |
| Strange attractor | Invariant topological object (the manifold) |
| Lyapunov exponent L | Stability diagnostic (sensitivity to perturbation) |
| Predictable segment | Region with preserved structure (low L) |
| Chaotic segment | Region with destroyed structure (high L, null model) |
| SOM clustering | Unsupervised matching of phase track segments |
| Phase track similarity | Distance metric on embedded trajectories |
| Intermittent chaos | Alternating parameterized regimes (phase transitions) |
| Hurst index h | Long-range dependence measure (stability of correlations) |

**See also**: `by-structure/filtrations.md`, `by-domain/tda.md` (cross-listed — uses topological reconstruction)

---

## Theiler, Eubank, Longtin, Galdrikian, Farmer (1992)
**"Testing for nonlinearity in time series: the method of surrogate data"**
DOI: 10.1016/0167-2789(92)90102-S | Physica D, 58:77--94

**Domain(s)**: Dynamical systems

**Abstract machines instantiated**:
- **Null hypothesis**: THE foundational surrogate data paper. Three algorithms define three null hypotheses: (0) random shuffle (destroys all temporal correlations, preserves amplitude distribution), (1) phase randomization (preserves power spectrum, destroys phase relationships -- null: linear Gaussian process), (2) AAFT (preserves power spectrum + amplitude distribution -- null: static nonlinear transformation of linear Gaussian process). Each surrogate type is a precise choice of what to destroy and what to preserve. Test statistic (correlation dimension, Lyapunov exponent, prediction error) computed on original vs. surrogate ensemble; significance by rank ordering.
- **Stability**: Preserved quantities (power spectrum under Algorithm 1, amplitude distribution under Algorithm 2) are stability invariants -- they survive the surrogate transformation exactly by construction.
- **Joint-vs-marginal excess** (weak): Phase relationships between Fourier components are joint structure; phase randomization destroys this while preserving marginal spectral properties. Significant test result = genuine joint phase structure.
- **Parameterized homology** (weak): Surrogate ensemble parameterizes a distribution of the test statistic under the null. Original's rank in this distribution determines significance.

**What is genuinely new**: The method itself -- the first rigorous statistical framework for testing nonlinearity claims in experimental time series. The graded hierarchy of nulls (Algorithm 0 < 1 < 2) has no analogue in other domains. AAFT specifically addresses nonlinear observation functions. Overturned many prior claims of low-dimensional chaos.

Full annotation: `inbox.md` (DOI: 10.1016/0167-2789(92)90102-S).

**See also**: `by-structure/phase_transitions.md`

---

## Takens (1981)
**"Detecting strange attractors in turbulence"**
Lecture Notes in Mathematics, vol. 898, Springer

THE foundational delay embedding theorem. For generic (C^2-residual) pairs (diffeomorphism phi, observation function y) on a compact manifold M, the delay map F(x) = (y(x), y(phi(x)), ..., y(phi^{2d}(x))) is an embedding if d > dim(M). Reconstructed manifold has identical homology to original. Single scalar observable suffices to recover attractor topology. Full annotation: `inbox.md`.
**Machines**: chain complex (implicit), stability (topological genericity), parameterized homology (weak -- embedding dimension as parameter).
**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`

---

## Sauer, Yorke, Casdagli (1991)
**"Embedology"**
Journal of Statistical Physics 65(3-4):579-616

Extends Takens to PREVALENCE (measure-theoretic genericity). Works for fractal attractors with non-integer box-counting dimension d_B(A). Minimal embedding dimension 2*d_B(A)+1. Prevalence is strictly stronger than topological genericity. Full annotation: `inbox.md`.
**Machines**: stability (prevalence = measure-theoretic robustness), parameterized homology (weak -- embedding dimension, now fractal-valued).
**See also**: `by-structure/phase_transitions.md`

---

## Sugihara, May, Ye, Hsieh, Deyle, Fogarty, Munch (2012)
**"Detecting Causality in Complex Ecosystems"**
DOI: 10.1126/science.1227079 | Science 338:496–500

**Domain(s)**: Dynamical systems, information theory (causal inference)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: CCM tests whether Y's shadow manifold contains information about X beyond Y's marginal dynamics. Cross-prediction success = excess of joint over marginal. The dynamical systems analogue of transfer entropy, operating on reconstructed state spaces rather than probability distributions.
- **Stability**: Convergence criterion — cross-prediction improves and stabilizes as library size L increases. Takens embedding theorem guarantees diffeomorphic reconstruction for generic parameters.
- **Null hypothesis**: No causal coupling → no convergence (flat prediction skill). Surrogates destroy temporal coupling. Granger causality as alternative method null.
- **Parameterized homology** (weak): Library size L parameterizes the convergence curve rho(L). Embedding dimension m and time delay tau as additional parameters from Takens' framework.

**What is genuinely new**: Convergence as a causal test with directional asymmetry. Handles separability failure (strong causation + zero correlation). Distinguishes geometric (manifold) from statistical (conditional probability) causal inference. Mirage correlations demonstrated.

**Connections the authors acknowledge**: Takens (1981), Granger causality (as foil). No TDA/QEC/information theory connections.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Convergent cross-mapping | Directed joint-vs-marginal test (manifold-based) |
| Shadow manifold | Takens reconstruction (topology-preserving embedding) |
| Cross-prediction skill rho | Joint-vs-marginal excess |
| Library size L | Parameterization (filtration scale) |
| Convergence with L | Stability (feature persistence) |
| No convergence | Null hypothesis (no causal coupling) |
| Granger causality | Alternative null method (linear assumption) |
| Mirage correlation | Spurious structure destroyed by proper null |

**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

Full annotation: `inbox.md` (DOI: 10.1126/science.1227079)

---

## Cross-domain: Bunne, Alvarez-Melis, Krause, Jegelka (2019)
**"Learning Generative Models across Incomparable Spaces"**
arXiv: 1905.05461 | ICML 2019

**Domain(s)**: Optimal transport, machine learning, geometry

**Abstract machines instantiated**:
- **Matching**: The Gromov-Wasserstein (GW) distance is the central object. It solves an optimal transport problem between distributions on DIFFERENT metric spaces (X, d_X) and (Y, d_Y) by matching pairwise intra-space distances: GW(mu, nu) = inf_pi integral |d_X(x,x') - d_Y(y,y')|^2 d(pi(x,y)) d(pi(x',y')). This is a second-order optimal transport — matching structures rather than points. The paper uses GW as the loss function for a GAN, where the generator learns to produce samples whose relational structure matches the reference data.
- **Stability**: The GW distance satisfies a triangle inequality and provides a metric on the space of metric measure spaces (up to measure-preserving isometries). Small perturbations in the reference data produce bounded changes in the GW distance and hence in the learned generator. The paper also proves that their parametrized adversarial approximation converges to the true GW distance under mild conditions.
- **Joint-vs-marginal excess (structural)**: The GW distance captures relational structure that is invariant to ambient dimension, rotation, and reflection. By comparing pairwise distances rather than absolute positions, the method detects structure in the RELATIONSHIPS between points — which is a form of joint structure (pairwise interactions) absent from marginal (pointwise) descriptions.

**What is genuinely new (not reducible to shared abstraction)**:
- GW-GAN: a generative model that can learn across incomparable spaces — different dimensions, different data types (e.g., graph to Euclidean). No previous GAN could generate samples in a space of different dimensionality from the training data.
- Orthogonality regularization on the adversary to prevent degenerate solutions. This constraint (the adversary's weight matrices should be approximately orthogonal) is a practical contribution for stabilizing GW-based learning.
- Steerable generation: the relational structure is preserved, but other properties (style, dimension, appearance) can be freely modified via regularization. This separates topology from geometry in the learned representation.
- Applications to manifold learning (dimensionality reduction that preserves topology), relational learning (graph to point cloud), and cross-domain transfer.

**Connections the authors acknowledge**: Cite Memoli (2011) on GW distance, Peyre et al. on computational OT, and the Wasserstein GAN literature (Arjovsky et al., Salimans et al., Genevay et al.). Acknowledge connections between GW distance and spectral methods (Laplacian eigenmaps). No citations to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Gromov-Wasserstein distance | Second-order optimal matching (structure-preserving) |
| Transport plan pi | Matching between features |
| Intra-space distances d_X, d_Y | Local structure (the metric to be preserved) |
| Incomparable spaces | Different ground spaces (no shared metric) |
| Generator g_theta | Map that realizes the matching |
| Orthogonality regularization | Constraint ensuring the matching is non-degenerate |
| Relational structure | Joint structure (pairwise, not pointwise) |
| Metric measure space (X, d, mu) | The topological/geometric object |
| Convergence of parametric approximation | Stability of the matching under approximation |

**See also**: `by-structure/optimal_transport.md`

---

## Cross-domain: Dabney, Rowland, Bellemare, Munos (2018)
**"Distributional Reinforcement Learning with Quantile Regression"**
AAAI 2018

**Domain(s)**: Machine learning (reinforcement learning), optimal transport

**Abstract machines instantiated**:
- **Matching**: The paper minimizes the Wasserstein distance between the predicted return distribution and the target distribution via quantile regression. The Wasserstein-1 distance W_1(F, G) = integral |F^{-1}(tau) - G^{-1}(tau)| d(tau) is an optimal transport metric — it finds the minimum-cost matching between two distributions. QR-DQN approximates the return distribution as a mixture of N Dirac deltas at adjustable quantile locations, and quantile regression adjusts these locations to minimize W_1 to the Bellman-updated target.
- **Stability**: The distributional Bellman operator is a contraction in the supremum Wasserstein metric (W_infinity). The paper extends this contraction result to the approximate setting with fixed quantile probabilities, proving that quantile regression converges to a fixed point. This is a stability guarantee: the iterative Bellman update produces bounded changes at each step and converges.
- **Parameterized homology (structural analogue)**: The return distribution Z(s,a) is tracked as the state-action pair (s,a) varies — a distribution-valued function parameterized by the policy's state space. The distributional Bellman equation Z(s,a) = R(s,a) + gamma * Z(s', a') is a recursive definition that propagates distributional information through the parameter space (state space of the MDP).

**What is genuinely new (not reducible to shared abstraction)**:
- Closing the theory-practice gap in distributional RL: C51 used heuristic projections incompatible with the Wasserstein metric; QR-DQN operates end-to-end under Wasserstein, making theory and algorithm consistent.
- The "transposed" parametrization: C51 uses fixed locations with adjustable probabilities; QR-DQN uses fixed probabilities (uniform 1/N) with adjustable locations. This inversion makes quantile regression applicable and the Wasserstein minimization tractable.
- Huber quantile regression for practical robustness: smoothing the quantile regression loss near zero to reduce sensitivity to outliers, yielding a 33% median improvement over C51 on Atari benchmarks.

**Connections the authors acknowledge**: Cite Bellemare, Dabney, Munos (2017) on distributional RL and the Wasserstein contraction. Cite optimal transport theory (Villani). Acknowledge the connection between quantile regression (Koenker, 2005) and Wasserstein distance minimization. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Wasserstein distance W_1 | Optimal transport cost (matching metric) |
| Quantile locations theta_i | Matched feature positions |
| Return distribution Z(s,a) | Parameterized distribution (invariant over state space) |
| Distributional Bellman operator | Parameterized map (analogous to persistence map) |
| Contraction in W_infinity | Stability guarantee |
| Quantile regression | Matching algorithm (minimizing transport cost) |
| Huber loss | Robustified matching cost |
| C51 projection | Heuristic matching (approximate) |

**See also**: `by-structure/optimal_transport.md`

---

## Cross-domain: Bayraktar & Zhou (2017)
**"On Model-Independent Pricing/Hedging Using Shortfall Risk and Quantiles"**
arXiv: 1307.2493

**Domain(s)**: Mathematical finance, optimal transport

**Abstract machines instantiated**:
- **Matching**: The model-independent pricing framework IS an optimal transport problem. Given marginal distributions mu_1, ..., mu_n for the stock price at times 1, ..., n (calibrated from call option prices), the set M of martingale measures with these marginals defines a transport polytope. Super-hedging prices are computed by optimizing over M — finding the worst-case matching between marginals that is consistent with no-arbitrage (martingale constraint).
- **Joint-vs-marginal excess**: The entire framework measures the gap between what marginal distributions alone determine and what the full joint dynamics allow. The duality result — that the minimum hedging cost equals sup_{Q in M} E_Q[Phi] + U^{-1}(alpha) — quantifies how much the joint distribution (the martingale coupling) can exceed any individual marginal's contribution to the option price.
- **Null hypothesis**: The martingale constraint serves as the structural null: any pricing model must be a martingale (no-arbitrage). The set M of all martingale measures with given marginals is the null class. Exotic option prices are bounded by optimizing over this null class.

**What is genuinely new (not reducible to shared abstraction)**:
- Extension of Follmer-Leukert shortfall hedging duality to the model-independent (optimal transport) setting. The classical result assumes a specific probability model; this paper removes that assumption.
- The proof that quantile hedging under marginal constraints reduces to super-hedging of knockout options — connecting two seemingly different risk management problems.
- The semi-static trading strategies (static vanilla portfolio + dynamic stock trading) as the dual objects to martingale transport plans.

**Connections the authors acknowledge**: Cite Beiglbock, Henry-Labordere, Penkner (2013) on martingale optimal transport. Cite Follmer-Leukert (1999, 2000) on shortfall and quantile hedging. Explicitly situated at the optimal transport / mathematical finance interface. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Marginal distributions mu_i | Marginal constraints (fixed components) |
| Martingale measure Q in M | Joint distribution (coupling) consistent with null (no-arbitrage) |
| Super-hedging price | Worst-case matching cost |
| Shortfall risk | Risk measure on the residual after matching |
| Transport polytope M | Feasible set of matchings |
| Semi-static strategy | Dual variable (hedging portfolio) |
| Knockout option | Truncated payoff (boundary condition on the matching) |
| Call option prices | Data determining the marginals |

**See also**: `by-structure/optimal_transport.md`, `by-structure/composite_systems.md`

---

## Cross-listed from Information Theory

- **Sugiyama, Nakahara & Tsuda (2016)** — "Information Decomposition on Structured Space." Dual theta/eta coordinates on posets as chain complex; KL divergence Pythagoras theorem as Hodge-like decomposition; higher-order interactions as joint-vs-marginal excess. Full annotation in `by-domain/information_theory.md`. Machines: chain complex, joint-vs-marginal, null hypothesis. Notable Rosetta connection: the orthogonal decomposition of D_KL on posets is the information-theoretic analogue of the Hodge decomposition on simplicial complexes (cf. Mollers et al., 2023).

---

## Cross-listed from Second Pass + Bridges

### Hawkes Process Cluster

- **Mei & Eisner (2017)** — "The Neural Hawkes Process." Continuous-time LSTM for event streams. Cross-excitation/inhibition as joint-vs-marginal. Exponential decay as stability mechanism. Full annotation: `second_pass.md` (SP-05). Machines: parameterized homology, joint-vs-marginal, stability.

- **Shang & Sun (2019)** — "Geometric Hawkes Processes with Graph Convolutional RNNs." Graph Laplacian (0th Hodge Laplacian) for inter-process correlations. Spectral convolutions respect chain complex structure. Full annotation: `second_pass.md` (SP-06). Machines: chain complex (weak), matching, stability.

- **Huang, Soliman, Paul, Xu (2022)** — "Latent Space Hawkes Process Model." Latent distance + mutual excitation decomposition = marginal + joint excess. Stationarity (spectral radius < 1) as stability. Full annotation: `second_pass.md` (SP-07). Machines: matching, joint-vs-marginal, stability.

- **Horst & Xu (2024)** — "Functional Limit Theorems for Hawkes Processes." Criticality parameter m as filtration. Phase transition at m=1. Wasserstein convergence rates. Brownian motion as null. Full annotation: `second_pass.md` (SP-08). Machines: parameterized homology, stability, null hypothesis.

- **Daw & Pender (2021)** — "An Ephemerally Self-Exciting Point Process." Activity duration parameterizes path from Poisson (null) to Hawkes (full structure). Batch scaling limit theorem. Full annotation: `second_pass.md` (SP-09). Machines: parameterized homology, null hypothesis, joint-vs-marginal.

### Cross-Domain

- **Tarnowski et al. (2019)** — "Measuring topology from dynamics: Chern number from linking number." Static topological invariant extracted from post-quench dynamics. Linking number = Chern number. Full annotation: `second_pass.md` (SP-12). Machines: chain complex, parameterized homology, null hypothesis, stability. **Also QEC.**

- **Bandt (2020)** — "Order patterns, their variation and change points." Permutation entropy with lag as filtration parameter. Brownian motion as null. Up-down balance as joint excess. Full annotation: `second_pass.md` (SP-13). Machines: null hypothesis, parameterized homology, joint-vs-marginal.

- **Bennett, Cucuringu, Reinert (2022)** — "Lead-lag detection and network clustering." Hermitian spectral clustering for directed networks. Lead-lag as directed matching. Full annotation: `second_pass.md` (SP-14). Machines: matching, chain complex (weak), null hypothesis, joint-vs-marginal.

- **Gallicchio & Micheli (2020)** — "Fast and Deep Graph Neural Networks." Reservoir GNNs: Banach contraction guarantees convergence. Untrained random weights suffice — architecture carries topology. Layer depth = scale parameter. Full annotation: `cross_domain_bridges.md`. Machines: stability, parameterized homology, null hypothesis, chain complex. **Bridge: dynamics + TDA.**

- **Chen et al. (2023)** — "ContiFormer: Continuous-Time Transformer." Neural ODE inside attention. Continuous-time matching. Subsumes existing methods as special cases. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, stability, matching.

---

## Wave 4 (2026-04-06) — Bridge Papers

### Perea & Harer (2013) — SW1PerS (cross-listed from TDA)
Sliding window embedding of time series → Rips complex → PH. SW1PerS score (max H₁ persistence) quantifies periodicity. Formal bridge: Takens embedding (dynamics) → persistent homology (TDA). Convergence theorems.
**Machines**: chain complex, parameterized homology, stability. Full annotation: `inbox.md` (arXiv: 1307.6188). **Bridge: dynamics + TDA.**

### Tsuda (2001) — Chaotic Itinerancy (cross-listed from Neuroscience)
**"Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems"**
DOI: 10.1017/S0140525X01000097
Chaotic itinerancy: trajectory wanders among attractor ruins (destroyed attractors that retain geometric influence). Each quasi-stable epoch has its own local topology; the itinerant trajectory traces a path through topology space parameterized by time. Milnor attractors formalize the intermediate stability status. Fixed-point/limit-cycle as non-itinerant null. Proposed as dynamical mechanism for cognitive flexibility (olfactory perception, episodic memory).
**Machines**: parameterized homology, stability (anti-stability: attractors destroyed but ruins exploited), null hypothesis, chain complex (weak). Full annotation: `inbox.md`.
**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`, `by-domain/neuroscience.md`.

---

## Third Pass (2026-04-05)

### Structure-Preserving Contrastive Learning for Spatial Time Series
**Domain(s)**: TDA, dynamical systems, machine learning
PH as regularizer for contrastive learning of time series. Dual-scale approach: global PH + local graph geometry. Wasserstein stability on persistence diagrams bounds topological distortion of learned mapping. Applied to traffic prediction.
**Machines**: parameterized homology, joint-vs-marginal, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-01).

### Thai Stock Market de Rham Cohomology
**Domain(s)**: TDA, dynamical systems (financial markets)
de Rham cohomology on correlation matrices. Wilson loops detect non-trivial manifold topology. Market transitions through 8 states; non-trivial cohomology appears during crash. Gauge theory tools (Chern-Simons currents, Pauli matrices) imported from mathematical physics. Pre/post-crisis states as null.
**Machines**: chain complex, parameterized homology, null hypothesis, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-02).
**See also**: `by-structure/boundary_operators.md`

### Cross-Correlation Integral (DOI: 10.1134/1.1259701)
**Domain(s)**: Dynamical systems, information theory
Cross-correlation integral C(ε) extends Grassberger-Procaccia to compare two time windows at multiple scales. Nonstationarity = gap between cross and auto integrals (joint-vs-marginal excess applied to attractor measures). Link to wavelet transforms of attractor density.
**Machines**: parameterized homology, joint-vs-marginal, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-03).

### Entropic Symmetry Breaking (arXiv: 2510.03572)
**Domain(s)**: Dynamical systems, information theory
Entropy/information-transfer framework for symmetry breaking. Symmetric state IS the null. Critical slowing down = loss of stability. Information transfer asymmetry after breaking = directed joint excess. Entropy diagnostics anticipate bifurcation before the critical point.
**Machines**: parameterized homology, null hypothesis, stability, joint-vs-marginal.
Full annotation: `third_pass_dynamics_tda.md` (TP-04).

### Ordinal Networks for Time Series
**Domain(s)**: Dynamical systems, information theory
Directed graphs from temporal succession of ordinal (permutation) patterns. Exact analytical null for random series. Local network entropy robust to noise. Hurst exponent estimation via matching to parameterized family. Applied to seismological data.
**Machines**: chain complex (weak), null hypothesis, parameterized homology, matching.
Full annotation: `third_pass_dynamics_tda.md` (TP-05).

### Visibility Graph Irreversibility (DOI: 10.3390/e27040402)
**Domain(s)**: Dynamical systems, information theory
Directed horizontal visibility graphs for time-series irreversibility detection. KL divergence between forward and reversed degree distributions as test statistic. Reversible (equilibrium) process as null. Applied to global financial markets 2004–2022.
**Machines**: null hypothesis, parameterized homology, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-06).

### Specific Differential Entropy Rate
**Domain(s)**: Information theory, dynamical systems
State-dependent entropy rate h(x) — local unpredictability varies across the attractor. Extends Shannon entropy rate from a scalar to a function. Uniform h(x) as null. Applied to heart rate variability. Variation h(x) - h_avg is joint-vs-marginal excess at state x.
**Machines**: parameterized homology, joint-vs-marginal, null hypothesis.
Full annotation: `third_pass_dynamics_tda.md` (TP-07).

### CP-PINNs: Changepoint Detection in PDEs
**Domain(s)**: Dynamical systems, machine learning
Physics-informed NNs with time-varying PDE parameters. Total Variation penalty enforces sparse changepoints. Constant-parameter PDE as null. Regret bounds provide algorithmic stability.
**Machines**: parameterized homology, null hypothesis, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-08).

### Ensemble Control on Lie Groups
**Domain(s)**: Dynamical systems (control theory)
Cartan decomposition of semisimple Lie algebras as Z/2-graded chain complex. Ensemble controllability = single control steers all systems simultaneously (population-level matching). Individual controllability lifts to ensemble controllability (stability). Extends from SO(3) to all semisimple Lie groups.
**Machines**: chain complex (algebraic), matching, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-12).
**See also**: `by-structure/boundary_operators.md`

### Pointwise Ergodic Theorem for Fuchsian Groups
**Domain(s)**: Dynamical systems (ergodic theory)
Cesaro averages of spherical averages converge a.e. to the space average. Bowen-Series coding maps group action to symbolic dynamics with Markovian transition structure. Space average as null expectation. Proved via reduction to free semigroup case.
**Machines**: chain complex (algebraic), stability, null hypothesis.
Full annotation: `third_pass_dynamics_tda.md` (TP-16).

### Barandes (2023) — Stochastic-Quantum Correspondence
Cross-listed from QEC. Derives QM from stochastic axioms. Also a dynamical systems result: functorial correspondence between Markov chains (stochastic dynamics) and unitary evolution (quantum dynamics).
Full annotation: `third_pass_neuro_qec.md` (TP-06).
