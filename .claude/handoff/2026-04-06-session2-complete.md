# Handoff: Post-Scratch Consolidation — Session 2 Complete

**Date**: 2026-04-06 (session 2)
**Project**: ~/topoyolo (topo-rosetta)
**Previous handoff**: `2026-04-06-scratch-complete.md` (session 1 — the 4-wave scratch execution)

---

## What Was Accomplished This Session

### Phase 1: Atlas File Updates (ALL 6 DONE)

Every atlas file now references all relevant papers from both session 1 (17 papers) and session 2 (4 papers). Zero "in inbox" tags remain anywhere in the atlas.

| Atlas File | Changes Made |
|---|---|
| `atlas/CHAIN_COMPLEX.md` | +8: Reimann, Dabaghian, Curto & Itskov, Giusti (updated), Gardner (updated), Kitaev, Dennis, Baudot-Bennequin, Bradley, Freedman-Kitaev-Wang, Bombin. Incarnation count → 7. Neural added as 7th incarnation with undirected/directed sub-flavors. |
| `atlas/PARAMETERIZED_HOMOLOGY.md` | +3: Harrington (multiparameter PH), Perea & Harer (SW1PerS), Kolchinsky (RB curve) |
| `atlas/MATCHING.md` | +4: Divol & Lacombe (PD=OT), Kitaev (anyon fusion), Dennis (MWPM), Wong & Yang (info-geo↪OT), Cross-Barcode |
| `atlas/STABILITY.md` | +2: Cohen-Steiner updated from "in inbox", Dennis (threshold=gauge theory), Freedman (e^{-αℓ}), Bombin (p_c≈0.109) |
| `atlas/NULL_HYPOTHESIS.md` | +2: Vejdemo-Johansson (universal PH null), Dennis (uncorrected evolution), Freedman (Abelian null), Bombin (factorized state) |
| `atlas/JOINT_VS_MARGINAL.md` | +5: Harrington (bifiltration), Kolchinsky (PID=IB), Schreiber (TE), Tort updated, Tononi IIT 3.0, Barannikov Cross-Barcode |

### Phase 2: Search + Annotate (4 NEW papers)

| Paper | arXiv/DOI | Machines | Filed to |
|---|---|---|---|
| Freedman, Kitaev, Larsen, Wang (2001) — Topological Quantum Computation | quant-ph/0101025 | chain, stability, matching, null | qec.md, boundary_operators.md, phase_transitions.md |
| Barannikov et al. (2021) — Cross-Barcode / MTop-Divergence | 2106.04024 | joint, param, matching, null | tda.md, composite_systems.md |
| Bombin & Martin-Delgado (2007) — Color Codes | 0711.0468 | chain, stability, null, joint | qec.md, boundary_operators.md, phase_transitions.md |
| Oizumi, Albantakis, Tononi (2014) — IIT 3.0 | 10.1371/journal.pcbi.1003588 | joint, null, stability, param | neuroscience.md, composite_systems.md, phase_transitions.md |

"Still to find" list reduced from 6 → 2 (Ay-Polani, Riehl).

### Phase 3: Glossary + Bridges

- `papers/cross_domain_bridges.md` — 7 new bridge entries
- `glossary/SYNONYMS.md` — 4 cells updated (TDA null distribution, TDA/neuro excess, QEC/TDA/info matching)
- `glossary/ANTISYNONYMS.md` — 2 new divergences (Cross-Barcode≠Wasserstein PD comparison; color code Z₂×Z₂≠toric code Z₂)

### Files Modified (18 total)

