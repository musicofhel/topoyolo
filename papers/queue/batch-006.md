# Queue batch-006 — arXiv foraging export, 2026-08-25

Third foraged batch (abstract-only provenance). Theme: **Gromov–Wasserstein
theory core** — the Matching machine's own mathematical literature (invariance,
stability, statistical inference, Monge-vs-Kantorovich), which the corpus
currently touches only through applications; plus one **neuro-PID bridge**.
Several candidates carry explicit stability theorems or null-hypothesis tests,
so expect multi-machine fits. Deduped by title vs batches 001–005; run the
index-prose check regardless.
Consume per papers/INGESTION.md (≤3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [gw-theory] — ANNOTATED as 2006.12287 (pass 35)

**Title:** Gromov-Wasserstein Distance based Object Matching: Asymptotic Inference

**URL:** https://arxiv.org/abs/2006.12287

**Description:** Weitkamp, Proksch, Tameling, Munk (2020). math.ST. Statistical theory for GW-based matching: asymptotic distributional limits of a trimmed GW lower bound yield a pose-invariant discrimination test — Matching + Null Hypothesis in one object.

**Content extract (abstract):**

```
In this paper, we aim to provide a statistical theory for object matching based on the Gromov-Wasserstein distance. To this end, we model general objects as metric measure spaces. Based on this, we propose a simple and efficiently computable asymptotic statistical test for pose invariant object discrimination. This is based on an empirical version of a beta-trimmed lower bound of the Gromov-Wasserstein distance. We derive for beta in [0,1/2) distributional limits of this test statistic. To this end, we introduce a novel U-type process indexed in beta and show its weak convergence. Finally, the theory developed is investigated in Monte Carlo simulations and applied to structural protein comparisons.
```

## candidate-02 [gw-theory] — ANNOTATED as 2212.14123 (pass 35)

**Title:** Comparison Results for Gromov-Wasserstein and Gromov-Monge Distances

**URL:** https://arxiv.org/abs/2212.14123

**Description:** Mémoli, Needham (2022). math.MG. GW (coupling) vs GM (map) formulations: equal on non-atomic metric measure spaces; bi-Hölder equivalence with isometry-invariant Monge OT — the Kantorovich-vs-Monge split inside the Matching machine itself.

**Content extract (abstract):**

```
Inspired by the Kantorovich formulation of optimal transport distance between probability measures on a metric space, Gromov-Wasserstein (GW) distances comprise a family of metrics on the space of isomorphism classes of metric measure spaces. In previous work, the authors introduced a variant of this construction which was inspired by the original Monge formulation of optimal transport; elements of the resulting family are referred to Gromov-Monge (GM) distances. These GM distances, and related ideas, have since become a subject of interest from both theoretical and applications-oriented perspectives. In this note, we establish several theoretical properties of GM distances, focusing on comparisons between GM and GW distances. In particular, we show that GM and GW distances are equal for non-atomic metric measure spaces. We also consider variants of GM distance, such as a Monge version of Sturm's Lp-transportion distance, and give precise comparisons to GW distance. Finally, we establish bi-Hölder equivalence between GM distance and an isometry-invariant Monge optimal transport distance between Euclidean metric measure spaces that has been utilized in shape and image analysis applications.
```

## candidate-03 [gw-theory] — ANNOTATED as 2201.09385 (pass 35)

**Title:** Classical Multidimensional Scaling on Metric Measure Spaces

**URL:** https://arxiv.org/abs/2201.09385

**Description:** Lim, Mémoli (2022). math.FA. cMDS generalized to metric measure spaces; sum of negative eigenvalues as a non-flatness invariant; stability of the process proven with respect to Gromov–Wasserstein distance.

**Content extract (abstract):**

```
We generalize the classical Multidimensional Scaling procedure to the setting of general metric measure spaces. We develop a related spectral theory for the generalized cMDS operator, which provides a more natural and rigorous mathematical background for cMDS. Also, we show that the sum of all negative eigenvalues of the cMDS operator is a new invariant measuring non-flatness of a metric measure space. Furthermore, the cMDS output of several non-finite exemplar metric measures spaces, in particular the cMDS for spheres S^{d-1} and subsets of Euclidean space, are studied. Finally, we prove the stability of the generalized cMDS process with respect to the Gromov-Wasserstein distance.
```

## candidate-04 [gw-theory] — ANNOTATED as 2507.01171 (pass 36)

**Title:** A Stable and Theoretically Grounded Gromov-Wasserstein Distance for Reeb Graph Comparison using Persistence Images

**URL:** https://arxiv.org/abs/2507.01171

**Description:** Chambers, Meng (2025). cs.CG. Reeb-graph GW distance weighted by persistence images from extended persistence diagrams, with a proven stability theorem under scalar-field perturbation — Matching + Stability + Filtration in one construction.

**Content extract (abstract):**

```
Reeb graphs are a fundamental structure for analyzing the topological and geometric properties of scalar fields. Comparing Reeb graphs is crucial for advancing research in this domain, yet existing metrics are often computationally prohibitive or fail to capture essential topological features effectively. In this paper, we explore the application of the Gromov-Wasserstein distance, a versatile metric for comparing metric measure spaces, to Reeb graphs. We propose a framework integrating a symmetric variant of the Reeb radius for robust geometric comparison, and a novel probabilistic weighting scheme based on Persistence Images derived from extended persistence diagrams to effectively incorporate topological significance. A key contribution of this work is the rigorous theoretical proof of the stability of our proposed Reeb Gromov-Wasserstein distance with respect to perturbations in the underlying scalar fields. This ensures that small changes in the input data lead to small changes in the computed distance between Reeb graphs, a critical property for reliable analysis. We demonstrate the advantages of our approach, including its enhanced ability to capture topological features and its proven stability, through comparisons with other alternatives on several datasets, showcasing its practical utility and theoretical soundness.
```

## candidate-05 [gw-theory] — ANNOTATED as 2606.10295 (pass 36)

**Title:** k-Nearest Neighbors in Gromov--Wasserstein Space

**URL:** https://arxiv.org/abs/2606.10295

**Description:** Hohmeier, Fraiman, Moosmueller (2026). stat.ML. Universal consistency of k-NN classification under GW and fused-GW distances on equivalence classes of metric measure spaces — a statistical guarantee (Stability-class) living directly on Matching-space geometry.

**Content extract (abstract):**

```
The Gromov--Wasserstein (GW) distance provides a framework for comparing metric measure spaces, regardless of their underlying structure or geometry. For network-based data, it enables direct comparisons of graphs with different numbers of nodes, without requiring an embedding or other abstraction. Furthermore, through a variant of GW known as fused Gromov--Wasserstein (fGW), it is also possible to incorporate node features in addition to graph structure. In this work, we implement k-nearest neighbors (k-NN) classification using the GW and fGW distances. We prove the universal consistency of the GW-k-NN classifier on the space of equivalence classes of metric measure spaces with finite support and uniform probability measure. By viewing graphs as finitely supported metric measure spaces equipped with the pairwise distance metric and a uniform probability measure on the nodes, we obtain universal consistency of GW-k-NN for the space of graphs. Likewise for fGW-k-NN, we prove universal consistency on the space of weak isomorphism classes of structured objects consisting of metric measure spaces with finite support and uniform probability measure and feature maps into Euclidean space, thus establishing universal consistency on the space of node-attributed graphs. Our numerical experiments show that GW-k-NN and fGW-k-NN consistently perform well across multiple graph datasets, suggesting that metric classifiers such as k-NN work well in the GW framework.
```

## candidate-06 [gw-theory] — ANNOTATED as 2608.09265 (pass 36)

**Title:** Entropic Partial Optimal Transport and Partial Gromov--Wasserstein Distance between Gaussian Mixtures

**URL:** https://arxiv.org/abs/2608.09265

**Description:** Yachimura, Zou (2026). math.OC. Partial (unbalanced) GW for Gaussian mixtures: existence/uniqueness of the entropic minimizer, large-penalty limits, metric property — mass-conservation relaxation inside the Matching machine.

**Content extract (abstract):**

```
Optimal transport and Gromov--Wasserstein distances are useful tools for comparing probability measures and metric measure spaces, but their balanced formulations force all mass to be matched. This constraint is often too strong for data with outliers, missing parts, or only partial overlap. In this paper, we develop entropic partial optimal transport for Gaussian mixture models and define a partial mixture Gromov--Wasserstein distance. For the finite entropic partial optimal transport problem, we prove the existence and uniqueness of the minimizer and establish quantitative large-penalty estimates. Moreover, the resulting entropic partial component couplings induce continuous partial transport plans through Gaussian optimal maps. We analyze their large-penalty and subsequent zero-entropy limits and construct the associated displacement interpolations and barycentric projection maps. In addition, by identifying each Gaussian mixture with a finite metric measure space of Gaussian components, we establish the metric property and large-penalty limit of the partial mixture Gromov--Wasserstein distance. Finally, numerical experiments on synthetic Gaussian mixtures and point clouds illustrate the effects of the penalty and entropic regularization and the robustness of partial matching to outliers.
```

## candidate-07 [gw-theory] — REJECTED (pass 37)
Barycentric-projection linearization is a computational accelerator for pairwise GW (a Matching-machine tool with numerical examples only): <2 machines and duplicate GW-theory coverage (2212.14123, 2201.09385).

**Title:** On a linear Gromov-Wasserstein distance

**Title:** On a linear Gromov-Wasserstein distance

**URL:** https://arxiv.org/abs/2112.11964

**Description:** Beier, Beinert, Steidl (2021). math.NA. Linear GW via barycentric projection of transport plans — likely single-machine (Matching linearization); triage candidate.

**Content extract (abstract):**

```
Gromov-Wasserstein distances are generalization of Wasserstein distances, which are invariant under distance preserving transformations. Although a simplified version of optimal transport in Wasserstein spaces, called linear optimal transport (LOT), was successfully used in practice, there does not exist a notion of linear Gromov-Wasserstein distances so far. In this paper, we propose a definition of linear Gromov-Wasserstein distances. We motivate our approach by a generalized LOT model, which is based on barycentric projection maps of transport plans. Numerical examples illustrate that the linear Gromov-Wasserstein distances, similarly as LOT, can replace the expensive computation of pairwise Gromov-Wasserstein distances in applications like shape classification.
```

## candidate-08 [neuro-pid] — ANNOTATED as 2203.10810 (pass 37)

**Title:** Information-theoretic analyses of neural data to minimize the effect of researchers' assumptions in predictive coding studies

**URL:** https://arxiv.org/abs/2203.10810

**Description:** Wollstadt, Rathbun, Usrey, Bastos, Lindner, Priesemann, Wibral (2022). q-bio.NC. Local active information storage + local transfer entropy + partial information decomposition to break the circularity of predictive-coding analyses; applied to cat retinogeniculate spiking — joint-vs-marginal + null hypothesis, neuroscience cell.

**Content extract (abstract):**

```
Studies investigating neural information processing often implicitly ask both, which processing strategy out of several alternatives is used and how this strategy is implemented in neural dynamics. A prime example are studies on predictive coding. These often ask if confirmed predictions about inputs or predictions errors between internal predictions and inputs are passed on in a hierarchical neural system--while at the same time looking for the neural correlates of coding for errors and predictions. If we do not know exactly what a neural system predicts at any given moment, this results in a circular analysis--as has been criticized correctly. To circumvent such circular analysis, we propose to express information processing strategies (such as predictive coding) by local information-theoretic quantities, such that they can be estimated directly from neural data. We demonstrate our approach by investigating two opposing accounts of predictive coding-like processing strategies, where we quantify the building blocks of predictive coding, namely predictability of inputs and transfer of information, by local active information storage and local transfer entropy. We define testable hypotheses on the relationship of both quantities to identify which of the assumed strategies was used. We demonstrate our approach on spiking data from the retinogeniculate synapse of the cat. Applying our local information dynamics framework, we are able to show that the synapse codes for predictable rather than surprising input. To support our findings, we apply measures from partial information decomposition, which allow to differentiate if the transferred information is primarily bottom-up sensory input or information transferred conditionally on the current state of the synapse. Supporting our local information-theoretic results, we find that the synapse preferentially transfers bottom-up information.
```
