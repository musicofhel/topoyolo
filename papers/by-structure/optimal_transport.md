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

### Divol & Lacombe (2019) — Understanding the Space of Persistence Diagrams via Optimal Partial Transport
PD distances (Wasserstein, bottleneck) ARE optimal partial transport problems — exact identification, not analogy. Extends PDs to Radon measures on the upper half-plane. Provides geometric description of Fréchet means. Characterizes ALL continuous linear representations. Full annotation: `inbox.md` (arXiv: 1901.03048).

*(See also inbox for Cohen-Steiner bottleneck distance, Adams persistence images)*

## Information Geometry / Optimal Transport

### Wong & Yang (2019) — Pseudo-Riemannian geometry embeds information geometry in optimal transport
Information geometry (Fisher metric, Bregman divergence) EMBEDS into OT geometry (Wasserstein) via pseudo-Riemannian framework. Ma-Trudinger-Wang condition ↔ information-geometric curvature. Exact functorial embedding, not analogy. Full annotation: `inbox.md` (arXiv: 1906.00030).

## Optimal Transport / Machine Learning

### Bunne, Alvarez-Melis, Krause, Jegelka (2019) — Gromov-Wasserstein GANs
Gromov-Wasserstein distance: second-order optimal transport matching pairwise intra-space distances across incomparable spaces. GW(mu, nu) = inf_pi integral |d_X(x,x') - d_Y(y,y')|^2. Used as GAN loss for cross-domain generation (graph to Euclidean, different dimensions). Orthogonality regularization on adversary. Steerable generation separates topology from geometry. Full annotation: `by-domain/dynamical_systems.md`.

### Dabney, Rowland, Bellemare, Munos (2018) — QR-DQN (Distributional RL)
Wasserstein-1 distance W_1(F,G) = integral |F^{-1}(tau) - G^{-1}(tau)| d(tau) minimized via quantile regression. Distributional Bellman operator contracts in W_infinity. QR-DQN uses N adjustable quantile locations with fixed uniform probabilities. Closes the theory-practice gap from C51 by operating end-to-end under Wasserstein. 33% median improvement on Atari. Full annotation: `by-domain/dynamical_systems.md`.

### Bayraktar & Zhou (2017) — Model-Independent Pricing via Optimal Transport
Martingale optimal transport: given marginals mu_1, ..., mu_n (from call prices), optimize over all martingale couplings. Super-hedging price = worst-case matching cost. Duality: min hedging cost = sup_{Q in M} E_Q[Phi] + U^{-1}(alpha). Shortfall hedging reduces to super-hedging of knockout options. Full annotation: `by-domain/dynamical_systems.md`.

## QEC

### Kitaev (1997) — Fault-tolerant quantum computation by anyons
Matching: Anyonic excitations come in pairs. Error correction = fusing (matching) anyon pairs back to vacuum. Fusion rules define which pairs can annihilate. Full annotation: `inbox.md` (arXiv: quant-ph/9707021).

### Dennis et al. (2002) — Topological quantum memory
Matching: Recovery = identifying and matching syndrome defects via MWPM on syndrome graph. Full annotation: `inbox.md` (arXiv: quant-ph/0110143).

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

---

## Third Pass (2026-04-05)

### QEC

**Quantum State Tomography (arXiv: 1810.10584)**: Tomography as inverse matching: given measurement outcomes, reconstruct the density matrix. Generative model matches model-generated statistics to empirical statistics. Informationally complete measurement basis as matching constraint. Full annotation: `third_pass_neuro_qec.md` (TP-07).

**Arovas-Zhang FQHE (weak)**: Anyonic fusion rules define matching constraint — which particle-antiparticle pairs can annihilate to vacuum. Full annotation: `third_pass_neuro_qec.md` (TP-05).

### Neuroscience

**Opponent Striatal Circuit**: D1/D2 opponent pairing — each D1 neuron encoding quantile tau implicitly paired with D2 neuron encoding 1-tau. Full annotation: `third_pass_neuro_qec.md` (TP-04).

**ConformalHDC**: Nearest-centroid matching in high-dimensional space for hippocampal decoding. Full annotation: `third_pass_neuro_qec.md` (TP-09).

