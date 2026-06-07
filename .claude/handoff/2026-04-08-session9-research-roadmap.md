# Session 9: Topoyolo-Guided Research Roadmap

**Date**: 2026-04-08
**Scope**: Cross-domain research transfer plan for att-docs, topo-features, topo-confidence

## Core Insight

All three implementation projects use only 1 of topoyolo's 6 abstract machines (Chain Complex via Rips/PH). Five machines are completely untapped:

| Machine | topo-features | topo-confidence | att-docs |
|---------|:---:|:---:|:---:|
| Chain Complex (Rips/PH) | H0, H1 | H0, H1 + bridge | H0, H1 (two-cluster) |
| Parameterized Homology | -- | -- | Partial (layer depth) |
| Matching / OT | -- | -- | -- |
| Stability | -- | -- | -- |
| Joint-vs-Marginal Excess | -- | -- | -- |
| Null Hypothesis | -- | -- | -- |

## Full Plan

The complete implementation plan is at:
`/home/musicofhel/.claude/plans/prancy-moseying-koala.md`

It was audited with fresh eyes — all 13 paper references verified against topoyolo corpus, all code claims verified against actual source files. Errors found and fixed:
- Berry et al. 2023 misattribution (was QEC paper, not brain data) → replaced with Dabaghian et al. 2012
- persim missing from topo-features deps → flagged
- extractor.py:103 only uses last layer → pinpointed
- Cohen-Steiner stability bound applies to bottleneck, not total persistence → corrected
- All feature definitions made deterministic (thresholds, degenerate cases, formulas)

## Implementation Status

**CRITICAL: Code was added but NOT validated.** All tests pass (shapes, no-NaN, type checks) but no experiments have been run. We do not know whether any of these new features actually improve AUROC or Spearman rho. The features might be degenerate on real data (all zeros), redundant with existing features, or actively harmful. Before treating any of this as "done":

1. **Extract features on real data** — run experiment scripts on actual LLM hidden states / dynamical systems
2. **Check for degenerate features** — are the new features producing non-trivial, varying values?
3. **Measure AUROC delta** — does topo-confidence improve from 0.699 toward 0.75+ with new features?
4. **Feature ablation** — which new features help, which are noise? Remove the noise.
5. **Cross-model transfer** — does the Phi-2 AUROC (0.383) improve?
6. **Spearman rho check** — does topo-features mean |rho| improve from 0.76?

Until steps 1-4 are done, this is toolkit expansion, not optimization.

### Phase 1: topo-confidence (~/topo-confidence) — CODE COMPLETE, NOT VALIDATED

Features went from 7 → 13. All tests pass (22/22).

| Step | Machine | Change | Status |
|------|---------|--------|--------|
| 1a | Joint-vs-Marginal | max_dim=1→2, added betti_2/h2_total_persistence/h2_persistence_entropy | **Code done** |
| 1b | Null Hypothesis | New null.py: K=100 shuffles, H0/H1_ph_significance z-scores | **Code done** |
| 1c | Stability | topological_sensitivity: noise at eps={0.01,0.05,0.1}, OLS slope | **Code done** |
| 1d | Parameterized Homology | Modify extractor.py:103 for multi-layer, crystallization/dissolution features | **Not started** |
| 1e | Matching/OT | Wasserstein calibration via persim | **Not started** |

New files created:
- `topo_confidence/null.py` — shuffled-token null distribution + z-score significance

Files modified:
- `topo_confidence/features.py` — max_dim=2, 6 new features, _compute_topological_sensitivity()
- `tests/test_confidence.py` — updated all shape assertions (7→13)
- `spaces/app.py` — updated FEATURE_NAMES display list

Performance note: max_dim=2 benchmarked at 44.5ms vs 3.5ms (12.7x slower, not 3x as plan estimated). Still <50ms/sample — acceptable.

### Phase 2: topo-features (~/topo-features) — CODE COMPLETE, NOT VALIDATED

Features went from 5 → 10. extract_windows() now also returns Wasserstein drift. All tests pass (26/26).

| Step | Feature | Status |
|------|---------|--------|
| 2a | `persistence_landscape_norm` — L2 norm of first landscape (N=100 grid) | **Code done** |
| 2b | `birth_death_slope` — OLS slope death~birth in H1 | **Code done** |
| 2c | `wasserstein_window_drift` — Mean W1 between consecutive windows (via persim) | **Code done** |
| 2d | `persistence_stability_ratio` — |total_H1(noisy)-total_H1(clean)|/eps, 5 seeds avg | **Code done** |
| 2e | `channel_synergy` — total_H1(joint) - mean(total_H1(chan_i)), Takens per channel | **Code done** |
| 2f | `persistence_significance` — Theiler Alg 1 surrogates K=19, rank test | **Code done** |

New files created:
- `topofeatures/landscape.py` — persistence landscape L2 norm
- `topofeatures/synergy.py` — channel synergy (joint vs marginal)
- `topofeatures/null.py` — Theiler phase-randomization surrogates
- `topofeatures/matching.py` — Wasserstein window drift

Files modified:
- `topofeatures/persistence.py` — added birth_death_slope
- `topofeatures/core.py` — wired all 5 new features + stability ratio, X_original preserved for synergy/significance
- `pyproject.toml` — added persim>=0.3, scipy>=1.10
- `tests/test_core.py` — updated shape assertions, extract_windows 3-tuple return
- `examples/sklearn_pipeline.py` — updated to 3-tuple unpack

API change: `extract_windows()` now returns `(features, names, drift)` instead of `(features, names)`.

