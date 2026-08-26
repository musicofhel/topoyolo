#!/usr/bin/env bash
# PreToolUse guard for the topo-rosetta READ-WRITE research loop (ox-alpha passes).
#
# Posture: the looping session may read, edit, and commit INSIDE ~/topoyolo
# (branch work only) — and nothing else. It must never: reach secrets (.env,
# rc files, ssh), push or switch branches, fetch from the network (paper
# content arrives via papers/queue/ files the orchestrator drops), touch
# cron/systemd/docker, or rewrite its own guard machinery
# (.claude/hooks/, .claude/rw-loop-settings.json, .claude/oxproxy.py,
# .claude/run-topoyolo-pass.sh).
#
# The GitHub Pages site deploys from master:/docs — the loop only ever
# commits to its own branch, so docs/ edits are safe until Aaron merges.
#
# Deny-list guard (same family as wavecast's): the pass runs real commands
# (python3, git), so enforcement focuses on the catastrophic actions.
#
# Contract: read hook JSON on stdin, emit a permissionDecision, exit 0.

set -uo pipefail

INPUT="$(cat)"
REPO="$HOME/topoyolo"

decide() { # $1=allow|deny  $2=reason
  jq -n --arg d "$1" --arg r "$2" \
    '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:$d,permissionDecisionReason:$r}}'
  exit 0
}
allow() { decide allow "$1"; }
deny()  { decide deny  "topoyolo rw-loop: $1"; }

TOOL="$(jq -r '.tool_name // ""' <<<"$INPUT")"

# Secret-bearing paths. The pass runs on a third-party stealth model.
SECRET_RE='\.env([^a-zA-Z0-9_.]|$)|\.credentials|\.zshrc|\.bashrc|\.ssh/|\.claude/projects'
check_secrets() {
  if [[ "$1" =~ $SECRET_RE ]]; then
    deny "that touches a secret-bearing path (.env / rc files / .ssh / memory)."
  fi
}

# The loop's own enforcement machinery is read-only to the pass.
GUARD_RE='\.claude/hooks/|rw-loop-settings\.json|oxproxy\.py|run-topoyolo-pass\.sh'

# ---------------------------------------------------------------- file writes
case "$TOOL" in
  Write|Edit|MultiEdit|NotebookEdit)
    FP="$(jq -r '.tool_input.file_path // .tool_input.notebook_path // ""' <<<"$INPUT")"
    check_secrets "$FP"
    if [[ "$FP" =~ $GUARD_RE ]]; then
      deny "the guard/launcher/proxy files are the loop's enforcement machinery — read-only to the pass. Propose changes in the report."
    fi
    case "$FP" in
      "$REPO"/.git/*) deny "no direct .git internals writes — use git commands." ;;
      "$REPO"/*|/tmp/*) allow "write inside the sanctioned trees" ;;
      *) deny "writes are confined to ~/topoyolo and /tmp. Blocked: $FP" ;;
    esac
    ;;
  Bash) : ;;   # falls through to the command analysis below
  Read|Grep|Glob)
    TARGET="$(jq -r '(.tool_input.file_path // "") + " " + (.tool_input.path // "")' <<<"$INPUT")"
    check_secrets "$TARGET"
    exit 0 ;;
  *) exit 0 ;;
esac

# -------------------------------------------------------------------- bash
CMD="$(jq -r '.tool_input.command // ""' <<<"$INPUT")"
[ -n "$CMD" ] || exit 0

check_secrets "$CMD"

# A write-capable verb aimed at the guard machinery is refused.
if [[ "$CMD" =~ $GUARD_RE ]]; then
  case "$CMD" in
    *rm\ *|*mv\ *|*cp\ *|*tee\ *|*truncate*|*chmod*|*sed\ -i*|*'>'*)
      deny "that command names the loop's enforcement machinery alongside a write-capable verb. Those files are read-only to the pass." ;;
  esac
fi

check_git() {
  local sub="$1"; shift
  local args="$*"
  case "$sub" in
    status|log|diff|show|blame|shortlog|describe|grep|ls-files|ls-tree|\
rev-parse|rev-list|cat-file|for-each-ref|count-objects|whatchanged|reflog|check-ignore|\
add|commit|restore|rm|mv|apply)
      return 0 ;;
    branch)
      case " $args " in
        *" -d "*|*" -D "*|*" -m "*|*" -M "*|*--delete*|*--move*|*--set-upstream*)
          deny "git branch with a mutating flag — the loop stays on its own branch." ;;
      esac
      return 0 ;;
    stash)
      deny "git stash can strand or destroy work in a headless session. Commit instead — WIP commits on the loop branch are fine." ;;
    tag)
      case " $args " in *" -l"*|*"--list"*|" ") return 0 ;; esac
      deny "tag creation is Aaron's." ;;
    config)
      case " $args " in *" --get"*|*" --list"*|*" -l "*) return 0 ;; esac
      deny "git config writes." ;;
    push|pull|fetch|checkout|switch|reset|rebase|merge|clean|remote|cherry-pick|revert|worktree|submodule)
      deny "git $sub is off-limits: the loop commits on its own branch (loop/atlas-structure-v1) and never pushes, switches, or rewrites history. Aaron reviews and pushes." ;;
    *)
      deny "git $sub is not on the sanctioned list (read subcommands + add/commit/restore/rm/mv/apply)." ;;
  esac
}

# Split on separators; check each segment's head command.
SEGMENTS="${CMD//&&/$'\n'}"; SEGMENTS="${SEGMENTS//||/$'\n'}"
SEGMENTS="${SEGMENTS//;/$'\n'}"

while IFS= read -r seg; do
  seg="${seg#"${seg%%[![:space:]]*}"}"; seg="${seg%"${seg##*[![:space:]]}"}"
  [ -n "$seg" ] || continue
  # shellcheck disable=SC2086
  set -- $seg
  while [ $# -gt 0 ]; do
    case "$1" in
      *=*) shift ;;
      timeout|nice|ionice) shift; [ $# -gt 0 ] && case "$1" in [0-9]*|-*) shift ;; esac ;;
      *) break ;;
    esac
  done
  [ $# -gt 0 ] || continue
  head_cmd="$(basename -- "$1")"; shift

  case "$head_cmd" in
    git) check_git "${1:-status}" "${@:2}" ;;
    crontab) deny "crontab is off-limits." ;;
    systemctl|sudo|su|shutdown|reboot) deny "$head_cmd mutates system state." ;;
    ssh|scp|rsync|sftp) deny "$head_cmd reaches other machines." ;;
    gh|claude|br|bv|ntm|docker|kubectl|cypher-shell|npx|npm|node) deny "$head_cmd reaches outside this loop's scope (no nested agents, no GitHub writes, no containers, no link-forge queries — paper content arrives via papers/queue/)." ;;
    curl|wget) deny "raw network fetches are blocked — paper content arrives via papers/queue/ files; missing sources go in the report as open questions." ;;
    pip|pip3) deny "no dependency installs — scripts/ must stay stdlib-only." ;;
    pkill|kill|killall) deny "process kills are not this loop's business." ;;
    rm)
      case "$seg" in
        *" /home/"*|*" ~"*|*" \$HOME"*)
          case "$seg" in
            *topoyolo*) ;; # repo-internal cleanup is fine (GUARD_RE already checked)
            *) deny "rm with an absolute path outside ~/topoyolo." ;;
          esac ;;
      esac ;;
  esac
done <<< "$SEGMENTS"

allow "sanctioned rw-loop command"
