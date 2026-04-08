# Stability

## The Abstract Machine

Small perturbation in the input produces bounded change in the output. The form of the bound varies — Lipschitz, exponential suppression, generic — but the claim is the same: the invariant is robust.

```
Input perturbation δ  →  Output change ≤ f(δ)
```

Where f is:
- **Lipschitz**: f(δ) = Cδ (proportional, continuous) — TDA
- **Exponential**: f(δ) = e^{-c/δ} (suppressed, discontinuous threshold) — QEC
- **Generic**: f(δ) = 0 for almost all perturbations (structurally stable) — Dynamics
- **Asymptotic**: f(δ) → 0 as n → ∞ (consistent estimator) — Information Theory

## Where It Appears

### TDA — Persistence Stability Theorem
Bottleneck distance between persistence diagrams ≤ Hausdorff distance between input point clouds (Cohen-Steiner, Edelsbrunner, Harer, 2007, arXiv: math/0604068). THE foundational stability theorem for persistent homology. This is a Lipschitz bound — the diagram changes smoothly with the data.

**Papers**: Bottleneck Degree (Di Rocco et al., 2019) — the reach τ_X controls sample density needed for correct topology recovery; bottleneck degree bounds computational complexity of reach estimation. Adams et al. (2017) — persistence images are W_1 Lipschitz stable: small changes in the persistence diagram (via Wasserstein-1 distance) produce proportionally small changes in the vectorized image. This extends the Cohen-Steiner stability theorem to the featurization step.

### QEC — Threshold Theorem
Below the error threshold, logical error probability is exponentially suppressed in code distance: P_logical ~ (p/p_th)^d. Above threshold, error correction fails. This is a phase transition, not a Lipschitz bound.

**Papers**: Dennis et al. (2002, arXiv: quant-ph/0110143) — threshold theorem for surface codes: below p_th, logical error suppressed exponentially in code distance; maps to phase transition in 3D Z₂ lattice gauge theory (below critical temperature = correctable). de la Fuente et al. (2025) — threshold at ~2.5%, gap to batch decoder (2.9%) quantifies cost of causality. Oreshkov (2013) — CTQEC stability: Markovian regime λ²/κ, Zeno regime λ⁴/κ² (quadratic improvement from non-Markovian noise). Aharonov & Ben-Or (1999) — original concatenated-code threshold theorem: doubly-exponential suppression P_logical ~ (c*p)^{2^L} through L concatenation levels. The first proof that arbitrarily long quantum computation is possible below a constant error rate. Knill, Laflamme & Zurek (1998) — independent threshold proof via Steane code fault-tolerant constructions; different code family, same qualitative result. Breuckmann & Eberhardt (2021) — LDPC codes achieve constant-overhead stability: the ratio of physical to logical qubits stays bounded as code distance grows, a strictly stronger form of QEC stability than the surface code's O(d²) overhead. Hastings & Haah (2021) — threshold theorem for Floquet codes despite time-varying stabilizers; the code maintains stability even though the chain complex structure changes each period.

### Information Theory — Multiple Forms

1. **MINE consistency** (Belghazi et al., 2018): MINE estimate → true MI as sample size → ∞. Lipschitz bound on estimator w.r.t. network parameters.
2. **MI-based regularization** (Jónsson et al., 2020): MI penalty stabilizes test accuracy, reducing variance across training epochs.
3. **Anti-stability** (Chwilka & Karbowski, 2024): MI divergence at finite variance — the invariant can blow up. This is a stability *failure* that marks a phase boundary.
4. **Redundancy stability** (Barrett, 2015): PID redundancy for Gaussian sources is independent of the correlation between sources — a stability result showing that the redundancy atom is robust to perturbations of the source dependence structure.

### Machine Learning — Lipschitz and Generalization Bounds

