# Session 11: CORAL Multi-Agent Setup for Topo Repos

**Date**: 2026-04-07
**Scope**: Setting up CORAL orchestration to optimize topo-confidence AUROC via multi-agent feature engineering

## What Was Done

Research and planning only — no code was written. The plan is at `~/.claude/plans/prancy-moseying-koala.md`.

### CORAL Exploration

CORAL v0.2.0 lives at `~/CORAL`. Key concepts learned:

- **Task structure**: `task.yaml` + `eval/grader.py` + `seed/` directory
- **Grader**: Class inheriting `TaskGrader` with `evaluate() -> ScoreBundle`. Helpers: `self.run_script_json()`, `self.read_eval_path()`, `self.score(value, explanation)`, `self.fail(reason)`
- **Agents**: Claude Code subprocesses in git worktrees. Share state via `.coral/public/` (attempts, notes, skills). Score via `coral eval -m "description"`.
- **Workflow**: agents modify seed code → `coral eval` → grader scores → agents read feedback → iterate
- **CLI**: `coral start -c task.yaml`, `coral status`, `coral log`, `coral ui` (web dashboard :8420)
- **Runtime**: `claude_code` runtime, can specify model (opus/sonnet), `agents.count=N` for parallel agents
- **Data**: Large files should NOT go in seed git repo. Use absolute paths to reference cached data externally.

### Data Audit

Both datasets are verified and compatible:

| Dataset | Path | Shape | Contents |
|---------|------|-------|----------|
| Token trajectories | `~/topo-confidence/data/experiment1_v2/trajectories.npz` | 500 × (var, 1536) | Per-token last-layer hidden states, 155MB |
| Layer states | `~/att-docs/data/transformer/math500_hidden_states_aligned.npz` | (500, 29, 1536) | Mean hidden state per layer, 205MB |
| TC correctness | `~/topo-confidence/data/experiment1_v2/trajectory_meta.json` | 500 labels | 57 correct (11.4%), key: `correct` |
| ATT correctness | `~/att-docs/data/transformer/math500_correctness.npz` | 433 labels | 38 correct (8.8%), key: `correct` |
| TC features | `~/topo-confidence/data/experiment1_v2/per_problem.jsonl` | 500 records | All 13 features + correctness per problem |
| TC manifest | `~/topo-confidence/data/experiment1_v2/manifest.json` | metadata | Model, config, git hash, timestamps |

**Alignment note**: Both datasets cover MATH-500 with Qwen2.5-1.5B but from separate inference runs. topo-confidence has 500 labels; ATT has 433 (67 unparseable). Use topo-confidence labels as ground truth for the CORAL task. The 500 problems are from the same HuggingFace MATH-500 split — ordering should match but this should be verified during implementation.

**Key discovery**: ATT's `layer_hidden_states` at shape (500, 29, 1536) is completely unexploited for correctness prediction. Each problem has 29 points in 1536D (one per layer) — the topology of how representations evolve through the network. This is Phase 1d from the roadmap, and it's the highest-potential remaining feature family.

### ATT Project State

