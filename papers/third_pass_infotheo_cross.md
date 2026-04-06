# Third Pass -- Information Theory & Cross-Domain Bridges (2026-04-05)

Papers found by searching the link-forge Neo4j database with 27+ search strategies targeting information theory papers and cross-domain bridge papers not found in the first two passes. Focus areas: optimal transport, rate-distortion, generalized entropy, transfer entropy, variational inference, MDL/Kolmogorov, Fisher information, information bottleneck variants, topological+information bridges, homological algebra, coding theory, network information theory, privacy, thermodynamics, geometric deep learning, representation learning, diffusion models, and broad algebraic topology terms (chain complex, homology, cohomology, exact sequence, spectral sequence, derived functors).

**Note**: Papers already annotated in second_pass.md, cross_domain_bridges.md, or the by-domain/by-structure indices are excluded. This file contains only genuinely new annotations.

---

## TP-01 -- Wang, Wang, Jin, Wei (2024)
**"GC-STCL: A Granger Causality-Based Spatial-Temporal Contrastive Learning Framework for EEG Emotion Recognition"**

**Domain(s)**: Neuroscience (EEG), information theory (Granger causality, contrastive learning)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Granger causality captures directed temporal dependencies between EEG channels that are absent from individual channel statistics. The spatial contrastive loss compares positive pairs (same video stimulus) against negatives (different stimuli). The temporal Granger-Former captures cross-channel information flow that marginal channel analyses miss.
- **Chain complex (weak)**: The Granger causality graph defines a directed network between EEG channels. The residual graph convolutional neural network operates on this directed graph, which has an implicit oriented structure (cause -> effect). The graph Laplacian of the GC-enhanced graph is the 0-th Hodge-like operator on this directed network.
- **Null hypothesis**: Positive sample pairs are selected from individuals watching the same video, while negatives are from different videos. The contrastive framework tests whether neural dynamics encode stimulus-specific information above what chance pairing would produce. The frequency-domain noise reduction module is a preprocessing null removal step.
- **Parameterized homology**: The Granger causality test operates across frequency bands (alpha, beta, gamma), each revealing different causal structures. As the frequency parameter varies, the GC graph topology changes -- some channels are causally linked in alpha but not gamma. This frequency-parameterized view of brain connectivity is analogous to a filtration.

**What is genuinely new**:
- Combining Granger causality graph construction with contrastive learning for EEG. Previous methods used either GC-based graphs OR contrastive learning, but not both.
- Dual spatial-temporal contrastive losses: one for spatial (inter-channel) structure, one for temporal (within-channel) dynamics.
- Application to emotion recognition from EEG, where the spatial GC graph reveals emotion-specific connectivity patterns.

**Connections the authors acknowledge**: Cite Granger causality, graph neural networks, contrastive learning (SimCLR). Bridge neuroscience (EEG) and information theory (GC, contrastive objectives). No connections to TDA, QEC, or dynamical systems theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Granger causality graph | Directed causal network (oriented chain-like structure) |
| Spatial contrastive loss | Inter-channel joint-vs-marginal comparison |
| Temporal contrastive loss | Within-channel temporal joint-vs-marginal comparison |
| Positive pair (same stimulus) | Joint structure (shared causal origin) |
| Negative pair (different stimulus) | Null (no shared causal origin) |
| Frequency-domain GC | Parameterized causal graph (filtration over frequency) |
| Granger-Former | Temporal causal attention mechanism |

---

## TP-02 -- Peng, Huang, Luo, Zheng, Rong, Xu, Huang (2020)
**"Graph Representation Learning via Graphical Mutual Information Maximization"**

**Domain(s)**: Information theory, machine learning (graph neural networks)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Graphical Mutual Information (GMI) generalizes MI from vector spaces to graph-structured data. It measures the correlation between input graphs and their learned hidden representations from two aspects: (1) node feature MI and (2) topological structure MI. The joint consideration of features AND topology is the key excess: neither feature-only nor structure-only MI captures the full graph information. GMI decomposes into node-level and edge-level terms.
- **Stability**: GMI is proved to be invariant under isomorphic transformations of the input graph. This is a strong stability result: the information measure does not change under graph relabeling (permutation of nodes). Proved analytically.
- **Null hypothesis**: The unsupervised learning objective maximizes GMI between input and output of a graph encoder. The implicit null is a random (uninformative) representation that preserves no input structure.
- **Chain complex (weak)**: The graph structure defines a 0-skeleton. The edge-level MI term measures information about the 1-skeleton (edge structure). The separate treatment of node-level and edge-level MI creates a graded information structure: 0-cell information (node features) and 1-cell information (topology), measured independently.

