# Third Pass -- Neuroscience & QEC Deep Dive (2026-04-05)

Papers found by querying the link-forge Neo4j database with 30+ search strategies targeting neuroscience and quantum error correction, filtered for relevance to the topo-rosetta 6 abstract machines (chain complex, parameterized homology, matching, stability, joint-vs-marginal excess, null hypothesis).

**Search strategies executed**: neural coding / neural manifold / population geometry; TDA + brain / neural / cortex; place cells / grid cells / hippocampus + topology; quantum LDPC / surface code / toric code / homological code; syndrome decoding / decoder / error correction + matching; stabilizer code / CSS code / color code / Floquet code; consciousness / IIT / Phi; neural oscillation / phase-amplitude / cross-frequency; connectome / brain network + homology; quantum channel / fault tolerant; persistent homology + neuroscience; simplicial complex + neural; tag-traversal via TAGGED_WITH for all relevant tags; description-level searches for attractor, dynamical system, phase transition, belief propagation, message passing, factor graph, LDPC, chain complex, boundary operator, mutual information, transfer entropy, information geometry, hodge, sheaf, morse, anyon, chern, berry phase, population code, place field, co-activation, functional connectivity, free energy principle, active inference, predictive coding, quantum state tomography, distributional reinforcement learning.

**Duplicates avoided** (already captured in previous passes):
- QEC: Oreshkov CTQEC (1311.2485), de la Fuente (2604.02033), Pati-Sanders (quant-ph/0503138), Tarnowski Chern (2309.07364), Garbaczewski entropy (quant-ph/0408192)
- Neuroscience: Fasoli cortex attractors, Simpson brain networks, Tort PAC, Tsuda chaotic itinerancy, Gardner grid cells, Giusti clique topology, Xi TE+directed PH
- Cross-listed from second_pass.md: Mezard-Mora (already in info theory + neuro cross-list), Wibral PID, Chwilka MI, Zhou Granger, Venkatesh info flows, Tax PID-RBM

---

## TP-01 -- IPWT: Integrated Predictive Workspace Theory
**"Integrated Predictive Workspace Theory"**
Source: link-forge (local PDF: ipwt.pdf)
**Domain(s)**: Neuroscience (consciousness science), information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The paper's central theoretical move is replacing IIT's physical causal indivisibility with "logical irreducibility of information integration" based on synergistic information. Synergy IS joint-vs-marginal excess: information present in the joint distribution of neural subsystems that is absent from any marginal. The IPWT criterion for consciousness is precisely that the whole-system information exceeds the sum of subsystem information -- the binding residual.
- **Parameterized homology**: IPWT fuses three theories (Predictive Coding, Workspace Theory, IIT) into a single framework. Each theory contributes a different structural component, and the unification reveals invariants that persist across the three formulations. The predictive coding dynamics provide the time parameter; as prediction error evolves, the workspace state changes, and the integrated information (Phi-like quantity) is tracked as a function of this parameter.
- **Null hypothesis**: The decomposition into predictive coding (dynamics) + workspace (architecture) + IIT (phenomenology) implicitly defines nulls: removing any component collapses the framework. A non-workspace system (no global broadcast) has no consciousness; a non-predictive system (no error correction) has no dynamics; a non-integrated system (zero synergy) is reducible.
- **Stability**: The paper aims to explain clinical conditions (schizophrenia, DID) as perturbations to the IPWT framework. This is a stability question: how much can you perturb the integration/prediction/workspace balance before consciousness qualitatively changes? The framework predicts that pathology corresponds to specific parameter regimes, not random breakdown.

**What is genuinely new**: The conceptual unification itself. IIT, PCT, and Global Workspace Theory are typically presented as competing theories of consciousness. IPWT shows they address different structural levels (phenomenology, dynamics, architecture) and can be composed. The replacement of IIT's controversial "physical indivisibility" with computationally tractable synergistic information is the key technical innovation.

**Connections the authors acknowledge**: Tononi IIT, Friston predictive coding, Baars/Dehaene workspace theory. Cite PID/synergy literature. No connections to TDA, QEC, or dynamical systems formalism.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Synergistic information | Joint-vs-marginal excess (binding residual) |
| Logical irreducibility | Non-decomposability of topological invariant |
| Global workspace broadcast | Matching (assignment of content to broadcast channel) |
| Prediction error | Boundary operator image (mismatch = non-trivial boundary) |
| Predictive coding dynamics | Parameterized evolution (time as filtration parameter) |
| Schizophrenia / DID | Instability under specific perturbation regimes |
| Substrate independence | Functoriality (structure preserved across categories) |

