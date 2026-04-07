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
- Kolchinsky (2024, arXiv: 2405.07665) — PID redundancy = information bottleneck; formally proves the compression-prediction tradeoff in IB IS the redundancy-synergy decomposition in PID. Bridges Joint and Param machines.
- Schreiber (2000, PRL 85:461) — transfer entropy T_{Y→X} = I(X_{t+1}; Y^(k)_t | X^(l)_t) as DIRECTED joint-vs-marginal excess. Asymmetric: T_{Y→X} ≠ T_{X→Y}. Bridges info theory and dynamical systems.
- Barrett (2015) — PID for Gaussians: closed-form decomposition showing synergy can be nonzero even when sources are uncorrelated (zero MI between them). The joint excess exists in the relationship to the target, not between the sources themselves. A precise characterization of when joint structure transcends marginal structure.
- Shwartz-Ziv & Tishby (2017) — MI between layers I(T_l; Y) as joint information: each layer's representation captures joint structure between input and output. The information plane trajectory tracks how much joint excess each layer preserves.
- Mediano et al. (2019) — PhiID 6-mode taxonomy of integration: decomposes the joint excess into redundancy, synergy, unique-X, unique-Y, transfer X→Y, and transfer Y→X. The most fine-grained decomposition of joint-vs-marginal in the literature.

### QEC — Entanglement
A quantum state ρ_AB is entangled iff it cannot be written as a mixture of product states. Entanglement measures (entropy of entanglement, concurrence, negativity) quantify how much the joint state exceeds what separable states can achieve. The excess is always non-negative (separable states form a convex set) and bounded by the Hilbert space dimension.

**Papers**: Oreshkov (2013) — subsystem decomposition H_A ⊗ H_B; code subsystem preserves joint structure that gauge subsystem absorbs.

### TDA — Binding and Higher-Order Structure
The binding residual R = ||PI_joint - f(PI_X, PI_Y)|| measures whether the joint persistence image contains topological structure absent from marginal persistence images. Tested against surrogate null distributions.

**Papers**: Harrington et al. (2017, arXiv: 1708.07390) — multiparameter bifiltration as joint object. Stratifying multiparameter PH reveals topological features visible in the joint bifiltration but invisible in either marginal (single-parameter) filtration. The excess IS the genuinely multi-scale structure. Barannikov et al. (2021, arXiv: 2106.04024) — Cross-Barcode(P,Q) tracks multiscale topological discrepancies between two manifold-supported distributions; MTop-Divergence = 0 iff topologically equivalent; builds a SINGLE barcode from the pair, conceptually distinct from comparing two PDs via Wasserstein. Varley et al. (2025, arXiv: 2504.10140) — H2 cavities in Rips filtration correlate with PID synergy (O < 0) in fMRI (ρ = −0.55 to −0.65); THE empirical bridge proving TDA cavities and info-theoretic synergy detect the same joint structure. Hamilton & Leditzky (2024, arXiv: 2307.07492) — PH of multipartite entanglement; integrated Euler characteristic = n-tangle; barcodes strictly finer than scalar entanglement measures; relative PH connects to strong subadditivity. Natarajan et al. (2026, arXiv: 2603.03237) — kernel/image/cokernel persistence of multi-species point clouds; cokernel = features ONLY visible in the joint (pure topological joint-vs-marginal excess); four-way decomposition richer than binary excess test.

### Dynamical Systems — Emergent Topology
When two uncoupled systems are coupled, the joint attractor may have topology (e.g., torus) absent from either component (e.g., two limit cycles). Convergent cross-mapping (Sugihara et al.) detects this as cross-predictability.

**Papers**: Sugihara et al. (2012) — CCM cross-prediction as joint excess: if species X and Y are causally coupled, the shadow manifold M_X contains information about Y that is absent from M_Y's own marginal. Cross-map correlation increasing with library length is the signature of genuine joint structure, distinguishing causation from correlation.