**What is genuinely new**:
- Extension of MI from Euclidean spaces to graph domains with joint node-feature and topology components. Previous graph MI methods (DGI, InfoGraph) only considered one aspect.
- Isomorphism invariance proof for GMI.
- Outperforms supervised methods on some benchmarks despite being fully unsupervised.

**Connections the authors acknowledge**: Cite MINE, Deep Graph Infomax (DGI), graph neural networks. Bridge information theory and graph representation learning. No connections to TDA, QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Graphical MI (GMI) | Joint-vs-marginal excess on graph-structured data |
| Node-level MI | 0-cell information content |
| Edge-level MI | 1-cell information content |
| Isomorphism invariance | Stability under graph symmetry |
| Graph encoder | Map from input complex to representation |
| Unsupervised MI maximization | Self-supervised extraction of joint structure |

---

## TP-03 -- Zhu, Zhang, Wan, Dai (2024)
**"On Finite-Time Mutual Information"**

**Domain(s)**: Information theory (channel capacity, communication theory)

**Abstract machines instantiated**:
- **Parameterized homology**: The central object is the mutual information I(t) between source and destination within a finite-time observation window of duration t. As t varies, I(t) traces a curve that converges to the classical Shannon capacity C = lim_{t->inf} I(t)/t in the limit. But the finite-time behavior reveals structure invisible in the limit: the paper discovers the "exceed-average phenomenon" where the instantaneous rate I(t)/t within a finite window can exceed the time-averaged rate C. This parameterized view (MI as a function of observation window length) is structurally analogous to tracking Betti numbers as a function of filtration scale.
- **Stability**: The Shannon-Hartley theorem is recovered as the stable (infinite-time) limit. The finite-time corrections quantify the deviation from this stable limit, providing convergence rate bounds. The Mercer expansion of the autocorrelation kernel connects the convergence to the eigenvalue spectrum of a trace-class operator.
- **Null hypothesis**: The infinite-time averaged rate serves as the reference. The exceed-average phenomenon shows that finite windows can exceed this reference, which is paradoxical from the classical perspective.

**What is genuinely new**:
- Derivation of finite-time mutual information for correlated Gaussian processes, filling a gap since Shannon's original work.
- Discovery of the exceed-average phenomenon: MI per second in a finite window can exceed the infinite-time average.
- Connection to Mercer expansion of trace-class operators, bridging functional analysis and information theory.

**Connections the authors acknowledge**: Cite Shannon-Hartley theorem, Gaussian channels, Mercer's theorem. Purely within communication theory. No connections to TDA, QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Observation window duration t | Filtration parameter |
| I(t) (finite-time MI) | Parameterized invariant (MI as function of scale) |
| Shannon capacity C | Stable (infinite-time) limit of the invariant |
| Exceed-average phenomenon | Finite-scale excess over asymptotic average |
| Mercer expansion | Spectral decomposition of the autocorrelation operator |
| Eigenvalue spectrum | Spectral invariants controlling convergence |

---

## TP-04 -- Chicharro (2017)
**"Quantifying multivariate redundancy with maximum entropy decompositions of mutual information"**

**Domain(s)**: Information theory (neuroscience adjacent)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The paper constructs rooted-tree-based decompositions of MI that separate redundant, unique, and synergistic atoms at multiple hierarchical levels. The maximum entropy distribution serves as the reference (the "most structureless" distribution consistent with given constraints), and deviation from this reference quantifies different types of information structure. Synergy = excess beyond what any proper subset provides. Unique redundancy = excess that one group shares about a target that another group does not.
- **Chain complex (tree structure)**: The rooted-tree decomposition creates a hierarchical structure where each node implements a binary unfolding of MI using hierarchically related maximum entropy constraints. The tree itself is a graded structure: the root represents total MI, and successive levels decompose into finer atoms. The local implementation at each tree node of binary unfoldings mirrors the local-to-global construction of chain complexes.
- **Null hypothesis**: The maximum entropy distribution subject to constraints is the explicit null at each decomposition level. The constraints define what structure is "expected"; the deviation from maximum entropy quantifies the "unexpected" structure at each level. This is a nested hierarchy of null models, one per tree level.

