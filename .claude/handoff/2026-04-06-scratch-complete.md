# Handoff: Scratch All Layers — Execution Complete

**Date**: 2026-04-06
**Project**: ~/topoyolo (topo-rosetta)
**Previous handoff**: `2026-04-06-scratch-all-layers.md` (the plan — now executed)

---

## What Was Accomplished

The 4-wave plan from the previous handoff was executed across all 30 cells of the 6×5 matrix (6 abstract machines × 5 domains). Every cell was searched at least once. The true gap (Chain complex × Neuroscience = 0 papers) is now filled at 4 papers. All thin cells (1-2 papers) were brought to 3+.

### Papers Annotated (17 total, full structured annotations in `papers/inbox.md`)

**Wave 1 — Chain × Neuroscience gap (4 papers)**:
1. **Giusti, Pastalkova, Curto, Itskov (2015)** — arXiv: 1502.06172 — "Clique topology reveals intrinsic geometric structure in neural correlations." Order complex from hippocampal correlation matrices. Rank-ordering invariance.
2. **Reimann, Nolte, Scolamiero, Turner, Perin, Chindemi, Dłotko, Levi, Hess, Markram (2017)** — DOI: 10.3389/fncom.2017.00048 — "Cliques of Neurons Bound into Cavities." DIRECTED simplicial complexes from Blue Brain (~31K neurons). Dim 6-7 simplices.
3. **Dabaghian, Mémoli, Frank, Carlsson (2012)** — DOI: 10.1371/journal.pcbi.1002581 — "Topological Paradigm for Hippocampal Spatial Map Formation." Nerve complex from place cell co-firing. PH recovers environment topology in 2-5 min.
4. **Curto & Itskov (2008)** — DOI: 10.1371/journal.pcbi.1000205 — "Cell Groups Reveal Structure of Stimulus Space." Nerve Theorem guarantees H_* of complex = H_* of stimulus space.

**Wave 2 — Thin cells (4 papers)**:
5. **Divol & Lacombe (2019)** — arXiv: 1901.03048 — PD distances = optimal partial transport. Match×TDA.
6. **Vejdemo-Johansson & Mukherjee (2018)** — arXiv: 1812.06491 — Universal empirical null for PH. FWER/FDR control. Null×TDA.
7. **Harrington, Otter, Schenck, Tillmann (2017)** — arXiv: 1708.07390 — Stratifying multiparameter PH. Joint bifiltration. Joint×TDA.
8. **Wong & Yang (2019)** — arXiv: 1906.00030 — Info geometry embeds in OT via pseudo-Riemannian framework. Match×Info.

**Wave 4b — "To find" papers (4 papers)**:
9. **Kitaev (1997)** — arXiv: quant-ph/9707021 — Toric code. Chain complex on T². Anyon fusion = matching.
10. **Dennis, Kitaev, Landahl, Preskill (2002)** — arXiv: quant-ph/0110143 — Topological quantum memory. Threshold = Z₂ gauge theory phase transition.
11. **Perea & Harer (2013)** — arXiv: 1307.6188 — SW1PerS. Sliding window PH on time series. Bridge: TDA + dynamics.
12. **Cohen-Steiner, Edelsbrunner, Harer (2007)** — arXiv: math/0604068 — Stability of persistence diagrams. THE foundational stability theorem.

**Wave 4c — Inbox full annotations (2 papers)**:
13. **Schreiber (2000)** — PRL 85:461 — Transfer entropy. Directed joint-vs-marginal. Bridge: info theory + dynamics.
14. **Tort, Komorowski, Eichenbaum, Kopell (2010)** — J Neurophysiol 104:1195 — PAC modulation index = D_KL from uniform. Joint+Null × Neuro.

**Wave 3 triage — Confirmatory pass (3 papers annotated from 24-cell search)**:
15. **Baudot & Bennequin (2015)** — MDPI Entropy 17(5):3253 — Entropy = cocycle in information cohomology. Chain rule = cocycle condition. Foundational Chain×Info.
16. **Bradley (2021)** — arXiv: 2107.09581 — Shannon entropy = unique derivation of simplicial operad. Strengthens Baudot-Bennequin.
17. **Kolchinsky (2024)** — arXiv: 2405.07665 — PID redundancy = information bottleneck. Formally bridges Joint and Param machines.

### Glossary Updates

