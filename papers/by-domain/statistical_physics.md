# Statistical Physics

Papers from the statistical physics / stochastic thermodynamics community, indexed by which abstract machines they instantiate. New domain opened in B2 batch-004 (stoch-thermo group); cross-references to `by-structure/` files are given per paper.

---

## Nakazato & Ito (2021)
**"Geometrical aspects of entropy production in stochastic thermodynamics based on Wasserstein distance"**
arXiv: 2103.00503 | cond-mat.stat-mech

**Domain(s)**: Statistical physics, optimal transport

Entropy production lower-bounded by the L2-Wasserstein path length of the density trajectory: dissipation cost = action of the cheapest matching path between measures. Yields a thermodynamic speed limit (time–entropy-production trade-off) and a geometric picture of optimal protocols; partial entropy production bounds generalize the second law of information thermodynamics.
**Machines**: matching (instrumental), joint-vs-marginal (weak).
Full annotation: `annotations/2103.00503.md` (B2 pass 25). Abstract-only provenance — depth-limited.
**See also**: `by-structure/optimal_transport.md`, `annotations/2206.14928.md`

## Ito, Oizumi & Amari (2018)
**"Unified framework for the entropy production and the stochastic interaction based on information geometry"**
arXiv: 1810.09545 | cond-mat.stat-mech

**Domain(s)**: Statistical physics, information theory

Violation of additivity of partial entropy productions = stochastic interaction (IIT): the joint-vs-marginal excess given a thermodynamic reading; entropy production also expressed as KL-minimizing projection. A deliberate Neuroscience↔Statistical-physics bridge (IIT + information geometry).
**Machines**: joint-vs-marginal (core), matching (weak), null hypothesis (implicit).
Full annotation: `annotations/1810.09545.md` (B2 pass 25). Abstract-only provenance — depth-limited.
**See also**: `by-domain/neuroscience.md`, `annotations/2103.00503.md`

## Ito (2022)
**"Geometric thermodynamics for the Fokker-Planck equation: Stochastic thermodynamic links between information geometry and optimal transport"**
arXiv: 2209.00527 | cond-mat.stat-mech/math-ph

**Domain(s)**: Statistical physics, optimal transport, information theory

Unifies information geometry and optimal transport via the excess entropy production rate of the Fokker–Planck equation: gradient flow ties excess EP to information geometry on probability-density space, OT velocity fields are read through information geometry on path-probability space. Yields thermodynamic trade-offs (cost vs observable fluctuation), minimum-cost optimal protocols, EP decomposition.
**Machines**: matching (core), joint-vs-marginal (weak).
Full annotation: `annotations/2209.00527.md` (B2 pass 26). Abstract-only provenance — depth-limited.
**See also**: `by-structure/optimal_transport.md`, `annotations/2103.00503.md`

## Barato & Seifert (2014)
**"Stochastic thermodynamics with information reservoirs"**
arXiv: 1408.1224 | cond-mat.stat-mech

**Domain(s)**: Statistical physics, information theory

Generalized second law for a system coupled to an information reservoir (bit sequence): work extraction from a single heat bath becomes possible once the information flow is credited — joint-vs-marginal bookkeeping in thermodynamic dress, with fluctuation theorem and linear response for information-processing machines (efficiency at max power can leave the universal 1/2).
**Machines**: joint-vs-marginal (core), null hypothesis (weak).
Full annotation: `annotations/1408.1224.md` (B2 pass 26). Abstract-only provenance — depth-limited.
**See also**: `by-structure/composite_systems.md`, `annotations/1810.09545.md`

## Sekizawa, Ito & Oizumi (2023)
**"Decomposing Thermodynamic Dissipation of Linear Langevin Systems via Oscillatory Modes and Its Application to Neural Dynamics"**
arXiv: 2312.03489 | q-bio.NC/cond-mat.stat-mech

**Domain(s)**: Statistical physics, neuroscience, dynamical systems

Housekeeping entropy production of linear Langevin systems decomposes into independent positive contributions from oscillatory modes (per element under diagonal noise); applied to monkey ECoG awake vs anesthesia — delta-band contribution larger, theta smaller under anesthesia. Neural oscillations get a thermodynamic reading via physical limits of information processing.
**Machines**: joint-vs-marginal (instrumental), filtration/parameterization (weak).
Full annotation: `annotations/2312.03489.md` (B2 pass 26). Abstract-only provenance — depth-limited.
**See also**: `by-domain/neuroscience.md`, `by-structure/composite_systems.md`, `annotations/1810.09545.md`

