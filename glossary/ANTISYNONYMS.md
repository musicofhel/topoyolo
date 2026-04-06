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

---

## Living Document

Add divergences as they are discovered. Each entry should specify: which two domains are being compared, what the apparent synonym is, and precisely where the correspondence fails.
