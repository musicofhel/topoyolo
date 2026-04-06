# Optimal Transport (Matching)

Papers instantiating the **matching** abstract machine: optimal assignment between features at minimum cost. This includes bottleneck/Wasserstein distances on persistence diagrams, syndrome decoding in QEC, Blahut-Arimoto in information theory, and optimal transport between distributions.

The shared pattern: two sets of features (diagram points, syndrome defects, source/channel symbols) and a cost function. The optimal matching minimizes total cost and defines a distance or a correction.

---

## Statistical Physics / Information Theory

### Mézard & Mora (2008) — Constraint Satisfaction
Belief Propagation as approximate matching on factor graphs. For LDPC codes, reduces to syndrome decoding. Survey Propagation as meta-level matching on the space of surveys. Full annotation: `by-domain/information_theory.md`.

---

## TDA / Algebraic Geometry

### Di Rocco, Eklund, Weinstein (2019) — Bottleneck Degree of Algebraic Varieties
Bottleneck pairs = critical points of squared distance ||x-y||^2 on the variety. This IS an optimal assignment problem: find pairs (x, y) where the line xy is normal to X at both points. Bottleneck degree counts solutions — algebraic complexity of the matching. Formula in Chern classes and polar classes. Controls the reach, which determines topological inference guarantees. Full annotation: `by-domain/tda.md`.

*(See also inbox for Cohen-Steiner bottleneck distance, Adams persistence images)*

## Optimal Transport / Machine Learning

### Bunne, Alvarez-Melis, Krause, Jegelka (2019) — Gromov-Wasserstein GANs
Gromov-Wasserstein distance: second-order optimal transport matching pairwise intra-space distances across incomparable spaces. GW(mu, nu) = inf_pi integral |d_X(x,x') - d_Y(y,y')|^2. Used as GAN loss for cross-domain generation (graph to Euclidean, different dimensions). Orthogonality regularization on adversary. Steerable generation separates topology from geometry. Full annotation: `by-domain/dynamical_systems.md`.

### Dabney, Rowland, Bellemare, Munos (2018) — QR-DQN (Distributional RL)
Wasserstein-1 distance W_1(F,G) = integral |F^{-1}(tau) - G^{-1}(tau)| d(tau) minimized via quantile regression. Distributional Bellman operator contracts in W_infinity. QR-DQN uses N adjustable quantile locations with fixed uniform probabilities. Closes the theory-practice gap from C51 by operating end-to-end under Wasserstein. 33% median improvement on Atari. Full annotation: `by-domain/dynamical_systems.md`.

### Bayraktar & Zhou (2017) — Model-Independent Pricing via Optimal Transport
Martingale optimal transport: given marginals mu_1, ..., mu_n (from call prices), optimize over all martingale couplings. Super-hedging price = worst-case matching cost. Duality: min hedging cost = sup_{Q in M} E_Q[Phi] + U^{-1}(alpha). Shortfall hedging reduces to super-hedging of knockout options. Full annotation: `by-domain/dynamical_systems.md`.

## QEC

*(MWPM syndrome decoding, JIT decoder — see inbox for de la Fuente)*

---

## Cross-domain observation

The matching machine appears in four incarnations:

1. **Algebraic geometry (Di Rocco et al.)**: Matching = critical points of distance function on an algebraic variety. Cost = squared Euclidean distance. The algebraic degree (bottleneck degree) counts solutions.

2. **Optimal transport (Bunne et al.)**: Matching = transport plan between distributions on different spaces. Cost = discrepancy in pairwise distance structure. Second-order (Gromov-Wasserstein) rather than first-order.

3. **Distributional RL (Dabney et al.)**: Matching = quantile alignment between predicted and target return distributions. Cost = Wasserstein-1 distance. The Bellman contraction ensures convergence.

4. **Mathematical finance (Bayraktar & Zhou)**: Matching = martingale coupling between given marginals. Cost = exotic option payoff. The martingale constraint (no-arbitrage) restricts the feasible set of matchings.

The cost function is always a metric or semi-metric, and the matching always respects structural constraints (normality in geometry, no-arbitrage in finance, Bellman consistency in RL).

---

## From Second Pass + Bridges

### Hawkes / Point Processes
- **Shang & Sun (2019)** — Geometric embedding matches processes to graph positions. Implicit optimal assignment. `second_pass.md` SP-06.
- **Huang et al. (2022)** — Latent space distance as matching cost. Learns which processes should be neighbors. `second_pass.md` SP-07.

### CSP / Assignment
- **Amizadeh et al. (2019) PDP** — Decimation = assignment of variables to values. Neural search strategy. `second_pass.md` SP-10.
- **Bennett et al. (2022)** — Lead-lag cluster pairing via Hermitian spectral clustering = directed matching. `second_pass.md` SP-14.

### Continuous-Time
- **Chen et al. (2023) ContiFormer** — Attention as continuous-time matching. Query-key pairing evolves via Neural ODE. `cross_domain_bridges.md`.

### Convergence Rates
- **Horst & Xu (2024)** — Wasserstein convergence bounds for rescaled Hawkes processes to their limits. `second_pass.md` SP-08.