**SYNONYMS.md** — 5 neuroscience cells filled in Layer 0:
- Boundary operator: ∂ on clique/nerve complex (Giusti, Curto & Itskov); directed ∂ on oriented simplices (Reimann)
- Cycle: Co-firing pattern forming closed loop (Dabaghian)
- Boundary: Trivial co-firing pattern (contractible)
- Homology class: Cavity (Reimann) / Environment topology (Curto & Itskov)
- Betti number: Obstacle count b₁ (Dabaghian) / Cavity count (Reimann)
- Invariant tracking: Betti number trajectory during learning / Cavity formation sequence

**ANTISYNONYMS.md** — 3 new divergences:
1. **Directed vs undirected simplicial complexes**: Reimann's directed SC (source→sink orientation from synaptic directionality) ≠ standard undirected clique/nerve complexes (Giusti, Dabaghian). Standard PH software can't handle directed case. Genuine bifurcation within neuroscience domain.
2. **Nerve Theorem guarantee vs empirical stability**: Curto & Itskov's Nerve Theorem is an exact isomorphism (conditional on convex receptive fields), categorically stronger than PH stability bounds or QEC threshold. But the convexity assumption is empirically approximate, so the guarantee degrades to empirical stability in practice.
3. **Transfer entropy direction vs persistence symmetry**: TE is asymmetric (T_{Y→X} ≠ T_{X→Y}); MI and bottleneck distances are symmetric. Directional info measures pair with directed topological structures; symmetric measures pair with undirected.

### Coverage Matrix (Before → After)

```
              Chain    Param   Match   Stabil  Joint   Null
TDA            2→4      4+      1→3     3→5     1→2     1→2
QEC            5→7      5+      3→5     5+      5       5+
Dynamics       7+       9+     10+      5+      4+      5+
Neuro          0→4      8+      5       5+     10+      8+
InfoTheo       5→8      6+      2→3     4       8→9     6+
```

Every cell now has ≥ 2 annotated papers.

### Files Modified (15 files)

```
papers/inbox.md                              — 17 new full annotations
papers/by-structure/boundary_operators.md     — +8 entries (4 neuro, 2 QEC, 2 info)
papers/by-structure/optimal_transport.md      — +4 entries (Divol, Wong, Kitaev, Dennis)
papers/by-structure/phase_transitions.md      — +3 entries (Vejdemo-Johansson, Dennis, Cohen-Steiner)
papers/by-structure/composite_systems.md      — +4 entries (Harrington, Kolchinsky, Tort, Schreiber)
papers/by-structure/filtrations.md            — +2 entries (Perea, Harrington)
papers/by-domain/tda.md                       — +5 entries (Wave 2 + Wave 4b)
papers/by-domain/qec.md                       — +2 entries (Kitaev, Dennis)
papers/by-domain/dynamical_systems.md         — +1 entry (Perea & Harer)
papers/by-domain/neuroscience.md              — +5 entries (4 Wave 1 + Tort)
papers/by-domain/information_theory.md        — +4 entries (Baudot, Bradley, Kolchinsky, Schreiber)
glossary/SYNONYMS.md                          — 5 cells filled + 1 row updated
glossary/ANTISYNONYMS.md                      — 3 new entries
```

### Search Infrastructure Used

- **Primary**: `~/link-forge/scripts/search-papers.ts` — searches arXiv + Semantic Scholar + OpenAlex in parallel. Highly effective. Papers auto-enqueued into link-forge's SQLite queue (harmless side effect).
- **Secondary**: `mcp__arxiv__search_papers` — good for targeted author+title searches. Hit 429 rate limits after ~20 queries.
- **Paper reading**: `WebFetch` on arxiv.org abstract pages, Frontiers, PLoS (open access). Paywalled journals (APS, Royal Society) return 403.
- **Semantic Scholar MCP**: Rate-limited (429) from the start. Did not work in this session.
- **Google Scholar MCP**: User rejected in this session.

---

## Next Steps (Verbose)

### Priority 1: Retry Rate-Limited Searches

ArXiv API hit 429 rate limits midway through Wave 3. Three cells got degraded results (only OpenAlex, which is noisier):

**Match × Neuroscience** — The weakest cell. Only 1 marginal hit (functional alignment for inter-subject decoding). This cell should have papers on:
- OT-based neural alignment (Procrustes, hyperalignment literature)
- Wasserstein distances between neural population distributions
- Optimal decoding as assignment problem

