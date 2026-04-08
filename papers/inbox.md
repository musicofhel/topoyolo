# Inbox

> Earlier annotations (Waves 1-3) are in [inbox-archive.md](inbox-archive.md).
> Cross-references from other files may point to `inbox.md` for papers now in the archive — check both files.

Full-depth annotations of papers in the topo-rosetta corpus. Each paper is cross-referenced in the dual index (by-domain + by-structure) and relevant atlas files.

---

## Still to find

- ~~Ay, Polani — information decomposition (PID).~~ **Resolved**: The reference was never specific (could be Ay 2015 "Information Geometry" or Polani 2009 "Information Flows in Causal Networks"). PID coverage is now thorough with 8 core PID papers + Kolchinsky 2024 (PID=IB) + Barrett 2015 (Gaussian PID) + Mediano 2019 (PhiID). Any Ay/Polani contribution is subsumed.
- ~~Riehl — "Category Theory in Context."~~ **Skipped**: Textbook, not paper. The abstract machines (functors, natural transformations) are the meta-level formalism that could describe the Rosetta's cross-domain correspondences, but formalizing this would require a dedicated categorical framework beyond the scope of paper annotation.
- ~~Rosas, Mediano, Jensen, Seth, Barrett, Carhart-Harris, Bor (2020)~~ **Annotated** — Full annotation below (Wave 7). Filed in `by-domain/information_theory.md`, `by-domain/neuroscience.md`, `by-structure/composite_systems.md`, `atlas/JOINT_VS_MARGINAL.md`.

---

## Wave 4c: Stability x QEC — Foundational Threshold Theorem Papers (2026-04-06)

---

## quant-ph/9906129 --- Aharonov & Ben-Or (1997/1999)
**"Fault-Tolerant Quantum Computation with Constant Error Rate"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: Uses Calderbank-Shor-Steane (CSS) quantum error correcting codes, which are defined by pairs of classical codes satisfying an orthogonality condition (H_Z H_X^T = 0 mod 2). This IS the chain complex condition: two boundary operators whose composition vanishes. The paper also introduces *polynomial codes* over F_p — a new class of CSS codes where codewords are superpositions of evaluations of random polynomials of degree d over a finite field. The algebraic structure of polynomial codes (degree filtration, evaluation maps) provides a graded chain complex with systematic fault-tolerant procedures derived from the algebraic properties.
- **Parameterized homology**: The error rate eta parameterizes the family. Below the threshold eta_c, the logical error rate is exponentially suppressed via concatenation: after r levels, the effective error is reduced to eta_eff ~ (c * eta)^{2^r}. The threshold eta_c is THE critical value — a phase transition between correctable and uncorrectable regimes. The paper estimates eta_c ~ 10^{-6} for polynomial codes.
- **Stability**: THE foundational stability result for quantum computation. The key theorem: if eta < eta_c, then arbitrarily long quantum computations can be performed with arbitrarily high reliability, at polylogarithmic overhead in space and time. The stability is achieved through recursive concatenation — each level of simulation improves reliability, and the improvement is exponential in the number of levels. The result holds for a very general noise model: probabilistic errors, decoherence, amplitude damping, depolarization, systematic inaccuracies, and even exponentially decaying correlations in space and time.
- **Null hypothesis**: The uncorrected quantum circuit (no error correction) as null. Without error correction, noise accumulates and ruins the computation — the error probability grows with circuit size. The threshold theorem quantifies the gap: with correction, the error can be made arbitrarily small at polylogarithmic cost; without correction, it grows without bound.

**What is genuinely new (not reducible to shared abstraction)**:
- The *constant error rate* threshold. Shor's prior result required the error rate to shrink polylogarithmically with computation size — physically unreasonable. Aharonov & Ben-Or show a CONSTANT threshold suffices. This is the quantum analogue of von Neumann's 1956 result for classical circuits.
- Polynomial codes: a new class of quantum codes where fault-tolerant procedures have a "simple and systematic structure" derived from the algebra of polynomials over finite fields. The degree-reduction step (interpolation on encoded states) has no analogue in other domains.
- No measurements or classical operations required during quantum computation. The quantum model is self-contained — it can be made fault-tolerant within itself. This eliminates the need for classical control, which itself could be noisy.
- Generality of the noise model: works with nearest-neighbor interactions on a 1D line, qupits (p > 2 states), exponentially decaying correlations — far beyond the independent stochastic model.
- The recursive concatenation proof technique: the hierarchical circuit M_r where each qubit becomes a block, each block becomes a block of blocks, etc. The analysis involves tracking "sparse fault paths" through the hierarchy — a combinatorial argument specific to the recursive structure.

**Connections the authors acknowledge**: Cite Knill, Laflamme, Zurek as independent co-discoverers of the threshold theorem. Cite Kitaev's toric code approach as an alternative (topological rather than concatenation-based). Situated entirely within QEC/quantum complexity theory. No connections to TDA, dynamical systems, neuroscience, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Error rate eta | Perturbation magnitude (parameter) |
| Threshold eta_c | Critical value (phase transition) |
| Concatenated code | Hierarchical chain complex (recursive) |
| Polynomial code | Chain complex over F_p (algebraic) |
| CSS code orthogonality H_Z H_X^T = 0 | Chain complex condition (partial^2 = 0) |
| Fault-tolerant procedure | Stability-preserving map |
| Recursive simulation M_r | Hierarchical refinement (r levels of correction) |
| Effective error (c*eta)^{2^r} | Exponential suppression (stability bound) |
| Sparse fault path | Correctable error pattern (element of boundary image) |
| Non-sparse fault path | Uncorrectable error (non-trivial homology class) |
| Block of qubits | Code space (protected subspace) |
| Logical state | Homology class (invariant under correction) |

**See also**: `by-structure/phase_transitions.md`, `by-domain/qec.md`

---

## quant-ph/9702058 --- Knill, Laflamme, Zurek (1998)
**"Resilient Quantum Computation: Error Models and Thresholds"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: Uses the 7-qubit Steane code (based on the classical [7,4,3] Hamming code) as the base code. The Hilbert space decomposes as Q^{tensor 7} = A tensor S, where A is the abstract (logical) qubit and S is the syndrome space. The six stabilizer observables S_1...S_6 (built from tensor products of Pauli operators) define the boundary operators. Syndrome measurement projects onto the code space — analogous to projection onto ker(partial)/im(partial). The normalizer group of the code provides the algebraic structure for encoded operations.
- **Parameterized homology**: Error probability p parameterizes the family. The concatenation procedure maps p to cp^2 at each level (single-error elimination). After h levels of concatenation, the effective error is c^{2^h - 1} p^{2^h}. The threshold p_c = 1/c is the critical value: below it, the doubly-exponential suppression drives the error to zero; above it, concatenation amplifies the error.
- **Stability**: The threshold theorem: if each gate in a physical implementation of a quantum network has error less than p_c, it is possible to perform encoded quantum computations with arbitrary accuracy. The paper provides explicit threshold calculations: ~10^{-6} for independent stochastic errors (p_c ~ 1/f where f ~ 10^6 is the number of minimal failure pairs in the recovery network). The stability result holds for quasi-independent stochastic and monotonic error models — substantially more general than independent errors.
- **Null hypothesis**: The unencoded, uncorrected quantum network as null. The paper explicitly frames the problem as: "the effect of noise will accumulate and ruin the entire computation, and hence the computation must be protected." The gap between encoded (error suppressed) and unencoded (error accumulates) is the value of error correction.

**What is genuinely new (not reducible to shared abstraction)**:
- The explicit construction of fault-tolerant procedures for a COMPLETE set of operations: encoded gates, state preparation, measurement, and error correction — all tolerating single faults. The paper introduces a method for obtaining fault-tolerantly encodable operations using the normalizer group and transversal gates.
- The detailed error model taxonomy: independent stochastic, quasi-independent stochastic, quasi-independent (general), and quasi-independent monotone. Each model makes different assumptions about correlations and boundedness. The threshold analysis applies to each, yielding different constants but the same qualitative result.
- The "error location" and "error expansion" framework: every noisy quantum network can be decomposed as a mixed sum of networks with linear error operators at each error location. This representation is the analytical foundation — it connects physical noise to the algebraic error model.
- The explicit counting of "minimal failure sets" to derive numerical thresholds. The recovery network for the 7-qubit code has ~190,785 operational pairs and ~415,605 total pairs that can cause failure, yielding p_c ~ 3.0 x 10^{-6}.
- The treatment of memory errors (idle qubits accumulate errors) alongside operational errors (gates introduce errors), and the explicit trade-off between parallelism and memory error accumulation.

**Connections the authors acknowledge**: Cite Shor's original fault-tolerance result, Calderbank-Shor-Steane codes, Gottesman's stabilizer formalism, and Kitaev as independent co-discoverer. Acknowledge that Aharonov and Ben-Or independently obtained threshold results. Entirely within QEC. No cross-domain connections.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Error probability p | Perturbation magnitude (parameter) |
| Threshold p_c | Critical value (phase transition) |
| Concatenation level h | Hierarchical depth (refinement scale) |
| Effective error c^{2^h-1} p^{2^h} | Doubly-exponential suppression (stability bound) |
| 7-qubit Steane code | Chain complex (Hamming-based) |
| Abstract particle A | Logical qubit (homology class) |
| Syndrome space S | Error detection space (cokernel) |
| Stabilizer observables S_1...S_6 | Boundary operators (parity checks) |
| Normalizer group | Symmetry group preserving code space |
| Error expansion | Decomposition into localized fault components |
| Error location | Localized perturbation site |
| Minimal failure set | Uncorrectable error pattern (non-trivial cycle) |
| Recovery network | Error correction circuit (projection to code space) |
| Transversal gate | Bitwise operation preserving code structure |

**See also**: `by-structure/phase_transitions.md`, `by-domain/qec.md`

---

## 2103.06309 --- Breuckmann & Eberhardt (2021)
**"Quantum Low-Density Parity-Check Codes"**

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: THE central organizing principle of the paper. CSS codes ARE chain complexes of length three: C_2 --partial_2--> C_1 --partial_1--> C_0, where 1-cells = physical qubits, partial_2 = H_Z (Z-stabilizer checks from faces), partial_1^T = H_X (X-stabilizer checks from vertices), and the CSS orthogonality condition H_Z H_X^T = 0 is EXACTLY partial_1 partial_2 = 0. Logical Z-operators = H_1(C) = ker(partial_1)/im(partial_2). Logical X-operators = H^1(C) = ker(partial_2^T)/im(partial_1^T). Number of logical qubits k = dim H_1. Code distance d = minimum Hamming weight of a non-trivial homology class. The paper systematically exploits this: hyperbolic codes from tessellations of hyperbolic manifolds, where k is determined by the Gauss-Bonnet-Chern theorem relating geometry to topology. Product constructions (hypergraph product, tensor product, fiber bundle, lifted product, balanced product) are ALL operations on chain complexes imported from homological algebra. The Kunneth formula gives the homology of product complexes.
- **Parameterized homology**: Multiple parameterizations. (1) Code family parameters [n, k, d]: as n grows, k and d scale according to the construction. Surface codes: k=1, d~sqrt(n). Hyperbolic surface codes: k~n, d~log(n). Fiber bundle codes: k~n^{3/5}, d~n^{3/5}. (2) The systole sys_i(M) of the underlying manifold parameterizes the distance — connecting code distance to a geometric invariant. (3) Error rate p parameterizes the decodability transition (threshold).
- **Stability**: Multiple stability results at different levels. (1) Gottesman's constant overhead theorem: LDPC codes with constant rate and sufficient error suppression enable fault-tolerant computation with only constant (not growing) overhead. This is the strongest resource-efficiency stability result. (2) Individual code thresholds: hyperbolic surface codes have thresholds under MWPM and union-find decoders; the error suppression below threshold is polynomial in n (not exponential as for concatenated codes, because d ~ log(n)). (3) The systolic geometry connection: the distance is related to the i-systole of the underlying manifold, linking code robustness to a deep geometric invariant.
- **Null hypothesis**: The surface code serves as the implicit null/baseline throughout. Every new construction is benchmarked against the surface code's parameters: k=1, d~sqrt(n), threshold ~1%. LDPC codes are judged by how far they exceed this baseline in encoding rate, distance scaling, or overhead. The "good code" question — whether quantum LDPC codes with k ~ n and d ~ n exist — is framed as the open problem of achieving what classical random LDPC codes achieve trivially.

**What is genuinely new (not reducible to shared abstraction)**:
- The taxonomy of product constructions on chain complexes IS a contribution to the Rosetta. Hypergraph product, tensor product, fiber bundle codes, lifted product, balanced product — these are all operations that take chain complexes (classical or quantum codes) and produce new chain complexes with predictable homological properties. The Kunneth formula, fiber bundle twisting, and balanced product are concrete tools for combining chain complexes across contexts.
- The systolic geometry connection: code distance = systole of the underlying manifold. The systole is the shortest non-contractible submanifold — a purely geometric quantity. This bridges QEC to Riemannian geometry in a precise, theorem-level way.
- The asymptotic gap between classical and quantum LDPC codes: random classical LDPC codes are good (k ~ n, d ~ n) but random quantum LDPC codes fail (the orthogonality constraint H_Z H_X^T = 0 cannot be satisfied randomly). This asymmetry has no classical analogue and is intrinsic to quantum mechanics.
- Gottesman's constant overhead theorem — the result that LDPC codes can reduce fault-tolerance overhead to a CONSTANT — is qualitatively different from concatenation-based thresholds (which give polylogarithmic overhead). This is a resource-efficiency result with no analogue in TDA or other domains.
- The connection to quantum gravity via holographic codes and the AdS/CFT correspondence (Section VII). Quantum LDPC codes serve as toy models for holographic quantum gravity — a bridge to fundamental physics.

