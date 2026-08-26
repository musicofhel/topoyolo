# ANTISYNONYMS.md

## Where the Analogy Breaks

The point of this file is to prevent the mapping from becoming sloppy. Every shared structure has a boundary beyond which the domains genuinely diverge. These divergences are not failures of the analogy — they are data about which aspects of the abstract machine each domain actually uses.

---

### Coefficient fields matter

TDA typically works over ℝ (persistence images, landscapes) or ℤ/2 (Ripser default). QEC works over ℤ/2 or ℤ/p because qubits are discrete. This is not cosmetic. Over ℤ/2, torsion vanishes and homology is a vector space. Over ℤ, torsion carries information. The "same" chain complex computation produces different answers depending on the coefficient ring. When we say "both compute homology," we must specify: over what?

### Persistence is multi-scale; code distance is single-scale

A persistence diagram encodes the full birth-death spectrum across all filtration values. Code distance is a single number — the minimum weight of a non-trivial logical operator. The QEC threshold is a phase transition at one critical parameter value. Persistence tracks all transitions simultaneously. These are related (both involve parameterized homology) but the objects being computed are different: a diagram vs. a scalar.

### Takens embedding has no QEC analogue

Delay embedding — reconstructing a manifold from a single observable — is specific to continuous dynamical systems. QEC starts with the complex already given (the code's cellulation). There is no "reconstruction from partial observation" step in QEC. This means ATT's entire embedding layer (AMI, FNN, quality gates) has no parallel in the QEC world. The shared structure begins only after the complex is constructed.

### Stability theorems protect different things

The PH stability theorem bounds perturbation of the diagram in terms of Hausdorff distance between input spaces. The QEC threshold theorem bounds logical error probability in terms of physical error rate and code distance. Both say "topology is robust," but the PH version is a Lipschitz bound (continuous, proportional) while the QEC version is an exponential suppression (discontinuous phase transition). The mathematical form of the guarantee is different even though the conceptual claim is similar.

### Entanglement is richer than binding

Calling the binding residual an "entanglement witness" is suggestive but lossy. Entanglement has a full theory: partial trace, Schmidt decomposition, LOCC, entanglement entropy, monogamy. Binding as defined in ATT has: a scalar score, a residual image, and a p-value. The analogy holds at the level of "joint exceeds marginals," but the QEC/QIT side has far more refined structure. Importing that structure into ATT would require defining analogues of partial trace and LOCC for persistence images, which may or may not be meaningful.

### Decoding is causal; diagram matching is not

The JIT decoder must make corrections in real time with incomplete syndrome history. Bottleneck matching on persistence diagrams is a batch computation on fully known inputs. The "just-in-time" constraint — deciding now with partial information — has no analogue in PH distance computation. This is a genuine structural difference, not a vocabulary difference.

### "Cycle" is a false cognate

In algebraic topology, a cycle is an element of ker(∂). In dynamical systems, a cycle is a periodic orbit. These are different objects. A periodic orbit in phase space does correspond to a 1-cycle in the attractor's topology, but the dynamical-systems usage is broader (it includes unstable periodic orbits that don't appear as persistent H₁ features) and narrower (it doesn't include higher-dimensional cycles). Use with care.

### MI divergence has no TDA analogue

In information theory, mutual information between lognormal variables can diverge to infinity at finite variance (Chwilka & Karbowski, 2024). The joint-vs-marginal excess becomes infinite. In TDA, persistence diagrams are always finite (bounded number of birth-death pairs for finite complexes). In QEC, entanglement measures are bounded by the Hilbert space dimension. The possibility of an infinite excess is specific to continuous-variable information theory. When mapping "excess" across domains, the information-theoretic version can blow up where the topological version cannot.

### Möbius function ≠ boundary operator (exactly)

Sugiyama et al. (2016) build chain-complex-like structure on posets using the Möbius function. The analogy is strong: Möbius inversion (μ * ζ = δ) parallels ∂² = 0. But the Möbius function operates on a poset (partial order) while ∂ operates on a simplicial or cell complex (geometric object). A poset can be realized as the face lattice of a simplicial complex, but not every poset arises this way. The information-geometric "chain complex" is more general than the topological one — it works on arbitrary partial orders, not just those with geometric realization.

### Information plane compression ≠ feature death

The "compression phase" in the information plane (I(X;T) decreasing during training) looks like feature death in persistence (a bar ending at a death-time). But Geiger (2021) showed that observed compression is often geometric (representations cluster/shrink) rather than information-theoretic (MI genuinely decreases). The persistence-diagram analogy suggests that lost features are gone; the ML reality is that the "lost" information may still be recoverable from the representation, just harder to estimate. Persistence is exact; information-plane compression can be an artifact of the estimator.

### Continuous vs. discrete error correction

CTQEC (Oreshkov, 2013) models error correction as a continuous Lindblad master equation. Discrete QEC (surface codes, toric codes) uses syndrome measurement + conditional unitary at discrete time steps. TDA filtrations are typically discrete (finite simplicial complexes). The continuous-time formulation introduces the Zeno effect (λ⁴/κ² scaling from non-Markovian noise exploitation), which has no analogue in discrete QEC or discrete TDA. The distinction between continuous and discrete parameterization is not just technical — it changes what stability guarantees are available.

### Factor graphs are looser than chain complexes

Mézard & Mora (2008) treat factor graphs as generalized chain complexes. For LDPC codes, the mapping is exact (parity-check matrix = boundary operator). But for general constraint satisfaction (random k-SAT), factor graphs lack the grading and ∂² = 0 property. A factor graph has variable nodes and factor nodes connected by edges, but the composition of two "boundary-like" operations is not generally zero. The chain complex structure is a special case within the broader factor graph formalism.

### Disconnectivity graphs ≈ but ≠ persistence diagrams

Niroomand & Wales (2023) show that disconnectivity graphs from energy landscape theory are mathematically isomorphic to H₀ persistence diagrams (sub-level set persistence). Both track connected components merging as a threshold rises. But the energy landscape tradition computes additional structure: transition states (saddle points), conserved coordinates across minima, and reaction pathways. TDA persistence diagrams do not record what happens at the saddle — only that a merge occurred and at what threshold. The energy landscape version is richer for the specific case of H₀ on scalar functions, but persistence generalizes to all dimensions (H₁, H₂, ...) where energy landscapes have no analogue.

### Hawkes criticality ≠ persistence criticality (exactly)

The Hawkes criticality parameter m (offspring number) at m=1 looks like a birth/death event in persistence: the process transitions from subcritical (Brownian limit) to supercritical (explosive). But in persistence, features are born and die at specific scales; in Hawkes, m=1 is a single global phase transition affecting the entire process. Persistence is multi-scale (many births and deaths at different ε); Hawkes criticality is single-scale (one transition at m=1). The structural parallel is real but the multiplicity is different.

### Phase (circular) TE ≠ real-valued TE

Phase transfer entropy (Lobier et al., 2014) operates on S^1-valued phase time series extracted by Morlet filtering. Standard TE operates on real-valued (R-valued) signals. The circular variable structure means phase wraps around: 0 and 2π are the same state. Euclidean distance-based estimators (kNN, kernel) are not directly applicable without modification for circular topology. More importantly, phase extraction discards amplitude information by design — this is a feature for oscillatory neural systems (isolates coupling from power) but a loss for general information-theoretic analysis. The "same" TE computation gives different results depending on whether the input is real-valued or phase-valued, even for the same underlying signal. Similarly, continuous-time TE (Shorten et al., 2021) operates on point processes (discrete events in continuous time), where the estimand is fundamentally different from discrete-time binned TE — the latter does not even converge to the correct value.

### Quantum no-partial-erasure ≠ classical stability

Pati & Sanders (2005) prove quantum information cannot be partially erased — the topological dimension of the Bloch sphere is absolutely invariant under all CPTP maps. Classical stability theorems (PH, IB generalization bounds) provide bounds that can be violated at cost; quantum no-partial-erasure is a hard impossibility. There is no "graceful degradation" in quantum information — you either preserve all of it or map to a fixed state. This is categorically stronger than any continuous stability guarantee.

### Three orthogonal decompositions — same structure, different spaces

Hodge decomposition (simplicial complexes), KL-Pythagoras (posets), and polynomial chaos expansion (stochastic spaces) all decompose signals into orthogonal graded components. But they operate on different mathematical spaces: Hodge on cochain complexes, KL on probability manifolds, PCE on L² function spaces. The orthogonality is with respect to different inner products (L² on cochains, Fisher metric, measure-theoretic). Calling them "the same" requires specifying a functor between the categories — which no one has done.

### Anti-stability ≠ instability

The spin-boson Born approximation reveals sqrt(alpha) prompt coherence loss at weak coupling — an anti-stability result. This is not the same as dynamical instability (positive Lyapunov exponent) or topological instability (feature death in persistence). Anti-stability means the standard stability estimate is wrong in a specific direction: the true decoherence is worse than the linearized bound predicts. A system can be dynamically stable (bounded trajectories) while exhibiting anti-stability (perturbation effects scale non-linearly). The TDA/dynamical-systems notion of stability is about bounded response; the quantum anti-stability is about the functional form of the bound being wrong.

### Frequency filtration ≠ scale filtration

Three independent neuroscience groups (GC-STCL, driver fatigue GC, nonparametric brain GC) use EEG frequency bands as a filtration parameter for causal networks. This looks like TDA's scale filtration but differs in a critical way: in TDA, increasing ε adds simplices monotonically (the filtration is nested). In neuroscience, changing frequency does NOT produce nested graphs — the alpha-band causal graph is not a subset of the gamma-band graph. Different frequencies reveal genuinely different structures, not progressively coarser views of the same structure. The "filtration" is parameterized but not nested. This matches the Hawkes criticality story (single-scale, not multi-scale) more than the persistence story.

### Distributional code ≠ persistence diagram (despite parameterization)

Dabney's dopamine neurons encode quantiles of a probability distribution parameterized by tau ∈ [0,1]. This looks like a persistence diagram parameterized by filtration scale. But persistence diagrams track topological features (born/die); distributional codes track probability mass (quantile levels). The "birth" and "death" events in persistence have no analogue in the distributional code — every quantile exists simultaneously. The parallel is in the parameterization structure, not in the tracked quantity.

### Stochastic-quantum correspondence is exact; other correspondences are approximate

Barandes's stochastic-quantum theorem is an isomorphism, not a bound. Every generalized stochastic system has a unique quantum counterpart and vice versa. By contrast, the TDA-QEC correspondence (chain complexes, parameterized homology) is an analogy — same abstract machine, different instantiations. The PH stability theorem and QEC threshold theorem have the same structure but different proofs and different constants. Treating an exact correspondence and a structural analogy as the same kind of bridge risks collapsing important distinctions.

### Triangulated MI ≠ direct MI

MI-NEE estimates MI by comparing both joint and marginal distributions to a common reference (uniform), then subtracting. MINE compares joint directly to product-of-marginals. Both measure the same quantity (MI) but the estimation paths differ. The triangulation approach has better convergence but introduces a dependence on the reference distribution. In TDA, there is no analogous choice — the bottleneck distance is computed directly, not via a reference. The lesson: joint-vs-marginal excess can be measured directly or via triangulation through a null, and the choice affects computational properties.

### Directed simplicial complexes ≠ undirected simplicial complexes

Reimann et al. (2017) build DIRECTED simplicial complexes from synaptic connectivity, where each simplex has a single source and single sink neuron encoding information flow direction. Standard TDA (Giusti, Dabaghian, Curto & Itskov) builds UNDIRECTED clique/nerve complexes from symmetric co-firing data. The directed version is closer to oriented chain complexes in algebraic topology, but the orientation comes from biology (synaptic directionality), not from an arbitrary choice of orientation. Standard PH software (Ripser, etc.) does not compute homology of directed complexes — the Reimann construction requires specialized tools. The boundary operator is different: in the directed case, ∂ respects the source→sink ordering. This means "neuroscience uses chain complexes" is true but hides a genuine bifurcation within the domain.

### Nerve Theorem guarantee ≠ empirical stability

Curto & Itskov (2008) invoke the Nerve Theorem to provide an EXACT guarantee: if receptive fields are convex, then H_*(nerve complex) ≅ H_*(stimulus space). This is categorically stronger than PH stability (which gives bounded perturbation) or QEC threshold (which gives exponential suppression). The Nerve Theorem is an isomorphism, not a bound. But it depends on an assumption (convexity of receptive fields) that is empirically approximate at best. In practice, the guarantee degrades to an empirical observation that "it works anyway" — more like stability than like a theorem. The gap between the mathematical guarantee (exact, conditional on convexity) and the empirical reality (approximate, without convexity) is itself informative.

### Transfer entropy direction ≠ persistence direction

Schreiber's TE is inherently asymmetric: T_{Y→X} ≠ T_{X→Y}. MI and bottleneck/Wasserstein distances on persistence diagrams are symmetric. The directionality of TE aligns with the directed simplicial complexes (Reimann) more than with standard PH. This suggests a deeper alignment: directional information measures naturally pair with directed topological structures, while symmetric measures pair with undirected structures. The SYNONYMS table's "joint-vs-marginal excess" entry currently conflates directed (TE, Granger) and undirected (MI, binding) versions.

### Cross-Barcode ≠ Wasserstein comparison of two PDs

Barannikov et al.'s Cross-Barcode(P,Q) builds a SINGLE barcode from a pair of distributions, tracking topological discrepancies between their support manifolds. This is NOT the same as computing PD(P) and PD(Q) separately and then measuring their Wasserstein distance. The latter is a Matching operation (optimal assignment between birth-death points); the former is a Joint-vs-marginal operation (what features exist in the pair that don't exist in either alone). The distinction matters: Wasserstein comparison misses features that are topologically equivalent but spatially displaced, while Cross-Barcode detects them.

