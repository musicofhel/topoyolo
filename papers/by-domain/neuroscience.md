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

## Chain Complex (annotated from inbox — Wave 1)

- **Giusti, Pastalkova, Curto, Itskov (2015)** — "Clique topology reveals intrinsic geometric structure in neural correlations." Order complex from hippocampal correlation matrices. Rank-ordering invariance under monotone transforms. Detects geometry invisible to spectral methods. Full annotation: `inbox.md` (arXiv: 1502.06172). Machines: chain complex, parameterized homology, null hypothesis. **See also**: `by-structure/boundary_operators.md`.

- **Reimann, Nolte, Scolamiero, Turner et al. (2017)** — "Cliques of Neurons Bound into Cavities Provide a Missing Link between Structure and Function." Directed simplicial complexes from Blue Brain reconstruction (~31K neurons). Directed simplices up to dim 6-7. Stimulus-evoked hierarchical cavity formation. Full annotation: `inbox.md` (DOI: 10.3389/fncom.2017.00048). Machines: chain complex, parameterized homology, null hypothesis. **See also**: `by-structure/boundary_operators.md`.

- **Dabaghian, Mémoli, Frank, Carlsson (2012)** — "A Topological Paradigm for Hippocampal Spatial Map Formation Using Persistent Homology." Nerve complex from place cell co-firing. PH recovers environment topology in 2-5 min. Learning region in parameter space. Full annotation: `inbox.md` (DOI: 10.1371/journal.pcbi.1002581). Machines: chain complex, parameterized homology, stability. **See also**: `by-structure/boundary_operators.md`.

- **Curto & Itskov (2008)** — "Cell Groups Reveal Structure of Stimulus Space." Nerve of receptive field cover. Nerve Theorem guarantees H_* of complex = H_* of stimulus space. Geometric reconstruction ~3% accuracy. Full annotation: `inbox.md` (DOI: 10.1371/journal.pcbi.1000205). Machines: chain complex, matching, stability. **See also**: `by-structure/boundary_operators.md`.

## Wave 4c (2026-04-06) — Inbox Annotations

- **Tort, Komorowski, Eichenbaum, Kopell (2010)** — "Measuring Phase-Amplitude Coupling Between Neuronal Oscillations of Different Frequencies." Modulation Index = D_KL(observed PAC distribution || uniform). Joint-vs-marginal excess quantifies cross-frequency coupling. Time-shifted surrogates as null. Full annotation: `inbox.md`. Machines: joint-vs-marginal, null hypothesis, parameterized homology (weak). **See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`.

### Oizumi, Albantakis, Tononi (2014) — Integrated Information Theory 3.0
**"From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0"**
DOI: 10.1371/journal.pcbi.1003588
THE foundational formalization of joint-vs-marginal excess in neuroscience. Φ = D(p(X^t|X^{t-1}) || Π_i p(X_i^t|X_i^{t-1})). Partitioned system as null. MICS = maximally irreducible conceptual structure specifying quality of experience. Exclusion postulate selects spatiotemporal grain maximizing Φ.
**Machines**: joint-vs-marginal, null hypothesis, stability, parameterized homology. **See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`.

## Annotated papers (full annotations in inbox)

- **Gardner et al. (2022)** — "Toroidal topology of population activity in grid cells." PH on Neuropixels grid cell recordings reveals toroidal manifold T². Five machines: chain complex (T² with H₁=Z²), parameterized homology (PH across filtration), stability (persists across environments and wake→sleep), null hypothesis (feedforward models falsified), joint-vs-marginal (torus is population-level, invisible from marginals). Full annotation: `inbox.md` (DOI: 10.1038/s41586-021-04268-7). **See also**: `by-structure/boundary_operators.md`, `cross_domain_bridges.md` (neuro ↔ QEC via shared T²).
- **Peek, Pritam, Skerritt, Chalup (2025)** — "Time Series Analysis of Spiking Neural Systems via Transfer Entropy and Directed Persistent Homology." TE+PH pipeline: spike trains -> pairwise TE -> directed flag complex -> directed PH. Applied to synthetic SNNs (logic gates, image classification) and mouse cortical recordings. Higher-dimensional homology discriminates task complexity. Wasserstein distances on PDs recover graded task space geometry. Triple-domain bridge: neuroscience + TDA + information theory. Full annotation: `inbox.md` (arXiv: 2508.19048). Machines: chain complex (directed flag complex from TE graph), parameterized homology (inverted TE filtration), null hypothesis (baseline epochs, simple tasks as reference). **See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-domain/tda.md`, `by-domain/information_theory.md`.
- **Tsuda (2001)** — "Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems." Chaotic itinerancy: trajectory wanders among attractor ruins, tracing a path through topology space parameterized by time. Quasi-stability via destroyed attractors (Milnor attractors). Fixed-point/limit-cycle as null. Full annotation: `inbox.md` (DOI: 10.1017/S0140525X01000097). Machines: parameterized homology, stability (anti-stability), null hypothesis, chain complex (weak). **See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`.

