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
Null hypothesis: Baselines without TDA features (univariate N-BEATS, temporal decomposition, time-delay embedding) serve as nulls that lack topological information. The gap measures TDA's contribution. Full annotation: `annotations/10.1007-s00521-024-10787-x.md` (B2 pass 20).

### Vejdemo-Johansson & Mukherjee (2018) — Multiple testing with persistent homology
Null hypothesis: Universal empirical null distribution for PH features — analogous to chi-squared tables for classical stats. Two multiple testing procedures: FWER and FDR control for rejecting acyclicity. Grounded in limit theorems for PH of point processes. Full annotation: `annotations/1812.06491.md` (arXiv: 1812.06491).

### Adams et al. (2017) — Persistence Images
Stability: Lipschitz w.r.t. 1-Wasserstein distance. ||rho_B - rho_{B'}||_inf <= C * W_1(B, B') for persistence surfaces; extends to discretized PI vectors with L_inf, L_1, L_2 bounds. Tighter constants for Gaussian distributions (Theorems 3-4). The weighting function f (zero on diagonal, continuous, piecewise differentiable) is essential -- without it, points emerging from the diagonal create discontinuities. Impossibility: PI inner product kernel NOT stable for W_p with p > 1 (Remark 1). Builds directly on Cohen-Steiner et al. (2007) stability foundation. Full annotation: `annotations/1507.06217.md` (arXiv: 1507.06217), `by-domain/tda.md`.

*(See also inbox for Cohen-Steiner PH stability theorem)*

## QEC

### Oreshkov (2013) — Continuous-time quantum error correction
Stability: Two regimes. Markovian: error rate ~ lambda^2/kappa (quadratic suppression). Non-Markovian: quantum Zeno effect gives lambda^4/kappa^2 (quadratic improvement over Markovian). Information loss bounded and continuous in perturbation parameters.
Null hypothesis: Uncorrected evolution (kappa = 0) = pure Lindblad decoherence. The gap between corrected and uncorrected evolution quantifies the value of error correction. Full annotation: `by-domain/qec.md`.

### Dennis, Kitaev, Landahl, Preskill (2002) — Topological quantum memory
Stability: Threshold theorem — below p_c, logical error rate exponentially suppressed in code distance. Phase transition maps EXACTLY to 3D Z₂ lattice gauge theory with quenched disorder. Accuracy threshold = critical temperature. Null: uncorrected system as baseline. Full annotation: `annotations/quant-ph-0110143.md` (arXiv: quant-ph/0110143).

### Freedman, Kitaev, Larsen, Wang (2001) — Topological Quantum Computation
Stability: Error rate e^{-αℓ} — topological protection by geometric length scale, strongest continuous stability. Abelian anyons as null (trivial braiding = no computational power). Non-Abelian anyons required for universal quantum computation. Full annotation: `annotations/quant-ph-0101025.md` (arXiv: quant-ph/0101025).

### Bombin & Martin-Delgado (2007) — Color Codes and Statistical Mechanics
Stability: Error threshold p_c = 0.109(2), close to toric code — enhanced computational capabilities do NOT imply lower noise resistance. Null: factorized state of qubits; overlap with color code state = 3-body Ising partition function. Different universality classes = different computational capabilities. Full annotation: `annotations/0711.0468.md` (arXiv: 0711.0468).

### Cohen-Steiner, Edelsbrunner, Harer (2007) — Stability of Persistence Diagrams
Stability: THE foundational result. d_B(Dgm(f), Dgm(g)) ≤ ||f - g||∞. Lipschitz bound. Made TDA rigorous as statistical methodology. Matching: bottleneck distance IS optimal matching between diagram points. Full annotation: `annotations/math-0604068.md` (arXiv: math/0604068).

## Dynamical Systems

### Takens (1981) --- Detecting strange attractors in turbulence
Stability: Embedding is GENERIC (residual set in C^2 topology). The set of pairs (phi, y) where the delay map fails to be an embedding is meager (first Baire category). Topology of the reconstructed attractor is robust to small perturbations of both dynamics and observation function. Full annotation: `annotations/takens-1981.md`.

### Sauer, Yorke, Casdagli (1991) --- Embedology
Stability: PREVALENT embeddings (measure-theoretic genericity, strictly stronger than topological genericity). The set of pairs where embedding fails has measure zero in the probe sense. Works for fractal attractors (non-integer box-counting dimension). Prevalence later became a standard robustness tool across dynamical systems. Full annotation: `annotations/sauer-1991.md`.

### Dogra & Redman (2020) — Koopman Training of Neural Networks
Stability: Koopman predictions accurate over a non-trivial training window before diverging. Complexity analysis shows when partitioned Koopman training provides speedup (small partitions). Stability degrades as loss landscape becomes increasingly nonlinear. Full annotation: `by-domain/dynamical_systems.md`.

