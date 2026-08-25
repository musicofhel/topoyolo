# topo-rosetta RW loop — INDEX

**Branch:** `loop/atlas-structure-v1` (never pushed; Aaron reviews/merges)
**Lint:** `python3 scripts/check_structure.py` → exit 0, 0 errors, 0 warnings.
`--check` mode also green: stats derived from papers/annotations/ match README /
docs/index.html / diagrams/coverage-matrix.md (68 fully annotated papers, 18/30
cells ≥10, min cell 1).

## Task status
- A1 structure lint tool — **done 2026-08-24 (e6d03df)**
- A2 cross-ref/link debt paydown — **done 2026-08-24 (6f10501+b673c24)**
- A3 per-paper annotation files — **done 2026-08-24** (slices 1–4: 1c96d87,
  5771173, 4b6db24, aa06188+9d5be1d+dec8b5f). All full annotations now
  per-paper in `papers/annotations/` (68 files, verbatim-migrated, conservation
  proven). Carried: Blahut+Arimoto stays ONE shared file; author-year fallback
  tightening still queued.
- A4 stats from data — **done 2026-08-24 (a49e738+db97bca)**. gen_stats.py derives
  matrix + headline counts from annotations, regenerates coverage-matrix.md;
  README/docs patched to derived truth; `--check` fails lint on drift.
  Thin cells exposed: Dynamics×Matching=1, QEC×JointMarg=2 → B2 targets.
- A5 loose-file adjudication — **done 2026-08-24 (61fee02)**. papers/README.md
  layout contract; five loose files = historical search-pass ledgers (67 SP/TP
  candidates), promotion-not-deletion rule; lint now fails on undocumented
  papers/ entries. Carried to B: promote Mollers-2023 + Mézard–Mora (index
  prose crossrefs with no annotation file).
- A6 SEPARATRIX review — **done 2026-08-24 (recommendation only; merge is
  Aaron's)**. Verdict: ACCEPT DIRECTIONALLY as PROPOSED 7th machine, gated on
  G1 sharpen signature/demote margin, G2 ANTISYNONYMS stub vs Stability,
  G3 no integration until ≥3 cited papers annotated in B2. If merged:
  follow-up task to extend gen_stats.py to 7 columns (+ possible ML domain).
  Details: research/2026-08-24-2353.md.
- **Phase A COMPLETE. Phase B UNLOCKED.**
- B1 ingestion contract — open (NEXT): papers/INGESTION.md + queue-hygiene lint.
  batch-001 (21 candidates, commit 27d8938) stays unconsumed until B1 exists.

## Reports (newest first)
- [2026-08-24-2353](2026-08-24-2353.md) — Pass 9 / A6 DONE: SEPARATRIX PR #1 review from orchestrator export; accept-directionally recommendation with three gates; answers to PR's Q1–Q3; gen_stats 7-column follow-up flagged.
- [2026-08-24-2345](2026-08-24-2345.md) — Pass 8 / A5 DONE: papers/README.md layout contract + lint enforcement; ledgers documented not folded; new debt class found (index→annotation gap).
- [2026-08-24-0840](2026-08-24-0840.md) — Pass 7 / A4 DONE: gen_stats.py + regenerated coverage-matrix.md, README/docs stats to derived truth (68 papers vs old 219 — delta explained), --check drift gate proven live.
- [2026-08-24-0737](2026-08-24-0737.md) — Pass 6 / A3 slice 4 DONE: Waves 4c–10c migrated (36 verbatim files incl. blahut-arimoto-1972), 149 crossrefs repointed, inbox reshaped to contract+leads+wave index, lint enforces empty inboxes. A3 flipped done.
- [2026-08-24-0730](2026-08-24-0730.md) — Pass 5 / A3 slice 3: archive Phase 2 migrated (9 verbatim files), 4 Core ATT stubs repointed.
- [2026-08-24-0723](2026-08-24-0723.md) — Pass 4 / A3 slice 2: Wave 4b + Wave 3 triage migrated (7 files), 16 crossrefs repointed.
- [2026-08-24-0713](2026-08-24-0713.md) — Pass 3 / A3 slice 1: Waves 1–2 migrated to per-paper files, 28 stale inbox pointers fixed.
- [2026-08-24-0701](2026-08-24-0701.md) — Pass 2 / A2: crossref debt cleared, 60 headers parse.
- [2026-08-24-0650](2026-08-24-0650.md) — Pass 1 / A1: lint tool committed + baseline census.
