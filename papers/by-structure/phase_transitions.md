# Phase Transitions (Stability + Null Hypothesis)

Papers instantiating the **stability** and/or **null hypothesis** abstract machines. These two machines often co-occur: stability theorems characterize robustness near a phase boundary, while null models provide the reference distribution against which structure is tested.

---

## Stability

The shared pattern: small perturbation in input → bounded change in output. PH stability (bottleneck ≤ Hausdorff), QEC threshold theorem (exponential error suppression), structural stability in dynamical systems. The form of the guarantee varies: Lipschitz (TDA), exponential (QEC), generic (dynamics).

## Null Hypothesis

The shared pattern: destroy specific structure while preserving other properties, then measure the residual. Surrogates (TDA), depolarizing channel (QEC), shuffled time series (dynamics/neuroscience), product distribution (information theory).

---

## Information Theory

### Belghazi et al. (2018) — MINE
Null: product of marginals P_X ⊗ P_Z. Stability: strong consistency + Lipschitz bound on estimator. Full annotation: `by-domain/information_theory.md`.

### Mézard & Mora (2008) — Constraint Satisfaction
Stability: BP convergence regimes (easy/hard/UNSAT). Null: random k-SAT ensemble as typical-case benchmark. Full annotation: `by-domain/information_theory.md`.

### Chwilka & Karbowski (2024) — Lognormal MI
Anti-stability: MI divergence at finite variance — a discontinuity in the invariant. Full annotation: `by-domain/information_theory.md`.

### Kirkley (2025) — Transfer Entropy for Finite Data
Null: MDL principle provides analytic null — model complexity cost log Ω/N penalizes spurious structure without simulation. Stability: H_C → H_S asymptotically (Stirling), quantifying finite-sample instability of standard TE. Full annotation: `by-domain/information_theory.md`.

### Zhang, Simeone et al. (2020) — ITENE
Null: ITE removes synergistic contributions via infimum over distributions preserving marginals — a structured null tighter than standard TE conditioning. Full annotation: `by-domain/information_theory.md`.

### Marinazzo, Pellicoro, Stramaglia (2008) — Kernel Granger Causality
Null: Bonferroni-corrected eigenvector selection controls false causalities at rate q. Stability: bivariate GC more stable than L1-minimization for limited data (bias-variance tradeoff). Full annotation: `by-domain/information_theory.md`.

### Khanna & Tan (2020) — Economy SRU
Null: group-wise L1 regularization drives input weights to zero (= no causal link). Zero-weight sparsity pattern IS the null hypothesis decision boundary. Full annotation: `by-domain/information_theory.md`.

### Marcinkevics & Vogt (2021) — GVAR
Null: sparsity penalty + time-reversal check. Stability: relationships must survive time-reversal perturbation to be declared causal. Full annotation: `by-domain/information_theory.md`.

### Zhou, Xiao et al. (2014) — GC in I&F Networks
Null: spike raster (severe information reduction) still permits connectivity reconstruction. Stability: GC-to-connectivity mapping insensitive to dynamical regime (tonic/bursting/irregular). Full annotation: `by-domain/information_theory.md`.

### Wibral, Finn et al. (2017) — PID in Developing Neural Networks
Null: BROJA synergy defined via optimization over Δ_P (distributions preserving marginals). Synergy = excess of true joint over null maximum. Parameterized: developmental trajectory (DIV) shows synergy-to-redundancy phase transition. Full annotation: `by-domain/information_theory.md`.

### Venkatesh, Dutta et al. (2021) — M-information Flow
Null: edge pruning tests causal null ("does removing this edge change output?"). Random pruning = unstructured null; flow-guided pruning = structured null targeting specific information pathways. Full annotation: `by-domain/information_theory.md`.

---

## TDA

### Mollers, Immer, Fortuin, Isufi (2023) — Hodge-Aware Contrastive Learning
Stability: Augmentations are designed to preserve spectral (Hodge) properties. Hodge-aware negative reweighting creates embeddings robust to spectral-preserving perturbations. Engineered stability — the embedding is constructed to be insensitive to augmentations within the same Hodge subspace. Full annotation: `by-domain/tda.md`.

### Di Rocco, Eklund, Weinstein (2019) — Bottleneck Degree
Stability: The reach tau_X = min(rho, b) controls PH stability — it determines sample density needed for correct homology recovery. Bottleneck degree bounds the computational complexity of reach estimation. Connects algebraic geometry (Chern classes) to topological inference stability. Full annotation: `by-domain/tda.md`.

### de Jesus Jr., Fernandez-Navarro, Carbonero-Ruz (2025) — TDA for Financial Forecasting
Stability: Relies implicitly on PH stability (Cohen-Steiner et al., 2007) — small time series perturbations produce bounded changes in persistence diagrams and hence in TDA features (entropy, amplitude, point count).
Null hypothesis: Baselines without TDA features (univariate N-BEATS, temporal decomposition, time-delay embedding) serve as nulls that lack topological information. The gap measures TDA's contribution. Full annotation: `by-domain/tda.md`.

