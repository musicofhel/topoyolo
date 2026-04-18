# Filtrations (Parameterized Homology)

Papers instantiating the **parameterized homology** abstract machine: tracking how topological or structural invariants change as a parameter varies. This includes persistence diagrams, error thresholds, bifurcation diagrams, rate-distortion curves, and information-plane trajectories.

The shared pattern: there is a parameter ε (scale, error rate, coupling strength, training epoch, constraint density) and an invariant I(ε) (Betti number, logical error rate, attractor count, MI). The paper studies how I(ε) changes — births, deaths, transitions, critical values.

---

## Information Theory / Machine Learning

### Wickstrøm et al. (2019) — Information Plane via Rényi Entropy
Parameter: training epoch. Invariant: I(X;T) and I(T;Y). Two phases: fitting (both increase) and compression (I(X;T) decreases). Full annotation: `by-domain/information_theory.md`.

### Tax, Mediano & Shanahan (2017) — PID of Generative NNs
Parameter: training epoch. Invariant: PID atoms (synergy, redundancy, unique). Phase transition from redundant to specialized. Full annotation: `by-domain/information_theory.md`.

### Chwilka & Karbowski (2024) — Lognormal MI
Parameter: variance σ². Invariant: MI. Phase boundary where MI diverges at finite σ². Full annotation: `by-domain/information_theory.md`.

### Geiger (2021) — Information Plane Review
Parameter: training epoch. Reviews whether fitting → compression trajectory is real or estimation artifact. Distinguishes geometric from information-theoretic compression. Full annotation: `by-domain/information_theory.md`.

### Jónsson et al. (2020) — DNN Convergence with MI Regularization
Parameter: training epoch. Confirms compression phase in VGG-16 via MINE. MI-based regularization stabilizes the trajectory. Full annotation: `by-domain/information_theory.md`.

### Shwartz-Ziv & Tishby (2017) — Opening the Black Box of DNNs via Information
Parameter: training epoch. Invariant: (I(X;T), I(T;Y)) per layer. Origin paper for the information plane. Two phases: fitting (drift, both MI increase) then compression (diffusion, I(X;T) decreases). Converged layers lie on the IB bound with layer-specific beta. DPI chain across layers creates monotonic information path = filtration. **Caveat**: compression phase contested — may require saturating activations + binning estimator (Saxe 2018, Geiger 2021). Full annotation: `inbox.md` (arXiv: 1703.00810).

## Statistical Physics

### Mézard & Mora (2008) — Constraint Satisfaction
Parameter: constraint density α = M/N. Invariant: solution space topology. Phase transitions at α_d (BP fails) and α_c ≈ 4.267 (SAT/UNSAT). Solution cluster shattering. Full annotation: `by-domain/information_theory.md`.

---

## TDA

### Mollers, Immer, Fortuin, Isufi (2023) — Hodge-Aware Contrastive Learning
Parameter: SCNN filter coefficients. Invariant: Hodge component proportions (gradient, curl, harmonic). The learned representations are parameterized by spectral weights on the three Hodge subspaces. The harmonic space ker(L_1) IS the first homology — the Hodge theorem made computational. Full annotation: `by-domain/tda.md`.

### de Jesus Jr., Fernandez-Navarro, Carbonero-Ruz (2025) — TDA for Financial Forecasting
Parameter: sliding window position (time) and Vietoris-Rips scale (epsilon). Invariant: persistent entropy, amplitude, point count from persistence diagrams. Sliding-window PH on time-delay embedded financial time series. First application of TDA-derived features specifically for forecasting (vs. classification/detection). Tested on 32 datasets across crypto and traditional instruments. Full annotation: `by-domain/tda.md`.

### Perea & Harer (2013) — SW1PerS
Parameter: TWO — Rips scale ε AND window size/embedding dimension. Invariant: H₁ persistence (periodicity score). Sliding window embedding of time series → point cloud → Rips PH. Convergence theorems + dependency estimates. Bridge paper: Takens (dynamics) + persistence (TDA). Full annotation: `inbox.md` (arXiv: 1307.6188).

