# topo-rosetta RW loop — plan of record

Adapted 2026-08-24 from the wavecast rw-loop machinery (Aaron: "loop 0x alpha
over topoyolo … clean up and push a bit on the structure … use the link forge
ingestion paper methodologies to add to topoyolo").

## Architecture

Two processes, strict separation:

1. **Pass** — headless `claude -p "/topoyolo-pass"` on OpenRouter
   `stealth/ox-alpha` via the retrying proxy on :8399. Does the actual repo
   work on branch `loop/atlas-structure-v1`. Guarded by
   `.claude/hooks/rw-loop-guard.sh` (bound via `--settings` ONLY — never
   project settings.json). May not: push, switch branches, network-fetch,
   touch secrets/systemd/docker/gh/claude, or edit the guard machinery.
2. **Orchestrator** — Fable session running `/topoyolo-orchestrate` on a
   ScheduleWakeup loop. Launches passes (Bash `run_in_background: true`,
   plain foreground command), verifies boundaries independently, runs the
   lint gate itself, pushes the branch + maintains the draft PR, digests for
   Aaron. Orchestrator notes to a pass go via the launcher's `$1`
   prompt-arg channel (`run-topoyolo-pass.sh "note"`), never report tails.

## Files

- `.claude/LOOP_MISSION.md` — mission + task ledger (pass owns status lines)
- `.claude/commands/topoyolo-pass.md` — the pass prompt
- `.claude/hooks/rw-loop-guard.sh` + `.claude/rw-loop-settings.json` — guard
- `.claude/run-topoyolo-pass.sh` — launcher (branch check, proxy env, model)
- `.claude/oxproxy.py` — retrying OpenRouter proxy on :8399 (generic; same
  code as wavecast's — only one instance runs regardless of which repo's
  copy launched it)
- `research/` — one report per pass + INDEX.md (orient surface)
- `papers/queue/` — orchestrator-dropped candidate batches for Phase B
- `~/.claude/commands/topoyolo-orchestrate.md` — orchestrator prompt

## Key differences from wavecast

- **No pytest/ruff.** Verification gate = `python3 scripts/check_structure.py`
  (built by task A1; stdlib-only). Until A1 lands, the gate is: repo intact,
  content conservation on migrations, commits parse.
- **No production artifacts on disk.** The production surface is the GitHub
  Pages site, which deploys from master:/docs. Protection = the loop never
  touches master and never pushes; Aaron merges the PR.
- **No network for the pass at all** (wavecast allowed repo fetchers). Paper
  content for Phase B arrives via `papers/queue/batch-NNN.md` files that the
  ORCHESTRATOR exports from link-forge Neo4j (docker start link-forge-neo4j →
  export → docker stop — Aaron's box is resource-constrained; never bring up
  the rest of the docker fleet or the link-forge bot for this).

## Boundary verification (orchestrator, every tick)

- branch still `loop/atlas-structure-v1`; `git rev-parse master` unchanged;
  `git log origin/master..master` empty.
- guard machinery unchanged: `git diff` on `.claude/hooks/`,
  `rw-loop-settings.json`, `run-topoyolo-pass.sh`, `oxproxy.py` vs the
  orchestrator's recorded shas.
- lint run independently; annotation-count conservation spot-check after
  migration commits.
Any violation: stop the loop, tell Aaron loudly.
