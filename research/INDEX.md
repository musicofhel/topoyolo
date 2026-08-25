# topo-rosetta RW loop — INDEX

**Branch:** `loop/atlas-structure-v1` (never pushed; Aaron reviews/merges)
**Lint:** `python3 scripts/check_structure.py --check` → **0 errors**, 25
warnings (gen_stats domain-alias notes — pre-existing debt class).
Derived truth: **77 fully annotated papers**.

## Task status
- A1 structure lint tool — **done 2026-08-24 (e6d03df)**
- A2 cross-ref/link debt paydown — **done 2026-08-24 (6f10501+b673c24)**
- A3 per-paper annotation files — **done 2026-08-24**. Carried debt: ~51 full
  annotations live as prose blocks in by-domain/by-structure index files;
  B2 promotes-on-encounter. Wrong-pointer instances in
  `by-structure/optimal_transport.md` FIXED pass 14 (5 repointed to their own
  annotation files); prose-block debt itself remains.
- A4 stats from data — **done 2026-08-24 (a49e738+db97bca)**. Thin cells:
  Dynamics×Matching (=4), QEC×JointMarg (=2) → B2 targets. README/docs count
  drift fixed pass 14 (77 / 20 cells ≥10, min cell 2).
- A5 loose-file adjudication — **done 2026-08-24 (61fee02)**.
- A6 SEPARATRIX review — **done 2026-08-24** (accept-directionally, gates G1–G3).
- **Phase A COMPLETE. Phase B UNLOCKED.**
- B1 ingestion contract — **done 2026-08-24 (6ebfcf2)**.
- B2 consume queue batches — **in_progress: slices 1–5 done.**
  batch-001 FULLY CONSUMED 21/21 (8 annotated, 13 rejected). **batch-002
  STARTED pass 14: candidates 01–03 REJECTED (geometric-dl wrappers, zero
  machines); 37 of 40 queued.** Lint --check 0 errors.
- B3 atlas synthesis touch-ups — open (after ~15 new papers).

## Reports (newest first)
- [2026-08-25-0235](2026-08-25-0235.md) — Pass 14 / B2 slice-5: batch-002 opened, candidates 01–03 rejected; 5 blahut-class wrong-pointers fixed; README/docs counts patched to 77; Dynamics×Matching still thin at 4.
- [2026-08-25-0221](2026-08-25-0221.md) — Pass 13 / B2 slice-4: batch-001 emptied (21/21); fresh annotations ying-2016, liu-2025, brusch-2023, silva-2018; 10 triage-rejections; Dynamics×Matching strengthened.
- [2026-08-25-0205](2026-08-25-0205.md) — Pass 12 / B2 slice-3: candidates 08, 04, 05 promoted from hidden prose (Fasoli pcbi.1013995, GC-STCL wang-2024, Simpson simpson-2013); content conserved; lint to 0 warnings.
- [2026-08-25-0007](2026-08-25-0007.md) — Pass 11 / B2 slice-2: candidate-13 annotated (2604.08539, Matching+Stability), 01+14 rejected; stats 70 papers.
- [2026-08-24-2358](2026-08-24-2358.md) — Pass 10 / B1 DONE + B2 slice-1: INGESTION.md + queue-hygiene lint; candidate-21 promotion; 51-block prose-annotation debt quantified.
- [2026-08-24-2353](2026-08-24-2353.md) — Pass 9 / A6 DONE: SEPARATRIX PR #1 review.
- [2026-08-24-2345](2026-08-24-2345.md) — Pass 8 / A5 DONE: layout contract + lint enforcement.
- [2026-08-24-0840](2026-08-24-0840.md) — Pass 7 / A4 DONE: gen_stats.py + coverage-matrix regen + --check drift gate.
- [2026-08-24-0737](2026-08-24-0737.md) — Pass 6 / A3 slice 4 DONE: Waves 4c–10c migrated, inbox reshaped, lint enforces empty inboxes.
- [2026-08-24-0730](2026-08-24-0730.md) — Pass 5 / A3 slice 3: archive Phase 2 migrated (9 files).
- [2026-08-24-0723](2026-08-24-0723.md) — Pass 4 / A3 slice 2: Wave 4b + Wave 3 triage (7 files).
- [2026-08-24-0713](2026-08-24-0713.md) — Pass 3 / A3 slice 1: Waves 1–2 migrated.
- [2026-08-24-0701](2026-08-24-0701.md) — Pass 2 / A2: crossref debt cleared.
- [2026-08-24-0650](2026-08-24-0650.md) — Pass 1 / A1: lint tool committed + baseline census.
