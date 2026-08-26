# Phase B ingestion contract (papers/INGESTION.md)

This is the agreement between the ORCHESTRATOR (who sweeps sources and drops
candidate batches) and the PASS (which consumes them). It is enforced
mechanically where possible by `scripts/check_structure.py` ("the lint").
Annotation semantics remain governed by `METHODOLOGY.md` and
`.claude/skills/annotate/SKILL.md` — this file is about pipeline, not method.

## 1. Queue format

- The orchestrator drops batches as `papers/queue/batch-NNN.md`, zero-padded,
  numbered in order of creation. Batches are consumed oldest-first.
- Each batch holds one candidate per section:

  ```
  ## candidate-NN [<target-cell-tag>] — <STATUS>
  ```

  followed by: **Title**, **URL** (arXiv id/URL preferred; a `file://` pdf
  path from the link-forge export is acceptable provenance), **Description**
  (abstract), and **Content extract** (` ``` `-fenced, ≤10k chars).
  `[<target-cell-tag>]` is the weak cell or bridge class that motivated the
  pick (e.g. `[neuroscience]`, `[dynamics-matching]`) — advisory only.
- `<STATUS>` is one of:
  - `UNCONSUMED` — awaiting triage.
  - `ANNOTATED` — promoted to the corpus; the header line gains the
    annotation id it became, e.g. `— ANNOTATED as 2401.12345`.
  - `REJECTED` — triaged out. The next non-empty line under the header must
    be a one-sentence rejection reason (see §4).
- A consumed batch is never hand-edited beyond status changes on its own
  candidate lines plus rejection sentences — history stays in the file.

## 2. Per-pass batch-size rule

A pass consumes **at most 3 papers** from the queue. Annotation depth beats
throughput: three full-depth annotations with clean dual indexing are worth
more than ten shallow ones. A pass may also consume fewer (including zero) —
e.g. when all remaining candidates in the oldest batch are rejected at triage.

## 3. Per-paper pipeline

For each accepted paper, in this order:

1. **Annotate** to full METHODOLOGY depth using `.claude/skills/annotate/`.
2. **Per-paper file:** write `papers/annotations/<arxiv-id>.md` (or
   `<doi-slug>.md` for non-arXiv), exactly one
   `## <id> --- <authors>` header per the layout contract in `papers/README.md`.
3. **Dual index:** add entries in ≥1 `papers/by-domain/<domain>.md` AND ≥1
   `papers/by-structure/<machine>.md`. Both sides are lint-enforced.
4. **Queue bookkeeping:** flip the candidate's status to
   `ANNOTATED as <id>` in the batch file.
5. **Glossary/atlas touch:** only if the paper introduces or materially
   sharpens a term or machine claim. Keep touches minimal; atlas synthesis
   is task B3's job, not every B2 pass's.
6. **Matrix regen:** run `python3 scripts/gen_stats.py` so
   `diagrams/coverage-matrix.md` and the headline counts follow the corpus.
7. **Lint green:** `python3 scripts/check_structure.py --check` must exit 0
   before commit.

## 4. Triage-reject rule

At consumption time a candidate may be REJECTED if either:

- it instantiates **fewer than 2 machines** (the atlas indexes shared
  algebraic structure across abstract machines — single-machine papers don't
  earn an annotation slot), or
- it **duplicates existing coverage**: another annotation already carries the
  same structural content (same machine pairing, same mechanism) with no
  material sharpening.

Rejection is recorded, never silent: set the header status to `REJECTED`,
then write exactly one sentence under the header naming the reason (which
rule fired, and what covers/duplicates it). Rejections live in the batch file
forever — the orchestrator uses them to retune future sweeps.

## 5. Lint enforcement (queue hygiene)

`check_structure.py` checks, for every `papers/queue/batch-*.md`:

- every `## candidate-*` header carries a valid STATUS token
  (`UNCONSUMED` / `ANNOTATED as <id>` / `REJECTED`);
- candidate ids are unique within a batch;
- every `REJECTED` candidate has a non-empty rejection sentence directly
  under its header.

Violations are errors — a queue edit that breaks hygiene blocks commits just
like any other lint failure.