**What is genuinely new**:
- Multivariate redundancy measures (beyond bivariate) within the maximum entropy framework.
- The identification of two types of constraints on entropy maximization that allow isolating redundancy from synergy by "mirroring" them.
- Separation of mechanistic redundancy (related to system function) versus source redundancy (arising from dependencies between inputs). No existing PID method makes this distinction.

**Connections the authors acknowledge**: Cite Williams & Beer PID, maximum entropy methods, neuroscience information processing. No connections to TDA, QEC, or dynamical systems.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Maximum entropy distribution | Null model (most structureless given constraints) |
| Rooted tree decomposition | Hierarchical chain (graded from total MI to individual atoms) |
| Binary unfolding | Local decomposition at each grade |
| Mechanistic redundancy | Functional shared structure (system-level) |
| Source redundancy | Statistical shared structure (input-level) |
| Mirroring (redundancy <-> synergy) | Duality between shared and excess structure |

---

## TP-05 -- Kong, Lin, Babiloni, Hu, Borghini (2015)
**"Investigating Driver Fatigue versus Alertness Using the Granger Causality Network"**
Sensors 15(8), 19181-19198

**Domain(s)**: Neuroscience (EEG), information theory (Granger causality)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Granger causality measures directed information flow between EEG channels. The GC network reveals causal connections that pairwise correlation (a marginal measure) misses. The key finding: the transition from alertness to drowsiness is characterized by changes in the GC network topology, including shifts in the strength and direction of causal connections, particularly in the alpha and theta bands.
- **Null hypothesis**: The alert state serves as the baseline/null against which the drowsy state is compared. Statistical significance of GC connections is tested against the null of no causal influence (shuffled surrogates).
- **Parameterized homology**: The GC analysis is performed separately in different EEG frequency bands (delta, theta, alpha, beta, gamma). Each frequency band reveals a different causal network. The frequency parameter defines a filtration of causal structure: low-frequency connections (global, slow) versus high-frequency connections (local, fast).
- **Matching**: The identification of which brain regions drive the alertness-to-drowsiness transition is an implicit matching problem: the method must assign causal roles (driver vs driven) to each EEG channel.

**What is genuinely new**:
- Application of Granger causality networks to fatigue detection. The finding that network topology (not just signal amplitude) distinguishes alert from drowsy states provides a structural biomarker.
- Frequency-band-specific causal networks: the causal structure differs across alpha, theta, and gamma bands.

**Connections the authors acknowledge**: Bridge between neuroscience (EEG, fatigue) and information theory (Granger causality). No connections to TDA, QEC, or dynamical systems theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Granger causality strength | Directed causal excess |
| Alert vs drowsy state | Two regimes with different topological structure |
| Frequency band (alpha, theta...) | Filtration parameter (scale of causal analysis) |
| Network topology change | Topological phase transition (alertness -> drowsiness) |
| Causal driver identification | Matching (assigning roles to nodes) |

---

## TP-06 -- Ding, Bressler, Yang, Liang (2009)
**"Analyzing Information Flow in Brain Networks with Nonparametric Granger Causality"**
AppliedMath, PMC 2685256

**Domain(s)**: Neuroscience, information theory (Granger causality, spectral methods)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Nonparametric Granger causality in the spectral domain measures directed information flow between brain regions at each frequency. The spectral GC decomposes the total causal influence into frequency-specific components. The frequency-resolved causal information is joint structure: it depends on the cross-spectral relationship between regions, not just individual region spectra (marginals).
- **Parameterized homology**: The frequency parameter defines a continuous family of causal graphs. At each frequency f, there is a different directed network of brain regions. As f varies, the causal structure changes -- connections appear and disappear. This frequency-parameterized view of brain connectivity is structurally analogous to a filtration.
- **Null hypothesis**: The no-causality hypothesis: testing whether the cross-spectral components are significantly different from what would be expected under independence (no directed information flow).
- **Stability**: The nonparametric approach avoids model misspecification errors that plague autoregressive GC. By using the Fourier transform directly, the method is robust to nonlinearities and non-stationarities.

