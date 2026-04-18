# Boundary Operators (Chain Complex)

Papers instantiating the **chain complex** abstract machine: boundary operators with ∂²=0, cycles as kernel of ∂, boundaries as image of ∂, homology as ker/im.

The shared pattern: there is a graded algebraic object (simplicial complex, code complex, factor graph) with maps between grades satisfying ∂² = 0. The kernel of ∂ (cycles/syndromes/periodic orbits) and the image of ∂ (boundaries/trivial syndromes) define homology classes that carry topological meaning.

---

## Statistical Physics / Information Theory

### Mézard & Mora (2008) — Constraint Satisfaction
LDPC parity-check matrix H as boundary operator over GF(2). Codewords are ker(H), syndromes are im(H). Factor graphs generalize the chain complex structure. Full annotation: `by-domain/information_theory.md`.

### Baudot & Bennequin (2015) — The Homological Nature of Entropy
Information structures as simplicial complexes. k-simplices = k-tuples of random variables. Coboundary δ maps (k-1)-information functions to k-information functions, δ²=0. Shannon entropy H is a 1-COCYCLE: the chain rule IS the cocycle condition δH=0. Exact identification, not analogy. Extends to Tsallis/Rényi as deformed cocycles. Full annotation: `inbox.md`.

### Bradley (2021) — Entropy as a Topological Operad Derivation
Shannon entropy = unique derivation (up to scalar) of the operad of topological simplices. Strengthens Baudot-Bennequin: not only is H a cocycle, it's the ONLY one satisfying operad derivation axioms. Category-theoretic chain complex perspective. Full annotation: `inbox.md` (arXiv: 2107.09581).

### Sugiyama, Nakahara & Tsuda (2016) — Information Decomposition on Structured Space
Dual θ/η coordinates on posets as order-theoretic chain complex. Möbius function as boundary operator. Principal ideals (↓x) and filters (↑x) as ∂ and δ supports. Pythagorean theorem for KL divergence decomposes interactions by level. Full annotation: `by-domain/information_theory.md`.

---

## TDA

### Mollers, Immer, Fortuin, Isufi (2023) — Hodge-Aware Contrastive Learning
Full chain complex on simplicial complexes of order 2. Incidence matrices B_1 (node-to-edge) and B_2 (edge-to-triangle) ARE the boundary operators. Hodge Laplacians L_k built from ∂ and ∂^T. The Hodge decomposition R^{N_1} = im(B_1^T) + im(B_2) + ker(L_1) is the chain complex decomposition into coboundaries + boundaries + homology. The contrastive learning objective preserves this decomposition in the embedding space. Full annotation: `by-domain/tda.md`.

### Kanjamapornkul, Pincak, Bartos (2020) — Cohomology Theory for Financial Time Series
Khovanov cohomology (categorification of Jones polynomial) on financial time series. Cochain groups from market microstructure states. Coboundary operators from knot/link structure of figure-eight hyperbolic knots. delta^2 = 0 from standard Khovanov construction. Cohomology classifies 8 fundamental market states. Full annotation: `by-domain/tda.md`.

### Bauer (2021) --- Ripser
Vietoris-Rips complex with implicit COBOUNDARY matrix representation. Coboundary is sparse (few cofaces per simplex) vs dense boundary matrix. Apparent/emergent pair optimizations identify persistence pairs without full column reduction. Clearing optimization via homology-cohomology duality. Full annotation: `inbox.md` (arXiv: 2108.03831).

### Peek, Pritam, Skerritt, Chalup (2025) --- TE + Directed PH in Spiking Systems
Directed flag complex from transfer entropy adjacency matrix. Directed k-simplices from consistently oriented (k+1)-cliques. Standard simplicial boundary on oriented simplices. Same construction as Reimann et al. but driven by information-theoretic (TE) coupling rather than synaptic connectivity. Flagser for directed PH computation. Full annotation: `inbox.md` (arXiv: 2508.19048).

## QEC

### Oreshkov (2013) — Continuous-time quantum error correction
Subsystem decomposition H_S = H_A ⊗ H_B ⊕ K as Hilbert-space chain complex. Code subsystem H_A = protected information (cycles); gauge subsystem H_B = correctable errors (boundaries); K = uncorrectable states. Error-correcting map R projects onto code space (projection to ker/im). Correctability condition = functional ∂^2 = 0. Full annotation: `by-domain/qec.md`.