### Colbrook, Drmac, Horning (2025) — Introductory Guide to Koopman Learning
Stability: Central theme. Residuals ||K*psi - A*psi|| quantify approximation error. Pseudospectra sigma_epsilon(K) provide perturbation bounds — eigenvalues in the epsilon-pseudospectrum persist under size-epsilon perturbations. This is the spectral analogue of persistence diagram stability. Rigorous convergence proofs for generalized Laplace analysis even with continuous spectra. Full annotation: `annotations/2510.22002.md` (B2 pass 19).

### Zhou, Chu, Xu, Liu, Yu (2020) — Detecting Predictable Segments in Chaotic Time Series
Stability: Takens embedding theorem guarantees topology preservation for generic parameters. SOM clustering adds second stability layer — similar phase track segments cluster together.
Null hypothesis: Chaotic segments (L > 1) serve as the null — regions where sensitivity to initial conditions has destroyed predictable structure. Predictable segments (0 < L < 1) are the signal. Lyapunov exponent is the diagnostic. Full annotation: `annotations/10.3390-electronics9050823.md` (B2 pass 19).

### Sugihara, May, Ye, Hsieh, Deyle, Fogarty, Munch (2012) — Convergent Cross-Mapping
Stability: Convergence criterion — cross-prediction skill improves and stabilizes as library size L increases. Takens embedding provides foundational stability (diffeomorphic reconstruction for generic parameters). The convergence curve rho(L) itself is a stability diagnostic: genuine causal coupling produces monotonically improving, stabilizing prediction; absence of coupling produces flat/non-convergent skill.
Null hypothesis: No causal coupling between X and Y. Under null, cross-prediction does NOT converge. Surrogates (randomized time indices, phase-shuffled series) destroy temporal coupling while preserving marginal statistics. Granger causality as the implicit alternative-method null — CCM succeeds where Granger fails (nonlinear, non-separable systems). Full annotation: `annotations/10.1126-science.1227079.md` (DOI: 10.1126/science.1227079).

### Tsuda (2001) — Chaotic Itinerancy
Stability (ANTI-stability): The attractors themselves are destroyed — they become "ruins" (relics/ghosts) that retain geometric influence but are not true attractors. The system lingers near ruins long enough for functional computation (quasi-stability) but inevitably transitions. Milnor attractors formalize this intermediate status: basins of positive measure but not open. This is a new flavor of anti-stability distinct from the Spin-Boson case: there the perturbation produces unexpectedly large effects; here the invariant set itself is destroyed but its GHOST continues to organize dynamics.
Null hypothesis: Fixed-point attractor, limit cycle, or conventional strange attractor as null — non-itinerant dynamics where the system converges to a single invariant set. Chaotic itinerancy is the departure: the system visits multiple invariant-like sets without settling. The Kaplan-Yorke dimension and Lyapunov spectrum of the full itinerant trajectory exceed what any single attractor would produce. Full annotation: `annotations/10.1017-S0140525X01000097.md` (DOI: 10.1017/S0140525X01000097).

### Theiler, Eubank, Longtin, Galdrikian, Farmer (1992) --- Testing for nonlinearity in time series: the method of surrogate data
Null hypothesis: THE foundational surrogate data paper. Three algorithms define three null hypotheses of increasing strength: (0) random shuffle destroys all temporal correlations, (1) phase randomization preserves power spectrum but destroys phase relationships (null: linear Gaussian process), (2) AAFT preserves power spectrum + amplitude distribution (null: static nonlinear transformation of linear Gaussian process). Each surrogate type is a precise choice of what to destroy and what to preserve. Test statistic compared to surrogate ensemble by rank ordering.
Stability: Preserved quantities (power spectrum under Algorithm 1, amplitude distribution under Algorithm 2) are stability invariants -- they survive the surrogate transformation exactly by construction. The rank-ordering significance test is nonparametric (no distributional assumptions on the test statistic).
Full annotation: `annotations/10.1016-0167-2789(92)90102-S.md` (DOI: 10.1016/0167-2789(92)90102-S).

### Timmer (2000) --- What can be inferred from surrogate data testing?
Null hypothesis: The null machine's epistemics at maximum sharpness — a surrogate rejection licenses only the negation of its constructed null ("not linear Gaussian stationary"), never confirmation of the favored nonlinear alternative. Every downstream null-surrogate fix responds to this falsification/confirmation gap.
Stability: The inferred conclusion is not stable under moving the truth within the null's complement — a non-stationary linear process rejects the same null.
Full annotation: `annotations/nlin-0009032.md` (arXiv: nlin/0009032).

