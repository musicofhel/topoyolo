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
Bottleneck distance between persistence diagrams ≤ Hausdorff distance between input point clouds (Cohen-Steiner, Edelsbrunner, Harer, 2007 — in inbox). This is a Lipschitz bound — the diagram changes smoothly with the data.

**Papers**: Bottleneck Degree (Di Rocco et al., 2019) — the reach τ_X controls sample density needed for correct topology recovery; bottleneck degree bounds computational complexity of reach estimation.

### QEC — Threshold Theorem
Below the error threshold, logical error probability is exponentially suppressed in code distance: P_logical ~ (p/p_th)^d. Above threshold, error correction fails. This is a phase transition, not a Lipschitz bound.

**Papers**: de la Fuente et al. (2025) — threshold at ~2.5%, gap to batch decoder (2.9%) quantifies cost of causality. Oreshkov (2013) — CTQEC stability: Markovian regime λ²/κ, Zeno regime λ⁴/κ² (quadratic improvement from non-Markovian noise).

### Information Theory — Multiple Forms

1. **MINE consistency** (Belghazi et al., 2018): MINE estimate → true MI as sample size → ∞. Lipschitz bound on estimator w.r.t. network parameters.
2. **MI-based regularization** (Jónsson et al., 2020): MI penalty stabilizes test accuracy, reducing variance across training epochs.
3. **Anti-stability** (Chwilka & Karbowski, 2024): MI divergence at finite variance — the invariant can blow up. This is a stability *failure* that marks a phase boundary.

### Dynamical Systems — Structural Stability
A dynamical system is structurally stable if small perturbations of the vector field produce topologically conjugate flows. Generic systems (Morse-Smale) are structurally stable. Bifurcation points are where structural stability fails — the analogue of error thresholds.

4. **IB generalization bound** (Kawaguchi et al., 2023): Δ ≤ sqrt(I(X;Z)/n). Same form as PH stability — controlling information content bounds generalization error.
5. **HSIC Lipschitz bounds** (Wang et al., 2021): Layer-wise HSIC controls per-layer Lipschitz constant. Proves HSIC bottleneck implies adversarial robustness.
6. **SNGP distance awareness** (Liu et al., 2020): Spectral normalization enforces bi-Lipschitz property. Identical mathematical structure to PH stability: ||h(x)-h(x')|| ≤ L||x-x'||.

### Dynamical Systems — Structural Stability (extended)
A dynamical system is structurally stable if small perturbations of the vector field produce topologically conjugate flows. Generic systems (Morse-Smale) are structurally stable. Bifurcation points are where structural stability fails — the analogue of error thresholds.

**Banach contraction** (Gallicchio & Micheli, 2020): spectral radius ρ(W) < 1 guarantees fixed-point convergence for reservoir GNNs. Directly analogous to QEC correction rate exceeding noise rate.

**Hawkes stationarity** (Huang et al., 2022): spectral radius of excitation matrix < 1 ensures bounded long-run intensity.

### QEC (extended)
**No partial erasure** (Pati & Sanders, 2005): The strongest stability theorem — absolute impossibility, not a bound. Topological dimension of quantum state space is invariant under ALL physical operations.

### Statistical Physics
Mézard & Mora (2008): BP convergence regimes. In the easy-SAT regime (α < α_d), the BP fixed point is stable. In the hard-SAT regime (α_d < α < α_c), BP oscillates but Survey Propagation works. Above α_c, all algorithms fail. Each transition marks a change in algorithmic stability.

## Key Divergences

- **Lipschitz vs. exponential vs. generic**: The mathematical form of the guarantee differs across domains, even though the conceptual claim is similar. See ANTISYNONYMS.md.
- **Continuous vs. discontinuous**: TDA stability is continuous (small input change → small output change). QEC threshold is discontinuous (below threshold → exponentially good; above → failure). The information-theory case has both (MINE is continuous; MI divergence is discontinuous).
