# Neuroscience

Papers from or relevant to the neuroscience community, indexed by which abstract machines they instantiate. Cross-references to `by-structure/` files are given per paper.

---

## Cross-listed from Information Theory

- **Mézard & Mora (2008)** — "Constraint satisfaction problems and neural networks: a statistical physics perspective." Proposes message-passing algorithm for inferring neural interactions from multi-electrode recordings. Full annotation in `by-domain/information_theory.md`. Machines: chain complex, parameterized homology, matching, stability, null hypothesis.

- **Tax, Mediano & Shanahan (2017)** — "The Partial Information Decomposition of Generative Neural Network Models." PID applied to RBM training dynamics: redundancy-then-specialization. Full annotation in `by-domain/information_theory.md`. Machines: joint-vs-marginal, parameterized homology, null hypothesis.

- **Chwilka & Karbowski (2024)** — "Explicit mutual information for simple networks and neurons with lognormal activities." Closed-form MI for lognormal neural firing rates; MI divergence at finite variance. Full annotation in `by-domain/information_theory.md`. Machines: joint-vs-marginal, stability (anti-stability).

- **Zhang, Simeone, Cvetkovic, Abela, Richardson (2020)** — "ITENE: Intrinsic Transfer Entropy Neural Estimator." Neural estimator for intrinsic (non-synergistic) directional information flow; motivated by neural and gene-regulatory networks. Full annotation in `by-domain/information_theory.md`. Machines: joint-vs-marginal, matching, null hypothesis.

- **Zhou, Xiao, Zhang, Xu, Cai (2014)** — "Granger Causality Network Reconstruction of Conductance-Based Integrate-and-Fire Neuronal Systems." Establishes quantitative mapping GC ∝ S² between functional (GC) and structural (synaptic) connectivity in I&F networks. Reconstruction works from voltage traces and spike rasters, insensitive to dynamical regime. Full annotation in `by-domain/information_theory.md`. Machines: joint-vs-marginal, stability, null hypothesis, parameterized homology.

- **Wibral, Finn, Wollstadt, Lizier, Priesemann (2017)** — "Quantifying Information Modification in Developing Neural Networks via Partial Information Decomposition." PID applied to developing neural cultures: synergy (information modification) rises during maturation then collapses as redundancy dominates. Full annotation in `by-domain/information_theory.md`. Machines: joint-vs-marginal, null hypothesis, parameterized homology.

- **Venkatesh, Dutta, Mehta, Grover (2021)** — "Can Information Flows Suggest Targets for Interventions in Neural Circuits?" M-information flow to identify intervention targets; fairness-in-ML as analogy for deep-brain stimulation. Full annotation in `by-domain/information_theory.md`. Machines: joint-vs-marginal, null hypothesis, matching.

---

## Papers to annotate (in inbox)

- **Giusti, Curto et al. (2015)** — "Clique topology reveals intrinsic geometric structure in neural correlations." Chain complex (clique complex on correlations), parameterized homology.
- **Gardner et al. (2022)** — "Toroidal topology of population activity in grid cells." Chain complex (the torus IS the neural manifold).
- **Xi et al.** — "TE + directed PH in spiking systems." Chain complex, parameterized homology, null model.
- **Tsuda (2001)** — "Chaotic itinerancy." Parameterized homology (attractor switching = topology change over time).
- **Tort et al. (2010)** — PAC modulation index. Joint-vs-marginal (cross-frequency coupling), null model.

---

## Cross-listed from Second Pass + Bridges

- **Simpson, Bowman, Laurienti (2013)** — "Analyzing complex functional brain networks." Survey identifying exact gaps where TDA machines apply: threshold selection = filtration problem, higher-order structure needs simplicial methods. Full annotation: `second_pass.md` (SP-15). Machines: chain complex (weak), parameterized homology, joint-vs-marginal, null hypothesis.

- **Fasoli et al. (2026)** — "Attractor dynamics of whole-cortex network model." Mouse cortex: directed connectivity essential for full attractor repertoire (Z vs Z/2 homology). Static fMRI constraints determine dynamic topology. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, stability, null hypothesis, joint-vs-marginal. **Bridge: neuroscience + dynamical systems.**

- **Tort et al. (2010)** — PAC modulation index. *(In inbox — not yet annotated.)*

---

## Third Pass (2026-04-05)

### IPWT — Integrated Predictive Workspace Theory
**Domain(s)**: Neuroscience (consciousness), information theory
Fuses IIT + Predictive Coding + Global Workspace via synergistic information. Synergy IS joint-vs-marginal excess: the whole-system information exceeds the sum of subsystem information. Replaces IIT's controversial "physical indivisibility" with computationally tractable synergistic information. Predicts clinical conditions (schizophrenia, DID) as specific perturbation regimes.
**Machines**: joint-vs-marginal, parameterized homology, null hypothesis, stability.
Full annotation: `third_pass_neuro_qec.md` (TP-01).
**See also**: `by-structure/composite_systems.md`