### Timmer (1998) --- The power of surrogate data testing with respect to non-stationarity
Null hypothesis: Quantifies the wrong-alternative firing rate — power of the surrogate test against linear *non-stationary* processes, which reject the stationary null as readily as nonlinear ones.
Stability: Power analysis = stability study of the test verdict under perturbing the true process away from the null along the stationarity direction while keeping linearity.
Full annotation: `annotations/chao-dyn-9807039.md` (arXiv: chao-dyn/9807039).

### Palus (1995) --- Detecting nonlinearity in multivariate time series
Null hypothesis: Surrogate null extended to multivariate linear stochastic processes — destroy cross-variable dependence, preserve univariate statistics.
Joint-vs-marginal: Test statistic separates general redundancy (joint dependence) from linear redundancy (marginal/Gaussian-level), so spurious rejections from imperfect surrogates are caught at the linear level before being read as nonlinearity. An early joint-vs-marginal protocol inside the null machinery, predating the permutation-consistency lineage (2005.06573).
Full annotation: `annotations/comp-gas-9507004.md` (arXiv: comp-gas/9507004).

### Guarin, Delgado, Orozco (2011) --- Band-phase-randomized surrogates
Null hypothesis: Band-split null generation — randomize only high-band phases so the constructed null retains the non-stationarity carrier; partially destructive by design.
Stability: Preserved low band = stability invariant holding drift fixed while phase structure is perturbed.
Full annotation: `annotations/1101.6063.md` (arXiv: 1101.6063).

### Donges, Donner, Kurths (2012) --- Visibility-graph irreversibility without surrogates
Null hypothesis: Reversibility null tested surrogate-free via two-sample comparison of time-directed degree/clustering distributions on standard and horizontal visibility graphs; viable on short series where surrogate ensembles are too thin.
Joint-vs-marginal: Excess structure visible only at the directed-graph encoding level — all reversal-symmetric marginals are blind to it.
Full annotation: `annotations/1211.1162.md` (arXiv: 1211.1162).

### Small, Judd, Stemler (2013) --- Surrogates for networks
Null hypothesis: Null-machine transplant to graphs — sample networks consistent with observed data + explicit null (degree distribution); asks which measured properties are typical vs peculiar. Rare explicit authorial acknowledgment of the analogy to time-series surrogate methods.
Full annotation: `annotations/1306.4064.md` (arXiv: 1306.4064).

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
- **Kawaguchi et al. (2023)** — Generalization bound Δ ≤ sqrt(I(X;Z)/n). Same form as PH stability. `annotations/2305.18887.md`.
- **Wang et al. (2021)** — HSIC bottleneck: layer-wise Lipschitz bounds as stability certificates. `second_pass.md` SP-04.
- **Wang (2026)** — Grokking as dimensional phase transition: effective dimensionality D (from FSS of gradient avalanche dynamics) crosses sub-diffusive → super-diffusive regimes at generalization, architecture-invariant. arXiv: 2604.04655. Full annotation: `annotations/10.1017-S0140525X01000097.md` (Wave 9).
- **Liu et al. (2020) SNGP** — Spectral normalization = Lipschitz constraint identical to PH stability form. `cross_domain_bridges.md`.
- **Gallicchio & Micheli (2020)** — Banach contraction (ρ(W) < 1) guarantees fixed-point convergence. `cross_domain_bridges.md`.
- **Pati & Sanders (2005)** — No partial erasure: absolute impossibility, not a bound. Strongest stability. `cross_domain_bridges.md`.
- **Garbaczewski (2005)** — H-theorem: D_KL monotonically non-increasing as Lyapunov function. `cross_domain_bridges.md`.
- **Tarnowski et al. (2019)** — Chern number: integer-valued, topologically protected, survives noisy dynamics. `second_pass.md` SP-12.

### Null Hypothesis
- **Horst & Xu (2024)** — Subcritical Hawkes → Brownian motion (same limit as Poisson null). `second_pass.md` SP-08.
- **Daw & Pender (2021)** — Poisson process (activity duration = 0) as null. `second_pass.md` SP-09.
- **Bandt (2020)** — Brownian motion as null for financial order patterns. `annotations/10.1007-s00362-020-01171-7.md`.
- **Simpson et al. (2013)** — Erdős-Rényi, configuration model, lattice as brain network nulls. `second_pass.md` SP-15.
- **Fasoli et al. (2026)** — Undirected connectivity as structural null (removes directionality). Full annotation: `annotations/10.1371-journal.pcbi.1013995.md` (DOI: 10.1371/journal.pcbi.1013995).

## Neuroscience

### Oizumi, Albantakis, Tononi (2014) — IIT 3.0
Null: partitioned system (parts operating independently) as explicit null for consciousness. Φ quantifies departure from this null via minimum information partition (MIP). Stability: exclusion postulate — the complex with maximal Φ persists; perturbations not changing which complex is maximal don't change the experience. Full annotation: `annotations/10.1371-journal.pcbi.1003588.md` (DOI: 10.1371/journal.pcbi.1003588).

