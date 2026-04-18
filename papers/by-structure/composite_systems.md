# Composite Systems (Joint-vs-Marginal Excess)

Papers instantiating the **joint-vs-marginal** abstract machine: detecting structure in composite systems that is absent from components. This includes entanglement, binding, synergy, mutual information, and integrated information.

The shared pattern: given components A and B, measure some property P of the joint system (A,B) and compare it to the combination of P(A) and P(B) separately. The excess P(A,B) - f(P(A), P(B)) > 0 signals genuine composite structure.

---

## Information Theory

### Belghazi et al. (2018) — MINE
MI as D_KL(P_XZ || P_X ⊗ P_Z). Neural estimator using Donsker-Varadhan dual. Joint-vs-marginal excess IS the paper's core object. Full annotation: `by-domain/information_theory.md`.

### Wickstrøm et al. (2019) — Information Plane via Rényi Entropy
I(X;T) and I(T;Y) at each hidden layer, tracked across training epochs. Also instantiates parameterized homology. Full annotation: `by-domain/information_theory.md`.

### Tax, Mediano & Shanahan (2017) — PID of Generative NNs
Synergy as the joint-vs-marginal excess in PID. Tracks synergistic, redundant, and unique information atoms through RBM training. Full annotation: `by-domain/information_theory.md`.

### Chwilka & Karbowski (2024) — Lognormal MI
Exact MI for lognormal distributions. MI can diverge at finite variance — infinite joint-vs-marginal excess. Full annotation: `by-domain/information_theory.md`.

### Mézard & Mora (2008) — Constraint Satisfaction
Factor graphs as generalized chain complexes. Solution-space shattering at α_c as topological phase transition. Also instantiates chain complex, matching, stability, null hypothesis. Full annotation: `by-domain/information_theory.md`.

### Sugiyama, Nakahara & Tsuda (2016) — Information Decomposition on Structured Space
Pythagorean theorem for KL divergence on posets decomposes interactions by order. Higher-order interactions = joint-vs-marginal excess at each level. Most algebraically rigorous treatment of the decomposition. Full annotation: `by-domain/information_theory.md`.

### Geiger (2021) — Information Plane Review
Surveys joint-vs-marginal (MI) estimation across architectures. Distinguishes geometric from information-theoretic compression. Full annotation: `by-domain/information_theory.md`.

### Shwartz-Ziv & Tishby (2017) — Opening the Black Box of DNNs via Information
I(X;T) and I(T;Y) per hidden layer T — each is a joint-vs-marginal excess (D_KL of joint vs product of marginals). Each layer is a marginal (compressed) view of the input; the joint network's Markov chain captures dependencies across layers. Also primary instantiation of parameterized homology (training epoch as parameter). Full annotation: `inbox.md` (arXiv: 1703.00810).

## TDA

### Harrington, Otter, Schenck, Tillmann (2017) — Stratifying multiparameter persistent homology
Multiparameter PH studies topological invariants as MULTIPLE parameters vary simultaneously. The joint bifiltration captures structure invisible to either single-parameter filtration alone — this IS joint-vs-marginal: joint persistent homology contains information absent from marginal (single-parameter) persistence diagrams. Three invariants from commutative algebra: multigraded associated primes, Hilbert series, local cohomology. Full annotation: `inbox.md` (arXiv: 1708.07390).

### Barannikov, Trofimov, Sotnikov et al. (2021) — Cross-Barcode / Manifold Topology Divergence
Cross-Barcode(P,Q) = pairwise topological comparison of two manifold-supported distributions. MTop-Divergence = 0 iff topologically equivalent. Detects mode-dropping, mode-collapse, mode-invention. Builds a SINGLE barcode from the pair — conceptually distinct from comparing two PDs via Wasserstein (which is Matching). Scales linearly with dimension. Full annotation: `inbox.md` (arXiv: 2106.04024).

## Information Theory — Causal Inference & PID

