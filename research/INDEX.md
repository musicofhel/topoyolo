# topo-rosetta RW loop — INDEX

**Branch:** `loop/atlas-structure-v1` (never pushed; Aaron reviews/merges)
**Lint:** `python3 scripts/check_structure.py` → exit 0, 0 errors, 1 warning
(claimed 219 papers vs 68 parsed headers — count-source drift; resolves at A4.
Author-year crossref debt: ZERO.)

## Task status
- A1 structure lint tool — **done 2026-08-24 (e6d03df)**
- A2 cross-ref/link debt paydown — **done 2026-08-24 (6f10501+b673c24)**
- A3 per-paper annotation files — **done 2026-08-24** (slices 1–4: 1c96d87,
  5771173, 4b6db24, aa06188+9d5be1d+dec8b5f). All full annotations now
  per-paper in `papers/annotations/` (68 files, verbatim-migrated, conservation
  proven). inbox.md = contract + leads + wave index; archive pointer-lists
  only; ~170 index/atlas/glossary crossrefs repointed; METHODOLOGY/SKILL/
  README canonical refs updated; lint extended to fail on any annotation left
  in an inbox file. Carried: Blahut+Arimoto stays ONE shared file (split would
  rewrite shared prose); author-year fallback tightening still queued.
- A4 stats from data — open (NEXT)
- A5 loose-file adjudication — open
- A6 SEPARATRIX review (read-only) — open
- Phase B (B1–B3) locked until A1–A5 done.

## Reports (newest first)
- [2026-08-24-0737](2026-08-24-0737.md) — Pass 6 / A3 slice 4 DONE: Waves 4c–10c migrated (36 verbatim files incl. blahut-arimoto-1972), 149 crossrefs repointed, inbox reshaped to contract+leads+wave index, lint enforces empty inboxes. A3 flipped done.
- [2026-08-24-0730](2026-08-24-0730.md) — Pass 5 / A3 slice 3: archive Phase 2 migrated (9 verbatim files, reconstruction diff clean), 4 Core ATT stubs repointed; count math reconciled (31 files + 34 inbox = 65).
- [2026-08-24-0723](2026-08-24-0723.md) — Pass 4 / A3 slice 2: Wave 4b + Wave 3 triage migrated (7 files, 117 body lines conserved exactly), 16 crossrefs repointed, ### Baudot header promoted with slug id.
- [2026-08-24-0713](2026-08-24-0713.md) — Pass 3 / A3 slice 1: Waves 1–2 migrated to per-paper files (5532 words conserved), 28 stale inbox pointers fixed, lint extended; author-year debt cleared.
- [2026-08-24-0701](2026-08-24-0701.md) — Pass 2 / A2: crossref debt cleared, 60 headers now parse; spurious soft-match finding; Blahut+Arimoto split decision flagged for A3.
- [2026-08-24-0650](2026-08-24-0650.md) — Pass 1 / A1: lint tool committed + baseline census (53 headers vs claimed 219; 6 loose crossrefs; nonconforming header grammar).