### Peek, Pritam, Skerritt, Chalup (2025) --- TE + Directed PH in Spiking Systems
Null hypothesis (implicit/structural): Three levels. (1) Simple logic gate tasks (AND, OR) as baseline against which XOR's richer topology is measured. (2) Clean images as baseline; noise perturbations systematically degrade structure. Bit-moving controls for spike energy. (3) Pre-stimulus baseline epochs vs stimulus/feedback epochs in mouse cortical recordings, with Cohen's d effect sizes. Full annotation: `annotations/2508.19048.md` (arXiv: 2508.19048).

---

## Third Pass (2026-04-05)

### Stability

**Barandes Stochastic-Quantum**: Exact isomorphism — strongest possible stability. The correspondence is stable under composition. Full annotation: `third_pass_neuro_qec.md` (TP-06).

**Arovas-Zhang FQHE**: Topological protection via energy gap. Perturbations smaller than gap leave invariants unchanged. Full annotation: `third_pass_neuro_qec.md` (TP-05).

**Spin-Boson Born (ANTI-stability)**: sqrt(alpha) prompt coherence loss at weak coupling. Standard linear-in-alpha estimate underestimates decoherence. Non-Markovian effects invisible to Markovian analysis. Full annotation: `third_pass_neuro_qec.md` (TP-10).

**ConformalHDC**: Conformal prediction provides distribution-free coverage guarantees: prediction set adjusts adaptively, guarantee holds for ANY distribution. Full annotation: `third_pass_neuro_qec.md` (TP-09).

**GMI — Isomorphism Invariance**: MI measure invariant under graph relabeling. Full annotation: `third_pass_infotheo_cross.md` (TP-02).

**HSIC-Bottleneck Orthogonalization**: Prevents catastrophic forgetting by orthogonal gradient projection. Updates for new tasks constrained to directions that don't interfere with old. Full annotation: `third_pass_infotheo_cross.md` (TP-09).

**Entropic Symmetry Breaking**: Critical slowing down = loss of stability. Diverging relaxation time near bifurcation. Entropy diagnostics provide early warning. Full annotation: `third_pass_dynamics_tda.md` (TP-04).

**Pointwise Ergodic Theorem**: Time averages = space averages almost everywhere. Measurement robust to starting point. Full annotation: `third_pass_dynamics_tda.md` (TP-16).

### Null Hypothesis

**Dabney Distributional Code**: Schultz mean-RPE model as null. Distributional hypothesis predicts asymmetric responses and neuron-specific reversal points; data decisively rejects null. Full annotation: `third_pass_neuro_qec.md` (TP-03).

**Ordinal Networks**: Exact analytical null for random (IID) series — known adjacency matrix. Departures indicate temporal dependence. Full annotation: `third_pass_dynamics_tda.md` (TP-05).

**Visibility Graph Irreversibility**: Reversible process as null. KL divergence between forward and reversed directed visibility graphs. Full annotation: `third_pass_dynamics_tda.md` (TP-06).

**CP-PINNs**: Constant-parameter PDE as null. Each detected changepoint rejects the null for a specific time interval. TV penalty controls false positive rate. Full annotation: `third_pass_dynamics_tda.md` (TP-08).

**MI-NEE**: Common uniform reference as null for both joint and marginal. Triangulation approach. Full annotation: `third_pass_infotheo_cross.md` (TP-08).

### Stability Taxonomy (Expanded)

The taxonomy now extends to 6 flavors:
1. **Lipschitz** (TDA) — bottleneck ≤ Hausdorff
2. **Exponential suppression** (QEC) — threshold theorem
3. **Topological protection** (FQHE) — energy gap makes invariants immune to small perturbations
4. **Anti-stability / perturbation-amplifying** (Spin-Boson) — sqrt singularity means even infinitesimal perturbation produces finite effect
5. **Distribution-free** (Conformal prediction) — guarantee holds regardless of data distribution
6. **Ghost stability** (Tsuda CI) — the attractor is destroyed but its geometric remnant (ruin) continues to organize dynamics transiently. Quasi-stability without a true invariant set. Distinct from #4: there, the invariant set exists but is more fragile than expected; here, the invariant set does not exist but its ghost provides transient trapping

---

## Wave 4c (2026-04-06) — Foundational Threshold Theorems (Stability x QEC)

### Stability

**Aharonov & Ben-Or (1997/1999) — Threshold Theorem**: THE foundational stability result for quantum computation. If eta < eta_c (constant), arbitrarily long quantum computations can be performed with arbitrarily high reliability at polylogarithmic overhead. Doubly-exponential error suppression: (c*eta)^{2^r} after r levels of concatenation. Holds for very general noise (probabilistic, decoherent, amplitude damping, depolarizing, correlated). The quantum analogue of von Neumann's 1956 classical fault-tolerance result. Full annotation: `annotations/quant-ph-9906129.md` (arXiv: quant-ph/9906129).