### Jónsson et al. (2020) — DNN Convergence with MI Regularization
MINE-estimated I(X;T) as regularizer. Confirms compression phase in VGG-16. MI-based loss stabilizes training. Full annotation: `by-domain/information_theory.md`.

### Kolchinsky (2024) — PID Redundancy as Information Bottleneck
Redundancy reformulated as IB compression-prediction tradeoff. "RB curve" = parameterized family of decompositions indexed by compression β. Bridges Joint (PID) and Param (IB) machines formally. Efficient iterative algorithm. Full annotation: `inbox.md` (arXiv: 2405.07665).

### Kirkley (2025) — Transfer Entropy for Finite Data
Reduced transfer entropy as debiased joint-vs-marginal excess with automatic MDL null. Combinatorial entropy avoids random-variable assumption. Full annotation: `by-domain/information_theory.md`.

### Zhang, Simeone et al. (2020) — ITENE
Intrinsic transfer entropy: refines joint-vs-marginal excess by subtracting synergistic information. Neural estimator via variational KL bounds. Also neuroscience. Full annotation: `by-domain/information_theory.md`.

### Amornbunchornvej, Zheleva, Berger-Wolf (2020) — Variable-lag GC and TE
Variable-lag Granger causality with DTW matching. Joint-vs-marginal excess computed after optimal temporal alignment. Full annotation: `by-domain/information_theory.md`.

### Marinazzo, Pellicoro, Stramaglia (2008) — Kernel Granger Causality
Granger causality as variance-ratio excess lifted to RKHS. Bonferroni-controlled eigenvector selection. Applied to gene regulatory and chaotic map networks. Full annotation: `by-domain/information_theory.md`.

### Khanna & Tan (2020) — Economy SRU for Nonlinear GC
Nonlinear Granger causality via sparse recurrent networks. Group-wise L1 regularization encodes null (no causal link) as zero input weights. Full annotation: `by-domain/information_theory.md`.

### Marcinkevics & Vogt (2021) — GVAR (Self-explaining NNs for GC)
Interpretable Granger causality with time-varying generalised coefficients. Signed effect detection + time-reversal stability. Full annotation: `by-domain/information_theory.md`.

### Zhou, Xiao, Zhang, Xu, Cai (2014) — GC Network Reconstruction in I&F
Quantitative mapping GC ∝ S² between functional and synaptic connectivity. Works across dynamical regimes. Also neuroscience. Full annotation: `by-domain/information_theory.md`.

### Wibral, Finn et al. (2017) — PID in Developing Neural Networks
PID synergy as information modification; developmental trajectory shows synergy rise then collapse. Also neuroscience. Full annotation: `by-domain/information_theory.md`.

### Venkatesh, Dutta et al. (2021) — M-information Flow for Interventions
Multi-message information flow (accuracy vs. bias) guides edge pruning. Observational flow predicts interventional effect. Also neuroscience. Full annotation: `by-domain/information_theory.md`.

### PID Core Papers (8 papers)

The PID programme is the information theory community's systematic treatment of joint-vs-marginal excess. All 8 papers decompose I(T; X1,...,Xn) into atoms. Synergy — the atom at the top of the redundancy lattice — is exactly the joint-vs-marginal excess: information present in the composite (X,Y) that is absent from X and Y individually.

**PID-01 — Kolchinsky (2022)**: "A Novel Approach to the Partial Information Decomposition." Blackwell-order-based PID. Synergy defined via independent redundancy/union (no inclusion-exclusion). Also instantiates chain complex (lattice + Mobius), matching (optimization over channels), stability (data processing inequality). Full annotation: `by-domain/information_theory.md`.

**PID-02 — Ince (2017)**: "The Partial Entropy Decomposition." Extends PID lattice to entropy (no target variable). Synergistic entropy = joint-vs-marginal excess in uncertainty. Reveals MI itself conflates redundant and synergistic entropy. Also instantiates chain complex, null hypothesis (diagnostic examples). Full annotation: `by-domain/information_theory.md`.

