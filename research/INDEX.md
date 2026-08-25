# research/INDEX.md — pass reports + task status (newest first)

**Lint state:** check_structure.py exit 0; --check exit 0 (35 informational
gen_stats domain-alias notes, pre-existing class). Derived corpus: **90 fully
annotated papers**, 30 cells, min cell 2, 21 cells ≥10.

## Reports
- `2026-08-25-0608.md` — Pass 23: B2 slices 18–22, **batch-003 CLOSED 28/28**
  (4 new annotations incl. Battiston Physics Reports survey; Bandt promote;
  4 rejects); counts to derived 90.
- `2026-08-25-0556.md` — Pass 22: B2 slices 15–17, batch-003 info-machines group closed 6/6 (5 promote-on-encounter dedups + CCMI new).
- `2026-08-24-*` — Passes up to 21: Phase A complete (A1–A6), B1 done, B2 slices 1–14 (batch-001 21/21 consumed; batch-002 18/40 with remaining 22 HELD-by-orchestrator).

## Task status (LOOP_MISSION.md ledger is canonical)
- **A1–A6:** all [done].
- **B1 ingestion contract:** [done] (6ebfcf2).
- **B2 queue consumption:** [in_progress] — batch-001 21/21, batch-002 18/40
  (22 HELD-by-orchestrator), **batch-003 28/28 FULLY CONSUMED (pass 23)**.
  No unconsumed candidates remain. Next pass needs a fresh queue batch from
  the orchestrator, or sanction to re-triage the held candidates.
- **gen_stats alias-table cleanup:** sanctioned next task pick — map ~20
  recurring free-text domain strings onto the 5 canonical domains in
  scripts/gen_stats.py; drive the 35 informational notes to 0.
- **B3 atlas synthesis:** [open], locked until ~15 new papers since B2 start.