### Kitaev (1997) — Fault-tolerant quantum computation by anyons
Toric code IS a chain complex on T². Qubits on edges (1-cells), X-stabilizers = ∂ (boundary of faces), Z-stabilizers = δ (coboundary of vertices). Logical qubits = H₁(T², ℤ/2). Computation via anyon braiding on the fusion space. Full annotation: `inbox.md` (arXiv: quant-ph/9707021).

### Dennis, Kitaev, Landahl, Preskill (2002) — Topological quantum memory
Surface codes with explicit recovery protocols. Qubits on edges, stabilizers from ∂ and δ. Threshold maps to 3D Z₂ lattice gauge theory. Full annotation: `inbox.md` (arXiv: quant-ph/0110143).

## Neuroscience

### Giusti, Pastalkova, Curto, Itskov (2015) — Clique topology reveals intrinsic geometric structure in neural correlations
Order complex from pairwise correlations of hippocampal pyramidal neurons. Vertices = neurons; k-cliques become (k-1)-simplices. Boundary operators are standard simplicial ∂. Key property: topological features depend only on rank ordering of correlations (invariant under monotone nonlinear transformations). Detects geometric structure invisible to eigenvalue methods. Structure persists during non-spatial behaviors (wheel running, REM sleep). Null model: random matrices. Full annotation: `inbox.md` (arXiv: 1502.06172).

### Reimann, Nolte, Scolamiero, Turner, Perin, Chindemi, Dłotko, Levi, Hess, Markram (2017) — Cliques of Neurons Bound into Cavities Provide a Missing Link between Structure and Function
DIRECTED simplicial complexes from synaptic connectivity in reconstructed rat neocortex (~31,000 neurons, ~8M connections). Directed k-simplex = clique of (k+1) neurons with single source and sink, encoding information flow direction. Standard simplicial ∂ on oriented simplices. Finds directed simplices up to dimension 6-7 (~80M directed 3-simplices), vastly exceeding Erdős-Rényi null. Stimulus triggers hierarchical cavity formation over time. Full annotation: `inbox.md` (DOI: 10.3389/fncom.2017.00048).

### Dabaghian, Mémoli, Frank, Carlsson (2012) — A Topological Paradigm for Hippocampal Spatial Map Formation Using Persistent Homology
Temporal nerve complex T(t) from place cell co-firing. Vertices = place cells; k cells co-firing within a theta cycle span a (k-1)-simplex. Complex grows with exploration. PH tracks Betti numbers (b₀ = components, b₁ = loops/obstacles). Identifies "learning region" in parameter space where correct environment topology is recovered in 2-5 minutes. Full annotation: `inbox.md` (DOI: 10.1371/journal.pcbi.1002581).

### Curto & Itskov (2008) — Cell Groups Reveal Structure of Stimulus Space
Nerve complex from place cell co-firing groups (250ms windows). The Nerve Theorem guarantees: homology of nerve complex = homology of stimulus space (given convex receptive fields). H₁ counts obstacles/holes. Geometric reconstruction via shortest-path distances on cell-group graph achieves ~3% accuracy with 120-140 cells. Robust to 10% spike-timing noise. Full annotation: `inbox.md` (DOI: 10.1371/journal.pcbi.1000205).

### Gardner, Hermansen, Pachitariu, Burak, Baas, Dunn, M. Moser, E. Moser (2022) — Toroidal topology of population activity in grid cells
Persistent cohomology on Neuropixels recordings of hundreds of grid cells reveals the population activity manifold is a torus T². The torus has H₁(T²,Z) = Z² — two independent 1-cycles encoding two spatial dimensions. This is the SAME homological structure as Kitaev's toric code, where H₁(T²,Z/2) = (Z/2)² defines two logical qubits. The chain complex is constructed via PH on the population activity point cloud. Toroidal structure persists across environments and wake-to-sleep transitions, consistent with CAN models. The torus is a population-level object invisible from individual cell marginals. Full annotation: `inbox.md` (DOI: 10.1038/s41586-021-04268-7). **Bridge**: neuro ↔ QEC via shared T² — see `cross_domain_bridges.md`.

---

## Cross-domain observation

The chain complex machine appears in five distinct incarnations across the first/second-pass papers (see "Phase 2" and "Third Pass" sections below for the expanded 7-incarnation taxonomy):

