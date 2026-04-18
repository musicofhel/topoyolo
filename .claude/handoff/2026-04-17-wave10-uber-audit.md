# Session Handoff: Wave 10 Uber Audit (2026-04-17, session 2)

## What was done

Fresh-eyes audit of ALL 16 files modified in the Wave 10 link-forge update. Read every file end-to-end: inbox.md (15 annotations, ~537 lines), all 5 by-domain files, all 5 by-structure files, cross_domain_bridges.md, ANTISYNONYMS.md, coverage-matrix.md, README.md, docs/index.html.

### Audit findings

#### Correct (vast majority)
- All 15 inbox.md annotations present, complete, high-quality SKILL.md template
- All 15 papers correctly dual-indexed in by-domain AND by-structure files
- Coverage matrix CELL VALUES consistent across README.md, coverage-matrix.md, docs/index.html
- docs/index.html CSS classes (cell-high/cell-mid/cell-low) correctly applied — 16 cell-high entries
- ANTISYNONYM entry (brain topology reproducibility) well-structured
- 5 cross-domain bridge entries with quality assessments
- Machine assignments in inbox annotations are thorough and well-justified

#### BUG #1: "18 cells >= 10" text is wrong — correct count is 16

Counted from the actual matrix values:
- TDA: Chain(10+), Param(11+), Stab(11+) = 3 cells >=10
- QEC: Chain(16+), Stab(11+) = 2 cells >=10
- Dynamics: Chain(13+), Param(16+), Match(11+), Stab(13+) = 4 cells >=10
- Neuro: Chain(11+), Param(12+), Joint(14+), Null(12+) = 4 cells >=10
- InfoTheo: Chain(10+), Param(10+), Joint(13+) = 3 cells >=10
- TOTAL: 16 cells >=10

NOT >=10: QEC×Null(9+), Dynamics×Null(9+), InfoTheo×Null(9+), QEC×Param(8+), QEC×Match(8+), QEC×Joint(6+), Neuro×Match(8+), Neuro×Stab(9+), InfoTheo×Stab(8+), InfoTheo×Match(5+), TDA×Match(7+), TDA×Joint(5+), TDA×Null(4+), Dynamics×Joint(6+)

**Files to fix:**
1. `diagrams/coverage-matrix.md` line 63: "18 new green cells (>=10) — up from 8 in Session 7" → should be 16
2. `diagrams/coverage-matrix.md` line 69: "18 cells >= 10" → "16 cells >= 10"
3. `diagrams/coverage-matrix.md` mermaid: remove `style IT_NH fill:#9f9` and `style QEC_NH fill:#9f9` (both are 9+, not >=10)
4. `README.md` line 9: `` `5 domains · 6 machines · 219 papers · 30 cells, all >= 4 · 18 cells >= 10` `` → change 18 to 16
5. `README.md` line 46: "18 cells >= 10" → "16 cells >= 10"
6. `.claude/handoff/2026-04-17-wave10-linkforge-update.md` line 39: "14 cells now >=10+" → "16 cells now >=10+"

**docs/index.html is CORRECT** — it has exactly 16 cell-high entries. No fix needed there.

#### BUG #2: Panaretos missing from tda.md

The Panaretos & Zemel (2019) inbox annotation says:
- "Domain(s): information theory (statistics), TDA"  
- "See also: `by-domain/information_theory.md`, `by-domain/tda.md`, `by-structure/optimal_transport.md`, `by-structure/phase_transitions.md`"

But tda.md Wave 10 section has NO Panaretos entry. It IS in information_theory.md and optimal_transport.md. The tda.md cross-ref is missing.

**Fix:** Add to tda.md Wave 10 section:
```
- **Panaretos & Zemel (2019)** — "Statistical Aspects of Wasserstein Distances." DOI: annurev-statistics-030718-104938. 913 citations. Comprehensive review of W_p family as statistical tools. Bottleneck distance on PDs IS W_∞. Otto calculus gives Riemannian geometry of Wasserstein space. Full annotation: `inbox.md` (Wave 10b). Machines: matching, stability, parameterized homology. **See also**: `by-domain/information_theory.md`, `by-structure/optimal_transport.md`.
```

## Complete file inventory of Wave 10 (for verification after fixes)

### inbox.md Wave 10 annotations (lines 972-1506):
- Wave 10a (lines 972-1158): Baudot, Ghorbanchian, Dey, Petri, Chaudhuri
- Wave 10b (lines 1162-1344): Panaretos, Chung, Dabaghian, Donato, Batko
- Wave 10c (lines 1348-1505): Lord, Jost, Trinca, Curry, Mendez

