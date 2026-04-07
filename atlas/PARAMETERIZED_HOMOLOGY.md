# Parameterized Homology

## The Abstract Machine

Track a topological or structural invariant as a parameter varies. The invariant changes character at critical parameter values — features are born, die, merge, or split. The full record of these transitions is the output.

```
Parameter ε:  ε₁ -------- ε₂ -------- ε₃ -------- ε₄
Invariant:    birth(α)    ·           death(α)    birth(β)
              ·           birth(γ)    ·           ·
```

The shared structure is: (1) a parameter space, (2) a family of objects indexed by the parameter, (3) invariants computed at each parameter value, (4) critical values where the invariants change qualitatively.

## Where It Appears

### TDA — Persistence Diagrams
The parameter is the filtration scale ε. As ε increases, simplices are added to the complex, homology classes are born and die. The persistence diagram records all (birth, death) pairs. This is the canonical instance.

**Papers**: Bottleneck Degree (Di Rocco et al., 2019) — the reach determines the scale at which topology is correctly recoverable; bottleneck degree bounds the number of critical scales. Financial TDA (de Jesus Jr. et al., 2025) — sliding-window persistence on time series, extracting persistent entropy, amplitude, and point count as the window moves. Harrington et al. (2017, arXiv: 1708.07390) — multiparameter PH stratification; joint bifiltration captures topological features invisible to any single-parameter filtration. Perea & Harer (2013, arXiv: 1307.6188) — SW1PerS: sliding window embedding of periodic time series into high-dimensional space, then PH on the point cloud; bridges TDA filtration to dynamical systems via Takens-style delay embedding. Adams et al. (2017) — persistence images vectorize the PH output at each filtration scale into a stable, finite-dimensional representation; the image itself is parameterized by bandwidth and weighting function. Berry et al. (2023) — filtration scale epsilon and dimension k jointly parameterize the quantum TDA algorithm; critical values where Betti numbers change correspond to topological phase transitions in the complex.

### QEC — Error Thresholds
The parameter is the physical error rate p (or the correction/decoherence ratio κ/λ in CTQEC). Below threshold, logical information (homology) is preserved with exponentially small error. Above threshold, information is destroyed.

**Papers**: de la Fuente et al. (2025) — threshold at ~2.5%, phase transition in noisy complexes. Oreshkov (2013) — continuous parameterization by κ/λ; quantum Zeno regime transitions. Hastings & Haah (2021) — time parameterizes the Floquet code: the stabilizer group cycles through three configurations per period, and logical qubits emerge from the periodic orbit rather than from any single time-slice. The parameter is discrete (period steps) but the invariant (logical qubit count) changes at the transition from static to dynamic code.

### Dynamical Systems — Bifurcation Diagrams
The parameter is a coupling strength, forcing amplitude, or system parameter. At bifurcation points, the attractor topology changes — fixed points become limit cycles, limit cycles become tori, etc.

**Papers**: Takens (1981) — embedding dimension d is the parameter; below critical d = 2 dim_box(A) + 1 the reconstruction fails, above it the attractor topology is preserved. The transition from insufficient to sufficient embedding is a critical value in the parameterized homology sense. Sauer, Yorke & Casdagli (1991) — box-counting dimension replaces topological dimension as the parameter determining critical embedding; strengthens Takens from generic (measure-zero exceptions) to prevalent (probability-one). Tsuda (2001) — time parameterizes attractor switching in chaotic itinerancy; the system trajectory visits quasi-stable ruins of attractors, with transitions between them constituting the topological changes.

### Information Theory — Multiple Instances

1. **Information plane** (Wickstrøm et al., 2019; Geiger, 2021; Jónsson et al., 2020): parameter = training epoch, invariant = I(X;T) and I(T;Y). Fitting and compression phases are birth and death of information-theoretic features. Kolchinsky (2024, arXiv: 2405.07665) — rate-distortion curve parameterized by compression level β; proves PID redundancy = IB compression-prediction tradeoff, formally bridging the Joint and Param machines. Shwartz-Ziv & Tishby (2017) — THE original information plane paper: training epoch parameterizes a trajectory through the I(X;T) vs I(T;Y) plane, with distinct fitting (MI increases) and compression (MI decreases) phases.