---

## Cross-listed from Second Pass + Bridges

- **Simpson, Bowman, Laurienti (2013)** — "Analyzing complex functional brain networks." Survey identifying exact gaps where TDA machines apply: threshold selection = filtration problem, higher-order structure needs simplicial methods. Full annotation: `second_pass.md` (SP-15). Machines: chain complex (weak), parameterized homology, joint-vs-marginal, null hypothesis.

- **Fasoli et al. (2026)** — "Attractor dynamics of whole-cortex network model." Mouse cortex: directed connectivity essential for full attractor repertoire (Z vs Z/2 homology). Static fMRI constraints determine dynamic topology. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, stability, null hypothesis, joint-vs-marginal. **Bridge: neuroscience + dynamical systems.**

- **Tort et al. (2010)** — PAC modulation index. *(Fully annotated in inbox.md — see Wave 4c above.)*

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

---

## Wave 5 — Matching (Optimal Transport) in Neuroscience (2026-04-06)

Papers filling the Match x Neuro cell: genuine optimal transport / matching applied to neural data.

### Thual, Tran, Zemskova, Courty, Flamary, Dehaene, Thirion (2022) — FUGW Brain Alignment
**"Aligning individual brains with Fused Unbalanced Gromov-Wasserstein"** (NeurIPS 2022, arXiv: 2206.09398)
Fused Unbalanced Gromov-Wasserstein computes optimal transport plans between cortical surfaces of different subjects. Combines feature-based Wasserstein matching with geometry-preserving Gromov-Wasserstein, with unbalanced marginals to handle inter-subject area size differences. Applied to whole-brain fMRI alignment on the Individual Brain Charting dataset (12 subjects, 400 maps each). Outperforms FreeSurfer and MSM baselines. 46 citations.
**Machines**: matching, stability, parameterized homology, null hypothesis.
Full annotation: `inbox.md` (Wave 5).
**See also**: `by-structure/optimal_transport.md`

### Janati, Bazeille, Thirion, Cuturi, Gramfort (2019) — Minimum Wasserstein Estimates
**"Group level MEG/EEG source imaging via optimal transport: minimum Wasserstein estimates"** (arXiv: 1902.04812)
Unbalanced OT as regularizer for multi-subject MEG/EEG source localization. Wasserstein barycenter defines group-level source estimate respecting cortical geometry. Cost matrix = geodesic distance on cortical mesh. Reduces localization error from ~4 cm (Lasso) to <1 cm. Validated on Wakeman-Henson face perception data; localizes fusiform face area consistent with fMRI.
**Machines**: matching, stability, null hypothesis, parameterized homology.
Full annotation: `inbox.md` (Wave 5).
**See also**: `by-structure/optimal_transport.md`

### Lee, Dabagia, Dyer, Rozell (2019) — Hierarchical OT for Neural Decoding
**"Hierarchical Optimal Transport for Multimodal Distribution Alignment"** (NeurIPS 2019, arXiv: 1906.11768)
Two-level OT: coarse cluster matching + fine within-cluster alignment. Applied to neural population decoding in macaque primary motor cortex (M1): aligns firing patterns across recording sessions to enable cross-session movement direction/velocity decoding. Exploits clustered structure in neural population activity. Distributed ADMM + Sinkhorn. 78 citations.
**Machines**: matching, stability, parameterized homology, null hypothesis.
Full annotation: `inbox.md` (Wave 5).
**See also**: `by-structure/optimal_transport.md`

---

## Joint x Neuro — Consciousness / Information Dynamics (Wave 5)

