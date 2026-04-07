# SYNONYMS.md

## The Translation Table

Each row is a single abstract concept. Each column is a domain's name for it. Empty cells mean the domain doesn't use this concept — which is itself informative.

---

### Layer 0: The Algebraic Object

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| The space | Simplicial complex | Code complex / cellulation | State space / phase space | Neural manifold | Source alphabet / Poset of event combinations |
| Local constraint | Simplex inclusion | Stabilizer | Flow equation | Firing rate constraint | Entropy bound |
| Boundary operator | ∂ (simplicial); coboundary δ (Ripser/Bauer 2021) | ∂ (cellular) | — | ∂ on clique/nerve complex (Giusti, Curto & Itskov); directed ∂ on oriented simplices (Reimann); directed ∂ on TE-derived flag complex (Peek 2025) | Möbius function on poset (Sugiyama 2016) |
| Cycle | Kernel of ∂ | Error syndrome pattern | Periodic orbit | Co-firing pattern forming closed loop (Dabaghian) | — |
| Boundary | Image of ∂ | Trivial syndrome | Gradient flow | Trivial co-firing pattern (contractible) | — |
| Homology class | Persistent feature | Logical qubit / dynamically generated logical qubit (Floquet: emerges from periodic orbit, not any snapshot) | Attractor topology | Population topology (Giusti) / Cavity (Reimann) / Environment topology (Curto & Itskov) | — |
| Betti number | Feature count per dim | Logical qubit count | — | Obstacle count b₁ (Dabaghian) / Cavity count (Reimann) | — |
| Coefficient field | Usually ℝ or ℤ/2 | ℤ/2 or ℤ/p | ℝ (continuous) | ℝ | ℝ |

### Layer 1: Parameterization

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| The parameter | Filtration scale ε / energy threshold / dimension k (Berry et al. 2023) | Error rate p / correction rate κ / Chern number / filling fraction ν / measurement round r mod 3 (Floquet, Hastings-Haah 2021) | Coupling strength / bifurcation parameter / criticality m (Hawkes) / time (itinerancy epoch, Tsuda) | Stimulus / task condition / connectivity strength / EEG frequency band / quantile index τ (Dabney) / itinerancy epoch (Tsuda CI) | Channel capacity / training epoch / constraint density α / IB β / observation window t (finite-time MI) |
| What changes | Which simplices exist | Which errors are correctable / ISG S(r) (Floquet: instantaneous code changes each round) | Attractor topology | Neural representation geometry | Achievable rate / MI / PID atoms |
| Critical value | Persistent feature birth/death | Error threshold (~2.5%) / Zeno transition | Bifurcation point / attractor ruin transition (Tsuda CI) | Perceptual switch / cognitive state transition (Tsuda CI) | Capacity boundary / compression onset / SAT/UNSAT α_c ≈ 4.267 |
| The invariant that tracks it | Persistence diagram | Threshold curve | Bifurcation diagram | Betti number trajectory during learning (Dabaghian) / Cavity formation sequence (Reimann) | Rate-distortion curve / information plane trajectory |
| Robustness of the invariant | Stability theorem (bottleneck ≤ Hausdorff) | Threshold theorem (exp. suppression) / Zeno λ⁴/κ² | Structural stability | — | Channel coding theorem / MINE consistency |

### Layer 2: Matching / Assignment

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| What is matched | Diagram points (birth,death) / Cross-Barcode feature pairs (Barannikov 2021) | Syndrome defects / anyon pairs (fusion) / quasiparticle worldlines (braiding, Freedman-Kitaev 2001) / spacetime syndrome defects (Floquet: 2+1D matching, Hastings-Haah 2021) | Latent space positions (Hawkes) / lead-lag clusters / coupling functions (IC-PINN) | D1/D2 opponent pairs (quantile τ ↔ 1-τ) / HD vectors to centroids (ConformalHDC) / cortical vertices across subjects (Thual FUGW 2022) / MEG source dipoles across subjects (Janati MWE 2019) / neural population vectors across sessions (Lee HOT 2019) | Source symbols to channel symbols / query-key pairs (attention) / Fisher-Rao ↪ Wasserstein (Wong-Yang 2019) |
| Cost function | Bottleneck (L∞) or Wasserstein (Lp) | Edge weight in syndrome graph | Latent distance / cut imbalance | Cortical geodesic distance (Thual, Janati) / Wasserstein on neural firing distributions (Lee) / fused Wasserstein + Gromov-Wasserstein (Thual) | Distortion measure / Gromov-Wasserstein |
| Algorithm | Hungarian / auction | MWPM / Union-Find | Spectral clustering / Neural ODE attention | Sinkhorn (entropic OT) / generalized Sinkhorn (unbalanced OT, Janati) / ADMM + Sinkhorn (hierarchical OT, Lee) | Blahut-Arimoto / BP on factor graphs |
| What the solution means | Distance between topological signatures | Most likely error correction | Temporal ordering / cluster assignment | Inter-subject functional alignment (Thual) / group-level source localization (Janati) / cross-session neural decoder transfer (Lee) | Optimal code / martingale coupling |