**PID-03 — Venkatesh, Schamberg (2022)**: "PID via Deficiency for Multivariate Gaussians." Convex optimization for Gaussian PID in high dimensions. Counterexample: Barrett's scalar result breaks for vector messages. Also instantiates matching (convex optimization over covariance matrices), stability (approximation bounds). Full annotation: `by-domain/information_theory.md`.

**PID-04 — Finn, Lizier (2018)**: "Pointwise PID Using Specificity and Ambiguity Lattices." Dual-lattice decomposition of unsigned pmi components. Satisfies target chain rule. Resolves two-bit-copy via Kelly gambling. Also instantiates chain complex (two parallel lattices), null hypothesis (canonical diagnostics). Full annotation: `by-domain/information_theory.md`.

**PID-05 — Schick-Poland, Makkeh, Gutknecht, Wollstadt, Sturm, Wibral (2021)**: "PID for discrete and continuous variables." Measure-theoretic extension via shared exclusions. Differentiable, transformation-invariant, admits target chain rule. Also instantiates chain complex, stability (three perturbation-robustness results), null hypothesis (prior as reference). Full annotation: `by-domain/information_theory.md`.

**PID-06 — Makkeh, Theis, Vicente (2018)**: "BROJA-2PID: A Robust Estimator." Exponential cone programming for BROJA PID. Proves strong duality. CI = I_joint - min_Q I_Q is literally excess of joint over marginal-preserving null. Also instantiates matching (optimal transport in distribution space), stability (solver robustness). Full annotation: `by-domain/information_theory.md`.

**PID-07 — Makkeh, Theis, Vicente (2017)**: "Bivariate PID: The Optimization Perspective." Theoretical convex analysis of BROJA. Boundary non-smoothness = singularity at deterministic limit. Also instantiates matching (KKT on transportation polytope), stability (gradient divergence analysis). Full annotation: `by-domain/information_theory.md`.

**PID-08 — Tian, Shamai (2025)**: "Broadcast Channel Cooperative Gain." First operational interpretation: BROJA synergy = cooperative gain (or lower bound) on broadcast channel sum-rate capacity. Cooperative gain IS joint-vs-marginal excess with a channel-coding interpretation. Also instantiates matching (channel optimization), null hypothesis (non-cooperative baseline), parameterized homology (capacity region deformation). Full annotation: `by-domain/information_theory.md`.

#### PID structural parallels across domains

The PID joint-vs-marginal pattern maps precisely to analogues in every other Rosetta domain:

| Domain | Joint object | Components | Excess | Null model |
|---|---|---|---|---|
| **PID** | I(T; X,Y) | I(T;X), I(T;Y) | Synergy CI | min_Q I_Q (marginal-preserving) |
| **QEC** | rho_AB | rho_A, rho_B | Entanglement | Product state rho_A tensor rho_B |
| **TDA** | PH(joint cloud) | PH(proj_X), PH(proj_Y) | Binding residual | Surrogate (phase-shuffled) |
| **Neuroscience** | Cross-region dynamics | Single-region activity | Neural binding | Trial-shuffled surrogates |
| **Dynamical systems** | Coupled attractor | Uncoupled components | Emergent topology | Decoupled system |

The BROJA null (min_Q preserving pairwise marginals) is the closest information-theoretic analogue to the TDA surrogate (destroy coupling, preserve marginal spectra). Both ask: "how much structure survives when we remove the joint dependence while keeping component-level statistics intact?"

**Open problem**: PID lacks a general stability theorem. TDA has bottleneck stability (small perturbation to input yields bounded change in persistence diagram). QEC has the threshold theorem (below threshold, logical error rate is exponentially suppressed). There is no PID result of the form "small perturbation to the joint distribution yields bounded perturbation to all PID atoms." PID-05's differentiability and PID-07's convexity analysis are partial steps, but neither provides a global Lipschitz-type bound. This gap is a concrete research target for the Rosetta programme.

---

## TDA / Mathematical Physics

