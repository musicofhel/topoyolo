# Queue batch-010 — arXiv foraging export, 2026-08-25

**CLOSED (pass 54): 9/9 annotated** (sheaf 4/4 passes 52–53; ccm 5/5 passes 52–54).

Seventh foraged batch (abstract-only provenance). Two groups:
**sheaf** — cellular sheaf theory as the chain-complex machine's modern working
form (foundational SNNs, predictive-coding cohomology — a Hodge/neuro bridge,
higher-dimensional constructions, and GIT-stability analysis of sheaf
diffusion); **ccm** — convergent-cross-mapping causal inference (Dynamics×Null:
tangent-space synchronization, the CCM-limits critique, multivariate partial
cross mapping as joint-vs-marginal, an empirical GC-vs-CCM null, and
path-signature signed-area tests).
Deduped by title vs batches 001-009; run the index-prose check regardless.
Consume per papers/INGESTION.md (<=3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [sheaf] — ANNOTATED as 2012.06333

**Title:** Sheaf Neural Networks

**URL:** https://arxiv.org/abs/2012.06333

**Description:** Hansen, Gebhart (2020). cs.LG/math.AT. The foundational SNN paper: sheaf Laplacian generalizes graph diffusion to non-constant, asymmetric, dimension-varying relations — the chain-complex machine operating as an ML architecture.

**Content extract (abstract):**

```
We present a generalization of graph convolutional networks by generalizing the diffusion operation underlying this class of graph neural networks. These sheaf neural networks are based on the sheaf Laplacian, a generalization of the graph Laplacian that encodes additional relational structure parameterized by the underlying graph. The sheaf Laplacian and associated matrices provide an extended version of the diffusion operation in graph convolutional networks, providing a proper generalization for domains where relations between nodes are non-constant, asymmetric, and varying in dimension. We show that the resulting sheaf neural networks can outperform graph convolutional networks in domains where relations between nodes are asymmetric and signed.
```

## candidate-02 [sheaf] — ANNOTATED as 2511.11092

**Title:** Sheaf Cohomology of Linear Predictive Coding Networks

**URL:** https://arxiv.org/abs/2511.11092

**Description:** Seely (2025). cs.LG. Linear predictive coding IS a cellular sheaf: coboundary = prediction error, inference = sheaf-Laplacian diffusion, cohomology = irreducible error inference cannot remove; Hodge decomposition locates learning stalls — chain complex + neuroscience bridge.

**Content extract (abstract):**

```
Predictive coding (PC) replaces global backpropagation with local optimization over weights and activations. We show that linear PC networks admit a natural formulation as cellular sheaves: the sheaf coboundary maps activations to edge-wise prediction errors, and PC inference is diffusion under the sheaf Laplacian. Sheaf cohomology then characterizes irreducible error patterns that inference cannot remove. We analyze recurrent topologies where feedback loops create internal contradictions, introducing prediction errors unrelated to supervision. Using a Hodge decomposition, we determine when these contradictions cause learning to stall. The sheaf formalism provides both diagnostic tools for identifying problematic network configurations and design principles for effective weight initialization for recurrent PC networks.
```

## candidate-03 [sheaf] — ANNOTATED as 2505.23993

**Title:** Cellular Sheaves on Higher-Dimensional Structures

**URL:** https://arxiv.org/abs/2505.23993

**Description:** Hu (2025). math.AT. Non-trivial sheaf constructions above dimension 1: geometric (0th sheaf Laplacian recovers anisotropic-network-model Hessians; higher Laplacians encode multi-way interactions) and algebraic (ringed spaces, sheaves of ideals) frameworks.

**Content extract (abstract):**

```
Defining cellular sheaves beyond graph structures, such as on simplicial complexes containing higher-dimensional simplices, is an essential and intriguing topic in topological data analysis (TDA) and the development of sheaf neural networks. In this paper, we explore methods for constructing non-trivial cellular sheaves on spaces that include structures of dimension greater than one. This extends the focus from 0- or 1-dimensional components, such as vertices and edges, to elements like triangles, tetrahedra, and other higher-dimensional simplices within a simplicial complex. We develop a unified framework that incorporates both geometric and algebraic approaches to modeling such complex systems using cellular sheaf theory. Motivated by the geometric and physical insights from anisotropic network models (ANM), we first introduce constructions that define sheaf structures whose 0-th sheaf Laplacians recover classical ANM Hessian matrices. The higher-dimensional sheaf Laplacians in this setting encode additional patterns of multi-way interactions. In parallel, we propose an algebraic framework based on commutative algebra and ringed spaces, where sheaves of ideals and modules are used to define sheaf structures in a combinatorial and algebraically grounded manner. These two perspectives -- the geometric-physical and the algebraic -- offer complementary strengths and together provide a versatile framework for encoding structural relationships and analyzing multi-scale data over simplicial complexes.
```

## candidate-04 [sheaf] — ANNOTATED as 2605.11178

**Title:** Oversmoothing as Representation Degeneracy in Neural Sheaf Diffusion

**URL:** https://arxiv.org/abs/2605.11178

**Description:** Dönmez, Mosig, Fritsche, Koch (2026). cs.LG/math.RT. Sheaves-as-quiver-representations: oversmoothing = degeneration toward low-complexity summands; GIT moment-map regularizers and a structural obstruction at equal stalk dimensions — stability theory applied to the chain-complex machine itself.

**Content extract (abstract):**

```
Neural Sheaf Diffusion (NSD) generalizes diffusion-based Graph Neural Networks by replacing scalar graph Laplacians with sheaf Laplacians whose learned restriction maps define a task-adapted geometry. While the diffusion limit of NSD is known to be the space of global sections, the representation-theoretic structure of this harmonic space remains largely implicit. We develop a quiver-theoretic interpretation of NSD by identifying cellular sheaves on graphs with representations of the associated incidence quiver. Under this correspondence, learned sheaf geometries become points in a finite-dimensional representation space. We show that direct-sum decompositions of the underlying incidence-quiver representation induce decompositions of the harmonic space reached in the diffusion limit. This gives an algebraic interpretation of oversmoothing as representation degeneration: learned sheaves may collapse toward low-complexity summands whose global sections fail to preserve discriminative information. Building on this viewpoint, we connect sheaf diffusion to stability and moment-map principles from Geometric Invariant Theory. We introduce moment-map-inspired regularizers that bias restriction maps toward balanced representation geometries, and identify a structural obstruction in equal-stalk architectures: when d_v = d_e, admissibility for learnable stability parameters forces the trivial all-object summand onto a stability wall. Non-uniform stalk dimensions remove this obstruction, making adaptive stability meaningful. Experiments on heterophilic benchmarks are consistent with this mechanism: breaking stalk symmetry can reduce variance or improve validation behavior, and adaptive stability becomes more effective in selected rectangular settings. Overall, our framework reframes oversmoothing as a degeneration phenomenon in the representation geometry underlying learned sheaf diffusion.
```

## candidate-05 [ccm] — ANNOTATED as 2410.23499

**Title:** Tangent Space Causal Inference: Leveraging Vector Fields for Causal Discovery in Dynamical Systems

**URL:** https://arxiv.org/abs/2410.23499

**Description:** Butler, Waxman, Djurić (2024). cs.LG/nlin.CD. TSCI: causality as synchronization degree between learned vector fields on reconstructed manifolds — drop-in CCM replacement; Dynamics + Matching + Null in one construction.

**Content extract (abstract):**

```
Causal discovery with time series data remains a challenging yet increasingly important task across many scientific domains. Convergent cross mapping (CCM) and related methods have been proposed to study time series that are generated by dynamical systems, where traditional approaches like Granger causality are unreliable. However, CCM often yields inaccurate results depending upon the quality of the data. We propose the Tangent Space Causal Inference (TSCI) method for detecting causalities in dynamical systems. TSCI works by considering vector fields as explicit representations of the systems' dynamics and checks for the degree of synchronization between the learned vector fields. The TSCI approach is model-agnostic and can be used as a drop-in replacement for CCM and its generalizations. We first present a basic version of the TSCI algorithm, which is shown to be more effective than the basic CCM algorithm with very little additional computation. We additionally present augmented versions of TSCI that leverage the expressive power of latent variable models and deep learning. We validate our theory on standard systems, and we demonstrate improved causal inference performance across a number of benchmark tasks.
```

## candidate-06 [ccm] — ANNOTATED as 1601.00716

**Title:** Limits to causal inference with state-space reconstruction for infectious disease

**URL:** https://arxiv.org/abs/1601.00716

**Description:** Cobey, Baskerville (2016). q-bio.QM. The CCM-limits paper: extreme sensitivity to shared periodicity, process noise, and attractor drift; a Timmer-class epistemics critique for the state-space-reconstruction null.

**Content extract (abstract):**

```
Infectious diseases are notorious for their complex dynamics, which make it difficult to fit models to test hypotheses. Methods based on state-space reconstruction have been proposed to infer causal interactions in noisy, nonlinear dynamical systems. These "model-free" methods are collectively known as convergent cross-mapping (CCM). Although CCM has theoretical support, natural systems routinely violate its assumptions. To identify the practical limits of causal inference under CCM, we simulated the dynamics of two pathogen strains with varying interaction strengths. The original method of CCM is extremely sensitive to periodic fluctuations, inferring interactions between independent strains that oscillate with similar frequencies. This sensitivity vanishes with alternative criteria for inferring causality. However, CCM remains sensitive to high levels of process noise and changes to the deterministic attractor. This sensitivity is problematic because it remains challenging to gauge noise and dynamical changes in natural systems, including the quality of reconstructed attractors that underlie cross-mapping. We illustrate these challenges by analyzing time series of reportable childhood infections in New York City and Chicago during the pre-vaccine era. We comment on the statistical and conceptual challenges that currently limit the use of state-space reconstruction in causal inference.
```

## candidate-07 [ccm] — ANNOTATED as 2502.03802

**Title:** MXMap: A Multivariate Cross Mapping Framework for Causal Discovery in Dynamical Systems

**URL:** https://arxiv.org/abs/2502.03802

**Description:** Zhang, Mirallès, Rousseau-Rizzi, Zinflou, Wu, Boulet (2025). cs.LG/math.DS. multiPCM extends partial cross mapping to multivariate embeddings; two-phase framework (pairwise CCM graph, multiPCM pruning of indirect links) — direct-vs-indirect causality as a joint-vs-marginal distinction.

**Content extract (abstract):**

```
Convergent Cross Mapping (CCM) is a powerful method for detecting causality in coupled nonlinear dynamical systems, providing a model-free approach to capture dynamic causal interactions. Partial Cross Mapping (PCM) was introduced as an extension of CCM to address indirect causality in three-variable systems by comparing cross-mapping quality between direct cause-effect mapping and indirect mapping through an intermediate conditioning variable. However, PCM remains limited to univariate delay embeddings in its cross-mapping processes. In this work, we extend PCM to the multivariate setting, introducing multiPCM, which leverages multivariate embeddings to more effectively distinguish indirect causal relationships. We further propose a multivariate cross-mapping framework (MXMap) for causal discovery in dynamical systems. This two-phase framework combines (1) pairwise CCM tests to establish an initial causal graph and (2) multiPCM to refine the graph by pruning indirect causal connections. Through experiments on simulated data and the ERA5 Reanalysis weather dataset, we demonstrate the effectiveness of MXMap. Additionally, MXMap is compared against several baseline methods, showing advantages in accuracy and causal graph refinement.
```

## candidate-08 [ccm] — ANNOTATED as 1909.00731

**Title:** Inferring species interactions using Granger causality and convergent cross mapping

**URL:** https://arxiv.org/abs/1909.00731

**Description:** Barraquand, Picoche, Detto, Hartig (2019). q-bio.PE. Linear Granger and CCM perform surprisingly similarly across deterministic-chaotic and stochastic ecological networks — no nonlinearity-to-method correspondence; an empirical null over the GC-vs-CCM methodological divide.

**Content extract (abstract):**

```
Identifying directed interactions between species from time series of their population densities has many uses in ecology. This key statistical task is equivalent to causal time series inference, which connects to the Granger causality (GC) concept: x causes y if x improves the prediction of y in a dynamic model. However, the entangled nature of nonlinear ecological systems has led to question the appropriateness of Granger causality, especially in its classical linear Multivariate AutoRegressive (MAR) model form. Convergent-cross mapping (CCM), a nonparametric method developed for deterministic dynamical systems, has been suggested as an alternative. Here, we show that linear GC and CCM are able to uncover interactions with surprisingly similar performance, for predator-prey cycles, 2-species deterministic (chaotic) or stochastic competition, as well as 10- and 20-species interaction networks. There is no correspondence between the degree of nonlinearity of the dynamics and which method performs best. Our results therefore imply that Granger causality, even in its linear MAR(p) formulation, is a valid method for inferring interactions in nonlinear ecological networks; using GC or CCM (or both) can instead be decided based on the aims and specifics of the analysis.
```

## candidate-09 [ccm] — ANNOTATED as 2110.12288

**Title:** Path Signature Area-Based Causal Discovery in Coupled Time Series

**URL:** https://arxiv.org/abs/2110.12288

**Description:** Glad, Woolf (2021). stat.ML. Signed areas of path signatures + confidence sequences as a model-free causal-discovery test with anytime-valid significance — new algebraic machinery for the lag/lead null.

**Content extract (abstract):**

```
Coupled dynamical systems are frequently observed in nature, but often not well understood in terms of their causal structure without additional domain knowledge about the system. Especially when analyzing observational time series data of dynamical systems where it is not possible to conduct controlled experiments, for example time series of climate variables, it can be challenging to determine how features causally influence each other. There are many techniques available to recover causal relationships from data, such as Granger causality, convergent cross mapping, and causal graph structure learning approaches such as PCMCI. Path signatures and their associated signed areas provide a new way to approach the analysis of causally linked dynamical systems, particularly in informing a model-free, data-driven approach to algorithmic causal discovery. With this paper, we explore the use of path signatures in causal discovery and propose the application of confidence sequences to analyze the significance of the magnitude of the signed area between two variables. These confidence sequence regions converge with greater sampling length, and in conjunction with analyzing pairwise signed areas across time-shifted versions of the time series, can help identify the presence of lag/lead causal relationships. This approach provides a new way to define the confidence of a causal link existing between two time series, and ultimately may provide a framework for hypothesis testing to define whether one time series causes another
```
