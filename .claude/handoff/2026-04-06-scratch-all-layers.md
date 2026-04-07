# Handoff: Scratch All Layers Across All Subjects

**Date**: 2026-04-06
**Project**: ~/topoyolo (topo-rosetta)
**Goal**: Run at least one search pass across every cell in the 6x5 matrix (6 machines × 5 domains), find new papers for sparse cells, confirm coverage for dense ones.

---

## Project Summary

topo-rosetta is a cartography of shared algebraic structure across disciplines. 6 abstract machines (chain complex, parameterized homology, matching, stability, joint-vs-marginal, null hypothesis) appear independently in 5 domains (TDA, QEC, dynamical systems, neuroscience, information theory). Papers are annotated using `/annotate <identifier>` and filed into a dual index (by-domain + by-structure).

## File Structure

```
~/topoyolo/
├── atlas/                          # 6 files — one per abstract machine
│   ├── CHAIN_COMPLEX.md
│   ├── PARAMETERIZED_HOMOLOGY.md
│   ├── MATCHING.md
│   ├── STABILITY.md
│   ├── NULL_HYPOTHESIS.md
│   └── JOINT_VS_MARGINAL.md
├── papers/
│   ├── by-domain/                  # 5 files — one per domain
│   │   ├── tda.md
│   │   ├── qec.md
│   │   ├── dynamical_systems.md
│   │   ├── neuroscience.md
│   │   └── information_theory.md
│   ├── by-structure/               # 5 files (NOT 6 — Stability+Null share one)
│   │   ├── boundary_operators.md        → Chain Complex
│   │   ├── filtrations.md               → Parameterized Homology
│   │   ├── optimal_transport.md         → Matching
│   │   ├── phase_transitions.md         → Stability + Null Hypothesis (SHARED)
│   │   └── composite_systems.md         → Joint-vs-Marginal
│   ├── inbox.md                    # Unsorted papers + "to find" list
│   ├── cross_domain_bridges.md
│   ├── second_pass.md
│   ├── third_pass_dynamics_tda.md
│   ├── third_pass_neuro_qec.md
│   └── third_pass_infotheo_cross.md
├── glossary/
│   ├── SYNONYMS.md                 # 4-layer translation table
│   └── ANTISYNONYMS.md             # Where analogies break (21 entries)
├── .claude/skills/annotate/SKILL.md  # Annotation workflow
├── README.md
└── METHODOLOGY.md
```

## Coverage Matrix (annotated papers per cell, excluding inbox)

```
              Chain  Param  Match  Stabil  Joint  Null
TDA            2      4+     1      3+      1-2?   1-2?
QEC            5+     5+     3      5+      5      5+
Dynamics       7+     9+    10+     5+      4+     5+
Neuro          0**    8+     5      5+     10+     8+
InfoTheo       5+     6+     2      4       8+     6+
```

`**` = TRUE gap: zero annotated papers in by-structure/boundary_operators.md for neuro
`?`  = Not fully verified — SYNONYMS.md describes concepts but by-structure indices may lack paper entries

## Cell-by-Cell Assignment (all 30 cells)

| Cell | Wave | Type | Current |
|------|------|------|---------|
| Chain x TDA | 2 | thin | 2 |
| Chain x QEC | 3 | confirm | 5+ |
| Chain x Dyn | 3 | confirm | 7+ |
| **Chain x Neuro** | **1** | **gap** | **0** |
| Chain x Info | 3 | confirm | 5+ |
| Param x TDA | 3 | confirm | 4+ |
| Param x QEC | 3 | confirm | 5+ |
| Param x Dyn | 3 | confirm | 9+ |
| Param x Neuro | 3 | confirm | 8+ |
| Param x Info | 3 | confirm | 6+ |
| Match x TDA | 2 | thin | 1 |
| Match x QEC | 3 | confirm | 3 |
| Match x Dyn | 3 | confirm | 10+ |
| Match x Neuro | 3 | confirm | 5 |
| Match x Info | 2 | thin | 2 |
| Stabil x TDA | 3 | confirm | 3+ |
| Stabil x QEC | 3 | confirm | 5+ |
| Stabil x Dyn | 3 | confirm | 5+ |
| Stabil x Neuro | 3 | confirm | 5+ |
| Stabil x Info | 3 | confirm | 4 |
| Joint x TDA | 2 | thin? | 1-2? |
| Joint x QEC | 3 | confirm | 5 |
| Joint x Dyn | 3 | confirm | 4+ |
| Joint x Neuro | 3 | confirm | 10+ |
| Joint x Info | 3 | confirm | 8+ |
| Null x TDA | 2 | thin? | 1-2? |
| Null x QEC | 3 | confirm | 5+ |
| Null x Dyn | 3 | confirm | 5+ |
| Null x Neuro | 3 | confirm | 8+ |
| Null x Info | 3 | confirm | 6+ |

