# research/INDEX.md — pass reports + task status (newest first)

**Lint state:** check_structure.py exit 0; 1 warning = pre-existing baseline
(2 author-year-prose crossrefs); `--check` 0 errors, zero gen_stats notes.
Derived corpus: **104 fully annotated papers**, **36 cells (6 machines × 6
domains)**, min cell 2, 23 cells ≥10. Domain-alias table landed in gen_stats.py
(pass 27); ML→InfoTheo and OT→TDA mappings await Aaron's ratification.

## Reports
- `2026-08-25-0648.md` — Pass 28: B2 slice-28 — batch-004 rate-distortion
  CLOSED 4/4 (13 Yadav et al. log-likelihood distortion annotated as
  2601.16461); ldpc-bp opened: 14 Aref–Macris–Vuffray spatially-coupled LDGM +
  cavity phase diagram (1307.5210), 16 Jain et al bounded-memory BP < KS with
  OT-as-proof-technology (1905.10031). ≤3/pass cap binds → 15+17 remain.
  Counts to derived 104.
- `2026-08-25-0636.md` — Pass 27: gen_stats grid+alias follow-up (StatPhys 6th
  column, alias table, 28 warnings→0) + B2 slice-27: batch-004 rate-distortion
  10 NERD (2204.01612) + 11 Theis–Wagner RDPF (2104.13662) ANNOTATED, 12
  REJECTED; 5 more Wave-9/10 wrong-pointer crossrefs fixed; counts to derived
  101.
- `2026-08-25-0630.md` — Pass 26: B2 slice-25, **stoch-thermo group CLOSED
  4/4** — Ito geometric thermodynamics, Barato–Seifert information reservoirs,
  Sekizawa ECoG EP decomposition; counts to derived 97.
- `2026-08-25-0623.md` — Pass 25: B2 slice-24 — dyn-matching group CLOSED 4/4
  + stoch-thermo opened (Nakazato–Ito new statistical_physics domain);
  counts to derived 95.
- `2026-08-25-0618.md` — Pass 24: B2 slice-23, batch-004 started — dyn-matching
  bridges 01+02 ANNOTATED (Takens↔OT both directions), 03 TrajectoryNet
  REJECTED; Dynamics×Matching 5→7; counts to 92.
- `2026-08-25-0608.md` — Pass 23: B2 slices 18–22, **batch-003 CLOSED 28/28**
  (4 new annotations incl. Battiston Physics Reports survey; Bandt promote;
  4 rejects); counts to derived 90.
- `2026-08-24-*` — Passes up to 22: Phase A complete (A1–A6), B1 done, B2
  slices 1–17 (batch-001 21/21 consumed; batch-002 18/40 with remaining 22
  HELD-by-orchestrator; batch-003 started).

## Task status (LOOP_MISSION.md ledger is canonical)
- **A1–A6:** all [done].
- **B1 ingestion contract:** [done] (6ebfcf2).
- **B2 queue consumption:** [in_progress] — batch-001 21/21, batch-002 18/40
  (22 HELD-by-orchestrator), batch-003 28/28 CLOSED,
  **batch-004 15/17 consumed (pass 28)**: dyn-matching 4/4 DONE;
  stoch-thermo 4/4 DONE; **rate-distortion 4/4 CLOSED** (13 Yadav et al.
  annotated pass 28); ldpc-bp 14+16 ANNOTATED, **15 + 17 unconsumed**
  (≤3 papers/pass cap). After slice-29 closes the batch: sanctioned
  Full-annotation-target lint check (wrong-pointer class).
- **B3 atlas synthesis:** [open] — trigger ~15 new papers since Wave-10 baseline; currently +31 new annotations. Candidate first target: thermodynamic-instantiation subsections on optimal_transport.md / composite_systems.md (the Ito-lineage cluster); second hook: OT-as-proof-technology inbound to statphys (1905.10031).