```
atlas/CHAIN_COMPLEX.md              — 8+ paper references added
atlas/PARAMETERIZED_HOMOLOGY.md     — 3 paper references added
atlas/MATCHING.md                   — 4+ paper references added
atlas/STABILITY.md                  — 4 paper references added/updated
atlas/NULL_HYPOTHESIS.md            — 4 paper references added
atlas/JOINT_VS_MARGINAL.md          — 5+ paper references added/updated
papers/inbox.md                     — 4 new full annotations, "still to find" updated
papers/by-domain/qec.md             — 2 new entries (Freedman, Bombin)
papers/by-domain/tda.md             — 1 new entry (Cross-Barcode)
papers/by-domain/neuroscience.md    — 1 new entry (Tononi IIT 3.0)
papers/by-structure/boundary_operators.md — 2 new entries + incarnation count fixed
papers/by-structure/composite_systems.md  — 2 new entries (Cross-Barcode, Tononi)
papers/by-structure/phase_transitions.md  — 3 new entries (Freedman, Bombin, Tononi)
papers/cross_domain_bridges.md      — 7 new bridge entries appended
glossary/SYNONYMS.md                — 4 cells updated
glossary/ANTISYNONYMS.md            — 2 new entries
```

---

## Coverage Matrix (Current State)

```
              Chain    Param   Match   Stabil  Joint   Null
TDA            4+       5+      3+      5+      3+      3+
QEC            9+       5+      5+      6+      5       6+
Dynamics       7+       9+     10+      5+      4+      5+
Neuro          4+       8+      5       5+     11+      8+
InfoTheo       8+       7+      3+      4+      9+      6+
```

All cells ≥ 3. The weakest cell remains **Match×Neuro** (5 papers but none from OT/alignment literature — all from third-pass triage of opponent pairing, conformal HD, driver fatigue GC).

---

## REMAINING WORK — ALL ITEMS, PRIORITIZED

### Tier 1: Inbox Backlog — Papers with Only Light Annotations (5 papers)

These exist in `papers/inbox.md` under "Core ATT papers" and "Papers to annotate" with 1-2 line descriptions only. They need full structured annotations via `/annotate`.

**1. Gardner et al. (2022)** — "Toroidal topology of population activity in grid cells" (Nature)
- **Why it matters**: The torus IS both the neural manifold (neuroscience) and the toric code base space (QEC). This is the single strongest neuro↔QEC bridge paper.
- **Fills**: Chain×Neuro (strengthen), cross-domain bridge
- **Blocker**: Not on arXiv. Nature paper. Previous session's OpenAlex search didn't surface it by title.
- **Search to try**:
  ```bash
  cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source semantic-scholar,openalex "Gardner Hermansen Pachitariu Burak toroidal grid cells Nature 2022"
  ```
  Or fetch directly: `WebFetch("https://www.nature.com/articles/s41586-021-04268-7", "Extract full abstract, authors, methods summary")`
- **Estimated DOI**: `10.1038/s41586-021-04268-7`

**2. Xi et al.** — "TE + directed PH in spiking systems"
- **Why it matters**: Rare triple-domain paper (Neuro+TDA+InfoTheo). Combines transfer entropy with directed persistent homology.
- **Fills**: Chain+Param+Null × Neuro/TDA/Info
- **Blocker**: No arXiv ID or DOI known. Title may be approximate.
- **Search to try**:
  ```bash
  cd ~/link-forge && npx tsx scripts/search-papers.ts --max 10 --source arxiv,semantic-scholar,openalex "transfer entropy directed persistent homology spiking neural"
  ```
  Also try broader: `"directed simplicial complex spike train information flow"`

**3. Tsuda (2001)** — "Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems"
- **Why it matters**: Foundational paper for chaotic itinerancy = attractor switching as parameterized homology.
- **Fills**: Param × Neuro/Dyn
- **Found at**: Behavioral and Brain Sciences, Cambridge. OpenAlex confirmed the title+URL in session 2.
- **URL for WebFetch**: `https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/toward-an-interpretation-of-dynamic-neural-activity-in-terms-of-chaotic-dynamical-systems/79BCBA39780C43EEC91EEADF4A89F9F0`
- **Action**: `WebFetch` the URL, then write annotation to inbox.md