### Kanjamapornkul, Pincak, Bartos (2020) — Cohomology Theory for Financial Time Series
Chern-Simons currents arise from the interaction of trader behavior fields (Yang-Mills). The current measures a geometric phase absent from individual trader actions — arbitrage as joint-vs-marginal excess. The Wilson loop path integral over interacting trader paths detects structure in the composite (bid-ask pair) that is absent from each side alone. Full annotation: `by-domain/tda.md`.

*(See also inbox for ATT binding residual)*

## Mathematical Finance

### Bayraktar & Zhou (2017) — Model-Independent Pricing via Optimal Transport
The entire framework measures the gap between what marginal distributions determine and what the joint (martingale coupling) allows. Super-hedging price optimized over the set M of all martingale measures with given marginals = worst-case joint-vs-marginal excess. Full annotation: `by-domain/dynamical_systems.md`.

## Optimal Transport

### Bunne, Alvarez-Melis, Krause, Jegelka (2019) — Gromov-Wasserstein GANs
GW distance captures relational structure invariant to ambient dimension/rotation — detecting structure in RELATIONSHIPS between points (joint, pairwise) absent from marginal (pointwise) descriptions. Full annotation: `by-domain/dynamical_systems.md`.

## QEC

*(Entanglement as non-separable state in tensor product — see inbox for Kitaev, Freedman-Kitaev-Wang)*

## Neuroscience

### Tort, Komorowski, Eichenbaum, Kopell (2010) — PAC Modulation Index
Phase-amplitude coupling: Modulation Index = D_KL(observed PAC distribution || uniform). Gamma amplitude modulated by theta phase = joint-vs-marginal excess. Time-shifted surrogates as null. Full annotation: `inbox.md`.

### Oizumi, Albantakis, Tononi (2014) — Integrated Information Theory 3.0
Φ = D(p(X^t|X^{t-1}) || Π_i p(X_i^t|X_i^{t-1})). THE foundational formalization of joint-vs-marginal excess for consciousness. Partitioned system as null. MICS = maximally irreducible conceptual structure. Exclusion postulate selects spatiotemporal grain maximizing Φ. Predicts simple systems can be conscious, complex feed-forward ones cannot. Full annotation: `inbox.md` (DOI: 10.1371/journal.pcbi.1003588).

## Information Theory / Dynamical Systems

### Schreiber (2000) — Transfer Entropy
T_{Y→X} = H(X_{t+1}|X_t^(k)) - H(X_{t+1}|X_t^(k),Y_t^(l)). Directed joint-vs-marginal: how much does joint (X,Y) history improve prediction beyond marginal X history? Asymmetric (unlike MI). Shuffled surrogates as null. Full annotation: `inbox.md`.

## Dynamical Systems

### Sugihara, May, Ye, Hsieh, Deyle, Fogarty, Munch (2012) — Convergent Cross-Mapping
Cross-prediction from Y's shadow manifold to X tests whether the joint (coupled) attractor contains more information than the marginal (single-variable) reconstruction. Convergence of cross-prediction skill with library size L = the excess is real and recoverable. Directional asymmetry (rho_{Y->X} != rho_{X->Y}) identifies causal direction. Surrogates as null. Full annotation: `inbox.md` (DOI: 10.1126/science.1227079). Machines: joint-vs-marginal, stability, null hypothesis, parameterized homology (weak).

---

## From Second Pass + Bridges

### Information Bottleneck Cluster
- **Shwartz-Ziv & Tishby (2017)** — IB objective min I(X;T) - βI(T;Y) decomposes learning into joint (prediction) and marginal (compression). `second_pass.md` SP-01.
- **Kawaguchi et al. (2023)** — Excess risk controlled by I(X;Z) gap. `cross_domain_bridges.md`.
- **Yu et al. (2024)** — CS divergence: closed-form joint-vs-marginal. `second_pass.md` SP-03.
- **Wang et al. (2021)** — HSIC as kernel dependence measure. `second_pass.md` SP-04.
- **Ma et al. (2020)** — HSIC bottleneck without backpropagation. `cross_domain_bridges.md`.