ATT at `~/att-docs` has:
- 44 scripts in `scripts/`, 97 tests (all passing), 16 modules in `att/`
- All 10 TDA-LLM directions complete with results
- Key modules: `att/llm/loader.py` (HiddenStateLoader), `att/llm/features.py` (TopologicalFeatureExtractor), `att/llm/crocker.py`, `att/llm/attention_binding.py`, `att/llm/zigzag.py`
- D2 correctness prediction AUROC: 0.580 (weaker than topo-confidence's 0.713 — different feature set)
- Cross-model data: Phi-2, Pythia-1.4B, StableLM-1.6B hidden states also cached
- Attention binding: coupling decreases with difficulty (0.683→0.465)
- Latest handoff: `2026-04-04-complex-compare-branch-b.md` (directed vs symmetric VR — null result)

---

## The Plan

### CORAL Task: `topo-auroc`

**Location**: `~/coral-tasks/topo-auroc/`

**Goal**: Beat AUROC 0.713 through multi-agent feature engineering on cached hidden-state data. Target 0.75+.

**Interface contract**: Agent's `features.py` must define:
```python
def extract_features(
    trajectories: list[np.ndarray],         # 500 arrays, each (n_tokens, 1536)
    layer_states: np.ndarray | None = None, # (500, 29, 1536)
) -> tuple[np.ndarray, list[str]]:          # (features, feature_names)
```

**Grader**: Loads trajectories + layer_states from absolute paths, loads private labels, calls agent's `extract_features()`, runs 50-fold StratifiedKFold LogisticRegression(balanced), returns AUROC as primary score with per-feature breakdown as feedback.

**Seed**: 7-feature baseline from topo-confidence (the known-good set), made self-contained. Includes `check.py` for local validation without labels, and `baseline_notes.md` documenting what failed and why.

**Config**: 3 agents, claude_code runtime, opus model, research enabled, heartbeat every 5 evals + plateau pivot at 15.

**Design space for agents**:
- Feature engineering (new topological features, persistence landscapes, Wasserstein distances)
- Fix the null hypothesis (Gaussian null instead of shuffled-token)
- Exploit multi-layer data (crystallization, dissolution, layer-wise entropy)
- Parameter tuning (PCA dims, subsample size, max_dim)
- Feature selection (forward/backward, L1 regularization)
- Better bridge features (different k, different token positions)

### Directory Structure

```
~/coral-tasks/topo-auroc/
├── task.yaml                    # Full task config
├── eval/
│   ├── grader.py               # AUROC evaluation (private)
│   └── data/
│       └── labels.json         # Correctness labels (private)
└── seed/
    ├── pyproject.toml           # numpy, ripser, persim, scikit-learn, scipy
    ├── features.py              # 7-feature baseline (agents modify this)
    ├── check.py                 # Local validation (shape/stats/timing)
    └── baseline_notes.md        # Research context + what failed
```

---

## Implementation Steps (for next session)

1. `mkdir -p ~/coral-tasks/topo-auroc/{eval/data,seed}`
2. Extract correctness labels → `eval/data/labels.json`
3. Write `eval/grader.py` — subprocess-based eval, loads data, computes AUROC
4. Extract `seed/features.py` from `~/topo-confidence/topo_confidence/features.py` — make self-contained, 7-feature baseline, `extract_features()` interface
5. Write `seed/check.py` — local validation
6. Write `seed/pyproject.toml` — minimal deps
7. Write `seed/baseline_notes.md` — research context
8. Write `task.yaml` — full config
9. `cd ~/CORAL && uv run coral validate ~/coral-tasks/topo-auroc` — verify grader works
10. `cd ~/coral-tasks/topo-auroc && uv run coral start -c task.yaml` — launch 3 agents
11. Monitor: `coral status`, `coral log`, `coral ui`

### Key Files to Extract From

| Source File | Extract What |
|-------------|-------------|
| `~/topo-confidence/topo_confidence/features.py` | 7-feature baseline: PCA, ripser, persistence_entropy, bridge_silhouette. Make self-contained with `extract_features()` interface. |
| `~/topo-confidence/scripts/experiment1_v2.py` lines 129-189 | AUROC computation: StratifiedKFold, LogisticRegression, bootstrap CI. Replicate in grader. |
| `~/CORAL/examples/mnist/eval/grader.py` | Grader pattern: TaskGrader subclass, subprocess evaluation, ScoreBundle return. |
| `~/CORAL/examples/mnist/task.yaml` | task.yaml pattern. |

### Critical Implementation Details

1. **Grader subprocess isolation**: The grader should run agent's code in a subprocess (not import directly) to catch crashes, OOM, infinite loops. Use `self.run_script_json()` pattern from MNIST grader.

2. **Feature extraction timeout**: Cap at 120s. If agents add expensive features (surrogates, large max_dim), the grader should fail gracefully with a timeout message.

3. **Degenerate feature detection**: Grader should warn (in feedback) about features with zero variance — agents need this signal to prune bad features.

4. **Multi-score feedback**: Primary score is LR AUROC. Also report per-feature univariate AUROC, extraction time, n_features, and any degeneracy warnings in the feedback string.

5. **Data loading**: Both data files are large (155MB + 205MB). The grader should load them once and cache, or load at evaluation time (300s timeout gives plenty of room). Agents' `check.py` loads the same data.

---

## Session 10 Results (carried forward from previous handoff)

### topo-features: VALIDATED — Mean max |rho| = 0.710
5-system benchmark passed. New features genuinely useful: persistence_landscape_norm (rho 0.961), channel_synergy (rho 0.910), persistence_significance (rho 0.723 on chaotic).

### topo-confidence: New features HURT AUROC
13-feature AUROC = 0.691 < 7-feature baseline 0.713. Root causes identified:
- **ph_significance**: Wrong null for high-dim point clouds (shuffling rows preserves geometry)
- **H2 features**: Sparse at subsample=100 in 30D (45% zero)
- **topological_sensitivity**: No predictive power (AUROC 0.511)

### Still Pending
- Feature ablation (`scripts/validate_features.py` ready, not run)
- Remove degenerate features from topo-confidence defaults
- Phase 1d (multi-layer) — now the primary target via CORAL
- Phase 1e (Wasserstein calibration) — not started
- Phase 3 (att-docs experiments) — not started
