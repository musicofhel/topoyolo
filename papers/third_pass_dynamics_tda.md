# Third Pass -- Dynamical Systems & TDA Focus (2026-04-05)

Papers found by querying the link-forge Neo4j database with 20+ search strategies targeting dynamical systems and TDA papers not captured in previous passes. All 20 query strategies were executed (attractor/chaos, Morse/Conley, bifurcation, Lyapunov/ergodic, Takens/delay, sheaf, Mapper/Reeb, topological signal processing, persistent homology + dynamics, simplicial complex, Betti/Euler, Wasserstein + persistence, algebraic topology + ML, filtration, cubical complex, Rips/Cech, topological descriptor, symbolic dynamics, entropy rate, flow/trajectory + topology). Additional sweeps over content/description fields, tag-based queries (TAGGED_WITH), and specialized searches (visibility graph, ordinal pattern, coupled oscillators, FitzHugh-Nagumo, ensemble control, Lie algebra cohomology, polynomial chaos).

Filters applied: relevance to at least 2 abstract machines, not a duplicate of any paper in second_pass.md, by-domain/*.md, cross_domain_bridges.md, or inbox.md.

---

## TP-01 -- Structure-Preserving Contrastive Learning for Spatial Time Series
**Title**: "Structure preserving contrastive learning for spatial time series"
**Source**: link-forge (PDF), tagged: persistent-homology
**Domain(s)**: TDA, dynamical systems (time series), machine learning

**Abstract machines instantiated**:
- **Parameterized homology**: The topology-preserving regularizer uses persistent homology of the learned representations to enforce that the latent space retains the global similarity structure of the input time series. As the contrastive learning training proceeds (parameter = training epoch), the persistent homology of the embedding evolves, and the regularizer penalizes topological distortion. The dynamic weighting mechanism adaptively balances contrastive loss and topology preservation, creating a parameterized family of objectives whose topological content changes with training progress.
- **Joint-vs-marginal excess**: The two regularizers decompose structure into (1) topology-preserving (global: persistent homology of the full representation space) and (2) graph-geometry-preserving (local: pairwise distances between neighboring sensors). The global regularizer captures joint structure absent from any individual sensor's representation. The local regularizer captures pairwise joint structure. The contrastive loss alone (marginal) does not preserve these -- the regularizers add back the joint excess.
- **Stability**: The topology-preserving regularizer IS a stability constraint: it ensures that the persistent homology of the representation is close to that of the input. Under the Wasserstein metric on persistence diagrams, this bounds the topological distortion caused by the learned mapping. The method improves performance on traffic prediction, where temporal stability of spatial structure is essential.

**What is genuinely new**:
- First work to use persistent homology as a regularizer for contrastive learning of time series. Previous topology-preserving methods (TopoReg, etc.) apply to static point clouds, not spatio-temporal data.
- The dual-scale approach (global PH + local graph geometry) is novel: it captures both the macro-topology and the micro-geometry of the sensor network.
- The dynamic weighting mechanism adaptively trades off contrastive learning against structure preservation during training, avoiding the need to manually tune lambda coefficients.
- Validated on both classification (multivariate time series) and forecasting (traffic), showing the topology-preserving inductive bias helps across task types.

**Connections the authors acknowledge**: Cite persistent homology, Wasserstein distance on persistence diagrams, and graph-based contrastive learning. Position against standard CL methods (SimCLR, TS2Vec) that do not preserve structure. No connections to QEC, Hawkes processes, or information bottleneck.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Topology-preserving regularizer | PH stability constraint on the embedding |
| Graph-geometry regularizer | Local distance stability (pairwise joint structure) |
| Persistent homology of latent space | Parameterized topological invariant (parameter = epoch) |
| Dynamic weighting | Adaptive filtration-parameter schedule |
| Contrastive loss | Marginal objective (does not enforce structural stability) |
| Wasserstein distance on PDs | Stability metric for parameterized homology |
| Spatial time series | Multivariate dynamical observation on a graph |

---

## TP-02 -- Thai Stock Market Cohomology and de Rham Theory
**Title**: "The study of Thai stock market across the 2008 financial crisis" (truncated)
**Source**: link-forge (PDF), tagged: algebraic-topology, de-rham-cohomology, cohomology-theory
**Domain(s)**: TDA (algebraic topology), dynamical systems (financial markets)

**Abstract machines instantiated**:
- **Chain complex**: The paper constructs a full mathematical superstructure using de Rham cohomology on the space of correlation matrices. The correlation matrices form a manifold, and de Rham cohomology detects topological features of this manifold. Wilson loops over this space define holonomy -- closed paths whose integrated curvature detects non-trivial topology. The boundary operator is the exterior derivative d on differential forms, and d^2 = 0 is the chain complex condition. Pauli matrices provide a basis for the fiber (the local tangent space to the correlation manifold).
- **Parameterized homology**: Eight explicit market states are defined within a Kolmogorov space framework. As time evolves through the 2008 crisis, the state trajectory moves through these states. The topological invariants (cohomology classes) change character at the crisis point -- non-trivial cohomology appears during the crash (the manifold of correlations develops "holes" as correlations break down), creating a parameterized family with a phase transition.
- **Null hypothesis**: The pre-crisis and post-crisis states serve as "equilibrium" null models. The crash state has non-equilibrium topological invariants -- topological features that are absent in the calm-market null. The closeness centrality analysis of planar graphs provides a graph-theoretic null: a fully connected correlation graph has maximum centrality, and deviations from this indicate structural breakdown.
- **Stability**: The topological invariants (cohomology classes) are discrete and thus robust to small perturbations of the correlation matrix. This provides a natural smoothing/denoising: small changes in returns do not change the cohomology. The Wilson loop curvature provides a continuous stability diagnostic: smoothly varying curvature with abrupt changes at the crisis.

**What is genuinely new**:
- Application of de Rham cohomology and gauge theory (Wilson loops, Chern-Simons currents) to financial data. This is a genuine import from mathematical physics -- the tools are standard in gauge field theory but novel in finance.
- The identification of eight market states via Kolmogorov space and topological methods. Previous financial topology papers (Aste, Tumminello et al.) used minimal spanning trees or persistent homology; this paper uses differential-geometric cohomology.
- Tensor networks of correlation matrices as the base space for topological analysis. This connects to quantum information (tensor networks are standard there) but is novel in finance.
- Empirical mode decomposition (EMD) for validation provides a signal-processing cross-check on the topological findings.

**Connections the authors acknowledge**: Cite de Rham cohomology, Pauli matrices, Wilson loops from mathematical physics/gauge theory. Cite planar graphs and centrality from network science. Acknowledge the 2008 crisis literature. No connections to TDA (in the computational sense -- persistent homology, Rips complexes), QEC, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| de Rham cohomology | Chain complex cohomology (boundary = exterior derivative) |
| Wilson loop | Holonomy (cycle around the correlation manifold) |
| Chern-Simons current | Secondary characteristic class (boundary of a curvature form) |
| Pauli matrices | Fiber basis (local coordinates on the chain complex) |
| Correlation manifold | State space of the dynamical system |
| Market state | Point in the parameterized family |
| Crisis transition | Phase transition in parameterized cohomology |
| Tensor network | Compositional structure (relating chain complexes) |
| Closeness centrality | Graph-level null hypothesis diagnostic |

---

## TP-03 -- Cross-Correlation Integral and Attractor Density Wavelets
**Title**: "The cross-correlation integral: Its features and application to nonstationarity detection in time series"
**Source**: link-forge, DOI: 10.1134/1.1259701, tagged: dynamical-systems, nonlinear-dynamics
**Domain(s)**: Dynamical systems, information theory

**Abstract machines instantiated**:
- **Parameterized homology**: The cross-correlation integral C(epsilon) generalizes the Grassberger-Procaccia correlation integral to pairs of point clouds (two time windows). As the scale parameter epsilon varies, C(epsilon) traces a curve whose slope at each scale reveals dimensional information. For two windows from the same stationary process, C(epsilon) should be self-similar; deviations indicate nonstationarity. The parameter epsilon is the filtration scale, and the invariant being tracked is the correlation dimension (a fractal analogue of a Betti number).
- **Joint-vs-marginal excess**: The cross-correlation integral measures the overlap between the attractor densities from two time windows. If the windows are from the same stationary attractor, the cross-integral equals the auto-integral (joint = marginal). Nonstationarity manifests as a gap: the cross-integral is smaller than the geometric mean of the auto-integrals. This gap IS the joint-vs-marginal excess applied to attractor measures.
- **Stability**: The connection to wavelet transforms of attractor density provides a multiscale stability analysis. The wavelet coefficients at each scale quantify how much the attractor structure changes between time windows. Stable dynamics have similar wavelet coefficients across windows; instability appears as divergence.

**What is genuinely new**:
- The generalized cross-correlation integral as a tool for nonstationarity detection. Previous uses of the correlation integral (Grassberger-Procaccia) computed it on a single dataset to estimate dimension; this paper extends it to compare two datasets at multiple scales.
- The link to wavelet transforms of the attractor density function provides a bridge between dynamical systems theory and signal processing.
- The multiscale comparison explicitly parallels the filtration-based comparison in persistent homology -- the paper is doing a version of persistent homology comparison (via correlation integral) without using the PH framework.

**Connections the authors acknowledge**: Cite Grassberger-Procaccia correlation integral, wavelet theory, nonstationarity detection. No connections to TDA, persistent homology, or topological methods.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Cross-correlation integral C(epsilon) | Parameterized overlap measure (analogue of cross-persistence) |
| Scale parameter epsilon | Filtration parameter |
| Correlation dimension | Fractal analogue of Betti number |
| Attractor density | Measure on the reconstructed manifold |
| Nonstationarity | Change in parameterized invariant (phase transition) |
| Wavelet coefficient at scale s | Scale-resolved stability diagnostic |
| Auto-correlation integral | Marginal invariant (single window) |
| Cross minus auto gap | Joint-vs-marginal excess (detects structural change) |

---

## TP-04 -- Entropic Characterization of Symmetry Breaking in Dynamical Systems
**Title**: "On Entropic Characterization of Symmetry Breaking in Dynamical Systems I: Spontaneous and Dynamical Symmetry Breaking"
**Source**: link-forge, arXiv: 2510.03572, tagged: dynamical-systems, nonlinear-dynamics
**Domain(s)**: Dynamical systems, information theory

**Abstract machines instantiated**:
- **Parameterized homology**: The framework tracks entropy and information transfer as a dynamical system approaches a symmetry-breaking transition. The control parameter (e.g., temperature, coupling strength) parameterizes a family of dynamical systems. At the critical point, the symmetry group of the dynamics reduces -- this is a discrete change in the algebraic structure of the system, analogous to a topological phase transition. The entropy of the system's invariant measure traces a curve parameterized by the control variable, with a singularity (non-analyticity) at the critical point.
- **Null hypothesis**: The symmetric state IS the null model. Symmetry breaking is departure from the null: the system's dynamics no longer respect the full symmetry group. The entropy production and information transfer metrics quantify the magnitude of this departure. The "dynamical slowdown" (critical slowing down) is a diagnostic for proximity to the phase transition -- it is the analogue of a test statistic that grows as the null is violated.
- **Stability**: The link between symmetry loss and dynamical slowdown is itself a stability result: as the system approaches the critical point, its relaxation time diverges -- small perturbations take longer to decay. This is the opposite of stability (loss of stability at the bifurcation), and the entropy framework provides quantitative diagnostics for this loss.
- **Joint-vs-marginal excess**: Information transfer between subsystems changes character at symmetry breaking. In the symmetric phase, information flow respects the symmetry (all directions equivalent). After breaking, directed information flow emerges -- some directions carry more information than others. This asymmetry is joint excess absent from the symmetric (marginal) description.

**What is genuinely new**:
- A unified entropy/information-transfer framework for characterizing BOTH spontaneous and dynamical symmetry breaking. Previous work treated these separately (Landau theory for spontaneous, Floquet theory for dynamical).
- The connection between entropy growth and symmetry loss provides an information-theoretic diagnostic for bifurcations that does not require identifying the specific symmetry being broken.
- The "anticipation" aspect: the entropy and information transfer diagnostics can detect approaching symmetry breaking before the critical point -- a form of early warning signal.

**Connections the authors acknowledge**: Cite entropy production theory, information transfer (transfer entropy), critical phenomena. Position at the dynamical systems / information theory interface. No connections to TDA, QEC, or persistent homology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Symmetry group | Algebraic structure of the null model |
| Symmetry breaking | Phase transition (null hypothesis rejection) |
| Control parameter | Filtration parameter in parameterized family |
| Entropy at criticality | Singularity in the parameterized invariant |
| Critical slowing down | Loss of stability (diverging relaxation time) |
| Information transfer | Directed joint excess between subsystems |
| Dynamical slowdown | Pre-transition instability diagnostic |
| Symmetric phase | Null regime |

---

## TP-05 -- Ordinal Networks for Time Series Characterization
**Title**: "Ordinal network" (untitled in link-forge; describes ordinal network methodology)
**Source**: link-forge (PDF)
**Domain(s)**: Dynamical systems, information theory

**Abstract machines instantiated**:
- **Chain complex (weak)**: Ordinal networks are directed graphs built from the temporal succession of ordinal (permutation) patterns. Each node is an ordinal pattern (e.g., "up-down-up" for a window of length 3), and edges connect consecutive patterns. This graph has a well-defined adjacency matrix A. While not a chain complex in the strict sense, the graph Laplacian L = D - A operates on 0-chains (functions on nodes), and the kernel of L detects connected components. The transition matrix T = D^{-1}A defines a Markov chain whose invariant measure captures the long-run distribution of ordinal patterns.
- **Null hypothesis**: The exact adjacency matrices for random (IID) series are derived analytically. This provides a principled null model: the ordinal network for a random process has known structure (uniform distribution over allowed transitions). Departures from this null indicate temporal dependence -- the series has structure that a random process lacks. The local network entropy is shown to be robust against noise, making it a reliable test statistic.
- **Parameterized homology**: The pattern length m (number of consecutive values defining a pattern) controls the resolution. As m increases, the number of possible patterns grows as m!, and the ordinal network becomes increasingly detailed. For a random process, all m! patterns appear with equal probability; for a structured process, only a subset appears. The effective dimension of the ordinal network (number of well-populated nodes) is a parameterized invariant that increases with m for complex processes and saturates for simple ones.
- **Matching**: The method estimates Hurst exponents with accuracy rivaling detrended fluctuation analysis. This is an implicit matching: the ordinal network structure of an empirical series is matched to a family of fractional processes parameterized by H, and the best-matching H is the estimate.

**What is genuinely new**:
- Constructing networks from ordinal pattern successions (not just counting pattern frequencies as in permutation entropy). The network structure captures transition dynamics -- which patterns tend to follow which -- information lost in the frequency-only approach.
- Exact analytical results for the null (random series) adjacency matrix enable rigorous hypothesis testing without simulation.
- Application to seismological data: detecting sudden changes in earthquake dynamics after large events. The network entropy drops sharply after a large earthquake, indicating a transition from complex to simple dynamics.
- Robustness of local network entropy to observational noise, making it practical for noisy real-world data.

**Connections the authors acknowledge**: Cite Bandt & Pompe (2002) permutation entropy, visibility graphs (Lacasa et al., 2008), recurrence networks. Position as a complementary approach to visibility graphs for time-series-to-network transformation. No connections to TDA, QEC, or persistent homology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Ordinal pattern | Local combinatorial invariant (window descriptor) |
| Ordinal network | Transition graph (directed 1-complex) |
| Adjacency matrix A | Weighted boundary-like operator |
| Random series null | IID null model (uniform distribution over patterns) |
| Local network entropy | Parameterized complexity measure |
| Pattern length m | Resolution / filtration parameter |
| Hurst exponent estimation | Matching to parameterized family |
| Transition probability | Joint excess (successive pattern dependence) |

---

## TP-06 -- Instability of Financial Time Series via Directed Visibility Graphs
**Title**: "Instability of Financial Time Series Revealed by Irreversibility Analysis"
**Source**: link-forge, DOI: 10.3390/e27040402
**Domain(s)**: Dynamical systems, information theory

**Abstract machines instantiated**:
- **Null hypothesis**: The method detects irreversibility in time series -- departure from time-reversal symmetry. A reversible (equilibrium) process is the null: for such processes, the visibility graph from the forward series is statistically identical to that from the reversed series. The KL divergence between the degree distributions of the forward and reversed directed horizontal visibility graphs (dHVGs) is the test statistic. High KLD indicates irreversibility, which implies the system is far from equilibrium.
- **Parameterized homology**: The sliding window creates a time-parameterized family of visibility graphs. As the window moves through the 2004-2022 period, the KLD traces a curve over time. Spikes in this curve correspond to financial instabilities (crises, market anomalies). The parameter is time, and the invariant is the KLD of the visibility graph degree distribution.
- **Stability**: The directed horizontal visibility graph construction is deterministic given the time series, making the method robust to noise. The KLD metric provides a continuous measure of departure from the null (reversibility), and the sliding window approach makes it sensitive to local instabilities while averaging out global noise.

**What is genuinely new**:
- Combining directed horizontal visibility graphs with irreversibility analysis for financial instability detection. Previous visibility graph work focused on degree distribution scaling (Lacasa et al.); this adds a directionality analysis that detects time-asymmetry.
- Application to a comprehensive dataset (global financial markets, 2004-2022) spanning multiple crises (2008, COVID, etc.).
- The connection between irreversibility (a thermodynamic concept) and financial instability provides a physics-inspired diagnostic for market health.

**Connections the authors acknowledge**: Cite Lacasa et al. on visibility graphs, time-series irreversibility literature, KL divergence. No connections to TDA, persistent homology, or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Directed horizontal visibility graph | Directed 1-complex from time series |
| Degree distribution | 0-chain statistic on the graph |
| KL divergence (forward vs reversed) | Null hypothesis test statistic |
| Reversibility | Null model (equilibrium, time-symmetric) |
| Irreversibility | Departure from null (non-equilibrium structure) |
| Sliding window | Time-parameterized family |
| Financial instability | Phase transition in the parameterized invariant |

---

## TP-07 -- Specific Differential Entropy Rate Estimation
**Title**: "Specific Differential Entropy Rate Estimation for Continuous Valued Time Series"
**Source**: link-forge (PDF), tagged: nonlinear-dynamics
**Domain(s)**: Information theory, dynamical systems

**Abstract machines instantiated**:
- **Parameterized homology**: The specific differential entropy rate is a function of the current state: h(x) quantifies how unpredictable the next observation is given that the system is currently at state x. This creates a parameterized family: as the state x varies over the attractor, the entropy rate traces a function whose shape encodes the dynamics. States near the attractor's stable manifold have low h(x) (predictable); states near the chaotic saddle have high h(x) (unpredictable). This state-dependent entropy function is a parameterized invariant of the dynamical system.
- **Joint-vs-marginal excess**: The standard (non-specific) entropy rate is the average of h(x) over the invariant measure: h_avg = integral h(x) d(mu). The specific entropy rate decomposes this average into its state-dependent components. The variation of h(x) around h_avg is the joint-vs-marginal excess: states where h(x) >> h_avg have unexpectedly high unpredictability (given the marginal average), while states where h(x) << h_avg are unexpectedly predictable. The full function h(x) contains strictly more information than the scalar h_avg.
- **Null hypothesis**: For a stationary process with a well-defined entropy rate, the null is that unpredictability is uniform across states (h(x) = h_avg for all x). Departures from this uniformity indicate state-dependent dynamics -- the system's predictability varies with its configuration. For i.i.d. processes, h(x) is indeed constant.

**What is genuinely new**:
- Extending Shannon entropy rate from a single number (the average) to a function of the system's state. This is a substantial conceptual advance: most dynamical complexity measures are global (Lyapunov exponents, correlation dimension, standard entropy rate); this is local.
- The conditional density estimation approach makes the method applicable to continuous-valued data without binning or symbolization.
- Application to heart rate variability (HRV) data demonstrates practical utility in physiological time series analysis, where different cardiac states have different predictability.

**Connections the authors acknowledge**: Cite Shannon entropy, Kolmogorov-Sinai entropy, conditional density estimation. Apply to nonlinear dynamics and physiology. No connections to TDA, QEC, or persistent homology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Specific entropy rate h(x) | State-parameterized invariant |
| Average entropy rate h_avg | Marginal (averaged) invariant |
| Variation h(x) - h_avg | Joint-vs-marginal excess at state x |
| State x on attractor | Point in the parameterized family |
| Uniform h(x) | Null model (state-independent unpredictability) |
| Conditional density p(x_{t+1} | x_t) | Local dynamics (transition kernel) |
| HRV application | Physiological dynamical system |

---

## TP-08 -- CP-PINNs: Changepoint Detection in PDE Dynamics
**Title**: "CP-PINNs: Data-Driven Changepoints Detection in PDEs Using Online Optimized Physics-Informed Neural Networks"
**Source**: link-forge (PDF), tagged: dynamical-systems
**Domain(s)**: Dynamical systems, machine learning

**Abstract machines instantiated**:
- **Parameterized homology**: The PDE parameters theta(t) are piecewise constant in time, with abrupt changes at unknown changepoints. The family of PDEs parameterized by theta defines a parameterized system whose qualitative behavior changes at each changepoint. The Total Variation penalty on theta(t) enforces sparsity of changes -- analogous to enforcing that the parameterized homology changes at only finitely many critical parameter values.
- **Null hypothesis**: The null model is a single PDE with constant parameters (no changepoints). The CP-PINN method tests whether allowing time-varying parameters significantly reduces the physics-informed loss. Each detected changepoint is a rejection of the constant-parameter null for a specific time interval.
- **Stability**: The exponentiated descent online learning scheme for dynamically re-weighting loss function terms comes with theoretical regret bounds. These bounds guarantee that the algorithm's cumulative loss is close to that of the best fixed weighting in hindsight -- a form of algorithmic stability. The Total Variation penalty also provides stability by preventing over-fitting to noise (which would produce spurious changepoints).

**What is genuinely new**:
- Combining physics-informed neural networks with changepoint detection. Previous PINNs assumed fixed PDE parameters; CP-PINNs allow them to change over time.
- The online learning scheme with regret bounds provides theoretical guarantees for the weight adaptation, unlike heuristic weighting strategies used in standard PINNs.
- The TV penalty on parameters directly enforces the structural assumption (piecewise constant dynamics) that is standard in changepoint detection but novel in the PINN context.

**Connections the authors acknowledge**: Cite PINNs (Raissi et al.), online convex optimization, Total Variation regularization. No connections to TDA, QEC, or topological methods.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| PDE parameters theta(t) | Filtration parameter (piecewise constant) |
| Changepoint | Critical parameter value (topology/dynamics changes) |
| Total Variation penalty | Sparsity constraint on parameter changes |
| Constant-parameter PDE | Null model (no transitions) |
| Physics-informed loss | Structural constraint (the PDE defines the chain complex) |
| Regret bound | Algorithmic stability guarantee |
| Exponentiated descent | Adaptive weighting (parameterized optimization) |

---

## TP-09 -- Unstable Wave Patterns in FitzHugh-Nagumo Neural Networks
**Title**: "Unstable wave patterns of information in neural network under light illumination and magnetic field"
**Source**: link-forge, DOI: 10.1142/s021797922450200x, tagged: nonlinear-dynamics
**Domain(s)**: Dynamical systems, neuroscience

**Abstract machines instantiated**:
- **Parameterized homology**: The FitzHugh-Nagumo neural network is studied under varying light illumination and magnetic flux -- two control parameters. As these parameters vary, the system transitions between different wave pattern regimes (stable plane waves, modulated patterns, spatiotemporal chaos). Each regime has a distinct topological character (the spatial wave pattern defines a different type of structure). The modulational instability (MI) analysis identifies critical parameter values where the base pattern becomes unstable -- these are the bifurcation points in the parameterized family.
- **Stability**: Modulational instability analysis IS stability analysis: it determines whether small perturbations to a uniform wave pattern grow or decay. The growth rate of perturbations (MI gain) as a function of wavenumber maps out the instability spectrum. Stable patterns (zero MI gain) are robust to perturbation; unstable patterns (positive MI gain) spontaneously develop spatial structure.
- **Null hypothesis**: The uniform (plane wave) solution is the null model. Pattern formation is departure from the null -- spontaneous emergence of spatial structure from a homogeneous state. The MI analysis quantifies the growth rate of this departure as a function of the perturbation wavenumber.

**What is genuinely new**:
- The combination of memristive coupling, photosensitivity, and magnetic flux in a FitzHugh-Nagumo network creates a three-parameter space of pattern formation dynamics. Previous work on FHN pattern formation considered fewer control parameters.
- The memristive coupling introduces memory-dependent dynamics that enrich the bifurcation structure beyond classical diffusive coupling.
- The magnetic flux as a control parameter connecting the neuroscience model (FHN) to condensed matter (Aharonov-Bohm-like effects).

**Connections the authors acknowledge**: Cite FitzHugh-Nagumo model, modulational instability theory, pattern formation literature. Acknowledge the neural network interpretation (biological plausibility of coupled neurons). No connections to TDA, QEC, or persistent homology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Light illumination / magnetic flux | Control parameters (filtration axes) |
| Modulational instability gain | Stability diagnostic (growth rate of perturbation) |
| Plane wave solution | Null model (uniform, no spatial structure) |
| Pattern formation | Null hypothesis rejection (spontaneous structure emergence) |
| Wave pattern regime | Phase in the parameterized family |
| Bifurcation point | Critical parameter value |
| FitzHugh-Nagumo equations | Dynamical system on a network (chain-like structure) |
| Memristive coupling | Memory-dependent boundary operator |

---

## TP-10 -- Higher-Order Network Compression via Information Theory
**Title**: "Compressing higher-order networks without losing what matters" (via Jorge Bravo Abad tweet)
**Source**: link-forge (Twitter/X), published in Physical Review Letters
**Domain(s)**: TDA (higher-order networks), information theory

**Abstract machines instantiated**:
- **Chain complex**: Higher-order hypergraph networks have group interactions at multiple orders: pairwise (edges), 3-way (triangles), 4-way, etc. Each order k defines a set of k-simplices, and the collection forms a (truncated) chain complex. The question is: which interaction orders carry genuinely new structural information? The compression framework identifies redundant orders -- those whose structure is fully determined by lower orders -- and removes them.
- **Joint-vs-marginal excess**: The core information-theoretic criterion measures whether a k-body interaction is predictable from (k-1)-body interactions. If the k-body structure is fully determined by the lower-order marginals, the k-body interactions carry no excess information and can be compressed away. If the k-body structure contains information absent from all lower-order marginals, it represents genuine joint-vs-marginal excess and must be retained.
- **Null hypothesis**: The null model at each order k is: "the k-body interactions are fully determined by the (k-1)-body interactions." Retaining an interaction order means rejecting this null -- the k-body level carries genuinely new information. The method provides a principled way to determine the minimal representation of a higher-order network.

**What is genuinely new**:
- An information-theoretic criterion for determining which interaction orders in a hypergraph carry genuinely new information. Previous approaches to higher-order networks either kept all orders or used ad hoc truncation.
- The compression scheme preserves the "structural information" (in the information-theoretic sense) while reducing representational cost.
- Published in PRL, indicating broad physics community interest in higher-order network simplification.

**Connections the authors acknowledge**: Cite higher-order network literature, information theory, hypergraph models. No connections to persistent homology, QEC, or Koopman operators.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| k-body interaction | k-simplex in the chain complex |
| Interaction order k | Chain complex dimension |
| Information carried by order k | Homological content at grade k |
| Redundant order | Exact chain (homologically trivial) |
| Genuinely new information | Non-trivial homology at grade k |
| Compression | Chain complex truncation (removing trivial grades) |
| Lower-order predictability | Boundary/coboundary structure (determined by neighbors) |
| Hypergraph network | Simplicial complex (or more general cell complex) |

---

## TP-11 -- IC-PINN for Coupled Oscillator Coupling Functions
**Title**: "Physics-informed neural networks for inferring how coupled oscillators interact" (via Jorge Bravo Abad tweet)
**Source**: link-forge (Twitter/X), tagged: dynamical-systems
**Domain(s)**: Dynamical systems, neuroscience (embryonic clocks)

**Abstract machines instantiated**:
- **Parameterized homology**: The coupling function H(phi_1, phi_2) describes how oscillator phases interact. IC-PINN learns this function from data without assuming a parametric form (no Fourier basis, no polynomial expansion). The coupling function is defined on the torus T^2 (phase pairs), and its structure -- peaks, nodes, symmetries -- encodes the dynamics. As the physical parameters change (coupling strength, natural frequency detuning), the coupling function changes shape, creating a parameterized family.
- **Matching**: The inference task is an implicit matching: given observed phase trajectories, find the coupling function that best explains the data. This is a function-level matching problem -- assigning a coupling function (from an infinite-dimensional function space) to the observed dynamics.
- **Stability**: The physics-informed loss enforces the phase oscillator equation as a soft constraint. This physics prior provides stability: the learned coupling function must be consistent with the governing equations, preventing over-fitting to noise. The method is validated on experimental data (embryonic clocks, spinning nanorods), demonstrating robustness to real-world measurement noise.

**What is genuinely new**:
- Basis-free inference of coupling functions. Previous methods (Kralemann et al., Stankovski et al.) required choosing a Fourier or polynomial basis; IC-PINN learns the function directly via neural networks.
- Validation on two biological/physical systems: embryonic segmentation clocks (where the coupling function controls somite formation timing) and spinning nanorods (where hydrodynamic coupling is complex).
- The method captures non-sinusoidal coupling that standard Kuramoto-type models miss.

**Connections the authors acknowledge**: Cite Kuramoto model, phase reduction theory, PINNs. Apply to developmental biology (somitogenesis) and soft matter physics. No connections to TDA, QEC, or information theory.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Coupling function H(phi_1, phi_2) | Interaction kernel on the torus (joint structure) |
| Phase oscillator equations | Dynamical constraint (the governing chain complex) |
| Basis-free inference | Non-parametric matching |
| Coupling strength | Parameter in the parameterized family |
| Physics-informed loss | Structural stability constraint |
| Embryonic clocks | Biological oscillator network |
| Torus T^2 | Phase space (the manifold underlying the dynamics) |

---

## TP-12 -- Ensemble Control on Lie Groups
**Title**: "Ensemble Control on Lie Groups"
**Source**: link-forge (PDF), tagged: dynamical-systems
**Domain(s)**: Dynamical systems (control theory)

**Abstract machines instantiated**:
- **Chain complex (algebraic)**: The Cartan decomposition of semisimple Lie algebras g = k + p decomposes the algebra into compact (k) and non-compact (p) parts. The Lie bracket relations [k,k] subset k, [k,p] subset p, [p,p] subset k define an algebraic grading that is structurally analogous to a Z/2-graded chain complex. The covering method iteratively generates Lie subgroups from this decomposition, building up the full group from algebraically graded pieces.
- **Matching**: The ensemble controllability problem is an assignment problem: find a single control signal u(t) that simultaneously steers ALL systems in the population to their respective targets. Each individual system maps the control u(t) to a trajectory on the Lie group. The covering method reduces this infinite-dimensional matching (one control to many systems) to a finite-dimensional problem (one control to finitely many subsystem generators).
- **Stability**: The main theorem establishes that classical controllability of individual systems implies ensemble controllability. This is a "lifting" stability result: stability (controllability) at the individual level lifts to stability at the population level. The covering method provides the constructive proof: if each subsystem is controllable, the ensemble can be steered via the covering decomposition.

**What is genuinely new**:
- Extension of ensemble controllability from SO(3) (previous work) to all semisimple Lie groups, including non-compact groups. This is a substantial generalization with applications to quantum control on SU(n) and classical control on SE(3).
- The covering method leveraging Cartan decompositions is a novel proof technique that converts the infinite-dimensional ensemble problem to finite-dimensional subsystem analysis.
- The algebraic structure (Cartan decomposition) does the heavy lifting -- this is a case where algebraic topology-like thinking (graded decomposition) directly solves a control theory problem.

**Connections the authors acknowledge**: Cite Lie group theory, ensemble control theory, quantum control. No connections to TDA, information theory, or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Semisimple Lie algebra g | Algebraic structure (graded by Cartan decomposition) |
| Cartan decomposition g = k + p | Z/2-grading (analogous to chain complex grading) |
| Ensemble controllability | Population-level stability (single input steers all) |
| Covering method | Constructive decomposition (building from graded pieces) |
| Broadcast control signal | Shared boundary operator (acts on all chain components) |
| Individual controllability | Local stability (single system) |
| Lie subgroup generation | Graded construction of the full group |

---

## TP-13 -- Deep Arbitrary Polynomial Chaos Neural Networks
**Title**: "The Deep Arbitrary Polynomial Chaos Neural Network or how Deep Artificial Neural Networks..."
**Source**: link-forge (PDF)
**Domain(s)**: Machine learning, dynamical systems (uncertainty quantification)

**Abstract machines instantiated**:
- **Chain complex (weak)**: The DaPC NN constructs adaptive multi-variate orthonormal bases on each node, with the network layers forming a graded structure. Each layer's polynomial chaos expansion operates in a space determined by the data distribution at that layer. The layer-to-layer transformation involves projecting signals through these adaptive bases, creating a graded chain of function spaces. While not a strict chain complex, the orthogonality constraints (inner product structure) between layers create algebraic structure analogous to the orthogonal decomposition in Hodge theory.
- **Parameterized homology**: Polynomial chaos expansion (PCE) is parameterized by the polynomial order p. As p increases, the expansion captures higher-order nonlinear interactions. The "homogeneous chaos" of Wiener is the theoretical foundation: the functional space is decomposed by polynomial order, and each order captures a specific complexity level. The convergence over training data size (the paper's key result) is a parameterized convergence where the order of approximation trades off against data requirements.
- **Null hypothesis**: The conventional deep neural network (with fixed activation functions) serves as the null. The DaPC NN's data-driven orthonormal bases systematically outperform conventional activations because they eliminate redundant signal representation. The improvement over the null demonstrates that the polynomial chaos structure carries useful information beyond what standard architectures capture.

**What is genuinely new**:
- Reinterpreting deep neural network layers through the lens of data-driven polynomial chaos (arbitrary PCE). This is a genuine conceptual bridge: polynomial chaos is standard in uncertainty quantification (UQ), and deep learning is standard in ML, but this paper connects them at the architectural level.
- The claim that DaPC NN enables "high-order neural interactions" that reduce dependence on activation functions is a structural insight about neural network expressivity.
- Convergence improvement over training data size is demonstrated empirically.

**Connections the authors acknowledge**: Cite Wiener polynomial chaos, arbitrary PCE (aPC), deep neural networks. Position at the uncertainty quantification / deep learning interface. No connections to TDA, QEC, or dynamical systems proper (though PCE is widely used in dynamical systems UQ).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Polynomial chaos expansion | Graded functional decomposition |
| Polynomial order p | Filtration parameter (complexity level) |
| Orthonormal basis (data-driven) | Adapted basis for the chain complex |
| Layer-wise PCE | Graded component of the decomposition |
| Homogeneous chaos (Wiener) | Pure-order component (analogous to homology at grade k) |
| Convergence over data size | Stability of the invariant under sampling |
| Conventional DNN | Null model (no polynomial chaos structure) |

---

## TP-14 -- Hom-Lie Algebra Representations and Cochain Complexes
**Title**: "Representations of hom-Lie algebras"
**Source**: link-forge (PDF), tagged: cohomology
**Domain(s)**: Pure mathematics (algebra), TDA (cohomological structures)

**Abstract machines instantiated**:
- **Chain complex**: The paper constructs cochain complexes for hom-Lie algebras -- algebraic structures where the Jacobi identity is twisted by a linear map alpha. The cochain complex C^n(g, M) with coboundary operator delta satisfying delta^2 = 0 is explicitly constructed for adjoint and trivial representations. This is a genuine chain complex (in the dual/cochain sense), and the resulting cohomology groups H^n(g, M) classify deformations and extensions of the hom-Lie algebra.
- **Parameterized homology**: The twisting map alpha parameterizes a family of algebraic structures. When alpha = id, the hom-Lie algebra reduces to an ordinary Lie algebra, and the cohomology reduces to Chevalley-Eilenberg cohomology. As alpha deviates from the identity, the cohomology changes -- some classes persist, others are born or die. This is a parameterized family of cochain complexes, with the cohomology varying as the parameter (the twisting map) changes.
- **Stability**: The "alpha^s-adjoint representations" (parameterized by integer s) provide a family of representations that continuously deform the adjoint representation. The cohomology's dependence on s measures the stability of algebraic features under deformation of the representation.

**What is genuinely new**:
- The systematic development of cochain complexes for hom-Lie algebras is foundational. Hom-Lie algebras are natural generalizations of Lie algebras that appear in deformation quantization, quantum groups, and discretization of differential geometry.
- The alpha^s-adjoint representations provide an infinite family of representations parameterized by a single integer, creating a naturally parameterized cohomological setup.
- Applications to formal deformations (infinitesimal: H^2 controls deformations; obstructions: H^3) and central extensions (H^2 with trivial coefficients) directly parallel the role of Hochschild/Chevalley-Eilenberg cohomology in classical algebra.

**Connections the authors acknowledge**: Cite Hartwig, Larsson, Silvestrov on hom-Lie algebras; Chevalley-Eilenberg cohomology; Nijenhuis-Richardson deformation theory. Purely algebraic setting -- no connections to TDA (computational), dynamical systems, QEC, or applied domains.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Cochain complex C^n(g, M) | Chain complex (dual grading) |
| Coboundary delta | Boundary operator (in cohomological grading) |
| delta^2 = 0 | Chain complex condition |
| Cohomology H^n | Invariant of the algebraic structure |
| Twisting map alpha | Deformation parameter |
| alpha = id | Undeformed (classical Lie algebra) limit |
| alpha^s-adjoint | Parameterized family of representations |
| H^2 controls deformations | Moduli of the parameterized family |
| H^3 obstructions | Stability constraint (when deformations fail to extend) |

---

## TP-15 -- Barandes Stochastic-Quantum Correspondence
**Title**: "2309.03085v1" (Jacob Barandes, Harvard)
**Source**: link-forge (PDF), arXiv: 2309.03085, tagged: dynamical-systems
**Domain(s)**: Dynamical systems, quantum mechanics (QEC-adjacent)

**Abstract machines instantiated**:
- **Chain complex (structural)**: The stochastic-quantum theorem establishes a precise correspondence between generalized stochastic systems (encompassing Markov chains) and unitarily evolving quantum systems. The Hilbert space structure of quantum mechanics (with its graded tensor product decomposition for composite systems) emerges from the stochastic framework. The correspondence maps transition matrices (stochastic dynamics) to unitary operators (quantum dynamics), preserving algebraic structure.
- **Joint-vs-marginal excess**: The correspondence reveals why quantum mechanics uses complex numbers and Hilbert spaces: these structures are necessary to encode the full joint information in a stochastic system. A classical probability distribution (marginal) does not uniquely determine the quantum state (joint); the phases of the quantum amplitudes encode the joint-vs-marginal excess -- information about transition probabilities that is absent from the instantaneous marginal distribution.
- **Parameterized homology**: The paper constructs a continuous family of correspondences parameterized by the system's transition structure. Different stochastic processes map to different quantum systems. The Born rule and unitary evolution are not axioms but consequences of the correspondence -- they are the quantum "invariants" that persist across the parameterized family.
- **Null hypothesis**: Classical (real, positive) stochastic processes serve as the null. Quantum phenomena are departures from this null -- the complex phases, superposition, and entanglement are all "excess structure" not present in the classical stochastic null.

**What is genuinely new**:
- A new formulation of quantum theory derived from classical stochastic processes. This is a foundational result that provides first-principles explanations for complex numbers, Hilbert spaces, linear-unitary evolution, and the Born rule in quantum mechanics.
- The suggestion that quantum computers can simulate any generalized stochastic process efficiently opens a computational bridge between classical stochastic simulation and quantum computation.
- The framework unifies Markov chains (discrete time, finite state) and random dynamical systems (continuous time, continuous state) under a single quantum-stochastic correspondence.

**Connections the authors acknowledge**: Cite Hilbert-space formulations of QM, path integral formulations, quasiprobability approaches. Explicitly claim this is a new formulation alongside these. No connections to TDA, information theory (beyond basic probability), or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Generalized stochastic system | Classical dynamical system (the marginal picture) |
| Unitary quantum system | Lifted representation (encoding full joint structure) |
| Transition matrix | Dynamical operator (boundary-like map between states) |
| Quantum phases | Joint-vs-marginal excess (invisible in marginal distribution) |
| Born rule | Measurement map (projection from joint to marginal) |
| Complex Hilbert space | Enriched state space (encodes excess information) |
| Classical limit | Null model (phases vanish, pure marginal) |
| Stochastic-quantum theorem | Correspondence principle (structural isomorphism) |

---

## TP-16 -- Pointwise Ergodic Theorem for Fuchsian Groups
**Title**: "A pointwise ergodic theorem for Fuchsian groups"
**Source**: link-forge (PDF)
**Domain(s)**: Dynamical systems (ergodic theory), pure mathematics

**Abstract machines instantiated**:
- **Chain complex (algebraic)**: The Fuchsian group acts on the hyperbolic plane, and the fundamental domain has boundary structure encoded by the generators and their relations. The Bowen-Series coding maps the group action to a symbolic dynamical system with a Markovian transition structure. The irreducible transition matrix defines a directed graph (a 1-complex) whose adjacency structure captures the algebraic relations of the group.
- **Stability**: The pointwise ergodic theorem IS a stability result: the Cesaro averages of spherical averages converge almost everywhere to the space average. This means that time averages (along orbits) equal space averages -- the measurement is robust to the choice of starting point (almost everywhere). The convergence is proved via reduction to the free semigroup case, where it follows from the Rota theorem.
- **Null hypothesis**: The space average (integral against the invariant measure) is the null expectation. The ergodic theorem states that time averages converge to this null almost surely. Departures from ergodicity (if they existed) would indicate non-mixing regions -- subsets of the space that are dynamically isolated.

**What is genuinely new**:
- Extension of the pointwise ergodic theorem from surface groups (genus >= 2) to all finitely generated Fuchsian groups whose generators arise from fundamental domains with even corners.
- The proof technique: reducing the group-theoretic ergodic theorem to a known result for free semigroups via the Bowen-Series coding. This is a bridge between geometric group theory and symbolic dynamics.
- The use of Markovian coding (a symbolic dynamics tool) to solve an ergodic theory problem on hyperbolic groups.

**Connections the authors acknowledge**: Cite Bowen-Series coding, ergodic theory, hyperbolic geometry. Purely within mathematics -- no connections to applied domains.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Fuchsian group | Symmetry group of the dynamical system |
| Cesaro average | Time average (running mean of orbit values) |
| Pointwise convergence | Stability of measurement (time avg = space avg) |
| Bowen-Series coding | Symbolic dynamics representation (Markov chain) |
| Irreducible transition matrix | Connectivity structure of the symbolic chain complex |
| Invariant measure | The null expectation (what time averages converge to) |
| Even corners of fundamental domain | Algebraic constraint on the generators |