### Harrington, Otter, Schenck, Tillmann (2017) — Stratifying Multiparameter PH
Parameter: MULTIPLE simultaneous parameters (bifiltration). Invariant: multigraded module over polynomial ring. Three partial invariants: associated primes, Hilbert series, local cohomology. No complete discrete invariant (unlike 1-param barcode). Full annotation: `inbox.md` (arXiv: 1708.07390).

### Di Rocco, Eklund, Weinstein (2019) — Bottleneck Degree of Algebraic Varieties
Parameter: scale at which topology is probed. Invariant: reach tau_X = min(rho, b). The reach determines the sample density needed for persistent homology to recover correct topology. Bottleneck degree bounds the number of critical parameter values where topology might change. Formula in terms of Chern classes and polar classes. Full annotation: `by-domain/tda.md`.

### Kanjamapornkul, Pincak, Bartos (2020) — Cohomology Theory for Financial Time Series
Parameter: Wilson loop parameter (trader interaction strength). Invariant: cohomological classification (8 market states, 16 physiological cones). Market phase transitions parameterized by Yang-Mills field coupling. Full annotation: `by-domain/tda.md`.

### Adams et al. (2017) — Persistence Images
Parameter: filtration scale epsilon (Vietoris-Rips or sublevel set). Invariant: persistence diagram vectorized into fixed-size R^n vector via weighted Gaussian sum + pixel grid integration. The persistence image IS a featurization of parameterized homology — it converts the birth-death pairs from any filtration into a form amenable to ML. Resolution and variance are secondary parameters controlling the vectorization itself. Stable w.r.t. W_1 (Theorems 1-4). Applications to dynamical systems parameter inference (linked twist map, Kuramoto-Sivashinsky PDE). Full annotation: `inbox.md` (arXiv: 1507.06217), `by-domain/tda.md`.

### Bauer (2021) --- Ripser
Parameter: Vietoris-Rips scale epsilon. Invariant: persistence barcode (birth-death intervals). THE standard computational implementation of parameterized homology for VR complexes. Apparent/emergent pair optimizations + clearing + implicit coboundary matrix. Full annotation: `inbox.md` (arXiv: 2108.03831).

### Peek, Pritam, Skerritt, Chalup (2025) --- TE + Directed PH in Spiking Systems
Parameter: inverted transfer entropy (strongest information transfer first). Invariant: directed Betti curves beta_d(epsilon), AUBC scalars, persistence diagrams. Higher-dimensional features (d=2,3) discriminate task complexity. Wasserstein distances between PDs recover graded task space geometry. Full annotation: `inbox.md` (arXiv: 2508.19048).

## QEC

### Oreshkov (2013) — Continuous-time quantum error correction
Parameter: ratio kappa/lambda (error correction rate / decoherence rate). Invariant: protected quantum information (fidelity). Regimes: kappa >> lambda (Zeno, information frozen), kappa ~ lambda (partial protection), kappa << lambda (information lost). Non-Markovian regime shows quadratic improvement (lambda^4/kappa^2 vs. lambda^2/kappa). Full annotation: `by-domain/qec.md`.

*(See also inbox for de la Fuente error threshold at ~2.5%)*

## Dynamical Systems

### Takens (1981) --- Detecting strange attractors in turbulence
Parameter: embedding dimension d. Invariant: faithfulness of delay embedding (diffeomorphic vs non-injective). Critical value: d > 2*dim(M). Below threshold, reconstruction has self-intersections (wrong topology); above, it is diffeomorphic to the attractor (correct homology). Weak parameterized homology -- the parametric dependence is implicit, not tracked. Full annotation: `inbox.md`.

### Sauer, Yorke, Casdagli (1991) --- Embedology
Parameter: embedding dimension d. Invariant: faithful embedding (prevalent). Critical value: d > 2*d_B(A) where d_B is box-counting dimension (can be non-integer). Extends Takens' filtration to fractal attractors -- the critical embedding dimension is now any real number, not just twice an integer. Full annotation: `inbox.md`.

