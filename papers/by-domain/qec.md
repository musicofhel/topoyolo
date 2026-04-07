# Quantum Error Correction

Papers from the QEC community, indexed by which abstract machines they instantiate. Cross-references to `by-structure/` files are given per paper.

---

## Cross-listed from Inbox

- **de la Fuente, Feldman, Eisert, Bauer (2025)** — "High-threshold decoding of non-Pauli codes for 2D universality." Toric/surface code as cellular homology, JIT matching decoder, error threshold as parameterized phase transition. Full annotation in `papers/inbox.md`. Machines: chain complex, matching, parameterized homology, stability, null hypothesis.

---

## Oreshkov (2013)
**"Continuous-time quantum error correction"**
arXiv: 1311.2485 | Chapter in *Quantum Error Correction* (Cambridge University Press, 2013)

**Domain(s)**: Quantum error correction, quantum information theory

**Abstract machines instantiated**:
- **Chain complex**: The subsystem decomposition H_S = H_A tensor H_B direct-sum K is the Hilbert space analogue of a chain complex. The code subsystem H_A contains the protected information; the gauge subsystem H_B absorbs correctable errors; the orthogonal complement K contains uncorrectable states. The error-correcting map R is a projection that returns states to the code subspace — analogous to projecting onto cycles modulo boundaries. The correctability condition Tr_B{P_AB . R . E(sigma)} = Tr_B{sigma} is the analogue of ∂^2 = 0: applying noise E followed by correction R followed by projection P_AB recovers the original information.
- **Parameterized homology**: The error correction rate kappa and decoherence rate lambda are the two parameters. As kappa/lambda varies, the system transitions between regimes: (1) kappa >> lambda: quantum Zeno regime, state frozen (information preserved); (2) kappa ~ lambda: partial protection; (3) kappa << lambda: information lost. The critical ratio kappa/lambda is the analogue of a filtration parameter — below it, the "topological" (information-theoretic) invariant is preserved; above it, the invariant is destroyed.
- **Stability**: Two stability results. First, Markovian regime: error rate scales as lambda^2/kappa — quadratic suppression of decoherence. Information loss is bounded and continuous in the perturbation parameter. Second, non-Markovian regime: CTQEC exhibits a quantum Zeno effect where error rate scales as lambda^4/kappa^2 — quadratic improvement over the Markovian case. The Zeno regime provides stronger stability because the noise process itself has internal correlations that the continuous correction can exploit.
- **Null hypothesis**: The uncorrected evolution (kappa = 0) serves as the null model. The Lindblad generator L(rho) describes pure decoherence — structure destruction without correction. The error-correction generator J(rho) = R(rho) - rho counteracts it. The gap between corrected and uncorrected evolution quantifies the value of error correction.

**What is genuinely new (not reducible to shared abstraction)**:
- The continuous-time formulation itself: both noise and correction are modeled as Lindblad master equations rather than discrete CPTP maps. The master equation d(rho)/dt = L(rho) + kappa*J(rho) has no direct analogue in TDA (where filtrations are discrete) or classical dynamical systems (where error correction is not part of the dynamics).
- Weak measurement + feedback architecture: error correction is implemented via a stream of ancilla qubits that continuously pump out entropy. The ancilla coupling strength epsilon controls the measurement weakness. This is a physical implementation of continuous error correction, not just a mathematical limit.
- The Zeno regime quadratic improvement: in non-Markovian dynamics, CTQEC achieves lambda^4/kappa^2 scaling instead of lambda^2/kappa. This exploits temporal correlations in the noise — a feature absent in classical error correction.
- The subsystem principle perspective: rather than thinking of error correction as syndrome measurement + conditional unitary, the paper frames it as maintaining a subsystem factorization. This is a more algebraic viewpoint that connects naturally to the chain complex picture.