## Aref, Macris & Vuffray (2013)
**"Approaching the Rate-Distortion Limit with Spatial Coupling, Belief Propagation and Decimation"**
arXiv: 1307.5210 | cs.IT

BP-guided decimation on spatially coupled LDGM codes approaches the Shannon rate-distortion limit; performance explained quantitatively via the cavity-method phase diagram of the binary symmetric test-channel Gibbs measure — dynamical threshold saturates toward condensation, which approaches the Shannon noise level at large check degree. Includes a self-contained cavity-method introduction.
**Machines**: matching, null hypothesis, stability (core).
Full annotation: `annotations/1307.5210.md` (B2 pass 28). Abstract-only provenance — depth-limited.
**See also**: `by-domain/information_theory.md`, `by-structure/phase_transitions.md`

## Jain, Koehler, Liu & Mossel (2019)
**"Accuracy-Memory Tradeoffs and Phase Transitions in Belief Propagation"**
arXiv: 1905.10031 | cs.IT/math.ST

Bounded-memory message passing on tree reconstruction has a phase transition strictly below the Kesten–Stigum threshold (EKP conjecture proved); proof imports optimal transport as a bounding device for message accuracy. A computational-to-statistical gap for reconstruction, made quantitative.
**Machines**: stability (core), null hypothesis, matching (instrumental).
Full annotation: `annotations/1905.10031.md` (B2 pass 28). Abstract-only provenance — depth-limited.
**See also**: `by-domain/information_theory.md`, `by-structure/phase_transitions.md`, `by-structure/optimal_transport.md`

## Vicente, Saad & Kabashima (1999)
**"Statistical Physics of Irregular Low-Density Parity-Check Codes"**
arXiv: cond-mat/9908358 | cond-mat.dis-nn

Replica method locates a decoding phase transition in irregular LDPC ensembles that coincides with Shannon's coding bound under chosen degree distributions; BP decoding analyzed statistically and checked against simulation. Early seed of the cavity-method coding literature; degree-distribution irregularity as threshold-placement engineering.
**Machines**: null hypothesis (core), stability, matching (instrumental).
Full annotation: `annotations/cond-mat-9908358.md` (B2 pass 29). Abstract-only provenance — depth-limited.
**See also**: `by-domain/information_theory.md`, `by-structure/phase_transitions.md`, `annotations/1307.5210.md`

## Decelle, Krzakala, Moore & Zdeborová (2011)
**"Asymptotic Analysis of the Stochastic Block Model for Modular Networks and Its Algorithmic Applications"**
arXiv: 1109.3041 | cond-mat.stat-mech

Cavity-method phase diagram of the SBM: detectability/undetectability transition (KS-bound style — below it planted structure is information-theoretically unextractable from topology) and an easy/hard transition (statistical-to-computational gap). Translates directly into an asymptotically optimal BP community-detection algorithm. Canonical anchor for the detectability-transition machine in network inference.
**Machines**: null hypothesis (core), stability, matching, joint-vs-marginal (instrumental).
Full annotation: `annotations/1109.3041.md` (B2 pass 29). Abstract-only provenance — depth-limited.
**See also**: `by-domain/information_theory.md`, `by-structure/phase_transitions.md`, `annotations/1905.10031.md`

*Batch-004 ldpc-bp group closed 4/4 (B2 pass 29): cond-mat/9908358, 1307.5210, 1905.10031, 1109.3041.*

---

## B2 batch-005 — channel-capacity ↔ dissipation / criticality (2026-08-25)

### Qian & Roy (2011) — Capacity of biochemical signaling modules vs free-energy expenditure
arXiv: 1112.4589. Equilibrium (zero free-energy expenditure) is exactly where channel capacity vanishes; driving breaks detailed balance and buys capacity. Cascades as distributed multistage codes maintained dissipatively.
**Machines**: parameterized homology, null hypothesis, matching.
Full annotation: `annotations/1112.4589.md` (B2 pass 30). Abstract-only provenance — depth-limited.
**See also**: `by-domain/information_theory.md`, `by-structure/optimal_transport.md`