### Mediano, Rosas, Carhart-Harris, Seth, Barrett (2019) — PhiID
**"Beyond integrated information: A taxonomy of information dynamics phenomena"**
arXiv: 1909.02297
**Domain(s)**: Neuroscience (consciousness), information theory
PhiID = Integrated Information Decomposition. Combines PID with IIT to decompose excess entropy into 16 atoms on a double-redundancy (product) lattice. Reveals that "integration" is actually an aggregate of storage, copy, transfer, erasure, upward causation, and downward causation — six qualitatively distinct modes of joint-vs-marginal excess. Shows existing Phi measures (Phi_WMS, psi, Phi_G, CD) each capture different subsets of atoms. Motivated by consciousness research: understanding WHAT KIND of integration the brain performs, not just HOW MUCH.
**Machines**: joint-vs-marginal, chain complex (product lattice + Moebius inversion), parameterized homology, null hypothesis, stability.
Full annotation: `inbox.md` (arXiv: 1909.02297).
**See also**: `by-structure/composite_systems.md`

### Barrett (2015) — PID for Gaussian Systems
**"Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems"**
arXiv: 1411.2832
**Domain(s)**: Information theory, neuroscience
First systematic PID analysis for continuous (Gaussian) variables. Key result: for univariate target, broad class of PIDs collapse to MMI (redundancy = min of individual MIs). Synergy prevalent even when sources are uncorrelated. Applied to MVAR dynamical systems: synergy decreases with lag depth, increases with weaker connection strength, decreases with source correlation. Discusses neuroscience applications: neural coding, EEG connectivity, epilepsy, consciousness.
**Machines**: joint-vs-marginal, parameterized homology, null hypothesis, stability.
Full annotation: `inbox.md` (arXiv: 1411.2832).
**See also**: `by-structure/composite_systems.md`

---

## Wave 6 — Directed Information Flow in Neural Oscillations and Spike Trains (2026-04-07)

### Lobier, Siebenhuhner, Palva, Palva (2014) — Phase Transfer Entropy
**"Phase transfer entropy: A novel phase-based measure for directed connectivity in networks coupled by oscillatory interactions"**
DOI: 10.1016/j.neuroimage.2013.08.056, NeuroImage 85(2):853-872. 281 citations.
**Domain(s)**: Neuroscience, information theory
Phase TE computes transfer entropy on Morlet-filtered phase time series, isolating directed oscillatory coupling from amplitude effects. Differential TE (dTE) quantifies net directionality. Robust to linear mixing (volume conduction) and noise at realistic MEG/EEG levels. Frequency-band-specific: different bands yield different directed coupling graphs. Validated on coupled Neural Mass Models. Computationally much faster than real-valued TE.
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology.
Full annotation: `inbox.md` (Wave 6).
**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`, `by-domain/information_theory.md`

### Rosas, Mediano et al. (2020) — Causal Emergence via PID
**"Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data"**
PLoS Computational Biology, 16(12), e1008289. arXiv: 2004.08220. 143 citations.
**Domain(s)**: Information theory, neuroscience, dynamical systems
Inverted joint-vs-marginal: macro coarse-grained feature has causal power exceeding sum of micro parts. Applied to 64-channel macaque ECoG during reaching: Ψ^(1) = 1.275 > 0 at 8ms timescale, motor representation emergent up to ~0.2s. Emergence decomposes into downward causation D^(k) and causal decoupling G^(k) ("statistical ghosts"). Extends Mediano PhiID.
**Machines**: joint-vs-marginal (inverted), parameterized homology, null hypothesis, chain complex (inherited).
Full annotation: `inbox.md` (Wave 7).
**See also**: `by-structure/composite_systems.md`, `by-domain/information_theory.md`, `atlas/JOINT_VS_MARGINAL.md`

### Shorten, Spinney, Lizier (2021) — Continuous-Time Transfer Entropy for Spike Trains
**"Estimating Transfer Entropy in Continuous Time Between Neural Spike Trains or Other Event-Based Data"**
DOI: 10.1371/journal.pcbi.1008054, PLOS Computational Biology 17(4):e1008054. 58 citations.
**Domain(s)**: Information theory, neuroscience
Continuous-time TE via Radon-Nikodym derivatives on path space, estimated with kNN in inter-event-interval embedding. Provably consistent (unlike discrete-time plug-in estimators which converge to wrong value). Local permutation surrogates for correct null hypothesis testing on point processes (source-time-shift surrogates shown to fail). Captures relationships at both fine and coarse timescales simultaneously. Validated on pyloric circuit (stomatogastric ganglion) where previous estimators failed.
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology.
Full annotation: `inbox.md` (Wave 6).
**See also**: `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`, `by-domain/information_theory.md`

### Varley, Mediano, Patania & Bongard (2025) — The Topology of Synergy
**"The topology of synergy: Linking topological and information-theoretic approaches to higher-order interactions in complex systems"**
PLoS Computational Biology, DOI: 10.1371/journal.pcbi.1013649. arXiv: 2504.10140. 4 citations.
**Domain(s)**: TDA, information theory, neuroscience
Applied to HCP resting-state fMRI (200-node Schaefer parcellation, 100 subjects). 1,313,400 triads tested; 30,100 significantly redundant, 6,200 significantly synergistic (circular-shift null). H2 persistent homology features (3D cavities) correlate with synergistic information: avg persistence vs normalized O-bar rho = -0.55 to -0.65. PCA fails to preserve synergy or topology: most synergistic triads look random to PCA (PC1 variance near 33%). Neural manifold learning systematically misses synergistic structure.
**Machines**: chain complex, parameterized homology, joint-vs-marginal, null hypothesis, stability.
Full annotation: `inbox.md` (Wave 7).
**See also**: `cross_domain_bridges.md`, `by-domain/tda.md`, `by-domain/information_theory.md`, `by-structure/composite_systems.md`, `by-structure/filtrations.md`

---

## Wave 10 — link-forge update (2026-04-17)

### Petri, Expert, Turkheimer, Carhart-Harris, Nutt, Hellyer & Vaccarino (2014) — Homological scaffolds
J. R. Soc. Interface, DOI: 10.1098/rsif.2014.0873. 657 citations. PH applied to weighted clique complex from fMRI correlations. Homological scaffold = network encoding which edges carry persistent cycles. Psilocybin dramatically restructures scaffold: many transient + few highly persistent structures not seen under placebo. Bridges TDA and network neuroscience.
**Machines**: chain complex, parameterized homology, null hypothesis.
Full annotation: `inbox.md` (Wave 10a).
**See also**: `by-domain/tda.md`, `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-structure/phase_transitions.md`, `papers/cross_domain_bridges.md`

### Chaudhuri, Gerçek, Pandey, Peyrache & Fiete (2019) — Head direction ring attractor
Nature Neuroscience, DOI: 10.1038/s41593-019-0460-x. 339 citations. Head direction circuit population activity traces S^1 ring manifold (H_1 = ℤ). Isometric and invariant across waking and REM sleep. Blind decoding from topology alone. Ring is population-level (absent from individual neurons). Complements Gardner 2022 T^2 grid cell toroid.
**Machines**: chain complex, stability, joint-vs-marginal.
Full annotation: `inbox.md` (Wave 10a).
**See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`, `by-structure/composite_systems.md`

