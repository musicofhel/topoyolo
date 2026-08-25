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
PD distances (Wasserstein, bottleneck) ARE optimal partial transport problems — exact identification, not analogy. Extends PDs to Radon measures on the upper half-plane. Provides geometric description of Fréchet means. Characterizes ALL continuous linear representations. Full annotation: `annotations/1901.03048.md` (arXiv: 1901.03048).

*(See also inbox for Cohen-Steiner bottleneck distance, Adams persistence images)*

## Information Geometry / Optimal Transport

### Wong & Yang (2019) — Pseudo-Riemannian geometry embeds information geometry in optimal transport
Information geometry (Fisher metric, Bregman divergence) EMBEDS into OT geometry (Wasserstein) via pseudo-Riemannian framework. Ma-Trudinger-Wang condition ↔ information-geometric curvature. Exact functorial embedding, not analogy. Full annotation: `annotations/1906.00030.md` (arXiv: 1906.00030).

## Optimal Transport / Machine Learning

### Bunne, Alvarez-Melis, Krause, Jegelka (2019) — Gromov-Wasserstein GANs
Gromov-Wasserstein distance: second-order optimal transport matching pairwise intra-space distances across incomparable spaces. GW(mu, nu) = inf_pi integral |d_X(x,x') - d_Y(y,y')|^2. Used as GAN loss for cross-domain generation (graph to Euclidean, different dimensions). Orthogonality regularization on adversary. Steerable generation separates topology from geometry. Full annotation: `by-domain/dynamical_systems.md`.

### Dabney, Rowland, Bellemare, Munos (2018) — QR-DQN (Distributional RL)
Wasserstein-1 distance W_1(F,G) = integral |F^{-1}(tau) - G^{-1}(tau)| d(tau) minimized via quantile regression. Distributional Bellman operator contracts in W_infinity. QR-DQN uses N adjustable quantile locations with fixed uniform probabilities. Closes the theory-practice gap from C51 by operating end-to-end under Wasserstein. 33% median improvement on Atari. Full annotation: `by-domain/dynamical_systems.md`.

### Hu et al. (2026) — OpenVLThinkerV2 / Gaussian GRPO (G²RPO)
1D optimal transport as an RL objective: a non-linear coupling forces each task's advantage distribution onto the fixed reference measure N(0,1), replacing moment-matching standardization. Equalizes gradient updates across tasks with different reward topologies (sparse binary vs dense IoU); tail compression gives outlier robustness (stability), entropy shaping bounds exploration two-sidedly. Moment-matching cannot fix distributional shape — same W_1-vs-shape gap QR-DQN sits on. Full annotation: `annotations/2604.08539.md` (arXiv: 2604.08539).

### Bayraktar & Zhou (2017) — Model-Independent Pricing via Optimal Transport
Martingale optimal transport: given marginals mu_1, ..., mu_n (from call prices), optimize over all martingale couplings. Super-hedging price = worst-case matching cost. Duality: min hedging cost = sup_{Q in M} E_Q[Phi] + U^{-1}(alpha). Shortfall hedging reduces to super-hedging of knockout options. Full annotation: `by-domain/dynamical_systems.md`.

## QEC

### Kitaev (1997) — Fault-tolerant quantum computation by anyons
Matching: Anyonic excitations come in pairs. Error correction = fusing (matching) anyon pairs back to vacuum. Fusion rules define which pairs can annihilate. Full annotation: `annotations/quant-ph-9707021.md` (arXiv: quant-ph/9707021).

### Dennis et al. (2002) — Topological quantum memory
Matching: Recovery = identifying and matching syndrome defects via MWPM on syndrome graph. Full annotation: `annotations/quant-ph-0110143.md` (arXiv: quant-ph/0110143).

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

**Amornbunchornvej, Zheleva & Berger-Wolf (2020) — Variable-lag Granger Causality and Transfer Entropy**: DTW optimal warping path = minimum-cost matching between time indices; fixed-lag causality is the rigid (diagonal-path) special case. Full annotation: `annotations/2002.00208.md` (arXiv: 2002.00208).

**Ensemble Control on Lie Groups**: Single broadcast control must simultaneously steer ALL systems in population to respective targets. Infinite-dimensional matching reduced to finite-dimensional by covering decomposition. Full annotation: `third_pass_dynamics_tda.md` (TP-12).

**IC-PINN Coupled Oscillators**: Basis-free inference = function-level matching. Assign a coupling function (from infinite-dimensional space) to observed dynamics. Full annotation: `third_pass_dynamics_tda.md` (TP-11).

**Ordinal Networks**: Hurst exponent estimation = matching to parameterized family of fractional processes. Full annotation: `third_pass_dynamics_tda.md` (TP-05).

### Neuroscience (Wave 5, 2026-04-06)

**Thual et al. (2022) — FUGW Brain Alignment**: arXiv: 2206.09398. Fused Unbalanced Gromov-Wasserstein for whole-brain inter-subject fMRI alignment. Transport plan P in R^{n x p} between cortical vertices. Combines Wasserstein (feature) + Gromov-Wasserstein (geometry) + unbalanced marginals. NeurIPS 2022, 46 citations. Full annotation: `annotations/2206.09398.md (Wave 5)` (Wave 5).