**Knill, Laflamme, Zurek (1998) — Threshold Theorem**: Independent proof via 7-qubit Steane code. Effective error c^{2^h-1} p^{2^h} after h concatenation levels. Explicit numerical threshold ~3 x 10^{-6} from counting minimal failure pairs in recovery network. Extends to quasi-independent stochastic and monotone error models. Full annotation: `annotaquant-ph-9702058.19048.md` (arXiv: quant-ph/9702058).

**Breuckmann & Eberhardt (2021) — LDPC Stability**: Multiple stability levels. Gottesman's constant overhead theorem: LDPC codes can reduce fault-tolerance overhead to a CONSTANT (not polylogarithmic). Hyperbolic surface code thresholds under MWPM/union-find decoders. Systolic geometry connects code distance to shortest non-contractible submanifold. Full annotation: `2103.06309s/2508.19048.md` (arXiv: 2103.06309).

### Null Hypothesis

**Aharonov & Ben-Or**: Uncorrected quantum circuit as null. Error accumulates without bound. Gap between corrected (exponentially suppressed) and uncorrected (linear growth) quantifies the value of error correction.

**Knill, Laflamme, Zurek**: Unencoded quantum network as null. "The effect of noise will accumulate and ruin the entire computation, and hence the computation must be protected."

**Breuckmann & Eberhardt**: Surface code as implicit null/baseline. All LDPC constructions benchmarked against surface code parameters (k=1, d~sqrt(n)). Classical random LDPC codes (which are trivially good) as the gold standard that quantum codes have not yet achieved.

### Stability Taxonomy Note

The three threshold papers refine flavor #2 (exponential suppression) into sub-flavors:
- **2a. Concatenation-based** (Aharonov-Ben-Or, Knill-Laflamme-Zurek): doubly-exponential suppression (c*p)^{2^r}, polylogarithmic overhead
- **2b. Topological/surface-code** (Dennis-Kitaev-Landahl-Preskill, already indexed): exponential suppression e^{-c*d}, overhead grows with code distance
- **2c. LDPC constant-overhead** (Gottesman via Breuckmann-Eberhardt): polynomial suppression 1/g(n), but CONSTANT overhead — no growing resource cost

---

## Wave 6 — Directed Information Flow Null Hypothesis Methods (2026-04-07)

### Lobier, Siebenhuhner, Palva, Palva (2014) — Phase Transfer Entropy
DOI: 10.1016/j.neuroimage.2013.08.056
**Null hypothesis**: Surrogate data destroys phase coupling while preserving spectral properties. No false positives under realistic noise + linear mixing levels. Same destroy-structure/preserve-statistics pattern as Theiler surrogates, specialized for oscillatory phase data. Sensitivity comparable to or better than prior TE implementations across range of noise and mixing values.
**Parameterized homology**: Frequency band as discrete parameter. Different oscillatory bands yield different directed connectivity graphs. Coupling strength and direction can reverse across bands --- the "topology" of the directed network changes with the frequency parameter.
Full annotation: `annotations/2508.19048.md` (Wave 6).

### Shorten, Spinney, Lizier (2021) — Continuous-Time TE for Spike Trains
DOI: 10.1371/journal.pcbi.1008054
**Null hypothesis**: Two key contributions. (1) NEGATIVE result: source-time-shift surrogates --- the standard method --- fail for continuous-time spike trains. They do not properly instantiate the null of conditional independence because time-shifting a point process changes inter-event statistics in ways that couple to the target. (2) POSITIVE result: local permutation surrogates correctly test conditional independence even with strong pairwise correlations. This is methodologically important --- the paper shows that naive null construction can lead to both false positives and false negatives.
**Stability (implicit)**: kNN estimator is provably consistent (converges to true TE). Discrete-time estimator converges to the WRONG VALUE --- an anti-stability result for the standard approach. The continuous-time estimator converges orders of magnitude faster, a practical stability advantage.
**Parameterized homology**: Continuous timescale as parameter. Pathwise TE decomposes into jump contributions (at spikes) and continuous contributions (between spikes), parameterizing information flow by event type and inter-event interval.
Full annotation: `annotations/2508.19048.md` (Wave 6).

---

## Wave 10 — link-forge update (2026-04-17)

### Baudot, Tapia, Bennequin & Goaillard (2019) — Topological Information Data Analysis
arXiv: 1907.04242. Stability: H_k, I_k have linearly independent gradients on open dense set of probability simplex — structural stability under perturbation. Information paths empirically robust across sample sizes and graining. Null: shuffling destroys dependences, I_k = 0 as null reference. Full annotation: `annotations/2508.19048.md` (Wave 10a).

