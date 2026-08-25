# topo-rosetta RW research loop — mission + task ledger

**Aaron's directive (2026-08-24):** "loop 0x alpha over topoyolo just to clean
up and push a bit on the structure as well as use the link forge ingestion
paper methodologies to add to topoyolo. likely need a good structure first
built out." — Phase A is the structure build-out + cleanup; Phase B is
link-forge-style paper ingestion, and it stays locked until A is clean.

**What this repo is:** a cartography of shared algebraic structure — 6 abstract
machines × 5 domains, ~219 annotated papers, dual-indexed (by-domain +
by-structure). It is a DOCS/ATLAS repo: no code, no tests, no build. The
GitHub Pages site deploys from **master `/docs`** — which this loop never
touches (work stays on the loop branch; Aaron merges).

**Posture:** commits on branch `loop/atlas-structure-v1` only, never push,
never switch branches, no network fetches, no docker/gh/claude. Paper content
for Phase B arrives via files the orchestrator drops in `papers/queue/` — you
never query link-forge or arXiv yourself.

**Verification gate (this repo's "test suite"):** `python3
scripts/check_structure.py` — built by task A1, run before every commit once
it exists. It must exit 0, or every violation it reports must be catalogued in
the pass report as pre-existing baseline debt.

**Ground truth observed 2026-08-24:**
- master @ 508a4c7 clean; site live; README/docs claim 219 papers, 30 cells ≥4.
- `papers/inbox.md` is a 1,505-line monolith holding full annotations
  (Waves 4+); Waves 1–3 in `papers/inbox-archive.md`. Cross-refs from
  by-domain/by-structure point loosely at "inbox" — check-both-files is
  policy, which means link integrity is currently unverifiable by machine.
- Loose files: `papers/second_pass.md`, `papers/third_pass_*.md` (3),
  `papers/cross_domain_bridges.md` — relationship to the dual index undocumented.
- Open PR #1 "Propose SEPARATRIX as seventh machine" (branch
  `atlas/separatrix`) — unadjudicated.
- METHODOLOGY.md + `.claude/skills/annotate/SKILL.md` define the annotation
  contract. They are the law for Phase B; A-tasks must not change their
  semantics, only their mechanics.

## Phase A — structure: make the atlas machine-checkable and ingestion-ready

- **A1 [done 2026-08-24 e6d03df] Structure lint tool.** Baseline: 0 errors, 2 warnings
  (9 prose-only crossrefs; claimed 219 vs 53 parseable headers — most Wave 1-3
  annotations live as prose inside by-domain files, resolves at A3/A4).
  Report: `research/2026-08-24-0650.md`.
  Original: Write `scripts/check_structure.py`
  (stdlib only, no deps). Checks: (1) every full annotation (header pattern
  `## <id> --- <authors>` in inbox.md + inbox-archive.md) is referenced in ≥1
  `by-domain/` file AND ≥1 `by-structure/` file; (2) every relative markdown
  link in the repo resolves to an existing file; (3) the paper counts claimed
  in README.md, docs/index.html, and diagrams/coverage-matrix.md agree with
  each other (parse and compare; exact-count agreement with the corpus can be
  a warning, not an error, for now); (4) no annotation header appears twice.
  Output: human-readable violation list, exit 0/1. Done = tool committed +
  full baseline violation census in the pass report (do NOT fix violations in
  this task).
- **A2 [done 2026-08-24 6f10501+b673c24] Cross-ref + link debt paydown.** 9 prose-only
  crossrefs tightened to carry ids (one was a spurious match — Wang 2026 had no
  genuine by-structure entry; added one under phase_transitions.md); 6 archive
  `###` headers promoted to `##`, Rosas (2020) header given its arXiv id.
  Lint: 0 errors, 1 warning (219-vs-60 count — deferred to A3/A4).
  Report: `research/2026-08-24-0701.md`.
  Original: Fix what A1 found: broken
  links, orphan annotations (in inbox but missing from one side of the dual
  index), stale counts. Mechanical fixes only — no annotation content changes.
  Done = `check_structure.py` exits 0.
- **A3 [done 2026-08-24: slices 1-4 (1c96d87, 5771173, 4b6db24, aa06188+9d5be1d+dec8b5f)] Per-paper annotation files.** All full annotations now live one-per-file in `papers/annotations/` (68 files verbatim-migrated from inbox.md + inbox-archive.md; content conservation proven per slice). `papers/inbox.md` reshaped to contract + leads + wave index; inbox-archive.md pointer-lists only; ~170 crossrefs in by-domain/by-structure/atlas/glossary repointed to per-paper files; METHODOLOGY/SKILL/README canonical refs updated; check_structure.py extended to fail if any full annotation remains in an inbox file. Lint: 0 errors, 1 warning (claimed 219 vs 68 parsed — count-source drift, resolves at A4).
  - carried to later A-tasks (orchestrator): Blahut+Arimoto kept as ONE shared file blahut-arimoto-1972.md (splitting would require rewriting shared prose — deferred); tighten lint author-year fallback (Wang/Tran spurious-match classes from A2).
- **A4 [done 2026-08-24 a49e738+db97bca] Stats from data, not by hand.** `scripts/gen_stats.py`
  derives paper/cell counts from papers/annotations/*.md and regenerates
  diagrams/coverage-matrix.md; README + docs/index.html patched to derived truth
  (68 fully annotated papers — NOT the old 219 claim; min cell 1, 18/30 cells ≥10);
  `check_structure.py --check` fails lint on matrix-regen or headline-count drift.
  Lint: 0 errors, 0 warnings (--check: 0 errors, 18 informational domain-alias notes).
  Report: `research/2026-08-24-0840.md`.
  Original: `scripts/gen_stats.py`: derive
  paper count, per-cell coverage counts, and the domain×machine matrix from
  the annotation files; emit `diagrams/coverage-matrix.md` and print the
  headline numbers (papers, cells, min cell). Patch README.md +
  docs/index.html stats to the derived truth (docs/ edits are fine on the
  branch — they only deploy when Aaron merges). Wire a `--check` mode into
  check_structure.py so drift fails the lint. Done = regenerated matrix
  committed, stats consistent, lint enforces it.
- **A5 [done 2026-08-24 61fee02] Loose-file adjudication.** `papers/README.md`
  layout contract: all five loose files adjudicated as historical search-pass
  ledgers (67 SP/TP candidate entries, non-canonical, promotion-not-deletion
  rule); check_structure.py now fails on any undocumented papers/ entry.
  Lint: 0 errors, 18 pre-existing gen_stats alias notes.
  Report: `research/2026-08-24-2345.md`.
  Original: `second_pass.md`,
  `third_pass_*.md`, `cross_domain_bridges.md`: for each, determine what it
  is (read it), then either (a) fold its content into the canonical structure
  (per-paper files / atlas / glossary) or (b) document its role in a
  `papers/README.md` layout guide. No deletions — content moves or gets
  documented, never dropped. Done = papers/ has a written layout contract and
  no undocumented files.
  - carried to Phase B: promote ledger candidates via normal ingestion; two
    index prose crossrefs lack annotation files (Mollers 2023 Hodge-aware CL;
    Mézard–Mora).
- **A6 [done 2026-08-24 — recommendation recorded, merge is Aaron's] SEPARATRIX
  proposal review.** Worked from orchestrator's export `papers/queue/separatrix-pr1.md`
  (no local origin branch needed). Verdict: ACCEPT DIRECTIONALLY — genuine seventh
  machine (distinct primary object; independent ML/philosophy rediscovery of boundary
  thickness; built-in falsification via EXP-88/F-10), with three gates before promotion:
  G1 sharpen signature + demote margin to degenerate case; G2 add ANTISYNONYMS entry vs
  Stability/Parameterized Homology; G3 no matrix/glossary/index integration until ≥3
  cited papers survive B2 annotation. If merged, gen_stats.py needs a follow-up task for
  the 7th column (+ possible ML domain). Answers to PR's Q1–Q3 in report.
  Report: `research/2026-08-24-2353.md`.

## Phase B — ingestion: link-forge methodology (locked until A1–A5 done)

The link-forge flow, adapted: the ORCHESTRATOR sweeps sources
(search-papers.ts → link-forge Neo4j → export) and drops candidate batches
into `papers/queue/batch-NNN.md` (per paper: title, authors, year, arXiv
id/URL, abstract, ≤10k-char content extract, source provenance). The PASS
consumes the queue: full-depth annotation per METHODOLOGY.md + the annotate
skill, dual-index filing, glossary/atlas updates, matrix regen via A4's tool.

- **B1 [open] Ingestion contract.** Write `papers/INGESTION.md`: the queue
  file format (so the orchestrator and pass agree), the per-paper pipeline
  (queue → annotate → per-paper file → dual index → glossary/atlas touch →
  gen_stats), batch-size rule (≤3 papers per pass — annotation depth beats
  throughput), and the triage rule (a queued paper may be REJECTED with one
  recorded sentence if it instantiates <2 machines or duplicates existing
  coverage; rejections logged in the queue file, never silently dropped).
  Done = contract committed + check_structure covers queue hygiene.
  - **done [2026-08-24 6ebfcf2]** papers/INGESTION.md committed (queue format,
    ≤3/pass, triage-reject rule); check_queue_hygiene() in check_structure.py,
    negative-tested. Report: `research/2026-08-24-2358.md`.
  - discovered subtask (A3 debt): **51 full annotations still live as prose
    blocks in by-domain/by-structure index files** (em-dash headers evade the
    lint). Promote to per-paper files; extend lint to fail on the class.
    B2 passes promote-on-encounter until then.
- **B2 [in_progress: slice-1 done faf7f4f — batch-001 candidate-21 promoted as
  2002.00208; 20 queued] Consume queue batches.** Repeatable task — each pass takes ≤3
  papers from the oldest unconsumed batch. Prioritize (from Wave-10 state):
  neuroscience cells (weakest), Matching×InfoTheory, and any paper bridging
  ≥3 domains. Every annotated paper: per-paper file + both indices + matrix
  regen + lint green. Status line here records papers consumed / queued.
- **B3 [open] Atlas synthesis touch-ups.** After ~15 new papers: re-read the
  6 atlas files against the new corpus; integrate the strongest new bridges
  and any new ANTISYNONYMS. One atlas file per pass max.

## Ledger protocol (every pass)

Pick the FIRST task not `[done]` (or continue an `[in_progress]` one). Phase B
is locked until A1–A5 are `[done]` (A6 may trail). When a pass advances a
task, edit its status line here: `[open]` → `[in_progress: <one-line state>]`
→ `[done <date> <commit>]`. Add discovered subtasks as indented bullets under
their parent. Never delete history — strike through with `~~` if a task dies,
and say why.
