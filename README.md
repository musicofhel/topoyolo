# topo-rosetta

**A cartography of shared structure across disciplines that independently discovered the same mathematics.**

Persistent homology, quantum error correction, dynamical systems, neural coding, information theory — these fields use different vocabularies to describe the same algebraic objects. This repo collects papers, maps the repetitions, and makes the synonyms explicit.

The goal is not synthesis or unification. It is *differentiation* — in the Deleuzian sense. The same abstract machine (chain complexes, parameterized homology, optimal matching on features) is actualized differently in each domain. By cataloguing the repetitions and the genuine divergences, we make visible the plane that connects them.

---

## Structure

```
topo-rosetta/
├── atlas/                  # The maps
│   ├── CHAIN_COMPLEX.md    # ∂²=0 across domains
│   ├── PARAMETERIZED_HOMOLOGY.md
│   ├── MATCHING.md
│   ├── STABILITY.md
│   ├── JOINT_VS_MARGINAL.md
│   └── NULL_HYPOTHESIS.md
│
├── papers/                 # Annotated bibliography, organized by concept
│   ├── by-domain/          # Entry point by discipline
│   │   ├── tda.md
│   │   ├── qec.md
│   │   ├── dynamical_systems.md
│   │   ├── neuroscience.md
│   │   └── information_theory.md
│   ├── by-structure/       # Entry point by shared abstraction
│   │   ├── boundary_operators.md
│   │   ├── filtrations.md
│   │   ├── optimal_transport.md
│   │   ├── phase_transitions.md
│   │   └── composite_systems.md
│   └── inbox.md            # Full-depth annotations (primary store)
│
├── glossary/
│   ├── SYNONYMS.md         # The core translation table
│   └── ANTISYNONYMS.md     # Where the analogy breaks — genuine divergences
│
├── diagrams/               # Visual maps (mermaid, SVG)
│   └── .gitkeep
│
└── METHODOLOGY.md          # How papers are categorized
```

## Methodology

Each paper gets a short annotation identifying:

1. **Which abstract machine it instantiates** — chain complex, filtration, matching, stability, composite-system excess, null model
2. **Domain-specific vocabulary** — the terms it uses for each shared concept
3. **What is genuinely new** — structure that does NOT reduce to the shared abstraction
4. **Connections claimed vs. connections actual** — does the paper itself acknowledge the parallel, or is it invisible to the authors?

Papers are filed under both `by-domain/` and `by-structure/`. The dual indexing is the point: the same paper appears in two places, revealing which disciplinary silo it sits in and which abstract machine it instantiates.

## The Plane

The working hypothesis is that at least six abstract machines recur:

| Machine | What it does |
|---------|-------------|
| **Chain complex** | Boundary operators, ∂²=0, cycles mod boundaries |
| **Parameterized homology** | Track topological invariants as a parameter varies — persistence diagrams, error thresholds, bifurcation |
| **Optimal matching** | Assign features to features at minimum cost — decoding, diagram distance, transport |
| **Stability** | Small input perturbation → bounded output change — PH stability, threshold theorem, structural stability |
| **Joint-vs-marginal excess** | Composite system has structure absent from components — binding, entanglement, synergy |
| **Null hypothesis** | Destroy structure, measure residual — surrogates, noise channels, shuffles |

These are not metaphors. They share definitions, theorems, and algorithms. The repo's job is to collect the evidence and mark precisely where the identity holds and where it doesn't.

## Anti-Synthesis

This is explicitly NOT a "grand unified theory" project. The domains diverge in ways that matter. QEC operates over finite fields; PH typically over reals. Takens embedding has no QEC analogue. Code distance is a combinatorial invariant; persistence is a multi-scale invariant. The divergences are as informative as the repetitions. `ANTISYNONYMS.md` tracks them.

## Contributing

Add papers to `papers/inbox.md` with a one-line annotation. Periodically they get sorted into the dual index.
