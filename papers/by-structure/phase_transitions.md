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

---

## TDA

*(PH stability theorem — see inbox for Cohen-Steiner)*

## QEC

*(Threshold theorem, exponential error suppression — see inbox for de la Fuente, Dennis)*

## Dynamical Systems

*(Structural stability, surrogate testing — see inbox for Takens, Schreiber)*
