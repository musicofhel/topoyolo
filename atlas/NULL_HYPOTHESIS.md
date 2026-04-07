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

**Papers**: Vejdemo-Johansson & Mukherjee (2018, arXiv: 1812.06491) — first principled statistical framework for PH significance. Universal empirical null distribution for persistent homology with FWER/FDR control via permutation testing. Domain-agnostic: works for any filtration type.

### QEC — Noise Channels
The depolarizing channel destroys coherence while preserving the state space dimension. The noise channel is the null model against which the decoder is benchmarked. Performance below threshold means the code beats the null.

**Papers**: Dennis et al. (2002, arXiv: quant-ph/0110143) — uncorrected noisy evolution as the explicit null; the gap between corrected and uncorrected error rates quantifies the value of error correction. Threshold maps to Z₂ gauge theory: below critical temperature = error correction beats the null. de la Fuente et al. (2025) — phenomenological error model as null. Oreshkov (2013) — uncorrected Lindblad evolution (κ = 0) as null; the gap between corrected and uncorrected quantifies the value of error correction. Hastings & Haah (2021) — static subsystem code with 0 logical qubits as the null for Floquet codes: the dynamical cycling through stabilizer configurations produces logical qubits that the time-independent version lacks. The null is "no time-dependence." Aharonov & Ben-Or (1999) — uncorrected evolution as explicit null; the threshold theorem quantifies how much concatenated correction beats the null (doubly-exponential improvement). Berry et al. (2023) — classical dequantization as null for quantum TDA: if classical algorithms can compute Betti numbers in comparable time, there is no quantum advantage. The null is "classically tractable."

### Dynamical Systems — Shuffled Surrogates
Shuffle temporal order (preserve marginal statistics, destroy temporal dependence). Time-reversed surrogates preserve spectrum but destroy causal direction. AAFT surrogates preserve both marginal distribution and power spectrum.

**Papers**: Theiler et al. (1992) — THE foundational surrogate paper. Three algorithms: (1) random shuffle (destroys all temporal structure, preserves marginal distribution), (2) phase randomization (preserves power spectrum, destroys phase coupling), (3) AAFT (preserves both marginal distribution and power spectrum, destroys nonlinear structure). Establishes the null-hypothesis testing framework that all subsequent surrogate methods build on. Tsuda (2001) — fixed-point or limit-cycle dynamics as the non-itinerant null: if the system converges to a stable attractor rather than wandering between attractor ruins, chaotic itinerancy is rejected. Sugihara et al. (2012) — no-coupling null for convergent cross-mapping: if cross-map correlation fails to converge with library length, the null of independent dynamics is not rejected.

### Information Theory — Product Distributions

1. **Product of marginals** (Belghazi et al., 2018): P_X ⊗ P_Z is the explicit null for MI estimation. MINE samples from both joint and product; the gap is I(X;Y).
2. **Independence at each hierarchy level** (Sugiyama et al., 2016): Lower-order model (e.g., pairwise-only) as null for testing higher-order interactions. The Pythagorean decomposition isolates each level's contribution against its lower-order null.
3. **Random constraint ensemble** (Mézard & Mora, 2008): Random k-SAT instances as null for typical-case complexity. Random structure with controlled density.
4. **Baseline without topological features** (de Jesus Jr. et al., 2025): N-BEATS without TDA inputs as null for forecasting comparison.

### Neuroscience — Trial Shuffling
Shuffle trials to preserve firing rates but destroy inter-trial coupling. Permutation test for functional connectivity. Surrogate distributions for phase-amplitude coupling significance.

### Machine Learning
**Geiger (2021)**: The geometric compression null — representations that cluster/shrink but preserve full MI. Distinguishes information-theoretic compression from geometric compression.

**Shwartz-Ziv & Tishby (2017)**: Random initialization as null — the initial network (before training) has high I(X;T) and low I(T;Y). Training moves the representation away from this null. The compression phase (decreasing I(X;T)) shows the network discarding input noise relative to the random-initialization null.

### Neuroscience — Additional Nulls
**Mediano et al. (2019)**: Independent subsystems as null for PhiID — if brain regions are informationally independent, all cross-region PhiID atoms (transfer, synergy) are zero. Non-zero atoms reject the independence null and quantify the nature of the integration (redundant vs. synergistic vs. transfer).

### Third Pass Additions

**Integer QHE as null** (Arovas-Zhang FQHE): Integer quantum Hall effect has trivial topological order — no anyons, no ground state degeneracy. Fractional states represent genuinely new structure beyond this null.

**Mean-RPE as null** (Dabney distributional code): Schultz mean-RPE model predicts symmetric responses and uniform reversal points. Data decisively rejects this null with asymmetric responses and neuron-specific reversal points.

**Exact analytical null** (Ordinal networks): Adjacency matrices for random (IID) series derived analytically. Principled null without simulation.

**Constant-parameter null** (CP-PINNs): Single PDE with constant parameters. Each detected changepoint rejects this null for a specific time interval.

**Common reference null** (MI-NEE): Uniform distribution as common reference for BOTH joint and marginal. Triangulated comparison rather than direct. Changes convergence properties.

**Maximum entropy null** (Chicharro multivariate redundancy): Max entropy distribution at each decomposition level. Deviation quantifies unexpected structure. Nested hierarchy of nulls — one per tree level.

**Symmetric state as null** (Entropic symmetry breaking): Symmetry = the null. Breaking = departure. Entropy production and information transfer quantify the departure magnitude.

## Key Divergences

- **What is preserved**: Each domain preserves different properties in the null. TDA preserves power spectrum; information theory preserves marginals; QEC preserves state space dimension; dynamics preserves marginal statistics. The null model defines what counts as "structure" vs. "noise" in each domain.
- **Parametric vs. non-parametric**: QEC noise models are parametric (depolarizing channel with known rate). TDA surrogates are non-parametric (phase randomization). Information theory uses both (product distribution is parametric; permutation is non-parametric).
- **Constructive vs. destructive**: In information theory, the null is constructive (build the product distribution). In TDA, the null is destructive (randomize phases to destroy coupling). Same mathematical operation, different conceptual framing.
- **Analytical vs. simulation**: Ordinal networks derive the null EXACTLY for random series. Most other domains require simulation or sampling to generate nulls. This affects statistical power and computational cost.
- **Nested nulls**: Chicharro's tree decomposition has nulls at EVERY level — a hierarchy of null hypotheses. Most other uses are single-level (one null, one test). The nested structure mirrors the chain complex grading.