### Color code Z₂×Z₂ ≠ toric code Z₂

Bombin's color codes use Z₂×Z₂ gauge group on trivalent lattices; Kitaev's toric code uses Z₂ on square lattices. Both instantiate the chain complex machine, but the richer gauge group of color codes enables transversal Clifford gates (toric code cannot). This is a genuine structural difference, not just a vocabulary difference. Error thresholds are similar (~0.109 vs ~0.109), but computational power differs. The chain complex machine is the same; the ALGEBRA acting on it determines what you can compute.

### Attractor ruins ≠ feature death ≠ error threshold crossing

Tsuda's attractor ruins (destroyed attractors that retain geometric influence) look like dead features in a persistence diagram or crossed error thresholds in QEC, but the dynamics are fundamentally different. In TDA, when a feature dies at filtration scale ε, it is gone — no ghost persists. In QEC, when the error rate exceeds threshold, logical information is destroyed without residue. In chaotic itinerancy, the attractor is destroyed by bifurcation but its GHOST continues to trap trajectories transiently. The ruin has no topological "bar" (it is not a well-defined homology class) and no error correction analogue (there is no code protecting it). The quasi-stability of attractor ruins is a dynamical phenomenon — trajectory trapping by a non-existent invariant set — that has no parallel in the static/discrete frameworks of TDA or QEC. When mapping "stability" across domains, Tsuda's ghost stability is a sixth flavor distinct from Lipschitz bounds, exponential suppression, topological protection, anti-stability, and distribution-free guarantees.