2. **PID through training** (Tax et al., 2017): parameter = training epoch, invariant = PID atoms (synergy, redundancy, unique). Redundancy-then-specialization transition.

3. **SAT phase transition** (Mézard & Mora, 2008): parameter = constraint density α, invariant = solution space topology. Shattering at α_c ≈ 4.267.

4. **MI divergence** (Chwilka & Karbowski, 2024): parameter = variance σ², invariant = MI. Phase boundary where MI diverges at finite σ².

5. **PID for Gaussians** (Barrett, 2015): Three parameter axes — number of sources, time lag, and correlation strength — each reveal different PID atom decompositions. Varying correlation with fixed structure shows synergy can be nonzero even when sources are uncorrelated.

### Hawkes Processes (discovered in second pass)
The criticality parameter m = ||φ||_L1 (average offspring number) parameterizes a family of point processes. At m < 1 (subcritical), m = 1 (critical), m > 1 (supercritical), the long-run behavior changes qualitatively. Subcritical → Brownian motion limit; critical → CIR diffusion (Horst & Xu, 2024). The ephemeral excitation model (Daw & Pender, 2021) parameterizes a path from Poisson (null) to Hawkes (full structure) via activity duration.

### Energy Landscapes
Disconnectivity graphs (Niroomand & Wales, 2023) ARE H₀ persistence diagrams: energy threshold = filtration parameter, component mergers = deaths. Independently invented by physical chemistry with zero TDA cross-citation.

### Neuroscience
Stimulus or task condition as parameter, neural representation geometry as invariant. Inter-hemispheric connectivity strength parameterizes attractor count in cortical models (Fasoli et al., 2026). (See inbox for Tsuda on chaotic itinerancy.)

**Papers**: Mediano et al. (2019) — spatiotemporal scale as parameter: different temporal windows and spatial groupings reveal different PhiID atoms (synergy, redundancy, transfer). The decomposition changes qualitatively across scales, with some atoms dominant at fast timescales and others at slow.

### Third Pass Additions

**Filling fraction** (Arovas-Zhang FQHE): nu = p/q parameterizes topological phases. At each rational filling, different anyonic excitations. Energy gap protects the phase — topological protection.

**Frequency as filtration** (3 neuroscience papers): EEG frequency bands function as filtration parameter for brain causal networks. Different frequencies reveal different causal topologies. Structurally identical to persistence but NOT nested — alpha-band causal graph is not a subset of gamma-band graph. See ANTISYNONYMS.md.

**Quantile index** (Dabney, Nature 2020): tau ∈ [0,1] indexes dopamine neurons. As tau varies, the full reward distribution is traced out. Each neuron's reversal point is a kind of "critical value." The population is the parameterized family.

**Observation window** (Finite-time MI, Zhu et al.): I(t)/t as function of observation duration t. Discovers "exceed-average phenomenon" — instantaneous rate can exceed time-averaged capacity C. Shannon capacity is the stable infinite-time limit.

**Twisting map** (Hom-Lie cohomology): α parameterizes family of algebraic structures. As α deviates from identity, cohomology changes — some classes persist, others born/die. Direct algebraic parallel to persistence.

**State-dependent entropy** (Specific entropy rate): h(x) varies across the attractor. Stable manifold regions have low h(x); chaotic saddle regions have high h(x). The variation is a spatial "persistence diagram" of unpredictability.

## Key Divergences

- **Multi-scale vs. single-scale**: Persistence diagrams encode the full birth-death spectrum. QEC thresholds and SAT phase transitions are single critical values. The ML information plane is a trajectory, not a diagram.
- **Nested vs. non-nested**: TDA filtrations are nested (increasing ε adds simplices monotonically). Neuroscience frequency "filtrations" are NOT nested — different frequencies reveal genuinely different structures. Hawkes criticality is also non-nested (single transition, not progressive). See ANTISYNONYMS.md.
- **Discrete vs. continuous**: TDA filtrations are typically discrete (finite number of simplices added). CTQEC parameterization is continuous (Lindblad). The ML case uses discrete epochs but treats the trajectory as continuous.
- **Artifact sensitivity**: Information-plane trajectories depend on the MI estimator used (Geiger, 2021). Persistence diagrams are exactly computable. QEC thresholds are Monte Carlo estimated. The "parameterized invariant" has different reliability across domains.