---

## Wave 1: The True Gap (Chain complex x Neuroscience)

**Goal**: Go from 0 annotated to 3+ papers where chain complex is PRIMARY.

### Step 1a — 3 parallel search agents:

**Agent 1** — arXiv (targeted):
```
mcp__arxiv__search_papers(
  query: "\"simplicial complex\" AND \"neural\" AND \"homology\"",
  categories: ["q-bio.NC", "math.AT"],
  max_results: 15
)
```
Known targets: Petri et al. 2014, Reimann et al. 2017, Sizemore et al., Curto & Itskov

**Agent 2** — Semantic Scholar (broader):
```
mcp__semantic-scholar__search_semantic_scholar(
  query: "clique topology neural correlations persistent homology brain",
  num_results: 15
)
```

**Agent 3** — Google Scholar (broadest):
```
mcp__paper-search__search_google_scholar(
  query: "algebraic topology neuroscience simplicial complex neural activity homology",
  max_results: 10
)
```

### Step 1b — Citation traversal (sequential, after 1a):

From search results, identify the Semantic Scholar paper ID for Giusti et al. 2015 ("Clique topology reveals intrinsic geometric structure in neural correlations"), then:
```
mcp__semantic-scholar__get_semantic_scholar_citations_and_references(
  paper_id: "<ID from search results>"
)
```

### Step 1c — Annotate inbox papers (sequential, after 1a/1b):

The inbox already has light annotations for these. Run `/annotate` to produce full annotations + file into dual index:
1. `/annotate Giusti et al. 2015` — "Clique topology reveals intrinsic geometric structure" (arXiv ID from search)
2. `/annotate Gardner et al. 2022` — "Toroidal topology of population activity in grid cells"

Then from search/citation results, pick 1-2 additional papers and annotate.

**Exit criterion**: boundary_operators.md neuroscience section has 3+ entries.

---

## Wave 2: Thin Cells

**Goal**: Bring 5-6 cells from 1-2 papers up to 3+.

### 3 parallel search agents:

**Agent 1** — Matching x TDA:
```
mcp__arxiv__search_papers(
  query: "\"Wasserstein distance\" AND \"persistence diagram\"",
  categories: ["math.AT", "cs.CG"],
  max_results: 10
)
```
Targets: Kerber et al. (geometry helps), Turner et al. (Frechet means of diagrams)

**Agent 2** — Matching x InfoTheo + Chain x TDA:
```
mcp__arxiv__search_papers(
  query: "\"optimal transport\" AND \"rate distortion\" AND \"information\"",
  categories: ["cs.IT", "math.IT"],
  max_results: 10
)
```
```
mcp__arxiv__search_papers(
  query: "\"cubical complex\" OR \"alpha complex\" AND \"homology\"",
  categories: ["math.AT", "cs.CG"],
  max_results: 10
)
```

**Agent 3** — Joint x TDA + Null x TDA (verify suspected thin cells):
```
mcp__arxiv__search_papers(
  query: "\"persistence\" AND \"joint\" AND \"cross-barcode\" OR \"bifiltration\"",
  categories: ["math.AT"],
  max_results: 10
)
```
```
mcp__arxiv__search_papers(
  query: "\"persistent homology\" AND \"null model\" OR \"significance\" OR \"surrogate\"",
  categories: ["math.AT", "stat.ME"],
  max_results: 10
)
```

### Then annotate: `/annotate` on 1-2 papers per thin cell. Expected: 4-8 new annotations.

---

## Wave 3: Confirmatory Pass (all 23-24 remaining cells)

**Goal**: One targeted search per cell. Only annotate if paper reveals new vocabulary, new antisynonym, or genuinely different machine instantiation.

### 3 parallel agents, grouped by domain:

**Agent 1 — TDA + QEC (9 cells):**