**What is genuinely new**:
- Nonparametric spectral Granger causality: no autoregressive model fitting required. Fundamental methodological advance for neuroscience.
- Application to monkey sensorimotor cortex recordings, revealing directional information flow patterns during task performance.

**Connections the authors acknowledge**: Cite Granger (1969), Geweke (1982), spectral analysis methods. Bridge neuroscience (neurophysiology) and information theory (directed information). No connections to TDA, QEC, or dynamical systems theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Spectral Granger causality | Frequency-resolved directed causal excess |
| Frequency f | Filtration parameter |
| Cross-spectral density | Joint spectral structure between regions |
| Autoregressive null | Parametric model assumption (eliminated by nonparametric approach) |
| Directed information flow | Oriented causal structure (directed edges in network) |

---

## TP-07 -- Jiao, van Cranenburgh, Calvert, van Lint (2024)
**"Structure-preserving contrastive learning for spatial time series"**

**Domain(s)**: Information theory (contrastive learning), TDA-adjacent (topology preservation)

**Abstract machines instantiated**:
- **Stability**: The core contribution is two structure-preserving regularizers for contrastive learning. The topology regularizer preserves the rank ordering of pairwise similarities -- a topological invariant. The geometry regularizer preserves graph geometry across spatial and temporal dimensions. The topology regularizer ensures that the learned representation preserves the nearest-neighbor structure, providing a stability guarantee.
- **Joint-vs-marginal excess**: The spatial time series has both spatial structure (inter-sensor correlations) and temporal structure (within-sensor dynamics). The regularizers enforce that the joint spatio-temporal structure is maintained, not just the marginal spatial or temporal structure independently.
- **Null hypothesis**: Standard contrastive learning without structure preservation serves as the null. The improvement from topology/geometry regularizers quantifies the information content of the preserved structure.

**What is genuinely new**:
- Topology-preserving regularizer for contrastive learning: ensures that the learned embedding preserves the rank ordering of pairwise similarities.
- Application to traffic prediction (both macroscopic and microscopic), where the topology of traffic flow interactions must be preserved.

**Connections the authors acknowledge**: Cite contrastive learning (SimCLR, CPC), graph neural networks, transportation science. No connections to TDA proper, QEC, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Topology regularizer | Stability guarantee (nearest-neighbor structure preserved) |
| Geometry regularizer | Metric structure preservation |
| Rank ordering of similarities | Topological invariant of the representation |
| Spatio-temporal joint structure | Joint-vs-marginal excess (spatial + temporal) |

---

## TP-08 -- Chan, Al-Bashabsheh, Huang, Lim, Tam, Zhao (2019)
**"Neural Entropic Estimation: A faster path to mutual information estimation"**

**Domain(s)**: Information theory (MI estimation)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: MI-NEE estimates MI via an intermediate step of entropy estimation. By choosing the reference distribution for entropy estimation to be the uniform distribution (rather than the product of marginals as in MINE), the gradient signal is larger in low-density regions. This changes the joint-vs-marginal comparison: instead of comparing joint to product-of-marginals directly, MI-NEE compares both to a common reference (uniform), then takes the difference.
- **Null hypothesis**: The uniform distribution serves as a common null reference for both the joint and the marginal distributions. MI is recovered as D_KL(P_XY || U) - D_KL(P_X * P_Y || U).
- **Stability**: MI-NEE avoids the initialization problem of MINE where the network fails to learn at the start. The uniform reference provides gradients in regions where product-of-marginals gives zero gradient, leading to more stable initial training.

**What is genuinely new**:
- The observation that MINE's slow convergence is caused by the reference distribution choice. By changing from product-of-marginals to uniform, the same architecture converges faster.
- The triangulation approach: estimate two entropies relative to a common reference, then subtract.

**Connections the authors acknowledge**: Cite MINE, Donsker-Varadhan representation. Purely within MI estimation. No connections to TDA, QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| MI-NEE | Triangulated joint-vs-marginal estimation |
| Uniform reference distribution | Common null (alternative to product of marginals) |
| MINE | Direct joint-vs-marginal estimation |
| Entropy estimation (intermediate) | Decomposition into simpler sub-problems |