### Hawkes Processes
- **Mei & Eisner (2017)** — Cross-excitation = positive joint excess; inhibition = negative. `second_pass.md` SP-05.
- **Huang et al. (2022)** — Baseline (marginal) + mutual excitation (joint excess). Reciprocity and transitivity as higher-order joint. `second_pass.md` SP-07.
- **Daw & Pender (2021)** — Epidemic/preferential attachment connections. Joint infection history > marginal. `second_pass.md` SP-09.

### Decomposition / Factorization
- **Liu et al. (2023) FOCAL** — Shared features = cross-modal joint excess; private features = modality-exclusive marginal. `second_pass.md` SP-16.
- **Oladyshkin et al. (2023) DaPC NN** — kth-order polynomial chaos terms = k-way joint excess beyond lower orders. `cross_domain_bridges.md`.
- **Napolitano (2026)** — Active (6-dim) vs dark (10-dim) Casimir modes. Dark dimensions = excess hidden by layer normalization. `second_pass.md` SP-11.

### QEC / Quantum
- **Pati & Sanders (2005)** — Quantum parameter space (Bloch sphere) not decomposable into marginal subspaces. Indivisibility IS joint-vs-marginal. `cross_domain_bridges.md`.
- **Garbaczewski (2005)** — Multi-level: S(ρ)=0 but H(|ψ|²)>0. Different entropy functionals capture different joint layers. `cross_domain_bridges.md`.

### Neuroscience / Networks
- **Simpson et al. (2013)** — Functional connectivity = pairwise joint excess. Integration vs segregation = global vs local balance. `second_pass.md` SP-15.
- **Fasoli et al. (2026)** — Attractor structure absent from individual regions, emerges from coupled system. `cross_domain_bridges.md`.
- **Bennett et al. (2022)** — Lead-lag = joint predictive structure. `second_pass.md` SP-14.
- **Bandt (2020)** — Up-down balance and turning rate as joint statistics absent from marginals. `second_pass.md` SP-13.

---

## Third Pass (2026-04-05)

### Neuroscience

**IPWT — Consciousness**: Synergistic information = joint-vs-marginal excess. IPWT criterion: whole-system information exceeds sum of subsystem information (binding residual). Replaces IIT's physical indivisibility with synergy. Full annotation: `third_pass_neuro_qec.md` (TP-01).

**Neurophenomenology** (arXiv: 2409.20318): First-person beliefs and third-person measurements as two marginals. Free energy measures divergence. The explanatory gap IS the joint excess yet to be accounted for. Full annotation: `third_pass_neuro_qec.md` (TP-02).

**Dabney Distributional Code** (Nature 2020): Population jointly encodes full reward distribution; no single neuron's marginal contains it. Quantile-indexed family. Full annotation: `third_pass_neuro_qec.md` (TP-03).

**Opponent Striatal Circuit**: D1/D2 opponent encoding: each encodes half the distribution (optimistic/pessimistic tails). Neither alone suffices. Full annotation: `third_pass_neuro_qec.md` (TP-04).

### QEC

**Barandes Stochastic-Quantum**: Interference terms = joint-vs-marginal excess. Quantum phases encode information invisible in marginal (probability) distribution. Born rule = projection from joint to marginal. Full annotation: `third_pass_neuro_qec.md` (TP-06).

**Quantum State Tomography**: Entanglement = joint structure absent from reduced density matrices. Separable state as null. Full annotation: `third_pass_neuro_qec.md` (TP-07).

**Spin-Boson**: Non-Markovian corrections = joint (spin-bath) structure invisible in marginal (spin-only) dynamics. Full annotation: `third_pass_neuro_qec.md` (TP-10).

### Information Theory

**GMI — Graphical Mutual Information**: Graded joint excess — separate MI for 0-cells (nodes) and 1-cells (edges). Extending to simplicial complexes would create information-theoretic Betti numbers. Full annotation: `third_pass_infotheo_cross.md` (TP-02).

