## annurev-statistics-030718-104938 — Panaretos & Zemel (2019)
**"Statistical Aspects of Wasserstein Distances"**

**Domain(s)**: information theory (statistics), TDA

**Abstract machines instantiated**:
- **Matching**: Wasserstein distances ARE optimal transport — the metric measures the minimal cost of reassigning probability mass from one distribution to another. W_p(μ,ν) = inf_{γ ∈ Γ(μ,ν)} (∫ c(x,y)^p dγ)^{1/p}, where the infimum is over all couplings (joint distributions with correct marginals). The review covers: Monge (deterministic) vs Kantorovich (probabilistic) formulations, dual formulations via Lipschitz functions, Brenier's theorem (optimal map = gradient of convex function), and computational methods (Sinkhorn, linear programming). Every Wasserstein computation IS a matching problem.
- **Stability**: Wasserstein distances metrize weak convergence AND convergence of moments — stronger than weak convergence alone. They are "well-adapted to quantify a natural notion of perturbation of a probability distribution." Key stability results: sample complexity bounds (convergence rates of empirical Wasserstein distances), central limit theorems for W_p, and dimension-dependent convergence rates (curse of dimensionality for d ≥ 3).
- **Parameterized homology**: The order p parameterizes the family of Wasserstein distances W_p. Different p values emphasize different aspects of distributional difference: W_1 (Earth mover's distance) captures location, W_2 (quadratic cost) connects to Riemannian geometry of the Wasserstein space, W_∞ (bottleneck) connects to PH stability theorems. The Wasserstein barycenter problem parameterizes a family of "average" distributions. Rate-distortion and channel capacity problems are OT problems parameterized by distortion/rate.

**What is genuinely new (not reducible to shared abstraction)**:
- The comprehensive unification of OT as a statistical tool: convergence rates, CLTs, minimax estimation, goodness-of-fit testing, all through the Wasserstein lens. This connects OT to the full statistical inference toolkit.
- The geometric perspective: Wasserstein space as an infinite-dimensional Riemannian manifold (Otto calculus), connecting OT to differential geometry. Displacement interpolation (McCann) provides geodesics.
- Statistical challenges unique to Wasserstein: the curse of dimensionality (convergence rate O(n^{-1/d}) for d ≥ 3), regularization strategies (entropic, sliced, projection), and the distinction between estimation and testing.
- The paper notes Wasserstein's deep connection to PH stability: the bottleneck distance on persistence diagrams IS a W_∞ distance. This bridge to TDA is acknowledged but not elaborated.

**Connections the authors acknowledge**: Cite Villani, Rachev-Rüschendorf for OT foundations. Note connection to PH stability (bottleneck = W_∞). Cite applications in Bayesian computation, generative models (Wasserstein GANs), and causal inference. Bridge statistics and OT theory. Do NOT cite QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Wasserstein distance W_p | Optimal matching cost (p-th order) |
| Coupling γ ∈ Γ(μ,ν) | Joint distribution with correct marginals |
| Optimal transport map T | Deterministic matching (Monge) |
| Kantorovich relaxation | Probabilistic matching |
| Brenier's theorem | Optimal map = gradient of convex function |
| Wasserstein barycenter | Fréchet mean in matching-metric space |
| Entropic regularization (Sinkhorn) | Smoothed matching (computational approximation) |
| Convergence rate O(n^{-1/d}) | Sample complexity of the matching metric |
| Displacement interpolation | Geodesic in matching space |
| Bottleneck distance | W_∞ (PH stability distance) |

**See also**: `by-domain/information_theory.md`, `by-domain/tda.md`, `by-structure/optimal_transport.md`, `by-structure/phase_transitions.md`