---

## TP-09 -- Li, Wang, Chen, Ren, Kawaguchi, Zeng (2024)
**"Towards Continual Learning Desiderata via HSIC-Bottleneck Orthogonalization and Equiangular Embedding"**
AAAI 2024

**Domain(s)**: Information theory, machine learning (continual learning)

**Abstract machines instantiated**:
- **Stability**: The paper addresses catastrophic forgetting -- an instability problem where learning a new task destroys previously learned knowledge. The HSIC-Bottleneck Orthogonalization (HBO) component prevents layer-wise parameter overwriting by projecting gradients onto the orthogonal complement of the previously important subspace. Updates for new tasks are constrained to directions that do not interfere with old task representations.
- **Joint-vs-marginal excess**: HSIC(Z, X) captures how much input information is retained (marginal), while HSIC(Z, Y) captures task-relevant information (joint). The bottleneck minimizes the former while maximizing the latter.
- **Chain complex (graded)**: The layer-wise HBO creates an independently controlled graded structure. Each layer l has its own orthogonalization constraint. The sequential task structure adds a second grading (by task index), creating a bigraded system: (layer, task).
- **Null hypothesis**: Standard continual learning without HBO/equiangular embedding serves as the null.

**What is genuinely new**:
- Combining HSIC bottleneck with gradient orthogonalization for continual learning without a memory buffer. Previous HSIC-based methods required rehearsal buffers.
- Equiangular Tight Frame (ETF) classifiers that fix the output layer geometry, preventing decision boundary distortion when new tasks are added.
- Achieves SOTA with constant model size and no stored exemplars.

**Connections the authors acknowledge**: Cite HSIC bottleneck (Ma et al. 2020), DualHSIC, and equiangular tight frames. No connections to TDA, QEC, dynamical systems, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Catastrophic forgetting | Instability under sequential perturbation (new tasks) |
| Gradient orthogonalization | Stability constraint (updates orthogonal to important subspace) |
| HSIC bottleneck | Joint-vs-marginal excess control per layer |
| Equiangular tight frame | Maximally separated output geometry |
| Layer-wise HBO | Graded stability (independent constraint per layer) |
| Sequential task learning | Parameterized system (task index as parameter) |

---

# Summary

## Search statistics
- **Total distinct search queries executed**: 47 (27 primary strategies + 20 supplementary content-level and follow-up searches)
- **Search strategies yielding zero results**: rate-distortion/source coding, channel capacity/Shannon limit, geometric deep learning/equivariant, representation learning+topology, manifold learning/UMAP, diffusion model/score matching, chain complex in title, boundary operator/coboundary, exact sequence, spectral sequence, derived functor/category, LDPC/algebraic coding, network information theory, Gromov-Wasserstein in title
- **Total papers with content retrieved and evaluated**: 38
- **Papers already in repo (skipped)**: ~20 (including Hodge-Aware CL, ITENE, Learning Generative Models across Incomparable Spaces, PID for discrete+continuous, Kernel Granger, Cohomology for Financial TS, GC Reconstruction of I&F, Convergence of DNNs with MI, Enhancing Financial TS Forecasting with TDA)
- **New papers annotated**: 9

## Coverage by machine

| Machine | Papers instantiating it |
|---|---|
| **Chain complex** | TP-01 (GC graph), TP-02 (node/edge grading), TP-04 (tree decomposition), TP-09 (bigraded layer x task) |
| **Parameterized homology** | TP-01 (frequency bands), TP-03 (finite-time window), TP-05 (frequency bands), TP-06 (spectral frequency) |
| **Matching** | TP-05 (causal role assignment) |
| **Stability** | TP-02 (isomorphism invariance), TP-03 (Shannon limit convergence), TP-06 (nonparametric robustness), TP-07 (topology/geometry preservation), TP-08 (convergence speed), TP-09 (gradient orthogonalization) |
| **Joint-vs-marginal excess** | TP-01 (spatial + temporal GC), TP-02 (GMI: node + edge), TP-03 (finite-time MI), TP-04 (multivariate redundancy tree), TP-05 (GC directed excess), TP-06 (spectral GC), TP-07 (spatio-temporal preservation), TP-08 (MI-NEE triangulation), TP-09 (HSIC per layer) |
| **Null hypothesis** | TP-01 (different stimulus), TP-02 (random representation), TP-03 (Shannon capacity), TP-04 (max entropy), TP-05 (alert state baseline), TP-06 (no-causality), TP-07 (no regularizer baseline), TP-08 (uniform reference), TP-09 (no HBO baseline) |

