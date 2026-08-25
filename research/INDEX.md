# research/INDEX.md — pass reports + task status (newest first)

**Lint state:** check_structure.py exit 0; 1 warning = pre-existing baseline
(2 author-year-prose crossrefs); `--check` 0 errors. Derived corpus: **161
fully annotated papers** (+1 pass 51), **36 cells (6 machines × 6 domains)**,
min cell 2, **32 cells ≥10**. Domain-alias table landed in gen_stats.py
(pass 27); ML→InfoTheo and OT→TDA mappings await Aaron's ratification.
Standing policy (pass 43): README/docs count patches land in the SAME commit
as the gen_stats regen.
Machine-vocabulary translation (pass 50, for consistent filing): by-structure
file names → six machines: boundary_operators→chain complex; filtrations→
parameterized homology; matching/optimal_transport→matching; phase_transitions→
stability; composite_systems→joint-vs-marginal excess; null hypothesis has no
structure file.

## Reports
- `2026-08-25-0856.md` — Pass 51: **batch-009 CLOSED 10/10** — candidate-10
  ANNOTATED as 1906.05212 (correlator diagnostics; RG-like patterns AND
  important differences) AS A PAIR with 1410.3831; B3 pairing flag discharged
  both sides; antisynonym "Exact RG↔DL mapping ≠ correlator-level identity"
  filed. B3 sub-slice 6: antisynonym "Abrupt jump ≠ phase transition"
  (2505.10114). Counts to derived 161, deep cells 32.
- `2026-08-25-0851.md` — Pass 50: B2 batch-009 rg-dl 4/5 ANNOTATED (07:
  2405.17538 BRG-NNFT Fisher-metric coarse graining; 08: 2504.12700 two-phase
  fit→compress with MI progress measure + null reading of grokking/DD/IB;
  09: 2506.04016 inverse-RG minimal nets — lineage's first inverse-direction
  entry). Counts to derived 160, deep cells 32. Fixed stale README "31 cells"
  debt from passes 47/49.
- `2026-08-25-0843.md` — Pass 49: batch-009 pid-theory group CLOSED 5/5
  (04: 2404.01470 Milzman I_ft source-failure redundancy + QEC crossref;
  05: 1303.3440 localizability axiom) + rg-dl opened 1/5 (06: 1410.3831
  Mehta-Schwab exact RG↔RBM map; B3 flag: pair with skeptical null
  1906.05212). Counts to derived 157, deep cells 32.
- `2026-08-25-0837.md` — Pass 48: batch-009 pid-theory 3/5 ANNOTATED
  (1004.2515 Williams-Beer founding lattice — fresh per-paper file despite
  heavy prose references; 2306.00734 mereological base-concept unification;
  1910.05979 cooperative-game second-lattice decomposition). Counts to
  derived 154, deep cells 31.
- `2026-08-25-0831.md` — Pass 47: **batch-008 CLOSED 11/11** (kuramoto 10–11)
  + B3 sub-slice 5 (MATCHING.md "Same theorem, two machines": Takens via
  conjugacy vs via pushforward). Counts to derived 151, deep cells 31.
- `2026-08-25-0827.md` — Pass 46: batch-008 kuramoto 3/5 ANNOTATED
  (2407.02416 Buendía mesoscopic; 2505.10114 extreme sync transitions;
  cond-mat/0606048 eight-regime taxonomy). Counts to derived 149.
- `2026-08-25-0750.md` / `2026-08-25-0740.md` — Passes 44–45: batch-008
  reservoir-gs group CLOSED 6/6 (GS=matching arc).
- `2026-08-25-0735.md` — Pass 37→43 window: **batch-007 CLOSED 12/12**
  (qec-mwpm + null-surrogate groups), sanctioned same-commit count protocol.
- Earlier (`2026-08-25-07*`, `2026-08-24-*`): batch-002/003/005/006 CLOSED,
  channel-capacity + ph-stability groups, Phase A complete (A1–A6), B1 done,
  gen_stats follow-up.

## Task status (LOOP_MISSION.md ledger is canonical)
- **A1–A6:** all [done].
- **B1 ingestion contract:** [done] (6ebfcf2).
- **B2 queue consumption:** [in_progress] — **batch-009 CLOSED 10/10**
  (pass 51: candidate-10 → annotations/1906.05212.md, paired with 1410.3831,
  pairing flag discharged). IDLE until batch-010 lands in papers/queue/
  (orchestrator foraging). Residual Wave-era catch-all pointer debt
  (~100, ≤5/pass sanctioned).
- **B3 atlas synthesis:** [in_progress] — sub-slices 1–6 done (6 = pass 51:
  two ANTISYNONYMS entries — RG↔DL claim-vs-refutation pair note discharging
  the pairing flag; abrupt-jump ≠ phase transition from 2505.10114). Open
  hooks: possible ANTISYNONYMS note from 1910.05979 (positivity+identity is a
  lattice property); dynamical_systems.md atlas re-read post-batch-008.
