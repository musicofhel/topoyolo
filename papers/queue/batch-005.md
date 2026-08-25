# Queue batch-005 — arXiv foraging export, 2026-08-25

Second foraged batch (abstract-only provenance, same rules as batch-004).
Targets: **channel-capacity** (last zero-coverage gap topic; several are
capacity↔phase-transition bridges, two feed the thin QEC×Joint-vs-Marginal
cell) and **ph-stability** (stability-theorem theory core for the Filtrations
row — interleaving/bottleneck machinery, not PH-as-descriptor wrappers).
Deduped by title against queue batches 001–004; run your index-prose check
before annotating regardless.
Consume per papers/INGESTION.md (≤3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [channel-capacity] — UNCONSUMED

**Title:** Secure Coding via Gaussian Random Fields

**URL:** https://arxiv.org/abs/2205.08782

**Description:** Bereyhi, Loureiro, Krzakala, Müller, Schulz-Baldes (2022). cs.IT. Replica method shows the all-or-nothing inference transition's critical rate IS the channel capacity; achieves wiretap secrecy capacity.

**Content extract (abstract):**

```
Inverse probability problems whose generative models are given by strictly nonlinear Gaussian random fields show the all-or-nothing behavior: There exists a critical rate at which Bayesian inference exhibits a phase transition. Below this rate, the optimal Bayesian estimator recovers the data perfectly, and above it the recovered data becomes uncorrelated. This study uses the replica method from the theory of spin glasses to show that this critical rate is the channel capacity. This interesting finding has a particular application to the problem of secure transmission: A strictly nonlinear Gaussian random field along with random binning can be used to securely encode a confidential message in a wiretap channel. Our large-system characterization demonstrates that this secure coding scheme asymptotically achieves the secrecy capacity of the Gaussian wiretap channel.
```

## candidate-02 [channel-capacity] — UNCONSUMED

**Title:** Typical Performance of Gallager-type Error-Correcting Codes

**URL:** https://arxiv.org/abs/cond-mat/9908104

**Description:** Kabashima, Murayama, Saad (1999). cond-mat.dis-nn. Statistical-physics analysis of Gallager/LDPC codes: Shannon capacity saturated for many code families; TAP decoding shown identical to belief propagation.

**Content extract (abstract):**

```
The performance of Gallager's error-correcting code is investigated via methods of statistical physics. In this approach, the transmitted codeword comprises products of the original message bits selected by two randomly-constructed sparse matrices; the number of non-zero row/column elements in these matrices constitutes a family of codes. We show that Shannon's channel capacity is saturated for many of the codes while slightly lower performance is obtained for others which may be of higher practical relevance. Decoding aspects are considered by employing the TAP approach which is identical to the commonly used belief-propagation-based decoding.
```

## candidate-03 [channel-capacity] — ANNOTATED as 1112.4589 (pass 30)

**Title:** An Information Theoretical Analysis of Kinase Activated Phosphorylation Dephosphorylation Cycle

**URL:** https://arxiv.org/abs/1112.4589

**Description:** Qian, Roy (2011). q-bio.SC/cond-mat.stat-mech. Channel capacity of biochemical signaling modules is zero iff free-energy expenditure is zero — capacity↔dissipation bridge; multistage-code interpretation of cascades.

**Content extract (abstract):**

```
Signal transduction, the information processing mechanism in biological cells, is carried out by a network of biochemical reactions. The dynamics of driven biochemical reactions can be studied in terms of nonequilibrium statistical physics. Such systems may also be studied in terms of Shannon's information theory. We combine these two perspectives in this study of the basic units (modules) of cellular signaling: the phosphorylation dephosphorylation cycle (PdPC) and the guanosine triphosphatase (GTPase). We show that the channel capacity is zero if and only if the free energy expenditure of biochemical system is zero. In fact, a positive correlation between the channel capacity and free energy expenditure is observed. In terms of the information theory, a linear signaling cascade consisting of multiple steps of PdPC can function as a distributed "multistage code". With increasing number of steps in the cascade, the system trades channel capacity with the code complexity. Our analysis shows that while a static code can be molecular structural based; a biochemical communication channel has to have energy expenditure.
```

## candidate-04 [channel-capacity] — ANNOTATED as 1903.05124 (pass 30)

**Title:** Quantum Error Correction in Scrambling Dynamics and Measurement-Induced Phase Transition

**URL:** https://arxiv.org/abs/1903.05124

**Description:** Choi, Bao, Qi, Altman (2019). quant-ph/cond-mat. Volume-law/area-law entanglement transition understood as quantum error correction; relates the entanglement phase transition to changes in quantum channel capacity — QEC-cell feed.

**Content extract (abstract):**

```
We analyze the dynamics of entanglement entropy in a generic quantum many-body open system from the perspective of quantum information and error corrections. We introduce a random unitary circuit model with intermittent projective measurements, in which the degree of information scrambling by the unitary and the rate of projective measurements are independently controlled. This model displays two stable phases, characterized by the volume-law and area-law scaling entanglement entropy in steady states. The transition between the two phases is understood from the point of view of quantum error correction: the chaotic unitary evolution protects quantum information from projective measurements that act as errors. A phase transition occurs when the rate of errors exceeds a threshold that depends on the degree of information scrambling. We confirm these results using numerical simulations and obtain the phase diagram of our model. Our work shows that information scrambling plays a crucial role in understanding the dynamics of entanglement in an open quantum system and relates the entanglement phase transition to changes in quantum channel capacity.
```

## candidate-05 [channel-capacity] — UNCONSUMED

**Title:** Coherence requirements for quantum communication from hybrid circuit dynamics

**URL:** https://arxiv.org/abs/2210.11547

**Description:** Kelly, Poschinger, Schmidt-Kaler, Fisher, Marino (2022). quant-ph/cond-mat. Adversarial unitary-vs-measurement game; coherence-tuned phase transitions in quantum channel capacity; coherence upper-bounds stabilizer code distance — QEC-cell feed.

**Content extract (abstract):**

```
The coherent superposition of quantum states is an important resource for quantum information processing which distinguishes quantum dynamics and information from their classical counterparts. In this article we determine the coherence requirements to communicate quantum information in a broad setting encompassing monitored quantum dynamics and quantum error correction codes. We determine these requirements by considering hybrid circuits that are generated by a quantum information game played between two opponents, Alice and Eve, who compete by applying unitaries and measurements on a fixed number of qubits. Alice applies unitaries in an attempt to maintain quantum channel capacity, while Eve applies measurements in an attempt to destroy it. By limiting the coherence generating or destroying operations available to each opponent, we determine Alice's coherence requirements. When Alice plays a random strategy aimed at mimicking generic monitored quantum dynamics, we discover a coherence-tuned phase transitions in entanglement and quantum channel capacity. We then derive a theorem giving the minimum coherence required by Alice in any successful strategy, and conclude by proving that coherence sets an upper bound on the code distance in any stabelizer quantum error correction codes. Such bounds provide a rigorous quantification of the coherence resource requirements for quantum communication and error correction.
```

## candidate-06 [channel-capacity] — ANNOTATED as quant-ph-0702059 (pass 30)

**Title:** Spin chains and channels with memory

**URL:** https://arxiv.org/abs/quant-ph/0702059

**Description:** Plenio, Virmani (2007). quant-ph. Channel capacity under correlated error mapped to critical behaviour in many-body physics; capacities can display phase-transition-like non-analyticity.

**Content extract (abstract):**

```
In most studies of the channel capacity of quantum channels, it is assumed that the errors in each use of the channel are independent. However, recent work has begun to investigate the effects of memory or correlations in the error. This work has led to speculation that interesting non-analytic behaviour may occur in the capacity. Motivated by these observations, we connect the study of channel capacities under correlated error to the study of critical behaviour in many-body physics. This connection enables us the techniques of many-body physics to either completely solve or understand qualitatively a number of interesting models of correlated error. The models can display analogous behaviour to associated many-body systems, including 'phase transitions'.
```

## candidate-07 [channel-capacity] — UNCONSUMED

**Title:** Locating Order-Disorder Phase Transition in a Cardiac System

**URL:** https://arxiv.org/abs/1708.03990

**Description:** Ashikaga, Asgari-Targhi (2017). q-bio.QM. Channel capacity, mutual information, and transfer entropy locate wavebreaks initiating ventricular fibrillation — capacity as a spatial predictor of an order-disorder transition in a driven dynamical system.

**Content extract (abstract):**

```
To prevent sudden cardiac death, predicting where in the cardiac system an order-disorder phase transition into ventricular fibrillation begins is as important as when it begins. We present a computationally efficient, information-theoretic approach to predicting the locations of wavebreaks that initiate fibrillation in a cardiac system where the order-disorder behavior is controlled by a single driving component, mimicking electrical misfiring from the pulmonary veins or the Purkinje fibers. Communication analysis between the driving component and each component of the system reveals that channel capacity, mutual information and transfer entropy can locate the wavebreaks. This approach is applicable to interventional therapies to prevent sudden death, as well as to a wide range of systems to mitigate or prevent imminent phase transitions.
```

## candidate-08 [ph-stability] — UNCONSUMED

**Title:** Categorification of persistent homology

**URL:** https://arxiv.org/abs/1205.3669

**Description:** Bubenik, Scott (2012). math.AT. Persistence modules as diagrams indexed by the reals; interleaving distance generalizes bottleneck distance; greatly generalized stability theorems.

**Content extract (abstract):**

```
We redevelop persistent homology (topological persistence) from a categorical point of view. The main objects of study are diagrams, indexed by the poset of real numbers, in some target category. The set of such diagrams has an interleaving distance, which we show generalizes the previously-studied bottleneck distance. To illustrate the utility of this approach, we greatly generalize previous stability results for persistence, extended persistence, and kernel, image and cokernel persistence. We give a natural construction of a category of interleavings of these diagrams, and show that if the target category is abelian, so is this category of interleavings.
```

## candidate-09 [ph-stability] — UNCONSUMED

**Title:** Galois Connections in Persistent Homology

**URL:** https://arxiv.org/abs/2201.06650

**Description:** Gulen, McCleary (2022). math.AT. Interleavings and matchings unified via Galois connections; Rota's theorem yields a substantially easier proof of bottleneck stability.

**Content extract (abstract):**

```
We present a new language for persistent homology in terms of Galois connections. This language has two main advantages over traditional approaches. First, it simplifies and unifies central concepts such as interleavings and matchings. Second, it provides access to Rota's Galois connection theorem -- a powerful tool with many potential applications in applied topology. To illustrate this, we use Rota's Galois connection theorem to give a substantially easier proof of the bottleneck stability theorem. Finally, we use this language to establish relationships between various notions of multiparameter persistence diagrams.
```

## candidate-10 [ph-stability] — UNCONSUMED

**Title:** On C0-persistent homology and trees

**URL:** https://arxiv.org/abs/2012.02634

**Description:** Perez (2020). math.AT. Tree construction identifying H0 persistence; quantitative Wasserstein stability theorem for Hölder functions; homological dimension bounds; applications to random fields.

**Content extract (abstract):**

```
In this paper we give a metric construction of a tree which correctly identifies connected components of superlevel sets of R-valued continuous functions f on X and show that it is possible to retrieve the H0-persistent diagram from this tree. We revisit the notion of homological dimension previously introduced by Schweinhart and give some bounds for the latter in terms of the upper-box dimension of X, thereby partially answering a question of the same author. We prove a quantitative version of the Wasserstein stability theorem valid for regular enough X and alpha-Hölder functions and discuss some applications of this theory to random fields and the topology of their superlevel sets.
```

## candidate-11 [ph-stability] — UNCONSUMED

**Title:** An isometry theorem for persistent homology of circle-valued functions

**URL:** https://arxiv.org/abs/2506.02999

**Description:** Broomhead, Pirashvili (2025). math.AT. Extends interleaving/bottleneck distances to circle-valued persistence; isometry theorem equating the two.

**Content extract (abstract):**

```
This paper explores persistence modules for circle-valued functions, presenting a new extension of the interleaving and bottleneck distances in this setting. We propose a natural generalisation of barcodes in terms of arcs on a geometric model associated to the derived category of quiver representations. The main result is an isometry theorem that establishes an equivalence between the interleaving distance and the bottleneck distance for circle-valued persistence modules.
```

## candidate-12 [ph-stability] — UNCONSUMED

**Title:** Persistent Homology and Applied Homotopy Theory

**URL:** https://arxiv.org/abs/2004.00738

**Description:** Carlsson (2020). math.AT. Survey: persistence modules, stability theorems for barcodes, generalized persistence, vectorization — candidate canonical reference for the Filtrations×Stability cell.

**Content extract (abstract):**

```
This paper is a survey of persistent homology, primarily as it is used in topological data analysis. It includes the theory of persistence modules, as well as stability theorems for persistence barcodes, generalized persistence, vectorization of persistence barcodes, as well as some applications.
```