**Connections the authors acknowledge**: Extensive connections to classical coding theory (Sipser-Spielman expander codes, Shannon capacity, Tanner graphs). Explicit connections to algebraic topology (homological algebra, chain complexes, Kunneth formula), differential geometry (hyperbolic manifolds, Gauss-Bonnet-Chern), systolic geometry, and even quantum gravity (holographic codes). This is one of the most cross-disciplinary papers in QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| CSS code | Chain complex of length 3 over F_2 |
| Parity check matrix H_X, H_Z | Boundary operators partial, partial^T |
| Orthogonality H_Z H_X^T = 0 | Chain complex condition (partial^2 = 0) |
| Logical operator | Non-trivial homology/cohomology class |
| Code distance d | Min-weight non-trivial cycle (systole) |
| Number of logical qubits k | dim H_1 (Betti number) |
| LDPC condition | Bounded degree (local constraint on chain complex) |
| Hypergraph/tensor product | Product of chain complexes (Kunneth) |
| Fiber bundle code | Twisted product of chain complexes |
| Systole sys_i(M) | Shortest non-contractible i-submanifold |
| Gauss-Bonnet-Chern theorem | Geometry-to-topology correspondence (k from curvature) |
| Tanner graph | Bipartite representation of chain complex |
| Surface code | Chain complex on T^2 (baseline) |
| Good code (k ~ n, d ~ n) | Optimal scaling of homological invariants |
| Constant overhead (Gottesman) | Stability with bounded resource cost |

**See also**: `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`, `by-domain/qec.md`

---

## DOI: 10.1016/0167-2789(92)90102-S --- Theiler, Eubank, Longtin, Galdrikian, Farmer (1992)
**"Testing for nonlinearity in time series: the method of surrogate data"**
Published in Physica D, vol. 58, pp. 77--94.

**Domain(s)**: Dynamical systems

**Abstract machines instantiated**:
- **Null hypothesis**: THIS is the foundational instantiation of the null machine in dynamical systems. The paper introduces a systematic framework: generate surrogate time series that satisfy a specific null hypothesis (linear stochastic process), then test whether the original data's nonlinear properties are statistically distinguishable from the surrogates. Three algorithms define three null hypotheses of increasing sophistication:
  - **Algorithm 0 (random shuffle)**: Destroys ALL temporal correlations. Preserves only the amplitude distribution (histogram). Null: the data are IID draws from a fixed distribution. This is the weakest null — rejecting it only establishes that temporal order matters at all.
  - **Algorithm 1 (phase randomization)**: Randomizes the phases of the Fourier transform while preserving the amplitudes. Preserves the power spectrum (and hence the autocorrelation function). Destroys all phase relationships between Fourier components. Null: the data are generated by a linear Gaussian process (stationary, with the observed power spectrum). Rejecting this null establishes nonlinearity in the generating process.
  - **Algorithm 2 (AAFT — Amplitude Adjusted Fourier Transform)**: Preserves BOTH the power spectrum AND the amplitude distribution of the original data. Null: the data are a static monotonic nonlinear transformation of a linear Gaussian process. This is the strongest null — rejecting it rules out the possibility that apparent nonlinearity is merely a measurement artifact (nonlinear observation function applied to linear dynamics).
  Each algorithm is a precise choice of what to destroy (phase correlations, nonlinear dynamics) and what to preserve (power spectrum, amplitude distribution). The preserved quantities define the null; the destroyed quantities are what the test is sensitive to.