### Dogra & Redman (2020) — Koopman Training of Neural Networks
Parameter: training step t. Invariant: Koopman eigenvalues (dynamical modes of weight evolution). Dominant eigenvalues = persistent modes; decaying eigenvalues = transient features. Weight trajectory in weight space treated as discrete dynamical system; Koopman operator lifts nonlinear dynamics to linear spectral analysis. Full annotation: `by-domain/dynamical_systems.md`.

### Colbrook, Drmac, Horning (2025) — Introductory Guide to Koopman Learning
Parameter: dictionary size N (finite-dimensional truncation). Invariant: spectral type of Koopman operator (point, absolutely continuous, singular continuous spectrum). Convergence of EDMD approximations as N grows. Spectral measures decompose dynamics into periodic, mixing, and fractal components. Residuals as convergence diagnostics. Full annotation: `by-domain/dynamical_systems.md`.

### Zhou, Chu, Xu, Liu, Yu (2020) — Detecting Predictable Segments in Chaotic Time Series
Parameter: embedding dimension m and time delay tau (phase space reconstruction). Invariant: attractor topology and Lyapunov exponent L. As m increases, the reconstructed phase space converges to the true attractor topology (Takens). L classifies predictability: 0 < L < 1 (predictable), L > 1 (unpredictable). SOM clustering separates phase track segments by dynamical regime. Full annotation: `by-domain/dynamical_systems.md`.

---

## Cross-domain observation

The parameter takes different forms across domains, but the structure is isomorphic:

| Domain | Parameter | Invariant tracked | Critical transition |
|---|---|---|---|
| TDA | Scale epsilon | Betti numbers, persistence | Birth/death of features |
| TDA (algebraic) | Sample density | Reach (bottleneck width) | Topology recovery threshold |
| QEC | kappa/lambda ratio | Fidelity (protected information) | Zeno boundary |
| Dynamical systems | Dictionary size N | Koopman spectrum | Spectral convergence |
| Dynamical systems | Embedding dimension m | Attractor topology | Takens faithful embedding |
| Information theory | Training epoch | MI, PID atoms | Fitting/compression boundary |
| Finance/TDA | Sliding window position | Persistence features | Regime transitions |
| Neuroscience/dynamics | Time (itinerancy epoch) | Local attractor topology | Attractor ruin transitions (Tsuda CI) |

---

## From Second Pass + Bridges

### Hawkes Processes (new domain for this machine)
- **Horst & Xu (2024)** — Criticality m as filtration parameter. Phase transition at m=1: subcritical → Brownian, critical → CIR process. `second_pass.md` SP-08.
- **Mei & Eisner (2017)** — Intensity λ_k(t) tracked continuously. Neural ODE-like interpolation between events. `second_pass.md` SP-05.
- **Daw & Pender (2021)** — Activity duration parameterizes path from Poisson null to full Hawkes. `second_pass.md` SP-09.

### Information Bottleneck
- **Shwartz-Ziv & Tishby (2017)** — Training epoch as parameter. Fitting → compression phases. SGD drift → diffusion transition. `second_pass.md` SP-01.
- **Kawaguchi et al. (2023)** — β (Lagrange multiplier) traces curve through representation space. `cross_domain_bridges.md`.

### Other
- **Bandt (2020)** — Lag parameter d as filtration. Pattern frequencies constant for small d (scale invariance). `second_pass.md` SP-13.
- **Tarnowski et al. (2019)** — Post-quench time as parameter. Vortex trajectories encode Chern number. `second_pass.md` SP-12.
- **Gallicchio & Micheli (2020)** — GNN layer depth = scale parameter. Receptive field grows with depth like Rips filtration. `cross_domain_bridges.md`.
- **Fasoli et al. (2026)** — Inter-hemispheric connectivity strength as bifurcation parameter. Attractor count changes at critical values. `cross_domain_bridges.md`.
- **Darmon (2018)** — Entropy rate lifted from scalar to function on state space — parameterized by position on attractor. `cross_domain_bridges.md`.

---

## Third Pass (2026-04-05)

### Neuroscience

**Dabney et al. (2020) — Distributional Code**: Quantile index tau parameterizes the dopamine neuron family (tau ∈ [0,1]). Each neuron has a different reversal point. As tau varies, the full reward distribution is traced out. Full annotation: `third_pass_neuro_qec.md` (TP-03).

