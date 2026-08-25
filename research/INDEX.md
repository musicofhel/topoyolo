# research/INDEX.md — pass reports + task status (newest first)

**Lint state:** check_structure.py exit 0; 1 warning = pre-existing baseline
(2 author-year-prose crossrefs); `--check` 0 errors. Derived corpus: **134
fully annotated papers** (+3 pass 41), **36 cells (6 machines × 6 domains)**,
min cell 2, 28 cells ≥10. Domain-alias table landed in gen_stats.py (pass 27);
ML→InfoTheo and OT→TDA mappings await Aaron's ratification.

## Reports
- `2026-08-25-0803.md` — Pass 41: B2 — batch-007 **qec-mwpm group CLOSED 6/6**:
  04 Baireuther et al RNN decoder 1705.07855 (joint-vs-marginal as decoder
  advantage); 05 Hack et al BP-on-decoding-graph 2603.05381 (carrier-graph fix,
  ldpc-bp lineage); 06 Fowler et al 1202.5602 (O(n²) average-case anchor of
  exact MWPM). Promote-on-encounter check vs RNN-decoder authors clean. Counts
  to derived 134, deep cells 28.
- `2026-08-25-0758.md` — Pass 40: B2 — batch-007 opened, qec-mwpm slice 3/12
  all ANNOTATED (01 Higgott–Gidney sparse blossom 2303.15933; 02 Pattison et
  al. soft info 2107.13589 — joint-vs-marginal gain in decoder form; 03
  Higgott et al. belief-matching 2203.04948 + fragile boundaries). Counts to
  derived 131; README line-5/line-9 count drift found and fixed.
- `2026-08-25-0752.md` — Pass 39: B2 — batch-002 HELD re-triage DONE: all
  22 held candidates (19–40) triaged machines-first; 3 ANNOTATED (2601.01359
  VR-shadow inverse limits; Wong–Vong PHGCN diagram loss; de Silva–Carlsson
  witness complexes), 19 REJECTED (<2 machines). Counts to derived 128.
- `2026-08-25-0749.md` — Pass 38: B3 sub-slice 4 — optimal_transport.md
  "Monge–Kantorovich split inside this file": coupling-side vs map-side corpus
  instances catalogued; Mémoli–Needham non-atomic GM=GW read as the regime
  theorem (split bites only on atomic instances).
- `2026-08-25-0735.md` — Pass 37: B2 slice-37 — **batch-006 CLOSED 8/8**
  (07 Beier et al 2112.11964 linear-GW REJECTED, <2 machines; 08 Wollstadt
  et al ANNOTATED as 2203.10810) + B3 sub-slice 3 (MATCHING.md cross-machine
  roles). Counts to derived 125.
- `2026-08-25-0731.md` / `2026-08-25-0726.md` — Passes 35–36: batch-006
  gw-theory core (2006.12287, 2212.14123, 2201.09385, 2507.01171, 2606.10295,
  2608.09265). Counts to derived 121.
- `2026-08-25-0723.md` / `2026-08-25-0718.md` — Passes 33–34: batch-005
  CLOSED 12/12 + B3 sub-slices 1–2 (ANTISYNONYMS Matching↔Stability duality;
  thermodynamic-instantiation sections on optimal_transport +
  composite_systems).
- Earlier (`2026-08-25-07*`, `2026-08-24-*`): batch-004 CLOSED, channel-capacity
  + ph-stability groups, Phase A complete (A1–A6), B1 done, gen_stats follow-up.

## Task status (LOOP_MISSION.md ledger is canonical)
- **A1–A6:** all [done].
- **B1 ingestion contract:** [done] (6ebfcf2).
- **B2 queue consumption:** [in_progress] — batch-007 open: qec-mwpm group
  CLOSED 6/6 (passes 40–41); null-surrogate group candidates 07–12 untouched
  (next default slice). Promote-on-encounter checks ran clean both passes.
  Residual Wave-era catch-all pointer debt (~101, ≤5/pass sanctioned).
- **B3 atlas synthesis:** [in_progress] — sub-slices 1–4 done (passes 33, 34,
  37, 38); queued hooks exhausted. Next option per orchestrator: a two-parameter
  refinement hook under PARAMETERIZED_HOMOLOGY, may alternate with batch-007
  slices at pass judgment.
