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

## Cross-domain: Sugiyama, Nakahara, Tsuda (2016)
**"Information Decomposition on Structured Space"**
arXiv: 1601.05533

**Domain(s)**: Information theory, information geometry, neuroscience (application)

**Abstract machines instantiated**:
- **Chain complex**: The partially ordered set (poset) of event combinations forms a graded structure. The Mobius function on the poset plays the role of an inclusion-exclusion operator — it is the combinatorial analogue of a boundary operator. The theta-coordinate system decomposes log p(x) = sum_{s <= x} theta(s), where the sum runs over the lower set of x in the poset. The eta-coordinate system gives eta(s) = Pr(X >= s). These dual coordinates are analogous to chain and cochain representations.
- **Joint-vs-marginal excess**: The orthogonal decomposition of KL divergence on the poset isolates the contribution of each event combination. Higher-order interactions (3-way, 4-way, ...) are the joint-vs-marginal excess: information present in the joint set of k events but absent from any (k-1)-subset. The paper provides efficient algorithms for computing these decompositions, even on incomplete hierarchies where some event combinations never occur.
- **Null hypothesis**: The product distribution (independence model) is the null: theta(s) = 0 for all non-singleton s corresponds to statistical independence. The deviation of theta(s) from zero for higher-order s measures the statistical interaction — the structure destroyed by the independence assumption.

**What is genuinely new (not reducible to shared abstraction)**:
- Extension of Amari's hierarchical decomposition from complete to incomplete posets. Many real-world scenarios have forbidden event combinations (e.g., "male" AND "ovarian cancer"), and the paper handles these gracefully by defining dual coordinates on arbitrary finite posets.
- The Pythagoras theorem for KL divergence on posets: D_KL(p||q) decomposes into orthogonal components corresponding to different levels of the hierarchy. This is a Hodge-like decomposition on a discrete structure — the information-theoretic analogue of the Hodge decomposition on simplicial complexes (cf. Mollers et al., 2023).
- Efficient algorithms (O(|S|^2) rather than exponential) for computing the decomposition, making it practical for neuroscience applications with many neurons.
- Application to isolating higher-order statistical interactions in neural spike train data.

**Connections the authors acknowledge**: Cite Amari (2001) on information geometry and hierarchical decomposition. Cite neuroscience applications (Schneidman et al., 2006; Ganmor et al., 2011 on neural interactions). Cite order theory (Birkhoff, Davey & Priestley). No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Poset of event combinations | Graded structure (analogous to simplicial complex) |
| theta-coordinate theta(s) | Interaction parameter (log-linear coefficient) |
| eta-coordinate eta(s) = Pr(X >= s) | Cumulative measure (dual coordinate) |
| Mobius function mu | Inclusion-exclusion (combinatorial boundary operator) |
| Orthogonal decomposition of D_KL | Hodge-like decomposition on discrete structure |
| Higher-order interaction | Joint-vs-marginal excess at order k |
| Independence model (theta = 0) | Null hypothesis (no interactions) |
| Incomplete hierarchy | Poset with forbidden combinations (holes in the complex) |
| Pythagoras theorem for D_KL | Orthogonality of components (analogous to Hodge orthogonality) |
| Principal ideal, principal filter | Lower/upper sets in the poset (local neighborhoods) |

**See also**: `by-structure/boundary_operators.md`, `by-structure/composite_systems.md`, `by-domain/information_theory.md`
