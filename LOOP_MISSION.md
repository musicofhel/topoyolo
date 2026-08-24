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
- **A3 [in_progress: slices 1-3 done 2026-08-24 (1c96d87, 5771173, 4b6db24) — entire inbox-archive.md now pointer-lists only (31 papers in papers/annotations/, incl. all Phase 2 + Core ATT full annotations); lint green; remaining: inbox.md Waves 4+] Per-paper annotation files.** The monolithic inbox does not
  scale for ingestion. Migrate: one file per paper at
  `papers/annotations/<slug>.md` (slug = arXiv id with `/`→`-`, else
  first-author-year), each holding the full annotation verbatim (content
  unchanged — this is a MOVE, not a rewrite). `papers/inbox.md` shrinks to:
  the ingestion queue contract + "Still to find" leads + an index of
  annotation files by wave. Update every by-domain/by-structure/atlas
  cross-ref to point at the per-paper file. Extend `check_structure.py` to
  enforce the new layout. This is the largest A task — split across passes
  freely (e.g. one wave per pass), committing incrementally; the lint must be
  green at every commit. Done = zero full annotations left in
  inbox.md/inbox-archive.md, lint green.
  - queued (orchestrator, later A-task): split Blahut+Arimoto's shared
    annotation block into two per-paper files; tighten the lint's
    author-year fallback (Wang/Tran spurious-match classes found in A2).
- **A4 [open] Stats from data, not by hand.** `scripts/gen_stats.py`: derive
  paper count, per-cell coverage counts, and the domain×machine matrix from
  the annotation files; emit `diagrams/coverage-matrix.md` and print the
  headline numbers (papers, cells, min cell). Patch README.md +
  docs/index.html stats to the derived truth (docs/ edits are fine on the
  branch — they only deploy when Aaron merges). Wire a `--check` mode into
  check_structure.py so drift fails the lint. Done = regenerated matrix
  committed, stats consistent, lint enforces it.
- **A5 [open] Loose-file adjudication.** `second_pass.md`,
  `third_pass_*.md`, `cross_domain_bridges.md`: for each, determine what it
  is (read it), then either (a) fold its content into the canonical structure
  (per-paper files / atlas / glossary) or (b) document its role in a
  `papers/README.md` layout guide. No deletions — content moves or gets
  documented, never dropped. Done = papers/ has a written layout contract and
  no undocumented files.
- **A6 [open] SEPARATRIX proposal review (read-only).** Fetch is denied, so
  work from `git log`/`git show` if `origin/atlas/separatrix` is available
  locally; if not, record the blocker and let the orchestrator attach the
  diff to `papers/queue/separatrix-diff.txt`. Assess against METHODOLOGY.md:
  is SEPARATRIX a genuine seventh machine or a special case of the six?
  Recommendation + evidence in the report. MERGE DECISION IS AARON'S — this
  task produces a recommendation only.

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
- **B2 [open] Consume queue batches.** Repeatable task — each pass takes ≤3
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