**Summary Statistics Review** (arXiv: 2504.16920): Training epoch as parameter. Summary statistics (representational similarity, dimensionality, alignment) tracked during learning. Conserved across individuals and species. Full annotation: `third_pass_neuro_qec.md` (TP-11).

**EEG Frequency as Filtration**: Three papers (GC-STCL, Driver Fatigue GC, Nonparametric Brain GC) converge on the same pattern: EEG frequency bands function as a filtration parameter for brain causal networks. Different frequencies reveal different causal topologies. This is structurally identical to persistence: track causal network topology as the frequency "scale" varies. The neuroscience community has not connected this to TDA's filtration framework.

**Tsuda (2001) — Chaotic Itinerancy** (DOI: 10.1017/S0140525X01000097): Time as parameter. The itinerant trajectory visits attractor ruins with different local topologies — each quasi-stable epoch has its own attractor geometry (dimension, basin structure, Lyapunov spectrum). The sequence of visited ruins IS a path through topology space, parameterized by time. Structurally analogous to a barcode where each bar is a quasi-stable epoch and transitions are births/deaths. This is a new filtration type: the parameter is time and the invariant is the LOCAL attractor topology (which changes discretely at transition events). Full annotation: `inbox.md`.

### QEC / Condensed Matter

**Arovas-Zhang FQHE (1992)**: Filling fraction nu = p/q parameterizes the family of topological phases. At each rational filling, different anyonic excitations. Energy gap protects the phase. Full annotation: `third_pass_neuro_qec.md` (TP-05).

**Spin-Boson Born Approximation**: Coupling strength alpha as parameter. sqrt(alpha) prompt coherence loss — non-analytic singularity even at weak coupling. Anti-stability: system less stable than Markovian analysis suggests. Full annotation: `third_pass_neuro_qec.md` (TP-10).

**Berry et al. (2023) — Quantum Advantage in TDA**: TWO parameterizations. (1) Standard TDA: distance scale epsilon determines which simplices exist; Betti numbers tracked as epsilon varies (persistent homology). (2) Dimension k: classical complexity exponential in k, quantum polynomial. The quantum advantage IS the ability to probe high-dimensional homology efficiently. Super-quadratic speedup requires multiplicative error + growing Betti number. Full annotation: `inbox.md` (arXiv: 2209.13581).

**Hastings & Haah (2021) — Floquet Code**: THE paradigm case of time-parameterized homology in QEC. Measurement round r parameterizes the ISG S(r) in period-3 cycle. Logical operator dynamics have period 6 (electric <-> magnetic exchange = monodromy). Logical qubits emerge from the PERIODIC ORBIT of the code, not from any snapshot (each snapshot has trivial homology as subsystem code). Structurally identical to Floquet theory in dynamical systems: stroboscopic map defines effective code, logical qubits are persistent eigenspace. Full annotation: `inbox.md` (arXiv: 2107.02194).

### Dynamical Systems

**Cross-Correlation Integral**: Scale parameter epsilon in C(epsilon). Correlation dimension as fractal analogue of Betti number. Nonstationarity detected as gap between cross and auto integrals. Full annotation: `third_pass_dynamics_tda.md` (TP-03).

**Entropic Symmetry Breaking** (arXiv: 2510.03572): Control parameter (temperature, coupling) parameterizes family. Entropy singularity at critical point. Critical slowing down = loss of stability diagnostic. Full annotation: `third_pass_dynamics_tda.md` (TP-04).

**CP-PINNs**: PDE parameters θ(t) piecewise constant with unknown changepoints. Total Variation enforces sparsity of transitions. Full annotation: `third_pass_dynamics_tda.md` (TP-08).

**Hom-Lie Cochain Complexes**: Twisting map α parameterizes family of algebraic structures. As α deviates from id, cohomology changes — some classes persist, others born/die. Full annotation: `third_pass_dynamics_tda.md` (TP-14).

### Information Theory

**Finite-Time MI** (Zhu et al. 2024): Observation window t as parameter. I(t)/t can exceed Shannon capacity C (exceed-average phenomenon). Mercer expansion connects to eigenvalue spectrum. Full annotation: `third_pass_infotheo_cross.md` (TP-03).