**4. Sugihara et al.** — Convergent Cross-Mapping (CCM)
- **Why it matters**: Joint-vs-marginal excess via manifold cross-prediction. Foundational causal inference tool.
- **Fills**: Joint×Dyn
- **Title**: Likely "Detecting Causality in Complex Ecosystems" (Science, 2012)
- **Search**: `mcp__arxiv__search_papers(query: au:"Sugihara" AND ti:"causality" AND ti:"ecosystems")` or WebFetch on Science DOI

**5. Adams et al. (2017)** — "Persistence Images: A Stable Vector Representation of Persistent Homology"
- **Why it matters**: Standard TDA featurization method. Param + matching machines.
- **Fills**: Param×TDA, Matching×TDA
- **arXiv ID**: Likely `1507.06217`
- **Action**: `mcp__arxiv__search_papers(query: ti:"persistence images" AND au:"Adams")`

**Lower priority within Tier 1** (foundational but well-known, less likely to reveal new Rosetta mappings):
- Takens (1981) — "Detecting strange attractors in turbulence" (no arXiv)
- Sauer, Yorke, Casdagli (1991) — "Embedology" (no arXiv)
- Bauer (2021) — "Ripser" (computational, likely `2108.03831`)

---

### Tier 2: Retry Rate-Limited Searches (4 cells)

These cells got degraded search results in session 1 due to arXiv API 429 rate limits.

**1. Match × Neuroscience** (weakest cell — needs OT/alignment literature)
```bash
cd ~/link-forge && npx tsx scripts/search-papers.ts --max 10 --source arxiv,semantic-scholar,openalex "optimal transport neural alignment Wasserstein brain decoding hyperalignment"
```
Also:
```bash
cd ~/link-forge && npx tsx scripts/search-papers.ts --max 10 --source arxiv,openalex "Procrustes alignment neural population geometry representational similarity"
```
**Targets**: Haxby et al. (hyperalignment), Churchland (neural trajectories), Graves et al. (Wasserstein for spike trains)

**2. Stabil × QEC** (missing foundational threshold papers)
```
mcp__arxiv__search_papers(query: au:"Aharonov" AND ti:"fault-tolerant", categories: ["quant-ph"])
mcp__arxiv__search_papers(query: au:"Knill" AND au:"Laflamme" AND ti:"threshold", categories: ["quant-ph"])
```
**Targets**: Aharonov & Ben-Or (1997) — original threshold theorem; Knill-Laflamme-Zurek (1998)

**3. Joint × Neuro** (adequate but incomplete — consciousness literature)
```bash
cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source openalex "Mediano beyond integrated information taxonomy information dynamics 2021"
```

**4. Null × Neuro** (adequate — mostly confirmatory)
```bash
cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source openalex "Aru untangling cross-frequency coupling 2015"
```

---

### Tier 3: Wave 3 Triage Candidates (14 papers identified, not annotated)

These papers were surfaced by Wave 3 search agents in session 1 and flagged as passing the triage filter (genuinely new machine instantiation), but were not annotated due to time. Grouped by priority:

**HIGH (fills specific cells or bridges):**

1. **Theiler, Eubank, Longtin, Galdrikian, Farmer (1992)** — "Testing for nonlinearity in time series"
   - THE foundational surrogate data paper. Fills Null×Dyn.
   - Search: `mcp__arxiv__search_papers(query: au:"Theiler" AND ti:"nonlinearity" AND ti:"time series")`
   - Likely not on arXiv (PhysRevA). Try OpenAlex.

2. **Shwartz-Ziv & Tishby (2015/2017)** — "Opening the Black Box of Deep Neural Networks via Information"
   - Origin of the information plane trajectory. Fills Param×Info.
   - arXiv: `1703.00810`
   - Implicitly covered (Geiger, Wickström cite it) but the original is not annotated.

3. **Breuckmann & Eberhardt (2021)** — "Quantum Low-Density Parity-Check Codes"
   - PRX Quantum review of QLDPC. Defines codes via chain complexes. Fills Chain×QEC (landmark survey).
   - Likely arXiv: `2103.06309`