### Topology is rotation-invariant; information is not

Varley et al. (2025) show that rotating a point cloud with PCA does not change its persistent homology (the Rips complex is invariant to isometries) but DOES change its information-theoretic properties (O-information, TC, DTC). A rotated plane has O = -2.819 nat; after PCA rotation, O = 0. The topology is unchanged but the information vanishes. This creates a split: "intrinsic" higher-order information (survives rotation, tied to topology like H2 cavities) vs. "contextual" higher-order information (destroyed by rotation, tied to embedding orientation). TDA sees both the same; information theory sees them as different. The H2-synergy correspondence (rho = -0.55 to -0.65) weakens but does not vanish after PCA rotation -- meaning the correspondence is partially intrinsic but not fully. When we say "TDA and information theory both detect higher-order structure," we must qualify: they agree on the intrinsic part (cavities, knots) but diverge on the contextual part (embedding-dependent correlations).

### O-information sign ≠ PH dimension

Synergy (O < 0) corresponds to H2 cavities; redundancy (O > 0) corresponds to knots (H1 features in 3D). But O-information is a single signed scalar, while persistent homology provides a diagram per dimension. There is no information-theoretic measure that maps to H1 vs. H2 separately -- O-information conflates dimension. A point cloud could have both H1 and H2 features with opposite information-theoretic character (synergistic cavities AND redundant loops), and O-information would report only the balance. The TDA side has finer resolution; the IT side has finer decomposition (TC, DTC, S). Neither subsumes the other.