### Ghorbanchian et al. (2020) — Higher-order simplicial synchronization
DOI: 10.1038/s42005-021-00605-4. Stability: hysteresis region = bistability. Synchronized state persists under decreasing σ until lower critical value. Full annotation: `annotations/2508.19048.md` (Wave 10a).

### Dey, Mrozek & Slechta (2021) — Conley-Morse graph persistence
arXiv: 2107.02115. Stability: Conley index invariant under choice of index pair. Intersection property guarantees zigzag intermediates are genuine. Noise-resilient thickened index pairs. Full annotation: `annotations/2508.19048.md` (Wave 10a).

### Petri et al. (2014) — Homological scaffolds
DOI: 10.1098/rsif.2014.0873. Null: placebo condition as experimental null. Psilocybin produces many transient structures + few highly persistent ones not seen under placebo. Gap quantifies drug's effect on brain topology. Full annotation: `annotations/2508.19048.md` (Wave 10a).

### Chaudhuri et al. (2019) — Head direction ring attractor
DOI: 10.1038/s41593-019-0460-x. Stability: ring manifold isometric and invariant across waking and REM sleep. S^1 topology robust to perturbation of brain state, sensory input, neuromodulatory context. Geometric stability (isometry) stronger than topological invariance. Full annotation: `annotations/2508.19048.md` (Wave 10a).

### Chung, El-Yaagoubi, Qiu & Ombao (2025) — From Density to Void
arXiv: 2503.14700. Anti-stability: higher-order topological features not reproducible across subjects. Overlap probability decays exponentially with simplex dimension. Null: FDR-corrected testing shows no significant higher-order interactions. Full annotation: `annotations/2508.19048.md` (Wave 10b).

### Dabaghian, Brandt & Frank (2014) — Hippocampal map as topological template
eLife.03476. Stability: topological representation invariant under geometric deformation (track morphing) and direction reversal. Null: geometric coding hypothesis rejected — place fields do not track metric features. Full annotation: `annotations/2508.19048.md` (Wave 10b).

### Donato et al. (2016) — PH analysis of Phase Transitions
arXiv: 1601.03641. Stability: PH detects phase transition despite extremely sparse sampling (300 landmarks from 6K snapshots). Robust to metric approximation and subsampling. Null: φ^4 model as negative control — no topological signal at phase transition, validating PH specificity. Full annotation: `annotations/2508.19048.md` (Wave 10b).

### Batko, Mischaikow, Mrozek & Przybylski (2019) — Conley Index from Sampled Dynamics
arXiv: 1904.03757. Stability: isolating neighborhoods persist under ε-perturbations (Theorem 3.2). Continuous ε-approximations inherit same Conley index via continuation/homotopy argument. Quantitative ε bounds from data to dynamics. Full annotation: `annotations/2508.19048.md` (Wave 10b).

### Jost & Zhang (2023) — Cheeger inequalities on simplicial complexes
arXiv: 2302.01069. Stability: spectral gap of Hodge Laplacian bounded from below by Cheeger constant — spectral stability from combinatorial topology. Perturbations preserving simplicial structure cannot collapse spectral gap below Cheeger bound. Full annotation: `annotations/2508.19048.md` (Wave 10c).

### Trinca, Bollauf & Zamir (2024) — n-Dimensional Toric Codes from Lattice Codes
arXiv: 2410.20233. Stability: interleaving distance between n-D toric codes inherits lattice geometry. Burst error correction from lattice structure — code distance scales with systole of T^n. Full annotation: `annotations/2508.19048.md` (Wave 10c).

### Curry, DeSha, Hoff, Limberger, Luo & Qin (2022) — Decorated merge trees for persistent topology
DOI: s41468-022-00089-3. Stability: DMT metric is stable — bounded by interleaving distance of underlying PH modules. Gromov-Wasserstein coupling provides computable stable metric on merge trees. Full annotation: `annotations/2508.19048.md` (Wave 10c).

### B2 batch-004: LDPC / belief-propagation phase diagrams (2026-08-25)

**Aref, Macris & Vuffray (2013)** — arXiv: 1307.5210. Stability: dynamical and condensation transition temperatures of the test-channel Gibbs measure computed by cavity method; spatial coupling saturates dynamical toward condensation, which approaches the Shannon noise level. Null hypothesis: Shannon rate-distortion limit as ideal-matcher reference. Full annotation: `annotations/1307.5210.md` (B2 pass 28). **See also**: `by-domain/information_theory.md`.

**Jain, Koehler, Liu & Mossel (2019)** — arXiv: 1905.10031. Stability: bounded-memory message-passing transition proved strictly below the Kesten–Stigum/BP threshold; asymptotic normality at criticality. Matching: optimal transport bounds message accuracy in the proof. Full annotation: `annotations/1905.10031.md` (B2 pass 28). **See also**: `by-domain/statistical_physics.md`.

