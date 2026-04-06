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

---

## Living Document

Add divergences as they are discovered. Each entry should specify: which two domains are being compared, what the apparent synonym is, and precisely where the correspondence fails.