**Connections the authors acknowledge**: Cite the Paz-Zurek quantum-jump model (2001), Sarovar-Milburn continuous cooling scheme (2005), and Ahn-Doherty-Landahl direct feedback (2002). Situated entirely within QEC/quantum control literature. No connections to TDA, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Code subsystem H_A | Cycle space (protected information = non-trivial homology) |
| Gauge subsystem H_B | Boundary space (absorbs correctable errors) |
| Orthogonal complement K | Uncorrectable states (outside the chain complex) |
| Error-correcting map R | Projection onto cycles mod boundaries |
| Correctability condition | ∂^2 = 0 analogue (noise + correction = identity on code) |
| Lindblad generator L | Noise process (structure destruction) |
| Error-correction generator J | Repair process (boundary projection) |
| Error correction rate kappa | Scale parameter (analogous to filtration resolution) |
| Decoherence rate lambda | Perturbation magnitude |
| Quantum Zeno regime | Stability regime (frozen topology under continuous observation) |
| Non-Markovian noise | Noise with temporal correlations (exploitable structure) |
| Weak measurement strength epsilon | Resolution parameter |
| Subsystem decomposition | Chain complex splitting |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`

---

## Cross-listed from Second Pass + Bridges

- **Pati & Sanders (2005)** — "No partial erasure of quantum information." Topological dimension of Bloch sphere S² is absolute invariant under all CPTP maps. Strongest possible stability: impossibility, not a bound. Full annotation: `cross_domain_bridges.md`. Machines: stability (impossibility), chain complex (topological), joint-vs-marginal.

- **Tarnowski et al. (2019)** — "Chern number from linking number." Static topological invariant (Chern number) measured from post-quench dynamics. Integer-valued and topologically protected. Full annotation: `second_pass.md` (SP-12). Machines: chain complex, parameterized homology, null hypothesis, stability. **Also dynamical systems.**

- **Garbaczewski (2005)** — "Differential entropy and time." Von Neumann entropy S(ρ)=0 for pure states while Shannon entropy of |ψ|² is dynamic — multi-level information decomposition. Full annotation: `cross_domain_bridges.md`. Machines: parameterized homology, joint-vs-marginal, stability, null hypothesis. **Bridge: info theory + dynamics + QEC.**

---

## Wave 4 (2026-04-06) — "To Find" Papers

### Kitaev (1997) — Fault-tolerant quantum computation by anyons
**"Fault-tolerant quantum computation by anyons"**
arXiv: quant-ph/9707021
THE foundational toric code paper. Chain complex on T² (qubits on edges, stabilizers from ∂/δ). Logical qubits = H₁(T², ℤ/2). Anyonic excitations matched by fusion. Computation via braid group on fusion space. Topological fault tolerance: errors must create non-trivial homology cycle.
**Machines**: chain complex, matching, stability. **See also**: `by-structure/boundary_operators.md`, `by-structure/optimal_transport.md`.

### Dennis, Kitaev, Landahl, Preskill (2002) — Topological quantum memory
**"Topological quantum memory"**
arXiv: quant-ph/0110143
Explicit surface code construction with recovery protocols. Threshold theorem: below p_c, exponential suppression. Phase transition maps EXACTLY to 3D Z₂ lattice gauge theory (cross-domain bridge to stat mech). MWPM syndrome matching. 4D procedure without measurement.
**Machines**: chain complex, parameterized homology, matching, stability, null hypothesis. **See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`, `by-structure/optimal_transport.md`.

### Freedman, Kitaev, Larsen, Wang (2001) — Topological Quantum Computation
**"Topological Quantum Computation"**
arXiv: quant-ph/0101025
Quantum computation from anyonic systems = unitary topological modular functors (Witten-Chern-Simons). Braiding computes gates; fusion rules generalize boundary operators. Error rate e^{-αℓ} — topological protection by length scale. Abelian anyons as null (trivial computation). Connection to Jones polynomial and knot invariants.
**Machines**: chain complex, stability, matching, null hypothesis. **See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`.

### Bombin & Martin-Delgado (2007) — Statistical Mechanical Models and Topological Color Codes
**"Statistical Mechanical Models and Topological Color Codes"**
arXiv: 0711.0468
Color codes on trivalent lattices with Z₂×Z₂ gauge group. Overlap with factorized state = 3-body Ising partition function. Different universality classes = different computational capabilities. Error threshold p_c ≈ 0.109 (close to toric code). Direct transversal Clifford gates.
**Machines**: chain complex, stability, null hypothesis, joint-vs-marginal. **See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`.

---

## Third Pass (2026-04-05)