### Dynamical Systems

**Ensemble Control on Lie Groups**: Single broadcast control must simultaneously steer ALL systems in population to respective targets. Infinite-dimensional matching reduced to finite-dimensional by covering decomposition. Full annotation: `third_pass_dynamics_tda.md` (TP-12).

**IC-PINN Coupled Oscillators**: Basis-free inference = function-level matching. Assign a coupling function (from infinite-dimensional space) to observed dynamics. Full annotation: `third_pass_dynamics_tda.md` (TP-11).

**Ordinal Networks**: Hurst exponent estimation = matching to parameterized family of fractional processes. Full annotation: `third_pass_dynamics_tda.md` (TP-05).

### Neuroscience (Wave 5, 2026-04-06)

**Thual et al. (2022) — FUGW Brain Alignment**: Fused Unbalanced Gromov-Wasserstein for whole-brain inter-subject fMRI alignment. Transport plan P in R^{n x p} between cortical vertices. Combines Wasserstein (feature) + Gromov-Wasserstein (geometry) + unbalanced marginals. NeurIPS 2022, 46 citations. Full annotation: `inbox.md` (Wave 5).

**Janati et al. (2019) — Minimum Wasserstein Estimates**: Unbalanced OT regularizer for multi-subject MEG/EEG source imaging. Wasserstein barycenter as group-level source estimate. Cost = cortical geodesic distance. Generalized Sinkhorn solver. Full annotation: `inbox.md` (Wave 5).

**Lee, Dabagia, Dyer, Rozell (2019) — Hierarchical OT for Neural Decoding**: Two-level Wasserstein alignment (cluster + point) for cross-session neural population decoding in macaque motor cortex. ADMM + Sinkhorn. NeurIPS 2019, 78 citations. Full annotation: `inbox.md` (Wave 5).

---

### Wave 8: TDA Matching Foundations (2026-04-07)

**Bubenik & Elchesen (2019) — Universality of PD Distances**: Proves bottleneck and Wasserstein distances on persistence diagrams are universal constructions — THE canonical optimal matching metrics. 1-Wasserstein satisfies Kantorovich-Rubinstein duality. Any distance on PDs factors through these. Extends to multiparameter persistence. arXiv: 1912.02563, 15 citations. Full annotation: `inbox.md` (Wave 8).

**Chen & Wang (2021) — Near-Linear Wasserstein on PDs**: Approximation algorithms for 1-Wasserstein distance between PDs via randomly shifted quadtrees. Near-linear time O(n log n / ε^d). Key technical challenge: diagonal as infinite reservoir. 100-1000x speedup over Hungarian/auction. arXiv: 2104.07710, 9 citations. Full annotation: `inbox.md` (Wave 8).

### Wave 8: Information Theory Matching Foundations (2026-04-07)

**Blahut (1972) + Arimoto (1972) — Channel Capacity and Rate-Distortion**: THE foundational IT matching algorithms. Channel capacity = optimal matching of source to channel inputs. Rate-distortion R(D) = minimum-cost soft assignment between source and reproduction alphabets. Alternating minimization: fix one marginal, optimize the other (predates EM by 5 years). R(D) curve parameterized by D with slope -s. 3000+ combined citations. Full annotation: `inbox.md` (Wave 8).

### Wave 9: Spectral Wasserstein (2026-04-07)

**Peyré (2026) — Muon Dynamics as a Spectral Wasserstein Flow**: Family of Spectral Wasserstein distances W_γ parameterized by Schatten norm index p. Cost acts on global displacement covariance matrix, not per-particle scalar costs. Trace norm (p=1) → classical W2; operator norm (p=∞) → Muon geometry. Kantorovich (couplings = matchings) equals Benamou-Brenier (gradient flows) for monotone norms. Max-min representation: W_γ² = max over anisotropic quadratic transports. Metric equivalence with W2: √c_γ · W2 ≤ W_γ ≤ √C_γ · W2. Geodesic convexity. Gaussian case: closed-form metric extending Bures-Wasserstein. arXiv: 2604.04891. Full annotation: `inbox.md` (Wave 9).
