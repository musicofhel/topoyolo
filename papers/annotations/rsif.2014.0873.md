## rsif.2014.0873 — Petri, Expert, Turkheimer, Carhart-Harris, Nutt, Hellyer & Vaccarino (2014)
**"Homological scaffolds of brain functional networks"**

**Domain(s)**: neuroscience, TDA

**Abstract machines instantiated**:
- **Chain complex**: The weighted functional brain network (from fMRI correlations) is converted to a weighted clique complex. Boundary operators on this simplicial complex define homology groups. The key construction is the *homological scaffold*: a new graph whose edges are those that participate in persistent homological cycles. This extracts chain-level information (which specific simplices carry cycles) and re-encodes it as a network amenable to standard graph-theoretic analysis.
- **Parameterized homology**: The weight filtration on the correlation network creates a persistence diagram. As the threshold parameter decreases (admitting weaker correlations), cycles appear and disappear. The scaffold captures the entire persistence history — each scaffold edge is weighted by the persistence (death − birth) of the cycle it participates in. Short-lived vs long-lived homological features are distinguished.
- **Null hypothesis**: The placebo condition serves as the experimental null. Psilocybin vs placebo comparison reveals that the drug dramatically alters the homological scaffold: psilocybin produces many transient structures of low stability alongside a small number of highly persistent ones not seen under placebo. The gap between conditions quantifies the drug's effect on brain topology.

**What is genuinely new (not reducible to shared abstraction)**:
- The *homological scaffold* is a genuinely novel construction: it transforms PH output (persistence diagrams, which discard spatial information) back into a network that retains WHICH edges carry cycles. Bridges PH and network science — two communities that typically do not share tools.
- Psilocybin increases topological complexity (more short-lived cycles) while creating a few highly persistent structures. Not just "more disorder" — a restructuring of the homological landscape.
- The scaffold enables standard network metrics (degree, modularity, clustering) to be computed on homological features. Operationalizes TDA for the neuroscience community.
- Correlation between scaffold structure and subjective drug experience provides empirical validation that homological features are behaviorally relevant.

**Connections the authors acknowledge**: Explicitly bridge TDA (persistent homology, simplicial complexes — cite Edelsbrunner, Harer, Carlsson) and neuroscience (brain functional networks — cite Bullmore & Sporns). This paper IS a cross-domain bridge — the authors are fully aware of bridging these communities.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Weighted clique complex | Chain complex from correlation data |
| Homological cycle | Element of ker ∂ (kernel of boundary operator) |
| Homological scaffold | Network encoding which edges carry persistent cycles |
| Persistence (death − birth) | Lifetime in parameterized homology |
| Weight filtration | Parameterization by correlation threshold |
| Placebo condition | Null model (no drug = structure-preserving reference) |
| Transient structure | Short-lived cycle (low persistence) |
| Persistent structure | Long-lived cycle (high persistence) |

**See also**: `by-domain/neuroscience.md`, `by-domain/tda.md`, `by-structure/boundary_operators.md`, `by-structure/filtrations.md`, `by-structure/phase_transitions.md`, `papers/cross_domain_bridges.md`