### by-domain cross-refs:
- `tda.md` Wave 10: Baudot, Ghorbanchian, Dey, Petri, Lord, Chung, Donato, Batko, Jost, Curry, Mendez (11 entries). **MISSING: Panaretos**
- `qec.md` Wave 10: Trinca (1 entry)
- `dynamical_systems.md` Wave 10: Ghorbanchian, Dey, Donato, Batko (4 entries)
- `neuroscience.md` Wave 10: Petri, Chaudhuri, Chung, Dabaghian, Lord (5 entries)
- `information_theory.md` Wave 10: Baudot, Panaretos (2 entries)

### by-structure cross-refs:
- `boundary_operators.md` Wave 10: All 15 papers that instantiate Chain Complex (13 entries: Baudot, Ghorbanchian, Dey, Petri, Chaudhuri, Chung, Dabaghian, Donato, Batko, Lord, Jost, Trinca, Curry, Mendez — wait, that's 14. Actually Panaretos doesn't have chain complex so it wouldn't be here)
  - Actually: Baudot, Ghorbanchian, Dey, Petri, Chaudhuri, Chung, Dabaghian, Donato, Batko, Lord, Jost, Trinca, Curry, Mendez = 14 entries
- `filtrations.md` Wave 10: Baudot, Ghorbanchian, Dey, Petri, Donato, Batko, Lord, Mendez (8 entries)
- `phase_transitions.md` Wave 10: Baudot (stab+null), Ghorbanchian (stab), Dey (stab), Petri (null), Chaudhuri (stab), Chung (anti-stab+null), Dabaghian (stab+null), Donato (stab+null), Batko (stab), Jost (stab), Trinca (stab), Curry (stab) = 12 entries
- `composite_systems.md` Wave 10: Baudot (joint), Chaudhuri (joint) = 2 entries
- `optimal_transport.md` Wave 10: Panaretos (matching), Curry (matching) = 2 entries

### Other files:
- `cross_domain_bridges.md` Wave 10a: Baudot, Ghorbanchian, Dey, Petri, Donato = 5 entries
- `glossary/ANTISYNONYMS.md`: 1 new entry (brain topology: Petri/Reimann vs Chung)
- `diagrams/coverage-matrix.md`: updated counts, mermaid, key changes
- `README.md`: updated matrix, paper count (219)
- `docs/index.html`: updated matrix cells, paper count, CSS classes

## Machine-to-paper mapping for Wave 10

### Chain Complex (contributed to 5 domain columns):
- TDA: Baudot, Ghorbanchian, Dey, Petri, Chung, Donato, Batko, Jost, Curry, Mendez, Lord
- QEC: Trinca
- Dynamics: Ghorbanchian, Dey, Donato, Batko
- Neuro: Petri, Chaudhuri, Chung, Dabaghian, Lord
- InfoTheo: Baudot

### Parameterized Homology:
- TDA: Baudot, Ghorbanchian, Dey, Petri, Donato, Batko, Lord, Mendez, Panaretos
- Dynamics: Ghorbanchian, Dey, Donato, Batko
- Neuro: Petri, Lord
- InfoTheo: Baudot, Panaretos

### Matching:
- TDA: Curry
- InfoTheo: Panaretos

### Stability:
- TDA: Baudot, Ghorbanchian, Dey, Donato, Batko, Jost, Curry, Panaretos
- QEC: Trinca
- Dynamics: Ghorbanchian, Dey, Donato, Batko
- Neuro: Chaudhuri, Chung (anti), Dabaghian
- InfoTheo: Baudot, Panaretos

### Joint-vs-Marginal:
- Neuro: Chaudhuri
- InfoTheo: Baudot

### Null Hypothesis:
- TDA: (none new)
- Neuro: Petri, Chung, Dabaghian
- InfoTheo: Baudot
- Dynamics: Donato

## What was NOT done (carry forward from session 1)
- Atlas essay updates (CHAIN_COMPLEX.md, PARAMETERIZED_HOMOLOGY.md, NULL_HYPOTHESIS.md)
- SYNONYMS.md glossary updates (Conley index terms, scaffold terminology, synchronization terms)
- docs/index.html domain description updates beyond QEC paper count

## What needs to be done (from this audit)
1. Fix "18 cells >= 10" → "16 cells >= 10" in coverage-matrix.md (2 locations) and README.md (2 locations)
2. Fix mermaid diagram: remove green styling from IT_NH and QEC_NH
3. Fix handoff file: "14 cells" → "16 cells"
4. Add Panaretos cross-ref to tda.md Wave 10 section

## Commits
- `e198226` — Wave 10: add 15 papers from link-forge DB (204→219 papers)
- `7c24caf` — Add session handoff for Wave 10 link-forge update
- No new commit from this audit session (fixes not yet applied)