### Choi, Bao, Qi & Altman (2019) — Measurement-induced phase transition as QEC transition
arXiv: 1903.05124. Random unitary circuits with intermittent measurements: volume-law/area-law entanglement transition understood via error-correction thresholds of the scrambling-encoded information.
**Machines**: joint-vs-marginal excess (core), stability, parameterized homology.
Full annotation: `annotations/1903.05124.md` (B2 pass 30). Abstract-only provenance — depth-limited.
**See also**: `by-domain/qec.md`, `by-structure/phase_transitions.md`

### Bereyhi, Loureiro, Krzakala, Müller & Schulz-Baldes (2022) — Secure coding via Gaussian random fields
arXiv: 2205.08782. All-or-nothing transition of nonlinear Gaussian random fields: below the critical rate Bayesian recovery is perfect, above it uncorrelated; replica computation identifies the critical rate exactly with the channel capacity.
**Machines**: parameterized homology, null hypothesis, joint-vs-marginal excess.
Full annotation: `annotations/2205.08782.md` (B2 pass 31). Abstract-only provenance — depth-limited.
**See also**: `by-domain/information_theory.md`, `by-structure/phase_transitions.md`

### Kabashima, Murayama & Saad (1999) — Typical performance of Gallager-type codes
arXiv: cond-mat/9908104. Spin-glass analysis of Gallager codes: capacity saturation across code families indexed by sparse-matrix density; TAP ≡ belief-propagation decoding identification makes cavity results transferable verbatim to practical decoders.
**Machines**: null hypothesis, stability, parameterized homology.
Full annotation: `annotations/cond-mat-9908104.md` (B2 pass 31). Abstract-only provenance — depth-limited.
**See also**: `by-domain/information_theory.md`, `annotations/1307.5210.md`

*Lineage note (B3 sub-slice 3, pass 37):* cond-mat/9908104 is the ancestor of the ldpc-bp cavity group closed in batch-004 — its TAP ≡ BP identification is what lets the later threshold-saturation results (cond-mat/9908358 replica decoding transition; 1307.5210 spatially-coupled LDGM cavity phase diagram; 1905.10031 bounded-memory transitions via OT proof technology; 1109.3041 SBM detectability) read as descendants of one spin-glass analysis.

### Kelly, Poschinger, Schmidt-Kaler, Fisher & Marino (2022) — Coherence requirements for quantum communication
arXiv: 2210.11547. Monitored-dynamics/QEC unified as an adversarial unitary-vs-measurement game; coherence itself is the order parameter of a capacity/entanglement phase transition.
**Machines**: parameterized homology, stability, null hypothesis.
Full annotation: `annotations/2210.11547.md` (B2 pass 31). Abstract-only provenance — depth-limited.
**See also**: `by-domain/qec.md`, `by-domain/information_theory.md`

### Buendía (2024) — A mesoscopic theory for stochastic coupled oscillators
arXiv: 2407.02416. Finite-N mesoscopic description of stochastic Kuramoto: first closed expressions for the stochastic order parameter; the missing piece beyond Ott–Antonsen is identified as *multiplicative* ensemble fluctuations — composite-level structure absent from both single-oscillator marginals and the thermodynamic-limit reduction.
**Machines**: joint-vs-marginal excess, stability (critical exponents under finite-size noise).
Full annotation: `annotations/2407.02416.md` (B2 pass 46). Abstract-only provenance — depth-limited.
**See also**: `by-structure/composite_systems.md`

### Oh, Lee, Kahng & Kim (2006) — Heterogeneously coupled oscillators on scale-free networks
arXiv: cond-mat/0606048. Degree-dependent coupling J k_i^{η−1} on scale-free networks yields eight synchronization-transition behaviors indexed by (η, λ), split by the η = λ−2 line into zero- and finite-J_c regimes; critical exponents + finite-size scaling per regime, cluster-size distributions via generating functions.
**Machines**: stability (finite-size scaling), parameterized homology (transition-class taxonomy in the (η, λ) plane), joint-vs-marginal (weak — synchronized clusters as composites).
Full annotation: `annotations/cond-mat-0606048.md` (B2 pass 46). Abstract-only provenance — depth-limited.
**See also**: `by-structure/phase_transitions.md`