5. **IB generalization bound** (Kawaguchi et al., 2023): Δ ≤ sqrt(I(X;Z)/n). Same form as PH stability — controlling information content bounds generalization error.
6. **HSIC Lipschitz bounds** (Wang et al., 2021): Layer-wise HSIC controls per-layer Lipschitz constant. Proves HSIC bottleneck implies adversarial robustness.
7. **SNGP distance awareness** (Liu et al., 2020): Spectral normalization enforces bi-Lipschitz property. Identical mathematical structure to PH stability: ||h(x)-h(x')|| ≤ L||x-x'||.

### Dynamical Systems — Structural Stability
A dynamical system is structurally stable if small perturbations of the vector field produce topologically conjugate flows. Generic systems (Morse-Smale) are structurally stable. Bifurcation points are where structural stability fails — the analogue of error thresholds.

**Papers**: Takens (1981) — C² genericity of the delay embedding: for a generic (residual set) pair of observable and delay, the embedding is a diffeomorphism on the attractor. This is stability in the topological sense — the property holds for "almost all" choices, and small perturbations of the observable don't break it. Sauer, Yorke & Casdagli (1991) — prevalence, strictly stronger than Takens' genericity: the set of observables yielding correct embeddings has full measure (not just residual). Prevalence is the measure-theoretic analogue of genericity, closing the gap between "topologically generic" and "probability-one." Theiler (1992) — preserved quantities (integrals of motion, Lyapunov exponents, correlation dimension) as stability invariants: these quantities are robust to measurement noise and serve as the dynamical systems analogue of persistent homology features. Tsuda (2001) — ghost stability (6th flavor): the system visits ruins of destroyed attractors, spending long times near each before transitioning. The attractor is unstable but its ghost persists as a quasi-stable structure, a weaker form of stability than structural but stronger than none.

**Banach contraction** (Gallicchio & Micheli, 2020): spectral radius ρ(W) < 1 guarantees fixed-point convergence for reservoir GNNs. Directly analogous to QEC correction rate exceeding noise rate.

**Hawkes stationarity** (Huang et al., 2022): spectral radius of excitation matrix < 1 ensures bounded long-run intensity.

### QEC (extended)
**No partial erasure** (Pati & Sanders, 2005): The strongest stability theorem — absolute impossibility, not a bound. Topological dimension of quantum state space is invariant under ALL physical operations.

### Statistical Physics
Mézard & Mora (2008): BP convergence regimes. In the easy-SAT regime (α < α_d), the BP fixed point is stable. In the hard-SAT regime (α_d < α < α_c), BP oscillates but Survey Propagation works. Above α_c, all algorithms fail. Each transition marks a change in algorithmic stability.

### Third Pass Additions

**Topological protection** (Arovas-Zhang FQHE): Energy gap renders topological invariants immune to perturbations smaller than the gap. Strongest continuous stability: no change at all (not just bounded change).

**Anti-stability** (Spin-Boson Born): sqrt(alpha) prompt coherence loss at weak coupling. The standard linear-in-alpha estimate is wrong — decoherence is WORSE than expected. This is a new stability category: the bound itself is wrong, not just violated.

**Distribution-free stability** (ConformalHDC): Conformal prediction guarantees hold for ANY data distribution. Coverage guarantee adapts (prediction set grows/shrinks) but never fails. No distributional assumptions required.

**Exact isomorphism** (Barandes stochastic-quantum): The correspondence is exact, not a bound. Every stochastic system has a unique quantum counterpart. The strongest possible stability — the map is an isomorphism.

**Orthogonal projection stability** (HSIC-Bottleneck): Gradient updates constrained to orthogonal complement of important subspace. Structurally identical to Hodge decomposition: harmonic component preserved, gradient/curl components modified.

**Ergodic convergence** (Fuchsian groups): Time averages converge to space averages a.e. Measurement robust to starting point.

**Spectral Wasserstein metric equivalence** (Peyré 2026): √c_γ · W2 ≤ W_γ ≤ √C_γ · W2 for all monotone norms γ. The entire parameterized family of Spectral Wasserstein distances is metrically equivalent to W2 — topology-preserving stability across the Schatten interpolation. Geodesic convexity gives a second form: interpolations in the geometry don't create pathological states.

**Dimensional phase transition** (Wang 2026): Grokking = stability boundary crossing. Effective dimensionality D crosses from sub-diffusive (D ≈ 0.90, stable/confined cascades) through D = 1 to super-diffusive (D ≈ 1.20, amplifying cascades). Three non-overlapping bootstrap distributions validate: D_pre = 0.90 ± 0.02, D_post = 1.20 ± 0.02, D_synth = 0.99 ± 0.01. This is a 7th flavor of stability: **dimensional** — the stability boundary is defined by whether gradient perturbations are confined (D < 1) or amplify (D > 1), measured by finite-size scaling across system sizes.

The stability taxonomy now has **7 flavors**: (1) Lipschitz (TDA, Adams persistence images), (2) exponential suppression (QEC threshold, Aharonov-Ben-Or concatenation), (3) topological protection (FQHE gap), (4) anti-stability (spin-boson sqrt singularity), (5) distribution-free (conformal prediction), (6) ghost stability (Tsuda chaotic itinerancy — quasi-stable visits to destroyed attractor ruins), (7) dimensional (Wang grokking — sub-/super-diffusive phase transition at D = 1).

## Key Divergences

- **Lipschitz vs. exponential vs. topological vs. distribution-free**: The mathematical form of the guarantee differs across domains. See ANTISYNONYMS.md.
- **Anti-stability is not instability**: Spin-boson anti-stability means the bound's functional form is wrong (sqrt not linear). The system may still be bounded — just worse than predicted. This differs from dynamical instability (positive Lyapunov) and topological instability (feature death).
- **Continuous vs. discontinuous**: TDA stability is continuous (small input change → small output change). QEC threshold is discontinuous (below threshold → exponentially good; above → failure). The information-theory case has both (MINE is continuous; MI divergence is discontinuous).