| Cell | Query | Tool | Categories |
|------|-------|------|------------|
| Param x TDA | `"multiparameter persistent homology"` | arxiv | math.AT |
| Stabil x TDA | `"interleaving distance" AND "stability"` | arxiv | math.AT |
| Chain x QEC | `"toric code" AND "homology"` | arxiv | quant-ph |
| Param x QEC | `"Floquet code" OR "dynamical quantum error correction"` | arxiv | quant-ph |
| Match x QEC | `"matching decoder" OR "union-find decoder"` | arxiv | quant-ph |
| Stabil x QEC | `"quantum error correction" AND "threshold theorem"` | arxiv | quant-ph |
| Joint x QEC | `"entanglement witness" AND "separability"` | arxiv | quant-ph |
| Null x QEC | `"depolarizing channel" OR "randomized benchmarking"` | arxiv | quant-ph |
| Joint x Dyn | `"emergent synchronization" AND "coupling" AND "topology"` | arxiv | nlin.CD, math.DS |

**Agent 2 — Dynamics + Neuro (8 cells):**

| Cell | Query | Tool | Categories |
|------|-------|------|------------|
| Chain x Dyn | `"Conley index" AND "chain complex"` | arxiv | math.DS |
| Param x Dyn | `"bifurcation" AND "persistence" AND "attractor"` | arxiv | math.DS, nlin.CD |
| Match x Dyn | `"optimal transport" AND "dynamical systems"` | arxiv | math.DS |
| Stabil x Dyn | `"structural stability" AND "Morse-Smale"` | arxiv | math.DS |
| Null x Dyn | `"surrogate data" AND "nonlinearity test"` | arxiv | nlin.CD |
| Param x Neuro | `"neural manifold" AND "dimensionality" AND "topology"` | pubmed | n/a |
| Match x Neuro | `"neural decoding" AND "optimal transport"` | semantic-scholar | n/a |
| Stabil x Neuro | `"representational drift" AND "stability" AND "neural"` | biorxiv | n/a |

**Agent 3 — InfoTheo + remaining Neuro (7 cells):**

| Cell | Query | Tool | Categories |
|------|-------|------|------------|
| Chain x Info | `"information cohomology" OR "Baudot Bennequin"` | arxiv | cs.IT, math.IT |
| Stabil x Info | `"channel coding" AND "robustness" AND "stability"` | arxiv | cs.IT |
| Param x Info | `"information bottleneck" AND "phase transition"` | arxiv | cs.IT, cs.LG |
| Null x Info | `"transfer entropy" AND "null model" AND "surrogate"` | arxiv | cs.IT |
| Joint x Info | `"partial information decomposition" AND "synergy"` | arxiv | cs.IT |
| Null x Neuro | `"phase-amplitude coupling" AND "surrogate" AND "null"` | pubmed | n/a |
| Joint x Neuro | `"neural binding" AND "synergy" AND "information"` | pubmed | n/a |

**Total: 9 + 8 + 7 = 24 cells** (all remaining cells after Waves 1-2).

### Triage filter: Only annotate if a result reveals:
1. New vocabulary mapping not in SYNONYMS.md
2. New antisynonym (where analogy breaks)
3. Genuinely different instantiation of the machine
4. A landmark paper that should have been in the atlas

Expected: 3-5 new annotations from confirmatory pass.

---

## Wave 4: Cross-Domain Bridges + Inbox Cleanup + Final Update

### Step 4a — Cross-domain bridge search (2 parallel agents):

**Agent 1** — TDA-QEC bridges:
```
mcp__semantic-scholar__search_semantic_scholar(
  query: "topological data analysis quantum error correction persistent homology",
  num_results: 10
)
```

**Agent 2** — Neuro-TDA-InfoTheo bridges:
```
mcp__paper-search__search_google_scholar(
  query: "neural manifold persistent homology information theory topological",
  max_results: 10
)
```

### Step 4b — Find and annotate "to find" papers (sequential):

These are in inbox.md's "to find" list — they need to be located first, then annotated:
1. Search for Kitaev 2003 → `/annotate <arXiv ID>` (Chain x QEC, foundational)
2. Search for Dennis et al. 2002 → `/annotate <arXiv ID>` (fills Chain+Match+Param+Stabil+Null x QEC)
3. Search for Perea & Harer → `/annotate <arXiv ID>` (Param x TDA+Dyn bridge)
4. Search for Cohen-Steiner et al. 2007 → `/annotate <arXiv ID>` (Stabil x TDA, foundational)

Note: these are NOT in the inbox yet — they are on the "to find" list. Each needs an arXiv search first to get the paper ID before annotation.

### Step 4c — Annotate remaining inbox papers (already identified):

