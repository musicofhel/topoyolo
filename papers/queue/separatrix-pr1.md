# SEPARATRIX PR #1 — exported by orchestrator 2026-08-24 for A6 review (pass cannot network-fetch)

Title: Propose SEPARATRIX as seventh machine

Body:
Proposes the **separatrix** as a candidate seventh machine: the codimension-1 boundary set between basins, with the claim that measures of the boundary itself (thickness, barrier height, basin entropy, margin) predict system behavior beyond bulk/prototype measures.

Instantiations mapped across: dynamical systems (home domain — Wada, riddled, basin entropy), chemistry/comp-neuro (barrier height, transition states), ML (margin → boundary thickness → barrier class), cognitive science/philosophy (Voronoi vagueness, the Douven thickness problem), statistical physics (manifold capacity as boundary budget), contrastive learning (uniformity as the sculptor).

Divergences documented per repo convention, including a measured failure case: topo-confidence EXP-88, where the naive LLM-residual-stream instantiation reduced entirely to generation length, and F-10, where PH instruments integrate away the (spectral) signal.

Marked PROPOSED — not yet in coverage matrix, glossary, or dual index. Three integration questions listed at the end.

## Diff
```diff
diff --git a/atlas/SEPARATRIX.md b/atlas/SEPARATRIX.md
new file mode 100644
index 0000000..f03b760
--- /dev/null
+++ b/atlas/SEPARATRIX.md
@@ -0,0 +1,160 @@
+# Separatrix (PROPOSED — seventh machine)
+
+**Status: candidate.** Not yet integrated into the coverage matrix, glossary, or dual
+index. This essay stakes the claim; integration follows if the machine survives
+annotation of its papers under METHODOLOGY.md.
+
+## The Abstract Machine
+
+Given a space partitioned into basins {B_i} (of attraction, of classification, of
+category membership), the **separatrix** is the codimension-1 set ∂B where basin
+membership changes. The machine's claim: discriminative and uncertain behavior of the
+system localizes on ∂B rather than in the bulk of any basin, and *measures of the
+boundary itself* — thickness, height, dimension, entropy — predict system behavior in
+ways that bulk measures (basin volume, centroid position, prototype distance) cannot.
+
+Signature: **∂B = {x : basin(x) is not locally constant}**, plus a boundary measure
+μ(∂B) ∈ {thickness, barrier height, fractal dimension, basin entropy, margin}.
+
+The test that separates this machine from trivial partition geometry: μ(∂B) must add
+predictive or causal power *beyond* distance-to-prototype. Where it does not, the
+separatrix is epiphenomenal and the instantiation fails (see Divergences — this
+failure has been directly measured at least once).
+
+## Where It Appears
+
+### Dynamical Systems — The Home Domain
+The separatrix is native vocabulary here: the invariant manifold separating basins of
+attraction. The richest substructure is the taxonomy of boundary *types*:
+
+- **Basin entropy** (Daza et al., arXiv: 2201.08083) — a single scalar classifying
+  boundaries as smooth / fractal / riddled / Wada / intermingled. Parameterized
+  unpredictability of the boundary itself.
+- **Wada property** — three or more basins sharing every boundary point; arbitrarily
+  small perturbation at the boundary can reach any outcome. Saddle-straddle detection
+  via the chaotic saddle (Valle, Wagemakers, Sanjuán).
+- **Riddled basins** — basin volume ill-posed at finite precision; only the boundary
+  is a well-defined object. Recent bridge to ML: riddling conditions met by real DNN
+  training via symmetry-induced invariant subspaces (arXiv: 2510.05606).
+- **Basin reconstruction as classification** (Shena et al., arXiv: 2109.06564) — the
+  boundary recovered as the level set where classifier probability ≈ 0.5. An
+  operational protocol other domains can borrow directly.
+
+### Chemistry / Computational Neuroscience — Barrier Height
+The transition state: lowest-energy point on the basin boundary, Morse index 1, one
+unstable direction connecting two minima. The boundary measure is scalar:
+**barrier height = U(saddle) − U(min)**.
+
+- Working-memory attractor models: barrier height quantifies stability; an emergent
+  intermediate state on the boundary lowers the barrier, trading robustness for
+  flexibility (PLOS Comput Biol 2020; arXiv: 2209.05002).
+- Brain-connectome energy landscapes: empirical basin-transition frequencies predicted
+  from energy barriers (maximum-entropy models, PMC5600845).
+- Kuramoto/Hebbian pattern recognition: saddles determine whether retrieval reaches
+  the stored pattern or a spurious state (arXiv: 2508.21310).
+
+### Machine Learning — Margin, Thickness, and the Barrier Class
+The decision boundary is the separatrix of a classifier. Three escalating boundary
+measures:
+
+- **Margin** — distance from a point to ∂B. The classical measure; predicts
+  generalization imperfectly.
+- **Boundary thickness** (Yang et al., NeurIPS 2020) — margin as a special case;
+  predicts the *robust* generalization gap where margin fails; causally manipulable
+  (noisy mixup thickens the boundary and improves adversarial/OOD robustness). The
+  strongest evidence in any domain that μ(∂B) is a first-class, trainable quantity.
+- **Boundary complexity** (Guan & Loew, arXiv: 2009.07974) — entropy of eigenvalues
+  of points sampled on/near ∂B, predicting test accuracy. A spectral boundary measure.
+- **The barrier class** (PadNet, ACM TOPS 2025) — the data-sparse region between
+  data-dense regions reified as an explicit class and trained on. The only known
+  engineering artifact that treats the void as an object with its own label.
+
+Counter-instantiation within the same domain: well-trained networks' boundaries can be
+approximately *linear*, with complexity vanishing over training (arXiv: 2211.16209),
+and fractal dimension of ∂B is an unreliable generalization measure. The domain
+contains both the machine and its strongest internal critique.
+
+### Cognitive Science / Philosophy — Vagueness as Boundary Measure
+Gärdenfors: concepts = convex Voronoi cells around prototypes; the boundary is where
+categorization fails. The field's central internal dispute is precisely the machine's
+key parameter:
+
+- **The thickness problem** (Douven et al.) — classical Voronoi boundaries are
+  measure-zero, empirically wrong for human concepts. Collated Voronoi tessellations
+  produce *thick* boundary regions where borderline cases neighbor other borderline
+  cases. **Vagueness = μ(∂B).** The philosophical twin of boundary thickness,
+  formulated independently, mutually uncited.
+- Topological dissolution (Mormann, Synthese) — Alexandroff-space account removing
+  the metric-choice and thickness problems; Gärdenfors's construction as special case.
+- Higher-order Voronoi diagrams for graded boundary vagueness (order-k framework,
+  Taylor & Francis 10.1080/08839510903078176).
+
+Empirical anchor — **categorical perception**: representations are pushed away from
+category boundaries and pulled toward prototypes; discrimination *peaks at the
+boundary* (the CP signature). Layerwise in deep nets (arXiv: 2012.05549); at
+digit-count boundaries in LLM hidden states (arXiv: 2603.28258); subcortically in
+human brainstem responses. The boundary is where the system spends its resolution.
+
+### Statistical Physics — Capacity as Boundary Budget
+Manifold capacity theory (Chung, Lee, Sompolinsky, PRX 8:031003; Cohen et al.):
+the critical number of linearly separable category manifolds per neuron, in closed
+form as a function of manifold dimension and radius. Read through this machine:
+capacity is the accounting of how much of the space the separatrices consume.
+"Untangling" along a processing hierarchy = reshaping manifolds so boundaries fit.
+
+### Contrastive Learning — The Sculptor
+Wang & Isola (arXiv: 2005.10242): the contrastive loss decomposes asymptotically into
+alignment (positives) + **uniformity** (everything vs. everything, driven by
+negatives). Uniformity pressure is the mechanism that *carves* separatrices: half the
+loss's geometric budget is spent organizing the not-space. The negative-sampling
+literature (arXiv: 2206.00212) is, under this reading, the engineering of ∂B.
+
+## Key Divergences
+
+- **Thin vs. thick is a real disagreement, not vocabulary.** Dynamical separatrices
+  and classical Voronoi walls are measure-zero; boundary thickness and collated
+  tessellations have volume. The domains disagree about the *dimensionality* of ∂B.
+  No translation reconciles this; it marks genuinely different objects.
+- **Coordinate artifacts.** Mode connectivity's permutation lesson (weight space):
+  barriers between trained solutions largely vanish after neuron permutation
+  (Entezari conjecture; Git Re-Basin; transformer version arXiv: 2506.22712). An
+  apparent separatrix can be an artifact of the coordinates. No analogue exists in
+  Voronoi or barrier-height framings, where the metric is fixed by assumption — a
+  standing threat to any activation-space instantiation.
+- **Energetic vs. entropic boundaries.** Some barriers are not walls but places noise
+  refuses to stay: flat loss with curvature rising off the minima (entropic
+  confinement, arXiv: 2512.06297). Barrier-height vocabulary has no term for this.
+- **Topological instruments can fail on real instantiations.** Direct measurement
+  (musicofhel/topo-confidence, EXP-88, Aug 2026): in Qwen-2.5-1.5B L19 residual
+  streams, every naive membrane feature (margin to cluster boundary, local shell
+  spectrum, local PR) reduced to generation length; length-residualized, the feature
+  block scored below chance. Same repo, F-10: persistent homology summaries on these
+  clouds are indistinguishable from a matched-covariance Gaussian null — the signal
+  that exists is spectral (eigenvalue decay), not topological. A documented case
+  where the separatrix machine's obvious instantiation is epiphenomenal and the
+  TDA-native instrument integrates away the information.
+- **Wada has no ML analogue yet.** Boundaries where *three or more* basins meet
+  everywhere are characterized in dynamics; multiclass decision boundaries are
+  studied pairwise almost everywhere in ML. Either the parallel is unexplored or the
+  objects genuinely differ.
+
+## Relation to the Existing Six
+
+Not reducible, but adjacent: the separatrix is where **parameterized homology**'s
+invariants change (bifurcation sets ARE separatrices in parameter space);
+**stability** theorems bound how much ∂B can move under perturbation; **null
+hypothesis** machinery is how failed instantiations get detected (EXP-88's matched
+Gaussian columns; F-10's covariance null). The distinctive content is the claim that
+μ(∂B) — a measure *of the boundary itself* — is the predictive object. None of the
+six existing machines takes the boundary as its primary object; they take cycles,
+filtrations, matchings, perturbations, composites, and nulls.
+
+## Open Questions for Integration
+
+1. Do the papers above survive full METHODOLOGY.md annotation, and which existing
+   machines does each co-instantiate?
+2. Does ML/robustness enter as a sixth domain, or file under existing domains?
+   (Methodology permits new domains when papers fit none.)
+3. Is thin-vs-thick one machine with a parameter, or two machines? The Douven
+   thickness problem and Yang boundary thickness suggest the thick version is the
+   empirically load-bearing one.
```