**Vicente, Saad & Kabashima (1999)** — arXiv: cond-mat/9908358. Stability: replica-method decoding transition of irregular LDPC ensembles; its location placed on Shannon's coding bound by degree-distribution choice. Null hypothesis: Shannon bound as the transition point itself. Full annotation: `annotations/cond-mat-9908358.md` (B2 pass 29). **See also**: `by-domain/information_theory.md`.

**Decelle, Krzakala, Moore & Zdeborová (2011)** — arXiv: 1109.3041. Stability: cavity-method phase diagram of the stochastic block model — detectability/undetectability transition (KS-style null boundary for planted structure) and easy/hard transition (statistical-to-computational gap); translates into asymptotically optimal BP detection. Canonical detectability-transition anchor. Full annotation: `annotations/1109.3041.md` (B2 pass 29). **See also**: `by-domain/statistical_physics.md`.

*Batch-004 ldpc-bp group closed 4/4 (B2 pass 29).*

### B2 batch-005: channel-capacity phase transitions (2026-08-25)

**Choi, Bao, Qi & Altman (2019)** — arXiv: 1903.05124. Entanglement-scaling invariant (volume-law ↔ area-law) tracked across measurement rate and scrambling degree; transition = QEC error threshold; quantum channel capacity itself undergoes the transition. Null: above-threshold area-law states erase all hidden logical structure. Canonical MIPT-as-QEC anchor. Full annotation: `annotations/1903.05124.md` (B2 pass 30). **See also**: `by-domain/qec.md`.

**Qian & Roy (2011)** — arXiv: 1112.4589. Channel capacity tracked along the free-energy-expenditure parameter; zero exactly at the equilibrium (detailed-balance) null. Full annotation: `annotations/1112.4589.md` (B2 pass 30). **See also**: `by-domain/information_theory.md`.

**Plenio & Virmani (2007)** — arXiv: quant-ph/0702059. Capacity-under-correlated-error as a function of memory strength with genuine non-analytic points; dictionary to spin-chain criticality. Full annotation: `annotations/quant-ph-0702059.md` (B2 pass 30). **See also**: `by-domain/qec.md`.

**Bereyhi, Loureiro, Krzakala, Müller & Schulz-Baldes (2022)** — arXiv: 2205.08782. All-or-nothing inference transition of nonlinear Gaussian random fields; replica proof that the critical rate equals the channel capacity (and wiretap secrecy capacity under binning). Null: above-critical reconstruction uncorrelated with data. Full annotation: `annotations/2205.08782.md` (B2 pass 31). **See also**: `by-domain/information_theory.md`.

**Kabashima, Murayama & Saad (1999)** — arXiv: cond-mat/9908104. Typical-case performance of Gallager-type codes across sparse-matrix-density families: capacity-saturating vs sub-capacity classes; TAP ≡ BP decoding identity. Full annotation: `annotations/cond-mat-9908104.md` (B2 pass 31). **See also**: `by-domain/statistical_physics.md`.

**Kelly, Poschinger, Schmidt-Kaler, Fisher & Marino (2022)** — arXiv: 2210.11547. Coherence-tuned phase transition in entanglement and quantum channel capacity under adversarial measurement pressure; coherence bounds stabilizer code distance. Full annotation: `annotations/2210.11547.md` (B2 pass 31). **See also**: `by-domain/qec.md`.

**Ashikaga & Asgari-Targhi (2017)** — arXiv: 1708.03990. Channel capacity / MI / transfer entropy as a spatially-resolved invariant field over a driven cardiac system; wavebreak sites initiating ventricular fibrillation are the loci of invariant character change — order parameter located by information profile. Closes the channel-capacity group 7/7. Full annotation: `annotations/1708.03990.md` (B2 pass 32). **See also**: `by-domain/dynamical_systems.md`, `by-domain/neuroscience.md`.

### B2 batch-005: ph-stability foundations (2026-08-25)

**Bubenik & Scott (2012)** — arXiv: 1205.3669. Persistence modules as diagrams indexed by (ℝ, ≤) in an arbitrary target category; interleaving distance generalizes bottleneck distance and stability theorems are greatly generalized; category of interleavings is abelian when the target is. Stability as categorical property rather than per-construction inequality. Full annotation: `annotations/1205.3669.md` (B2 pass 32). **See also**: `by-domain/tda.md`, `by-structure/filtrations.md`.

**Gulen & McCleary (2022)** — arXiv: 2201.06650. Galois connections unify interleavings and matchings; Rota's theorem yields an easier proof of bottleneck stability; multiparameter persistence notions related. Second, order-theoretic route to the stability guarantee. Full annotation: `annotations/2201.06650.md` (B2 pass 32). **See also**: `by-domain/tda.md`, `by-structure/filtrations.md`, `by-structure/optimal_transport.md`.

