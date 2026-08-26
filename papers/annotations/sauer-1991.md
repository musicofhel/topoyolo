## sauer-1991 --- Sauer, Yorke, Casdagli (1991)
**"Embedology"**
Journal of Statistical Physics 65(3-4):579-616

**Domain(s)**: Dynamical systems

**Abstract machines instantiated**:
- **Stability**: The central contribution is replacing Takens' topological genericity (residual sets) with PREVALENCE -- a measure-theoretic notion of "almost every." A property holds for prevalent pairs (phi, y) if the set of exceptions has measure zero in a probe sense (analogous to "Lebesgue almost every" in infinite dimensions). This is strictly stronger than genericity: prevalent sets are always residual, but not vice versa. The embedding theorem holds for almost every delay map in the measure-theoretic sense, not merely the topological sense.
- **Parameterized homology (weak)**: The box-counting dimension d_B(A) of the attractor A determines the minimal embedding dimension: 2·d_B(A) + 1 suffices for prevalent embeddings. Since d_B can be non-integer (fractal attractors), the critical embedding dimension is no longer tied to the integer manifold dimension as in Takens. This extends the parametric dependence: the transition from unfaithful to faithful embedding occurs at d > 2·d_B(A), which can be any real number, making the "filtration" finer-grained than Takens' integer threshold.

**What is genuinely new (not reducible to shared abstraction)**:
- Extension to FRACTAL ATTRACTORS: Takens required a smooth compact manifold. Sauer-Yorke-Casdagli prove embedding for sets of arbitrary (possibly non-integer) box-counting dimension, including fractal attractors, products of fractals, and sets with zero Lebesgue measure.
- Prevalence replaces genericity: this is the measure-theoretic analogue of "open and dense." It avoids pathologies of the topological notion (e.g., meager sets can have full measure). Prevalence later became a standard tool across dynamical systems.
- The box-counting dimension d_B(A) is the operative quantity, not the topological or Hausdorff dimension. This is practically important because d_B is computable from data (Grassberger-Procaccia algorithm) while topological dimension is not.
- The result applies to delay embeddings, projections, and more general observation maps -- unifying several embedding results under one framework.

**Connections the authors acknowledge**: Extends Takens (1981) and Whitney (1936). Cite Grassberger-Procaccia for dimension estimation. No connections to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Prevalence | Measure-theoretic robustness (stability in the measure-zero complement sense) |
| Box-counting dimension d_B | Effective dimension of the attractor (fractal analogue of manifold dimension) |
| Delay embedding | Topology-preserving map (Takens) |
| Fractal attractor | Invariant set with non-integer dimension |
| 2·d_B + 1 | Critical embedding dimension (parameter threshold) |
| Whitney embedding | Smooth manifold case (predecessor) |
| Probe measure | Reference measure for prevalence (infinite-dimensional Lebesgue analogue) |