**Cross-domain awareness**: None to TDA or QEC. Stays within neuroscience/consciousness.

---

## TP-02 -- Neurophenomenology via Free Energy
**"A Mathematical Perspective on Neurophenomenology"**
arXiv: 2409.20318
**Domain(s)**: Neuroscience, dynamical systems (active inference)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The paper formalizes the "explanatory gap" between first-person experience (phenomenology) and third-person measurement (neuroscience) as a correspondence between two probabilistic descriptions. The first-person beliefs and third-person neural measurements are two marginals; the neurophenomenological correspondence is the joint structure that relates them. The free energy functional measures the divergence between these descriptions.
- **Parameterized homology**: Active inference provides a continuous-time parameter (the agent's action-perception loop). As this parameter evolves, the agent's beliefs and the neural state co-evolve. The free energy tracks the quality of the correspondence at each time step -- it is the tracked invariant parameterized by time.
- **Stability**: The free energy principle itself is a stability statement: systems that persist are those that minimize surprise (free energy). The mathematical formulation shows that the phenomenological-neural correspondence is stable precisely when the system is at a free energy minimum -- perturbations that increase free energy are corrected by the active inference dynamics.
- **Null hypothesis**: The null is the case where first-person and third-person descriptions are independent (no neurophenomenological correspondence). The free energy divergence between the two descriptions quantifies the gap; when it is zero, the two descriptions are in perfect correspondence.

**What is genuinely new**: The mathematical formalization of neurophenomenology -- turning Varela's philosophical program into measure-theoretic language. The use of active inference as the bridge formalism between subjective and objective descriptions of brain states.

**Connections the authors acknowledge**: Varela neurophenomenology, Friston free energy principle, active inference. No connections to TDA, QEC, or error correction.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| First-person beliefs | One marginal description |
| Third-person neural measurements | Other marginal description |
| Neurophenomenological correspondence | Joint structure (excess over marginals) |
| Free energy | Divergence measure (tracks quality of correspondence) |
| Active inference loop | Parameterized dynamics (time evolution) |
| Surprise minimization | Stability mechanism |
| Explanatory gap | Joint-vs-marginal excess yet to be accounted for |

**Cross-domain awareness**: Bridges neuroscience and philosophy of mind via mathematics. No awareness of parallels to TDA or QEC.

---

## TP-03 -- Dabney et al. (2020) Distributional Code for Value
**"A distributional code for value in dopamine-based reinforcement learning"**
Nature (2020) | PMC: 7476215
**Domain(s)**: Neuroscience (computational), information theory

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The landmark finding is that individual dopamine neurons encode not the mean reward prediction error (which is the marginal/expected value) but different quantiles of the full reward distribution. The population jointly encodes the entire distribution; no single neuron's marginal contains it. The full distributional code is strictly richer than the mean code -- this is joint-vs-marginal excess in the neural population.
- **Parameterized homology**: The quantile parameter tau indexes the family of dopamine neurons. Each neuron has a different "reversal point" (the value at which its response changes sign from positive to negative RPE). As tau varies from 0 to 1, the entire distribution is traced out. This is a parameterized family whose aggregate (the distribution) is the invariant being tracked.
- **Null hypothesis**: The classical Schultz model (all dopamine neurons encode the same mean RPE) is the explicit null. The distributional hypothesis predicts asymmetric response functions and neuron-specific reversal points; the mean hypothesis predicts symmetric responses and uniform reversal points. The data decisively rejects the null.
- **Stability**: The distributional code is more robust than the mean code: it preserves information about rare events (tail risk) that the mean discards. This is a stability property -- the representation is more informative under perturbation (unusual rewards) because it retains the full shape, not just the first moment.

**What is genuinely new**: Empirical demonstration that biological neural systems implement distributional RL, not just expected-value RL. The quantile-indexed family of neurons is a biological parameterized decomposition of a probability distribution. This was theoretically predicted by Bellemare et al. (2017) in the AI/RL community but the neural implementation was unknown.

**Connections the authors acknowledge**: Bellemare et al. (2017) C51, Schultz (1997) dopamine RPE, Bayer & Glimcher (2005) heterogeneous dopamine. Bridge between computational RL theory and experimental neuroscience. No connections to TDA, QEC, or topology.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Quantile index tau | Parameter in parameterized family |
| Reversal point | Critical value (birth/death in persistence analogy) |
| Full distribution | Joint invariant (population-level) |
| Mean RPE | Marginal summary (information-lossy projection) |
| Asymmetric response function | Non-trivial structure at specific parameter value |
| Schultz mean-RPE model | Null hypothesis |
| Distributional code | Parameterized decomposition of joint structure |

**Cross-domain awareness**: Bridges computational neuroscience and AI/RL theory. No awareness of topological or error-correction parallels.

---

## TP-04 -- Opponent Striatal Circuit for Distributional RL
**"An opponent striatal circuit for distributional reinforcement learning"**
bioRxiv: 2024.01.02.573966
**Domain(s)**: Neuroscience (experimental), computational neuroscience

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Extends Dabney et al. by showing D1 and D2 striatal neurons encode OPPOSITE tails of the reward distribution. D1 neurons encode the upper tail (optimistic quantiles); D2 neurons encode the lower tail (pessimistic quantiles). Neither population alone captures the distribution; the full distributional representation requires the joint opponent encoding. This is a refined joint-vs-marginal story: the two marginals (D1 alone, D2 alone) each miss half the distribution.
- **Matching**: The opponent D1/D2 pairing is a matching problem: each D1 neuron encoding quantile tau is implicitly paired with a D2 neuron encoding quantile 1-tau. The biological circuit implements a matching between optimistic and pessimistic representations.
- **Chain complex (weak)**: The pathway dopamine -> D1/D2 -> downstream decision is a graded sequence. The D1/D2 layer decomposes the dopamine signal into complementary (opponent) components. While not a chain complex in the strict algebraic sense, the opponent decomposition (positive tail + negative tail = full distribution) has the flavor of a direct sum decomposition.
- **Null hypothesis**: The non-opponent null (D1 and D2 encode the same information, just with opposite signs) is tested and rejected. The opponent encoding is genuinely asymmetric: D1 and D2 carry different quantile ranges, not just sign-flipped copies of the same signal.

**What is genuinely new**: The biological mechanism implementing the distributional code. Optogenetic manipulation of D1 vs D2 pathways selectively disrupts optimistic vs pessimistic evaluation, providing causal evidence for the opponent architecture. This extends Dabney et al. from correlation to mechanism.

**Connections the authors acknowledge**: Dabney et al. (2020), Bellemare et al. (2017), D1/D2 pathway literature. No connections outside neuroscience/RL.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| D1 neurons (optimistic quantiles) | One component of matched pair |
| D2 neurons (pessimistic quantiles) | Complementary component |
| Opponent encoding | Direct sum decomposition (positive + negative = whole) |
| Optogenetic manipulation | Targeted perturbation of one chain level |
| Full reward distribution | Joint invariant requiring both components |

**Cross-domain awareness**: None to TDA or QEC.

---

## TP-05 -- Arovas & Zhang (1992) Topological Aspects of FQHE
**"Topological aspects of quantum Hall physics"**
Local PDF: arovas-Zhang1992A.pdf
**Domain(s)**: Quantum error correction (topological order), condensed matter physics

**Abstract machines instantiated**:
- **Chain complex**: The fractional quantum Hall effect is the original physical system where topological order was identified. The effective field theory is a Chern-Simons gauge theory, whose observables (Wilson loops, braiding phases) are computed from the homology of the underlying surface. The ground state degeneracy on a genus-g surface is dim(H_1(Sigma_g, Z/n)) -- directly a chain complex computation.
- **Parameterized homology**: The filling fraction nu = p/q parametrizes the family of FQHE states. At each rational filling, a different topological phase appears with different anyonic excitations. The phase diagram maps nu to the topological order (number of ground states, braiding statistics). This is parameterized homology: the invariant (topological order type) changes as the parameter (filling fraction) varies.
- **Stability**: Topological order is robust: small perturbations to the Hamiltonian cannot change the ground state degeneracy or braiding statistics, because these are topological invariants. The energy gap protects the topological phase -- perturbations smaller than the gap leave the invariants unchanged. This is the strongest form of stability: topological protection.
- **Null hypothesis**: The null is the integer quantum Hall effect (nu = integer), which has trivial topological order (no anyons, no ground state degeneracy on higher-genus surfaces). The fractional states represent genuinely new topological structure beyond the integer case.
- **Matching (weak)**: Anyonic excitations come in particle-antiparticle pairs that can be created from the vacuum and must annihilate in pairs. The fusion rules define a matching constraint: which pairs of anyons can annihilate to the vacuum.

**What is genuinely new**: The original connection between condensed matter physics and topological quantum field theory. The Arovas-Zhang paper was instrumental in establishing that fractional quantum Hall states have the same mathematical structure as Chern-Simons theory -- the bridge that eventually led to topological quantum computation proposals.

**Connections the authors acknowledge**: Laughlin wavefunctions, Witten Chern-Simons theory, braid group. Bridges condensed matter and mathematical physics. The connection to quantum error correction (toric code etc.) was not yet established in 1992 -- that came later via Kitaev (1997/2003).

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Filling fraction nu | Filtration parameter |
| Topological order | Non-trivial homology (ground state degeneracy = Betti number) |
| Energy gap | Stability threshold (perturbations below gap preserve topology) |
| Anyonic excitation | Non-trivial homology class (cycle that cannot be shrunk) |
| Braiding statistics | Pairing structure on homology classes |
| Chern-Simons theory | Chain complex formalism (gauge theory on manifold) |
| Integer QHE | Null/trivial topology |
| Genus-g surface | Base space of the chain complex |
| Wilson loop | Cycle evaluation (homological observable) |

**Cross-domain awareness**: Bridges condensed matter and TQFT. Does not connect to TDA or neuroscience (predates both fields).

---

## TP-06 -- Barandes (2023) Stochastic-Quantum Theorem
**"Generalized Stochastic Systems and the Stochastic-Quantum Correspondence"**
arXiv: 2309.03085
**Domain(s)**: Quantum foundations, dynamical systems

**Abstract machines instantiated**:
- **Chain complex**: The stochastic-quantum correspondence establishes a functorial mapping between generalized stochastic systems (Markov chains with interference) and unitarily evolving quantum systems. The Hilbert space structure, complex amplitudes, and Born rule all arise from this correspondence. The mapping preserves the compositional structure: tensor products of stochastic systems map to tensor products of quantum systems. This is a chain-complex-level equivalence between two apparently different algebraic structures.
- **Stability**: The correspondence is exact, not approximate. Any generalized stochastic system has a unique quantum counterpart and vice versa. The mapping is stable under composition: combining systems preserves the correspondence. This is the strongest possible stability -- an isomorphism, not a bound.
- **Parameterized homology**: The paper derives why quantum mechanics uses specific mathematical structures (complex numbers, Hilbert spaces, unitary evolution, Born rule) from first principles. Each structure emerges at a specific stage of the correspondence, forming a graded sequence: stochastic process -> interference structure -> complex amplitudes -> Hilbert space -> unitarity -> Born rule.
- **Joint-vs-marginal excess**: The interference terms in generalized stochastic systems are precisely the joint-vs-marginal excess: they are present in the joint evolution of the system but absent from any classical (non-interfering) marginal. Quantum coherence IS joint-vs-marginal excess under this correspondence.

**What is genuinely new**: A new formulation of quantum mechanics as a theorem about stochastic processes. Unlike the many existing formulations (Hilbert space, path integral, algebraic, categorical), this one derives quantum structure from purely stochastic axioms with no quantum postulates. The correspondence also suggests quantum computers can simulate any generalized stochastic process.

**Connections the authors acknowledge**: Cites quantum foundations literature (Dirac, Feynman, Hardy). Does NOT connect to TDA, error correction, or neuroscience -- but the functorial structure is crying out for categorical treatment.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Generalized stochastic system | Classical chain complex (probabilistic) |
| Unitarily evolving quantum system | Quantum chain complex (amplitude-based) |
| Stochastic-quantum correspondence | Functor between categories |
| Interference terms | Joint-vs-marginal excess (coherence) |
| Born rule | Projection from joint (amplitude) to marginal (probability) |
| Complex amplitudes | Algebraic enrichment enabling interference |
| Tensor product | Composition of chain complexes |

**Cross-domain awareness**: Bridges quantum foundations and probability theory. Does not acknowledge parallels to TDA or neuroscience.

---

## TP-07 -- Reconstructing Quantum States with Generative Models
**"Reconstructing quantum states with generative models"**
arXiv: 1810.10584
**Domain(s)**: Quantum error correction (state tomography), machine learning

**Abstract machines instantiated**:
- **Matching**: Quantum state tomography is fundamentally a matching problem: given measurement outcomes (observables), reconstruct the density matrix (state) that produced them. The generative model learns a mapping from latent variables to measurement probabilities, and the training matches model-generated statistics to empirical statistics. The informationally complete measurement basis provides the matching constraint: enough observables to uniquely determine the state.
- **Parameterized homology**: The latent space of the generative model is parameterized. As training progresses, the model traces a path through parameter space. The reconstructed density matrix (the invariant) changes along this path, converging to the true state. The final model is a compressed representation of the quantum state.
- **Joint-vs-marginal excess**: A density matrix encodes all correlations between subsystems -- including entanglement, which is joint structure absent from the reduced (marginal) density matrices. The tomographic reconstruction must capture this joint structure. The generative model must learn to represent entanglement, not just marginal statistics.
- **Null hypothesis**: The separable (unentangled) state serves as the implicit null. Deviations from separability in the reconstructed state indicate genuine quantum correlations. The model's ability to represent entangled states is what distinguishes it from a product-state approximation.

**What is genuinely new**: Reducing quantum state tomography to unsupervised learning. The generative model approach scales better than direct density matrix reconstruction for large systems because it exploits structure (low-rank, area-law entanglement) automatically. The connection between ML generative models and quantum state representation.

**Connections the authors acknowledge**: Quantum state tomography literature, RBMs, variational methods. Bridges ML and quantum information. No connections to TDA or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Density matrix | Joint state (full description) |
| Reduced density matrix | Marginal (subsystem description) |
| Entanglement | Joint-vs-marginal excess (quantum correlations) |
| Informationally complete basis | Sufficient measurement set (matching constraints) |
| Generative model latent space | Compressed chain complex |
| Tomographic reconstruction | Inverse matching problem (data -> state) |

**Cross-domain awareness**: Bridges ML and quantum information. No TDA or neuroscience awareness.

---

## TP-08 -- Hodge-Aware Contrastive Learning on Simplicial Complexes
**"Hodge-Aware Contrastive Learning"**
Local PDF
**Domain(s)**: TDA (applied), machine learning -- relevant to neuroscience via simplicial structure

**Abstract machines instantiated**:
- **Chain complex**: The paper works directly with simplicial complexes and their Hodge Laplacians. The Hodge decomposition L_k = B_k^T B_k + B_{k+1} B_{k+1}^T decomposes k-chain space into gradient, curl, and harmonic components. This is the explicit chain complex B_{k+1} -> C_k -> C_{k-1} with the Hodge Laplacian as the structure operator.
- **Parameterized homology (weak)**: The contrastive learning augmentations are designed to preserve the Hodge spectral properties. The augmentation parameter controls how much the simplicial complex is perturbed. Spectral preservation means the topological invariants (harmonic component = homology) are maintained across augmentations.
- **Stability**: The spectral-preserving augmentation strategy is explicitly a stability mechanism: the learned embeddings are stable under topology-preserving perturbations of the input complex. The reweighting of negative samples in the InfoNCE loss further enforces stability by penalizing representations that change under Hodge-spectral-preserving deformations.
- **Joint-vs-marginal excess**: The Hodge decomposition reveals three types of signal flow: gradient (potential-driven), curl (rotational), and harmonic (topological). The gradient and curl components are "local" (reducible to vertex/face information); the harmonic component is "global" (irreducible to lower-dimensional data). The harmonic component IS the joint-vs-marginal excess in this setting.

**What is genuinely new**: The Hodge decomposition as a principled foundation for contrastive learning on simplicial complexes. Previous graph contrastive learning methods (GraphCL, GCA) work only on graphs (1-skeleton) and miss higher-order structure. The Hodge-aware approach respects the full chain complex structure.

**Connections the authors acknowledge**: Hodge theory, simplicial neural networks (Ebli et al., 2020), graph contrastive learning. Aware of the TDA connection but focused on the ML application. The paper does not connect to neuroscience, but Giusti et al. (2015) showed that neural correlation networks have rich simplicial structure -- Hodge-aware methods could analyze this structure directly.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Hodge Laplacian L_k | Chain complex structure operator |
| Gradient component | Boundary image (im B_k^T) |
| Curl component | Coboundary image (im B_{k+1}) |
| Harmonic component | Homology (ker L_k = ker B_k cap ker B_{k+1}^T) |
| Spectral-preserving augmentation | Topology-preserving perturbation |
| InfoNCE with Hodge reweighting | Stability-aware objective |
| Simplicial complex | Input chain complex |

**Cross-domain awareness**: Aware of TDA foundations. Potential bridge to neuroscience (via Giusti-type simplicial neural analysis) not acknowledged.

---

## TP-09 -- ConformalHDC: Hippocampal Neural Decoding
**"ConformalHDC: Uncertainty-Aware Hyperdimensional Computing with Application to Neural Decoding"**
arXiv: 2602.21446
**Domain(s)**: Neuroscience (neural decoding), machine learning (conformal prediction)

**Abstract machines instantiated**:
- **Null hypothesis**: Conformal prediction provides distribution-free coverage guarantees: the prediction set contains the true label with probability >= 1 - alpha, regardless of the data distribution. This is a null-hypothesis framework: the non-conformity score measures how "surprising" a new observation is relative to a calibration set. High non-conformity = outlier relative to the null (calibration distribution).
- **Stability**: The conformal guarantee is a stability result: the prediction set size adjusts adaptively to maintain coverage even under distribution shift. When the decoder is uncertain (high non-conformity), the prediction set grows; when confident, it shrinks. The guarantee holds for ANY underlying distribution, making it distribution-free stable.
- **Matching**: The hyperdimensional computing (HDC) encoder maps neural spike trains to high-dimensional binary vectors, and classification is done by nearest-centroid matching in HD space. The encoding-then-matching pipeline is structurally parallel to feature extraction + assignment in persistence.
- **Joint-vs-marginal excess (weak)**: The hippocampal neural population code for spatial position is inherently a population-level (joint) representation. Individual neuron firing rates (marginals) are ambiguous; the joint population vector determines position.

**What is genuinely new**: The combination of conformal prediction (statistical guarantees) with hyperdimensional computing (neuromorphic efficiency) for neural decoding. The application to hippocampal place cell decoding connects to the Gardner et al. toroidal manifold result: ConformalHDC is decoding FROM the manifold that Gardner showed IS a torus.

**Connections the authors acknowledge**: Conformal prediction (Vovk), HDC (Kanerva), neural decoding literature. No explicit connection to TDA or QEC, but the hippocampal population code IS the same object studied by Gardner et al.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Non-conformity score | Null-hypothesis test statistic |
| Coverage guarantee 1-alpha | Stability bound (confidence level) |
| Prediction set | Uncertainty region (larger = less stable) |
| HD binary vector | Compressed representation (chain-level encoding) |
| Nearest-centroid matching | Matching / assignment in feature space |
| Hippocampal population code | Joint neural manifold (torus per Gardner) |

**Cross-domain awareness**: None to TDA or QEC. The connection to Gardner's toroidal topology is implicit but unacknowledged.

---

## TP-10 -- Rigorous Born Approximation for the Spin-Boson Model
**"Rigorous Born Approximation and beyond for the Spin-Boson Model"**
Local PDF
**Domain(s)**: Quantum error correction (open quantum systems), dynamical systems

**Abstract machines instantiated**:
- **Parameterized homology**: The spin-boson coupling strength alpha is the parameter. As alpha varies, the system transitions between regimes: weak coupling (perturbative, coherent oscillations persist), strong coupling (localization, coherence destroyed). The "prompt loss of coherence" scaling as sqrt(alpha) is a non-analytic feature that appears even at weak coupling -- a parametric singularity.
- **Stability**: The calculation reveals non-Markovian effects that are invisible to standard Markovian approximations. The prompt coherence loss (scaling sqrt(alpha) rather than alpha) shows that the system is LESS stable than Markovian analysis suggests: a square-root singularity means even infinitesimal coupling produces a finite coherence loss. This is an anti-stability result -- the standard stability estimate (linear in alpha) is wrong.
- **Null hypothesis**: The Markovian (memoryless) approximation is the null model. The Born approximation reveals non-Markovian corrections: memory effects where the bath's past states influence its future action on the spin. The gap between Markovian and non-Markovian dynamics quantifies the information stored in the bath about the system's history.
- **Joint-vs-marginal excess**: The spin and bath are entangled during evolution. The reduced spin dynamics (marginal) lose information about this entanglement. The non-Markovian corrections are precisely the joint (spin-bath) structure that is invisible in the marginal (spin-only) dynamics. The Born approximation partially captures this joint structure.

**What is genuinely new**: The exact analytical calculation within the Born approximation for the ohmic spin-boson model. The discovery of the sqrt(alpha) prompt coherence loss -- a non-perturbative effect visible within a perturbative framework. This challenges the standard assumption that weak coupling implies weak decoherence.

**Connections the authors acknowledge**: Leggett et al. spin-boson model, decoherence literature, quantum Brownian motion. Situated in open quantum systems. No connections to TDA or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Coupling strength alpha | Filtration/perturbation parameter |
| Coherence | Preserved topological structure (quantum phase information) |
| Prompt coherence loss | Parametric singularity (sqrt scaling) |
| Markovian approximation | Null model (memoryless) |
| Non-Markovian corrections | Joint-vs-marginal excess (bath memory effects) |
| Localization transition | Phase transition (topology change) |
| Born approximation | Finite-order chain complex truncation |

**Cross-domain awareness**: None to TDA or neuroscience. Relevant to QEC because decoherence analysis determines error correction requirements.

---

## TP-11 -- Summary Statistics Link Neural Representations to Behavior
**"Summary statistics of learning link changing neural representations to behavior"**
arXiv: 2504.16920
**Domain(s)**: Neuroscience (computational), dynamical systems, information theory

**Abstract machines instantiated**:
- **Parameterized homology**: The central thesis is that summary statistics from statistical physics (order parameters, susceptibilities, correlation functions) can track how neural representations change during learning. As training progresses (the parameter), the representation quality (the tracked statistic) evolves. The paper reviews multiple such statistics: representational similarity, neural dimensionality, alignment measures.
- **Joint-vs-marginal excess**: The paper discusses how neural population-level statistics (joint) capture learning dynamics that single-neuron statistics (marginals) miss. Representational similarity analysis (RSA) explicitly compares the joint distance structure across conditions to individual neuron tuning curves.
- **Null hypothesis**: Shuffled/random representations serve as null baselines. The gap between the learned representation's summary statistics and the null's statistics quantifies the information content of learning.
- **Stability**: The paper addresses whether summary statistics are stable across individuals, species, and artificial networks. The claim is that certain statistics (e.g., dimensionality, alignment) are conserved across these variations -- they are stable invariants of the learning process.

**What is genuinely new**: The meta-perspective: reviewing which summary statistics successfully bridge the gap between neural representation changes and behavioral changes, for both biological and artificial networks. The statistical physics lens (order parameters for neural learning) is the framing innovation.

**Connections the authors acknowledge**: Statistical physics, neuroscience (representational similarity analysis), machine learning (loss landscape analysis). Aware of cross-domain parallels between biological and artificial networks. No connection to TDA or QEC.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Summary statistic / order parameter | Topological invariant (tracked quantity) |
| Training epoch / learning | Parameterization variable |
| Representational similarity | Joint distance structure (correlation matrix) |
| Neural dimensionality | Rank of the chain complex (effective degrees of freedom) |
| Cross-individual conservation | Stability (invariant preserved across instances) |
| Shuffled baseline | Null hypothesis (structure-free reference) |

**Cross-domain awareness**: Bridges neuroscience and statistical physics. Aware of parallels between biological and artificial networks. No awareness of TDA or QEC parallels.

---

## TP-12 -- Mezard & Mora (2009) CSP, Neural Networks, and LDPC
**"Constraint satisfaction problems and neural networks: a statistical physics perspective"**
Local PDF
**Domain(s)**: Information theory, neuroscience, quantum error correction (LDPC decoding)

**NOTE**: This paper was already cross-listed in neuroscience.md and information_theory.md. This annotation captures the QEC-relevant aspects not previously emphasized.

**QEC-relevant abstract machines**:
- **Chain complex**: The factor graph for LDPC decoding IS a chain complex. Variable nodes are 0-cells, check nodes are 1-cells, and the parity-check matrix H defines the boundary operator. The code space ker(H) is exactly the cycle space. Mezard-Mora treat LDPC decoding as a constraint satisfaction problem solvable by belief propagation on this factor graph -- the same message-passing that applies to neural inference and random k-SAT.
- **Matching**: Belief propagation on factor graphs is a soft matching algorithm: it iteratively assigns probability distributions to variables subject to check constraints. In LDPC decoding, this is equivalent to finding the most likely error pattern matching the syndrome -- a probabilistic version of the minimum-weight matching used in toric code decoders.
- **Stability**: The paper identifies phase transitions in the solvability of constraint satisfaction problems. Below a critical constraint density, BP converges to the correct solution (decodable); above it, the problem becomes unsolvable (uncorrectable errors). The phase transition threshold is the analogue of the error correction threshold in QEC.

**What this adds to the QEC picture**: The unification of LDPC decoding, neural inference, and k-SAT under a single graphical model + message passing framework. The phase transitions in CSPs map directly to error correction thresholds. This paper is a bridge between the statistical physics / coding theory / neuroscience communities that has not been exploited in the topo-rosetta context.

**Vocabulary mapping (QEC emphasis)**:
| Paper term | Rosetta term |
|---|---|
| Factor graph | Chain complex (bipartite graph = boundary operator) |
| Parity check H | Boundary map |
| Variable node | 0-cell |
| Check node | 1-cell |
| Codeword | Cycle (element of ker H) |
| Belief propagation | Soft matching on chain complex |
| Phase transition in CSP | Error correction threshold |
| Survey propagation | Higher-order message passing (exploits metastable states) |

**Cross-domain awareness**: Explicitly bridges coding theory, statistical physics, and neuroscience. Does NOT use topological language but the structures are homological.

---

## Summary of Third Pass Finds

### Neuroscience (new, not previously captured):
| ID | Paper | Key machines | Novelty |
|---|---|---|---|
| TP-01 | IPWT (consciousness) | joint-vs-marginal, parameterized, null, stability | Synergistic info replaces IIT's physical indivisibility |
| TP-02 | Neurophenomenology (2409.20318) | joint-vs-marginal, parameterized, stability, null | Mathematical formalization of explanatory gap via free energy |
| TP-03 | Dabney distributional code | joint-vs-marginal, parameterized, null, stability | Biological distributional RL -- quantile-indexed neuron family |
| TP-04 | Opponent striatal circuit | joint-vs-marginal, matching, chain (weak), null | D1/D2 opponent encoding of reward distribution tails |
| TP-09 | ConformalHDC | null, stability, matching, joint-vs-marginal (weak) | Conformal prediction for hippocampal decoding -- connects to Gardner torus |
| TP-11 | Summary statistics review | parameterized, joint-vs-marginal, null, stability | Meta-review of invariants bridging neural learning and behavior |

### QEC (new, not previously captured):
| ID | Paper | Key machines | Novelty |
|---|---|---|---|
| TP-05 | Arovas-Zhang FQHE (1992) | chain complex, parameterized, stability, null, matching (weak) | Original FQHE-TQFT connection; filling fraction as filtration |
| TP-06 | Barandes stochastic-quantum (2309.03085) | chain complex, stability, parameterized, joint-vs-marginal | Quantum mechanics derived from stochastic axioms; interference = joint excess |
| TP-07 | Quantum state tomography (1810.10584) | matching, parameterized, joint-vs-marginal, null | Tomography as unsupervised learning; entanglement = joint excess |
| TP-10 | Spin-boson Born (open quantum) | parameterized, stability (anti), null, joint-vs-marginal | sqrt(alpha) prompt coherence loss; non-Markovian = bath memory |

### Cross-domain / Multi-domain:
| ID | Paper | Domains | Key insight |
|---|---|---|---|
| TP-08 | Hodge-aware contrastive learning | TDA + (potential neuroscience) | Chain complex structure preserved in learned embeddings; bridge to Giusti neural simplicial |
| TP-12 | Mezard-Mora (QEC emphasis) | Info theory + neuroscience + QEC | Factor graph = chain complex; BP on LDPC = soft matching; CSP threshold = error threshold |