### B2 batch-006: GW-theory core (2026-08-25)

**Weitkamp, Proksch, Tameling & Munk (2020)** — arXiv: 2006.12287. Null-hypothesis side: the beta-trimmed GW lower bound becomes a pose-invariant discrimination test with proven distributional limits under the isomorphism null; trimming adds outlier mass robustness inside the statistic itself. Full annotation: `annotations/2006.12287.md` (B2 pass 35). **See also**: `by-domain/tda.md`, `by-structure/optimal_transport.md`.

**Lim & Mémoli (2022)** — arXiv: 2201.09385. Stability side: generalized cMDS output stable w.r.t. Gromov-Wasserstein perturbation of the input mm-space; negative-eigenvalue sum vanishes exactly on Euclidean-flat reference structure (weak null-hypothesis reading). Full annotation: `annotations/2201.09385.md` (B2 pass 35). **See also**: `by-domain/tda.md`, `by-structure/optimal_transport.md`.

**Hohmeier, Fraiman & Moosmueller (2026)** — arXiv: 2606.10295. Statistical-limit side: universal consistency of GW-k-NN on weak-isomorphism classes — classification risk converges to Bayes risk only after quotienting by structure-annihilating equivalence; the null reading is the quotient itself. Full annotation: `annotations/2606.10295.md` (B2 pass 36). **See also**: `by-domain/tda.md`, `by-structure/optimal_transport.md`.

### B2 batch-007: decoder-side threshold shifts (2026-08-25)

**Higgott & Gidney (2023)** — arXiv: 2303.15933. Sparse blossom MWPM operating deep in the sub-threshold regime at hardware syndrome rates; throughput-matched decoding as a stability claim about sustained noisy streams. Full annotation: `annotations/2303.15933.md` (B2 pass 40). **See also**: `by-domain/qec.md`.

**Pattison, Beverland, da Silva & Delfosse (2021)** — arXiv: 2107.13589. Threshold raised 25% over any hard decoder by decoding from the joint analog outcome distribution instead of its binary marginal — the critical error rate itself moves with decoder information access; measurement-time parameter carries a resolution-vs-disturbance trade-off. Full annotation: `annotations/2107.13589.md` (B2 pass 40). **See also**: `by-domain/qec.md`.

**Higgott, Bohdanowicz, Kubica, Flammia & Campbell (2022)** — arXiv: 2203.04948. Belief-propagation posteriors feeding matching shift the circuit-noise threshold 0.82% → 0.94%; fragile boundaries make the resource-optimal code geometry reverse across noise regimes. Full annotation: `annotations/2203.04948.md` (B2 pass 40). **See also**: `by-domain/qec.md`, `by-structure/boundary_operators.md`.

**Baireuther, O'Brien, Tarasinski & Beenakker (2017)** — arXiv: 1705.07855. LSTM decoder trained on experimental syndrome data outperforms MWPM by exploiting X–Z error correlations matching factorizes away — the threshold-relevant information content of the syndrome stream exceeds its marginal decomposition. Full annotation: `annotations/1705.07855.md` (B2 pass 41). **See also**: `by-domain/qec.md`, `by-structure/composite_systems.md`.

**Hack, Menti, Lazaro & Paler (2026)** — arXiv: 2603.05381. Belief propagation re-carried on the decoding graph reaches standalone thresholds close to MWPM where Tanner-graph BP has none — the stability boundary is reachable by message passing alone once the carrier graph matches the matching substrate. Full annotation: `annotations/2603.05381.md` (B2 pass 41). **See also**: `by-domain/qec.md`.

### B2 batch-008: kuramoto — transition classification and taxonomy (2026-08-25)

**Lee, Kuklinski & Timme (2025)**: arXiv: 2505.10114. "Extreme synchronization transitions" in complexified Kuramoto systems look like explosive phase transitions but occur at finite N as multi-dimensional bifurcations (order parameter ~N^{-1/2} → ~1 past critical coupling) — a built-in falsification test for transition-vs-bifurcation inference from order-parameter jumps. Machines: null hypothesis (core), stability. Full annotation: `annotations/2505.10114.md` (B2 pass 46). **See also**: `by-domain/dynamical_systems.md`.

**Oh, Lee, Kahng & Kim (2006)**: arXiv: cond-mat/0606048. Eight synchronization-transition behaviors on scale-free networks indexed by coupling-degree exponent η and degree exponent λ, split at η = λ−2 into zero-/finite-J_c regimes; critical exponents and cluster-size distributions per regime. Machines: parameterized homology (transition-class taxonomy), stability (finite-size scaling). Full annotation: `annotations/cond-mat-0606048.md` (B2 pass 46). **See also**: `by-domain/statistical_physics.md`.
