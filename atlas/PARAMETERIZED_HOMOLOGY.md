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

**Papers**: Bottleneck Degree (Di Rocco et al., 2019) — the reach determines the scale at which topology is correctly recoverable; bottleneck degree bounds the number of critical scales. Financial TDA (de Jesus Jr. et al., 2025) — sliding-window persistence on time series, extracting persistent entropy, amplitude, and point count as the window moves.

### QEC — Error Thresholds
The parameter is the physical error rate p (or the correction/decoherence ratio κ/λ in CTQEC). Below threshold, logical information (homology) is preserved with exponentially small error. Above threshold, information is destroyed.

**Papers**: de la Fuente et al. (2025) — threshold at ~2.5%, phase transition in noisy complexes. Oreshkov (2013) — continuous parameterization by κ/λ; quantum Zeno regime transitions.

### Dynamical Systems — Bifurcation Diagrams
The parameter is a coupling strength, forcing amplitude, or system parameter. At bifurcation points, the attractor topology changes — fixed points become limit cycles, limit cycles become tori, etc.

### Information Theory — Multiple Instances

1. **Information plane** (Wickstrøm et al., 2019; Geiger, 2021; Jónsson et al., 2020): parameter = training epoch, invariant = I(X;T) and I(T;Y). Fitting and compression phases are birth and death of information-theoretic features.

2. **PID through training** (Tax et al., 2017): parameter = training epoch, invariant = PID atoms (synergy, redundancy, unique). Redundancy-then-specialization transition.

3. **SAT phase transition** (Mézard & Mora, 2008): parameter = constraint density α, invariant = solution space topology. Shattering at α_c ≈ 4.267.

4. **MI divergence** (Chwilka & Karbowski, 2024): parameter = variance σ², invariant = MI. Phase boundary where MI diverges at finite σ².

### Hawkes Processes (discovered in second pass)
The criticality parameter m = ||φ||_L1 (average offspring number) parameterizes a family of point processes. At m < 1 (subcritical), m = 1 (critical), m > 1 (supercritical), the long-run behavior changes qualitatively. Subcritical → Brownian motion limit; critical → CIR diffusion (Horst & Xu, 2024). The ephemeral excitation model (Daw & Pender, 2021) parameterizes a path from Poisson (null) to Hawkes (full structure) via activity duration.

### Energy Landscapes
Disconnectivity graphs (Niroomand & Wales, 2023) ARE H₀ persistence diagrams: energy threshold = filtration parameter, component mergers = deaths. Independently invented by physical chemistry with zero TDA cross-citation.

### Neuroscience
Stimulus or task condition as parameter, neural representation geometry as invariant. Inter-hemispheric connectivity strength parameterizes attractor count in cortical models (Fasoli et al., 2026). (See inbox for Tsuda on chaotic itinerancy.)

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