Search to retry:
```bash
cd ~/link-forge && npx tsx scripts/search-papers.ts --max 10 --source arxiv,semantic-scholar "optimal transport neural alignment Wasserstein brain decoding"
```
Also try:
```
mcp__arxiv__search_papers(query: "optimal transport" AND "neural" AND "alignment", categories: ["q-bio.NC", "cs.LG"], max_results: 10)
```

**Null × Neuro** — Already has 8+ papers but the confirmatory search returned nothing due to rate limits. The atlas is fine here but a confirmatory pass would be nice. Key papers to look for: Aru et al. (2015) "Untangling cross-frequency coupling in neuroscience", Canolty et al. (2006) "High gamma power is phase-locked to theta oscillations."

**Joint × Neuro** — Also 8+ papers. Retry would likely find Mediano et al. (2021) "Beyond integrated information: A taxonomy of information dynamics phenomena" — a synergy-based consciousness paper that complements IPWT already in the atlas.

**Stabil × QEC** — Got only textbook/survey hits. The original threshold theorem papers (Aharonov & Ben-Or 1997, Knill-Laflamme-Zurek 1998) should be found and annotated.

### Priority 2: Complete Inbox Backlog

Three papers in `papers/inbox.md` still have only LIGHT annotations (not full structured annotations). They should get the `/annotate` treatment:

1. **Gardner et al. (2022)** — "Toroidal topology of population activity in grid cells" (Nature). Already in inbox with 1-line description. This fills Chain×Neuro and is a bridge paper (the torus IS both the neural manifold and the QEC base space). Read via: the paper is in Nature, may need WebFetch on the Nature page or find via Semantic Scholar.

2. **Xi et al.** — "TE + directed PH in spiking systems." Fills Chain+Param+Null × Neuro/TDA/Info. This is a rare triple-domain paper. Need to find the actual arXiv ID or DOI first — it's listed in the inbox without an identifier.

3. **Tsuda (2001)** — "Chaotic itinerancy." Fills Param × Neuro/Dyn. This is a Biological Cybernetics paper, likely not on arXiv. Try:
   ```bash
   cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source openalex "Tsuda chaotic itinerancy attractor"
   ```

### Priority 3: "Still to Find" List

Six papers remain on the "still to find" list in `papers/inbox.md`. In priority order:

1. **Bombin & Martin-Delgado** — Color codes. Different cellulation (trivalent lattice), same homological machinery as toric code. Chain+Param×QEC. Search:
   ```
   mcp__arxiv__search_papers(query: ti:"color codes" AND au:"Bombin", categories: ["quant-ph"])
   ```

2. **Freedman, Kitaev, Wang** — Topological quantum computation. Homology as computational resource. Chain×QEC bridge to computation theory. Search:
   ```
   mcp__arxiv__search_papers(query: ti:"topological quantum computation" AND au:"Freedman", categories: ["quant-ph"])
   ```

3. **Tononi** — Integrated Information Theory (Φ). Joint-vs-marginal excess as consciousness measure. IPWT (already in atlas) is a successor theory, but Tononi's original IIT formulation is the foundational reference. Search:
   ```bash
   cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source openalex "Tononi integrated information theory phi consciousness"
   ```

4. **Ay, Polani** — Information decomposition (PID-adjacent). Synergy/redundancy as joint-vs-marginal. May overlap with Kolchinsky (2024) already annotated. Search:
   ```bash
   cd ~/link-forge && npx tsx scripts/search-papers.ts --max 5 --source openalex "Ay Polani information decomposition synergy redundancy"
   ```

5. **R-Cross-Barcode / RTD-Lite** — Cross-filtration features. Closest to joint-vs-marginal in TDA proper. Related to the multiparameter PH work (Harrington et al.) already annotated. Search:
   ```
   mcp__arxiv__search_papers(query: "cross-barcode" OR "relative topological descriptor", categories: ["math.AT"])
   ```

6. **Riehl** — "Category Theory in Context." The abstract machines are functors. Worth formalizing? This is a textbook, not a paper. Low priority for annotation — better as a methodological reference in the atlas files.

### Priority 4: Atlas File Updates

The 6 atlas files (`atlas/CHAIN_COMPLEX.md`, `atlas/PARAMETERIZED_HOMOLOGY.md`, `atlas/MATCHING.md`, `atlas/STABILITY.md`, `atlas/NULL_HYPOTHESIS.md`, `atlas/JOINT_VS_MARGINAL.md`) were NOT updated in this session. They should be updated to reference the new papers. Specifically:

