# Queue batch-008 — arXiv foraging export, 2026-08-25

Fifth foraged batch (abstract-only provenance). Two groups:
**reservoir-gs** — reservoir computing as generalized synchronization; the
crown jewel is Grigoryeva-Hart-Ortega proving Takens embedding IS a
generalized synchronization (direct companion to the annotated 2409.08768
measure-theoretic Takens-via-OT — a Dynamics-side closure of that bridge);
plus conditional-Lyapunov stability conditions and pullback-dimension bounds.
**kuramoto** — synchronization-transition theory (order parameters, critical
exponents, finite-N bifurcation-vs-phase-transition distinctions that feed the
Null Hypothesis and Phase Transition rows).
Deduped by title vs batches 001-007; run the index-prose check regardless.
Consume per papers/INGESTION.md (<=3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [reservoir-gs] — UNCONSUMED

**Title:** Learning strange attractors with reservoir systems

**URL:** https://arxiv.org/abs/2108.05024

**Description:** Grigoryeva, Hart, Ortega (2021). math.DS. Takens' Embedding Theorem shown to be a special case of generalized synchronization in random linear state-space systems — embedding IS synchronization; topological conjugacy between reservoir dynamics and source system.

**Content extract (abstract):**

```
This paper shows that the celebrated Embedding Theorem of Takens is a particular case of a much more general statement according to which, randomly generated linear state-space representations of generic observations of an invertible dynamical system carry in their wake an embedding of the phase space dynamics into the chosen Euclidean state space. This embedding coincides with a natural generalized synchronization that arises in this setup and that yields a topological conjugacy between the state-space dynamics driven by the generic observations of the dynamical system and the dynamical system itself. This result provides additional tools for the representation, learning, and analysis of chaotic attractors and sheds additional light on the reservoir computing phenomenon that appears in the context of recurrent neural networks.
```

## candidate-02 [reservoir-gs] — UNCONSUMED

**Title:** Attractor reconstruction with reservoir computers: The effect of the reservoir's conditional Lyapunov exponents on faithful attractor reconstruction

**URL:** https://arxiv.org/abs/2401.00885

**Description:** Hart (2023). cs.LG/nlin.CD. Faithful attractor reconstruction requires the reservoir's largest conditional Lyapunov exponent to be significantly more negative than the target's most negative exponent — a quantitative stability condition on the reconstruction map.

**Content extract (abstract):**

```
Reservoir computing is a machine learning framework that has been shown to be able to replicate the chaotic attractor, including the fractal dimension and the entire Lyapunov spectrum, of the dynamical system on which it is trained. We quantitatively relate the generalized synchronization dynamics of a driven reservoir during the training stage to the performance of the trained reservoir computer at the attractor reconstruction task. We show that, in order to obtain successful attractor reconstruction and Lyapunov spectrum estimation, the largest conditional Lyapunov exponent of the driven reservoir must be significantly more negative than the most negative Lyapunov exponent of the target system. We also find that the maximal conditional Lyapunov exponent of the reservoir depends strongly on the spectral radius of the reservoir adjacency matrix, and therefore, for attractor reconstruction and Lyapunov spectrum estimation, small spectral radius reservoir computers perform better in general. Our arguments are supported by numerical examples on well-known chaotic systems.
```

## candidate-03 [reservoir-gs] — UNCONSUMED

**Title:** On the dimension of pullback attractors in recurrent neural networks

**URL:** https://arxiv.org/abs/2501.11357

**Description:** Fadera (2025). math.DS. Box-counting dimension of the reservoir's pullback attractor bounded above by the input-sequence space dimension — effective low-dimensionality explains attractor-reconstruction success.

**Content extract (abstract):**

```
Recurrent neural networks trained via the reservoir computing paradigm have demonstrated remarkable success in learning and reconstructing attractors from chaotic systems, often replicating quantities such as Lyapunov exponents and fractal dimensions. It has recently been conjectured that this is because the reservoir computer embeds the dynamics of the chaotic system in its state space before learning. This conjecture has been established for reservoir computers with linear activation functions and remains open for more general reservoir systems. In this work, we employ a non-autonomous dynamical systems approach to establish an upper bound for the box-counting dimension of the pullback attractor, a subset of the reservoir state space that is approximated during training and prediction phases. We prove that the box-counting dimension of the pullback attractor is bounded above by the box-counting dimension of the space of input sequences with respect to the product topology. In particular, for input sequences originating from an Nin-dimensional smooth dynamical system or their generic continuously differentiable observations, the box-counting dimension of the pullback attractor is bounded above by Nin. The results obtained here highlight the fact that, while a reservoir computer may possess a very high-dimensional state space, it exhibits effective low-dimensional dynamics. Our findings also partly explain why reservoir computers are successful in tasks such as attractor reconstruction and the computation of dynamic invariants like Lyapunov exponents and fractal dimensions.
```

## candidate-04 [reservoir-gs] — UNCONSUMED

**Title:** Learning Continuous Chaotic Attractors with a Reservoir Computer

**URL:** https://arxiv.org/abs/2110.08631

**Description:** Smith, Kim, Lu, Bassett (2021). cs.NE. RC trained on isolated attractor examples abstracts a continuum of attractors, quantified by an extra zero Lyapunov exponent — abstraction as differentiable generalized synchronization.

**Content extract (abstract):**

```
Neural systems are well known for their ability to learn and store information as memories. Even more impressive is their ability to abstract these memories to create complex internal representations, enabling advanced functions such as the spatial manipulation of mental representations. While recurrent neural networks (RNNs) are capable of representing complex information, the exact mechanisms of how dynamical neural systems perform abstraction are still not well-understood, thereby hindering the development of more advanced functions. Here, we train a 1000-neuron RNN -- a reservoir computer (RC) -- to abstract a continuous dynamical attractor memory from isolated examples of dynamical attractor memories. Further, we explain the abstraction mechanism with new theory. By training the RC on isolated and shifted examples of either stable limit cycles or chaotic Lorenz attractors, the RC learns a continuum of attractors, as quantified by an extra Lyapunov exponent equal to zero. We propose a theoretical mechanism of this abstraction by combining ideas from differentiable generalized synchronization and feedback dynamics. Our results quantify abstraction in simple neural systems, enabling us to design artificial RNNs for abstraction, and leading us towards a neural basis of abstraction.
```

## candidate-05 [reservoir-gs] — UNCONSUMED

**Title:** Model-free inference of unseen attractors: Reconstructing phase space features from a single noisy trajectory using reservoir computing

**URL:** https://arxiv.org/abs/2108.04074

**Description:** Röhm, Gauthier, Fischer (2021). cs.LG. Trained RC predicts co-existing attractors never seen in training from a single noisy trajectory — phase-space generalization beyond the sampled basin.

**Content extract (abstract):**

```
Reservoir computers are powerful tools for chaotic time series prediction. They can be trained to approximate phase space flows and can thus both predict future values to a high accuracy, as well as reconstruct the general properties of a chaotic attractor without requiring a model. In this work, we show that the ability to learn the dynamics of a complex system can be extended to systems with co-existing attractors, here a 4-dimensional extension of the well-known Lorenz chaotic system. We demonstrate that a reservoir computer can infer entirely unexplored parts of the phase space: a properly trained reservoir computer can predict the existence of attractors that were never approached during training and therefore are labelled as unseen. We provide examples where attractor inference is achieved after training solely on a single noisy trajectory.
```

## candidate-06 [reservoir-gs] — UNCONSUMED

**Title:** Robust quantum reservoir computers for forecasting chaotic dynamics: generalized synchronization and stability

**URL:** https://arxiv.org/abs/2506.22335

**Description:** Ahmed, Tennie, Magri (2025). quant-ph/cs.LG. QRCs formulated as generalized-synchronization systems; GS=ESP criterion (generalized synchronization iff echo state property); noise dissipation enhances robustness.

**Content extract (abstract):**

```
We show that recurrent quantum reservoir computers (QRCs) and their recurrence-free architectures (RF-QRCs) are robust tools for learning and forecasting chaotic dynamics from time-series data. First, we formulate and interpret quantum reservoir computers as coupled dynamical systems, where the reservoir acts as a response system driven by training data; in other words, quantum reservoir computers are generalized-synchronization (GS) systems. Second, we show that quantum reservoir computers can learn chaotic dynamics and their invariant properties, such as Lyapunov spectra, attractor dimensions, and geometric properties such as the covariant Lyapunov vectors. This analysis is enabled by deriving the Jacobian of the quantum reservoir update. Third, by leveraging tools from generalized synchronization, we provide a method for designing robust quantum reservoir computers. We propose the criterion GS=ESP: GS implies the echo state property (ESP), and vice versa. We analytically show that RF-QRCs, by design, fulfill GS=ESP. Finally, we analyze the effect of simulated noise. We find that dissipation from noise enhances the robustness of quantum reservoir computers. Numerical verifications on systems of different dimensions support our conclusions. This work opens opportunities for designing robust quantum machines for chaotic time series forecasting on near-term quantum hardware.
```

## candidate-07 [kuramoto] — UNCONSUMED

**Title:** A mesoscopic theory for stochastic coupled oscillators

**URL:** https://arxiv.org/abs/2407.02416

**Description:** Buendía (2024). cond-mat.stat-mech. Mesoscopic finite-N description of stochastic Kuramoto: first closed expressions for the stochastic order parameter, multiplicative ensemble fluctuations, and synchronization-transition critical exponents.

**Content extract (abstract):**

```
The celebrated Ott-Antonsen ansatz for coupled oscillators provides a useful framework to work with deterministic systems in the thermodynamic limit, but remains just an approximation for stochastic models. In this paper, I construct a general mesoscopic description of finite-sized populations of stochastic coupled oscillators and apply it to study the stochastic Kuramoto model. From such a mesoscopic description it is possible to obtain the natural, multiplicative fluctuations of the oscillator ensemble. The analysis allows one to derive highly accurate, closed expressions for the stochastic Kuramoto model's order parameter for the first time. Moreover, it is possible to get novel insights into the system's fluctuations and the synchronization transition's critical exponents which were inaccessible before.
```

## candidate-08 [kuramoto] — UNCONSUMED

**Title:** Extreme Synchronization Transitions

**URL:** https://arxiv.org/abs/2505.10114

**Description:** Lee, Kuklinski, Timme (2025). nlin.AO. Finite-N transitions that mimic explosive phase transitions but are multi-dimensional bifurcations: order parameter jumps from ~N^{-1/2} to ~1 at critical coupling — a sharp test case for transition-vs-bifurcation nulls.

**Content extract (abstract):**

```
Across natural and human-made systems, transition points mark sudden changes of order and are thus key to understanding overarching system features. Motivated by recent experimental observations, we here uncover an intriguing class of transitions in coupled oscillators, extreme synchronization transitions, from asynchronous disordered states to synchronous states with almost completely ordered phases. Whereas such a transition appears like discontinuous or explosive phase transitions, it exhibits markedly distinct features. First, the transition occurs already in finite systems of N units and so constitutes an intriguing bifurcation of multi-dimensional systems rather than a genuine phase transition that emerges in the thermodynamic limit N to infinity only. Second, the synchronization order parameter jumps from moderate values of the order of N^(-1/2) to values extremely close to 1, its theoretical maximum, immediately upon crossing a critical coupling strength. We analytically explain the mechanisms underlying such extreme transitions in coupled complexified Kuramoto oscillators. Extreme transitions may similarly occur across other systems of coupled oscillators as well as in certain percolation processes. In applications, their occurrence impacts our ability of ensuring or preventing strong forms of ordering, for instance in biological and engineered systems.
```

## candidate-09 [kuramoto] — UNCONSUMED

**Title:** Synchronization transition of heterogeneously coupled oscillators on scale-free networks

**URL:** https://arxiv.org/abs/cond-mat/0606048

**Description:** Oh, Lee, Kahng, Kim (2006). cond-mat.stat-mech. Mean-field phase diagram of degree-dependent-coupling Kuramoto on scale-free networks: eight transition behaviors, critical exponents, cluster-formation view via generating functions.

**Content extract (abstract):**

```
We investigate the synchronization transition of the modified Kuramoto model where the oscillators form a scale-free network with degree exponent lambda. An oscillator of degree k_i is coupled to its neighboring oscillators with asymmetric and degree-dependent coupling in the form of J k_i^(eta-1). By invoking the mean-field approach, we determine the synchronization transition point J_c, which is zero (finite) when eta > lambda-2 (eta < lambda-2). We find eight different synchronization transition behaviors depending on the values of eta and lambda, and derive the critical exponents associated with the order parameter and the finite-size scaling in each case. The synchronization transition is also studied from the perspective of cluster formation of synchronized vertices. The cluster-size distribution and the largest cluster size as a function of the system size are derived for each case using the generating function technique. Our analytic results are confirmed by numerical simulations.
```

## candidate-10 [kuramoto] — UNCONSUMED

**Title:** Machine learning approaches for Kuramoto coupled oscillator systems

**URL:** https://arxiv.org/abs/2109.08918

**Description:** Song, Choi, Kahng (2021). cond-mat.stat-mech. ML determination of hybrid-synchronization transition point and criticality; network-structure inference from chaotic patterns — learned order parameters as transition detectors.

**Content extract (abstract):**

```
Recently, there has been significant advancement in the machine learning (ML) approach and its application to diverse systems ranging from complex to quantum systems. As one of such systems, a coupled-oscillators system exhibits intriguing collective behaviors, synchronization phase transitions, chaotic behaviors and so on. Even though traditional approaches such as analytical and numerical methods enable to understand diverse properties of such systems, some properties still remain unclear. Here, we applied the ML approach to such systems particularly described by the Kuramoto model, with the aim of resolving the following intriguing problems, namely determination of the transition point and criticality of a hybrid synchronization transition; understanding network structures from chaotic patterns; and comparison of ML algorithms for the prediction of future chaotic behaviors. The proposed method is expected to be useful for further problems such as understanding a neural network structure from electroencephalogram signals.
```

## candidate-11 [kuramoto] — UNCONSUMED

**Title:** Kuramoto dynamics in Hamiltonian systems

**URL:** https://arxiv.org/abs/1305.1742

**Description:** Witthaut, Timme (2013). nlin.CD. Conservative Hamiltonian system whose action-angle dynamics exactly reproduces Kuramoto on invariant manifolds; synchronization transition = transverse instability of the Hamiltonian action dynamics.

**Content extract (abstract):**

```
The Kuramoto model constitutes a paradigmatic model for the dissipative collective dynamics of coupled oscillators, characterizing in particular the emergence of synchrony. Here we present a classical Hamiltonian (and thus conservative) system with 2N state variables that in its action-angle representation exactly yields Kuramoto dynamics on N-dimensional invariant manifolds. We show that the synchronization transition on a Kuramoto manifold emerges where the transverse Hamiltonian action dynamics becomes unstable. The uncovered Kuramoto dynamics in Hamiltonian systems thus distinctly links dissipative to conservative dynamics.
```
