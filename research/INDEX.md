# topo-rosetta RW loop — INDEX

**Branch:** `loop/atlas-structure-v1` (never pushed; Aaron reviews/merges)
**Lint:** `python3 scripts/check_structure.py` → exit 0, 0 errors, 1 warning
(claimed 219 papers vs 65 parsed headers — resolves as A3 slices land / A4;
author-year crossref debt ZERO — all annotations id-matched incl. slug
fallback `baudot-2015`)

## Task status
- A1 structure lint tool — **done 2026-08-24 (e6d03df)**
- A2 cross-ref/link debt paydown — **done 2026-08-24 (6f10501+b673c24)**
- A3 per-paper annotation files — **in_progress**: slices 1–2 done (1c96d87,
  5771173): inbox-archive Waves 1–2 + Wave 4b + Wave 3 triage →
  `papers/annotations/` (22 verbatim files), crossrefs repointed, lint green.
  Remaining: Phase 2 section of archive (~12 papers), then inbox.md Waves 4+.
  Queued subtasks: Blahut+Arimoto shared-block split; tighten lint author-year
  fallback (Wang/Tran spurious-match classes).
- A4 stats from data — open
- A5 loose-file adjudication — open
- A6 SEPARATRIX review (read-only) — open
- Phase B (B1–B3) locked until A1–A5 done.

## Reports (newest first)
- [2026-08-24-0723](2026-08-24-0723.md) — Pass 4 / A3 slice 2: Wave 4b + Wave 3 triage migrated (7 files, 117 body lines conserved exactly), 16 crossrefs repointed, ### Baudot header promoted with slug id.
- [2026-08-24-0713](2026-08-24-0713.md) — Pass 3 / A3 slice 1: Waves 1–2 migrated to per-paper files (5532 words conserved), 28 stale inbox pointers fixed, lint extended; author-year debt cleared.
- [2026-08-24-0701](2026-08-24-0701.md) — Pass 2 / A2: crossref debt cleared, 60 headers now parse; spurious soft-match finding; Blahut+Arimoto split decision flagged for A3.
- [2026-08-24-0650](2026-08-24-0650.md) — Pass 1 / A1: lint tool committed + baseline census (53 headers vs claimed 219; 6 loose crossrefs; nonconforming header grammar).
