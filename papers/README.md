# papers/ — layout contract

Everything under `papers/` falls into one of the roles below. The structure
lint (`scripts/check_structure.py`) enforces this: every file or directory
directly under `papers/` must be listed here. Adding something new to
`papers/` without documenting its role here fails the lint.

## Canonical corpus

- **`annotations/`** — the corpus itself: one fully annotated paper per file,
  named by id (`<arxiv-id>.md`, `<doi-slug>.md`). Each file holds exactly one
  `## <id> --- <authors>` header at the top of its body. This directory is
  the single source of truth for counts (`scripts/gen_stats.py` derives all
  headline numbers from it). Annotation depth/format is defined by
  `METHODOLOGY.md` and `.claude/skills/annotate/SKILL.md`.
- **`by-domain/`** — index by domain (TDA, QEC, dynamical systems,
  neuroscience, information theory). Every annotation here must also appear
  in `by-structure/`.
- **`by-structure/`** — index by abstract machine (chain complex,
  parameterized homology / filtrations, matching, stability, joint-vs-marginal
  excess, null hypothesis). Dual-indexing is the core law: every annotation is
  filed on BOTH sides, enforced by the lint.
- **`atlas/`, `glossary/` live at repo root and in `docs/`; they reference
  into `annotations/` by id.

## Intake

- **`inbox.md`** — current leads and wave log. Contract at the top; pointer
  lists only — full annotations are NOT allowed here anymore (lint-enforced).
  New leads go here; when annotated, the annotation moves to `annotations/`
  and the lead line stays as history.
- **`inbox-archive.md`** — Waves 1–3 archive, pointer lists only
  (lint-enforced, same rule as inbox.md).
- **`queue/`** — Phase B ingestion queue. The orchestrator drops batches
  (`batch-NNN.md`); each pass consumes ≤3 papers per `papers/INGESTION.md`.
  See `queue/README.md`.

## Search-pass ledgers (historical, not canonical)

These four files are the working notes of the April 2026 link-forge search
passes. They hold **candidate annotations** (`## SP-nn …`, `## TP-nn …`)
written before the per-paper layout existed. They are NOT part of the corpus:
their entries have no files in `annotations/`, are not dual-indexed, and do
not count toward derived stats. Content conservation applies — entries move
out only by promotion to `annotations/` + dual index (Phase B style), never
by deletion.

- **`second_pass.md`** (2026-04-05) — second link-forge sweep, 17 candidates
  (SP-01…SP-17) plus summary tables: information bottleneck / ML-heavy
  cluster, Hawkes processes, and others.
- **`third_pass_dynamics_tda.md`** (2026-04-05) — third sweep, dynamics+TDA
  focus, 16 candidates (TP-01…TP-16, own numbering).
- **`third_pass_infotheo_cross.md`** (2026-04-05) — third sweep,
  information-theory/cross-domain focus, 9 new candidates + summary tables of
  machine/domain coverage and zero-result search gaps.
- **`third_pass_neuro_qec.md`** (2026-04-05) — third sweep, neuroscience+QEC
  focus, 12 candidates + summary tables. Note: TP-08 (Hodge-aware contrastive
  learning) and TP-12 (Mézard–Mora) were subsequently promoted and DO exist as
  canonical annotations; their ledger entries remain as provenance.
- **`cross_domain_bridges.md`** — curated list of papers explicitly bridging
  ≥2 domains (the atlas's highest-value class): 13 paper entries across three
  sections (core bridges, Phase-2 additions 2026-04-06, Wave-10a additions
  2026-04-17) plus pattern notes. Same non-canonical status as the ledgers
  above until individual entries are promoted.

Promotion path for any ledger entry: annotate to full METHODOLOGY depth →
`annotations/<id>.md` → add to both indices → regen matrix
(`python3 scripts/gen_stats.py`) → lint green. Ledger prose stays put.