### Arovas & Zhang (1992) — Topological Aspects of FQHE
**Domain(s)**: QEC (topological order), condensed matter
The original FQHE-TQFT connection. Filling fraction nu parameterizes the family of topological phases. Ground state degeneracy on genus-g surface = dim(H₁(Σ_g, ℤ/n)) — directly a chain complex computation. Energy gap provides topological protection (strongest stability). Anyonic excitations come in particle-antiparticle pairs (matching constraint via fusion rules). Integer QHE as null (trivial topological order).
**Machines**: chain complex, parameterized homology, stability, null hypothesis, matching (weak).
Full annotation: `third_pass_neuro_qec.md` (TP-05).
**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`

### Barandes (2023) — Stochastic-Quantum Correspondence (arXiv: 2309.03085)
**Domain(s)**: Quantum foundations, dynamical systems
Derives quantum mechanics from stochastic axioms. Interference terms = joint-vs-marginal excess. Complex Hilbert space encodes joint structure invisible in marginal (probability) distribution. Born rule = projection from joint to marginal. Functorial mapping between stochastic and quantum categories. Classical (real, positive) stochastic processes as null.
**Machines**: chain complex, stability, parameterized homology, joint-vs-marginal.
Full annotation: `third_pass_neuro_qec.md` (TP-06).
**See also**: `by-structure/boundary_operators.md`, `by-structure/composite_systems.md`

### Quantum State Tomography via Generative Models (arXiv: 1810.10584)
**Domain(s)**: QEC (tomography), machine learning
Tomography as inverse matching: given measurement outcomes, reconstruct the density matrix. Generative model learns mapping from latent to measurement probabilities. Entanglement = joint structure absent from reduced density matrices. Separable (unentangled) state as null.
**Machines**: matching, parameterized homology, joint-vs-marginal, null hypothesis.
Full annotation: `third_pass_neuro_qec.md` (TP-07).
**See also**: `by-structure/optimal_transport.md`, `by-structure/composite_systems.md`

### Spin-Boson Born Approximation
**Domain(s)**: QEC (open quantum systems), dynamical systems
Non-Markovian sqrt(alpha) prompt coherence loss — an anti-stability result. Standard perturbation theory (linear in alpha) underestimates decoherence. Non-Markovian corrections = joint (spin-bath) structure invisible in marginal (spin-only) dynamics. Markovian approximation as null.
**Machines**: parameterized homology, stability (anti), null hypothesis, joint-vs-marginal.
Full annotation: `third_pass_neuro_qec.md` (TP-10).
**See also**: `by-structure/phase_transitions.md`

### Mézard & Mora (2008) — QEC-relevant aspects
Factor graph for LDPC decoding IS a chain complex (variable nodes = 0-cells, check nodes = 1-cells, H = boundary operator). BP on LDPC = soft matching. Phase transition threshold in CSP = error correction threshold. Already in info theory; this annotation captures QEC-specific content.
Full annotation: `third_pass_neuro_qec.md` (TP-12).

---

## Wave 5 (2026-04-06) — Quantum TDA Bridge + Floquet Codes

### Berry, Su, Gyurik, King, Basso, Del Toro Barba, Rajput, Wiebe, Dunjko, Babbush (2023) — Quantum Advantage in TDA
**"Analyzing Prospects for Quantum Advantage in Topological Data Analysis"**
arXiv: 2209.13581 | PRX Quantum 4, 040349 (2023)

**Domain(s)**: TDA, QEC (quantum algorithms) — DIRECT BRIDGE PAPER

The paper that asks: can quantum computers speed up TDA? Works directly with the chain complex of the clique complex of a graph G: boundary operators dG_k, combinatorial Laplacian Delta^G_{k-1}, Dirac operator BG = dG + dG^{dagger}. Betti number = dim(ker(Delta)). Quantum algorithm projects onto ker(BG) via Chebyshev polynomial eigenvalue filtering + amplitude estimation. Key finding: super-quadratic quantum speedup requires multiplicative error AND asymptotically growing Betti number. Dequantization via classical random walk on k-simplices shows exponentially large dimension + Betti number are necessary but INSUFFICIENT for super-polynomial advantage. Tens of billions of Toffoli gates sufficient for classically intractable instances.
**Machines**: chain complex (the computation IS the chain complex), parameterized homology (epsilon-filtration + dimension k), matching (weak — random walk on simplices), stability (robustness of quantum advantage to parameter regime), null hypothesis (dequantization as classical null).
Full annotation: `inbox.md`.
**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `cross_domain_bridges.md`

### Hastings & Haah (2021) — Dynamically Generated Logical Qubits (Honeycomb/Floquet Code)
**"Dynamically Generated Logical Qubits"**
arXiv: 2107.02194

**Domain(s)**: QEC

The foundational Floquet code paper. Honeycomb lattice with 2-qubit Pauli checks measured in period-3 rounds. As a subsystem code: ZERO logical qubits. With periodic measurement schedule: TWO logical qubits with distance proportional to system size. The ISG S(r) changes every round; logical operators have period-6 dynamics (electric <-> magnetic exchange). Fault tolerance via MWPM on 2+1D spacetime syndrome lattice (bipartite simple cubic structure). Maps to Kitaev's honeycomb model via Majorana fermions; inner logical operators transport fermions, outer transport bosons (e/m anyons).
**Machines**: chain complex (honeycomb cellular complex on T^2, stabilizers from cycles), parameterized homology (THE key machine — time parameterizes the code, logical qubits emerge from periodic orbit not any snapshot), stability (error threshold despite time-varying code), null hypothesis (static subsystem code with 0 logical qubits), matching (MWPM on spacetime syndrome lattice).
Full annotation: `inbox.md`.
**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`

