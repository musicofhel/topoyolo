## takens-1981 --- Takens (1981)
**"Detecting strange attractors in turbulence"**
Lecture Notes in Mathematics, vol. 898, Springer, pp. 366-381

**Domain(s)**: Dynamical systems

**Abstract machines instantiated**:
- **Chain complex (implicit)**: The delay embedding theorem guarantees that for a generic pair (diffeomorphism phi, observation function y) on a compact manifold M, the delay map F(x) = (y(x), y(phi(x)), ..., y(phi^{2d}(x))) is an embedding of M into R^{2d+1}. The reconstructed manifold F(M) is diffeomorphic to M and therefore has identical homology: H_k(F(M)) = H_k(M) for all k. The chain complex of M is preserved under embedding, though it is never explicitly constructed -- the theorem guarantees existence, not computation. This is the foundational result that makes topological analysis of time series possible: you can recover the topology of an unknown attractor from a single scalar observable.
- **Stability**: The embedding is GENERIC: it holds for a residual (topologically generic) set of pairs (phi, y) in the C^2 topology. This is a topological robustness result -- the embedding persists under small perturbations of both the dynamics and the observation function. Generic = open and dense, so the set of "bad" pairs (where embedding fails) is meager (first Baire category). This is structural stability in the sense of dynamical systems: the qualitative (topological) properties of the reconstruction are robust.
- **Parameterized homology (weak)**: The embedding dimension d serves as a parameter. For d < dim(M), the delay map generically fails to be injective (self-intersections in the reconstruction). For d > 2·dim(M), it generically succeeds. The transition from unfaithful to faithful reconstruction as d increases is a discrete analogue of a filtration: the topology of the reconstructed object changes at a critical parameter value. However, Takens does not track this parametric dependence explicitly.

**What is genuinely new (not reducible to shared abstraction)**:
- The delay embedding construction itself: a SINGLE scalar time series y(x(t)) suffices to reconstruct the full topology of the attractor, provided the observation is generic. No other domain has this property -- in TDA you start with point clouds, in QEC you have direct access to the code space.
- The genericity condition is C^2-topological, not measure-theoretic. This is weaker than Sauer et al.'s later prevalence result but historically came first and shaped the field.
- The theorem applies to diffeomorphisms (discrete dynamics). The continuous-time extension (flows) requires one additional embedding dimension due to the trivial direction along the trajectory.
- No algorithm is given for determining the correct embedding dimension d or delay tau from data -- the theorem is purely existential. Practical methods (false nearest neighbors, mutual information) came later.

**Connections the authors acknowledge**: Situated in the dynamical systems / ergodic theory tradition (Smale, Ruelle). The "turbulence" in the title connects to fluid dynamics. No connections to TDA (which did not exist in 1981), QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Delay map F | Topology-preserving embedding |
| Observation function y | Observable (analogous to cochain) |
| Diffeomorphism phi | Dynamics (discrete time map) |
| Embedding dimension 2d+1 | Sufficient parameter for faithful reconstruction |
| Generic pair (phi, y) | Structurally stable configuration |
| Compact manifold M | The space (attractor) |
| Strange attractor | Invariant topological object with non-integer dimension |
| Residual set | Topologically generic (open dense) |