### Layer 3: Composite Systems

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| Components | Marginal point clouds | Subsystem Hilbert spaces | Uncoupled systems | Brain regions | Independent sources |
| Joint object | Joint embedding | Tensor product space | Coupled system | Cross-region dynamics | Joint source |
| Independence | I_joint ≈ combo of I_X, I_Y | Product state | No coupling | No functional connectivity | Independence |
| Excess | Binding residual (R > 0) / MTop-Divergence (Cross-Barcode, Barannikov 2021) | Entanglement (non-separable) / interference (Barandes) | Emergent attractor topology / info transfer asymmetry (symmetry breaking) | Neural binding / synergistic PID / distributional code (Dabney) / consciousness Φ (Tononi IIT 3.0) / IPWT synergy / PhiID 16 atoms: 6 modes of integration (Mediano 2019) | Mutual information / synergy / higher-order interaction / k-body excess (PRL compression) / MMI synergy for Gaussians (Barrett 2015) |
| Detection method | PI subtraction + surrogate test | Entanglement witness / Born rule gap | Cross-correlation gap / entropy production / CCM convergence (Sugihara 2012) | Coherence / Granger / PID / PhiID (Mediano 2019) / quantile diversity / Phase TE (Lobier 2014: directed phase coupling) | I(X;Y) estimation / MINE / MI-NEE (triangulated) / Pythagorean KL decomposition / MMI PID (Barrett 2015) / continuous-time TE via kNN (Shorten 2021) |

### Layer 4: Null Models

| Concept | TDA | QEC | Dynamical Systems | Neuroscience | Information Theory |
|---------|-----|-----|-------------------|--------------|-------------------|
| What is destroyed | Phase coupling (surrogates) | Coherence (depolarizing channel) / Markovian memory (Born approx) | Temporal structure (shuffle, Theiler Alg 0) / phase correlations (Theiler Alg 1-2) / excitation (Poisson null) / symmetry (symmetry breaking) / stationarity (changepoints) | Neural correlation (trial shuffle) / directionality (undirected null) / mean-RPE assumption (Dabney) / alert state (fatigue GC) / oscillatory phase coupling (Phase TE surrogates, Lobier 2014) | Dependence (product distribution) / higher-order interactions / structure preservation (standard CL) / source-target temporal coupling (local permutation surrogates, Shorten 2021; source-time-shift shown to fail) |
| What is preserved | Power spectrum | State space dimension | Power spectrum (Theiler Alg 1) / power spectrum + amplitude distribution (Theiler Alg 2 AAFT) / event rates | Firing rates / degree sequence | Marginal distributions / lower-order terms |
| Null distribution | Surrogate binding scores / Universal empirical PH null (Vejdemo-Johansson 2018) / classical Monte Carlo dequantization (Berry et al. 2023) | Logical error rates under noise / integer QHE (Arovas-Zhang) / static subsystem code with 0 logical qubits (Floquet null, Hastings-Haah 2021) | Surrogate ensemble (Theiler 1992: shuffle / phase-randomized / AAFT) / Brownian motion limit (Hawkes) / Erdős-Rényi / constant-parameter PDE (CP-PINNs) / IID ordinal patterns / non-convergent cross-prediction (CCM, Sugihara 2012) | Shuffled test statistics / random networks / mean-RPE (Schultz model) / partitioned system (IIT Φ=0, Tononi 2014) | Random assignment energy / Poisson baseline / uniform reference (MI-NEE) / max entropy (Chicharro) |
| Significance | p < 0.05 (permutation) | Below threshold | Departure from Brownian / Lyapunov exponent / entropy production | p < 0.05 (permutation) / small-world excess / quantile asymmetry | MI > 0 / IB compression degree / exceed-average phenomenon |

---

## Notes on the Table

Empty cells are as important as filled ones. Dynamical systems rarely use matching. Information theory rarely uses boundary operators. The emptiness marks where the domains genuinely diverge rather than merely using different words.

Some filled cells are weaker than others. Calling a periodic orbit a "cycle" is a pun — it's a cycle in the flow, not in the chain complex. These false cognates are tracked in ANTISYNONYMS.md.
