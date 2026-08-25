# Queue batch-009 — arXiv foraging export, 2026-08-25

Sixth foraged batch (abstract-only provenance). Two theory-core groups:
**pid-theory** — the Joint-vs-Marginal machine's own axiomatic literature
(Williams-Beer founding lattice, mereological unification, game-theoretic
alternative, fault-tolerance redundancy that is QEC-adjacent, localizability);
**rg-dl** — the renormalization-group↔deep-learning bridge (exact variational-RG
↔ RBM mapping, Bayesian RG at Fisher scale, two-phase learning dynamics,
inverse-RG generation, plus one skeptical diagnostic paper as a built-in null).
Deduped by title vs batches 001-008; run the index-prose check regardless —
Williams-Beer 2010 in particular may have Wave-era prose coverage.
Consume per papers/INGESTION.md (<=3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [pid-theory] — ANNOTATED as 1004.2515 (pass 48; founding lattice; no prior per-paper file despite heavy prose references — fresh annotation, not promote-on-encounter)

**Title:** Nonnegative Decomposition of Multivariate Information

**URL:** https://arxiv.org/abs/1004.2515

**Description:** Williams, Beer (2010). cs.IT. THE founding PID paper: redundancy as minimum per-outcome information induces the redundancy lattice; partial information atoms nonnegative by construction; explains interaction information's negativity as redundancy/synergy confounding.

**Content extract (abstract):**

```
Of the various attempts to generalize information theory to multiple variables, the most widely utilized, interaction information, suffers from the problem that it is sometimes negative. Here we reconsider from first principles the general structure of the information that a set of sources provides about a given variable. We begin with a new definition of redundancy as the minimum information that any source provides about each possible outcome of the variable, averaged over all possible outcomes. We then show how this measure of redundancy induces a lattice over sets of sources that clarifies the general structure of multivariate information. Finally, we use this redundancy lattice to propose a definition of partial information atoms that exhaustively decompose the Shannon information in a multivariate system in terms of the redundancy between synergies of subsets of the sources. Unlike interaction information, the atoms of our partial information decomposition are never negative and always support a clear interpretation as informational quantities. Our analysis also demonstrates how the negativity of interaction information can be explained by its confounding of redundancy and synergy.
```

## candidate-02 [pid-theory] — ANNOTATED as 2306.00734 (pass 48)

**Title:** From Babel to Boole: The Logical Organization of Information Decompositions

**URL:** https://arxiv.org/abs/2306.00734

**Description:** Gutknecht, Makkeh, Wibral (2023). cs.IT. Mereological formulation unifies redundancy/synergy/unique/union-based PIDs as special cases of one logical pattern; reveals novel base-concepts including 'vulnerable information'.

**Content extract (abstract):**

```
The conventional approach to the general Partial Information Decomposition (PID) problem has been redundancy-based: specifying a measure of redundant information between collections of source variables induces a PID via Moebius-Inversion over the so called redundancy lattice. Despite the prevalence of this method, there has been ongoing interest in examining the problem through the lens of different base-concepts of information, such as synergy, unique information, or union information. Yet, a comprehensive understanding of the logical organization of these different based-concepts and their associated PIDs remains elusive. In this work, we apply the mereological formulation of PID that we introduced in a recent paper to shed light on this problem. Within the mereological approach base-concepts can be expressed in terms of conditions phrased in formal logic on the specific parthood relations between the PID components and the different mutual information terms. We set forth a general pattern of these logical conditions of which all PID base-concepts in the literature are special cases and that also reveals novel base-concepts, in particular a concept we call "vulnerable information".
```

## candidate-03 [pid-theory] — ANNOTATED as 1910.05979 (pass 48)

**Title:** Information Decomposition based on Cooperative Game Theory

**URL:** https://arxiv.org/abs/1910.05979

**Description:** Ay, Polani, Virgo (2019). cs.IT. Decomposition from cooperative game theory (fair-share allocation) on a different lattice: fewer atoms, no redundancy term, but satisfies local positivity + identity simultaneously — which no PID measure can.

**Content extract (abstract):**

```
We offer a new approach to the information decomposition problem in information theory: given a 'target' random variable co-distributed with multiple 'source' variables, how can we decompose the mutual information into a sum of non-negative terms that quantify the contributions of each random variable, not only individually but also in combination? We derive our composition from cooperative game theory. It can be seen as assigning a "fair share" of the mutual information to each combination of the source variables. Our decomposition is based on a different lattice from the usual 'partial information decomposition' (PID) approach, and as a consequence our decomposition has a smaller number of terms: it has analogs of the synergy and unique information terms, but lacks terms corresponding to redundancy. Because of this, it is able to obey equivalents of the axioms known as 'local positivity' and 'identity', which cannot be simultaneously satisfied by a PID measure.
```

## candidate-04 [pid-theory] — ANNOTATED as 2404.01470 (pass 49)

**Title:** Measuring the Redundancy of Information from a Source Failure Perspective

**URL:** https://arxiv.org/abs/2404.01470

**Description:** Milzman (2024). cs.IT. Redundancy defined by robustness to source failures — an order-reversing correspondence between fault-tolerant instantiations and the PID lattice; bridges information redundancy to engineering fault tolerance (QEC-adjacent).

**Content extract (abstract):**

```
In this paper, we define a new measure of the redundancy of information from a fault tolerance perspective. The partial information decomposition (PID) emerged last decade as a framework for decomposing the multi-source mutual information I(T;X_1,...,X_n) into atoms of redundant, synergistic, and unique information. It built upon the notion of redundancy/synergy from McGill's interaction information (McGill 1954). Separately, the redundancy of system components has served as a principle of fault tolerant engineering, for sensing, routing, and control applications. Here, redundancy is understood as the level of duplication necessary for the fault tolerant performance of a system. With these two perspectives in mind, we propose a new PID-based measure of redundancy I_ft, based upon the presupposition that redundant information is robust to individual source failures. We demonstrate that this new measure satisfies the common PID axioms from (Williams 2010). In order to do so, we establish an order-reversing correspondence between collections of source-fallible instantiations of a system, on the one hand, and the PID lattice from (Williams 2010), on the other.
```

## candidate-05 [pid-theory] — ANNOTATED as 1303.3440 (pass 49)

**Title:** Towards a Synergy-based Approach to Measuring Information Modification

**URL:** https://arxiv.org/abs/1303.3440

**Description:** Lizier, Flecker, Williams (2013). cs.IT. Information modification in distributed computation measured via PID synergy; proposes a localizability axiom for redundancy measures — local dynamics of computation in space-time.

**Content extract (abstract):**

```
Distributed computation in artificial life and complex systems is often described in terms of component operations on information: information storage, transfer and modification. Information modification remains poorly described however, with the popularly-understood examples of glider and particle collisions in cellular automata being only quantitatively identified to date using a heuristic (separable information) rather than a proper information-theoretic measure. We outline how a recently-introduced axiomatic framework for measuring information redundancy and synergy, called partial information decomposition, can be applied to a perspective of distributed computation in order to quantify component operations on information. Using this framework, we propose a new measure of information modification that captures the intuitive understanding of information modification events as those involving interactions between two or more information sources. We also consider how the local dynamics of information modification in space and time could be measured, and suggest a new axiom that redundancy measures would need to meet in order to make such local measurements. Finally, we evaluate the potential for existing redundancy measures to meet this localizability axiom.
```

## candidate-06 [rg-dl] — UNCONSUMED

**Title:** An exact mapping between the Variational Renormalization Group and Deep Learning

**URL:** https://arxiv.org/abs/1410.3831

**Description:** Mehta, Schwab (2014). stat.ML/cond-mat. The canonical result: exact mapping from Kadanoff's variational RG to RBM-based deep architectures — deep learning as generalized RG-like feature extraction, on the Ising model.

**Content extract (abstract):**

```
Deep learning is a broad set of techniques that uses multiple layers of representation to automatically learn relevant features directly from structured data. Recently, such techniques have yielded record-breaking results on a diverse set of difficult machine learning tasks in computer vision, speech recognition, and natural language processing. Despite the enormous success of deep learning, relatively little is understood theoretically about why these techniques are so successful at feature learning and compression. Here, we show that deep learning is intimately related to one of the most important and successful techniques in theoretical physics, the renormalization group (RG). RG is an iterative coarse-graining scheme that allows for the extraction of relevant features (i.e. operators) as a physical system is examined at different length scales. We construct an exact mapping from the variational renormalization group, first introduced by Kadanoff, and deep learning architectures based on Restricted Boltzmann Machines (RBMs). We illustrate these ideas using the nearest-neighbor Ising Model in one and two-dimensions. Our results suggests that deep learning algorithms may be employing a generalized RG-like scheme to learn relevant features from data.
```

## candidate-07 [rg-dl] — UNCONSUMED

**Title:** Bayesian RG Flow in Neural Network Field Theories

**URL:** https://arxiv.org/abs/2405.17538

**Description:** Howard, Klinger, Maiti, Stapleton (2024). hep-th/cs.LG. BRG-NNFT: information-theoretic coarse graining in parameter space at a Fisher-metric distinguishability scale; training = IR→UV flow, coarse-graining = UV→IR; equals exact-RG when scales coincide.

**Content extract (abstract):**

```
The Neural Network Field Theory correspondence (NNFT) is a mapping from neural network (NN) architectures into the space of statistical field theories (SFTs). The Bayesian renormalization group (BRG) is an information-theoretic coarse graining scheme that generalizes the principles of the exact renormalization group (ERG) to arbitrarily parameterized probability distributions, including those of NNs. In BRG, coarse graining is performed in parameter space with respect to an information-theoretic distinguishability scale set by the Fisher information metric. In this paper, we unify NNFT and BRG to form a powerful new framework for exploring the space of NNs and SFTs, which we coin BRG-NNFT. With BRG-NNFT, NN training dynamics can be interpreted as inducing a flow in the space of SFTs from the information-theoretic 'IR' to 'UV'. Conversely, applying an information-shell coarse graining to the trained network's parameters induces a flow in the space of SFTs from the information-theoretic 'UV' to 'IR'. When the information-theoretic cutoff scale coincides with a standard momentum scale, BRG is equivalent to ERG. We demonstrate the BRG-NNFT correspondence on two analytically tractable examples. First, we construct BRG flows for trained, infinite-width NNs, of arbitrary depth, with generic activation functions. As a special case, we then restrict to architectures with a single infinitely-wide layer, scalar outputs, and generalized cos-net activations. In this case, we show that BRG coarse-graining corresponds exactly to the momentum-shell ERG flow of a free scalar SFT. Our analytic results are corroborated by a numerical experiment in which an ensemble of asymptotically wide NNs are trained and subsequently renormalized using an information-shell BRG scheme.
```

## candidate-08 [rg-dl] — UNCONSUMED

**Title:** A Two-Phase Perspective on Deep Learning Dynamics

**URL:** https://arxiv.org/abs/2504.12700

**Description:** de Mello Koch, Ghosh (2025). hep-th/cs.LG. Learning = rapid curve-fitting then slow compression; grokking, double descent, and the information bottleneck share this temporal structure; compression phase as principled RG-like forgetting critical for generalization.

**Content extract (abstract):**

```
We propose that learning in deep neural networks proceeds in two phases: a rapid curve fitting phase followed by a slower compression or coarse graining phase. This view is supported by the shared temporal structure of three phenomena: grokking, double descent and the information bottleneck, all of which exhibit a delayed onset of generalization well after training error reaches zero. We empirically show that the associated timescales align in two rather different settings. Mutual information between hidden layers and input data emerges as a natural progress measure, complementing circuit-based metrics such as local complexity and the linear mapping number. We argue that the second phase is not actively optimized by standard training algorithms and may be unnecessarily prolonged. Drawing on an analogy with the renormalization group, we suggest that this compression phase reflects a principled form of forgetting, critical for generalization.
```

## candidate-09 [rg-dl] — UNCONSUMED

**Title:** Dreaming up scale invariance via inverse renormalization group

**URL:** https://arxiv.org/abs/2506.04016

**Description:** Rançon, Rançon, Ivek, Balog (2025). cond-mat/cs.LG. Minimal nets (3 trainable parameters) invert RG coarse-graining probabilistically, generating critical 2D Ising configurations that reproduce scaling and nontrivial RG eigenvalues; added depth gives no benefit.

**Content extract (abstract):**

```
We explore how minimal neural networks can invert the renormalization group (RG) coarse-graining procedure in the two-dimensional Ising model, effectively 'dreaming up' microscopic configurations from coarse-grained states. This task - formally impossible at the level of configurations - can be approached probabilistically, allowing machine learning models to reconstruct scale-invariant distributions without relying on microscopic input. We demonstrate that even neural networks with as few as three trainable parameters can learn to generate critical configurations, reproducing the scaling behavior of observables such as magnetic susceptibility, heat capacity, and Binder ratios. A real-space renormalization group analysis of the generated configurations confirms that the models capture not only scale invariance but also reproduce nontrivial eigenvalues of the RG transformation. While the inversion is necessarily imperfect, these minimal models robustly reproduce the RG-relevant structure of the critical distribution. Surprisingly, we find that increasing network complexity by introducing multiple layers offers no significant benefit. These findings suggest that simple local rules, akin to those generating fractal structures, are sufficient to encode the universality of critical phenomena, creating an opportunity for efficient generative models of statistical ensembles in physics.
```

## candidate-10 [rg-dl] — UNCONSUMED

**Title:** Is Deep Learning a Renormalization Group Flow?

**URL:** https://arxiv.org/abs/1906.05212

**Description:** de Mello Koch, de Mello Koch, Cheng (2019). cs.LG/cond-mat. Hidden-visible correlator diagnostics for RG-like coarse graining in RBMs trained on Ising configurations — finds RG-like patterns AND important differences; a skeptical counterweight to the exact-mapping claims.

**Content extract (abstract):**

```
Although there has been a rapid development of practical applications, theoretical explanations of deep learning are in their infancy. Deep learning performs a sophisticated coarse graining. Since coarse graining is a key ingredient of the renormalization group (RG), RG may provide a useful theoretical framework directly relevant to deep learning. In this study we pursue this possibility. A statistical mechanics model for a magnet, the Ising model, is used to train an unsupervised restricted Boltzmann machine (RBM). The patterns generated by the trained RBM are compared to the configurations generated through an RG treatment of the Ising model. Although we are motivated by the connection between deep learning and RG flow, in this study we focus mainly on comparing a single layer of a deep network to a single step in the RG flow. We argue that correlation functions between hidden and visible neurons are capable of diagnosing RG-like coarse graining. Numerical experiments show the presence of RG-like patterns in correlators computed using the trained RBMs. The observables we consider are also able to exhibit important differences between RG and deep learning.
```