### Higher-order brain topology: robust (Petri 2014, Reimann 2017) ≠ non-reproducible (Chung 2025)

Petri et al. (2014) found dramatic homological scaffold changes under psilocybin; Reimann et al. (2017) found directed simplices up to dimension 6-7 in Blue Brain. Both suggest rich higher-order structure. Chung et al. (2025, arXiv: 2503.14700) show the opposite: in HCP fMRI data (116 regions, 100 subjects), the ratio λ_k of observed to possible k-simplices drops below FDR significance after dimension 3 (λ_3 = 4.54 × 10^{-4}). Overlap probability across subjects decays exponentially: 3-simplices vanish beyond 10 subjects. The divergence has three possible explanations: (1) methodological — correlation-based networks are either too dense (masking gaps) or too sparse (destroying simplices), creating a density-void dilemma that Rips filtrations on point clouds don't face; (2) statistical — none of the prior studies controlled for multiple comparisons across C(p,k) possible k-subsets; (3) scale — Reimann uses simulated high-resolution connectivity (31K neurons), while Chung uses parcellated fMRI (116 regions). The resolution may determine whether higher-order structure is detectable. When claiming "brain networks have higher-order topology," specify: which data type, which construction, and whether it survives cross-subject replication.

### Matching metric ≠ stability guarantee (the duality is proven, not definitional)

