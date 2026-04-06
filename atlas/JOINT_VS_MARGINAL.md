# Joint vs. Marginal Excess

## The Abstract Machine

Given components A and B, the composite system (A,B) may have structure absent from either component alone. The excess — P(A,B) - f(P(A), P(B)) > 0 — signals genuine composite structure that cannot be explained by the parts independently.

This is the most widely instantiated machine in the Rosetta. Every domain has a version, and the versions are connected by more than analogy — they share mathematical structure (typically: a divergence between a joint distribution and a product of marginals).

## Where It Appears

### Information Theory — The Home Domain
This machine originates here. Mutual information I(X;Y) = D_KL(P_XY || P_X ⊗ P_Y) IS the joint-vs-marginal excess, measured in bits.

**Rich substructure via PID**: Partial Information Decomposition refines MI into synergy (information present only in the joint), redundancy (information duplicated across sources), and unique information (specific to one source). The PID lattice decomposes the excess into finer atoms.

**Papers**:
- MINE (Belghazi et al., 2018) — neural estimator for MI via Donsker-Varadhan dual
- Wickstrøm et al. (2019) — I(X;T) and I(T;Y) at each layer
- Tax et al. (2017) — PID atoms through RBM training (synergy as joint-vs-marginal excess)
- Chwilka & Karbowski (2024) — MI divergence at finite variance (infinite excess possible)
- Sugiyama et al. (2016) — Pythagorean KL decomposition on posets (orthogonal isolation of higher-order interactions)
- Geiger (2021) — review of MI estimation artifacts
- Jónsson et al. (2020) — MI-based regularization

### QEC — Entanglement
A quantum state ρ_AB is entangled iff it cannot be written as a mixture of product states. Entanglement measures (entropy of entanglement, concurrence, negativity) quantify how much the joint state exceeds what separable states can achieve. The excess is always non-negative (separable states form a convex set) and bounded by the Hilbert space dimension.

**Papers**: Oreshkov (2013) — subsystem decomposition H_A ⊗ H_B; code subsystem preserves joint structure that gauge subsystem absorbs.

### TDA — Binding
The binding residual R = ||PI_joint - f(PI_X, PI_Y)|| measures whether the joint persistence image contains topological structure absent from marginal persistence images. Tested against surrogate null distributions.

### Dynamical Systems — Emergent Topology
When two uncoupled systems are coupled, the joint attractor may have topology (e.g., torus) absent from either component (e.g., two limit cycles). Convergent cross-mapping (Sugihara et al.) detects this as cross-predictability.

### Neuroscience — Neural Binding
Cross-frequency coupling (Tort et al., 2010 — in inbox), integrated information (Tononi — in inbox), and synergistic coding (Tax et al., 2017 applied to neural codes).

### Statistical Physics — Phase Transitions
Mézard & Mora (2008): solution-space structure in coupled constraint systems exceeds what individual constraints predict. The SAT/UNSAT transition is a collective (composite-system) phenomenon.

## Key Divergences

- **Entanglement is richer than binding**: QIT has partial trace, Schmidt decomposition, LOCC, monogamy. TDA binding has a scalar + p-value. See ANTISYNONYMS.md.
- **MI can diverge; topological excess cannot**: Lognormal MI → ∞ at finite variance. Persistence diagrams are always finite.
- **Estimation vs. computation**: MI must be estimated (MINE, KDE, binning). Entanglement can sometimes be computed exactly (pure states). Persistence is algorithmically exact.
