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

## Statistical Physics

### Mézard & Mora (2008) — Constraint Satisfaction
Parameter: constraint density α = M/N. Invariant: solution space topology. Phase transitions at α_d (BP fails) and α_c ≈ 4.267 (SAT/UNSAT). Solution cluster shattering. Full annotation: `by-domain/information_theory.md`.

---

## TDA

### Mollers, Immer, Fortuin, Isufi (2023) — Hodge-Aware Contrastive Learning
Parameter: SCNN filter coefficients. Invariant: Hodge component proportions (gradient, curl, harmonic). The learned representations are parameterized by spectral weights on the three Hodge subspaces. The harmonic space ker(L_1) IS the first homology — the Hodge theorem made computational. Full annotation: `by-domain/tda.md`.

### de Jesus Jr., Fernandez-Navarro, Carbonero-Ruz (2025) — TDA for Financial Forecasting
Parameter: sliding window position (time) and Vietoris-Rips scale (epsilon). Invariant: persistent entropy, amplitude, point count from persistence diagrams. Sliding-window PH on time-delay embedded financial time series. First application of TDA-derived features specifically for forecasting (vs. classification/detection). Tested on 32 datasets across crypto and traditional instruments. Full annotation: `by-domain/tda.md`.

### Di Rocco, Eklund, Weinstein (2019) — Bottleneck Degree of Algebraic Varieties
Parameter: scale at which topology is probed. Invariant: reach tau_X = min(rho, b). The reach determines the sample density needed for persistent homology to recover correct topology. Bottleneck degree bounds the number of critical parameter values where topology might change. Formula in terms of Chern classes and polar classes. Full annotation: `by-domain/tda.md`.

### Kanjamapornkul, Pincak, Bartos (2020) — Cohomology Theory for Financial Time Series
Parameter: Wilson loop parameter (trader interaction strength). Invariant: cohomological classification (8 market states, 16 physiological cones). Market phase transitions parameterized by Yang-Mills field coupling. Full annotation: `by-domain/tda.md`.

*(See also inbox for Cohen-Steiner stability, Bauer/Ripser, Adams persistence images)*

## QEC

### Oreshkov (2013) — Continuous-time quantum error correction
Parameter: ratio kappa/lambda (error correction rate / decoherence rate). Invariant: protected quantum information (fidelity). Regimes: kappa >> lambda (Zeno, information frozen), kappa ~ lambda (partial protection), kappa << lambda (information lost). Non-Markovian regime shows quadratic improvement (lambda^4/kappa^2 vs. lambda^2/kappa). Full annotation: `by-domain/qec.md`.

*(See also inbox for de la Fuente error threshold at ~2.5%)*

## Dynamical Systems

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