1. **Geometric (TDA — Mollers et al.)**: Incidence matrices B_k on simplicial complexes. ∂ maps k-simplices to (k-1)-simplices. Homology = topological features of the data. Hodge decomposition = gradient + curl + harmonic.

2. **Algebraic (QEC — Oreshkov)**: Subsystem decomposition of Hilbert space. The "boundary" is the error map; "cycles" are code states; "homology" = logical qubits (protected information).

3. **Categorified (TDA/Finance — Kanjamapornkul et al.)**: Khovanov cohomology on knot diagrams derived from time series. Coboundary from knot crossings. Cohomology classifies market states.

4. **Combinatorial (Information theory — Sugiyama et al.)**: Mobius function on posets. ∂ is inclusion-exclusion. Orthogonal decomposition of D_KL mirrors Hodge orthogonality.

5. **Neural (Neuroscience — Giusti, Reimann, Dabaghian, Curto & Itskov)**: Simplicial complexes from neural co-activity or synaptic connectivity. Two sub-flavors: (a) UNDIRECTED clique/nerve complexes from co-firing (Giusti, Dabaghian, Curto & Itskov) — the Nerve Theorem guarantees homology = stimulus space topology; (b) DIRECTED simplicial complexes from synaptic connectivity (Reimann) — orientation encodes information flow direction. Both use standard simplicial ∂, but the directed version is closer to oriented chain complexes in algebraic topology.

The Hodge decomposition appears in both the TDA and information theory contexts with the same orthogonality structure.

---

## From Second Pass + Bridges

### Factor Graphs / CSP
- **Amizadeh et al. (2019) PDP** — Factor graph message passing as proto-chain complex. Variable→factor = forward boundary; factor→variable = adjoint. `second_pass.md` SP-10.

### Spectral / Graph
- **Shang & Sun (2019)** — Graph Laplacian as 0th Hodge Laplacian for Hawkes process networks. Spectral convolutions respect chain structure. `second_pass.md` SP-06.
- **Bennett et al. (2022)** — Hermitian adjacency matrix for directed lead-lag networks. Oriented 0th Hodge operator. `second_pass.md` SP-14.
- **Simpson et al. (2013)** — Brain network graph Laplacian, clustering, community structure as 0-skeleton invariants. `second_pass.md` SP-15.

### Quantum / Topological
- **Pati & Sanders (2005)** — Bloch sphere S² has H₂(S²)=Z. No CPTP map can reduce this. Topological dimension as absolute invariant. `cross_domain_bridges.md`.
- **Tarnowski et al. (2019)** — Chern number as fiber bundle invariant. Ground-state band structure = chain complex of Bloch states over Brillouin zone. `second_pass.md` SP-12.

### Algebraic Decomposition
- **Napolitano (2026)** — gl(4,R) Lie algebra Casimir decomposition. Not boundary operators strictly but graded eigenspace decomposition. `second_pass.md` SP-11.
- **Oladyshkin et al. (2023)** — Polynomial chaos orthogonal decomposition graded by interaction order. Parallel to Hodge decomposition. `cross_domain_bridges.md`.

---

## Third Pass (2026-04-05)

### Condensed Matter / QEC

**Arovas & Zhang (1992) — FQHE**: Chern-Simons gauge theory on genus-g surface. Ground state degeneracy = dim(H₁(Σ_g, ℤ/n)). Wilson loops as cycle evaluation. The original physical system where topological order was identified. Full annotation: `third_pass_neuro_qec.md` (TP-05).

**Barandes (2023) — Stochastic-Quantum Correspondence**: Functorial mapping between stochastic (Markov chain) and quantum (unitary) categories. Tensor products preserved. The correspondence IS a chain-complex-level equivalence between two algebraic structures. Full annotation: `third_pass_neuro_qec.md` (TP-06).

### Dynamical Systems

**Thai Stock Market de Rham Cohomology**: de Rham cohomology on correlation matrices. Exterior derivative d as boundary operator, d²=0 as chain complex condition. Wilson loops detect non-trivial topology. Chern-Simons currents. Full annotation: `third_pass_dynamics_tda.md` (TP-02).