### Song, Choi & Kahng (2021) — Machine learning approaches for Kuramoto coupled oscillator systems
arXiv: 2109.08918. ML determination of the transition point and criticality of a hybrid synchronization transition; network-structure inference from chaotic patterns; comparison of ML algorithms for chaotic time-series prediction, with a forward look to EEG-style inverse problems.
**Machines**: stability (learned order parameters as transition detectors), matching (weak — recovering coupling structure from dynamics).
Full annotation: `annotations/2109.08918.md` (B2 pass 47). Abstract-only provenance — depth-limited.
**See also**: `by-structure/phase_transitions.md`, `by-structure/optimal_transport.md`

### Witthaut & Timme (2013) — Kuramoto dynamics in Hamiltonian systems
arXiv: 1305.1742. A classical conservative system with 2N state variables whose N-dimensional invariant manifolds carry exact Kuramoto dynamics; the synchronization transition emerges where the transverse Hamiltonian action dynamics becomes unstable — dissipative sync located by conservative instability analysis.
**Machines**: stability (transition as transverse instability), joint-vs-marginal excess (transverse dynamics = composite-level excess over the Kuramoto marginal).
Full annotation: `annotations/1305.1742.md` (B2 pass 47). Abstract-only provenance — depth-limited.
**See also**: `by-domain/dynamical_systems.md`, `by-structure/composite_systems.md`

## B2 batch-009 — rg-dl bridge (2026-08-25)

### Mehta & Schwab (2014) — Exact mapping: variational RG ↔ deep learning
arXiv: 1410.3831. Term-by-term identity between Kadanoff's variational renormalization group and RBM-stack deep architectures (weights ↔ couplings, layers ↔ coarse-graining stages, relevant operators ↔ persisting features), demonstrated on the 1D/2D Ising model. Founding hypothesis of the rg-dl lineage: deep learning as a generalized RG-like feature-extraction scheme; its skeptical refinement is 1906.05212 (pass 51).
**Machines**: parameterized homology (core; layer index = scale parameter), stability (relevance = persistence under the coarse-graining flow).
Full annotation: `annotations/1410.3831.md` (B2 pass 49). Abstract-only provenance — depth-limited. **B3 flag DISCHARGED (pass 51):** paired with the skeptical null 1906.05212 — claim-vs-refutation note in `glossary/ANTISYNONYMS.md`.
**See also**: `annotations/1906.05212.md`, `by-structure/filtrations.md`, `by-structure/phase_transitions.md`.

### Howard, Klinger, Maiti & Stapleton (2024) — Bayesian RG flow in neural network field theories
arXiv: 2405.17538. BRG-NNFT: coarse-graining in *parameter space* against a Fisher-metric distinguishability scale; training = IR→UV flow, information-shell coarse graining = UV→IR; BRG ≡ ERG exactly when the two cutoffs coincide, demonstrated as exact momentum-shell ERG for a free scalar SFT in the infinite-width cos-net case. Replaces Mehta–Schwab's RBM-stack identity with an information-geometric one.
**Machines**: parameterized homology (Fisher cutoff as filtration parameter), stability (equivalence-at-matched-cutoffs as persistence under reparameterization), matching (NN↔SFT structure-preserving correspondence).
Full annotation: `annotations/2405.17538.md` (B2 pass 50). Abstract-only provenance — depth-limited.
**See also**: `by-structure/filtrations.md`.

### de Mello Koch & Ghosh (2025) — Two-phase deep learning dynamics
arXiv: 2504.12700. Learning as rapid curve-fitting then slow compression/coarse-graining; grokking, double descent and the information bottleneck unified by shared timescale structure; hidden-layer/input mutual information as the progress measure; compression = principled RG-like forgetting critical for generalization, not actively optimized by SGD.
**Machines**: parameterized homology (training time as filtration parameter, MI as persistent quantity), stability (generalization as what survives the compression phase), null hypothesis (delayed generalization as excess over the "fitting explains it" null).
Full annotation: `annotations/2504.12700.md` (B2 pass 50). Abstract-only provenance — depth-limited.
**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`.

### Rançon, Rançon, Ivek & Balog (2025) — Dreaming up scale invariance via inverse RG
arXiv: 2506.04016. Minimal nets (three trainable parameters) invert real-space RG coarse-graining probabilistically on the 2D Ising model, generating critical configurations whose scaling observables and nontrivial RG eigenvalues check out; added depth gives no benefit — universality capturable by fractal-rule-style local rules. The lineage's first inverse-direction entry: generating microstates from coarse-grained ones rather than coarse-graining data or training dynamics.
**Machines**: stability (certified by persistence of RG eigenvalues under iterated coarse-graining), parameterized homology (scale-indexed observable family), null hypothesis (probabilistic recovery against the destroyed-information null; depth ablation as complexity-null control).
Full annotation: `annotations/2506.04016.md` (B2 pass 50). Abstract-only provenance — depth-limited.
**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`.