4. **PRX Quantum (2024)** — "Analyzing Prospects for Quantum Advantage in Topological Data Analysis"
   - Literal TDA↔QEC bridge paper. Found in session 1 but not annotated.
   - Search: `mcp__arxiv__search_papers(query: ti:"quantum advantage" AND ti:"topological data analysis")`

**MEDIUM (adds new instantiation or vocabulary):**

5. **Barrett (2015)** — "Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems"
   - PID atoms in dynamical systems. Bridges Joint×Info and dynamics.
   - arXiv: `1410.1532`

6. **Lobier, Siebenhühner, Palva, Palva (2013)** — "Phase transfer entropy: A novel phase-based measure for directed connectivity"
   - Phase TE with surrogate nulls. Bridges Null×Info and Null×Neuro.
   - Not on arXiv. NeuroImage paper.

7. **Shorten, Spinney, Lizier (2021)** — "Estimating Transfer Entropy in Continuous Time Between Neural Spike Trains"
   - Continuous-time TE for spike trains. Null×Info with neuro bridge.
   - arXiv: likely `2002.07762` or similar

8. **Representational drift papers** (Nat Comms 2022, bioRxiv 2020)
   - Topological invariance despite metric-level drift. Fills Stabil×Neuro.
   - Search: `cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source openalex "representational drift topological stability neural population 2022"`

9. **Floquet codes cluster** (2023-2025, multiple papers)
   - Dynamical QEC = parameterized homology where parameter is time-periodic scheduling. Novel Param×QEC.
   - Search: `mcp__arxiv__search_papers(query: ti:"Floquet code", categories: ["quant-ph"], max_results: 5)`

**LOWER (diminishing returns for cells already ≥ 5):**

10. **Topological structure in V1** (2024 iScience)
    - Population activity topology encodes stimulus rotations. Param×Neuro.

11. **Wasserstein distance on climate attractors** (2017)
    - Detecting attractor changes via OT. Match×Dyn bridge.

12-14. Additional papers from Wave 3 agents (see session 1 handoff Priority 5 for details)

---

### Tier 4: "Still to Find" List (2 papers remaining)

1. **Ay & Polani** — Information decomposition (PID)
   - May be redundant with Kolchinsky (2024) already annotated
   - The specific paper is unclear — could be Ay (2015) "Information Geometry" or Polani (2009) "Information Flows in Causal Networks"
   - Low priority given PID coverage (Kolchinsky, Williams-Beer, Chicharro already annotated)
   - Search if time: `cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source openalex "Ay information geometry synergy redundancy decomposition"`

2. **Riehl** — "Category Theory in Context" (textbook)
   - Lowest priority. Methodological reference, not a paper with machine instantiations.
   - Skip unless the atlas needs a formal categorical framework section.

---

### Tier 5: Structural Improvements

1. **METHODOLOGY.md review** — Incarnation count updated to 7 in atlas + by-structure, but METHODOLOGY.md itself may reference older counts.

2. **Link-forge queue processing** — ~100+ papers enqueued into link-forge SQLite during searches. Processing them (`cd ~/link-forge && npm run dev`) would make them searchable via `forge_search`, `forge_concepts`, `forge_related` MCP tools.

3. **Inbox cleanup** — The "Core ATT papers" section (lines 38-69) contains light annotations for 10 papers, some of which (Cohen-Steiner, Giusti) already have full annotations elsewhere in the inbox. These duplicates should be deduplicated or cross-referenced.

4. **by-domain/neuroscience.md line 53** — Stale reference: "Tort et al. (2010) — PAC modulation index. *(In inbox — not yet annotated.)*" This IS now annotated (session 1). Remove the stale note.

---

## Search Tool Notes

