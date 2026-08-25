# topo-rosetta RW loop — INDEX

**Branch:** `loop/atlas-structure-v1` (never pushed; Aaron reviews/merges)
**Lint:** `python3 scripts/check_structure.py --check` → exit 0, **0 errors,
18 warnings** (pre-existing gen_stats domain-alias notes). Derived truth: 69
fully annotated papers, 19/30 cells ≥10, min cell 2.

## Task status
- A1 structure lint tool — **done 2026-08-24 (e6d03df)**
- A2 cross-ref/link debt paydown — **done 2026-08-24 (6f10501+b673c24)**
- A3 per-paper annotation files — **done 2026-08-24** (68 files verbatim-migrated).
  Carried: Blahut+Arimoto shared file; author-year fallback tightening.
  **Rediscovered debt (Pass 10): 51 full annotations still live as prose blocks
  in by-domain/by-structure files** (em-dash headers evade the lint) — needs a
  promotion pass + lint extension; B2 promotes-on-encounter meanwhile.
- A4 stats from data — **done 2026-08-24 (a49e738+db97bca)**. Thin cells:
  Dynamics×Matching, QEC×JointMarg → B2 targets.
- A5 loose-file adjudication — **done 2026-08-24 (61fee02)**. Layout contract;
  ledgers documented not folded; promotion-not-deletion rule lint-enforced.
- A6 SEPARATRIX review — **done 2026-08-24**. ACCEPT DIRECTIONALLY, gates
  G1–G3; merge is Aaron's. research/2026-08-24-2353.md.
- **Phase A COMPLETE. Phase B UNLOCKED.**
- B1 ingestion contract — **done 2026-08-24 (6ebfcf2)**. papers/INGESTION.md
  (queue format, ≤3/pass, triage-reject w/ one sentence); check_queue_hygiene()
  in lint, negative-tested.
- B2 consume queue batches — **in_progress**: slice-1 done (faf7f4f) — batch-001
  candidate-21 promoted to `annotations/2002.00208.md` (421 words conserved),
  dual-indexed, matrix regen (69 papers). **20 queued in batch-001.**
- B3 atlas synthesis touch-ups — open (after ~15 new papers).

## Reports (newest first)
- [2026-08-24-2358](2026-08-24-2358.md) — Pass 10 / B1 DONE + B2 slice-1: INGESTION.md + queue-hygiene lint; candidate-21 = promotion of existing prose annotation (2002.00208); 51-block prose-annotation debt quantified.
- [2026-08-24-2353](2026-08-24-2353.md) — Pass 9 / A6 DONE: SEPARATRIX PR #1 review; accept-directionally with three gates; gen_stats 7-column follow-up flagged.
- [2026-08-24-2345](2026-08-24-2345.md) — Pass 8 / A5 DONE: papers/README.md layout contract + lint enforcement; new debt class found (index→annotation gap).
- [2026-08-24-0840](2026-08-24-0840.md) — Pass 7 / A4 DONE: gen_stats.py + regenerated coverage-matrix.md, --check drift gate proven live.
- [2026-08-24-0737](2026-08-24-0737.md) — Pass 6 / A3 slice 4 DONE: Waves 4c–10c migrated, inbox reshaped, lint enforces empty inboxes.
- [2026-08-24-0730](2026-08-24-0730.md) — Pass 5 / A3 slice 3: archive Phase 2 migrated (9 files).
- [2026-08-24-0723](2026-08-24-0723.md) — Pass 4 / A3 slice 2: Wave 4b + Wave 3 triage (7 files).
- [2026-08-24-0713](2026-08-24-0713.md) — Pass 3 / A3 slice 1: Waves 1–2 migrated.
- [2026-08-24-0701](2026-08-24-0701.md) — Pass 2 / A2: crossref debt cleared.
- [2026-08-24-0650](2026-08-24-0650.md) — Pass 1 / A1: lint tool committed + baseline census.