The atlas pairs Matching and Stability wherever barcodes appear: the bottleneck/Wasserstein distance between diagrams IS the quantity the stability theorem bounds. Three batch-005 papers sharpen what that pairing actually is — and where it breaks.

**Where it holds — and how tightly.** Bubenik & Scott (1205.3669) categorify: interleavings generalize bottleneck matchings, so stability becomes a property of the indexing category rather than a per-construction inequality. Gulen & McCleary (2201.06650) unify interleavings and matchings under one Galois-connection formalism (Rota's theorem ⇒ easier bottleneck-stability proof). Broomhead & Pirashvili (2506.02999) go furthest: for circle-valued persistence modules, the interleaving distance and the bottleneck distance are not merely comparable — they are ISOMETRIC. So within TDA's parameterized-homology setting, "Matching = Stability" is a theorem with exact content, not a loose analogy.

**Why it still cannot be read across domains.** The equality lives inside one machine instantiation. Outside it, the two words diverge in kind:

- **QEC**: the matching (MWPM on syndrome defects) is a *computational procedure* whose success the threshold theorem guarantees probabilistically; stability there is exponential suppression, not a metric identity. No isometry-type statement connects decoder cost to protection strength.
- **Statistical physics**: Nakazato–Ito (2103.00503) prove entropy production ≥ L2-Wasserstein path length — the matching cost between time-marginals appears as *dissipated heat*, a lower bound on irreversibility, not a robustness certificate. Same mathematical object (an optimal-coupling cost), opposite semantic role: in TDA it measures how little the invariant moved; in stochastic thermodynamics it measures how much was necessarily burned.

**The rule this forces:** when the table says "bottleneck distance" in the TDA column and something coupling-shaped elsewhere, check whether the quantity is (a) a metric on invariants bounded by a perturbation of inputs (Stability sense), (b) an assignment problem solved by an algorithm (Matching sense), or (c) a transport cost equated with physical dissipation (thermodynamic sense). TDA is currently the only domain where all three coincide exactly — which is itself the finding: the Matching↔Stability duality is a special structure of parameterized homology, not a general property of matchings or of stability.

---

### Exact RG↔DL mapping ≠ correlator-level identity (1410.3831 vs 1906.05212)

Within one domain pair (statistical physics ↔ machine learning), the rg-dl lineage contains its own claim-vs-refutation arc, and the boundary is worth stating precisely. Mehta & Schwab (1410.3831) prove a term-by-term identity between Kadanoff's *variational* RG and an RBM stack — but the identity is architectural: it maps the equations of one coarse-graining step onto one layer's training objective. It does not show that what a trained network actually computes is an RG flow. de Mello Koch, de Mello Koch & Cheng (1906.05212) test exactly that stronger reading with hidden-visible correlator diagnostics on Ising-trained RBMs and find RG-like patterns **and** important differences between RG and deep learning in the same observables.

The apparent synonym — "deep learning performs renormalization" — fails at the level of what is measured versus what is mapped: an exact correspondence between two formalisms at one step is not evidence that the learned representation traverses the same flow as the physical system's RG treatment. The Rosetta rule this forces: for any "X is Y" claim in the corpus, distinguish the mapped formalism (where exactness can hold) from the instantiated dynamics (where only diagnostics can decide). The pairing also fixes how the corpus should read its own founding hypothesis: 1410.3831 states it, 1906.05212 qualifies it, and neither alone is the lineage's position.

---

### Abrupt order-parameter jump ≠ phase transition (2505.10114)

Statistical physics and dynamical systems both say "transition," and both diagnose it from an order parameter moving abruptly. Lee, Kuklinski & Timme (2505.10114) give a named counterexample class: complexified Kuramoto systems exhibit "extreme synchronization transitions" — the order parameter leaps from ~N⁻¹ᐟ² to ~1 immediately past critical coupling, visually indistinguishable from an explosive/discontinuous phase transition — that occur at finite N and are therefore multi-dimensional bifurcations, not thermodynamic-limit transitions.

The null hypothesis this supports: "abrupt jump ⇒ phase transition" is destroyed by exhibiting a mechanism (high-dimensional bifurcation analysis) that produces the identical observable without the thermodynamic structure. The sharp test is the N-scaling of the jump onset — finite-N immediacy is the bifurcation signature. When either domain reports a "transition" in this corpus, the entry should record whether the claim survives this null; the same caution applies to criticality claims in the rg-dl lineage (1410.3831/1906.05212 lean on Ising criticality where the transition is genuine, but the inference pattern is the one this entry polices).

---

### Markov-blanket formalism ≠ established lemma (1906.10184 vs 2001.06408)

Neuroscience (the FEP lineage) supplies its own claim-vs-refutation arc, and the failure is sharper than the rg-dl case: not a qualification of scope but a counterexample. Friston (1906.10184) derives, from Markov-blanket conditional independence plus nonequilibrium steady-state dynamics, a free energy lemma whose payoff is reading internal states as performing Bayesian inference on external states. Biehl, Pollock & Kanai (2001.06408) show the derivation's rewriting steps need unstated assumptions, prove the lemma false by counterexample as stated, and — the part that outlives any single fix — show that "Markov blanket" is defined inequivalently across the lineage's own papers, with variational densities re-parameterized by different variables in newer formulations.

The apparent synonym — "the free energy principle has been derived from statistical mechanics" — fails at definition-stability: an inference licensed by a partition cannot be stronger than the partition, and here the partition is version-dependent within the source lineage itself. The Rosetta rule this forces: when a corpus entry rests on a composite boundary (blanket, coarse-graining, sheaf stalk), record *which* definition of the boundary is load-bearing; two entries using the same term under different definitions are not instances of one machine but of two. The pairing fixes how the corpus reads the fep group: 1906.10184 states the program, 2001.06408 fences what is actually proven, and the corpus position — like rg-dl — is the pair. The null-machinery note: this is the first corpus refutation aimed at a *derivation* rather than an empirical claim, so the null witness is a system, not a surrogate dataset.

### Power-law avalanche scaling ≠ evidence of self-organized criticality (2102.09124 vs 0910.0805 + 1203.0738) — first structured-disagreement entry

The corpus's claim-vs-refutation rule handled pairs; this is its first **three-party structured disagreement**, recorded as a role map rather than a winner:

- **Claim** — Plenz et al. (2102.09124): layered cortex self-organizes to a second-order phase transition; −3/2 avalanche power laws, branching parameter 1, nested oscillations, E/I and dopamine as control parameters.
- **Methodological null** — Touboul & Destexhe (0910.0805): thresholded stochastic processes generically produce apparent power laws under log-log regression that fail Kolmogorov-Smirnov scrutiny; surrogate signals reproduce the scaling. The null attacks the *evidence procedure*, not the phenomenon.
- **Empirical null** — Dehghani et al. (1203.0738): applying the rigorous tests across cat/monkey/human, wake and sleep, unit-defined avalanches scale exponentially and nLFP apparent power laws fail CDF-based checks (bi-exponential fits win). The null reports what the *phenomenon* looks like when the methodological critique is honored.

The two nulls are not redundant: one is analytic/surrogate (the test cannot distinguish), the other empirical (tested properly, the effect is absent). The claim paper is not refuted point-for-point either — Plenz's preparations include the thresholded-LFP measurement channel both nulls indict, but also branching-process and homeostatic evidence outside that channel. The corpus position is therefore **not** "SOC in the brain is false" nor "established"; it is the role assignment plus the load-bearing distinction both nulls force: *power-law-shaped scaling measured by regression ≠ power-law distribution surviving distributional tests*. The apparent synonym — "avalanche power laws show the brain is critical" — fails at evidence-class: a shape observed on log axes is a different kind of object than a fitted and tested tail distribution.

The Rosetta rules this forces: (1) any criticality entry must record which statistical class its scaling claim lives in (regression shape vs tested distribution) — the same discipline as recording which boundary definition is load-bearing in the fep pair above; (2) multi-party disagreements are annotated by ROLE (claim / methodological null / empirical null / mechanism reconciler), each party cross-referencing this entry, so a future fourth party slots into the map instead of restarting the argument. The soc group continues this pattern below with two further angles: 1807.07213 (oscillation-criticality coexistence — dissolves the "theoretically incompatible" premise shared by all three parties) and 1209.3271 (subsampling artifacts — a fourth measurement-channel concern adjacent to the nulls).

---

### GIT semistability ≠ persistence stability (2605.11178 vs math/0604068 lineage)

STABILITY.md now carries three incarnations of the stability claim; incarnations 1 and 3 are the pair most at risk of collapsing into one word, because both are called "stability of the representation." They differ in kind on every axis that matters:

- **What is stabilized.** Persistence stability (Cohen-Steiner–Edelsbrunner–Harer; interleavings per 1205.3669) protects an *invariant computed from data* against perturbation of the input. GIT semistability (Dönmez et al., 2605.11178) is a property of *the learned structure itself* — a point in a representation space judged non-degenerate relative to a group action and a linearization.
- **Quantifier shape.** The TDA theorem is a for-all-perturbations *inequality*: ‖diagram−diagram′‖ ≤ f(‖cloud−cloud′‖), quantitative and graded — diagrams can be more or less stable. Semistability is a *dichotomy*: a point is semistable or it is not; there is no distance-to-instability in the statement, only orbit-closure membership. Two non-isomorphic sheaf geometries can even be S-equivalent — indistinguishable at the invariant level while distinct as points.
- **Failure mode.** TDA instability = the bound is exceeded (perturbation moved the invariant too much). GIT instability = *degeneration*: the geometry flows to the orbit closure of a direct-sum-decomposable, low-complexity summand whose global sections lose discriminative information. Oversmoothing is not "too much perturbation"; it is falling INTO an attractor of the algebraic action.

The apparent synonym — "the stable configuration resists change" — fails at direction of implication. In TDA, stability is something you *prove about a pipeline after the fact*. In GIT, semistability is something you *bias learning toward beforehand* (moment-map-inspired regularizers), precisely because nothing downstream certifies it. That is also why the three incarnations compose rather than substitute (see STABILITY.md): a level-3 certificate (non-degenerate boundary data) says nothing about level-1 robustness (persistence diagram movement), and vice versa — each is blind to the other's failure mode.

The structural null is also native to incarnation 3 and has no TDA analogue: Dönmez et al.'s equal-stalk "stability wall," where every admissible stability functional forces the trivial summand and adaptive stability is vacuous. A Lipschitz bound cannot be vacuous this way — it degrades continuously with constants. The Rosetta rule this forces: when a corpus entry says "stable," record whether the claim is (a) a metric inequality over inputs (incarnation 1), (b) a contraction rate of dynamics (2), or (c) an orbit-closure membership test on the structure (3) — and never read a certificate across levels.

---

## Living Document

Add divergences as they are discovered. Each entry should specify: which two domains are being compared, what the apparent synonym is, and precisely where the correspondence fails.
