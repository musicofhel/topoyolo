# Composite Systems (Joint-vs-Marginal Excess)

Papers instantiating the **joint-vs-marginal** abstract machine: detecting structure in composite systems that is absent from components. This includes entanglement, binding, synergy, mutual information, and integrated information.

The shared pattern: given components A and B, measure some property P of the joint system (A,B) and compare it to the combination of P(A) and P(B) separately. The excess P(A,B) - f(P(A), P(B)) > 0 signals genuine composite structure.

---

## Information Theory

### Belghazi et al. (2018) — MINE
MI as D_KL(P_XZ || P_X ⊗ P_Z). Neural estimator using Donsker-Varadhan dual. Joint-vs-marginal excess IS the paper's core object. Full annotation: `by-domain/information_theory.md`.

### Wickstrøm et al. (2019) — Information Plane via Rényi Entropy
I(X;T) and I(T;Y) at each hidden layer, tracked across training epochs. Also instantiates parameterized homology. Full annotation: `by-domain/information_theory.md`.

### Tax, Mediano & Shanahan (2017) — PID of Generative NNs
Synergy as the joint-vs-marginal excess in PID. Tracks synergistic, redundant, and unique information atoms through RBM training. Full annotation: `by-domain/information_theory.md`.

### Chwilka & Karbowski (2024) — Lognormal MI
Exact MI for lognormal distributions. MI can diverge at finite variance — infinite joint-vs-marginal excess. Full annotation: `by-domain/information_theory.md`.

### Mézard & Mora (2008) — Constraint Satisfaction
Factor graphs as generalized chain complexes. Solution-space shattering at α_c as topological phase transition. Also instantiates chain complex, matching, stability, null hypothesis. Full annotation: `by-domain/information_theory.md`.

### Sugiyama, Nakahara & Tsuda (2016) — Information Decomposition on Structured Space
Pythagorean theorem for KL divergence on posets decomposes interactions by order. Higher-order interactions = joint-vs-marginal excess at each level. Most algebraically rigorous treatment of the decomposition. Full annotation: `by-domain/information_theory.md`.

### Geiger (2021) — Information Plane Review
Surveys joint-vs-marginal (MI) estimation across architectures. Distinguishes geometric from information-theoretic compression. Full annotation: `by-domain/information_theory.md`.

### Jónsson et al. (2020) — DNN Convergence with MI Regularization
MINE-estimated I(X;T) as regularizer. Confirms compression phase in VGG-16. MI-based loss stabilizes training. Full annotation: `by-domain/information_theory.md`.

---

## TDA / Mathematical Physics

### Kanjamapornkul, Pincak, Bartos (2020) — Cohomology Theory for Financial Time Series
Chern-Simons currents arise from the interaction of trader behavior fields (Yang-Mills). The current measures a geometric phase absent from individual trader actions — arbitrage as joint-vs-marginal excess. The Wilson loop path integral over interacting trader paths detects structure in the composite (bid-ask pair) that is absent from each side alone. Full annotation: `by-domain/tda.md`.

*(See also inbox for ATT binding residual)*

## Mathematical Finance

### Bayraktar & Zhou (2017) — Model-Independent Pricing via Optimal Transport
The entire framework measures the gap between what marginal distributions determine and what the joint (martingale coupling) allows. Super-hedging price optimized over the set M of all martingale measures with given marginals = worst-case joint-vs-marginal excess. Full annotation: `by-domain/dynamical_systems.md`.

## Optimal Transport

### Bunne, Alvarez-Melis, Krause, Jegelka (2019) — Gromov-Wasserstein GANs
GW distance captures relational structure invariant to ambient dimension/rotation — detecting structure in RELATIONSHIPS between points (joint, pairwise) absent from marginal (pointwise) descriptions. Full annotation: `by-domain/dynamical_systems.md`.

## QEC

*(Entanglement as non-separable state in tensor product — see inbox for Kitaev, Freedman-Kitaev-Wang)*

## Neuroscience

*(Neural binding, cross-frequency coupling, integrated information — see inbox for Tort, Tononi)*

## Dynamical Systems

*(Emergent attractor topology from coupling — see inbox for Sugihara CCM)*
