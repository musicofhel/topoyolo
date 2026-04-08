# topo-rosetta

*A cartography of shared algebraic structure across five disciplines that independently discovered the same six abstract machines.*

Persistent homology, quantum error correction, dynamical systems, neural coding, information theory — these fields use different vocabularies to describe the same algebraic objects. This repo collects 200+ papers, maps the repetitions, and makes the synonyms explicit. It also maps the divergences — where the analogy breaks, which is equally informative.

The goal is not synthesis or unification. It is *differentiation* — in the Deleuzian sense. The same abstract machine is actualized differently in each domain. By cataloguing the repetitions and the genuine divergences, we make visible the plane that connects them.

`5 domains · 6 machines · 200+ papers · 30 cells, all ≥ 4`

---

## The Six Machines

| Machine | Signature | What it detects |
|---------|-----------|-----------------|
| **Chain complex** | ker(∂ₙ) / im(∂ₙ₊₁) | Boundary operators, ∂²=0, cycles mod boundaries, homology classes |
| **Parameterized homology** | Hₙ(ε) as ε varies | Topological invariants changing with a parameter — persistence, thresholds, bifurcation |
| **Optimal matching** | min_σ Σ c(xᵢ, y_σ(i)) | Assign features to features at minimum cost — decoding, diagram distance, transport |
| **Stability** | d(f,g) ≤ ε ⇒ d(H(f),H(g)) ≤ Cε | Small perturbation → bounded change in topological invariants |
| **Joint-vs-marginal excess** | I(X_joint) − Σ I(Xᵢ) > 0 | Structure in composite systems absent from components — binding, entanglement, synergy |
| **Null hypothesis** | H₀: destroy, measure residual | Reference distribution by destroying specific structure while preserving other properties |

## The Five Domains

- **TDA** — Topological Data Analysis. Multi-scale filtration; the only domain where persistence diagrams are native objects.
- **QEC** — Quantum Error Correction. Finite fields; error thresholds as phase transitions. The richest chain complex instantiation (15+ papers).
- **Dynamical Systems** — Temporal structure, delay embedding, attractor reconstruction from partial observation. Takens embedding has no QEC analogue.
- **Neuroscience** — Population-level topology. Both undirected co-firing complexes and directed synaptic complexes — where the chain complex bifurcates.
- **Information Theory** — The home of joint-vs-marginal excess. PID decomposition, information cohomology, Shannon entropy as 1-cocycle.

---

## Coverage Matrix

<!-- Coverage data also in docs/index.html and diagrams/coverage-matrix.md -->

| | Chain Complex | Param. Homology | Matching | Stability | Joint vs Marginal | Null Hypothesis |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **TDA** | 6+ | 7+ | 5+ | 7+ | 5+ | 4+ |
| **QEC** | **15+** | 8+ | 8+ | **10+** | 6+ | 9+ |
| **Dynamics** | 8+ | **11+** | **10+** | 8+ | 6+ | 7+ |
| **Neuro** | 6+ | **10+** | 8+ | 7+ | **13+** | **10+** |
| **InfoTheo** | 9+ | 9+ | 4+ | 6+ | **12+** | 8+ |

**Bold** = 10+ papers (deep coverage). All 30 cells ≥ 4.

---

## How to Read This Repository

There are four entry points, depending on what you're looking for:

**By domain** — Start in [`papers/by-domain/`](papers/by-domain/). Pick your discipline. See all papers annotated from your vocabulary. Good for: "What has my field contributed to these shared structures?"

**By machine** — Start in [`papers/by-structure/`](papers/by-structure/). Pick an abstract machine. See it instantiated across all five domains by communities that don't cite each other. Good for: "Who else discovered this?"

**The atlas** — [`atlas/`](atlas/) contains one deep essay per machine, tracing how it appears in each domain. The chain complex map alone documents seven incarnations: geometric, algebraic, categorified, combinatorial, gauge-theoretic, graded-informational, and neural.

**The glossary** — [`glossary/SYNONYMS.md`](glossary/SYNONYMS.md) is the Rosetta Stone itself: five-column tables mapping domain-specific vocabulary to shared concepts across five layers (algebraic objects, parameterization, matching, composite systems, null models). [`glossary/ANTISYNONYMS.md`](glossary/ANTISYNONYMS.md) is equally important — 30 documented divergences where the mapping breaks. Empty cells in the synonyms table are data: they mark where the domains genuinely diverge rather than merely using different words.

---

## Anti-Synthesis

This is explicitly NOT a "grand unified theory" project. The domains diverge in ways that matter:

- QEC operates over finite fields (ℤ/2); PH typically over reals. Same machine, different arithmetic, different answers.
- Takens delay embedding reconstructs a manifold from a single observable. QEC starts with the complex already given. The shared structure begins only after construction.
- Code distance is a single number; a persistence diagram encodes the full birth-death spectrum. Related but structurally different objects.
- Tsuda's attractor ruins — destroyed attractors that retain geometric influence — have no persistence bar and no error-correction analogue. A sixth flavor of stability with no parallel in the static frameworks of TDA or QEC.

The divergences are as informative as the repetitions. [`ANTISYNONYMS.md`](glossary/ANTISYNONYMS.md) tracks all 30.

---

## Repository Structure

```
topo-rosetta/
├── atlas/                      # One deep essay per abstract machine
│   ├── CHAIN_COMPLEX.md        # 7 incarnations: geometric → neural
│   ├── PARAMETERIZED_HOMOLOGY.md
│   ├── MATCHING.md
│   ├── STABILITY.md
│   ├── JOINT_VS_MARGINAL.md
│   └── NULL_HYPOTHESIS.md
│
├── papers/                     # Annotated bibliography (200+ papers)
│   ├── inbox.md                # Full-depth annotations (primary store)
│   ├── inbox-archive.md        # Archived earlier waves
│   ├── by-domain/              # Papers indexed by discipline
│   │   ├── tda.md
│   │   ├── qec.md
│   │   ├── dynamical_systems.md
│   │   ├── neuroscience.md
│   │   └── information_theory.md
│   ├── by-structure/           # Papers indexed by abstract machine
│   │   ├── boundary_operators.md
│   │   ├── filtrations.md
│   │   ├── optimal_transport.md
│   │   ├── phase_transitions.md
│   │   └── composite_systems.md
│   └── cross_domain_bridges.md # Papers that explicitly connect domains
│
├── glossary/
│   ├── SYNONYMS.md             # The translation table (5 layers)
│   └── ANTISYNONYMS.md         # 30 documented divergences
│
├── diagrams/
│   └── coverage-matrix.md      # 6×5 heatmap with paper counts
│
├── METHODOLOGY.md              # Annotation guidelines
└── docs/                       # GitHub Pages site
    └── index.html
```

## Methodology

Every paper is annotated along four axes: which abstract machine it instantiates, its domain-specific vocabulary mapped to shared terms, what is genuinely new (structure that does *not* reduce to the shared abstraction), and whether the paper acknowledges the cross-domain parallel or is blind to it. Papers are dual-indexed under both `by-domain/` and `by-structure/` — the same paper appears in two places. A weak paper that instantiates an unusual combination of machines is more interesting here than a landmark paper that stays within one domain's standard machinery. See [METHODOLOGY.md](METHODOLOGY.md) for full guidelines.

## Contributing

Add papers to `papers/inbox.md` with a full annotation following the methodology. Periodically they get sorted into the dual index and integrated into the atlas and glossary.