These ARE in the inbox with light annotations — just need full treatment:
- Tsuda 2001 (Param x Neuro/Dyn)
- Tort et al. 2010 (Joint+Null x Neuro)
- Schreiber 2000 (Joint+Null x InfoTheo/Dyn)
- Xi et al. (Chain+Param+Null x Neuro/TDA/Info)

### Step 4d — Update atlas + glossary:

- Update all 6 atlas files with new paper references from Waves 1-3
- Update SYNONYMS.md with any new vocabulary discovered
- Update ANTISYNONYMS.md with any new divergences
- Re-count coverage matrix and confirm all cells >= 2

---

## Search Tool Selection Guide

| Domain | Primary Tool | Category Filter | Secondary |
|--------|-------------|-----------------|-----------|
| TDA | `mcp__arxiv__search_papers` | `["math.AT", "cs.CG"]` | Semantic Scholar |
| QEC | `mcp__arxiv__search_papers` | `["quant-ph"]` | Semantic Scholar |
| Dynamics | `mcp__arxiv__search_papers` | `["math.DS", "nlin.CD"]` | Google Scholar |
| Neuro | `mcp__paper-search__search_pubmed` | n/a | `search_biorxiv`, arXiv `["q-bio.NC"]` |
| Info Theory | `mcp__arxiv__search_papers` | `["cs.IT", "math.IT"]` | Semantic Scholar |
| Cross-domain | `mcp__semantic-scholar__search_semantic_scholar` | n/a | Google Scholar |

**Citation traversal**: `mcp__semantic-scholar__get_semantic_scholar_citations_and_references(paper_id: "...")` — accepts Semantic Scholar ID, `DOI:...`, or `arXiv:XXXX.XXXXX` format.

**Reading papers**: `mcp__arxiv__read_paper(paper_id: "XXXX.XXXXX")` or `mcp__paper-search__read_arxiv_paper(paper_id: "XXXX.XXXXX")` for arXiv. PubMed papers: `mcp__paper-search__read_pubmed_paper(paper_id: "PMID")`.

**Annotation**: `/annotate <arXiv ID | title | URL>` — invokes the skill at `~/topoyolo/.claude/skills/annotate/SKILL.md`.

## Triage Filters (applied every wave)

1. **Machine instantiation test**: Does the paper *construct/use* the machine with a specific mechanism? Or does it merely mention related concepts? Only annotate if genuinely instantiated.
2. **Cross-domain bonus**: Papers spanning 2+ domains fill multiple cells — prioritize.
3. **Vocabulary novelty**: New terms for Rosetta concepts → update SYNONYMS.md.
4. **Divergence detection**: Where the analogy breaks → update ANTISYNONYMS.md.
5. **Diminishing returns**: If cell has 4+ papers instantiating the same way, skip.

## Files Modified

- `papers/inbox.md` — new annotations land here first
- `papers/by-domain/{tda,qec,dynamical_systems,neuroscience,information_theory}.md` — domain filings
- `papers/by-structure/{boundary_operators,filtrations,optimal_transport,composite_systems,phase_transitions}.md` — structure filings (5 files)
- `atlas/{CHAIN_COMPLEX,PARAMETERIZED_HOMOLOGY,MATCHING,STABILITY,JOINT_VS_MARGINAL,NULL_HYPOTHESIS}.md` — atlas updates (6 files)
- `glossary/SYNONYMS.md` — new vocabulary rows
- `glossary/ANTISYNONYMS.md` — new divergence entries

## Estimated Volume

| Activity | Count |
|----------|-------|
| Search queries (Waves 1-4) | ~35 |
| Citation graph traversals | 1-2 |
| Papers triaged (abstracts read) | 50-70 |
| New papers annotated via `/annotate` | 10-15 |
| Inbox + "to find" papers annotated | 8-10 |
| Total new annotations | 18-25 |
| SYNONYMS.md updates | 5-10 new rows |
| ANTISYNONYMS.md updates | 2-5 new entries |
| Atlas file updates | 6 |

## Verification

After all 4 waves:
1. `wc -l papers/by-structure/boundary_operators.md` — neuroscience section should have 3+ entries (currently 0)
2. Every cell in the 30-cell matrix was searched at least once
3. Every cell shows >= 2 annotated papers in the coverage matrix
4. Spot-check 3 annotations: machine instantiation is specific, not vague
5. Verify SYNONYMS.md empty cells that could be filled by new papers
6. Inbox "to find" list is either annotated or explicitly deprioritized with reason
7. `wc -l papers/by-domain/{qec,neuroscience}.md` — both should show growth
