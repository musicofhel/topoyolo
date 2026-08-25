# Queue batch-004 — arXiv foraging export, 2026-08-25

First FORAGED batch (link-forge corpus exhausted for gap topics — Aaron authorized
fresh acquisition). Source: arXiv API search, orchestrator-side. **Provenance:
abstract-only** — content extracts below are the arXiv abstracts, not full text;
annotate from the abstract's stated machinery and flag depth-limited entries in
the report. Targets: Dynamics×Matching (finally — genuine Takens/OT bridge
papers exist), stochastic-thermodynamics×OT, rate-distortion (Blahut–Arimoto
feed), LDPC/belief-propagation×phase-transitions.
Consume per papers/INGESTION.md (≤3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [dyn-matching] — ANNOTATED as 2409.08768 (B2 pass 24 → annotations/2409.08768.md)

**Title:** Measure-Theoretic Time-Delay Embedding

**URL:** https://arxiv.org/abs/2409.08768

**Description:** Botvinick-Greenhouse, Oprea, Maulik, Yang (2024). math.DS/cs.LG. Generalizes Takens' embedding theorem measure-theoretically using optimal transport — the delay embedding becomes a pushforward map between spaces of probability measures.

**Content extract (abstract):**

```
The celebrated Takens' embedding theorem provides a theoretical foundation for reconstructing the full state of a dynamical system from partial observations. However, the classical theorem assumes that the underlying system is deterministic and that observations are noise-free, limiting its applicability in real-world scenarios. Motivated by these limitations, we formulate a measure-theoretic generalization that adopts an Eulerian description of the dynamics and recasts the embedding as a pushforward map between spaces of probability measures. Our mathematical results leverage recent advances in optimal transport. Building on the proposed measure-theoretic time-delay embedding theory, we develop a computational procedure that aims to reconstruct the full state of a dynamical system from time-lagged partial observations, engineered with robustness to handle sparse and noisy data. We evaluate our measure-based approach across several numerical examples, ranging from the classic Lorenz-63 system to real-world applications such as NOAA sea surface temperature reconstruction and ERA5 wind field reconstruction.
```

## candidate-02 [dyn-matching] — ANNOTATED as 1907.08260 (B2 pass 24 → annotations/1907.08260.md)

**Title:** A geometric approach to the transport of discontinuous densities

**URL:** https://arxiv.org/abs/1907.08260

**Description:** Moosmüller, Dietrich, Kevrekidis (2019). physics.data-an. Uses attractor-reconstruction ideas (short observation histories) to disambiguate optimal transport maps when source-target densities are non-bijective.

**Content extract (abstract):**

```
Different observations of a relation between inputs ("sources") and outputs ("targets") are often reported in terms of histograms (discretizations of the source and the target densities). Transporting these densities to each other provides insight regarding the underlying relation. In (forward) uncertainty quantification, one typically studies how the distribution of inputs to a system affects the distribution of the system responses. Here, we focus on the identification of the system (the transport map) itself, once the input and output distributions are determined, and suggest a modification of current practice by including data from what we call "an observation process". We hypothesize that there exists a smooth manifold underlying the relation; the sources and the targets are then partial observations (possibly projections) of this manifold. Knowledge of such a manifold implies knowledge of the relation, and thus of "the right" transport between source and target observations. When the source-target observations are not bijective (when the manifold is not the graph of a function over both observation spaces, either because folds over them give rise to density singularities, or because it marginalizes over several observables), recovery of the manifold is obscured. Using ideas from attractor reconstruction in dynamical systems, we demonstrate how additional information in the form of short histories of an observation process can help us recover the underlying manifold. The types of additional information employed and the relation to optimal transport based solely on density observations is illustrated and discussed, along with limitations in the recovery of the true underlying relation.
```

## candidate-03 [dyn-matching] — REJECTED
REJECT (one sentence): single-machine dynamic-OT application wrapper (CNF↔dynamic-OT link in service of scRNA-seq trajectory interpolation) — same class as the GWGAN rejection in pass 17, and superseded within this very batch by candidate-04 MIOFlow.

**Title:** TrajectoryNet: A Dynamic Optimal Transport Network for Modeling Cellular Dynamics

**URL:** https://arxiv.org/abs/2002.04461

**Description:** Tong, Huang, Wolf, van Dijk, Krishnaswamy (2020). stat.ML. Links continuous normalizing flows to dynamic optimal transport to model trajectories between static cross-sectional snapshots (scRNA-seq).

**Content extract (abstract):**

```
It is increasingly common to encounter data from dynamic processes captured by static cross-sectional measurements over time, particularly in biomedical settings. Recent attempts to model individual trajectories from this data use optimal transport to create pairwise matchings between time points. However, these methods cannot model continuous dynamics and non-linear paths that entities can take in these systems. To address this issue, we establish a link between continuous normalizing flows and dynamic optimal transport, that allows us to model the expected paths of points over time. Continuous normalizing flows are generally under constrained, as they are allowed to take an arbitrary path from the source to the target distribution. We present TrajectoryNet, which controls the continuous paths taken between distributions to produce dynamic optimal transport. We show how this is particularly applicable for studying cellular dynamics in data from single-cell RNA sequencing (scRNA-seq) technologies, and that TrajectoryNet improves upon recently proposed static optimal transport-based models that can be used for interpolating cellular distributions.
```

## candidate-04 [dyn-matching] — ANNOTATED as 2206.14928 (B2 pass 25 → annotations/2206.14928.md)

**Title:** Manifold Interpolating Optimal-Transport Flows for Trajectory Inference

**URL:** https://arxiv.org/abs/2206.14928

**Description:** Huguet, Magruder, Tong, Fasina, Kuchroo, Wolf, Krishnaswamy (2022). cs.LG. MIOFlow: neural ODE dynamics + manifold geodesic distance + OT penalty for population trajectory inference between snapshots.

**Content extract (abstract):**

```
We present a method called Manifold Interpolating Optimal-Transport Flow (MIOFlow) that learns stochastic, continuous population dynamics from static snapshot samples taken at sporadic timepoints. MIOFlow combines dynamic models, manifold learning, and optimal transport by training neural ordinary differential equations (Neural ODE) to interpolate between static population snapshots as penalized by optimal transport with manifold ground distance. Further, we ensure that the flow follows the geometry by operating in the latent space of an autoencoder that we call a geodesic autoencoder (GAE). In GAE the latent space distance between points is regularized to match a novel multiscale geodesic distance on the data manifold that we define. We show that this method is superior to normalizing flows, Schrödinger bridges and other generative models that are designed to flow from noise to data in terms of interpolating between populations. Theoretically, we link these trajectories with dynamic optimal transport. We evaluate our method on simulated data with bifurcations and merges, as well as scRNA-seq data from embryoid body differentiation, and acute myeloid leukemia treatment.
```

## candidate-05 [stoch-thermo] — ANNOTATED as 2103.00503 (B2 pass 25 → annotations/2103.00503.md; new by-domain/statistical_physics.md opened)

**Title:** Geometrical aspects of entropy production in stochastic thermodynamics based on Wasserstein distance

**URL:** https://arxiv.org/abs/2103.00503

**Description:** Nakazato, Ito (2021). cond-mat.stat-mech. Entropy production lower-bounded by L2-Wasserstein path length — optimal transport as the geometry of dissipation; thermodynamic speed limits.

**Content extract (abstract):**

```
We study a relationship between optimal transport theory and stochastic thermodynamics for the Fokker-Planck equation. We show that the lower bound on the entropy production is the action measured by the path length of the L2-Wasserstein distance. Because the L2-Wasserstein distance is a geometric measure of optimal transport theory, our result implies a geometric interpretation of the entropy production. Based on this interpretation, we obtain a thermodynamic trade-off relation between transition time and the entropy production. This thermodynamic trade-off relation is regarded as a thermodynamic speed limit which gives a tighter bound of the entropy production. We also discuss stochastic thermodynamics for the subsystem and derive a lower bound on the partial entropy production as a generalization of the second law of information thermodynamics. Our formalism also provides a geometric picture of the optimal protocol to minimize the entropy production. We illustrate these results by the optimal stochastic heat engine and show a geometrical bound of the efficiency.
```

## candidate-06 [stoch-thermo] — ANNOTATED as 2209.00527 (B2 pass 26 → annotations/2209.00527.md)

**Title:** Geometric thermodynamics for the Fokker-Planck equation: Stochastic thermodynamic links between information geometry and optimal transport

**URL:** https://arxiv.org/abs/2209.00527

**Description:** Ito (2022). cond-mat.stat-mech/math-ph. Unifies information geometry and optimal transport through excess entropy production rate; trade-off relations and optimal protocols.

**Content extract (abstract):**

```
We propose a geometric theory of non-equilibrium thermodynamics, namely geometric thermodynamics, using our recent developments of differential-geometric aspects of entropy production rate in non-equilibrium thermodynamics. By revisiting our recent results on geometrical aspects of entropy production rate in stochastic thermodynamics for the Fokker-Planck equation, we introduce a geometric framework of non-equilibrium thermodynamics in terms of information geometry and optimal transport theory. We show that the proposed geometric framework is useful for obtaining several non-equilibrium thermodynamic relations, such as thermodynamic trade-off relations between the thermodynamic cost and the fluctuation of the observable, optimal protocols for the minimum thermodynamic cost and the decomposition of the entropy production rate for the non-equilibrium system. We clarify several stochastic-thermodynamic links between information geometry and optimal transport theory via the excess entropy production rate based on a relation between the gradient flow expression and information geometry in the space of probability densities and a relation between the velocity field in optimal transport and information geometry in the space of path probability densities.
```

## candidate-07 [stoch-thermo] — ANNOTATED as 1810.09545 (B2 pass 25 → annotations/1810.09545.md)

**Title:** Unified framework for the entropy production and the stochastic interaction based on information geometry

**URL:** https://arxiv.org/abs/1810.09545

**Description:** Ito, Oizumi, Amari (2018). cond-mat.stat-mech. Violation of additivity of subsystem entropy productions = stochastic interaction (integrated information theory) — a joint-vs-marginal machine in thermodynamic dress.

**Content extract (abstract):**

```
We show a relationship between the entropy production in stochastic thermodynamics and the stochastic interaction in the information integrated theory. To clarify this relationship, we newly introduce an information geometric interpretation of the entropy production for a total system and the partial entropy productions for subsystems. We show that the violation of the additivity of the entropy productions is related to the stochastic interaction. This framework is a thermodynamic foundation of the integrated information theory. We also show that our information geometric formalism leads to a novel expression of the entropy production related to an optimization problem minimizing the Kullback-Leibler divergence. We analytically illustrate this interpretation by using the spin model.
```

## candidate-08 [stoch-thermo] — ANNOTATED as 1408.1224 (B2 pass 26 → annotations/1408.1224.md)

**Title:** Stochastic thermodynamics with information reservoirs

**URL:** https://arxiv.org/abs/1408.1224

**Description:** Barato, Seifert (2014). cond-mat.stat-mech. Second law generalized to systems coupled to bit-sequence information reservoirs; fluctuation theorem for information-processing entropy production.

**Content extract (abstract):**

```
We generalize stochastic thermodynamics to include information reservoirs. Such information reservoirs, which can be modeled as a sequence of bits, modify the second law. For example, work extraction from a system in contact with a single heat bath becomes possible if the system also interacts with an information reservoir. We obtain an inequality, and the corresponding fluctuation theorem, generalizing the standard entropy production of stochastic thermodynamics. From this inequality we can derive an information processing entropy production, which gives the second law in the presence of information reservoirs. We also develop a systematic linear response theory for information processing machines. For a unicyclic machine powered by an information reservoir, the efficiency at maximum power can deviate from the standard value of 1/2. For the case where energy is consumed to erase the tape, the efficiency at maximum erasure rate is found to be 1/2.
```

## candidate-09 [stoch-thermo] — ANNOTATED as 2312.03489 (B2 pass 26 → annotations/2312.03489.md; second Neuroscience bridge)

**Title:** Decomposing Thermodynamic Dissipation of Linear Langevin Systems via Oscillatory Modes and Its Application to Neural Dynamics

**URL:** https://arxiv.org/abs/2312.03489

**Description:** Sekizawa, Ito, Oizumi (2023). q-bio.NC/cond-mat.stat-mech. Housekeeping entropy production decomposed into oscillatory-mode contributions; applied to monkey ECoG under awake vs anesthesia — a neuroscience×stoch-thermo bridge.

**Content extract (abstract):**

```
Recent developments in stochastic thermodynamics have elucidated various relations between the entropy production rate (thermodynamic dissipation) and the physical limits of information processing in nonequilibrium dynamical systems. These findings have opened new perspectives in analyzing real biological systems. In neuroscience, the importance of quantifying entropy production has attracted attention for understanding information processing in the brain. However, the relationship between the entropy production rate and oscillations, which are common in many biological systems, remains unclear. For instance, neural oscillations like delta, theta, and alpha waves play crucial roles in brain information processing. Here, we derive a novel decomposition of the entropy production rate of linear Langevin systems. We show that one component of the entropy production rate, called the housekeeping entropy production rate, can be decomposed into independent positive contributions from oscillatory modes. Our decomposition enables us to calculate the contribution of oscillatory modes to the housekeeping entropy production rate. In addition, when the noise matrix is diagonal, the contribution of each oscillatory mode can be further decomposed into the contribution of each system element. To demonstrate the utility of our decomposition, we applied it to an electrocorticography (ECoG) dataset recorded during awake and anesthetized conditions in monkeys, where the oscillatory properties change drastically. We showed consistent trends across different monkeys: the contribution of delta band was larger in the anesthetized condition than in the awake condition, while those from higher frequency bands, such as the theta band, were smaller. These results allow us to interpret the changes in neural oscillation in terms of stochastic thermodynamics and the physical limits of information processing.
```

## candidate-10 [rate-distortion] — ANNOTATED as 2204.01612 (B2 pass 27 → annotations/2204.01612.md)

**Title:** Neural Estimation of the Rate-Distortion Function With Applications to Operational Source Coding

**URL:** https://arxiv.org/abs/2204.01612

**Description:** Lei, Hassani, Saeedi Bidokhti (2022). cs.IT/cs.LG. NERD: reformulates the rate-distortion objective as neural functional optimization where Blahut–Arimoto is computationally infeasible; yields operational one-shot lossy codes.

**Content extract (abstract):**

```
A fundamental question in designing lossy data compression schemes is how well one can do in comparison with the rate-distortion function, which describes the known theoretical limits of lossy compression. Motivated by the empirical success of deep neural network (DNN) compressors on large, real-world data, we investigate methods to estimate the rate-distortion function on such data, which would allow comparison of DNN compressors with optimality. While one could use the empirical distribution of the data and apply the Blahut-Arimoto algorithm, this approach presents several computational challenges and inaccuracies when the datasets are large and high-dimensional, such as the case of modern image datasets. Instead, we re-formulate the rate-distortion objective, and solve the resulting functional optimization problem using neural networks. We apply the resulting rate-distortion estimator, called NERD, on popular image datasets, and provide evidence that NERD can accurately estimate the rate-distortion function. Using our estimate, we show that the rate-distortion achievable by DNN compressors are within several bits of the rate-distortion function for real-world datasets. Additionally, NERD provides access to the rate-distortion achieving channel, as well as samples from its output marginal. Therefore, using recent results in reverse channel coding, we describe how NERD can be used to construct an operational one-shot lossy compression scheme with guarantees on the achievable rate and distortion. Experimental results demonstrate competitive performance with DNN compressors.
```

## candidate-11 [rate-distortion] — ANNOTATED as 2104.13662 (B2 pass 27 → annotations/2104.13662.md)

**Title:** A coding theorem for the rate-distortion-perception function

**URL:** https://arxiv.org/abs/2104.13662

**Description:** Theis, Wagner (2021). cs.IT. Proves the rate-distortion-perception function is achievable with stochastic variable-length codes and lower-bounds achievable rate — the realism/distortion trade-off made operational.

**Content extract (abstract):**

```
The rate-distortion-perception function (RDPF; Blau and Michaeli, 2019) has emerged as a useful tool for thinking about realism and distortion of reconstructions in lossy compression. Unlike the rate-distortion function, however, it is unknown whether encoders and decoders exist that achieve the rate suggested by the RDPF. Building on results by Li and El Gamal (2018), we show that the RDPF can indeed be achieved using stochastic, variable-length codes. For this class of codes, we also prove that the RDPF lower-bounds the achievable rate.
```

## candidate-12 [rate-distortion] — REJECTED (B2 pass 27)
Shannon-machinery bounds paper: the conditional-independence decomposition instantiates no machine beyond the already-covered RD/matching lineage (BA 1972, NERD, RDPF); <2 genuine machines.

**Title:** Information-Theoretic Limits on Compression of Semantic Information

**URL:** https://arxiv.org/abs/2306.02305

**Description:** Tang, Yang, Zhang (2023). cs.IT. Semantic source as Bayesian-network-correlated variables; lossless/lossy limits, rate-distortion bounds, and Wyner–Ziv side-information variant.

**Content extract (abstract):**

```
As conventional communication systems based on classic information theory have closely approached the limits of Shannon channel capacity, semantic communication has been recognized as a key enabling technology for the further improvement of communication performance. However, it is still unsettled on how to represent semantic information and characterise the theoretical limits. In this paper, we consider a semantic source which consists of a set of correlated random variables whose joint probabilistic distribution can be described by a Bayesian network. Then we give the information-theoretic limit on the lossless compression of the semantic source and introduce a low complexity encoding method by exploiting the conditional independence. We further characterise the limits on lossy compression of the semantic source and the corresponding upper and lower bounds of the rate-distortion function. We also investigate the lossy compression of the semantic source with side information at both the encoder and decoder, and obtain the rate distortion function. We prove that the optimal code of the semantic source is the combination of the optimal codes of each conditional independent set given the side information.
```

## candidate-13 [rate-distortion] — ANNOTATED as 2601.16461 (B2 pass 28 → annotations/2601.16461.md; rate-distortion group CLOSED 4/4)

**Title:** Log-Likelihood Loss for Semantic Compression

**URL:** https://arxiv.org/abs/2601.16461

**Description:** Yadav, Song, Shkel, Özgür (2026). cs.IT. Lossy source coding under negative-log-likelihood distortion — reconstruction as semantic representation from which the source is probabilistically generated.

**Content extract (abstract):**

```
We study lossy source coding under a distortion measure defined by the negative log-likelihood induced by a prescribed conditional distribution P_{X|U}. This log-likelihood distortion models compression settings in which the reconstruction is a semantic representation from which the source can be probabilistically generated, rather than a pointwise approximation. We formulate the corresponding rate-distortion problem and characterize fundamental properties of the resulting rate-distortion function, including its connections to lossy compression under log-loss, classical rate-distortion problems with arbitrary distortion measures, and rate-distortion with perfect perception.
```

## candidate-14 [ldpc-bp] — UNCONSUMED

**Title:** Approaching the Rate-Distortion Limit with Spatial Coupling, Belief propagation and Decimation

**URL:** https://arxiv.org/abs/1307.5210

**Description:** Aref, Macris, Vuffray (2013). cs.IT. BP-guided decimation on spatially coupled LDGM codes approaches the Shannon rate-distortion limit; performance explained via spin-glass cavity method phase diagram (dynamical + condensation transitions).

**Content extract (abstract):**

```
We investigate an encoding scheme for lossy compression of a binary symmetric source based on simple spatially coupled Low-Density Generator-Matrix codes. The degree of the check nodes is regular and the one of code-bits is Poisson distributed with an average depending on the compression rate. The performance of a low complexity Belief Propagation Guided Decimation algorithm is excellent. The algorithmic rate-distortion curve approaches the optimal curve of the ensemble as the width of the coupling window grows. Moreover, as the check degree grows both curves approach the ultimate Shannon rate-distortion limit. The Belief Propagation Guided Decimation encoder is based on the posterior measure of a binary symmetric test-channel. This measure can be interpreted as a random Gibbs measure at a "temperature" directly related to the "noise level of the test-channel". We investigate the links between the algorithmic performance of the Belief Propagation Guided Decimation encoder and the phase diagram of this Gibbs measure. The phase diagram is investigated thanks to the cavity method of spin glass theory which predicts a number of phase transition thresholds. In particular the dynamical and condensation "phase transition temperatures" (equivalently test-channel noise thresholds) are computed. We observe that: (i) the dynamical temperature of the spatially coupled construction saturates towards the condensation temperature; (ii) for large degrees the condensation temperature approaches the temperature (i.e. noise level) related to the information theoretic Shannon test-channel noise parameter of rate-distortion theory. This provides heuristic insight into the excellent performance of the Belief Propagation Guided Decimation algorithm. The paper contains an introduction to the cavity method.
```

## candidate-15 [ldpc-bp] — UNCONSUMED

**Title:** Statistical Physics of Irregular Low-Density Parity-Check Codes

**URL:** https://arxiv.org/abs/cond-mat/9908358

**Description:** Vicente, Saad, Kabashima (1999). cond-mat.dis-nn. Replica method finds a phase transition in irregular LDPC codes coinciding with Shannon's coding bound; BP decoding analyzed with statistical-physics arguments.

**Content extract (abstract):**

```
Low-density parity-check codes with irregular constructions have been recently shown to outperform the most advanced error-correcting codes to date. In this paper we apply methods of statistical physics to study the typical properties of simple irregular codes. We use the replica method to find a phase transition which coincides with Shannon's coding bound when appropriate parameters are chosen. The decoding by belief propagation is also studied using statistical physics arguments; the theoretical solutions obtained are in good agreement with simulations. We compare the performance of irregular with that of regular codes and discuss the factors that contribute to the improvement in performance.
```

## candidate-16 [ldpc-bp] — UNCONSUMED

**Title:** Accuracy-Memory Tradeoffs and Phase Transitions in Belief Propagation

**URL:** https://arxiv.org/abs/1905.10031

**Description:** Jain, Koehler, Liu, Mossel (2019). cs.IT/math.ST. Proves bounded-memory message passing has a phase transition strictly below the Kesten–Stigum/BP threshold; proof combines recursive reconstruction, information theory, and optimal transport.

**Content extract (abstract):**

```
The analysis of Belief Propagation and other algorithms for the reconstruction problem plays a key role in the analysis of community detection in inference on graphs, phylogenetic reconstruction in bioinformatics, and the cavity method in statistical physics. We prove a conjecture of Evans, Kenyon, Peres, and Schulman (2000) which states that any bounded memory message passing algorithm is statistically much weaker than Belief Propagation for the reconstruction problem. More formally, any recursive algorithm with bounded memory for the reconstruction problem on the trees with the binary symmetric channel has a phase transition strictly below the Belief Propagation threshold, also known as the Kesten-Stigum bound. The proof combines in novel fashion tools from recursive reconstruction, information theory, and optimal transport, and also establishes an asymptotic normality result for BP and other message-passing algorithms near the critical threshold.
```

## candidate-17 [ldpc-bp] — UNCONSUMED

**Title:** Asymptotic analysis of the stochastic block model for modular networks and its algorithmic applications

**URL:** https://arxiv.org/abs/1109.3041

**Description:** Decelle, Krzakala, Moore, Zdeborová (2011). cond-mat.stat-mech. Cavity-method phase diagram of the stochastic block model: detectability/undetectability and easy/hard transitions; BP algorithm asymptotically optimal for community detection.

**Content extract (abstract):**

```
In this paper we extend our previous work on the stochastic block model, a commonly used generative model for social and biological networks, and the problem of inferring functional groups or communities from the topology of the network. We use the cavity method of statistical physics to obtain an asymptotically exact analysis of the phase diagram. We describe in detail properties of the detectability/undetectability phase transition and the easy/hard phase transition for the community detection problem. Our analysis translates naturally into a belief propagation algorithm for inferring the group memberships of the nodes in an optimal way, i.e., that maximizes the overlap with the underlying group memberships, and learning the underlying parameters of the block model. Finally, we apply the algorithm to two examples of real-world networks and discuss its performance.
```
