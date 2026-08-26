## blahut-arimoto-1972 --- Blahut (1972) + Arimoto (1972)
**Blahut: "Computation of channel capacity and rate-distortion functions" (IEEE Trans. IT, 18(4):460–473)**
**Arimoto: "An algorithm for computing the capacity of arbitrary discrete memoryless channels" (IEEE Trans. IT, 18(1):14–20)**
Combined citations: 3000+.

**Domain(s)**: Information theory (foundational)

**Abstract machines instantiated**:

- **Matching**: THE central machine. Both papers solve the same problem: find the optimal input distribution P(x) that maximizes mutual information I(X;Y) over a discrete memoryless channel P(y|x). This IS an optimal assignment problem — match source symbols to channel inputs to maximize throughput. Blahut extends this to rate-distortion: find the optimal test channel P(y|x) that minimizes I(X;Y) subject to an expected distortion constraint E[d(x,y)] ≤ D. This is optimal assignment between source alphabet and reproduction alphabet at minimum rate. The algorithm alternates between optimizing the input distribution (fixing the conditional) and optimizing the conditional (fixing the input) — each step is a matching update. Convergence is guaranteed by the EM-like double minimization of a KL divergence.

- **Parameterized homology**: The rate-distortion function R(D) traces a curve in (rate, distortion) space as the distortion parameter D varies. At each D, the optimal matching changes. The slope dR/dD = -s (the Lagrange multiplier) parameterizes the family. The capacity-cost function C(P) similarly parameterizes by power constraint.

- **Null hypothesis (weak)**: The uniform input distribution serves as the naive baseline. The algorithm converges to the capacity-achieving distribution, which may be very non-uniform. The gap C - I(X;Y)|_{uniform} measures how much structure the optimal matching exploits.

**What is genuinely new (not reducible to shared abstraction)**:
1. The alternating minimization structure: fix one marginal, optimize the other. This predates the EM algorithm (1977) and is structurally identical. Every iteration improves the objective, and the algorithm converges to the global optimum (convexity of mutual information in the input distribution for fixed channel).
2. Rate-distortion as matching: the optimal test channel P*(y|x) assigns each source symbol x to reproduction symbols y with probabilities that minimize rate at fixed distortion. This is a soft matching (probabilistic assignment) rather than hard matching (bijection).
3. Universality: the algorithm works for ANY discrete memoryless channel with ANY distortion measure. No structure beyond finite alphabets is required.

**Connections the authors acknowledge**: Shannon (1948, 1959) capacity and rate-distortion theorems. No connections to TDA, QEC (despite syndrome decoding being a matching problem on the same algebraic object), or neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Channel capacity C | Maximum matching value (throughput) |
| Rate-distortion R(D) | Minimum-cost matching curve (parameterized) |
| Input distribution P(x) | Source-side matching weights |
| Test channel P(y\|x) | Soft assignment (probabilistic matching) |
| Alternating minimization | Iterative matching refinement |
| Lagrange multiplier s | Slope of parameterized matching curve |
| Distortion constraint E[d] ≤ D | Matching quality bound |

**See also**: `by-domain/information_theory.md`, `by-structure/optimal_transport.md`, `atlas/MATCHING.md`

---
