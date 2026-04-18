# Session Handoff: Wave 10 link-forge update (2026-04-17)

## What was done

Added 15 papers from the link-forge Neo4j database to topo-rosetta, organized as Wave 10 in three sub-waves:

### Wave 10a: Cross-Domain Bridges (5 papers)
1. **Baudot, Tapia, Bennequin & Goaillard (2019)** — "Topological Information Data Analysis" (1907.04242). I_k co-chains on simplicial complex of variables, δH = I_2. ALL 5 machines instantiated. Chain×InfoTheo, Joint×InfoTheo, Null×InfoTheo, Param×InfoTheo, Stab×InfoTheo.
2. **Ghorbanchian, Restrepo, Torres & Bianconi (2020)** — "Higher-order simplicial synchronization" (Nature Comms). Hodge Laplacian dynamics, explosive sync. Chain×Dynamics, Param×Dynamics, Stab×Dynamics.
3. **Dey, Mrozek & Slechta (2021)** — "Conley-Morse graph persistence" (2107.02115). Zigzag persistence on Conley-Morse graphs. Chain×Dynamics, Param×Dynamics, Stab×Dynamics.
4. **Petri et al. (2014)** — "Homological scaffolds of brain networks" (rsif.2014.0873). PH scaffolds under psilocybin. Chain×Neuro, Param×Neuro, Null×Neuro.
5. **Chaudhuri et al. (2019)** — "Head direction ring attractor" (Nature Neuro). S^1 ring manifold across waking/sleep. Chain×Neuro, Stab×Neuro, Joint×Neuro.

### Wave 10b: Weak Cell Strengthening (5 papers)
6. **Panaretos & Zemel (2019)** — "Statistical Aspects of Wasserstein Distances" (Annual Reviews). Match×InfoTheo (was weakest cell at 4+).
7. **Chung et al. (2025)** — "From Density to Void" (2503.14700). ANTISYNONYM: higher-order brain topology fails FDR/cross-subject replication. Null×Neuro, Chain×Neuro.
8. **Dabaghian, Brandt & Frank (2014)** — "Reconceiving hippocampal map as topological template" (eLife). Chain×Neuro.
9. **Donato et al. (2016)** — "PH analysis of Phase Transitions" (1601.03641). Param×Dynamics, Stab×Dynamics. Petri is coauthor.
10. **Batko, Mischaikow, Mrozek & Przybylski (2019)** — "Conley Index Approach to Sampled Dynamics" (1904.03757). Chain×Dynamics.

### Wave 10c: Strategic Deepening (5 papers)
11. **Lord et al. (2016)** — "Brain Architectures from Homological Scaffolds" (Frontiers). Companion to Petri 2014. Chain×Neuro, Param×Neuro.
12. **Jost & Zhang (2023)** — "Cheeger inequalities on simplicial complexes" (2302.01069). Chain×TDA, Stab×TDA.
13. **Trinca et al. (2024)** — "n-Dimensional Toric Codes from Lattice Codes" (2410.20233). Chain×QEC.
14. **Curry et al. (2022)** — "Decorated merge trees" (s41468-022-00089-3). Chain×TDA, Match×TDA, Stab×TDA.
15. **Méndez & Sánchez-García (2020)** — "Directed PH theory" (2008.00711). Chain×TDA. Underpins Peek 2025.

## Coverage matrix (before → after)

```
              Chain    Param   Match   Stabil  Joint   Null
TDA            6→10+   8→11+   6→7+   8→11+    5+      4+
QEC           15→16+    8+      8+   10→11+     6+      9+
Dynamics       9→13+  12→16+   11+    9→13+     6+    8→9+
Neuro          6→11+  10→12+    8+    7→9+   13→14+  10→12+
InfoTheo       9→10+   9→10+   4→5+   6→8+   12→13+   8→9+
```

16 cells now ≥10+ (was 8). ~219 papers total.

## Files modified (16 files, +906 lines)
- `papers/inbox.md` — 15 full-depth annotations under Wave 10a/b/c headers
- `papers/by-domain/{dynamical_systems,information_theory,neuroscience,qec,tda}.md` — one-liner cross-refs
- `papers/by-structure/{boundary_operators,composite_systems,filtrations,optimal_transport,phase_transitions}.md` — one-liner cross-refs
- `papers/cross_domain_bridges.md` — 5 bridge entries (4 Wave A + Donato from Wave B)
- `glossary/ANTISYNONYMS.md` — new entry: brain topology reproducibility
- `diagrams/coverage-matrix.md` — updated counts and mermaid diagram
- `README.md` — updated matrix and paper count
- `docs/index.html` — updated matrix cells, paper count, CSS classes for 10+ threshold

## Commit
`e198226` — pushed to `origin/master`

## What was NOT done (potential future work)
- Atlas essay updates (CHAIN_COMPLEX.md, PARAMETERIZED_HOMOLOGY.md, NULL_HYPOTHESIS.md) — the plan called for this but would require reading + carefully extending existing long essays
- SYNONYMS.md glossary updates — Conley index terms, scaffold terminology, synchronization terms could be added
- docs/index.html domain description updates beyond QEC paper count
