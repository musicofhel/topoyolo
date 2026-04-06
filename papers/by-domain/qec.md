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