**Multivariate Redundancy** (Chicharro 2017): Synergy = excess beyond any proper subset. Mechanistic vs source redundancy distinguished. Tree decomposition isolates atoms at each hierarchical level. Full annotation: `third_pass_infotheo_cross.md` (TP-04).

**MI-NEE**: Triangulated joint-vs-marginal: compare both to a common null (uniform) rather than directly to each other. Full annotation: `third_pass_infotheo_cross.md` (TP-08).

**HSIC Bottleneck Orthogonalization**: HSIC(Z,X) = marginal info retained; HSIC(Z,Y) = task-relevant joint info. Bottleneck minimizes former, maximizes latter. Full annotation: `third_pass_infotheo_cross.md` (TP-09).

### Dynamical Systems

**Cross-Correlation Integral**: Nonstationarity = gap between cross and auto correlation integrals. Cross < geometric mean of autos indicates structural change. Full annotation: `third_pass_dynamics_tda.md` (TP-03).

**Entropic Symmetry Breaking**: After symmetry breaking, directed information flow emerges — some directions carry more information than others. This asymmetry is joint excess absent from the symmetric (marginal) description. Full annotation: `third_pass_dynamics_tda.md` (TP-04).

**Specific Entropy Rate**: Variation h(x) - h_avg is joint-vs-marginal excess at state x. States with unexpectedly high/low unpredictability carry structure absent from the average. Full annotation: `third_pass_dynamics_tda.md` (TP-07).

### TDA

**Higher-Order Network Compression** (PRL): k-body interactions predictable from (k-1)-body = no excess. Genuinely new information = non-trivial homology. Information-theoretic criterion for chain complex truncation. Full annotation: `third_pass_dynamics_tda.md` (TP-10).

### Cross-Domain Comparison (Expanded)

| Domain | What's joint | What's marginal | Excess type | Detection |
|--------|-------------|-----------------|-------------|-----------|
| TDA | Joint embedding | Marginal point clouds | Binding residual | PI subtraction |
| QEC | Tensor product state | Subsystem states | Entanglement | Witness / partial trace |
| QEC (Barandes) | Quantum amplitude | Classical probability | Interference / phases | Born rule gap |
| Dynamics | Coupled system | Uncoupled components | Emergent topology | Cross-correlation gap |
| Dynamics | Symmetry-broken state | Symmetric state | Directed info flow | Entropy production |
| Neuroscience | Population code | Single neuron | Distributional code | Quantile diversity |
| Neuroscience | Whole brain | Subsystems | Synergistic info (Φ) | PID / IIT |
| Neuroscience | Neurophenomenology | 1st/3rd person descriptions | Free energy gap | Variational inference |
| Info theory | Joint distribution | Product of marginals | MI | MINE / MI-NEE |
| Info theory | k-body interaction | (k-1)-body marginals | Higher-order info | PRL compression criterion |

---

## Joint x Neuro — Consciousness / Information Dynamics (Wave 5)

### Mediano, Rosas, Carhart-Harris, Seth, Barrett (2019) — PhiID
arXiv: 1909.02297
PhiID decomposes the total joint-vs-marginal excess (excess entropy E) into 16 atoms on a product lattice, distinguishing SIX modes of how joint information exceeds marginal: storage, copy, transfer, erasure, upward causation, downward causation. Synergistic atoms (source or target = {12}) are the pure joint-vs-marginal excess; redundant atoms are the "shared floor." The corrected Phi_WMS,c removes the confound of double-redundancy causing negative integration scores. Key contribution to the composite_systems programme: "integration" is not one thing --- it is a heterogeneous aggregate of qualitatively distinct excess types. Full annotation: `inbox.md`.