### de Mello Koch, de Mello Koch & Cheng (2019) — Is Deep Learning a Renormalization Group Flow?
arXiv: 1906.05212. Skeptical counterweight to the lineage's founding claim: hidden-visible correlators of RBMs trained on Ising configurations are used as operational diagnostics for RG-like coarse graining. Numerics find RG-like patterns AND important differences between RG and deep learning in the same observables — converts Mehta–Schwab's mapping into a measurable, partially-refuted hypothesis.
**Machines**: null hypothesis (the "deep learning is just RG" reading constructed so it can fail partially), stability (correlator persistence as the tracked signal), parameterized homology (layer ↔ RG step as scale parameter, used as test bench).
Full annotation: `annotations/1906.05212.md` (B2 pass 51). Abstract-only provenance — depth-limited. **Annotated AS A PAIR with 1410.3831; claim-vs-refutation note filed in `glossary/ANTISYNONYMS.md`.**
**See also**: `by-structure/filtrations.md`, `by-structure/phase_transitions.md`.

### Touboul & Destexhe (2009) — Can power-law scaling and neuronal avalanches arise from stochastic dynamics?
Analytic + surrogate null for avalanche-based SOC claims: thresholded stochastic processes provably produce spurious log-log power-law scaling that fails Kolmogorov-Smirnov testing; a known-SOC artificial network passes the same rigorous tests — the null is discriminating, not universal.
**Machines**: null hypothesis (core), stability (verdict instability under threshold/analysis-class perturbation).
Full annotation: `annotations/0910.0805.md` (B2 pass 57). **See also**: `by-domain/neuroscience.md`, `by-structure/phase_transitions.md` (null-surrogate lineage).

### Biehl, Pollock & Kanai (2020) — A Technical Critique of Some Parts of the Free Energy Principle
arXiv: 2001.06408. Refutation side of the FEP pair: counterexample disproving the original free energy lemma; non-equivalent Markov-blanket definitions across FEP works; the Bayesian-inference reading shown to hinge on an unjustified variational/ergodic density equality — the composite boundary is version-dependent, so the excess it licenses is not well-defined until the definition class is fixed.
**Machines**: null hypothesis (core — first corpus entry whose null targets a formalism's derivation rather than an empirical claim), stability (locus-of-failure analysis), joint-vs-marginal (boundary non-well-definedness).
Full annotation: `annotations/2001.06408.md` (B2 pass 56; filed here pass 58 — backfill debt). Abstract-only provenance — depth-limited. **Annotated AS A PAIR with `annotations/1906.10184.md`; note in `glossary/ANTISYNONYMS.md`.**
**See also**: `by-domain/neuroscience.md`, `by-structure/composite_systems.md`.

### Moosavi, Montakhab & Valizadeh (2018) — Coexistence of scale invariant and rhythmic behavior in self-organized criticality
arXiv: 1807.07213. Oscillatory perturbation of the Zhang model: rhythms embedded in scale-free avalanches, amplitude decaying with frequency, optimal amplification at the critical point — criticality-as-resonance in a known-SOC positive control.
**Machines**: stability (core), parameterized homology (frequency axis), null hypothesis (incompatibility reading).
Full annotation: `annotations/1807.07213.md` (B2 pass 58). Abstract-only provenance — depth-limited.
**See also**: `by-domain/neuroscience.md`, `by-structure/phase_transitions.md` (batch-011 soc group).

### Girardi-Schappo, Kinouchi & Tragtenberg (2012) — Critical Avalanches and Subsampling in Map-based Neural Networks
arXiv: 1209.3271. Synaptic noise as sufficient generator of critical avalanches in map-based networks, plus explicit subsampling analysis — noise-induced criticality as alternative mechanism and partial recording as artifact channel for experimental SOC claims.
**Machines**: null hypothesis (core), stability, parameterized homology (weak).
Full annotation: `annotations/1209.3271.md` (B2 pass 58). Abstract-only provenance — depth-limited.
**See also**: `by-domain/neuroscience.md`, `by-structure/phase_transitions.md` (batch-011 soc group).