### Cross-Domain Observation

### Varley, Mediano, Patania & Bongard (2025) — The Topology of Synergy
PLoS Comput. Biol., DOI: 10.1371/journal.pcbi.1013649. arXiv: 2504.10140.
Parameter: Rips filtration scale epsilon (Chebyshev distance). Invariants tracked: H2 average persistence and void count. Key finding: these topological summaries correlate with O-information (joint-vs-marginal excess). Synergy-dominated triads have more numerous, longer-lived H2 features. PCA rotation weakens but does not eliminate the correlation for O-bar (intrinsic synergy persists).
**Machines**: parameterized homology, chain complex, joint-vs-marginal, null hypothesis, stability.
Full annotation: `inbox.md` (Wave 7).

### Cross-Domain Observation

The third pass identifies a new filtration parameter class: **frequency** in brain networks. Combined with existing parameters (scale ε in TDA, error rate p in QEC, coupling strength in dynamics, training epoch in ML, constraint density in CSP), the filtration concept now spans 7 distinct parameter types across 5 domains. The neuroscience frequency-filtration is notable because 3 independent groups discovered it without connecting to the TDA framework.

---

## Wave 10 — link-forge update (2026-04-17)

### Baudot, Tapia, Bennequin & Goaillard (2019) — Topological Information Data Analysis
arXiv: 1907.04242. Information landscape tracks I_k across dimension k. Iso-graining landscapes add second parameter: granularity N, creating 2D (k, N) space with phase transitions at N_c = 3. Full annotation: `inbox.md` (Wave 10a).

### Ghorbanchian et al. (2020) — Higher-order simplicial synchronization
DOI: 10.1038/s42005-021-00605-4. Coupling strength σ parameterizes the system. Explosive synchronization at critical σ_c — discontinuous phase transition. Hysteresis creates bistable region. Width depends on Hodge spectral gap. Full annotation: `inbox.md` (Wave 10a).

### Dey, Mrozek & Slechta (2021) — Conley-Morse graph persistence
arXiv: 2107.02115. Central contribution is parameterized persistence: sequence of multivector fields yields sequence of Conley-Morse graphs. Zigzag persistence tracks both Conley index evolution and Morse decomposition topology across parameter. Composite barcode after redundancy elimination. Full annotation: `inbox.md` (Wave 10a).

### Petri et al. (2014) — Homological scaffolds of brain networks
DOI: 10.1098/rsif.2014.0873. Weight filtration on correlation network creates persistence diagram. Scaffold captures entire persistence history — each edge weighted by persistence of the cycle it participates in. Full annotation: `inbox.md` (Wave 10a).

### Donato et al. (2016) — PH analysis of Phase Transitions
arXiv: 1601.03641. Two-parameter filtration: energy density ε (physical) × Rips scale ρ (topological). H_1 persistence distribution qualitatively changes at critical energy ε_c. Persistence landscapes provide statistical summaries with confidence bands. Full annotation: `inbox.md` (Wave 10b).

### Batko, Mischaikow, Mrozek & Przybylski (2019) — Conley Index from Sampled Dynamics
arXiv: 1904.03757. Binning scale δ as filtration parameter. Authors explicitly acknowledge the connection to persistent homology: understanding results under varying δ "in the spirit of persistent homology." ε-approximation neighborhood also parameterizes a family of continuous maps. Full annotation: `inbox.md` (Wave 10b).

### Lord et al. (2016) — Insights into Brain Architectures from the Homological Scaffolds
DOI: fnsys.2016.00085. Weight threshold on correlation network as filtration parameter. Persistent cycles tracked across weight filtration — scaffold summarizes entire persistence history. Second parameterization: granularity of brain parcellation. Full annotation: `inbox.md` (Wave 10c).

### Méndez & Sánchez-García (2020) — Directed Persistent Homology for Dissimilarity Functions
arXiv: 2008.00711. Directed filtration from asymmetric dissimilarity function. Scale parameter ε determines which directed simplices exist. Tracks directed Betti numbers as ε varies — a new filtration type for non-symmetric data. Full annotation: `inbox.md` (Wave 10c).