### Barrett (2015) — PID for Gaussian Systems
arXiv: 1411.2832
WMS = I(X;Y,Z) - I(X;Y) - I(X;Z) = S - R is the net joint-vs-marginal excess. For Gaussians with univariate target, all PIDs collapse to MMI: R = min{I(X;Y), I(X;Z)}, S = I(X;Z|Y) when I(X;Y) >= I(X;Z). Net synergy positive even when sources uncorrelated (b=0) because log concavity creates excess absent from the linear variance measure. In dynamical (MVAR) systems, synergy decreases as more history is observed (infinite-lag vs 1-lag). Proposes synergistic complexity SC = average synergy per triplet as complexity measure. Full annotation: `inbox.md`.

### Connection to existing PID cluster
Both papers extend the PID programme (8 core PID papers already in composite_systems) into the **dynamical** regime. Mediano's PhiID is the temporal extension of PID to multivariate time series (source = past, target = future), while Barrett provides the first continuous-variable (Gaussian) instantiation. Together with IIT 3.0 (Oizumi et al. 2014, already indexed), they form a trio:
- **IIT 3.0**: Phi as scalar joint-vs-marginal excess (partitioned null)
- **Barrett (2015)**: PID atoms for Gaussians, synergy as the excess
- **Mediano (2019)**: PhiID unifying IIT + PID into 16-atom taxonomy

| Domain | Joint object | Components | Excess | Null model |
|---|---|---|---|---|
| **PhiID** | E = I(X1,X2; Y1,Y2) | I(Xi; Yi) per component | 16 PhiID atoms (6 modes) | Partitioned (independent subsystems) |
| **Gaussian PID** | I(X; Y,Z) | I(X;Y), I(X;Z) | Synergy S (MMI) | Product of source-target marginals |

---

## Wave 6 — Directed Information Flow (2026-04-07)

### Lobier, Siebenhuhner, Palva, Palva (2014) — Phase Transfer Entropy
DOI: 10.1016/j.neuroimage.2013.08.056
Phase TE is joint-vs-marginal at two levels: (1) directed TE measures how joint (source + target) phase history exceeds marginal (target-only) for prediction, and (2) phase extraction itself projects the full amplitude-phase signal to its phase marginal. Differential TE (dTE = TE(1->2) - TE(2->1)) isolates the asymmetric directional excess. Frequency-band-specific: directed coupling graphs differ across oscillatory bands, yielding a parameterized family of joint-vs-marginal measures. Surrogate nulls validated.
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology.
Full annotation: `inbox.md` (Wave 6).

### Shorten, Spinney, Lizier (2021) — Continuous-Time TE for Spike Trains
DOI: 10.1371/journal.pcbi.1008054
Continuous-time TE = KL divergence between true conditional measure (given full source + target history) and reduced conditional (target history only) on path space. The purest Radon-Nikodym formulation of directed joint-vs-marginal excess for event data. Local permutation surrogates generate correct null for conditional independence testing on point processes (source-time-shift surrogates fail). Pathwise TE decomposes into jump (at events) and continuous (between events) components.
**Machines**: joint-vs-marginal, null hypothesis, parameterized homology.
Full annotation: `inbox.md` (Wave 6).

### Rosas, Mediano et al. (2020) — Causal Emergence
PLoS Computational Biology, 16(12), e1008289. arXiv: 2004.08220. 143 citations.
Inverted joint-vs-marginal: macro Ψ = I(V_t; V_{t'}) - Σ_j I(X^j_t; V_{t'}) > 0 means coarse-grained macro has causal power exceeding sum of micro parts. Ψ iff dynamical synergy Syn^(k) > 0 (Theorem 1). Decomposition: downward causation D^(k) + causal decoupling G^(k) = "statistical ghosts" (emergent features with no micro-level causal trace). Three parameters: order k, time lag, partition. Game of Life particles decoupled from cells, flocking emergence at critical regime, macaque ECoG motor decoding emergent.
**Machines**: joint-vs-marginal (inverted), parameterized homology, null hypothesis, chain complex (inherited).
Full annotation: `inbox.md` (Wave 7).

### Connection to existing TE cluster
Together with Schreiber (2000, already indexed), Lobier (2014), and Peek et al. (2025, already indexed), these papers form a progression of the joint-vs-marginal machine in directed information flow:

| Paper | Domain | Signal type | TE formulation | Null method | Key advance |
|---|---|---|---|---|---|
| **Schreiber (2000)** | Dynamical systems | Real-valued | Discrete-time, plug-in | Shuffled surrogates | Original TE definition |
| **Lobier (2014)** | Neuroscience (MEG/EEG) | Phase (circular) | Discrete-time, phase-only | Surrogate data | Phase isolation, mixing robustness |
| **Shorten (2021)** | Info theory + neuroscience | Point process | Continuous-time, kNN | Local permutation | Consistency, multi-timescale |
| **Peek (2025)** | Neuroscience + TDA | Spike trains | Pairwise TE -> flag complex -> PH | Baseline epochs | TE as input to chain complex |

### Varley, Mediano, Patania & Bongard (2025) — The Topology of Synergy
PLoS Comput. Biol., DOI: 10.1371/journal.pcbi.1013649. arXiv: 2504.10140. 4 citations.
O-information (TC - DTC) as signed joint-vs-marginal excess: synergy = information in joint absent from all proper subsets. H2 cavities in Rips filtration correlate with synergy dominance. Normalized O-bar vs avg H2 persistence: rho = -0.55 to -0.65 in fMRI. PCA preferentially preserves redundancy (marginal-preserving) and destroys synergy (joint-only). Connects to Rosas (2020): O-information is the O(X) = TC - DTC family that Rosas used to define causal emergence; this paper gives it a topological interpretation.
**Machines**: joint-vs-marginal, parameterized homology, chain complex, null hypothesis, stability.
Full annotation: `inbox.md` (Wave 7).

### Hamilton & Leditzky (2023/2024) — PH of Multipartite Entanglement
Commun. Math. Phys. 405, art. 125. arXiv: 2307.07492. 8 citations.
PH with multipartite filtration: q-deformed total correlation C_q(J) as sublevel set functional on the simplex of n parties. Integrated Euler characteristic = n-tangle (entanglement monotone) at q=2. Barcodes strictly finer than n-tangle — distinguish SLOCC orbits. Relative PH gives -I(A:B|R) ≤ 0 by strong subadditivity. Entanglement IS joint-vs-marginal excess; PH captures its multiscale structure.
**Machines**: joint-vs-marginal, chain complex, parameterized homology, stability, matching, null hypothesis.
Full annotation: `inbox.md` (Wave 7).

### Natarajan, Chaplin, Bull et al. (2026) — Multi-species Topology
arXiv: 2603.03237.
Kernel/image/cokernel persistence of k-chromatic gluing map yields four categories: (i) common features, (ii) features destroyed by composition (kernel), (iii) features ONLY in the joint (cokernel = pure joint-vs-marginal excess), (iv) features formed by some, persisting with others (image). Cokernel captures topological structure invisible in all k-species marginals. Applied to tumor microenvironment: recovers immunoediting regimes, detects trichromatic spatial interactions.
**Machines**: joint-vs-marginal, chain complex, parameterized homology, null hypothesis, stability.
Full annotation: `inbox.md` (Wave 7).

---

## Wave 10 — link-forge update (2026-04-17)

### Baudot, Tapia, Bennequin & Goaillard (2019) — Topological Information Data Analysis
arXiv: 1907.04242. I_k measures k-th-order excess structure in joint absent from lower-order marginals. I_k = 0 for all k ≥ 2 iff independence (necessary and sufficient). Negative I_k = synergy = Borromean-link structure (pairwise independent, collectively dependent). Total correlation G_k is weaker — fails to discriminate subtypes. Full annotation: `inbox.md` (Wave 10a).

### Chaudhuri et al. (2019) — Head direction ring attractor
DOI: 10.1038/s41593-019-0460-x. Ring (S^1) manifold is a population-level phenomenon — individual neurons show noisy tuning curves. The topology emerges only from joint activity, not from any single neuron. Pure joint-vs-marginal excess. Full annotation: `inbox.md` (Wave 10a).