### Neurophenomenology via Free Energy (arXiv: 2409.20318)
**Domain(s)**: Neuroscience, dynamical systems (active inference)
Formalizes Varela's neurophenomenology via free energy principle. First-person beliefs and third-person neural measurements are two marginals; free energy measures the divergence. The explanatory gap IS the joint-vs-marginal excess yet to be accounted for.
**Machines**: joint-vs-marginal, parameterized homology, stability, null hypothesis.
Full annotation: `third_pass_neuro_qec.md` (TP-02).

### Dabney et al. (2020) — Distributional Code for Value (Nature)
**Domain(s)**: Neuroscience (computational), information theory
Dopamine neurons encode quantiles of the full reward distribution, not just the mean. The quantile index tau parameterizes the neuron family. Population jointly encodes the entire distribution; no single neuron's marginal contains it. Schultz mean-RPE model is the explicit null.
**Machines**: joint-vs-marginal, parameterized homology, null hypothesis, stability.
Full annotation: `third_pass_neuro_qec.md` (TP-03).
**See also**: `by-structure/composite_systems.md`, `by-structure/filtrations.md`

### Opponent Striatal Circuit (bioRxiv 2024)
**Domain(s)**: Neuroscience (experimental)
D1/D2 neurons encode opposite tails of reward distribution. Neither population alone captures the distribution; the full representation requires the joint opponent encoding. D1 encodes optimistic quantiles, D2 encodes pessimistic. Optogenetic manipulation provides causal evidence.
**Machines**: joint-vs-marginal, matching, chain complex (weak), null hypothesis.
Full annotation: `third_pass_neuro_qec.md` (TP-04).

### ConformalHDC — Hippocampal Decoding (arXiv: 2602.21446)
**Domain(s)**: Neuroscience (decoding), machine learning
Conformal prediction + hyperdimensional computing for hippocampal place cell decoding. Non-conformity score as null-hypothesis test statistic, coverage guarantee as stability bound. Decodes FROM the same toroidal manifold that Gardner et al. showed IS a torus.
**Machines**: null hypothesis, stability, matching, joint-vs-marginal (weak).
Full annotation: `third_pass_neuro_qec.md` (TP-09).

### Summary Statistics Link Neural Representations to Behavior (arXiv: 2504.16920)
**Domain(s)**: Neuroscience (computational), dynamical systems, information theory
Meta-review: summary statistics from statistical physics (order parameters, susceptibilities) track how neural representations change during learning. The tracked statistics are conserved across individuals, species, and artificial networks — stable invariants of the learning process.
**Machines**: parameterized homology, joint-vs-marginal, null hypothesis, stability.
Full annotation: `third_pass_neuro_qec.md` (TP-11).

### FitzHugh-Nagumo Wave Patterns (DOI: 10.1142/s021797922450200x)
**Domain(s)**: Dynamical systems, neuroscience
FHN neural network under varying light illumination and magnetic flux — two-parameter space of pattern formation. Modulational instability analysis determines where small perturbations grow or decay. Uniform plane wave is the null; pattern formation is departure from null.
**Machines**: parameterized homology, stability, null hypothesis.
Full annotation: `third_pass_dynamics_tda.md` (TP-09).

### IC-PINN Coupled Oscillators — Embryonic Clocks
**Domain(s)**: Dynamical systems, neuroscience
Physics-informed neural networks for basis-free inference of coupling functions between oscillators. Applied to embryonic segmentation clocks (somitogenesis) and spinning nanorods. Coupling function defined on the torus T².
**Machines**: parameterized homology, matching, stability.
Full annotation: `third_pass_dynamics_tda.md` (TP-11).

### GC-STCL — EEG Emotion Recognition (Wang et al. 2024)
**Domain(s)**: Neuroscience (EEG), information theory
Granger causality graph + contrastive learning for EEG emotion recognition. Frequency-band-specific causal networks as filtration. GC graph reveals directed temporal dependencies absent from individual channel statistics.
**Machines**: joint-vs-marginal, chain complex (weak), null hypothesis, parameterized homology.
Full annotation: `third_pass_infotheo_cross.md` (TP-01).

### Driver Fatigue via Granger Causality Network (Kong et al. 2015)
**Domain(s)**: Neuroscience (EEG), information theory
GC network topology distinguishes alert from drowsy states. Frequency-band-specific causal networks: different causal structures across alpha, theta, gamma. Alert state as baseline null.
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology, matching.
Full annotation: `third_pass_infotheo_cross.md` (TP-05).

### Nonparametric Granger Causality in Brain (Ding et al. 2009, PMC 2685256)
**Domain(s)**: Neuroscience, information theory
Nonparametric spectral Granger causality — no autoregressive model fitting. Frequency parameter defines continuous family of causal graphs. Applied to monkey sensorimotor cortex.
**Machines**: joint-vs-marginal, parameterized homology, null hypothesis, stability.
Full annotation: `third_pass_infotheo_cross.md` (TP-06).