## Coverage by domain

| Domain | Papers |
|---|---|
| **TDA** | (none new -- Hodge-Aware CL already in repo) |
| **QEC** | (none new in this pass) |
| **Dynamical systems** | (none new -- Kernel Granger, Cohomology TS already in repo) |
| **Neuroscience** | TP-01 (EEG emotion), TP-05 (driver fatigue EEG), TP-06 (brain information flow) |
| **Information theory** | TP-01, TP-02, TP-03, TP-04, TP-06, TP-07, TP-08, TP-09 |

## Key new patterns discovered

1. **Frequency as filtration parameter in brain networks**: Multiple papers (TP-01, TP-05, TP-06) analyze brain connectivity at different EEG frequency bands. The frequency-resolved causal graph changes qualitatively across bands. This is structurally identical to persistence: track the topology of the causal network as the frequency "scale" parameter varies. The neuroscience community has not connected this to TDA's filtration framework.

2. **The PID lattice is a proto-chain complex**: The rooted-tree decomposition in TP-04 (and the redundancy lattice of PID generally) is a partially ordered set with Mobius inversion, structurally parallel to inclusion-exclusion on simplicial complexes. The PID atoms (synergy, redundancy, unique) decompose MI analogously to how the Hodge decomposition decomposes cochains. This connection is not made in any PID paper.

3. **Triangulation of MI estimation via common reference**: TP-08 (MI-NEE) shows that comparing joint and marginal distributions to a COMMON reference (uniform) rather than comparing them to EACH OTHER (as MINE does) yields faster convergence. This triangulation principle -- measuring two things relative to a shared null rather than directly against each other -- is a general strategy applicable beyond MI estimation. It parallels the use of invariant measures as universal references in dynamical systems.

4. **Orthogonal subspace projection as topological stability**: TP-09 prevents catastrophic forgetting by projecting gradient updates onto the orthogonal complement of the important subspace for previous tasks. This is structurally identical to the Hodge decomposition: the gradient component (task-relevant) is preserved, while the orthogonal component (new task direction) is the only one modified. The analogy: gradient = existing knowledge (harmonic component), update direction = new information (gradient/curl component), orthogonalization = ensuring independence of decomposition components.

5. **Granger causality as a tool for chain complex reconstruction**: TP-01, TP-05, TP-06 all use Granger causality to reconstruct directed networks (causal graphs) from time series data. These reconstructed networks ARE chain complexes (directed graphs with oriented edges). Combined with the existing repo's annotation of Kernel Granger causality (by-domain/information_theory.md) and GC Reconstruction of I&F Systems (by-domain/neuroscience.md), there is now a substantial body of evidence that Granger causality is the information-theoretic tool for chain complex reconstruction from dynamical data.

6. **GMI creates a graded information measure on complexes**: TP-02 defines separate MI terms for 0-cells (nodes) and 1-cells (edges) of a graph. This is a graded information measure -- one quantity per dimension of the complex. Extending GMI to simplicial complexes (adding 2-cell MI for triangles, etc.) would create an information-theoretic analogue of Betti numbers: one MI value per dimension, measuring how much information the representation preserves at each topological level.

## Gaps identified (for future passes)

The following search strategies yielded zero results in the link-forge database, suggesting these areas are underrepresented in the collection:
- Rate-distortion theory / lossy compression / source coding
- Channel capacity beyond finite-time MI
- Geometric deep learning / equivariant networks / gauge theory
- Representation learning explicitly paired with topology
- Manifold learning / UMAP with topological grounding
- Diffusion models / score matching with topological structure
- Chain complex, exact sequence, spectral sequence, derived functor in paper titles
- LDPC / algebraic coding theory with explicit topological connections
- Network information theory / distributed source coding
- Stochastic thermodynamics / fluctuation theorems
- Thermodynamics + information (Landauer principle)
