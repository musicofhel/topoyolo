# SYNONYMS.md

## The Translation Table

Each row is a single abstract concept. Each column is a domain's name for it. Empty cells mean the domain doesn't use this concept — which is itself informative.

---

### Layer 0: The Algebraic Object

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| The space | Simplicial complex | Code complex / cellulation | State space / phase space | Neural manifold | Source alphabet / Poset of event combinations |
| Local constraint | Simplex inclusion | Stabilizer | Flow equation | Firing rate constraint | Entropy bound |
| Boundary operator | ∂ (simplicial) | ∂ (cellular) | — | — | Möbius function on poset (Sugiyama 2016) |
| Cycle | Kernel of ∂ | Error syndrome pattern | Periodic orbit | Recurrent activity pattern | — |
| Boundary | Image of ∂ | Trivial syndrome | Gradient flow | — | — |
| Homology class | Persistent feature | Logical qubit | Attractor topology | Population topology (Giusti) | — |
| Betti number | Feature count per dim | Logical qubit count | — | Intrinsic dimension (related) | — |
| Coefficient field | Usually ℝ or ℤ/2 | ℤ/2 or ℤ/p | ℝ (continuous) | ℝ | ℝ |

### Layer 1: Parameterization

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| The parameter | Filtration scale ε / energy threshold | Error rate p / correction rate κ / Chern number | Coupling strength / bifurcation parameter / criticality m (Hawkes) | Stimulus / task condition / connectivity strength | Channel capacity / training epoch / constraint density α / IB β |
| What changes | Which simplices exist | Which errors are correctable | Attractor topology | Neural representation geometry | Achievable rate / MI / PID atoms |
| Critical value | Persistent feature birth/death | Error threshold (~2.5%) / Zeno transition | Bifurcation point | Perceptual switch | Capacity boundary / compression onset / SAT/UNSAT α_c ≈ 4.267 |
| The invariant that tracks it | Persistence diagram | Threshold curve | Bifurcation diagram | — | Rate-distortion curve / information plane trajectory |
| Robustness of the invariant | Stability theorem (bottleneck ≤ Hausdorff) | Threshold theorem (exp. suppression) / Zeno λ⁴/κ² | Structural stability | — | Channel coding theorem / MINE consistency |

### Layer 2: Matching / Assignment

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| What is matched | Diagram points (birth,death) | Syndrome defects | Latent space positions (Hawkes) / lead-lag clusters | — | Source symbols to channel symbols / query-key pairs (attention) |
| Cost function | Bottleneck (L∞) or Wasserstein (Lp) | Edge weight in syndrome graph | Latent distance / cut imbalance | — | Distortion measure / Gromov-Wasserstein |
| Algorithm | Hungarian / auction | MWPM / Union-Find | Spectral clustering / Neural ODE attention | — | Blahut-Arimoto / BP on factor graphs |
| What the solution means | Distance between topological signatures | Most likely error correction | Temporal ordering / cluster assignment | — | Optimal code / martingale coupling |

### Layer 3: Composite Systems

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| Components | Marginal point clouds | Subsystem Hilbert spaces | Uncoupled systems | Brain regions | Independent sources |
| Joint object | Joint embedding | Tensor product space | Coupled system | Cross-region dynamics | Joint source |
| Independence | I_joint ≈ combo of I_X, I_Y | Product state | No coupling | No functional connectivity | Independence |
| Excess | Binding residual (R > 0) | Entanglement (non-separable) | Emergent attractor topology | Neural binding / synergistic PID | Mutual information / synergy / higher-order interaction |
| Detection method | PI subtraction + surrogate test | Entanglement witness | — | Coherence / Granger / PID | I(X;Y) estimation / MINE / Pythagorean KL decomposition |

### Layer 4: Null Models

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| What is destroyed | Phase coupling (surrogates) | Coherence (depolarizing channel) | Temporal structure (shuffle) / excitation (Poisson null) | Neural correlation (trial shuffle) / directionality (undirected null) | Dependence (product distribution) / higher-order interactions |
| What is preserved | Power spectrum | State space dimension | Marginal statistics / event rates | Firing rates / degree sequence | Marginal distributions / lower-order terms |
| Null distribution | Surrogate binding scores | Logical error rates under noise | Brownian motion limit (Hawkes) / Erdős-Rényi | Shuffled test statistics / random networks | Random assignment energy / Poisson baseline |
| Significance | p < 0.05 (permutation) | Below threshold | Departure from Brownian / Lyapunov exponent | p < 0.05 (permutation) / small-world excess | MI > 0 / IB compression degree |

---

## Notes on the Table

Empty cells are as important as filled ones. Dynamical systems rarely use matching. Information theory rarely uses boundary operators. The emptiness marks where the domains genuinely diverge rather than merely using different words.

Some filled cells are weaker than others. Calling a periodic orbit a "cycle" is a pun — it's a cycle in the flow, not in the chain complex. These false cognates are tracked in ANTISYNONYMS.md.