**Janati et al. (2019) — Minimum Wasserstein Estimates**: arXiv: 1902.04812. Unbalanced OT regularizer for multi-subject MEG/EEG source imaging. Wasserstein barycenter as group-level source estimate. Cost = cortical geodesic distance. Generalized Sinkhorn solver. Full annotation: `annotations/1902.04812.md (Wave 5)` (Wave 5).

**Lee, Dabagia, Dyer, Rozell (2019) — Hierarchical OT for Neural Decoding**: arXiv: 1906.11768. Two-level Wasserstein alignment (cluster + point) for cross-session neural population decoding in macaque motor cortex. ADMM + Sinkhorn. NeurIPS 2019, 78 citations. Full annotation: `annotations/1906.11768.md (Wave 5)` (Wave 5).

---

### Wave 8: TDA Matching Foundations (2026-04-07)

**Bubenik & Elchesen (2019) — Universality of PD Distances**: Proves bottleneck and Wasserstein distances on persistence diagrams are universal constructions — THE canonical optimal matching metrics. 1-Wasserstein satisfies Kantorovich-Rubinstein duality. Any distance on PDs factors through these. Extends to multiparameter persistence. arXiv: 1912.02563, 15 citations. Full annotation: `annotations/1912.02563.md (Wave 8)` (Wave 8).

**Chen & Wang (2021) — Near-Linear Wasserstein on PDs**: Approximation algorithms for 1-Wasserstein distance between PDs via randomly shifted quadtrees. Near-linear time O(n log n / ε^d). Key technical challenge: diagonal as infinite reservoir. 100-1000x speedup over Hungarian/auction. arXiv: 2104.07710, 9 citations. Full annotation: `annotations/2104.07710.md (Wave 8)` (Wave 8).

### Wave 8: Information Theory Matching Foundations (2026-04-07)

**Blahut (1972) + Arimoto (1972) — Channel Capacity and Rate-Distortion**: THE foundational IT matching algorithms. Channel capacity = optimal matching of source to channel inputs. Rate-distortion R(D) = minimum-cost soft assignment between source and reproduction alphabets. Alternating minimization: fix one marginal, optimize the other (predates EM by 5 years). R(D) curve parameterized by D with slope -s. 3000+ combined citations. Full annotation: `annotations/blahut-arimoto-1972.md` (slug: blahut-arimoto-1972).

### B2 batch-004: rate-distortion lineage (2026-08-25)

**Lei, Hassani & Saeedi Bidokhti (2022) — NERD**: Neural estimation of the RD functional where BA alternating minimization is infeasible; recovers the optimal test channel and the parameterized R(D) curve; reverse channel coding turns the estimate into an operational one-shot lossy code. Machines: matching, null hypothesis, parameterized homology (weak). arXiv: 2204.01612. Full annotation: `annotations/2204.01612.md` (B2 pass 27). Abstract-only provenance — depth-limited.

**Theis & Wagner (2021) — RDPF coding theorem**: The perception term is a marginal-agreement constraint on the coupling — the OT-style distributional matching condition layered on top of the distortion-constrained soft assignment; achievability + converse for stochastic variable-length codes. Machines: matching, null hypothesis (weak). arXiv: 2104.13662. Full annotation: `annotations/2104.13662.md` (B2 pass 27). Abstract-only provenance — depth-limited.

**Yadav, Song, Shkel & Özgür (2026) — Log-likelihood loss for semantic compression**: RD under a cross-entropy cost on the coupling induced by a prescribed generative channel P_{X|U} — soft-matching where "distortion" is misfit to a generative model; perfect-perception (marginal-agreement) RD appears as a boundary case. Closes batch-004 rate-distortion 4/4. Machines: matching, null hypothesis (weak). arXiv: 2601.16461. Full annotation: `annotations/2601.16461.md` (B2 pass 28). Abstract-only provenance — depth-limited.

### Wave 9: Spectral Wasserstein (2026-04-07)

**Peyré (2026) — Muon Dynamics as a Spectral Wasserstein Flow**: Family of Spectral Wasserstein distances W_γ parameterized by Schatten norm index p. Cost acts on global displacement covariance matrix, not per-particle scalar costs. Trace norm (p=1) → classical W2; operator norm (p=∞) → Muon geometry. Kantorovich (couplings = matchings) equals Benamou-Brenier (gradient flows) for monotone norms. Max-min representation: W_γ² = max over anisotropic quadratic transports. Metric equivalence with W2: √c_γ · W2 ≤ W_γ ≤ √C_γ · W2. Geodesic convexity. Gaussian case: closed-form metric extending Bures-Wasserstein. arXiv: 2604.04891. Full annotation: `annotations/2604.04891.md` (Wave 9).

### Wave 10: Statistical Wasserstein (2026-04-17)