**Ensemble Control on Lie Groups**: Cartan decomposition g = k + p as Z/2-graded chain complex. Bracket relations [k,k]⊂k, [k,p]⊂p, [p,p]⊂k define the grading. Covering method builds full group from graded pieces. Full annotation: `third_pass_dynamics_tda.md` (TP-12).

**Pointwise Ergodic Theorem (Fuchsian Groups)**: Bowen-Series coding maps group action to symbolic dynamics. Irreducible transition matrix defines a directed 1-complex. Full annotation: `third_pass_dynamics_tda.md` (TP-16).

### Pure Math / TDA

**Hom-Lie Algebra Cochain Complexes**: Explicit construction of cochain complex C^n(g, M) with δ²=0 for hom-Lie algebras. Twisting map α parameterizes family; α=id recovers Chevalley-Eilenberg. H² controls deformations, H³ gives obstructions. Full annotation: `third_pass_dynamics_tda.md` (TP-14).

**Higher-Order Network Compression (PRL)**: k-body interactions as k-simplices. Information-theoretic criterion for which orders carry genuinely new information vs being determined by lower orders (exact chains). Full annotation: `third_pass_dynamics_tda.md` (TP-10).

### Information Theory

**Multivariate Redundancy (Chicharro 2017)**: Rooted-tree decomposition of MI as hierarchical chain. Each node implements binary unfolding with maximum entropy constraints. The tree is a graded structure from total MI to individual atoms. Full annotation: `third_pass_infotheo_cross.md` (TP-04).

**HSIC-Bottleneck Orthogonalization**: Layer-wise orthogonal projection creates bigraded (layer × task) structure. Gradient orthogonalization structurally identical to Hodge decomposition. Full annotation: `third_pass_infotheo_cross.md` (TP-09).

### Phase 2 (2026-04-06)

**Freedman, Kitaev, Larsen, Wang (2001) — Topological Quantum Computation**: arXiv: quant-ph/0101025. Quantum computation from anyonic systems = unitary topological modular functors (Witten-Chern-Simons). Fusion rules generalize boundary operators. Braiding as categorified chain complex composition. Error rate e^{-αℓ} via topological protection. Full annotation: `inbox.md`.

**Bombin & Martin-Delgado (2007) — Statistical Mechanical Models and Topological Color Codes**: arXiv: 0711.0468. Color codes on trivalent lattices with Z₂×Z₂ gauge group. Overlap with factorized state = 3-body Ising partition function. Different cellulation from toric code, same homological machinery but richer transversality (direct Clifford gates). Full annotation: `inbox.md`.

**Berry et al. (2023) — Quantum Advantage in TDA**: arXiv: 2209.13581. The chain complex in its purest COMPUTATIONAL form. Boundary operators dG_k on clique complexes, combinatorial Laplacian Delta = dG^{dagger} dG + dG dG^{dagger}, Dirac operator BG = dG + dG^{dagger}. Betti number = dim(ker(Delta)). The quantum algorithm projects onto ker(BG) restricted to k-chain subspace. Direct TDA-QEC bridge: quantum algorithm computes TDA's chain complex invariants. Full annotation: `inbox.md`.

**Hastings & Haah (2021) — Floquet Code (Honeycomb Code)**: arXiv: 2107.02194. Honeycomb cellular complex on T^2. Qubits on vertices (0-cells), 2-qubit Pauli checks on edges (1-cells), hexagonal plaquettes (2-cells). Product of checks on any 1-cycle = stabilizer; plaquette stabilizers = boundaries. As subsystem code: 0 logical qubits (all homology is trivial). With periodic measurement schedule: 2 logical qubits from H_1(T^2, Z/2). DYNAMICAL chain complex: the boundary structure changes each round (different edge subset measured). Syndrome in 2+1D spacetime forms cubic lattice for MWPM decoding. Full annotation: `inbox.md`.

### Cross-Domain Observation

