# Null Hypothesis

## The Abstract Machine

Destroy specific structure while preserving other properties. Measure the residual. If the residual is significant, the destroyed structure was real; if not, it was noise.

```
Original data X  →  Surrogate X'  →  Compute statistic T(X')
                    (destroy coupling,       (is T(X) >> T(X')?)
                     preserve marginals)
```

The null model defines what "no signal" looks like. The test statistic measures the signal. The gap between T(X) and the null distribution of T(X') is the evidence.

## Where It Appears

### TDA — Surrogate Testing
Phase-randomized surrogates preserve power spectrum but destroy phase coupling. Compute persistence features on original vs. surrogates. The binding residual is significant iff it exceeds the surrogate distribution.

### QEC — Noise Channels
The depolarizing channel destroys coherence while preserving the state space dimension. The noise channel is the null model against which the decoder is benchmarked. Performance below threshold means the code beats the null.

**Papers**: de la Fuente et al. (2025) — phenomenological error model as null. Oreshkov (2013) — uncorrected Lindblad evolution (κ = 0) as null; the gap between corrected and uncorrected quantifies the value of error correction.

### Dynamical Systems — Shuffled Surrogates
Shuffle temporal order (preserve marginal statistics, destroy temporal dependence). Time-reversed surrogates preserve spectrum but destroy causal direction. AAFT surrogates preserve both marginal distribution and power spectrum.

### Information Theory — Product Distributions

1. **Product of marginals** (Belghazi et al., 2018): P_X ⊗ P_Z is the explicit null for MI estimation. MINE samples from both joint and product; the gap is I(X;Y).
2. **Independence at each hierarchy level** (Sugiyama et al., 2016): Lower-order model (e.g., pairwise-only) as null for testing higher-order interactions. The Pythagorean decomposition isolates each level's contribution against its lower-order null.
3. **Random constraint ensemble** (Mézard & Mora, 2008): Random k-SAT instances as null for typical-case complexity. Random structure with controlled density.
4. **Baseline without topological features** (de Jesus Jr. et al., 2025): N-BEATS without TDA inputs as null for forecasting comparison.

### Neuroscience — Trial Shuffling
Shuffle trials to preserve firing rates but destroy inter-trial coupling. Permutation test for functional connectivity. Surrogate distributions for phase-amplitude coupling significance.

### Machine Learning
**Geiger (2021)**: The geometric compression null — representations that cluster/shrink but preserve full MI. Distinguishes information-theoretic compression from geometric compression.

## Key Divergences

- **What is preserved**: Each domain preserves different properties in the null. TDA preserves power spectrum; information theory preserves marginals; QEC preserves state space dimension; dynamics preserves marginal statistics. The null model defines what counts as "structure" vs. "noise" in each domain.
- **Parametric vs. non-parametric**: QEC noise models are parametric (depolarizing channel with known rate). TDA surrogates are non-parametric (phase randomization). Information theory uses both (product distribution is parametric; permutation is non-parametric).
- **Constructive vs. destructive**: In information theory, the null is constructive (build the product distribution). In TDA, the null is destructive (randomize phases to destroy coupling). Same mathematical operation, different conceptual framing.
