## silva-2018 — Silva, Giusti, Keogh, Batista (2018)
**"Speeding up similarity search under dynamic time warping by pruning unpromising alignments"**

**Domain(s)**: dynamical systems (time-series mining), computational geometry

**Abstract machines instantiated**:
- **Matching**: Works entirely inside the DTW assignment: exact DTW is the minimum-cost monotone correspondence between two sequences, and the paper attacks the cost of *verifying* candidate assignments — pruning "unpromising alignments" (cells of the DP grid that provably cannot lie on the optimal correspondence path) before they are evaluated.
- **Stability**: Exactness is preserved: the pruned computation returns exactly dtw(P,Q), so the matching value is stable under the acceleration (a zero-error bound, stronger than ying-2016's (1+ε)). Pruning decisions rest on lower-bound certificates, i.e., rigorous bounds on the optimal cost.
- **Null hypothesis (weak)**: Lower-bound rejection is a falsification test per candidate pair: a pair is discarded once its cheap lower bound exceeds the current best matching cost — the incumbent optimum serves as the reference against which alternatives are destroyed.

**What is genuinely new (not reducible to shared abstraction)**:
- Prior speedups prune *between* pairs of series; this prunes *within* a single DTW calculation (the residual alignments surviving lower-bound pruning), complementing rather than duplicating the UCR suite's outer pruning.
- Up to 5× speedup over UCR for long queries and wide warping windows, with the useful scaling property that the speedup grows with search difficulty.
- Purely algorithmic; no topological or information-theoretic content. Pairs naturally with ying-2016 (approximate-within-curve) as the exact counterpart.

**Connections the authors acknowledge**: Cites the UCR suite (Rakthanmanon et al.), Sakoe-Chiba band constraints, LB_Keogh lower bounds. Time-series data-mining silo; no connection to TDA/QEC/neuroscience acknowledged.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Unpromising alignment | Non-optimal correspondence (prunable) |
| DTW calculation | Monotone optimal assignment |
| Lower-bound certificate | Rigorous bound on matching value |
| Exactness under pruning | Stability of matching value (zero error) |

---