*(See also inbox for Cohen-Steiner PH stability theorem)*

## QEC

### Oreshkov (2013) — Continuous-time quantum error correction
Stability: Two regimes. Markovian: error rate ~ lambda^2/kappa (quadratic suppression). Non-Markovian: quantum Zeno effect gives lambda^4/kappa^2 (quadratic improvement over Markovian). Information loss bounded and continuous in perturbation parameters.
Null hypothesis: Uncorrected evolution (kappa = 0) = pure Lindblad decoherence. The gap between corrected and uncorrected evolution quantifies the value of error correction. Full annotation: `by-domain/qec.md`.

*(See also inbox for de la Fuente threshold, Dennis threshold theorem)*

## Dynamical Systems

### Dogra & Redman (2020) — Koopman Training of Neural Networks
Stability: Koopman predictions accurate over a non-trivial training window before diverging. Complexity analysis shows when partitioned Koopman training provides speedup (small partitions). Stability degrades as loss landscape becomes increasingly nonlinear. Full annotation: `by-domain/dynamical_systems.md`.

### Colbrook, Drmac, Horning (2025) — Introductory Guide to Koopman Learning
Stability: Central theme. Residuals ||K*psi - A*psi|| quantify approximation error. Pseudospectra sigma_epsilon(K) provide perturbation bounds — eigenvalues in the epsilon-pseudospectrum persist under size-epsilon perturbations. This is the spectral analogue of persistence diagram stability. Rigorous convergence proofs for generalized Laplace analysis even with continuous spectra. Full annotation: `by-domain/dynamical_systems.md`.

### Zhou, Chu, Xu, Liu, Yu (2020) — Detecting Predictable Segments in Chaotic Time Series
Stability: Takens embedding theorem guarantees topology preservation for generic parameters. SOM clustering adds second stability layer — similar phase track segments cluster together.
Null hypothesis: Chaotic segments (L > 1) serve as the null — regions where sensitivity to initial conditions has destroyed predictable structure. Predictable segments (0 < L < 1) are the signal. Lyapunov exponent is the diagnostic. Full annotation: `by-domain/dynamical_systems.md`.

## Reinforcement Learning

### Dabney, Rowland, Bellemare, Munos (2018) — QR-DQN
Stability: Distributional Bellman operator is a contraction in W_infinity (supremum Wasserstein). Extended to approximate setting with fixed quantile probabilities. Convergence to fixed point guaranteed. Full annotation: `by-domain/dynamical_systems.md`.

---

## Cross-domain observation

Stability takes three flavors across domains:

1. **Metric stability (TDA, optimal transport)**: Perturbation in input metric space → bounded change in output (persistence diagram, transport cost). The bound is a Lipschitz-type inequality.

2. **Spectral stability (dynamical systems)**: Perturbation in operator → bounded change in spectrum. Pseudospectra quantify this. Closely analogous to PH stability when eigenvalues are viewed as "features."

3. **Information-theoretic stability (QEC, information theory)**: Perturbation in noise rate → bounded change in protected information. The Zeno regime (Oreshkov) provides super-linear stability gains from temporal correlations — a feature absent in the metric and spectral cases.

---

## From Second Pass + Bridges

### Stability
- **Kawaguchi et al. (2023)** — Generalization bound Δ ≤ sqrt(I(X;Z)/n). Same form as PH stability. `cross_domain_bridges.md`.
- **Wang et al. (2021)** — HSIC bottleneck: layer-wise Lipschitz bounds as stability certificates. `second_pass.md` SP-04.
- **Liu et al. (2020) SNGP** — Spectral normalization = Lipschitz constraint identical to PH stability form. `cross_domain_bridges.md`.
- **Gallicchio & Micheli (2020)** — Banach contraction (ρ(W) < 1) guarantees fixed-point convergence. `cross_domain_bridges.md`.
- **Pati & Sanders (2005)** — No partial erasure: absolute impossibility, not a bound. Strongest stability. `cross_domain_bridges.md`.
- **Garbaczewski (2005)** — H-theorem: D_KL monotonically non-increasing as Lyapunov function. `cross_domain_bridges.md`.
- **Tarnowski et al. (2019)** — Chern number: integer-valued, topologically protected, survives noisy dynamics. `second_pass.md` SP-12.

### Null Hypothesis
- **Horst & Xu (2024)** — Subcritical Hawkes → Brownian motion (same limit as Poisson null). `second_pass.md` SP-08.
- **Daw & Pender (2021)** — Poisson process (activity duration = 0) as null. `second_pass.md` SP-09.
- **Bandt (2020)** — Brownian motion as null for financial order patterns. `second_pass.md` SP-13.
- **Simpson et al. (2013)** — Erdős-Rényi, configuration model, lattice as brain network nulls. `second_pass.md` SP-15.
- **Fasoli et al. (2026)** — Undirected connectivity as structural null (removes directionality). `cross_domain_bridges.md`.
