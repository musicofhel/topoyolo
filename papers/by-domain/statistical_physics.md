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