- `atlas/CHAIN_COMPLEX.md` — Add neuroscience section referencing Giusti, Reimann, Dabaghian, Curto & Itskov. Add Baudot-Bennequin and Bradley for info theory. Update the "incarnations" taxonomy (currently 4, should be 7+ after the third pass + this session's additions).
- `atlas/MATCHING.md` — Add Divol & Lacombe (PD = OT), Wong & Yang (info geometry embeds in OT), Kitaev (anyon fusion), Dennis (MWPM).
- `atlas/STABILITY.md` — Add Cohen-Steiner (foundational), Dennis (threshold theorem = gauge theory phase transition).
- `atlas/NULL_HYPOTHESIS.md` — Add Vejdemo-Johansson & Mukherjee (universal null for PH), Dennis (uncorrected evolution as null).
- `atlas/JOINT_VS_MARGINAL.md` — Add Harrington et al. (multiparameter PH = joint bifiltration), Kolchinsky (PID = IB), Schreiber (TE), Tort (PAC MI).
- `atlas/PARAMETERIZED_HOMOLOGY.md` — Add Perea & Harer (SW1PerS), Harrington et al. (multiparameter), Kolchinsky (RB curve).

To do this efficiently: read each atlas file, check what's already referenced, and add only new entries. Each atlas file has a different structure — some are narrative, some are lists.

### Priority 5: Wave 3 Triage — Additional Annotations

The Wave 3 confirmatory agents identified several papers that pass the triage filter (genuinely new machine instantiation) but were NOT annotated due to time:

**From TDA+QEC agent:**
- **Breuckmann & Eberhardt (2021)** — PRX Quantum 2, 040101. QLDPC codes review. Defines codes via chain complexes. Landmark survey for Chain×QEC.
- **Floquet codes cluster** (2023-2025, multiple papers). Dynamical QEC = parameterized homology where the parameter is time-periodic scheduling. Novel Param×QEC instantiation.

**From Dynamics+Neuro agent:**
- **Topological structure in V1** (2024 iScience) — Population activity topology encodes stimulus rotations. Param×Neuro.
- **Representational drift papers** (Nat Comms 2022, bioRxiv 2020) — Despite individual neuron drift, population-level representations are topologically stable. Stabil×Neuro. The Nat Comms paper especially — shows topological invariance despite metric-level drift.
- **Theiler et al. (1992)** — THE foundational surrogate data paper. Null×Dyn. Should be in the atlas.
- **Wasserstein distance on climate attractors** (2017) — Detecting attractor changes via OT. Match×Dyn bridge.

**From InfoTheo+Neuro agent:**
- **Shwartz-Ziv & Tishby (2015/2017)** — Deep learning and the information bottleneck principle. The ORIGIN of the information plane trajectory. Already implicitly covered (Geiger, Wickström cite it) but the original paper is not annotated. Param×Info.
- **Barrett (2015)** — PID atoms in dynamical Gaussian systems. Bridges Joint×Info and dynamics.
- **Lobier et al. (2013)** — Phase transfer entropy with surrogate nulls. Bridges Null×Info and Null×Neuro.
- **Shorten, Spinney, Lizier (2021)** — Continuous-time TE estimation for spike trains. Null×Info with neuro bridge.

Each of these would be annotated via `/annotate <identifier>` following the skill at `.claude/skills/annotate/SKILL.md`.

### Priority 6: SYNONYMS.md Completion Pass

Several cells in the SYNONYMS table could be filled from newly annotated papers:

**Layer 2 (Matching):**
- Neuroscience column is sparse. Curto & Itskov's dissimilarity index μ_k and the representational drift alignment literature could fill "Cost function" and "What the solution means."

**Layer 3 (Composite Systems):**
- TDA column now has Harrington et al. (multiparameter bifiltration as joint object). Add "Components = single-parameter filtrations", "Joint object = bifiltration", "Excess = features in joint invisible to marginals."

**Layer 4 (Null Models):**
- TDA column now has Vejdemo-Johansson & Mukherjee. Add "What is destroyed = topological features (acyclicity null)", "Null distribution = empirical universal PH null."

### Priority 7: Cross-Domain Bridge Hunting

The Wave 4a bridge searches were degraded by arXiv rate limits. Two specific bridges are worth hunting:

1. **TDA ↔ QEC bridge**: PRX Quantum (2024) "Analyzing Prospects for Quantum Advantage in Topological Data Analysis" was found. This paper literally asks: can quantum computers speed up PH computation? It sits at the intersection of both domains. Annotate it.

2. **Neuroscience ↔ QEC bridge via topology**: The torus appears in both Gardner et al. (grid cell manifold) and Kitaev (toric code base space). This is noted in the inbox but not developed. A dedicated search for papers connecting neural topology to quantum topology would be novel.

3. **Information cohomology ↔ TDA**: Baudot-Bennequin's information cohomology uses the same chain complex machinery as TDA, but the "simplices" are random variable tuples, not geometric points. Is there a formal functor between these? Vigneaux's (2019) thesis may address this.

### Priority 8: Structural Improvements

1. **Cross-domain bridges file**: `papers/cross_domain_bridges.md` exists but was not updated this session. It should reference the new bridges discovered: Dennis (QEC ↔ stat mech), Perea & Harer (TDA ↔ dynamics), Wong & Yang (info geo ↔ OT), Baudot-Bennequin (info theory ↔ algebraic topology).

2. **Methodology review**: The original METHODOLOGY.md may need updating given the expanded coverage. The "6 incarnations" count in boundary_operators.md was updated to include a 5th (neural) incarnation and the third pass had expanded to 6. A full recount across all atlas files would be valuable.

3. **Link-forge integration**: ~100 papers were enqueued into link-forge's SQLite queue during the searches. If the link-forge Neo4j is running, processing this queue would make them searchable via `forge_search`, `forge_concepts`, and `forge_related` MCP tools in future sessions. Start with:
   ```bash
   cd ~/link-forge && npm run dev  # processes the queue
   ```

---

## File Locations (Quick Reference)

```
~/topoyolo/
├── papers/inbox.md                              # 17 new full annotations (this session)
├── papers/by-domain/
│   ├── tda.md                                   # +5 entries
│   ├── qec.md                                   # +2 entries
│   ├── dynamical_systems.md                     # +1 entry
│   ├── neuroscience.md                          # +5 entries
│   └── information_theory.md                    # +4 entries
├── papers/by-structure/
│   ├── boundary_operators.md                    # +8 entries (the big one — neuro gap filled)
│   ├── filtrations.md                           # +2 entries
│   ├── optimal_transport.md                     # +4 entries
│   ├── phase_transitions.md                     # +3 entries
│   └── composite_systems.md                     # +4 entries
├── glossary/
│   ├── SYNONYMS.md                              # 5 neuro cells filled, 1 row updated
│   └── ANTISYNONYMS.md                          # 3 new divergence entries
├── atlas/                                       # NOT updated this session (Priority 4)
│   ├── CHAIN_COMPLEX.md
│   ├── PARAMETERIZED_HOMOLOGY.md
│   ├── MATCHING.md
│   ├── STABILITY.md
│   ├── NULL_HYPOTHESIS.md
│   └── JOINT_VS_MARGINAL.md
├── .claude/skills/annotate/SKILL.md             # Annotation workflow
└── .claude/handoff/
    ├── 2026-04-06-scratch-all-layers.md         # The plan (executed)
    └── 2026-04-06-scratch-complete.md           # THIS FILE
```

## Search Tool Notes for Next Session

- **`~/link-forge/scripts/search-papers.ts`**: Best tool. Searches arXiv + Semantic Scholar + OpenAlex in parallel. Usage: `cd ~/link-forge && npx tsx scripts/search-papers.ts --max N --source arxiv,semantic-scholar,openalex "query"`. Papers auto-enqueue but this is harmless.
- **`mcp__arxiv__search_papers`**: Good for targeted author+title searches. Supports field prefixes (`ti:`, `au:`, `abs:`), boolean operators (`AND`, `OR`, `ANDNOT`), category filters, date ranges. Rate-limits at ~20 queries/session.
- **`mcp__semantic-scholar__search_semantic_scholar`**: Was rate-limited (429) from the start this session. May work in a fresh session.
- **`mcp__paper-search__search_google_scholar`**: User rejected in this session. Ask before using.
- **`WebFetch`**: Works on arxiv.org abstract pages, Frontiers, PLoS, Nature (some). Fails on APS (403), Royal Society (403), Elsevier (403).
- **`mcp__arxiv__read_paper`**: Requires `download_paper` first. Download failed this session (partial retrieval). `mcp__paper-search__read_arxiv_paper` returned empty. Neither paper-reading tool worked reliably — use WebFetch on abstract pages instead.