**Panaretos & Zemel (2019) — Statistical Aspects of Wasserstein Distances**: Comprehensive review unifying OT as statistical inference tool. W_p family parameterized by order p: W_1 (location), W_2 (Riemannian geometry via Otto calculus), W_∞ (bottleneck = PH stability). Convergence rates, CLTs, minimax estimation, goodness-of-fit testing. Curse of dimensionality O(n^{-1/d}) for d ≥ 3. Entropic/sliced regularization. DOI: annurev-statistics-030718-104938, 913 citations. Full annotation: `annotations/annurev-statistics-030718-104938.md` (Wave 10b).

### Wave 10c: DMT Matching (2026-04-17)

**Curry, DeSha, Hoff, Limberger, Luo & Qin (2022) — Decorated merge trees for persistent topology**: DOI: s41468-022-00089-3. Gromov-Wasserstein coupling between decorated merge trees defines a stable metric for comparing persistent homology modules. The matching is between tree edge sets with costs determined by interleaving distance. DMT metric provides a computable alternative to interleaving distance that preserves the full tree structure (not just the barcode). Full annotation: `annotations/s41468-022-00089-3.md` (Wave 10c). **See also**: `by-domain/tda.md`, `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`.

### Ying, Pan, Fox, Agarwal (2016) — Fast Approximate DTW (κ-packed curves)
DTW as minimum-cost monotone correspondence assignment; (1+ε) stability bound on matching value; packing constant κ as the structure condition enabling fast matching. Also dynamical systems. Full annotation: `annotations/ying-2016.md` (B2 pass 13).

### Silva, Giusti, Keogh, Batista (2018) — Pruning unpromising DTW alignments
Exact monotone assignment with zero-error pruning inside the DP grid; lower-bound certificates bound the matching value. Complements ying-2016's (1+ε) approximation. Full annotation: `annotations/silva-2018.md` (B2 pass 13).

### B2 batch-004: Dynamics×Matching bridges (2026-08-25)

**Botvinick-Greenhouse, Oprea, Maulik & Yang (2024) — Measure-Theoretic Time-Delay Embedding**: arXiv: 2409.08768. Delay embedding as pushforward between probability-measure spaces (Eulerian dynamics); OT machinery supplies the coupling; robustness to sparse/noisy data. Machines: matching, stability. Full annotation: `annotations/2409.08768.md` (B2 pass 24). **See also**: `by-domain/dynamical_systems.md`.

**Moosmüller, Dietrich & Kevrekidis (2019) — Transport of Discontinuous Densities**: arXiv: 1907.08260. Attractor-reconstruction side information (short histories) disambiguates non-bijective transport-map identification. Machines: matching, stability (weak). Full annotation: `annotations/1907.08260.md` (B2 pass 24). **See also**: `by-domain/dynamical_systems.md`.

**Huguet, Magruder, Tong, Fasina, Kuchroo, Wolf & Krishnaswamy (2022) — Manifold Interpolating Optimal-Transport Flows (MIOFlow)**: arXiv: 2206.14928. Neural-ODE population dynamics penalized by dynamic OT with a manifold (multiscale geodesic) ground cost; geodesic autoencoder couples the learned latent metric to the OT cost. Machines: matching, stability (weak). Full annotation: `annotations/2206.14928.md` (B2 pass 25). Abstract-only provenance — depth-limited. **See also**: `by-domain/dynamical_systems.md`, `annotations/2409.08768.md`.

**Nakazato & Ito (2021) — Geometrical Aspects of Entropy Production via Wasserstein Distance**: arXiv: 2103.00503. Entropy production ≥ L2-Wasserstein path length of the density path — the matching cost reappears as physical dissipation; thermodynamic speed limits, optimal protocols, partial EP bounds. Machines: matching (instrumental), joint-vs-marginal (weak). Full annotation: `annotations/2103.00503.md` (B2 pass 25). Abstract-only provenance — depth-limited. **See also**: `by-domain/statistical_physics.md`.

**Ito (2022) — Geometric Thermodynamics for the Fokker-Planck Equation**: arXiv: 2209.00527. Information geometry and optimal transport unified through the excess entropy production rate: gradient flow ↔ information geometry on probability-density space, OT velocity field ↔ information geometry on path-probability space; thermodynamic trade-offs and minimum-cost optimal protocols fall out of the shared geometry. Machines: matching (core), joint-vs-marginal (weak). Full annotation: `annotations/2209.00527.md` (B2 pass 26). Abstract-only provenance — depth-limited. **See also**: `by-domain/statistical_physics.md`.

**Gulen & McCleary (2022) — Galois Connections in Persistent Homology**: arXiv: 2201.06650. Barcode matchings and interleavings unified via Galois connections; Rota's theorem gives an easier proof of bottleneck stability — the matching machine revealed as order-theoretically dual to the perturbation relation in the PH setting. Machines: matching, stability, parameterized homology. Full annotation: `annotations/2201.06650.md` (B2 pass 32). Abstract-only provenance — depth-limited. **See also**: `by-domain/tda.md`, `annotations/1205.3669.md`.