### Neuroscience — Neural Binding
Cross-frequency coupling: Tort et al. (2010, J Neurophysiol 104:1195) — phase-amplitude coupling modulation index = D_KL(observed amplitude distribution || uniform), measuring how much the joint (phase, amplitude) distribution exceeds the product of marginals. Oizumi, Albantakis & Tononi (2014, DOI: 10.1371/journal.pcbi.1003588) — IIT 3.0: Φ = D(p(X^t|X^{t-1}) || Π_i p(X_i^t|X_i^{t-1})), THE foundational formalization of joint-vs-marginal for consciousness; MICS specifies quality of experience. Synergistic coding (Tax et al., 2017 applied to neural codes). Peek et al. (2025) — TE-based directed coupling as joint excess: transfer entropy from neuron Y to neuron X measures the information in the joint (X-future, Y-past) that exceeds the marginal (X-future, X-past). The directed flag complex built from significant TE links encodes the topological structure of this directed joint excess. Thual et al. (2022) — fused OT reveals joint brain alignment: the Gromov-Wasserstein component captures joint geometric structure (spatial relationships between regions) that is absent from either subject's marginal anatomy alone. Weak instantiation — the "joint" is across subjects, not within a single system.

### Statistical Physics — Phase Transitions
Mézard & Mora (2008): solution-space structure in coupled constraint systems exceeds what individual constraints predict. The SAT/UNSAT transition is a collective (composite-system) phenomenon.

### Third Pass Additions

**Consciousness as excess** (IPWT): Synergistic information — whole-system information exceeding sum of subsystem information — as the criterion for consciousness. Replaces IIT's physical indivisibility with synergy. The binding residual applied to the whole brain.

**Quantum interference as excess** (Barandes): Complex phases in quantum amplitudes encode joint structure invisible in the marginal (probability) distribution. Born rule = projection from joint to marginal. Interference terms ARE the excess.

**Distributional code** (Dabney, Nature 2020): Population of dopamine neurons jointly encodes full reward distribution; no single neuron's marginal contains it. Quantile diversity measures the excess.

**Opponent encoding** (Striatal circuit): D1/D2 neurons encode opposite distribution tails. Neither half-population captures the full distribution. A matched-pair version of joint excess.

**Non-Markovian memory** (Spin-boson): Non-Markovian corrections are joint (spin-bath) structure invisible in marginal (spin-only) dynamics. The bath "remembers" the system's history.

**Causal emergence as inverted excess** (Rosas et al. 2020): Standard joint-vs-marginal asks "does the joint exceed the marginals?" Causal emergence inverts this: "does the coarse-grained MACRO exceed the sum of the MICRO parts?" Ψ = I(V_t; V_{t'}) - Σ_j I(X^j_t; V_{t'}) > 0 measures excess macro causal power. Theorem: emergence iff dynamical synergy > 0. Key decomposition: Syn = downward causation D + causal decoupling G, where G > 0 implies "statistical ghosts" — emergent features predicting their own future without micro-level causal trace. Applied to Game of Life (particles decoupled from cells), flocking (emergence at critical regime), macaque ECoG (motor representation emergent). A new direction for the machine: not just detecting excess, but decomposing it into qualitatively distinct modes.

**Graded information excess** (GMI): Separate MI for 0-cells (nodes) and 1-cells (edges) of a graph. Extending to simplicial complexes would create information-theoretic Betti numbers — one MI per dimension.

**Triangulated detection** (MI-NEE): Compare joint and marginal to a COMMON reference (uniform) rather than to each other. Faster convergence, different computational properties. A general strategy beyond MI estimation.

**State-dependent excess** (Specific entropy rate): h(x) - h_avg at state x. The variation of local unpredictability around the global average carries structure absent from the scalar average.

## Key Divergences

- **Entanglement is richer than binding**: QIT has partial trace, Schmidt decomposition, LOCC, monogamy. TDA binding has a scalar + p-value. See ANTISYNONYMS.md.
- **MI can diverge; topological excess cannot**: Lognormal MI → ∞ at finite variance. Persistence diagrams are always finite.
- **Estimation vs. computation**: MI must be estimated (MINE, KDE, binning). Entanglement can sometimes be computed exactly (pure states). Persistence is algorithmically exact.
- **Direct vs. triangulated detection**: MINE compares joint directly to product. MI-NEE triangulates through a common reference. Both measure MI but via different estimation paths with different convergence. No TDA analogue of this choice.
- **Distributional code ≠ persistence**: Dabney's quantile-indexed neurons look like parameterized homology but track probability mass, not topology. Every quantile exists simultaneously; there are no birth/death events. See ANTISYNONYMS.md.
