# Queue batch-011 — arXiv foraging export, 2026-08-25

Eighth foraged batch (abstract-only provenance). Both groups arrive with
BUILT-IN claim-vs-null structure per the corpus's claim-vs-refutation rule:
**fep** — Markov-blanket/free-energy formalism (Friston's canonical monograph
+ the Biehl-Pollock-Kanai technical critique that disproves the original free
energy lemma by counterexample — annotate as a PAIR; plus dual-aspect
information geometry and one triage-candidate DL survey);
**soc** — neural self-organized criticality (Plenz's affirmative review vs
Touboul-Destexhe's spurious-power-law methodological null vs Dehghani's
empirical refutation across cat/monkey/human — a THREE-WAY structured
disagreement, plus oscillation-coexistence and subsampling-artifact angles).
Deduped by title vs batches 001-010; run the index-prose check regardless.
Consume per papers/INGESTION.md (<=3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [fep] — ANNOTATED as 1906.10184

**Title:** A free energy principle for a particular physics

**URL:** https://arxiv.org/abs/1906.10184

**Description:** Friston (2019). q-bio.NC. The canonical formal monograph: Markov blankets as recursive conditional-independence structure; internal states acquire an information geometry interpretable as inference about external states — joint-vs-marginal as a physics of 'things'.

**Content extract (abstract):**

```
This monograph attempts a theory of every 'thing' that can be distinguished from other things in a statistical sense. The ensuing statistical independencies, mediated by Markov blankets, speak to a recursive composition of ensembles (of things) at increasingly higher spatiotemporal scales. This decomposition provides a description of small things; e.g., quantum mechanics - via the Schrodinger equation, ensembles of small things - via statistical mechanics and related fluctuation theorems, through to big things - via classical mechanics. These descriptions are complemented with a Bayesian mechanics for autonomous or active things. Although this work provides a formulation of every thing, its main contribution is to examine the implications of Markov blankets for self-organisation to nonequilibrium steady-state. In brief, we recover an information geometry and accompanying free energy principle that allows one to interpret the internal states of something as representing or making inferences about its external states. The ensuing Bayesian mechanics is compatible with quantum, statistical and classical mechanics and may offer a formal description of lifelike particles.
```

## candidate-02 [fep] — ANNOTATED as 2001.06408

**Title:** A Technical Critique of Some Parts of the Free Energy Principle

**URL:** https://arxiv.org/abs/2001.06408

**Description:** Biehl, Pollock, Kanai (2020). q-bio.NC. The paired null: Markov-blanket definitions across FEP works are non-equivalent; the original free energy lemma is disproven by counterexample; the Bayesian-inference interpretation hinges on an unjustified equality — annotate as Friston's counterweight per the corpus claim-vs-refutation rule.

**Content extract (abstract):**

```
We summarize the original formulation of the free energy principle, and highlight some technical issues. We discuss how these issues affect related results involving generalised coordinates and, where appropriate, mention consequences for and reveal, up to now unacknowledged, differences to newer formulations of the free energy principle. In particular, we reveal that various definitions of the "Markov blanket" proposed in different works are not equivalent. We show that crucial steps in the free energy argument which involve rewriting the equations of motion of systems with Markov blankets, are not generally correct without additional (previously unstated) assumptions. We prove by counterexample that the original free energy lemma, when taken at face value, is wrong. We show further that this free energy lemma, when it does hold, implies equality of variational density and ergodic conditional density. The interpretation in terms of Bayesian inference hinges on this point, and we hence conclude that it is not sufficiently justified. Additionally, we highlight that the variational densities presented in newer formulations of the free energy principle and lemma are parameterised by different variables than in older works, leading to a substantially different interpretation of the theory. Note that we only highlight some specific problems in the discussed publications. These problems do not rule out conclusively that the general ideas behind the free energy principle are worth pursuing.
```

## candidate-03 [fep] — UNCONSUMED

**Title:** Neural and phenotypic representation under the free-energy principle

**URL:** https://arxiv.org/abs/2008.03238

**Description:** Ramstead, Hesp, Tschantz, Smith, Constant, Friston (2020). q-bio.NC. Dual-aspect information geometry from Markovian structure: intrinsic geometry of internal-state trajectories + extrinsic geometry encoding beliefs about external states; neuronal packet hypothesis with simulations.

**Content extract (abstract):**

```
The aim of this paper is to leverage the free-energy principle and its corollary process theory, active inference, to develop a generic, generalizable model of the representational capacities of living creatures; that is, a theory of phenotypic representation. Given their ubiquity, we are concerned with distributed forms of representation (e.g., population codes), whereby patterns of ensemble activity in living tissue come to represent the causes of sensory input or data. The active inference framework rests on the Markov blanket formalism, which allows us to partition systems of interest, such as biological systems, into internal states, external states, and the blanket (active and sensory) states that render internal and external states conditionally independent of each other. In this framework, the representational capacity of living creatures emerges as a consequence of their Markovian structure and nonequilibrium dynamics, which together entail a dual-aspect information geometry. This entails a modest representational capacity: internal states have an intrinsic information geometry that describes their trajectory over time in state space, as well as an extrinsic information geometry that allows internal states to encode (the parameters of) probabilistic beliefs about (fictive) external states. Building on this, we describe here how, in an automatic and emergent manner, information about stimuli can come to be encoded by groups of neurons bound by a Markov blanket; what is known as the neuronal packet hypothesis. As a concrete demonstration of this type of emergent representation, we present numerical simulations showing that self-organizing ensembles of active inference agents sharing the right kind of probabilistic generative model are able to encode recoverable information about a stimulus array.
```

## candidate-04 [fep] — UNCONSUMED

**Title:** The Free Energy Principle for Perception and Action: A Deep Learning Perspective

**URL:** https://arxiv.org/abs/2207.06415

**Description:** Mazzaglia, Verbelen, Çatal, Dhoedt (2022). cs.LG. Deep-learning realization survey of active inference (variational inference + amortized planning) — triage candidate: may be an application survey rather than machine-bearing.

**Content extract (abstract):**

```
The free energy principle, and its corollary active inference, constitute a bio-inspired theory that assumes biological agents act to remain in a restricted set of preferred states of the world, i.e., they minimize their free energy. Under this principle, biological agents learn a generative model of the world and plan actions in the future that will maintain the agent in an homeostatic state that satisfies its preferences. This framework lends itself to being realized in silico, as it comprehends important aspects that make it computationally affordable, such as variational inference and amortized planning. In this work, we investigate the tool of deep learning to design and realize artificial agents based on active inference, presenting a deep-learning oriented presentation of the free energy principle, surveying works that are relevant in both machine learning and active inference areas, and discussing the design choices that are involved in the implementation process. This manuscript probes newer perspectives for the active inference framework, grounding its theoretical aspects into more pragmatic affairs, offering a practical guide to active inference newcomers and a starting point for deep learning practitioners that would like to investigate implementations of the free energy principle.
```

## candidate-05 [soc] — UNCONSUMED

**Title:** Self-Organized Criticality in the Brain

**URL:** https://arxiv.org/abs/2102.09124

**Description:** Plenz, Ribeiro, Miller, Kells, Vakili, Capek (2021). q-bio.NC. The affirmative case: -3/2 avalanche power laws, branching parameter 1, nested oscillations, E/I + dopamine as control parameters — layered cortex self-organizing toward a 2nd-order phase transition.

**Content extract (abstract):**

```
Self-organized criticality (SOC) refers to the ability of complex systems to evolve towards a 2nd-order phase transition at which interactions between system components lead to scale-invariant events beneficial for system performance. For the last two decades, considerable experimental evidence accumulated that the mammalian cortex with its diversity in cell types and connections might exhibit SOC. Here we review experimental findings of isolated, layered cortex preparations to self-organize towards four dynamical motifs identified in the cortex in vivo: up-states, oscillations, neuronal avalanches, and coherence potentials. During up-states, the synchronization observed for nested theta/gamma-oscillations embeds scale-invariant neuronal avalanches that exhibit robust power law scaling in size with a slope of -3/2 and a critical branching parameter of 1. This dynamical coordination, tracked in the local field potential (nLFP) and pyramidal neuron activity using 2-photon imaging, emerges autonomously in superficial layers of organotypic cortex cultures and acute cortex slices, is homeostatically regulated, displays separation of time scales, and reveals unique size vs. quiet time dependencies. A threshold operation identifies coherence potentials; avalanches that in addition maintain the precise time course of propagated synchrony. Avalanches emerge under conditions of external driving. Control parameters are established by the balance of excitation and inhibition (E/I) and the neuromodulator dopamine. This rich dynamical repertoire is not observed in dissociated cortex cultures, which lack cortical layers and exhibit dynamics similar to a 1st-order phase transition. The precise interactions between up-states, nested oscillations, avalanches, and coherence potentials in superficial cortical layers provide compelling evidence for SOC in the brain.
```

## candidate-06 [soc] — UNCONSUMED

**Title:** Can power-law scaling and neuronal avalanches arise from stochastic dynamics?

**URL:** https://arxiv.org/abs/0910.0805

**Description:** Touboul, Destexhe (2009). nlin.AO. The methodological null: thresholded stochastic processes generically produce apparent power laws that fail Kolmogorov-Smirnov scrutiny; surrogate signals reproduce the scaling — log-log regression is not evidence of SOC.

**Content extract (abstract):**

```
The presence of self-organized criticality in biology is often evidenced by a power-law scaling of event size distributions, which can be measured by linear regression on logarithmic axes. We show here that such a procedure does not necessarily mean that the system exhibits self-organized criticality. We first provide an analysis of multisite local field potential (LFP) recordings of brain activity and show that event size distributions defined as negative LFP peaks can be close to power-law distributions. However, this result is not robust to change in detection threshold, or when tested using more rigorous statistical analyses such as the Kolmogorov-Smirnov test. Similar power-law scaling is observed for surrogate signals, suggesting that power-law scaling may be a generic property of thresholded stochastic processes. We next investigate this problem analytically, and show that, indeed, stochastic processes can produce spurious power-law scaling without the presence of underlying self-organized criticality. However, this power-law is only apparent in logarithmic representations, and does not survive more rigorous analysis such as the Kolmogorov-Smirnov test. The same analysis was also performed on an artificial network known to display self-organized criticality. In this case, both the graphical representations and the rigorous statistical analysis reveal with no ambiguity that the avalanche size is distributed as a power-law. We conclude that logarithmic representations can lead to spurious power-law scaling induced by the stochastic nature of the phenomenon. This apparent power-law scaling does not constitute a proof of self-organized criticality, which should be demonstrated by more stringent statistical tests.
```

## candidate-07 [soc] — UNCONSUMED

**Title:** Avalanche analysis from multi-electrode ensemble recordings in cat, monkey and human cerebral cortex during wakefulness and sleep

**URL:** https://arxiv.org/abs/1203.0738

**Description:** Dehghani, Hatsopoulos, Haga, Parker, Greger, Halgren, Cash, Destexhe (2012). q-bio.NC. The empirical null: unit-defined avalanches scale exponentially not power-law across cat/monkey/human, wake and sleep; CDF-based tests reject the apparent nLFP power laws; bi-exponential fits win.

**Content extract (abstract):**

```
Self-organized critical states are found in many natural systems, from earthquakes to forest fires, they have also been observed in neural systems, particularly, in neuronal cultures. However, the presence of critical states in the awake brain remains controversial. Here, we compared avalanche analyses performed on different in vivo preparations during wakefulness, slow-wave sleep and REM sleep, using high-density electrode arrays in cat motor cortex (96 electrodes), monkey motor cortex and premotor cortex and human temporal cortex (96 electrodes) in epileptic patients. In neuronal avalanches defined from units (up to 160 single units), the size of avalanches never clearly scaled as power-law, but rather scaled exponentially or displayed intermediate scaling. We also analyzed the dynamics of local field potentials (LFPs) and in particular LFP negative peaks (nLFPs) among the different electrodes (up to 96 sites in temporal cortex or up to 128 sites in adjacent motor and pre-motor cortices). In this case, the avalanches defined from nLFPs displayed power-law scaling in double log representations, as reported previously in monkey. However, avalanche defined as positive LFP (pLFP) peaks, which are less directly related to neuronal firing, also displayed apparent power-law scaling. Closer examination of this scaling using more reliable cumulative distribution functions (CDF) and other rigorous statistical measures, did not confirm power-law scaling. The same pattern was seen for cats, monkey and human, as well as for different brain states of wakefulness and sleep. We also tested other alternative distributions. Multiple exponential fitting yielded optimal fits of the avalanche dynamics with bi-exponential distributions. Collectively, these results show no clear evidence for power-law scaling or self-organized critical states in the awake and sleeping brain of mammals, from cat to man.
```

## candidate-08 [soc] — UNCONSUMED

**Title:** Coexistence of scale invariant and rhythmic behavior in self-organized criticality

**URL:** https://arxiv.org/abs/1807.07213

**Description:** Moosavi, Montakhab, Valizadeh (2018). cond-mat.dis-nn. Oscillatory perturbation of the Zhang model yields rhythms embedded in scale-free avalanches; optimal oscillation amplification AT the critical point — reconciles the 'theoretically incompatible' criticality + oscillations (links to the annotated Sekizawa ECoG entry).

**Content extract (abstract):**

```
Scale-free behavior as well as oscillations are frequently observed in the activity of many natural systems. One important example is the cortical tissues of mammalian brain where both phenomena are simultaneously observed. Rhythmic oscillations as well as critical (scale-free) dynamics are thought to be important, but theoretically incompatible, features of a healthy brain. Motivated by the above, we study the possibility of coexistence of scale-free avalanches along with rhythmic behavior within the framework of self-organized criticality. In particular, we add an oscillatory perturbation to local threshold condition of the continuous Zhang model and characterize the subsequent activity of the system. We observe regular oscillations embedded in well-defined avalanches which exhibit scale-free size and duration in line with observed neuronal avalanches. The average amplitude of such oscillations are shown to decrease with increasing frequency consistent with real brain oscillations. Furthermore, it is shown that optimal amplification of oscillations occur at the critical point, further providing evidence for functional advantages of criticality.
```

## candidate-09 [soc] — UNCONSUMED

**Title:** Critical Avalanches and Subsampling in Map-based Neural Networks

**URL:** https://arxiv.org/abs/1209.3271

**Description:** Girardi-Schappo, Kinouchi, Tragtenberg (2012). cond-mat.dis-nn. Synaptic noise as the mechanism driving critical avalanches in map-based networks; explicit subsampling analysis — the measurement-artifact angle on experimental SOC claims.

**Content extract (abstract):**

```
We investigate the synaptic noise as a novel mechanism for creating critical avalanches in the activity of neural networks. We model neurons and chemical synapses by dynamical maps with a uniform noise term in the synaptic coupling. An advantage of utilizing maps is that the dynamical properties (action potential profile, excitability properties, post synaptic potential summation etc.) are not imposed to the system, but occur naturally by solving the system equations. We discuss the relevant neuronal and synaptic properties to achieve the critical state. We verify that networks of excitatory by rebound neurons with fast synapses present power law avalanches. We also discuss the measuring of neuronal avalanches by subsampling our data, shedding light on the experimental search for Self-Organized Criticality in neural networks.
```