- **Best tool**: `~/link-forge/scripts/search-papers.ts` — searches arXiv + Semantic Scholar + OpenAlex in parallel. Usage: `cd ~/link-forge && npx tsx scripts/search-papers.ts --max N --source arxiv,semantic-scholar,openalex "query"`. Papers auto-enqueue (harmless).
- **arXiv MCP**: `mcp__arxiv__search_papers` — good for targeted au:/ti: searches. Rate-limits ~20 queries/session.
- **Semantic Scholar MCP**: `mcp__semantic-scholar__search_semantic_scholar` — rate-limited (429) in session 1. May work in fresh session.
- **Google Scholar MCP**: `mcp__paper-search__search_google_scholar` — user rejected in session 1. Ask before using.
- **Paper reading**: `WebFetch` on arxiv.org abstract pages, Frontiers, PLoS, Nature (open access). APS/Royal Society/Elsevier = 403.
- **Citation traversal**: `mcp__semantic-scholar__get_semantic_scholar_citations_and_references(paper_id: "arXiv:XXXX.XXXXX")`

## Annotation Workflow

For each paper: `/annotate <arXiv ID | DOI | URL>` using skill at `.claude/skills/annotate/SKILL.md`. This produces the structured template (Domain, Machines instantiated with specific mechanisms, What is genuinely new, Connections, Vocabulary mapping) and files into both by-domain/ and by-structure/ indices.

## File Locations

```
~/topoyolo/
├── papers/inbox.md                              — 21 full annotations + 10 light annotations
├── papers/by-domain/
│   ├── tda.md                                   — Wave 2 + Cross-Barcode + Third Pass
│   ├── qec.md                                   — Kitaev, Dennis, Freedman, Bombin + Third Pass
│   ├── dynamical_systems.md                     — Perea & Harer + Third Pass
│   ├── neuroscience.md                          — 4 Wave 1 + Tort + Tononi + Third Pass
│   └── information_theory.md                    — Baudot, Bradley, Kolchinsky, Schreiber, Wong + Third Pass
├── papers/by-structure/
│   ├── boundary_operators.md                    — 7 incarnations documented
│   ├── filtrations.md                           — Perea, Harrington + extensive coverage
│   ├── optimal_transport.md                     — Divol, Wong, Kitaev, Dennis + existing
│   ├── phase_transitions.md                     — Vejdemo-Johansson, Dennis, Cohen-Steiner, Freedman, Bombin, Tononi
│   └── composite_systems.md                     — Harrington, Kolchinsky, Tort, Schreiber, Cross-Barcode, Tononi
├── papers/cross_domain_bridges.md               — 7 new bridge entries (session 2)
├── atlas/                                       — ALL 6 UPDATED (session 2)
│   ├── CHAIN_COMPLEX.md                         — 7 incarnations, full QEC+neuro+info coverage
│   ├── PARAMETERIZED_HOMOLOGY.md                — Harrington, Perea, Kolchinsky added
│   ├── MATCHING.md                              — Divol, Kitaev, Dennis, Wong, Cross-Barcode
│   ├── STABILITY.md                             — Cohen-Steiner updated, Dennis+Freedman+Bombin added
│   ├── NULL_HYPOTHESIS.md                       — Vejdemo-Johansson, Dennis, Freedman, Bombin added
│   └── JOINT_VS_MARGINAL.md                     — Harrington, Kolchinsky, Schreiber, Tononi, Cross-Barcode
├── glossary/
│   ├── SYNONYMS.md                              — 4 cells updated (session 2)
│   └── ANTISYNONYMS.md                          — 26 total entries (2 new in session 2)
└── .claude/handoff/
    ├── 2026-04-06-scratch-all-layers.md         — The original plan
    ├── 2026-04-06-scratch-complete.md           — Session 1 handoff
    └── 2026-04-06-session2-complete.md          — THIS FILE
```

## Total Paper Count

| Category | Count |
|---|---|
| Full structured annotations (inbox.md) | 21 |
| Light annotations (Core ATT, inbox) | 10 |
| Filed in by-domain/ | 131+ entries across 5 files |
| Filed in by-structure/ | 131+ entries across 5 files |
| Cross-domain bridges | 14+ entries |
| Second/third pass annotations | 91 across 3 files |
| **Total unique papers in system** | **~170+** |