### Phase 3: att-docs (~/att-docs) — NOT STARTED

| Step | Experiment | Question |
|------|------------|----------|
| 3a | Attention-shuffled null | Is two-cluster organization real or geometric artifact? |
| 3b | Training epoch sweep | When does topology crystallize? |
| 3c | Cross-layer OT | How do token representations flow through layers? |
| 3d | Ghost stability | Do overwritten features leave topological traces? |
| 3e | PhiID decomposition | Are layers cooperating or duplicating? |

## Session 10: Validation Results (2026-04-07)

### topo-features: VALIDATED — Mean max |rho| = 0.710

5-system benchmark on dynamical systems (Rossler, Lorenz, Kuramoto, Lotka-Volterra, Sine):

| System | Max |rho| | Best Feature | Status |
|--------|----------|--------------|--------|
| Rossler | 0.851 | max_H1_persistence | PASS |
| Lorenz | 0.910 | total_H1_persistence | PASS |
| Kuramoto | 0.608 | persistence_entropy | PASS |
| Lotka-Volterra | 0.961 | max_H1_persistence | PASS |
| Sine | 0.219 | persistence_significance | FAIL |

New feature highlights:
- `persistence_landscape_norm`: max |rho| = 0.961 (Lotka-Volterra) — **best new feature**
- `channel_synergy`: max |rho| = 0.910 (Lorenz) — strong cross-channel signal
- `persistence_significance`: max |rho| = 0.723 (Rossler) — surrogates work on chaotic systems
- `birth_death_slope`: max |rho| = 0.711 (Rossler) — useful for periodic/chaotic distinction

Timing: 3.7s/sample (up from ~150ms with 5 features). Surrogates (K=19) dominate cost.

Smoke test: All 10 features finite on sine/Rossler. `channel_synergy` > 0 on 3D, = 0 on 1D (correct). `persistence_significance` = 0 on non-chaotic data (expected).

### topo-confidence: VALIDATED — New features HURT AUROC

**Headline: 13-feature AUROC = 0.691, WORSE than 7-feature baseline (0.713). Delta = -0.022.**

| Feature | Per-feature AUROC | Degenerate? | Verdict |
|---------|------------------|-------------|---------|
| H0_persistence_entropy | 0.718 | No | KEEP (top feature) |
| H0_n_features | 0.722 | No | KEEP (best individual) |
| H0_total_persistence | 0.699 | No | KEEP |
| H1_n_features | 0.684 | No | KEEP |
| H1_persistence_entropy | 0.683 | No | KEEP |
| bridge_silhouette | 0.618 | No | KEEP |
| H1_max_lifetime | 0.596 | No | KEEP |
| **H2_total_persistence** | 0.609 | 45% zero | INVESTIGATE |
| **H2_n_features** | 0.604 | 45% zero | INVESTIGATE |
| **H2_persistence_entropy** | 0.538 | 45% zero | REMOVE (near chance) |
| **topological_sensitivity** | 0.511 | No | REMOVE (near chance) |
| **H0_ph_significance** | N/A | **100% zero** | REMOVE (degenerate) |
| **H1_ph_significance** | N/A | **100% zero** | REMOVE (degenerate) |

**Why the new features failed:**
- **ph_significance (shuffled-token null)**: Completely degenerate on real LLM data. Shuffling token positions doesn't change PH of high-dimensional point clouds. The null is wrong for this domain — permuting rows of a (n_tokens × 1536) matrix preserves the overall cloud geometry.
- **H2 features**: Semi-degenerate (45% zero). 100 points in 30D is sparse for detecting 2D voids. When present, H2 features show weak signal (AUROC ~0.6).
- **topological_sensitivity**: No predictive power (AUROC 0.511 ≈ chance). Noise perturbation doesn't differentiate correct from incorrect.

**What the 7-feature baseline actually achieves:** AUROC 0.713 (CI: [0.635, 0.791]) — *higher* than the previously reported 0.699, because the bridge_silhouette (0.618) was added to the original 6 features.

**Feature extraction timing:** 0.175s/problem (87.4s for 500) — acceptable. null_k=100 adds ~0.1s/problem overhead.

**Trajectories cached:** `data/experiment1_v2/trajectories.npz` (prevents re-running 56 min of inference). Use `--from-cache` flag for future experiments.

### What's Still Needed

1. **Feature ablation** — `scripts/validate_features.py` ready, run to find optimal subset (maybe 7-feature baseline + H2_n_features?)
2. **Remove degenerate features** — ph_significance (both), H2_persistence_entropy, topological_sensitivity should be removed or made optional
3. **Phase 1d** (multi-layer extraction) — not started, highest-potential remaining feature family
4. **Phase 1e** (Wasserstein calibration) — not started
5. **Phase 3** (att-docs experiments) — not started

### Code Fixes Applied
- `topo-features/topofeatures/tsfresh_binding.py:46-49` — fixed stale 5-feature fallback to use FEATURE_NAMES
- `topo-confidence/configs/default.yaml` — updated max_dim=1→2, added null_k=100
- `topo-confidence/topo_confidence/combined.py:56` — fixed stale "7 topo" comment

### New Scripts Created
- `topo-features/scripts/validate_smoke.py` — 10-feature sanity check
- `topo-features/scripts/validate_benchmark.py` — 5-system Spearman rho benchmark
- `topo-confidence/scripts/validate_smoke.py` — 13-feature sanity check
- `topo-confidence/scripts/experiment1_v2.py` — MATH-500 with trajectory caching + --from-cache
- `topo-confidence/scripts/validate_features.py` — per-feature AUROC + ablation + speed