The chain complex now has **7 incarnations** (expanding from 6 in third pass), with incarnation 7 now having three sub-flavors:
1. **Geometric** (simplicial/cellular) — TDA (Ripser/Bauer 2021 uses coboundary dual), QEC toric codes
2. **Algebraic** (Lie algebra cohomology, Cartan decomposition) — pure math, control theory
3. **Categorified** (Khovanov, modular functors) — knot theory, topological quantum computation
4. **Combinatorial** (PID lattice, factor graphs) — information theory
5. **Gauge-theoretic** (de Rham, Chern-Simons, Wilson loops) — financial topology, FQHE
6. **Graded-informational** (k-body information, bigraded layers) — higher-order networks, continual learning
7. **Neural** — three sub-flavors: (a) undirected clique/nerve complexes from co-firing (Giusti, Dabaghian, Curto & Itskov) where Nerve Theorem guarantees homology = stimulus topology; (b) directed simplicial complexes from synaptic connectivity (Reimann) where orientation encodes information flow direction; (c) directed flag complexes from transfer entropy networks (Peek 2025) where the chain complex is driven by information-theoretic coupling rather than structural connectivity — bridges neural (7) with information theory (4)

---

## Wave 4c (2026-04-06) — Foundational Threshold Theorems

### Breuckmann & Eberhardt (2021) — Quantum LDPC Codes
arXiv: 2103.06309. THE definitive statement that CSS codes ARE chain complexes. C_2 --partial_2--> C_1 --partial_1--> C_0 with partial_1 partial_2 = 0 (equivalently H_Z H_X^T = 0). Physical qubits = 1-cells, Z-stabilizers from partial_2 (faces), X-stabilizers from partial_1^T (vertices). Logical qubits = H_1(C). Code distance = min-weight non-trivial homology class = systole of underlying manifold. Product constructions (hypergraph, tensor, fiber bundle, lifted, balanced) are operations on chain complexes governed by Kunneth formula. Hyperbolic codes exploit Gauss-Bonnet-Chern (curvature determines homology dimension). Full annotation: `papers/inbox.md`.

### Aharonov & Ben-Or (1997/1999) — CSS and Polynomial Codes
arXiv: quant-ph/9906129. CSS codes defined by orthogonality condition H_Z H_X^T = 0 = chain complex condition. Polynomial codes over F_p: codewords are superpositions of polynomial evaluations, degree d filtration provides graded algebraic structure. Fault-tolerant procedures systematically derived from algebraic properties of the polynomial ring. Full annotation: `papers/inbox.md`.

### Knill, Laflamme, Zurek (1998) — 7-Qubit Steane Code
arXiv: quant-ph/9702058. The 7-qubit code based on [7,4,3] Hamming code. Q^{tensor 7} = A tensor S decomposition: A = logical qubit (homology class), S = syndrome space (cokernel). Six stabilizer observables S_1...S_6 (tensor products of Pauli operators) = boundary operators. Syndrome measurement = projection onto code space = projection to ker/im. Normalizer group provides algebraic structure for encoded operations. Full annotation: `papers/inbox.md`.

### Cross-Domain Observation (Updated)

The chain complex incarnation count remains at **7** but incarnation #1 (Geometric/cellular) now has significantly deeper exemplification in QEC: the threshold theorem papers show that the chain complex is not merely a convenient representation — it is the *reason* fault tolerance works. The CSS orthogonality condition partial^2 = 0 is what makes syndrome extraction possible, and the homology dimension determines the number of protected qubits. The product constructions (Breuckmann & Eberhardt) show that operations on chain complexes (tensor product, fiber bundle twist, balanced product) produce new codes with predictable homological properties via the Kunneth formula — the same algebraic tool used in pure algebraic topology.

---

## Wave 10 — link-forge update (2026-04-17)

### Baudot, Tapia, Bennequin & Goaillard (2019) — Topological Information Data Analysis
arXiv: 1907.04242. Simplicial complex Δ([n]) of random variables. Entropy and MI are co-chains. I_2 = coboundary of H (δH = I_2). Topos-theoretic cohomology foundation. Full annotation: `inbox.md` (Wave 10a).

### Ghorbanchian, Restrepo, Torres & Bianconi (2020) — Higher-order simplicial synchronization
DOI: 10.1038/s42005-021-00605-4. Hodge Laplacian L_k from boundary operators B_k. Dynamics ON a chain complex — boundary operator mediates coupling between topological signals on different-dimensional simplices. Full annotation: `inbox.md` (Wave 10a).

### Dey, Mrozek & Slechta (2021) — Conley-Morse graph persistence
arXiv: 2107.02115. Conley index = relative homology H_k(P,E) of index pair. Explicitly chain-level construction on simplicial complexes with face-relation boundary operators. Morse sets annotated with Poincaré polynomials (graded homological fingerprint). Full annotation: `inbox.md` (Wave 10a).

