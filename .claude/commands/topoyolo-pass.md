---
description: One read-write structure/ingestion pass over topo-rosetta — pick the next mission task, implement + verify + commit, report to research/.
---

# Read-write research pass — topo-rosetta (~/topoyolo)

You are one pass of a recurring loop doing REAL structure and curation work on
this atlas repo, one small task at a time. You run headless (no human to ask —
finish the pass and write the report). A PreToolUse guard enforces the hard
boundaries: no pushing/branch-switching, no network (curl/wget/npx/docker all
denied — paper content arrives via `papers/queue/` files), no secrets, and the
loop's own guard machinery is read-only. If a command is refused, that is the
guard working; route around it, don't fight it.

This is a DOCS/ATLAS repo — no pytest, no build. The verification gate is
`python3 scripts/check_structure.py` (built by task A1). METHODOLOGY.md and
`.claude/skills/annotate/SKILL.md` are the annotation law; structure tasks
change mechanics, never annotation semantics.

**Hard rules:**
- ONE ledger task per pass (A3/B2 may do one sub-slice), done properly:
  implement → verify → commit. A finished small diff beats a sprawling dead
  session.
- Never `git push`, never switch branches — you work on
  `loop/atlas-structure-v1` and Aaron reviews. Commit messages:
  `loop: <task-id> <what changed>`.
- **Content conservation:** structure tasks MOVE text, they never rewrite,
  summarize, or delete annotation content. After any migration commit, prove
  conservation in the report (e.g. compare `grep -c '^## .* ---'` totals
  before/after, or wc -w on moved blocks).
- The lint is the currency: run `python3 scripts/check_structure.py` before
  every commit once it exists. New violations you introduced = fix before
  committing. Pre-existing baseline debt = catalogue in the report.
- Do not spawn subagents or use Agent/Task tools; everything happens in this
  session.
- No dependency installs; scripts/ stays Python stdlib only.

**Session budget (ox-alpha reliability — measured on prior loops).** This
model intermittently emits an empty turn; two in a row kill the session, and
deaths cluster past ~120k accumulated context. Protect the pass:
- **Commit early, commit incrementally.** The moment a coherent sub-step is
  done and lint-green, commit it. A dead session must leave its progress in
  git, not in context. WIP commits on the loop branch are fine.
- **Write the report skeleton FIRST** (right after picking the task), then
  edit findings in as they land.
- **Windowed reads only.** Grep with `head_limit`; Read with offset/limit
  (≤250 lines); `papers/inbox.md` is 1,500+ lines — NEVER whole-read it; work
  wave-by-wave via grep for `^## ` headers and offset reads.
- **By ~60 tool calls, wrap up**: commit what is green, set the ledger status
  honestly (`in_progress` with a one-line state is a fine outcome), finish
  the report.

## Step 1 — orient (cheap)

1. Read `.claude/LOOP_MISSION.md` — the mission, ground truth, and task ledger.
2. `git log --oneline -8` and `git status` — what prior passes landed; confirm
   you are on `loop/atlas-structure-v1`.
3. Read `research/INDEX.md` if it exists (INDEX only — open a prior pass
   report only when you need a specific finding's evidence).

## Step 2 — pick ONE task

First task not `[done]` in the ledger, or continue an `[in_progress]` one from
its recorded state. Phase B is locked until A1–A5 are done. If the natural
next step of your task is blocked (needs Aaron, needs a queue file that isn't
there, needs network), do the unblocked part, then record the blocker in the
ledger + report and STOP — don't improvise around a hard rule.

## Step 3 — implement

Small diffs in the repo's own idiom (match the existing markdown voice and
annotation format exactly). Baseline first: if something is already broken
before your change, record that before fixing or working around it.

## Step 4 — verify + commit

`python3 scripts/check_structure.py` (once it exists) before the final commit
of the pass. For migrations, run the conservation check too. Commit everything
that is green. Never leave good work uncommitted.

## Step 5 — report + ledger

One report per pass: `research/YYYY-MM-DD-HHMM.md` (stamp from `date
+%Y-%m-%d-%H%M`, pass START time), written incrementally:

```markdown
# Pass N — <task-id> — <date>
**Task:** <ledger line>
**Since last pass:** <commits landed before this pass / ledger moves>

## What landed
<commits with hashes, one line each>

## Verification
<lint output summary + conservation proof, with the exact commands>

## Findings / surprises
<anything learned that changes the mission — structure debt, corpus gaps>

## Blockers / for Aaron
<aaron-gated decisions, queue requests for the orchestrator>

## Next
<the single next step, concrete enough for a fresh session>
```

Then: update the task's status line in `.claude/LOOP_MISSION.md`, and rewrite
`research/INDEX.md` (full overwrite): per-task one-line status + latest lint
state + a `Reports:` list (newest first). INDEX is what Aaron and the
orchestrator read; keep it under ~40 lines.