## Wave 4c (2026-04-06) — Foundational Threshold Theorems

### Aharonov & Ben-Or (1997/1999) — Fault-Tolerant Quantum Computation with Constant Error Rate
**"Fault-Tolerant Quantum Computation with Constant Error Rate"**
arXiv: quant-ph/9906129 (originally STOC 1997, full version 1999)
THE original threshold theorem (with Knill-Laflamme-Zurek independently). Proves that if error rate eta < eta_c (a constant), arbitrarily long quantum computation can be performed at polylogarithmic overhead. Uses concatenated CSS codes including novel polynomial codes over F_p. Effective error after r levels: (c*eta)^{2^r} — doubly-exponential suppression. General noise model: probabilistic, decoherence, amplitude damping, depolarization, correlations. Threshold ~10^{-6}. No measurements needed.
**Machines**: chain complex (CSS/polynomial codes), parameterized homology (eta parameterizes family), stability (THE threshold theorem), null hypothesis (uncorrected circuit).
Full annotation: `papers/inbox.md`.
**See also**: `by-structure/phase_transitions.md`

### Knill, Laflamme, Zurek (1998) — Resilient Quantum Computation
**"Resilient Quantum Computation: Error Models and Thresholds"**
arXiv: quant-ph/9702058
Independent proof of the threshold theorem. Uses 7-qubit Steane code (Hamming-based). Concatenation maps p to cp^2; after h levels: c^{2^h-1} p^{2^h}. Explicit threshold calculation from counting minimal failure sets in recovery network (~190K pairs for operational, ~416K for total). Threshold ~3 x 10^{-6} for stochastic errors. Detailed error model taxonomy: independent stochastic, quasi-independent stochastic/monotone. Complete fault-tolerant procedure set via normalizer group.
**Machines**: chain complex (Steane code), parameterized homology (p parameterizes family), stability (threshold theorem), null hypothesis (unencoded network).
Full annotation: `papers/inbox.md`.
**See also**: `by-structure/phase_transitions.md`

### Breuckmann & Eberhardt (2021) — Quantum LDPC Codes
**"Quantum Low-Density Parity-Check Codes"**
arXiv: 2103.06309 | PRX Quantum review
Comprehensive review placing quantum LDPC codes in their homological context. CSS codes ARE chain complexes (partial^2 = 0). Surveys geometric constructions (hyperbolic manifolds, Gauss-Bonnet-Chern), product constructions (hypergraph, tensor, fiber bundle, lifted, balanced — all chain complex operations with Kunneth formula). Gottesman's constant overhead theorem. Systolic geometry: code distance = systole of underlying manifold. Bridge to quantum gravity (holographic codes). The most cross-disciplinary QEC paper.
**Machines**: chain complex (PRIMARY — CSS = chain complex), parameterized homology (code families, systole), stability (Gottesman constant overhead, individual thresholds), null hypothesis (surface code as baseline).
Full annotation: `papers/inbox.md`.
**See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`

---

## Cross-listed from TDA (Wave 7)

- **Hamilton & Leditzky (2023/2024)** — "Probing Multipartite Entanglement Through Persistent Homology." Commun. Math. Phys. 405, article 125. arXiv: 2307.07492. 8 citations. PH applied to multipartite entanglement. Sublevel set filtration by q-deformed total correlation C_q(J) = Σ S_q(v) - S_q(J). Integrated Euler characteristic = n-tangle τ_n at q=2 (resolves Eltschka-Siewert conjecture). Barcodes distinguish SLOCC orbits with identical τ_n (strictly finer). Relative PH gives -I(A:B|R) ≤ 0 by strong subadditivity. Proposes generalization to arbitrary resource theories. Full annotation: `inbox.md` (Wave 7). Machines: joint-vs-marginal, chain complex, parameterized homology, stability, matching, null hypothesis. **See also**: `by-domain/tda.md`, `by-structure/composite_systems.md`.
