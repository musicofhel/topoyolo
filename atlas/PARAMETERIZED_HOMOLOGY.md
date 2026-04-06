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

### Neuroscience
Stimulus or task condition as parameter, neural representation geometry as invariant. (See inbox for Tsuda on chaotic itinerancy — attractor switching as topology change over time.)

## Key Divergences

- **Multi-scale vs. single-scale**: Persistence diagrams encode the full birth-death spectrum. QEC thresholds and SAT phase transitions are single critical values. The ML information plane is a trajectory, not a diagram.
- **Discrete vs. continuous**: TDA filtrations are typically discrete (finite number of simplices added). CTQEC parameterization is continuous (Lindblad). The ML case uses discrete epochs but treats the trajectory as continuous.
- **Artifact sensitivity**: Information-plane trajectories depend on the MI estimator used (Geiger, 2021). Persistence diagrams are exactly computable. QEC thresholds are Monte Carlo estimated. The "parameterized invariant" has different reliability across domains.
