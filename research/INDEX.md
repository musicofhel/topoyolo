# research/INDEX.md — pass reports + task status (newest first)

**Lint state:** check_structure.py exit 0; 1 warning = pre-existing baseline
(2 author-year-prose crossrefs). Derived corpus: **95 fully annotated papers**,
30 cells, min cell 2, 21 cells ≥10. **New domain this pass:
`by-domain/statistical_physics.md`** (stoch-thermo group) — gen_stats cell grid
still says "6 machines × 5 domains"; follow-up noted in pass 25 report.

## Reports
- `2026-08-25-0623.md` — Pass 25: B2 slice-24, **dyn-matching group CLOSED
  4/4 + stoch-thermo opened** — 04 MIOFlow annotated (2206.14928), 05
  Nakazato–Ito annotated (2103.00503, new statistical_physics domain), 07
  Ito–Oizumi–Amari annotated (1810.09545, joint-vs-marginal-in-dissipation);
  counts to derived 95.
- `2026-08-25-0618.md` — Pass 24: B2 slice-23, batch-004 started — dyn-matching
  bridges 01+02 ANNOTATED (Takens↔OT both directions), 03 TrajectoryNet
  REJECTED; Dynamics×Matching 5→7; counts to 92.
- `2026-08-25-0608.md` — Pass 23: B2 slices 18–22, **batch-003 CLOSED 28/28**
  (4 new annotations incl. Battiston Physics Reports survey; Bandt promote;
  4 rejects); counts to derived 90.
- `2026-08-25-0556.md` — Pass 22: B2 slices 15–17, batch-003 info-machines group closed 6/6 (5 promote-on-encounter dedups + CCMI new).
- `2026-08-24-*` — Passes up to 21: Phase A complete (A1–A6), B1 done, B2 slices 1–14 (batch-001 21/21 consumed; batch-002 18/40 with remaining 22 HELD-by-orchestrator).

## Task status (LOOP_MISSION.md ledger is canonical)
- **A1–A6:** all [done].
- **B1 ingestion contract:** [done] (6ebfcf2).
- **B2 queue consumption:** [in_progress] — batch-001 21/21, batch-002 18/40
  (22 HELD-by-orchestrator), batch-003 28/28 CLOSED,
  **batch-004 6/17 consumed (pass 25)**: dyn-matching 4/4 DONE; stoch-thermo
  1/5 done (05 annotated; 06/08/09 pending); rate-distortion (10–13) and
  ldpc-bp (14–17) untouched.
- **B3 atlas synthesis:** [open] — trigger ~15 new papers since Wave-10 baseline; currently +25 new annotations.
