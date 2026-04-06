# METHODOLOGY.md

## How Papers Are Categorized

Every paper entering this repo gets annotated along two axes and filed under both.

### Axis 1: Domain

Which disciplinary community produced and reads this paper? A paper can belong to multiple domains. The current domains are: TDA, QEC, dynamical systems, neuroscience, information theory. New domains are added when a paper doesn't fit any existing one.

### Axis 2: Structure

Which abstract machines does the paper instantiate? The current machines are:

1. **Chain complex** — The paper constructs or uses boundary operators, computes homology, or reasons about cycles and boundaries.
2. **Parameterized homology** — The paper tracks how topological invariants change as a parameter varies. This includes persistence diagrams, error thresholds, bifurcation diagrams, and capacity curves.
3. **Matching** — The paper solves an optimal assignment problem between topological features. This includes diagram distances, syndrome decoding, and optimal transport.
4. **Stability** — The paper proves or exploits the robustness of topological invariants under perturbation.
5. **Joint-vs-marginal excess** — The paper detects structure in composite systems that is absent from components. This includes entanglement, binding, synergy, and integrated information.
6. **Null hypothesis** — The paper constructs a reference distribution by destroying specific structure while preserving other properties.

A paper typically instantiates 2–4 machines. The annotation should identify which ones and how.

### What Gets Recorded

For each paper:

- **Citation**: Authors, year, title, arXiv ID or DOI.
- **Domain(s)**: Which communities.
- **Machine(s)**: Which abstract structures, with a sentence each explaining how.
- **Vocabulary**: A small table mapping the paper's terms to Rosetta terms.
- **Genuine novelty**: What in the paper does NOT reduce to the shared machines. This is the most important field. If everything reduces, say so explicitly.
- **Awareness**: Does the paper acknowledge the cross-domain parallels? Most don't. When one does, note it — these are the rare existing bridges.

### What Does NOT Get Recorded

This is not a literature review. We do not summarize results, evaluate quality, or assess impact. We map structure. A weak paper that instantiates an unusual combination of machines is more interesting here than a landmark paper that stays within one domain's standard machinery.

### The Dual Index

Each annotated paper is referenced in both a `by-domain/` file and a `by-structure/` file. The domain file groups papers by disciplinary home. The structure file groups papers by which machine they use, regardless of domain. Reading down a domain file shows one community's trajectory. Reading down a structure file shows the same idea recurring across communities that don't cite each other.

The cross-references are the point. When `by-structure/filtrations.md` lists a TDA persistence paper next to a QEC threshold paper next to a bifurcation theory paper, the repetition becomes visible.