### Petri et al. (2014) — Homological scaffolds of brain networks
DOI: 10.1098/rsif.2014.0873. Weighted clique complex from fMRI correlations. Homological scaffold extracts which edges carry persistent cycles. Chain-level information preserved and re-encoded as network. Full annotation: `inbox.md` (Wave 10a).

### Chaudhuri et al. (2019) — Head direction ring attractor
DOI: 10.1038/s41593-019-0460-x. Population activity traces S^1 ring manifold (H_1 = ℤ). The 1-cycle is the topological invariant of the circuit. Extracted via Isomap dimensionality reduction. Full annotation: `inbox.md` (Wave 10a).

### Chung, El-Yaagoubi, Qiu & Ombao (2025) — From Density to Void
arXiv: 2503.14700. Explicit ∂_k boundary matrices from Intersecting Neighbor Sets algorithm on fMRI correlations. λ_k = N_k / C(p,k) ratio drops to ~10^{-5} for k ≥ 4. Chain complex machinery reveals absence of higher-order structure. Full annotation: `inbox.md` (Wave 10b).

### Dabaghian, Brandt & Frank (2014) — Hippocampal map as topological template
eLife 03476. Nerve complex from place cell co-firing. Topological invariants (H_0, H_1) of the complex encode environment topology. Geometric deformations (track morphing) do not change the chain complex invariants. Full annotation: `inbox.md` (Wave 10b).

### Donato et al. (2016) — PH analysis of Phase Transitions
arXiv: 1601.03641. Rips-Vietoris complex with full ∂_n boundary operators in appendix. Betti numbers β_0, β_1 tracked through filtration. Chain complex formalism applied to configuration space samples from MFXY and φ^4 models. Full annotation: `inbox.md` (Wave 10b).

### Batko, Mischaikow, Mrozek & Przybylski (2019) — Conley Index from Sampled Dynamics
arXiv: 1904.03757. Cohomological Conley index: endomorphism on H*(P_1/P_2, [P_2]) via Leray functor. Cubical homology on binned phase space. Index map matrices on H^1 give explicit symbolic dynamics encoding. Full annotation: `inbox.md` (Wave 10b).

### Lord, Expert, Fernandes, Petri, Van Hartevelt, Vaccarino, Deco, Turkheimer & Kringelbach (2016) — Insights into Brain Architectures from the Homological Scaffolds
DOI: fnsys.2016.00085. Weighted clique complex from resting-state fMRI correlations. Extends Petri et al. 2014 scaffold: boundary operators on weighted simplicial complex mediate scaffold extraction. Chain complex formalism identifies which edges carry persistent cycles. Full annotation: `inbox.md` (Wave 10c).

### Jost & Zhang (2023) — Cheeger inequalities on simplicial complexes
arXiv: 2302.01069. Higher-order Cheeger constants h_k defined via boundary operators on k-chains. Spectral gap of k-Hodge Laplacian L_k = B_k^T B_k + B_{k+1} B_{k+1}^T bounded by h_k. Explicit ∂²=0 chain complex structure underlies the spectral analysis. Full annotation: `inbox.md` (Wave 10c).

### Trinca, Bollauf & Zamir (2024) — n-Dimensional Toric Codes from Lattice Codes
arXiv: 2410.20233. n-dimensional toric codes constructed from lattice codes via chain complex on n-torus T^n. Boundary operators ∂_k on k-cells of the cellular decomposition. Logical qubits = H_k(T^n, Z/2). Extends Kitaev's 2D toric code to arbitrary dimension. Full annotation: `inbox.md` (Wave 10c).

### Curry, DeSha, Hoff, Limberger, Luo & Qin (2022) — Decorated merge trees for persistent topology
DOI: s41468-022-00089-3. Boundary operators on merge tree edge complex. DMT functor preserves chain complex structure from PH module to merge tree. Interleaving of R[x]-modules encodes birth-death via boundary map kernels and images. Full annotation: `inbox.md` (Wave 10c).

### Méndez & Sánchez-García (2020) — Directed Persistent Homology for Dissimilarity Functions
arXiv: 2008.00711. Directed boundary operators on oriented simplices of pre-ordered Rips complex. Asymmetric dissimilarity function drives directed filtration. ∂²=0 on directed chains — same algebraic condition, new geometric content capturing asymmetry. Full annotation: `inbox.md` (Wave 10c).