- **Stability**: The properties preserved by each surrogate algorithm are stability invariants — they survive the surrogate transformation by construction. The power spectrum is invariant under Algorithm 1 (phase randomization preserves Fourier amplitudes exactly). The amplitude distribution is invariant under Algorithm 2 (the amplitude adjustment step restores the original marginal distribution). These are engineered invariances: the surrogate construction is designed so that specific statistical properties are EXACTLY preserved, making the null hypothesis precise. The robustness of the test itself is also a stability question: the rank-ordering significance test (comparing the original's test statistic to the surrogate distribution) is nonparametric and does not assume a specific distribution for the test statistic.
- **Joint-vs-marginal excess** (weak): Phase relationships between Fourier components represent joint structure — the relative timing and coherence of different frequency modes. Phase randomization (Algorithm 1) destroys this joint structure while preserving the marginal spectral properties (the power at each frequency). A significant test result means the original time series contains joint phase structure absent from the phase-randomized surrogates. This is precisely the joint-vs-marginal pattern: the marginal (power spectrum) is preserved, but the joint (phase coherence) is destroyed, and the test measures the excess.
- **Parameterized homology** (weak): The test statistic (correlation dimension, Lyapunov exponent, prediction error, or any other nonlinear measure) defines a scalar computed on both the original and each surrogate. The ensemble of surrogate values parameterizes a distribution under the null. The original's value is compared to this distribution — significance is determined by where the original falls in the null distribution's ranking. This is a parameterized family (indexed by the surrogate ensemble) where the invariant (the test statistic) is tracked to detect departure from the null.

**What is genuinely new (not reducible to shared abstraction)**:
- The METHOD itself: a principled, algorithmic framework for hypothesis testing in nonlinear dynamics. Before this paper, claims of chaos/nonlinearity in experimental data were often unfalsifiable — there was no systematic way to test whether observed nonlinear signatures were genuine or artifacts of finite data, colored noise, or nonlinear measurement functions. The surrogate data method provided the first rigorous statistical framework.
- The hierarchy of null hypotheses (Algorithm 0 < Algorithm 1 < Algorithm 2) is a taxonomy of "levels of linearity" — each successive algorithm preserves more structure, making the null harder to reject and the conclusion stronger. This graded approach to null construction has no direct analogue in other domains' null models.
- The identification that AAFT (Algorithm 2) addresses the specific pitfall of nonlinear observation functions: a linear system observed through a static nonlinearity (e.g., a diode, a saturating sensor) will appear nonlinear. Algorithm 2 accounts for this by preserving the amplitude distribution, which encodes the observation function's effect.
- The practical diagnostics: the paper demonstrates that correlation dimension and Lyapunov exponent estimates on surrogates can expose spurious claims of chaos in experimental data (sunspot numbers, measles epidemics, white noise). This had immediate impact on the field — many prior claims of low-dimensional chaos were subsequently overturned using surrogate testing.
- The connection to bootstrap and permutation testing in classical statistics, but adapted to the specific structure of time series (where temporal order is the structure being tested).

**Connections the authors acknowledge**: Cite Grassberger-Procaccia (correlation dimension), Wolf et al. (Lyapunov exponents), Takens embedding. Acknowledge the connection to classical hypothesis testing and bootstrap methods (Efron). No connections to TDA, QEC, or information theory — the paper is situated entirely within nonlinear dynamics / time series analysis.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Surrogate time series | Null realization (sample from the null distribution) |
| Algorithm 0 (random shuffle) | Strongest structure destruction (destroys all temporal order) |
| Algorithm 1 (phase randomization) | Selective structure destruction (destroys phase, preserves spectrum) |
| Algorithm 2 (AAFT) | Minimal structure destruction (preserves spectrum + amplitude distribution) |
| Power spectrum preservation | Stability invariant of the surrogate transformation |
| Amplitude distribution preservation | Stability invariant (marginal) |
| Phase relationships | Joint structure (between Fourier components) |
| Test statistic (correlation dimension, etc.) | Diagnostic scalar (compared across null ensemble) |
| Rank-ordering significance | Nonparametric p-value from surrogate ensemble |
| Null hypothesis: linear stochastic process | The reference model (what surrogates instantiate) |
| Nonlinear observation function | Static monotonic transformation (Algorithm 2 accounts for this) |
| Rejection of null | Evidence for genuine nonlinear dynamics |

---

## 2209.13581 --- Berry, Su, Gyurik, King, Basso, Del Toro Barba, Rajput, Wiebe, Dunjko, Babbush (2023)
**"Analyzing Prospects for Quantum Advantage in Topological Data Analysis"**
PRX Quantum 4, 040349 (2023)

**Domain(s)**: TDA, QEC (quantum algorithms)

**Abstract machines instantiated**:
- **Chain complex**: The paper works directly with the simplicial chain complex of the clique complex of a graph G. The boundary operator dG_k maps k-simplices to (k-1)-simplices. The combinatorial Laplacian Delta^G_{k-1} = dG^{dagger}_{k-1} dG_{k-1} + dG_k dG^{dagger}_k is the central object. The Betti number beta_{k-1} = dim(ker(Delta^G_{k-1})) is the quantity to be estimated. The Dirac operator BG = dG + dG^{dagger} is constructed; BG^2 is block-diagonal with the combinatorial Laplacian in the middle block. The quantum algorithm projects onto ker(BG) restricted to the k-chain subspace H^G_k. This is the chain complex in its purest computational form: boundary operators, their adjoints, and the kernel/image structure ARE the computation.
- **Parameterized homology**: TWO distinct parameterizations. (1) The standard TDA filtration: the distance scale epsilon determines which simplices exist in the clique complex, and Betti numbers are tracked as epsilon varies (persistent homology). The paper explicitly discusses this as the motivating application. (2) The dimension k itself is a parameter: the complexity of computing beta_k grows exponentially in k classically (the number of k-cliques can be C(n,k)), but the quantum algorithm's complexity is polynomial in k. The quantum advantage IS the ability to probe high-dimensional homology efficiently.
- **Matching**: The dequantization argument uses a random walk on k-simplices (a Markov chain whose stationary distribution is uniform over k-cliques). The mixing time of this walk is governed by the spectral gap gamma_M of the transition matrix. This spectral approach to sampling k-simplices is structurally related to matching: the random walk must find and connect cliques, which is an assignment problem between vertices. The MWPM decoder in QEC syndrome matching has a structural parallel here: both solve assignment problems on combinatorial structures derived from chain complexes.
- **Stability**: The paper establishes that quantum advantage is robust only under specific parameter regimes: (1) the Betti number must grow asymptotically for super-quadratic speedup, (2) exponentially large dimension AND Betti number are necessary but insufficient for super-polynomial advantage. The dequantization result is itself a stability analysis: it asks how robust the quantum advantage is to the existence of classical competitors. The answer is that advantage is fragile --- it requires very specific parameter regimes (large beta_k, large spectral gap lambda_min, specific graph families). This is a meta-stability result: the computational advantage is not topologically robust; it depends sensitively on problem parameters.
- **Null hypothesis**: The dequantization serves as the null. The classical random-walk algorithm (Monte Carlo sampling of k-simplices) is the "structureless" baseline. The quantum advantage is measured as the gap between quantum and classical complexity. The paper shows this gap can be superpolynomial for specifically constructed graph families (dense random graphs with parameters tuned for large Betti numbers) but may collapse for generic instances. The naive classical algorithm (enumerate all k-cliques, compute nullity) with complexity O(C(n,k)) is the strongest null; the Monte Carlo dequantization is a weaker null that narrows the advantage.

**What is genuinely new (not reducible to shared abstraction)**:
- The paper is the first to compile a quantum TDA algorithm to a fault-tolerant gate set with explicit constant factors. The Toffoli complexity (tens of billions of Toffolis for classically intractable instances) places quantum TDA in the resource landscape between quantum chemistry and Shor's algorithm. This resource estimation has no analogue in the abstract machine framework.
- The dequantization result (classical Monte Carlo algorithm for Betti number estimation) is genuinely new: it shows that the quantum advantage for TDA is NOT simply a consequence of the exponential size of the chain complex. The mixing time of the classical random walk (governed by the spectral gap of the transition matrix on k-simplices) is the key quantity that determines whether classical algorithms can compete. This creates a nuanced landscape: quantum advantage exists in a narrow regime where the chain complex is large but the classical random walk mixes slowly.
- The specific graph families constructed for super-polynomial advantage (dense random graphs with parameters n, k ~ n/2, degree ~ n/2) are novel mathematical objects. They demonstrate that the regime of quantum advantage is non-empty but highly constrained.
- Kaiser-window amplitude estimation, Chebyshev polynomial eigenvalue projectors, and Dicke state preparation via inequality testing are algorithmic innovations specific to quantum computing with no classical or topological analogue.
- The key insight that super-quadratic speedup requires MULTIPLICATIVE error estimation (relative error in beta_k) rather than additive error in the normalized Betti number. This distinction between error types is a computational refinement absent from the abstract stability concept.

**Connections the authors acknowledge**: Explicitly connect quantum algorithms (QEC/quantum computing) to TDA (simplicial homology, Betti numbers, persistent homology). This is a DIRECT TDA-QEC bridge paper: the quantum algorithm computes TDA invariants. The authors cite Lloyd et al.'s original quantum TDA algorithm, Gyurik et al.'s DQC1-hardness results, and the dequantization literature. They acknowledge that the chain complex structure is shared between TDA and the quantum algorithm. They do NOT connect to dynamical systems, neuroscience, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Clique complex of graph G | Simplicial complex (the space) |
| Boundary operator dG_k | Boundary operator ∂ |
| Combinatorial Laplacian Delta^G_{k-1} | Hodge Laplacian L_k (up/down components) |
| Dirac operator BG = dG + dG^{dagger} | ∂ + ∂^{dagger} (Dirac = boundary + coboundary) |
| Betti number beta_k | dim(ker(L_k)) = k-th homological feature count |
| Kernel projector | Projection onto harmonic space (homology representatives) |
| Distance scale epsilon | Filtration parameter |
| Persistent homology | Parameterized homology (tracking beta_k(epsilon)) |
| Dequantization | Classical null algorithm (Monte Carlo on k-simplices) |
| Spectral gap lambda_min | Gap of combinatorial Laplacian (separation of harmonic from non-harmonic) |
| Toffoli complexity | Computational resource (fault-tolerant gate count) |
| Multiplicative error in beta_k | Relative perturbation size (stability metric) |
| Dense random graph family | Specific problem instance in the advantage regime |
| Quantum walk operator | Block encoding of Dirac/boundary operator |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `cross_domain_bridges.md`

---

## 2107.02194 --- Hastings, Haah (2021)
**"Dynamically Generated Logical Qubits"**
arXiv: 2107.02194

**Domain(s)**: QEC

**Abstract machines instantiated**:
- **Chain complex**: The honeycomb code is defined on a hexagonal lattice with qubits on vertices and two-qubit Pauli checks on edges. When viewed as a subsystem code, the product of checks along any 1-cycle on the lattice is a stabilizer. Plaquette stabilizers correspond to homologically trivial cycles (boundaries); logical operators correspond to homologically non-trivial cycles on the torus (H_1(T^2, Z/2)). The stabilizer group has dimension n_p + 1, the gauge group 3n_p - 1, leaving n_p - 1 gauge qubits and ZERO logical qubits as a static subsystem code. The chain complex is the standard cellular chain complex of the honeycomb lattice: 0-cells (vertices/qubits), 1-cells (edges/checks), 2-cells (hexagonal plaquettes/stabilizers). The boundary operator maps edges to their endpoint vertices; the stabilizer condition (product of checks on a boundary = identity) is exactly del^2 = 0.
- **Parameterized homology**: THE key machine. Time (measurement round r) parameterizes the code. The instantaneous stabilizer group (ISG) S(r) changes with each measurement round in a period-3 cycle (r mod 3 determines which edge type is measured). But the DYNAMICS of logical operators has period 6: after one period of 3 rounds, every electric logical operator maps to a parallel magnetic operator and vice versa; after 6 rounds, they return to themselves. The ISG at each time step defines a different instantaneous code, but the logical information is encoded in the ORBIT of the ISG under the periodic measurement schedule --- not in any single snapshot. This is deeply analogous to Floquet theory in dynamical systems: the stroboscopic map (ISG after one full period) defines the "Floquet multipliers" of the code, and the logical qubits live in the persistent eigenspace of this map. The period-6 dynamics of logical operators (electric <-> magnetic automorphism with period 6 despite period-3 measurements) is a non-trivial monodromy: the codespace does not return to itself after one measurement period, only after two.
- **Stability**: Error correction is possible despite the time-varying code. The syndrome bits (eigenvalues of plaquette stabilizers) form a lattice in 2+1 dimensional spacetime with basis vectors s_1, s_2, s_3 that span a structure isomorphic to a simple cubic lattice (after bipartition into two congruent sublattices). Standard MWPM decoding on this spacetime lattice achieves fault tolerance: below a threshold error rate, logical errors are exponentially suppressed with system size. The stability result is that the dynamical code protects information as well as the static toric code despite never having a fixed codespace. Each individual measurement round has no protection (the subsystem code has zero logical qubits); protection emerges only from the SEQUENCE.
- **Null hypothesis**: The static subsystem code (ignoring measurement order) serves as the null. This null has zero logical qubits --- no information protection at all. The Floquet structure (specific periodic measurement schedule) is the structure that must be added to create protection. The gap between null (0 logical qubits) and Floquet code (2 logical qubits with distance proportional to linear system size) is maximal: the dynamical structure creates protection from nothing. A secondary null is the static toric code: it protects the same 2 logical qubits but requires 4-qubit measurements. The honeycomb Floquet code achieves the same protection with only 2-qubit measurements, at the cost of requiring a specific temporal schedule.
- **Matching**: The fault-tolerant decoder uses MWPM on the spacetime syndrome lattice. Syndrome defects (violations of plaquette stabilizer eigenvalues between consecutive rounds) are matched in the 2+1D spacetime lattice. The matching cost is the spacetime distance between defects. This is the standard QEC matching machine, but lifted to spacetime: the matching is not just spatial (as in static toric code decoding) but spatiotemporal (defects at different times and locations are matched).

**What is genuinely new (not reducible to shared abstraction)**:
- The concept of DYNAMICALLY GENERATED logical qubits: a code that has zero logical qubits as a static object but generates protected logical qubits through a specific periodic measurement schedule. This is fundamentally new --- there is no TDA analogue where a simplicial complex has trivial homology but gains non-trivial homology through a specific sequence of operations. The closest analogue would be a time-varying filtration where the complex at each time step is contractible but the periodic orbit of complexes has non-trivial topology. This does not exist in standard TDA.
- The period-6 automorphism of logical operators (electric <-> magnetic exchange): after 3 measurement rounds, the ISG returns (up to signs) but logical operators undergo a non-trivial permutation. This 6/3 period ratio is a form of monodromy --- the logical information picks up a phase (here, an operator permutation) when transported around one period of the driving schedule. This is structurally identical to Berry phase / holonomy in quantum mechanics or monodromy in dynamical systems, but applied to the codespace itself.
- The Majorana fermion perspective: the honeycomb code maps (via Jordan-Wigner) to free Majorana fermions on a honeycomb lattice, with the gauge field structure of Kitaev's honeycomb model. The inner logical operators transport FERMIONS (their commutation relations show fermionic statistics), while outer logical operators transport BOSONS (e and m anyons). This anyon content is a domain-specific structure with no analogue in TDA or information theory.
- The measurement-only quantum computation aspect: no unitary gates are applied; all dynamics come from 2-qubit Pauli measurements. The logical information is maintained purely by the pattern of measurements. This is a new computational paradigm with no classical analogue.
- The spacetime syndrome lattice structure: syndrome bits in 2+1D spacetime form a lattice spanned by vectors that, after bipartition, give two copies of the simple cubic lattice. This specific geometric structure is engineered for MWPM decoding efficiency.

**Connections the authors acknowledge**: Cite Kitaev's toric code (the static QEC chain complex they generalize), the subsystem code framework (Poulin, Bacon-Shor, Bombin-Martin-Delgado color codes), and Kitaev's honeycomb model (the condensed matter Hamiltonian whose measurement-based analogue they construct). Situated entirely within QEC. No connections to TDA, dynamical systems, or information theory. The Floquet analogy (periodic driving) is implicit but not acknowledged --- the authors do not use the term "Floquet" in the original paper (the name was given by the community).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Honeycomb lattice | The space (cellulation) |
| Two-qubit Pauli check | Local constraint (edge measurement) |
| Gauge group | Full group generated by local constraints |
| Stabilizer group | Center of gauge group (global constraints = boundaries) |
| Instantaneous stabilizer group S(r) | Snapshot of the chain complex at time r |
| Measurement round r mod 3 | Parameterization variable (discrete time) |
| Period-3 ISG cycle | Periodic orbit of the code complex |
| Period-6 logical operator dynamics | Monodromy of the parameterized family |
| Logical qubit (dynamically generated) | Homology class (emergent from periodic orbit, not from any snapshot) |
| Plaquette stabilizer | Boundary (product of checks on contractible cycle = identity) |
| Non-trivial cycle on torus | Non-trivial homology class (logical operator) |
| Syndrome bit | Cycle violation (departure from del^2 = 0) |
| Spacetime syndrome lattice | 2+1D chain complex for decoding |
| MWPM decoder | Optimal matching on syndrome defects |
| Electric/magnetic logical operators | Dual homology classes (H_1 vs cohomology) |
| Fermion (inner logical operator) | Odd element under exchange (fermionic statistics) |
| Code distance ~ L | Minimum-weight non-trivial cycle (robustness scale) |
| Zero static logical qubits | Trivial static homology (null) |
| Two dynamical logical qubits | Non-trivial dynamical homology (Floquet-generated) |

**See also**: `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-domain/qec.md`

**See also**: `by-structure/phase_transitions.md`, `by-domain/dynamical_systems.md`

---

## 1909.02297 --- Mediano, Rosas, Carhart-Harris, Seth, Barrett (2019)
**"Beyond integrated information: A taxonomy of information dynamics phenomena"**

**Domain(s)**: neuroscience, information theory

**Abstract machines instantiated**:
- **Chain complex**: The double-redundancy lattice is a product lattice A x A with 16 nodes, ordered by the PID partial order on source/target subsets. The Moebius inversion on this lattice defines the 16 PhiID atoms, exactly as PID uses Moebius inversion on the single redundancy lattice. The lattice is the algebraic scaffold; the atoms are the "homology" of the information structure.
- **Parameterized homology**: The PhiID atoms can be computed for different time lags, system sizes, noise levels, or redundancy function choices. The paper shows that existing integration measures (Phi_WMS, psi, Phi_G, CD) are different projections of the same 16-atom lattice --- they are different "slices" of a parameterized family, analogous to how different filtration thresholds reveal different persistent features.
- **Joint-vs-marginal excess**: THE central object. PhiID decomposes the excess entropy E = I(X1,X2; Y1,Y2) into 16 atoms that distinguish HOW joint information exceeds marginal information. Synergistic atoms (those involving {12} in source or target) are the information present in the composite system but absent from any component. The paper's key insight: what IIT calls "integration" is actually an aggregate of synergy, transfer, storage, copy, erasure, upward causation, and downward causation --- all distinct modes of joint-vs-marginal excess.
- **Null hypothesis**: Independent subsystems (Phi = 0) is the explicit null. The partitioned system where X1,X2 evolve independently is the baseline against which all 16 atoms are measured. The paper also constructs specific null systems (copy-transfer, downward-XOR, parity-preserving-random) that each have Phi_WMS = 1 but with different non-zero atoms --- showing the null model is insufficient to distinguish qualitatively different integration modes.
- **Stability**: The corrected Phi_WMS,c (which adds back the double-redundancy term to avoid negativity) is more robust across noise correlation levels than the standard Phi_WMS. The paper demonstrates that Phi_WMS goes negative in highly redundant systems, while the corrected version tends to 0 --- a stability improvement.

**What is genuinely new (not reducible to shared abstraction)**:
- The 6-category taxonomy of information dynamics (storage, copy, transfer, erasure, downward causation, upward causation) is genuinely new. These are not just different names for joint-vs-marginal excess --- they are structurally distinct modes of how information moves through a multivariate process across time. No other Rosetta domain has this fine-grained temporal decomposition.
- Upward causation (individual past states determining collective future) and downward causation (collective past determining individual futures) are formally distinguished for the first time. These are directional modes of joint-vs-marginal excess that have no direct analogue in TDA, QEC, or standard dynamical systems.
- The demonstration that Phi_WMS, psi, Phi_G, and CD each capture different subsets of the 16 PhiID atoms (Table I) is a meta-result about integration measures themselves, not about any specific system.
- Synergistic storage I_partial({12}->{12}) --- information that is jointly encoded in both past variables and jointly decodable only from both future variables --- had not been reported before this paper.

**Connections the authors acknowledge**: The paper explicitly bridges IIT (Tononi) and PID (Williams & Beer), unifying them into PhiID. They cite Lizier's "information modification" as a precursor to their 6-category taxonomy. They note connections to Granger causality and causal density but do not acknowledge parallels to TDA, QEC, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Excess entropy E | Joint-vs-marginal excess (total) |
| PhiID atom | Information atom (decomposed excess) |
| Double-redundancy lattice | Chain complex (product lattice with Moebius inversion) |
| Redundancy function Red(.) | Overlap measure (common information in components) |
| Synergy Syn(X1,X2; Y1Y2) | Joint-vs-marginal excess (synergistic component) |
| Integrated information Phi | Scalar summary of joint-vs-marginal excess |
| Partitioned system (Phi=0) | Null hypothesis (independent subsystems) |
| Upward causation | Individual-to-collective information flow |
| Downward causation | Collective-to-individual information flow |
| Information storage | Self-predictive information (same variable, past to future) |
| Transfer entropy | Directed information flow (unique cross-variable prediction) |

**See also**: `by-structure/composite_systems.md`, `by-domain/neuroscience.md`, `by-domain/information_theory.md`

---

## 1411.2832 --- Barrett (2015)
**"Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems"**

**Domain(s)**: information theory, neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The entire paper is about decomposing I(X; Y, Z) into redundancy R, unique information U, and synergy S --- and synergy IS the joint-vs-marginal excess: S(X; Y, Z) = information about X present in (Y,Z) jointly that is absent from Y alone and Z alone. The key result: for Gaussian systems with univariate target, a broad class of PIDs all reduce to the MMI (Minimum Mutual Information) PID where R = min{I(X;Y), I(X;Z)}, making synergy = extra information from the weaker source given the stronger. The paper's WMS = I(X;Y,Z) - I(X;Y) - I(X;Z) = S - R is the net joint-vs-marginal excess.
- **Parameterized homology**: The paper systematically varies three parameters: (i) correlation coefficients a, b, c between the three Gaussian variables; (ii) time lag (1-lag vs infinite-lag pasts in dynamical systems); (iii) connection strengths alpha, gamma, rho in MVAR models. For each parameter setting, the PID atoms change, creating a parameterized family. The key finding: net synergy at 1-lag is always >= net synergy at infinite lag for order-1 MVAR systems (Eq. 96), because restricted regressions on infinite pasts reduce apparent synergy.
- **Null hypothesis**: The product of marginals (Y independent of Z) is the baseline null. The paper shows the surprising result that net synergy can be positive even when the two sources are uncorrelated (b=0), violating the naive intuition that synergy requires source correlation. The "information as variance reduction" alternative (WMS_Sigma) gives zero synergy when sources are uncorrelated, highlighting that the nonlinearity of the log in Shannon information creates synergy absent from the linear (variance) measure.
- **Stability**: The MMI PID has a remarkable stability property: redundancy R_MMI = min{I(X;Y), I(X;Z)} is completely independent of the correlation between sources. Only synergy depends on the full joint distribution. This factorization is a robustness result --- redundancy is stable under perturbations to the source-source relationship. The paper also shows that synergy is a monotonically increasing function of the weaker connection strength and monotonically decreasing with source correlation (Eq. 110), giving predictable perturbation behavior.

**What is genuinely new (not reducible to shared abstraction)**:
- The proof that ALL PIDs satisfying the marginal-dependence property collapse to MMI for Gaussian systems with univariate target is a universality result specific to the Gaussian structure. This has no analogue in TDA or QEC --- it says the information-theoretic decomposition is uniquely determined by the domain's distributional assumptions.
- The distinction between Shannon information (log of variance ratio) and variance-based information (I_Sigma = variance difference) reveals that synergy in Gaussian systems is partly an artifact of the logarithm's concavity. WMS_Sigma = 0 when sources are uncorrelated, but WMS > 0. This is a genuinely domain-specific insight about how the choice of information measure affects the decomposition.
- The infinite-lag vs 1-lag comparison (synergy decreases with more history) is a temporal effect with no direct TDA or QEC analogue. It arises because restricted regressions on longer histories capture more variance, reducing the apparent excess from knowing both sources.
- The proposed "synergistic complexity" measure SC (Eq. 134) as an alternative to causal density and Phi is new, measuring the average excess synergy in a system of n variables.

**Connections the authors acknowledge**: Explicitly discusses implications for neuroscience (neural coding, EEG connectivity, epilepsy, consciousness). Cites Granger causality literature and its equivalence to transfer entropy for Gaussians. Notes that net synergy has been observed in intracranial EEG during epileptic seizures and in information transfer between neural variables. Does NOT cite TDA, QEC, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Synergy S(X; Y, Z) | Joint-vs-marginal excess (synergistic atom) |
| Redundancy R(X; Y, Z) | Common information in components |
| Whole-Minus-Sum WMS | Net joint-vs-marginal excess (synergy minus redundancy) |
| MMI PID (Minimum Mutual Information) | Canonical decomposition for Gaussian composites |
| Partial covariance Sigma(X|Y) | Conditional structure (residual after marginal removed) |
| Net synergy | Excess of joint over sum of marginals |
| Transfer entropy | Directed joint-vs-marginal excess |
| Causal density | Average pairwise transfer (double-counts synergy) |
| Synergistic complexity SC | Average joint-vs-marginal excess per triplet |
| Granger causality F | Variance-ratio directed information flow |

**See also**: `by-structure/composite_systems.md`, `by-domain/information_theory.md`, `by-domain/neuroscience.md`

---

## Wave 5 — Match x Neuro (2026-04-06)

Papers filling the weakest cell in the 6x5 coverage matrix: Matching machine instantiated in Neuroscience. All three use optimal transport as the core algorithmic mechanism applied to neural data.

---

## 2206.09398 --- Thual, Tran, Zemskova, Courty, Flamary, Dehaene, Thirion (2022)
**"Aligning individual brains with Fused Unbalanced Gromov-Wasserstein"**

**Domain(s)**: Neuroscience (neuroimaging, fMRI), TDA (optimal transport)

**Abstract machines instantiated**:
- **Matching**: The central contribution. FUGW computes an optimal transport plan P in R^{n x p} between cortical vertices of two subjects. The plan is a soft assignment matrix that matches vertices across brains. The loss has three terms: (1) Wasserstein loss L_W(P) matching vertices with similar functional features, (2) Gromov-Wasserstein loss L_GW(P) penalizing changes in pairwise geodesic distance structure (second-order matching), and (3) unbalanced KL marginal relaxation allowing functional areas to differ in size across subjects. The parameter alpha interpolates between feature-based and geometry-based matching. This is a genuine optimal assignment problem: minimize total cost of transporting mass from source cortical surface to target cortical surface, subject to structural constraints.
- **Stability**: The unbalanced feature (parameter rho) provides robustness: areas where signal or geometry differ too much between subjects simply transport less mass rather than forcing a bad match. The method is shown to be robust to noise and inter-individual anatomical variability. Alignment quality degrades gracefully as brain differences increase.
- **Parameterized homology**: The parameter alpha traces a family of alignments from pure feature matching (alpha=0) to pure geometry preservation (alpha=1). The optimal alpha (selected on validation data) reveals the relative importance of functional vs anatomical structure. The training set size (number of fMRI contrasts) also parameterizes alignment quality.
- **Null hypothesis**: Baseline alignment via FreeSurfer anatomical co-registration (fsaverage5) serves as the null. FUGW alignment significantly increases between-subject correlation of held-out functional data compared to this anatomical-only baseline. MSM (multimodal surface matching) serves as the primary competing method.

**What is genuinely new (not reducible to shared abstraction)**:
- The fusion of Wasserstein and Gromov-Wasserstein in a single objective is domain-specific: it encodes the neuroscience insight that functional alignment should respect cortical geometry (nearby cortical areas should map to nearby areas). This is not just OT; it is OT constrained by the Riemannian geometry of the cortical sheet.
- Unbalanced transport handles the biological fact that homologous functional areas differ in size across individuals. This is a neuroscience-specific constraint absent from standard OT in TDA or QEC.
- The method is landmark-free and whole-brain, unlike hyperalignment (Haxby) which requires ROI selection or stimulus-driven alignment. FUGW discovers the alignment from data geometry alone.
- Applied to the Individual Brain Charting dataset (12 subjects, 400 fMRI maps each), demonstrating that OT-based alignment captures fine-grained functional organization invisible to anatomy-based methods.

**Connections the authors acknowledge**: Cite Haxby hyperalignment and Procrustes-based methods as predecessors but note they require stimulus labels (supervised). Cite Gromov-Wasserstein literature (Memoli, Peyre, Vayer) for the mathematical framework. Do NOT cite TDA/PH literature --- the connection to persistence diagram matching is implicit but unacknowledged.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transport plan P | Optimal assignment / matching |
| Wasserstein loss L_W | Feature-based matching cost |
| Gromov-Wasserstein loss L_GW | Second-order (structure-preserving) matching cost |
| Fused loss (alpha) | Parameterized family of matchings |
| Unbalanced (rho) | Robustness / partial transport |
| Marginal relaxation (KL) | Soft constraint on matching completeness |
| Sinkhorn iterations | Matching algorithm (entropic regularization) |
| Cortical vertex | Feature point |
| Functional signature | Feature vector |
| Geodesic distance matrix D | Cost matrix |
| FreeSurfer baseline | Null model (anatomy-only alignment) |

**See also**: `by-structure/optimal_transport.md`, `by-domain/neuroscience.md`

---

## 1902.04812 --- Janati, Bazeille, Thirion, Cuturi, Gramfort (2019)
**"Group level MEG/EEG source imaging via optimal transport: minimum Wasserstein estimates"**

**Domain(s)**: Neuroscience (MEG/EEG source imaging), TDA (optimal transport)

**Abstract machines instantiated**:
- **Matching**: The core innovation. Minimum Wasserstein Estimates (MWE) define a multi-task regression penalty Omega using unbalanced optimal transport. For S subjects, the penalty is: Omega = mu * min_{x-bar} sum_s W(x^(s), x-bar) + lambda * ||x^(s)||_1, where W is the unbalanced Wasserstein distance on the cortical source space and x-bar is the Wasserstein barycenter. The cost matrix M_ij is the geodesic distance between cortical vertices i and j. The transport plan matches source activations across subjects: it finds the minimum-cost assignment of neural current dipoles from each subject to a common "average" source pattern, where cost respects cortical geometry. This is OT-as-regularizer: the matching constrains the inverse problem to prefer solutions where different subjects' sources are nearby on the cortex.
- **Stability**: MWE infers per-subject noise standard deviation sigma^(s) jointly with sources. This makes the method robust to varying signal-to-noise ratios across subjects --- a practical stability guarantee. The unbalanced formulation (KL marginal relaxation with parameter gamma) prevents forcing mass transport when source amplitudes differ. Reduces localization error from ~4 cm (Lasso) to <1 cm.
- **Null hypothesis**: Independent Lasso (L1 regularization per subject, no cross-subject coupling) serves as the baseline. Group Lasso (L21 norm forcing identical source locations) is the rigid null. MWE outperforms both, demonstrating that OT-based spatial proximity is the right prior --- neither independence nor identity.
- **Parameterized homology**: The number of subjects S parameterizes the estimation quality. As S increases from 2 to 16, MWE's AUC rises from ~0.6 to ~0.9 --- more subjects make the inverse problem better-posed. The regularization parameters (mu, lambda, gamma, epsilon) also define a multi-dimensional parameter space over which alignment quality varies.

**What is genuinely new (not reducible to shared abstraction)**:
- OT as a regularizer for an ill-posed inverse problem (MEG/EEG source imaging). This is not just computing OT distance between distributions; it is embedding OT inside a regression objective to constrain the solution space. The matching is between latent (unobserved) neural sources, not between observed signals.
- The Wasserstein barycenter x-bar emerges as a group-level neural source estimate --- an "average brain activation" that respects cortical geometry. This is the Frechet mean in Wasserstein space, a concept from OT theory applied to neural source localization.
- Concomitant noise estimation (sigma^(s) per subject) extends MTW to handle heterogeneous noise --- a practical neuroscience requirement absent from abstract OT.
- Validated on the Wakeman-Henson face perception dataset: MWE localizes sources in the fusiform face area consistent with fMRI ground truth, closing the gap between MEG temporal resolution and fMRI spatial resolution.
- Generalized Sinkhorn algorithm for unbalanced transport enables efficient computation on cortical meshes (~2500 sources per hemisphere).

**Connections the authors acknowledge**: Cite Kantorovich OT, Cuturi (Sinkhorn distances), Chizat et al. (unbalanced OT). Cite fMRI multi-subject methods (Varoquaux, Kozunov). Do NOT cite TDA or persistence diagrams --- the connection to Wasserstein distance on PDs is implicit.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transport plan P | Optimal assignment / matching |
| Unbalanced Wasserstein distance W | Matching cost with mass relaxation |
| Wasserstein barycenter x-bar | Frechet mean of matched features |
| Cost matrix M (geodesic) | Pairwise cost for matching |
| Generalized Sinkhorn | Matching algorithm (entropic, unbalanced) |
| Left marginal m = P*1 | Transported mass per source |
| Source space | Feature space (cortical vertices) |
| Leadfield matrix L | Forward model (linear constraint) |
| Current dipole amplitude x | Feature value to be matched |
| L1 penalty (lambda) | Sparsity (focal sources) |
| Noise variance sigma^(s) | Per-subject robustness parameter |
| MCE (minimum current estimates) | Independent matching baseline (null) |
| Group Lasso (L21) | Rigid matching (forced identity, null) |
| Earth mover distance (EMD) | Wasserstein-1 evaluation metric |

**See also**: `by-structure/optimal_transport.md`, `by-domain/neuroscience.md`

---

## 1906.11768 --- Lee, Dabagia, Dyer, Rozell (2019)
**"Hierarchical Optimal Transport for Multimodal Distribution Alignment"**

**Domain(s)**: Neuroscience (neural decoding, motor cortex), TDA (optimal transport)

**Abstract machines instantiated**:
- **Matching**: The central contribution. Hierarchical OT (HOT) formulates cross-domain alignment as a two-level optimal transport problem. Level 1: match clusters across domains (coarse assignment). Level 2: match individual data points within matched clusters (fine-grained assignment). The Wasserstein distance serves as the divergence measure at both levels. Applied to neural decoding: align neural population activity from macaque primary motor cortex (M1) across different recording sessions/conditions, then decode movement directions and velocities from the aligned representations. The transport plan maps neural firing patterns from one session to another, enabling cross-session generalization.
- **Stability**: Performance guarantees describe when cluster correspondences can be recovered under the hierarchical formulation. The method is robust to noise, ambiguity, and multimodality in the data distributions --- precisely the conditions encountered in neural recordings where trial-to-trial variability is high. The hierarchical structure provides stability: even if fine-grained matching fails, the coarse cluster assignment can still be correct.
- **Parameterized homology**: The hierarchy itself is a parameterization: as the number of clusters varies, the alignment transitions from fully global (one cluster = standard OT) to fully local (each point is its own cluster). The entropic regularization parameter epsilon also controls the softness of the assignment.
- **Null hypothesis**: Standard (flat) optimal transport alignment serves as the baseline null. The hierarchical formulation outperforms flat OT when data has clustered structure (as neural population activity does, with clusters corresponding to movement directions). Vanilla averaging of unaligned representations is the weakest null.

**What is genuinely new (not reducible to shared abstraction)**:
- Two-level hierarchy in OT is a structural innovation: it exploits the fact that neural population activity has meaningful clustered structure (corresponding to discrete movement directions). Standard OT treats all points equally; HOT respects the categorical structure of the neural code.
- Application to cross-session neural decoding in macaque M1 is a genuinely new use case: align neural population vectors recorded on different days/conditions so that a decoder trained on one session works on another. This is "domain adaptation" for neural data via OT.
- Distributed ADMM algorithm with Sinkhorn distance provides computational efficiency scaling quadratically with the largest cluster rather than the full dataset --- important for real-time neural decoding.
- Worst-case geometry analysis: the paper characterizes dataset geometries where hierarchical alignment fails, providing a negative result about the limits of OT-based neural alignment.
- Unitary transformation model between sessions: when the cross-session mapping is approximately orthogonal (rotation of neural population geometry), HOT provably recovers the correct alignment.

**Connections the authors acknowledge**: Cite OT literature (Villani, Cuturi, Peyre). Cite neural decoding/BCI literature (Churchland, Shenoy). Do NOT cite TDA, persistence diagrams, or hyperalignment explicitly --- the work bridges OT theory and systems neuroscience without referencing the broader Rosetta.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transport plan | Optimal assignment / matching |
| Wasserstein distance | Matching cost |
| Hierarchical OT | Two-level matching (coarse + fine) |
| Cluster correspondence | Coarse-level matching |
| Within-cluster alignment | Fine-level matching |
| Sinkhorn distance | Entropically regularized matching cost |
| ADMM solver | Matching algorithm (distributed) |
| Neural population vector | Feature vector |
| Movement direction cluster | Category in feature space |
| Cross-session alignment | Domain adaptation via matching |
| Unitary transformation | Structure-preserving map between feature spaces |

**See also**: `by-structure/optimal_transport.md`, `by-domain/neuroscience.md`

---

## Wave 6 — Directed Information Flow in Neural Oscillations and Spike Trains (2026-04-07)

### DOI: 10.1016/j.neuroimage.2013.08.056 --- Lobier, Siebenhuhner, Palva, Palva (2014)
**"Phase transfer entropy: A novel phase-based measure for directed connectivity in networks coupled by oscillatory interactions"**

**Domain(s)**: Neuroscience, information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Phase TE quantifies directed phase coupling between oscillatory neural signals. The measure computes TE on phase time series extracted via Morlet filtering, detecting directed information flow from source to target that exceeds what the target's own phase history can predict. Differential TE (dTE = TE(1->2) - TE(2->1)) isolates the net directional excess. This is joint-vs-marginal at two levels: (1) the TE itself measures how the joint (source + target) history exceeds the marginal (target-only) history for prediction, and (2) the phase extraction step takes the joint amplitude-phase signal and projects to the phase marginal, discarding amplitude to isolate oscillatory coupling.
- **Null hypothesis**: Surrogate data constructs the null distribution. The paper validates that surrogate-based null-hypothesis testing correctly identifies statistical significance of directed phase coupling. Crucially, the surrogates must destroy phase relationships while preserving spectral properties --- the same destroy-structure/preserve-statistics pattern as Theiler surrogates. Phase TE yields no false positives under mixing and noise when tested against surrogate nulls.
- **Parameterized homology**: Frequency band serves as the filtration parameter. The paper demonstrates frequency-band-specific directed connectivity: different oscillatory frequency bands (e.g., alpha, beta, gamma) yield different directed coupling patterns. The coupling strength and direction can reverse across bands. This is a discrete parameterized family of directed graphs indexed by frequency, analogous to a filtration where each frequency band reveals a different connectivity topology.

**What is genuinely new (not reducible to shared abstraction)**:
- Phase extraction as a preprocessing step before TE is domain-specific to oscillatory neural systems. The Hilbert/Morlet phase time series is a circular (S^1-valued) variable, not a real-valued one. Standard TE estimators on real-valued signals conflate amplitude and phase contributions; Phase TE isolates the phase component. This circular-variable structure has no direct analogue in standard TDA or QEC chain complexes.
- Robustness to linear mixing (volume conduction) is a uniquely neuroimaging concern. MEG/EEG signals are linear superpositions of sources, creating spurious correlations. Phase TE's demonstrated robustness to mixing is a domain-specific stability property absent from information-theoretic TE in other contexts.
- Computational efficiency: Phase TE is "considerably more efficient computationally" than real-valued TE because phase time series have lower dimensionality than the original signals. This practical advantage is specific to the oscillatory-neural-data use case.
- Bidirectional frequency-band-specific interaction patterns that confound real-valued TE are "accurately untangled" by Phase TE. The ability to resolve per-band directionality is a capability absent from broadband TE.

**Connections the authors acknowledge**: Cite Schreiber (2000) transfer entropy, Granger causality, Dynamic Causal Modeling. Situated in the MEG/EEG effective connectivity literature. Do NOT cite TDA, persistent homology, or dynamical systems topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Phase transfer entropy | Joint-vs-marginal excess (directed, on phase time series) |
| Differential TE (dTE) | Net directed excess (asymmetric joint-vs-marginal) |
| Surrogate data | Null hypothesis distribution (structure-destroying) |
| Frequency band | Parameter in parameterized family |
| Coupling strength | Excess magnitude |
| Linear mixing / volume conduction | Perturbation (domain-specific noise model) |
| Neural Mass Model | Generative model for validation |
| Effective connectivity | Directed information flow |

**See also**: `by-domain/neuroscience.md`, `by-domain/information_theory.md`, `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

### DOI: 10.1371/journal.pcbi.1008054 --- Shorten, Spinney, Lizier (2021)
**"Estimating Transfer Entropy in Continuous Time Between Neural Spike Trains or Other Event-Based Data"**

**Domain(s)**: Information theory, neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Continuous-time TE measures directed information flow: how much the joint history (source + target point processes) improves prediction of target updates beyond the target's own history. The TE is formulated via Radon-Nikodym derivatives between measures of complete path realizations --- the joint measure vs the product of conditional and marginal measures. This is the purest mathematical formulation of joint-vs-marginal excess for event-based data: the excess is literally the KL divergence between the true conditional (given full history) and the reduced conditional (given only target history).
- **Null hypothesis**: The paper develops a local permutation scheme for generating null surrogates specifically for point process data. Standard source-time-shift surrogates are shown to FAIL for continuous-time spike trains (they do not properly destroy the source-target coupling while preserving marginal statistics). The local permutation scheme correctly generates surrogates conforming to the null hypothesis of conditional independence: H_source is independent of updates in target given H_target. This is a significant methodological advance --- the paper demonstrates that naive null-generation methods produce incorrect results, and provides a principled alternative.
- **Parameterized homology**: The continuous-time framework implicitly parameterizes TE by timescale. Unlike discrete-time TE which is locked to a single bin width, the kNN estimator captures relationships occurring at both fine temporal precision and over long time intervals simultaneously. The inter-spike interval serves as a natural continuous parameter. The pathwise transfer entropy (introduced by the precursor Spinney, Prokopenko, Lizier 2016) decomposes into discontinuous jump contributions (at target spikes) and continuously varying contributions (between spikes) --- a natural two-component parameterization by event type.

**What is genuinely new (not reducible to shared abstraction)**:
- Continuous-time formulation of TE via Radon-Nikodym derivatives on path space is mathematically distinct from discrete-time MI/TE. The pathwise transfer entropy --- accumulated TE along a specific realization, analogous to work/heat along a thermodynamic path --- is a genuinely new information-theoretic object without direct parallel in TDA or QEC.
- The k-nearest-neighbours estimator in the inter-event-interval embedding space is provably consistent (converges to the true TE) while discrete-time plug-in estimators are NOT consistent for event-based data. This is not merely an engineering improvement but a fundamental mathematical distinction: the discrete approach converges to the wrong value.
- Demonstration that source-time-shift surrogates fail for continuous-time data is a negative result about null hypothesis construction. The failure mode is specific to point processes: time-shifting a source spike train changes its temporal relationship to the target in a way that does not correspond to the intended null of conditional independence.
- Application to the pyloric circuit of the crustacean stomatogastric ganglion provides a biologically grounded validation where previous related estimators (discrete-time TE, model-based approaches) failed to correctly infer the known connectivity.

**Connections the authors acknowledge**: Cite Schreiber (2000) TE, Spinney/Prokopenko/Lizier (2016) continuous-time TE theory, JIDT toolkit. Cite neuroscience spike-train analysis literature. Acknowledge connection to Granger causality and point process GLMs. Do NOT cite TDA, persistent homology, or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transfer entropy | Directed joint-vs-marginal excess |
| Conditional independence | Null hypothesis (no directed coupling) |
| Local permutation surrogate | Null hypothesis distribution (structure-destroying, preserving marginal statistics) |
| Source-time-shift surrogate | Naive null (shown to fail) |
| kNN estimator | Estimation algorithm for excess |
| Pathwise transfer entropy | Accumulated excess along a realization |
| Inter-event interval | Continuous parameter (timescale) |
| Point process | Event-based time series (domain object) |
| Radon-Nikodym derivative | Density ratio quantifying excess |
| Pyloric circuit | Biological validation system |
| Spike train | Neural event sequence |

**See also**: `by-domain/information_theory.md`, `by-domain/neuroscience.md`, `by-structure/composite_systems.md`, `by-structure/phase_transitions.md`

---

## Wave 7: Session 5 — Causal Emergence + Joint×TDA Gap-Fill (2026-04-07)

---

## Rosas, Mediano, Jensen, Seth, Barrett, Carhart-Harris, Bor (2020)
**"Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data"**
PLoS Computational Biology, 16(12), e1008289.
arXiv: 2004.08220 (q-bio.NC, nlin.AO)
DOI: 10.1371/journal.pcbi.1008289
143 citations.

**Domain(s)**: Information theory, neuroscience, dynamical systems (complex systems)

**Abstract machines instantiated**:

- **Joint-vs-marginal excess (PRIMARY — inverted direction)**: The core of the paper, but with an inversion. Standard joint-vs-marginal asks "does the composite have structure absent from components?" Rosas et al. ask "does the coarse-grained macro have causal power absent from the fine-grained micro parts?" Formally: Ψ^(1)_{t,t'}(V) = I(V_t; V_{t'}) - Σ_j I(X^j_t; V_{t'}) > 0. This is whole-minus-sum: the emergent feature V's predictive power exceeds the sum of individual micro-parts' predictive power. Same mathematical structure (information in the joint exceeding sum of marginals) but applied at a different level of description — the "joint" is the COARSE-GRAINED macro feature, not the full system. Theorem 1 establishes that causal emergence exists iff Syn^(k)(X_t; X_{t'}) > 0, i.e., iff there is dynamical synergy among the parts. Total emergence capacity decomposes as Syn^(k) = D^(k) + G^(k): downward causation (macro affects micro) plus causal decoupling (macro affects only macro — "statistical ghosts").

- **Parameterized homology**: Three distinct parameters. (1) The order k of the emergence analysis: at k=1, test whether features emerge beyond individual parts; at general k, test beyond k-plet information. Critical values of k mark where emergence switches from present to absent — directly analogous to a filtration parameter. Lemma 2 gives exact decomposition I(X;Y) = Red^(k) + Syn^(k) + ΣUn^(k) for every k. (2) Time lag t'-t: the ECoG results show Ψ as a function of timescale, with emergence detectable up to ~0.2s then decaying. (3) The microscopic partition itself: emergence depends on how you carve the system into parts, and different partitions yield different emergence capacities.

- **Null hypothesis**: Multiple null constructions. (1) Formal: Syn^(k)(X_t; X_{t'}) = 0 means no emergent features exist. (2) Practical: Ψ^(k) ≤ 0 as sufficient condition (but not necessary — false negatives possible due to redundancy double-counting). (3) Perfect decoupling: D^(k) = 0 (no downward causation) as null for top-down effects. (4) Application-level: low-avoidance and high-avoidance regimes in boids model serve as no-emergence controls.

- **Chain complex (inherited)**: Inherits from PID lattice (antichain collections ordered by refinement with Moebius inversion) and PhiID double lattice A × A (Mediano 2019). The k-order coarse-graining (grouping atoms by order into Syn^(k), Red^(k), Un^(k)) is a novel quotient of the PID lattice creating a graded family of simpler decompositions.

**What is genuinely new (not reducible to shared abstraction)**:
1. **The inversion of direction**: Not "joint vs. product of marginals" but "macro vs. sum of micro." Could be formalized as a new pattern: "upward excess" (standard MI) vs. "downward excess" (causal emergence). The Rosetta doesn't currently capture this directionality.
2. **The D^(k) + G^(k) decomposition**: Total emergence = downward causation + causal decoupling. No analogue in TDA, QEC, or dynamical systems. You can't "decompose entanglement into downward causation plus decoupling."
3. **Statistical ghosts**: Perfectly decoupled emergent features — patterns that predict their own future without any individual part influencing or being influenced by them. The parity example: parity of a binary system propagates in time, but no individual bit affects or is affected by it. Emergence without micro-level causal trace. No other Rosetta domain has this concept.
4. **Reconciliation of strong/weak emergence**: Supervenient features CAN have irreducible causal power without violating physical laws — irreducibility is in the PID sense (information synergy), not metaphysical. A meta-result about levels of description.
5. **Practical sufficiency criteria** (Eqs. 10a-c): Require only pairwise MI, scale linearly with system size. PID-agnostic data-efficient emergence tests.

**Key results**:
- **Game of Life**: 15×15 cells, particle collider initial conditions. Feature V_t = particle type (still lifes, oscillators, gliders, etc.). Ψ^(1) = 0.58 ± 0.02 > 0. Γ^(1) = 0.009 ± 0.0002, orders of magnitude smaller than I(V_t; V_{t'}) = 0.99 ± 0.02. Particle dynamics are causally decoupled from substrate — "their own collision rules."
- **Reynolds flocking**: N=10 boids, avoidance parameter a2 swept. Ψ > 0 only in intermediate a2 range ("edge of chaos" where flocks form and disintegrate). At low a2 (ordered), individual boids predict center of mass (high redundancy). At high a2 (repulsive), no flocks. Emergence detected at the critical regime.
- **Neural ECoG**: 64-channel macaque ECoG during reaching (Neurotycho). Feature V_t = PLS+SVM decoder for 3D wrist position. Ψ^(1) = 1.275 ± 0.002 > 0 at 8ms timescale. Γ^(1) = 0.049 ± 0.002. Motor representation has irreducible causal power decoupled from individual electrodes. Emergence holds up to ~0.2s timescale.

**Connections the authors acknowledge**: Extensive comparison with Hoel et al. (2013) do-calculus emergence, Seth (2010) G-emergence, Chang et al. (2019) NTIC, IIT (Tononi). Deep engagement with philosophy (Bedau, Chalmers, Anderson). Cite Takens for future extension. **NO acknowledgment of TDA, QEC, or topological parallels** — despite k-order coarse-graining being structurally similar to a filtration.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Causal emergence (Ψ > 0) | Joint-vs-marginal excess (inverted: macro over micro) |
| Downward causation (D^(k) > 0) | Directed joint excess (macro-to-micro flow) |
| Causal decoupling (G^(k) > 0) | Self-sustaining joint excess ("statistical ghost") |
| Emergence capacity Syn^(k) | Synergy (PID synergy, applied temporally) |
| Supervenient feature V_t | Coarse-grained observable / macro feature |
| Coarse-graining (V = F(X)) | Projection / quotient map (micro to macro) |
| k-synergistic channel C_k | Channel carrying only k-th order synergy |
| Statistical ghost | Perfectly decoupled emergent feature |
| Emergence order k | Filtration parameter |
| PhiID lattice | Double redundancy lattice (Mediano 2019) |
| Whole-minus-sum (Ψ) | Interaction information / O-information family |
| Granger causality | Directed information (time-lagged predictive power) |

---

## 2504.10140 --- Varley, Mediano, Patania & Bongard (2025)
**"The topology of synergy: Linking topological and information-theoretic approaches to higher-order interactions in complex systems"**
PLoS Computational Biology, DOI: 10.1371/journal.pcbi.1013649 | arXiv: 2504.10140
Citations: 4 (Semantic Scholar, April 2025)

**Domain(s)**: TDA, information theory, neuroscience

**Abstract machines instantiated**:
- **Chain complex**: The Vietoris-Rips filtration constructs a simplicial complex from the point cloud of multivariate time series data. Ripser computes persistent homology up to dimension 2 (H2 features = three-dimensional cavities/voids). The chain complex is implicit in the standard VR construction with Chebyshev distance. Crucially, the same distance metric (Chebyshev) is used for both the TDA (Rips filtration) and the information-theoretic analysis (KNN-based entropy estimation via JIDT), ensuring the two frameworks see the same geometry.
- **Parameterized homology**: The Rips filtration scale epsilon is the parameter. As epsilon grows, simplices are added to the complex. The paper tracks two H2 summary statistics: (1) average persistence time of three-dimensional voids and (2) total number of three-dimensional voids. These are scalar summaries of the persistence diagram, parameterized by the filtration. The key finding is that these topological invariants correlate with information-theoretic measures: more negative normalized O-information (greater synergy dominance) is associated with more numerous and longer-lived H2 cavities.
- **Joint-vs-marginal excess**: This is the paper's central conceptual object. The O-information O(X) = TC(X) - DTC(X) decomposes the balance between "collective constraints" (TC, information in marginals exceeding the joint) and "shared information" (DTC, information in the joint exceeding marginals). Synergy is defined precisely as joint-vs-marginal excess: information present in the joint state of X1 AND X2 AND X3 that cannot be learned from any proper subset. The normalized O-information O-bar = O/S provides a scale-free redundancy-synergy balance in [-1,1]. The paper finds this quantity tracks H2 topology: O-bar vs average H2 persistence gives rho = -0.65 (p < 10^-100) for synergy-dominated triads and rho = -0.55 (p < 10^-100) for redundancy-dominated triads.
- **Null hypothesis**: Autocorrelation-preserving null model via circular time-shift: each time series is shifted to come from a different fMRI scan (recorded hours apart), destroying genuine higher-order dependencies while preserving first-order autocorrelation. A triad is significantly synergistic/redundant only if its O-information deviates by > 3 standard deviations from this null distribution. Result: 30,100 significantly redundant triads and 6,200 significantly synergistic triads out of 1,313,400 unique triads.
- **Stability**: Implicit. The paper relies on the stability of persistent homology (persistence diagram robust to small perturbations of the point cloud) and the consistency of KNN-based information estimators (Kraskov estimator converges to true MI). The common use of Chebyshev distance for both analyses ensures metric consistency. The rotation-invariance experiments (PCA rotation) test a form of stability: intrinsic topological features (H2 cavities) are preserved under rotation, while contextual information-theoretic quantities are not.

**What is genuinely new (not reducible to shared abstraction)**:
- **The synergy-cavity correspondence**: Three-dimensional cavities (H2 persistent homology features) correspond to synergistic information, while knots correspond to redundancy. This is the first empirical demonstration that PH features at a specific homological dimension have a defined information-theoretic character. This is NOT just "both detect higher-order structure" -- the correspondence is specific: H2 cavities <-> synergy, 1D curves <-> redundancy. No prior work established this mapping.
- **Intrinsic vs. contextual higher-order information**: The paper introduces a novel distinction. Intrinsic higher-order information persists under rotation (PCA); contextual information depends on embedding orientation. Spheres have purely intrinsic synergy (rotationally symmetric cavity). Rotated planes have purely contextual synergy (vanishes after PCA). Toroids have a mixture. This distinction has no prior formalization.
- **PCA systematically destroys synergy**: The paper shows that PCA (and by extension manifold learning) preferentially preserves redundancy and is blind to synergy. The correlation between normalized O-information and variance explained by PC1 is rho = 0.91-0.95 (p < 10^-100). The most synergistic triads look random to PCA (variance explained by PC1 near 33%, the expected value for independent variables). This implies that the entire neural manifold learning literature is systematically missing synergistic structure.
- **Gauss Theorema Egregium intuition**: The authors conjecture that the synergy-cavity link follows from the impossibility of projecting a sphere onto a plane without distortion. The information lost in projection is precisely synergistic. This is a conceptual bridge, not a proof, but it suggests a formal theorem may be derivable.
- **No formal proof of the TDA-IT correspondence**: The authors explicitly state this is "experimental mathematics" -- correlational, not proven. A formal theorem linking H2 Betti numbers to O-information remains open.

**Key quantitative results (fMRI, HCP data, 200-node Schaefer parcellation)**:
- **Avg H2 persistence vs TC**: rho = -0.76 (redundant triads), -0.66 (synergistic triads), all p < 10^-100
- **Avg H2 persistence vs DTC**: rho = -0.74 (redundant), -0.66 (synergistic), all p < 10^-100
- **Avg H2 persistence vs normalized O-bar**: rho = -0.55 (redundant), -0.65 (synergistic), all p < 10^-100
- **Number H2 voids vs normalized O-bar**: rho = -0.30 (redundant), -0.32 (synergistic), all p < 10^-100
- **Normalized O-bar vs PC1 variance explained**: rho = 0.91 (redundant), 0.95 (synergistic), all p < 10^-100
- After PCA rotation: correlations between O-bar and H2 features remain significant but weaker (rho = -0.12 to -0.17); direction does NOT reverse (unlike TC/DTC which reverse sign after PCA)
- Toy examples: Sphere O = -1.384 nat (invariant under PCA); Hollow torus O = -1.554 nat (-> -1.096 after PCA); Plane O = -2.819 nat (-> 0 after PCA); Trefoil knot O = +3.246 nat (-> +1.893 after PCA)

**Methods**:
- **Filtration**: Vietoris-Rips, computed via Ripser
- **Distance metric**: Chebyshev (L-infinity), used consistently for both TDA and KNN-based information estimation
- **Information estimator**: KNN-based O-information estimator (Eq. 14, derived from Gomez-Herrero et al. 2015 entropy combination framework), single neighbor search to minimize bias. Implemented in JIDT (Lizier 2014). Uses k-nearest neighbor distances in joint space, range counts in marginal and (N-1)-dimensional marginal spaces.
- **Cohomology dimension**: max_dim = 2 (computes H0, H1, H2)
- **Sample size**: 1,100 frames per triad (subsampled from 4,400 concatenated fMRI frames)
- **Data**: HCP resting-state fMRI, 100 unrelated subjects, 200-node Schaefer parcellation, 4 concatenated scans, TR = 720ms

**Connections the authors acknowledge**: Cite Rosas et al. (2019) on O-information, Varley et al. (2023) on synergistic subsystems, Kraskov et al. (2004) on KNN estimators, Petri et al. (2014) on homological scaffolds in brain networks, Reimann et al. (2017) on cliques/cavities. Cite the link between synergy and causal colliders (Rosas et al. 2024), synergy and chaos in Boolean networks. **EXPLICITLY a cross-domain bridge between TDA and information theory**, applied to neuroscience data. The authors note the two fields developed "largely in parallel with limited interdisciplinary cross-talk."

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| O-information O(X) | Joint-vs-marginal excess (signed: synergy vs redundancy balance) |
| Normalized O-information O-bar | Scale-free joint-vs-marginal balance |
| Total correlation TC | Collective constraint (deviation from independence) |
| Dual total correlation DTC | Shared information (multipartite dependency) |
| S-information S = TC + DTC | Total higher-order information (normalizer) |
| Three-dimensional cavity (H2 void) | Persistent homology class (Betti-2 feature) |
| Average persistence | Parameterized homology summary (mean lifetime) |
| Number of voids | Betti number count (H2) |
| Rips filtration | Parameterization (scale parameter epsilon) |
| Chebyshev distance | L-infinity metric (used for both TDA and KNN estimation) |
| KNN-based estimator | Non-parametric joint-vs-marginal estimator (Kraskov/Kozachenko-Leonenko) |
| Intrinsic higher-order information | Rotation-invariant joint-vs-marginal excess |
| Contextual higher-order information | Embedding-dependent joint-vs-marginal excess |
| Circular shift null | Autocorrelation-preserving null hypothesis |
| Synergy-dominated (O < 0) | Cavity-bearing topology (H2 features present) |
| Redundancy-dominated (O > 0) | Low-dimensional / knot-like topology (H2 features absent) |
| PCA rotation | Dimensionality reduction (destroys synergy, preserves redundancy) |

**See also**: `by-domain/information_theory.md`, `by-domain/neuroscience.md`, `by-structure/composite_systems.md`, `atlas/JOINT_VS_MARGINAL.md`

---

## 2307.07492 --- Hamilton & Leditzky (2023/2024)
**"Probing Multipartite Entanglement Through Persistent Homology"**
Communications in Mathematical Physics, vol. 405, article 125 (2024).
arXiv: 2307.07492 | DOI: 10.1007/s00220-024-04953-4
8 citations.

**Domain(s)**: QEC (quantum entanglement), TDA

**Abstract machines instantiated**:

- **Joint-vs-marginal excess**: The paper uses persistent homology to probe multipartite entanglement — the canonical joint-vs-marginal excess in quantum mechanics. The q-deformed total correlation C_q(J) = Σ_{v∈J} S_q(v) - S_q(J) measures how much the joint entropy of subsystem J falls below the sum of marginal entropies. This is exactly the joint-vs-marginal gap: entanglement means the composite system has correlations absent from individual parts. The main theorem: the reduced integrated Euler characteristic of the persistence complex equals the q-deformed interaction information, which for q=2 and n qubits (n even) equals the **n-tangle** τ_n — a standard entanglement monotone. Barcodes provide FINER discrimination than the n-tangle: two 6-qubit graph states with identical τ_n = 1 have visibly different barcodes, detecting different SLOCC orbits. Two states with τ_n = 0 also distinguished by barcodes.

- **Chain complex**: Treats the n parties as vertices of the full simplex Δ = 2^{A_1,...,A_n}. The sublevel set filtration G(ε) = {J ∈ Δ : C_q(J) ≤ ε} adds simplices as the total correlation threshold grows. Persistent homology is computed on this filtered simplicial complex. The algebraic structure is the standard chain complex of the simplex, with the filtration driven by the quantum correlation measure.

- **Parameterized homology**: The filtration parameter ε (total correlation threshold) parameterizes a family of simplicial complexes. Birth-death pairs in the persistence barcode track when multipartite correlations appear and when they are filled in by higher-order correlations. The barcode encodes the full multiscale entanglement structure.

- **Stability**: Implicit via standard PH stability. The paper also connects to entropy inequalities: relative persistent homology with respect to a subcomplex Δ_{A,B} yields the negative conditional mutual information -I(A:B|R) ≤ 0, with non-positivity following from strong subadditivity (Lieb-Ruskai 1973). This connects topological invariants to fundamental quantum information constraints.

- **Matching**: Barcode comparison between different quantum states is an implicit matching problem (comparing persistence diagrams).

- **Null hypothesis**: Separable (product) states serve as the baseline — for product states, all C_q(J) decompose into sums of bipartite correlations and higher-order entanglement vanishes.

**What is genuinely new (not reducible to shared abstraction)**:
1. The filtration is driven by a MULTIPARTITE correlation measure (total correlation over all subsets), not a pairwise distance. This captures k-body correlations directly in k-simplices — a departure from standard Vietoris-Rips (pairwise distance → simplicial complex).
2. The IEC = n-tangle theorem connects a topological summary (integrated Euler characteristic) to a standard entanglement measure (n-tangle), answering an open question of Eltschka & Siewert (2018).
3. Barcodes are strictly finer than scalar entanglement measures: states with identical n-tangle are distinguished. This suggests persistence diagrams as a new tool for SLOCC classification.
4. Relative PH connects to strong subadditivity — entropy inequalities become topological constraints.
5. The paper proposes generalization to arbitrary resource theories via generalized divergences satisfying the data processing inequality.

**Connections the authors acknowledge**: Cite prior work using bipartite measures for PH (Di Pierro, Mengoni — inverse MI as pairwise distance). Explicitly contrast their multipartite approach. Connection to entanglement theory (SLOCC, entanglement monotones, n-tangle). No awareness of PID, dynamical systems, or neuroscience parallels. The bridge to strong subadditivity via relative PH is the most surprising cross-domain connection.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| q-deformed total correlation C_q(J) | Joint-vs-marginal excess (entropic) |
| Sublevel set filtration G(ε) | Parameterized homology (correlation threshold) |
| Integrated Euler characteristic X̃_q(∞) | Topological summary of persistence |
| n-tangle τ_n | Scalar entanglement measure = IEC at q=2 |
| Persistence barcode | Birth-death pairs across filtration |
| SLOCC equivalence | Equivalence under local operations |
| Relative PH | Persistent homology of pair (space, subspace) |
| Conditional mutual information I(A:B|R) | Tripartite correlation conditioned on reference |
| Strong subadditivity | Fundamental entropy inequality → topological constraint |
| Product state | Null hypothesis (no entanglement) |
| Graph state | Quantum state from graph structure |

**See also**: `by-domain/qec.md`, `by-domain/tda.md`, `by-structure/composite_systems.md`, `by-structure/boundary_operators.md`, `atlas/JOINT_VS_MARGINAL.md`

---

## 2603.03237 --- Natarajan, Chaplin, Bull, Mulholland-Illingworth, Leedham, Byrne, Jimenez & Harrington (2026)
**"Topology of Multi-species Localization"**
arXiv: 2603.03237 [math.AT]. March 2026.
0 citations (preprint, 1 month old).

**Domain(s)**: TDA, computational biology

**Abstract machines instantiated**:

- **Joint-vs-marginal excess (PRIMARY)**: The M2S2 (Multiscale Multi-species Spatial Signatures) framework decomposes the persistent homology of a multi-species point cloud into four categories via the k-chromatic gluing map q_{k,*}: ⊔_{|A|=k} F_r(X_A) → F_r(X). The **cokernel** of this map identifies features that are NOT k-chromatic — they appear ONLY when more than k species are considered together. This is the pure topological joint-vs-marginal excess: structure visible in the joint (multi-species) space that is absent from all k-species marginals. The **kernel** captures the reverse: features destroyed by composition (present in some k-tuple but filled in or merged when other species are added). The **image** captures features formed by some species that persist in the joint. This four-way decomposition (image / kernel / cokernel / domain) is richer than a binary excess/no-excess test.

- **Chain complex**: Built on chromatic Delaunay-Cech filtrations. The k-chromatic gluing map induces maps between chain complexes at each filtration level, and functoriality of homology gives maps of persistence modules. Kernel, image, and cokernel persistence computed via Cohen-Steiner et al. (2009) algorithm (phimaker package). Z/2 coefficients throughout.

- **Parameterized homology**: The filtration parameter r (spatial scale) and the chromatic parameter k (number of species) jointly parameterize a family of persistence diagrams. At each k, the four persistence diagrams (image, kernel, cokernel, domain) capture different aspects of multi-species spatial structure across scales.

- **Null hypothesis**: Single-species persistence diagrams (domain diagrams) serve as the baseline. The cokernel measures what the joint adds beyond all k-species subsets. In applications: the ABM model provides parameter-controlled ground truth for validating that the topological signatures recover known biological regimes.

- **Stability**: Uses chromatic Delaunay-Cech filtration (homotopy-equivalent to Cech) with discrete Morse theory for efficiency. Standard PH stability applies to each persistence module.

**What is genuinely new (not reducible to shared abstraction)**:
1. The four-way decomposition (image / kernel / cokernel / domain) goes beyond binary joint-vs-marginal. Kernel features (destroyed by composition) have no analogue in PID — you can't have "information present in component A that vanishes in the joint."
2. The chromatic Delaunay-Cech filtration solves a fundamental technical problem: standard alpha filtrations do NOT respect inclusions of point clouds (adding points can remove simplices), breaking functoriality. This filtration is both homotopy-correct and inclusion-respecting.
3. Application to spatial biology: the framework recovers immunoediting regimes (elimination / equilibrium / escape) from cell-type point clouds, and identifies biologically meaningful multi-species interactions (periostin-macrophage, cytotoxic T cell-macrophage-neutrophil triples) in colorectal cancer tissue.
4. Three-way interactions detected by cokernel persistence that are invisible to all pairwise analyses — a concrete demonstration that TDA can detect genuinely higher-order spatial structure.

**Connections the authors acknowledge**: Cite Stolz (2024, Dowker persistence for pairs), Wagner (2024, mixup barcodes), Montesano (2024/2026, chromatic TDA). Contrast with pairwise-only methods. Cite Cohen-Steiner et al. for kernel/image/cokernel persistence theory. No connections to QEC, information theory, or dynamical systems — despite the kernel/cokernel decomposition being structurally analogous to PID's redundancy/synergy.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Cokernel persistence | Joint-vs-marginal excess (topological features only in joint) |
| Kernel persistence | Features destroyed by composition (no PID analogue) |
| Image persistence | Features formed by subset, persisting in joint |
| k-chromatic gluing map | Inclusion from k-species subsets to full system |
| Chromatic Delaunay-Cech filtration | Functorial filtration (scale parameter) |
| M2S2 signatures | Feature vector from persistence diagrams |
| Species labels | Component identities in composite system |
| Elimination / equilibrium / escape | Biological regimes recovered by topology |
| Persistent statistics | 34-dimensional vectorization of persistence diagram |
| phimaker | Software for kernel/image/cokernel PH |

**See also**: `by-domain/tda.md`, `by-structure/composite_systems.md`, `by-structure/boundary_operators.md`, `atlas/JOINT_VS_MARGINAL.md`

---

## Wave 8: Match×TDA and Match×InfoTheo Gap-Fill (2026-04-07)

---

## arXiv: 1912.02563 --- Bubenik & Elchesen (2019)
**"Universality of persistence diagrams and the bottleneck and Wasserstein distances"**
Computational Geometry, 15 citations.

**Domain(s)**: TDA (algebraic topology, metric geometry)

**Abstract machines instantiated**:

- **Matching**: THE central object. The paper proves that bottleneck and Wasserstein distances on persistence diagrams arise from universal constructions — they are the canonical optimal matching metrics. The 1-Wasserstein distance satisfies Kantorovich-Rubinstein duality, exactly characterizing the matching as a linear program over transport plans. The bottleneck distance is the sup-cost matching. The universality theorem says: for ANY metric space with basepoint, these distances are the UNIQUE distances satisfying the universal property — every other distance factors through them. This is the strongest possible statement that matching IS the fundamental operation on persistence diagrams.

- **Stability**: Universal property implies stability: since the distances are canonical, any continuous map from persistence diagrams to another metric space automatically factors through them, giving Lipschitz-type stability for free. The Kantorovich-Rubinstein duality provides a dual characterization of stability via 1-Lipschitz functions.

- **Chain complex (weak)**: Persistence diagrams encode homological information from chain complexes. The paper works at the level of persistence diagrams (the output), not the chain complexes (the input), but the universal construction respects the algebraic origin.

**What is genuinely new (not reducible to shared abstraction)**:
1. The UNIVERSALITY result: bottleneck/Wasserstein are not just useful metrics — they are the unique metrics satisfying a universal property. This is a category-theoretic statement about the space of all possible distances on PDs.
2. Extension to arbitrary metric spaces with basepoint, not just multisets in the upper half-plane. This means the framework applies to multiparameter persistence.
3. Kantorovich-Rubinstein duality for 1-Wasserstein on PDs — connects the matching problem to optimization over 1-Lipschitz functions.

**Connections the authors acknowledge**: Cohen-Steiner, Edelsbrunner, Harer (stability theorem). Persistence landscapes (Bubenik 2015). Optimal transport theory. No connections to QEC, information theory, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Bottleneck distance | Sup-cost optimal matching between diagram points |
| p-Wasserstein distance | L^p-cost optimal matching (transport plan) |
| Universal property | Canonical factorization of all distance functionals |
| Kantorovich-Rubinstein duality | Dual formulation of matching via 1-Lipschitz functions |
| Basepoint | Diagonal (death = birth) as distinguished point |
| Multiset with metric | Persistence diagram in abstract setting |

**See also**: `by-domain/tda.md`, `by-structure/optimal_transport.md`, `atlas/MATCHING.md`

---

## arXiv: 2104.07710 --- Chen & Wang (2021)
**"Approximation algorithms for 1-Wasserstein distance between persistence diagrams"**
Journal of Machine Learning Research, 9 citations.

**Domain(s)**: TDA (computational topology, algorithms)

**Abstract machines instantiated**:

- **Matching**: THE central object. Computing 1-Wasserstein distance between persistence diagrams IS solving an optimal matching problem: assign each point in diagram A to a point in diagram B (or to the diagonal) at minimum total cost. The paper gives near-linear time approximation algorithms via randomly shifted quadtrees, adapted from Euclidean OT to the half-plane geometry of PDs. The key technical contribution is handling the diagonal — each PD point can match either to another point or to its projection onto the diagonal, creating a mixed assignment problem.

- **Stability**: The approximation guarantee (1+epsilon factor) preserves the stability properties of the exact distance. Near-linear time makes stability-based pipelines practical at scale.

**What is genuinely new (not reducible to shared abstraction)**:
1. First near-linear time algorithm for Wasserstein distance on PDs. Previous algorithms were O(n^3) (Hungarian) or O(n^{1.5} log n) (auction). This is O(n log n / epsilon^d) for d=2.
2. Adaptation of quadtree-based OT algorithms to the persistence diagram setting, where the diagonal acts as a reservoir of zero-cost points. This is technically non-trivial because standard OT assumes finite discrete measures, but PDs have the continuous diagonal.
3. Extensive experimental validation showing 100-1000x speedup over exact methods with <1% approximation error.

**Connections the authors acknowledge**: Optimal transport literature (Villani, Peyré-Cuturi). TDA stability (Cohen-Steiner). No connections to QEC, information theory, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| 1-Wasserstein distance | L^1-cost optimal matching on PDs |
| Quadtree decomposition | Hierarchical spatial partitioning for matching |
| Diagonal projection | Trivial matching (feature matched to nothing) |
| Hungarian algorithm | Exact optimal assignment (O(n^3) baseline) |
| Auction algorithm | Alternative exact matching (Bertsekas) |
| Approximation factor (1+epsilon) | Controlled matching quality |

**See also**: `by-domain/tda.md`, `by-structure/optimal_transport.md`, `atlas/MATCHING.md`

---

## Blahut (1972) + Arimoto (1972)
**Blahut: "Computation of channel capacity and rate-distortion functions" (IEEE Trans. IT, 18(4):460–473)**
**Arimoto: "An algorithm for computing the capacity of arbitrary discrete memoryless channels" (IEEE Trans. IT, 18(1):14–20)**
Combined citations: 3000+.

**Domain(s)**: Information theory (foundational)

**Abstract machines instantiated**:

- **Matching**: THE central machine. Both papers solve the same problem: find the optimal input distribution P(x) that maximizes mutual information I(X;Y) over a discrete memoryless channel P(y|x). This IS an optimal assignment problem — match source symbols to channel inputs to maximize throughput. Blahut extends this to rate-distortion: find the optimal test channel P(y|x) that minimizes I(X;Y) subject to an expected distortion constraint E[d(x,y)] ≤ D. This is optimal assignment between source alphabet and reproduction alphabet at minimum rate. The algorithm alternates between optimizing the input distribution (fixing the conditional) and optimizing the conditional (fixing the input) — each step is a matching update. Convergence is guaranteed by the EM-like double minimization of a KL divergence.

- **Parameterized homology**: The rate-distortion function R(D) traces a curve in (rate, distortion) space as the distortion parameter D varies. At each D, the optimal matching changes. The slope dR/dD = -s (the Lagrange multiplier) parameterizes the family. The capacity-cost function C(P) similarly parameterizes by power constraint.

- **Null hypothesis (weak)**: The uniform input distribution serves as the naive baseline. The algorithm converges to the capacity-achieving distribution, which may be very non-uniform. The gap C - I(X;Y)|_{uniform} measures how much structure the optimal matching exploits.

**What is genuinely new (not reducible to shared abstraction)**:
1. The alternating minimization structure: fix one marginal, optimize the other. This predates the EM algorithm (1977) and is structurally identical. Every iteration improves the objective, and the algorithm converges to the global optimum (convexity of mutual information in the input distribution for fixed channel).
2. Rate-distortion as matching: the optimal test channel P*(y|x) assigns each source symbol x to reproduction symbols y with probabilities that minimize rate at fixed distortion. This is a soft matching (probabilistic assignment) rather than hard matching (bijection).
3. Universality: the algorithm works for ANY discrete memoryless channel with ANY distortion measure. No structure beyond finite alphabets is required.

**Connections the authors acknowledge**: Shannon (1948, 1959) capacity and rate-distortion theorems. No connections to TDA, QEC (despite syndrome decoding being a matching problem on the same algebraic object), or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Channel capacity C | Maximum matching value (throughput) |
| Rate-distortion R(D) | Minimum-cost matching curve (parameterized) |
| Input distribution P(x) | Source-side matching weights |
| Test channel P(y\|x) | Soft assignment (probabilistic matching) |
| Alternating minimization | Iterative matching refinement |
| Lagrange multiplier s | Slope of parameterized matching curve |
| Distortion constraint E[d] ≤ D | Matching quality bound |

**See also**: `by-domain/information_theory.md`, `by-structure/optimal_transport.md`, `atlas/MATCHING.md`

---

## Wave 9: Paper Drop Folder — Topo-Rosetta Relevant (2026-04-07)

---

## arXiv: 2604.04891 --- Peyré (2026)
**"Muon Dynamics as a Spectral Wasserstein Flow"**
Gabriel Peyré, CNRS and ENS, PSL Université. April 2026.

**Domain(s)**: TDA / Optimal Transport, Dynamical Systems

**Abstract machines instantiated**:

- **Matching**: THE central object. The paper introduces a family of Spectral Wasserstein costs W_γ(μ,ν)² := inf_{π ∈ Π(μ,ν)} γ(∫ (y-x)(y-x)^T dπ(x,y)), where the infimum is over transport couplings (matchings between source and target measures) and γ is a norm on the positive semidefinite cone. This is the Kantorovich formulation — every coupling π IS a matching between μ and ν. The key novelty: instead of summing individual transport costs (as in classical W2), the cost depends on the global displacement covariance matrix, penalizing correlated displacements. The max-min representation (Theorem 2.10) W_γ(μ,ν)² = max_{Q ∈ K_γ} W^Q(μ,ν)² shows the Spectral Wasserstein cost as a worst-case matching over anisotropic quadratic transport problems.

- **Parameterized homology**: The Schatten norm index p parameterizes the entire family of geometries. At p=1 (trace norm), γ₁(S) = tr(S), recovering the classical quadratic Wasserstein W2. At p=∞ (operator norm), γ_∞(S) = λ_max(S), recovering the Muon optimizer geometry. Intermediate p interpolates continuously between these extremes. The comparison constants c_{γ_p} = d^{1/p - 1} and C_{γ_p} = 1 (Proposition 2.8) quantify exactly how the geometry deforms as p varies. This is a one-parameter family of transport geometries, directly analogous to parameterized filtrations in TDA.

- **Stability**: The paper proves that for monotone norms γ (including all Schatten norms), the Spectral Wasserstein cost is a genuine metric (Corollary 3.4): √c_γ · W2(μ,ν) ≤ W_γ(μ,ν) ≤ √C_γ · W2(μ,ν). This is a Lipschitz stability result — the Spectral Wasserstein distance is metrically equivalent to W2, so all topological properties (convergence, compactness) are preserved. The geodesic convexity results (Section 5) give a second form of stability: interpolations in the Spectral Wasserstein geometry don't create pathological intermediate states.

- **Chain complex (weak)**: The Benamou-Brenier dynamic formulation (Section 3) expresses the transport cost as an infimum over paths (velocity fields) satisfying the continuity equation ∂_t ρ + div(ρv) = 0. The continuity equation IS the chain complex condition — it encodes conservation of mass, the dynamical analogue of ∂² = 0. For monotone norms, the static (Kantorovich) and dynamic (Benamou-Brenier) formulations coincide (Theorem 3.3).

**What is genuinely new (not reducible to shared abstraction)**:
1. The MATRIX-AWARENESS of the transport cost. Classical W2 sums scalar displacement costs independently per particle. Spectral Wasserstein penalizes the global matrix norm of the displacement covariance — particles are forced to interact collectively. This is the geometric insight behind the Muon optimizer: spectral normalization of gradients respects the matrix structure of weight parameters.
2. The identification of Muon dynamics as a gradient flow on Spectral Wasserstein space. The continuous-time Muon step X_{k+1} = X_k - τ ||G_k||_{S_1} Proj_O(G_k) is EXACTLY the gradient flow of the loss functional F in the W_{γ_∞} geometry. This connects an empirically successful optimizer to rigorous transport theory.
3. The Gaussian case admits a closed form (Corollary 2.13): the Spectral Wasserstein distance between Gaussians defines a genuine metric on covariance matrices that extends the Bures-Wasserstein metric. For commuting covariances in the Schatten family, the formula is explicit.

**Connections the authors acknowledge**: Villani (optimal transport theory), Benamou-Brenier (dynamic OT), Peyré-Cuturi (computational OT), Chizat-Bach (mean-field training), Gozlan et al. (generalized transport costs), Paty-Cuturi (subspace robust Wasserstein). No connections to QEC, neuroscience, or information theory (beyond general entropy/convexity). Code: https://github.com/gpeyre/spectral-wasserstein.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transport coupling π | Matching (assignment between source and target) |
| Kantorovich formulation | Static matching (couplings) |
| Monge restriction | Deterministic matching (transport maps) |
| Benamou-Brenier formulation | Dynamic matching (velocity fields + continuity equation) |
| Spectral Wasserstein distance W_γ | Parameterized family of matching costs |
| Schatten norm index p | Parameter controlling matching geometry |
| Displacement covariance | Global coupling structure of the matching |
| Muon geometry (p=∞) | Operator-norm matching = max-eigenvalue cost |
| Classical W2 (p=1) | Trace-norm matching = sum-of-eigenvalues cost |
| Geodesic convexity | Stability of interpolations in matching geometry |
| Mean-field gradient flow | Continuous dynamics on the space of matchings |

**See also**: `by-domain/tda.md`, `by-domain/dynamical_systems.md`, `by-structure/optimal_transport.md`, `atlas/MATCHING.md`, `atlas/STABILITY.md`

---

## arXiv: 2604.04655 --- Wang (2026)
**"Grokking as Dimensional Phase Transition in Neural Networks"**
Ping Wang, Institute of High Energy Physics, Chinese Academy of Science, Beijing. April 2026.

**Domain(s)**: Dynamical Systems (self-organized criticality, gradient dynamics)

**Abstract machines instantiated**:

- **Stability**: THE central machine. The paper identifies grokking — the abrupt memorization-to-generalization transition — as a dimensional phase transition. The effective dimensionality D, extracted via finite-size scaling of gradient avalanche dynamics, crosses from sub-diffusive (D ≈ 0.90, pre-grokking) through the random-diffusion baseline (D = 1) to super-diffusive (D ≈ 1.20, post-grokking). This crossing IS a stability boundary: below D = 1, gradient perturbations are spatially confined (sub-extensive cascades); above D = 1, perturbations amplify collectively (super-extensive cascades). The phase transition is validated by three non-overlapping bootstrap distributions (10,000 resamples each) with D_pre = 0.90 ± 0.02, D_post = 1.20 ± 0.02, D_synth = 0.99 ± 0.01.

- **Null hypothesis**: Synthetic i.i.d. Gaussian gradients (g_i ~ N(0, 0.5²)) serve as the explicit null model. Under this null, D_synth = 0.99 ± 0.01 across all network topologies (5 types × 6 seeds, CV < 0.3%). This is the random-diffusion baseline: if gradients have no learned structure, the effective dimensionality is exactly 1 regardless of network architecture. Real training deviates from this null in both directions — sub-diffusive before grokking, super-diffusive after. The D(t) crossing through D = 1 at the grokking epoch is the signature that rejects the null.

- **Parameterized homology**: D(t) evolves continuously during training (Fig. 1b), tracing a trajectory from D ≈ 0.90 through a multi-scale critical window to D ≈ 1.20. The effective dimensionality is extracted at each epoch via finite-size scaling of s_max ~ N^D across 8 model scales (N = 81–2001, spanning 1.4 decades). This is a parameterized observable: the training epoch t parameterizes a family of gradient geometries, and D(t) tracks the topological/geometric phase of the system.

- **Chain complex (weak)**: Parameters are mapped onto a Barabási-Albert scale-free network (m=2, ⟨k⟩=4). The Threshold-based Diffusion Update (TDU-OFC) propagates gradients along edges when |g_i| > τ (90th percentile threshold). The network Laplacian governs diffusion, and the cascade structure — which nodes fire, in what order — encodes the combinatorial topology of the gradient flow. The avalanche size s (total triggered updates) is the 0-dimensional analogue of a persistent feature.

**What is genuinely new (not reducible to shared abstraction)**:
1. First identification of grokking as a DIMENSIONAL phase transition governed by self-organized criticality. Previous explanations (circuit formation, representation learning, phase-transition-like dynamics) were qualitative. This is quantitative: D crosses from 0.90 to 1.20 with R² > 0.99 across 1.4 decades of system size.
2. The key finding that D reflects gradient field geometry, NOT network architecture. Five different network topologies (Ring, SW p=0.05, SW p=0.2, Scale-Free, Random) all produce D_synth ≈ 0.99 for synthetic Gaussian gradients (CV < 0.3%). The topology-invariance rules out architecture as the cause of the dimensional crossing.
3. Companion study [11] independently confirms the identical D(t) signature in canonical grokking (Transformer on ModAdd-59, 80/20 train/test split), establishing that the gradient mechanism generalizes beyond XOR to standard grokking settings.

**Connections the authors acknowledge**: Bak-Tang-Wiesenfeld (SOC, sandpile models), Olami-Feder-Christensen (earthquake model, threshold dynamics), Beggs & Plenz (neuronal avalanches), Chialvo (brain criticality), Sethna-Dahmen-Myers (crackling noise), Onsager (phase transitions), Goldenfeld (renormalization group). The connection to neuronal avalanches [9,10] is explicit — gradient avalanches in NNs are directly analogous to neuronal avalanches in cortex. No connections to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Effective dimensionality D | Parameterized observable tracking geometric phase |
| Finite-size scaling (FSS) | System-size parameterized analysis (N = 81–2001) |
| Gradient avalanche | Cascade = topological event in gradient flow |
| s_max ~ N^D | Scaling relation = stability diagnostic |
| D = 1 crossing | Phase transition = stability boundary |
| Sub-diffusive (D < 1) | Confined cascades = stable regime |
| Super-diffusive (D > 1) | Amplifying cascades = unstable/generalized regime |
| Synthetic Gaussian gradients | Null model (D_synth = 0.99 ± 0.01) |
| TDU-OFC | Threshold diffusion = discrete dynamical system on network |
| Barabási-Albert graph | Combinatorial substrate for gradient propagation |
| Grokking epoch | Critical time at which D(t) crosses the null |
| Topology invariance (CV < 0.3%) | Universality of the null across architectures |

**See also**: `by-domain/dynamical_systems.md`, `atlas/STABILITY.md`, `atlas/NULL_HYPOTHESIS.md`