### Chung, El-Yaagoubi, Qiu & Ombao (2025) — From Density to Void
arXiv: 2503.14700. Simplicial complexes from fMRI correlations with explicit boundary operators. Central finding is a null result: higher-order brain interactions (k > 3) fail FDR correction and cross-subject replication. Anti-stability: topological features not robust across subjects. Density-void dilemma as fundamental methodological limitation.
**Machines**: chain complex, null hypothesis, stability (anti).
Full annotation: `inbox.md` (Wave 10b).
**See also**: `by-domain/tda.md`, `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`

### Dabaghian, Brandt & Frank (2014) — Reconceiving the hippocampal map as a topological template
eLife 03476. 136 citations. Place cells encode topology, not geometry. Morphing linear tracks dissociates topology from geometry; place fields preserve spatial ordering but not metric features. Direction-independent. Extends Dabaghian et al. 2012 from computation to experiment.
**Machines**: chain complex, stability, null hypothesis.
Full annotation: `inbox.md` (Wave 10b).
**See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`

### Lord, Expert, Fernandes, Petri, Van Hartevelt, Vaccarino, Deco, Turkheimer & Kringelbach (2016) — Insights into Brain Architectures from the Homological Scaffolds
Frontiers in Systems Neuroscience, DOI: fnsys.2016.00085. Extends Petri et al. 2014 homological scaffold method to resting-state fMRI across multiple subjects. Scaffold encodes which edges carry persistent cycles in the weighted clique complex. Reveals hierarchical modular organization invisible to standard graph metrics. Chain complex from correlation-weighted clique filtration; parameterized homology across weight threshold.
**Machines**: chain complex, parameterized homology.
Full annotation: `inbox.md` (Wave 10c).
**See also**: `by-domain/tda.md`, `by-structure/boundary_operators.md`, `by-structure/filtrations.md`
