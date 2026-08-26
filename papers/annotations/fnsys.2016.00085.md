## fnsys.2016.00085 — Lord, Expert, Fernandes, Petri, van Hartevelt, Vaccarino, Deco, Turkheimer & Kringelbach (2016)
**"Insights into Brain Architectures from the Homological Scaffolds of Functional Connectivity Networks"**

**Domain(s)**: neuroscience, TDA

**Abstract machines instantiated**:
- **Chain complex**: Extends Petri et al. (2014) scaffold approach. Weighted functional network → simplicial complex → persistent homology → homological scaffold. The scaffold summarizes persistent homology structure without ad hoc thresholding — uses all edge weights. Simplicial structures (not just dyadic interactions) contribute to the organization.
- **Parameterized homology**: Weight filtration across all edge weights produces persistence diagrams. The scaffold is a summary of this persistence structure. Node strength in the scaffold measures the aggregate persistence contribution of each brain region — a parameterized invariant.

**What is genuinely new (not reducible to shared abstraction)**:
- Systematic comparison of scaffold metrics to standard graph metrics (degree, clustering, betweenness). The scaffold captures information that graph-theoretic measures miss — specifically, the role of each node in supporting functional integration across distributed networks.
- Uses all edge weights without thresholding (unlike standard graph approaches), avoiding the arbitrary threshold problem.
- Identifies network elements supporting functional integration — a higher-order structural role invisible to standard network analysis.
- Companion to Petri 2014: Petri showed scaffold changes under psilocybin; this paper characterizes what scaffold metrics capture in healthy resting-state data.

**Connections the authors acknowledge**: Directly extend Petri et al. (2014). Cite TDA (persistent homology, simplicial complexes) and network neuroscience (graph-theoretic metrics). Same Petri and Vaccarino as A4. Explicit cross-domain bridge.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Persistence homological scaffold | Network encoding persistent cycles |
| Node strength in scaffold | Aggregate persistence contribution |
| Weight filtration (no threshold) | Continuous parameterization |
| Simplicial structure | Higher-order interaction (beyond dyadic) |
| Functional integration | Distributed joint structure |

**See also**: `by-domain/neuroscience.md`, `by-domain/tda.md`, `by-structure/boundary_operators.md`, `by-structure/filtrations.md`
