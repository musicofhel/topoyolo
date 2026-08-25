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
- **B2 [in_progress: pass 45 — batch-008 reservoir-gs group CLOSED 6/6 (04 2110.08631 Smith-Kim-Lu-Bassett abstraction-as-continuum-of-attractors, zero-Lyapunov spectral certificate; 05 2108.04074 Röhm-Gauthier-Fischer unseen-attractor inference beyond training support; 06 2506.22335 Ahmed-Tennie-Magri quantum RC GS=ESP + noise-dissipation robustness — completes the matching-stability-capacity ladder); counts to derived 146, deep cells 29. Next: kuramoto candidates 07-09, then B3 dynamical_systems bridge-pair slice after batch close. History: pass 44 — batch-008 reservoir-gs slice 3/6 ANNOTATED (2108.05024 Grigoryeva-Hart-Ortega Takens-as-generalized-synchronization — flagged B3 bridge pair with 2409.08768 recorded in annotation + both index entries; 2401.00885 Hart conditional-Lyapunov stability margin; 2501.11357 Fadera pullback-attractor dimension bound); counts to derived 143, deep cells 29. Index-prose dedup check clean for all three. batch-008 reservoir-gs slice 3/6 ANNOTATED (2108.05024 Grigoryeva-Hart-Ortega Takens-as-generalized-synchronization — flagged B3 bridge pair with 2409.08768 recorded in annotation + both index entries; 2401.00885 Hart conditional-Lyapunov stability margin; 2501.11357 Fadera pullback-attractor dimension bound); counts to derived 143, deep cells 29. Index-prose dedup check clean for all three. Next: batch-008 reservoir-gs candidates 04–06. History: pass 43 — batch-007 CLOSED 12/12: null-surrogate candidates 10-12 ANNOTATED (1101.6063 Guarin band-phase randomized surrogates — partially-destructive null for non-stationarity; 1211.1162 Donges visibility-graph irreversibility — surrogate-free branch of the null lineage, origin of the e27040402 Third-Pass entry; 1306.4064 Small/Judd/Stemler network surrogates — rare explicit authorial cross-domain bridge to time-series surrogates). Sanctioned protocol adopted: README/docs count patches now happen in the SAME commit as gen_stats regen (drift class removed). Counts at derived 140, deep cells 28. B3 flag: batch-008 reservoir-gs candidate-01 (Takens embedding IS generalized synchronization) pairs with 2409.08768 — treat as bridge pair. Next: batch-008 reservoir-gs candidates 01-03. History: pass 41 closed batch-007 qec-mwpm group 6/6 (01 Higgott–Gidney sparse blossom 2303.15933; 02 Pattison et al. soft info 2107.13589; 03 Higgott et al. belief-matching 2203.04948 → boundary_operators; 04 Baireuther et al. RNN decoder 1705.07855 — joint-vs-marginal gain over marginal matching; 05 Hack et al. BP-on-decoding-graph 2603.05381 — carrier-graph fix for Tanner-BP's threshold failure, joins ldpc-bp lineage; 06 Fowler et al. 1202.5602 — O(n²) average-case complexity anchor of exact MWPM). See history below for batches 001–006.]]**** History: batch-001 21/21, batch-002 18/40 (22 HELD-by-orchestrator),
  **batch-003 28/28 FULLY CONSUMED (pass 23)** — (8 annotated, 13 rejected): pass-13 added
  candidate-18 → ying-2016, candidate-12 → liu-2025, candidate-03 → brusch-2023,
  candidate-19 → silva-2018; pass-13 rejections 02/06/07/09/10/11/15/16/17/20
  (zero machines / off-mission / DTW-as-tool). **batch-002 started (pass 14:
  candidates 01–03 REJECTED — geometric-dl application wrappers, zero
  machines). Pass 15 (slice-6): candidate-04 REJECTED (GNN text-class
  wrapper), candidate-07 REJECTED (Mézard-Mora duplicate — already annotated
  as 0803.3061), candidate-09 REJECTED (Hodge-Aware CL duplicate, already in
  tda.md), candidate-10 ANNOTATED → TPCC `annotations/2303.16716.md`;
  candidate-10 ANNOTATED → TPCC `annotations/2303.16716.md`; passes 16–17
  (slices 7–8): candidates 05, 06 REJECTED (equivariance wrappers), 08
  REJECTED (CL wrapper — separatrix tag confirmed misassigned), 11 REJECTED
  (Cheeger refinement duplicate of Jost & Zhang 2302.01069), 12 REJECTED
  (cavity-as-tool), 13 REJECTED (KMM Fano, zero machines), 14 REJECTED
  (Osher–Sethian level-set numerics <2 machines), 15 REJECTED (Barandes
  stochastic-quantum: one machine only); batch-002 now 18/40 consumed
  (pass 18/slice-9: candidates 16 REJECTED — Seshadri constants, zero machines;
  17 REJECTED — SNGP, one-machine Stability-only, OOD is separatrix-class per A6;
  18 REJECTED — Dean BSM info-geometry single-author draft); atlas-general
  tranche ran 6/6 rejects. **HALT ADOPTED (orchestrator, pass 19): remaining 22
  batch-002 candidates are HELD-by-orchestrator (NOT rejected) — may return under
  a machines-first re-triage.** **batch-003 started (pass 19/slice-10): candidates
  01+02 were both already prose blocks in the indices (queue dedup checked only
  annotations/) → promote-on-encounter: migrated verbatim to
  annotations/2510.22002.md + annotations/10.3390-electronics9050823.md,
  crossrefs repointed, counts to derived 80. **Pass 20/slice-11: candidate-04
  also a prose block (by-domain/tda.md) → promote-on-encounter to
  annotations/10.1007-s00521-024-10787-x.md (dedup-gap fix adopted and
  confirmed); candidates 03 REJECTED (CHIRPS, zero machines — filter artifact),
  05 REJECTED (TopP-S, one-machine PH-descriptor wrapper); counts to derived
  81; Dynamics×Matching unchanged at 5. **Pass 21/slice-12–14: filtration-ph
  remainder + transport-matching group fully consumed, ALL six rejected —
  06 PHOM one-machine PH-descriptor wrapper; 07 PHG-Net + 08 ATPGCN
  PH-as-feature application wrappers; 09 QR-DQN Wasserstein-as-loss;
  10 Hawkes FCLT convergence-rate tool; 11 GWGAN single-machine GW wrapper
  (covered by FUGW 2206.09398 + merge-tree s41468); 12 CDRL Cramér-distance
  RL theory; 13 Cornulier commability pure geometric group theory; 14 CP-DRL
  OT-curriculum wrapper. **Pass 22 (slices 15–17): info-machines group CLOSED,
  6/6 consumed — 5 were dedup artifacts (promote-on-encounter: 15 Kawaguchi from
  cross_domain_bridges ledger, 16 Kolchinsky PID-01 prose block, 17 Belghazi MINE
  prose block, 20 Wickstrøm prose block, 19 CS-IB from second_pass SP-03 ledger);
  only 18 CCMI was genuinely new (annotated as 1906.01824). **Pass 23
  (slices 18–22): batch-003 FULLY CONSUMED 28/28 — stability-bounds group:
  21+22 REJECTED (one-machine Stability-class; 22 Raginsky–Recht flagged
  notable for re-triage); null-surrogate group: 23 REJECTED (filter artifact),
  24 ANNOTATED → annotations/2005.06573.md (dHSIC permutation consistency,
  machines null hypothesis + joint-vs-marginal), 25 promote-on-encounter
  (Bandt SP-13 → annotations/10.1007-s00362-020-01171-7.md), 26 ANNOTATED →
  annotations/10.1111-2041-210X.13985.md (max-ent soft-constraint nulls);
  chain-complex group: 27 ANNOTATED → annotations/10.1016-j.physrep.2020.05.004.md
  (Battiston higher-order networks survey), 28 REJECTED (PH-as-tool pruning
  wrapper). **Pass 24 (slice-23): batch-004 started, dyn-matching group 3/4 consumed — 01 ANNOTATED as
  2409.08768 (measure-theoretic Takens: delay embedding as pushforward between measure spaces, OT machinery) + 02 ANNOTATED as
  1907.08260 (reverse direction: attractor-reconstruction histories disambiguate OT map identification); 03 TrajectoryNet REJECTED
  (one-machine dynamic-OT wrapper, superseded by MIOFlow candidate-04). Dynamics×Matching 5→7; counts at derived 92. Abstract-only
  provenance — both entries depth-limited.] **Pass 25 (slice-24): dyn-matching CLOSED 4/4 + stoch-thermo opened —
  04 MIOFlow ANNOTATED as 2206.14928 (neural-ODE flow realizing dynamic-OT coupling; geodesic autoencoder couples learned latent metric to the OT ground cost; matching + stability weak);
  NEW DOMAIN by-domain/statistical_physics.md opened for the stoch-thermo group;
  05 Nakazato-Ito ANNOTATED as 2103.00503 (entropy production ≥ L2-Wasserstein path length; thermodynamic speed limits; matching-as-dissipation semantic divergence flagged);
  07 Ito-Oizumi-Amari ANNOTATED as 1810.09545 (additivity violation of partial EP = stochastic interaction/IIT — joint-vs-marginal excess in dissipation units; Neuroscience↔StatPhys bridge).
  Counts at derived 95. Lint 0 errors, crossref debt back to baseline 2. Abstract-only provenance — all depth-limited.] **Pass 26 (slice-25): stoch-thermo CLOSED
  4/4 — 06 ANNOTATED as 2209.00527 (info geometry ↔ OT unified via excess EP; matching core), 08 ANNOTATED as 1408.1224 (Barato–Seifert information reservoirs;
  generalized second law as joint-vs-marginal bookkeeping; null weak), 09 ANNOTATED as 2312.03489 (oscillatory-mode EP decomposition → monkey ECoG awake vs
  anesthesia; second Neuroscience↔StatPhys bridge). batch-004 now 9/17 consumed; counts at derived 97 — README/docs were stale at 92, now patched and enforced by
  --check. gen_stats grid question answered in report: alias/6th-column follow-up should precede domain confirmation.]** **Pass 27 (orchestrator-directed
  grid/alias follow-up, 4fb71b9): statistical_physics added as 6th domain column in gen_stats (36 cells); full DOMAIN_ALIASES + KNOWN_QUALIFIERS table landed,
  unrecognized-domain warnings 28→0; parser now accepts the short `Joint-vs-marginal` bullet label and 2404.17951 got its missing Domain(s) metadata line → counts
  at derived 99, min cell 2, 23/36 deep; README/docs/matrix repointed, lint --check 0 errors. Awaiting Aaron ratification of ML→InfoTheo and OT→TDA alias calls.] **Pass 27 cont. (slice-27): batch-004 rate-distortion 10 NERD ANNOTATED as 2204.01612 (neural amortization of the BA soft-matching functional; RD as computable null for DNN codecs) + 11 Theis–Wagner ANNOTATED as 2104.13662 (RDPF achievability/converse; perception = marginal-agreement constraint on the coupling); 12 REJECTED (<2 machines beyond covered RD lineage). 5 Wave-9/10-era wrong-pointer crossrefs fixed (optimal_transport ×3, information_theory Wave-10a/10b). Counts at derived 101; lint --check 0 errors.] **Pass 28 (slice-28): batch-004 rate-distortion CLOSED 4/4 (13 Yadav et al. ANNOTATED as 2601.16461 — log-likelihood distortion, semantic reconstruction as generative soft-matching, perfect-perception RD as boundary case); ldpc-bp opened 2/2-of-remaining consumed — 14 Aref-Macris-Vuffray ANNOTATED as 1307.5210 (spatially coupled LDGM + BP decimation, cavity phase diagram explains threshold saturation to the Shannon null) + 16 Jain-Koehler-Liu-Mossel ANNOTATED as 1905.10031 (bounded-memory BP transitions strictly below KS; OT imported as proof technology). Ingestion cap ≤3/pass binds → candidates 15+17 remain for slice-29, then batch-004 closes. Counts at derived 104; lint --check 0 errors.] **Pass 29 (slice-29): batch-004 CLOSED 17/17 — ldpc-bp 15 Vicente-Saad-Kabashima ANNOTATED as cond-mat-9908358 (replica decoding transition placed on Shannon's bound by degree-distribution choice) + 17 Decelle et al. ANNOTATED as 1109.3041 (SBM cavity phase diagram: detectability/undetectability + easy/hard transitions; canonical detectability-transition anchor). Sanctioned wrong-pointer lint task executed same pass: all 106 Full-annotation targets verified to exist; 9 high-confidence wrong pointers repaired via inline-id resolution (2508.19048 → quant-ph-9906129/quant-ph-9702058/2103.06309; 1703.00810/tort-2010 → 1909.02297/1411.2832; Tsuda → 2209.13581). RESIDUAL DEBT catalogued: Wave-1–10-era "Full annotation" pointers to shared catch-all files (2508.19048 ×~38, Tsuda 10.1017 ×~19, 0711.0468 ×~26, tort-2010 ×~14, 1703.00810 ×~16 across by-* files) whose entries carry no inline id — need per-entry title→annotation lookup, ~5/pass. Counts at derived 106; lint --check 0 errors.] **Pass 30 (slice-30): batch-005 opened, channel-capacity 3/7 consumed — 04 Choi-Bao-Qi-Altman ANNOTATED as 1903.05124 (MIPT AS a QEC transition; feeds thin QEC×Joint-vs-Marginal cell), 03 Qian-Roy ANNOTATED as 1112.4589 (channel capacity zero iff free-energy expenditure zero), 06 Plenio-Virmani ANNOTATED as quant-ph/0702059 (memory-channel capacity ↔ spin-chain criticality); dual-index filed qec/info/statphys + phase_transitions. Sanctioned wrong-pointer sweep same pass: 3 repaired (Trinca→2410.20233, Hamilton-Leditzky→2307.07492, Berry→2209.13581, all off the 0711.0468 catch-all). Counts at derived 109, deep cells 23→26; lint --check 0 errors.] **Pass 31 (slice-31): batch-005 channel-capacity 6/7 consumed — 01 Bereyhi et al. ANNOTATED as
2205.08782 (all-or-nothing critical rate IS channel capacity via replica; wiretap secrecy as joint-vs-marginal threshold — second QEC-adjacent feed), 02 Kabashima-Murayama-Saad ANNOTATED
as cond-mat/9908104 (Gallager typical-case capacity saturation across sparse-matrix families; TAP ≡ BP decoding — ancestor of ldpc-bp group), 05 Kelly et al. ANNOTATED as 2210.11547
(adversarial unitary-vs-measurement game; coherence-tuned capacity phase transition; coherence bounds stabilizer code distance). Sanctioned wrong-pointer sweep same pass: 5 repaired in
qec.md (Berry→2209.13581, Hastings-Haah→2107.02194, Aharonov-Ben-Or→quant-ph-9906129, Knill-Laflamme-Zurek→quant-ph-9702058, Breuckmann-Eberhardt→2103.06309) — qec.md now clean of
0711.0468 catch-alls except its own genuine entry. Counts at derived 112, deep cells 27; lint --check 0 errors.]** **Pass 32 (slice-32): channel-capacity group CLOSED 7/7 + ph-stability opened 2/5 — 07 Ashikaga-Asgari-Targhi ANNOTATED as 1708.03990 (capacity/MI/TE as spatial invariant field locating cardiac order-disorder wavebreaks; applied-dynamics close), 08 Bubenik-Scott ANNOTATED as 1205.3669 (categorified PH; interleaving generalizes bottleneck; stability as categorical property), 09 Gulen-McCleary ANNOTATED as 2201.06650 (Galois connections unify interleavings+matchings; Rota => easier bottleneck-stability proof). Counts to derived 115, deep cells 27; README cell-count drift (23 vs 27 deep) found and patched. Lint --check 0 errors.]** Also pass 14: fixed 5 wrong-pointer
  crossrefs in by-structure/optimal_transport.md; counts now at derived 78.
  Lint --check 0 errors.]
  Consume queue batches.** Repeatable task — each pass takes ≤3
  papers from the oldest unconsumed batch. Prioritize (from Wave-10 state):
  neuroscience cells (weakest), Matching×InfoTheory, and any paper bridging
  ≥3 domains. Every annotated paper: per-paper file + both indices + matrix
  regen + lint green. Status line here records papers consumed / queued.
- **B3 [in_progress: sub-slices 1–4 done passes 33–38 — 1: ANTISYNONYMS "Matching metric ≠ stability guarantee"; 2: thermodynamic-instantiation subsections on optimal_transport.md + composite_systems.md; 3 (pass 37): MATCHING.md "Two Cross-Machine Roles" (OT-as-proof-technology inbound to statphys via 1905.10031; PH→Matching bridge via Chambers–Meng 2507.01171) + cond-mat/9908104 ldpc-bp ancestor lineage note in statistical_physics.md; 4 (pass 38): optimal_transport.md "Monge–Kantorovich split inside this file" (coupling-side vs map-side corpus instances, non-atomic GM=GW as regime theorem). No queued hooks remain; next options: batch-002 HELD re-triage slice (machines-first) or request batch-007.] Atlas synthesis touch-ups.** After ~15 new papers: re-read the
  6 atlas files against the new corpus; integrate the strongest new bridges
  and any new ANTISYNONYMS. One atlas file per pass max.

## Ledger protocol (every pass)

Pick the FIRST task not `[done]` (or continue an `[in_progress]` one). Phase B
is locked until A1–A5 are `[done]` (A6 may trail). When a pass advances a
task, edit its status line here: `[open]` → `[in_progress: <one-line state>]`
→ `[done <date> <commit>]`. Add discovered subtasks as indented bullets under
their parent. Never delete history — strike through with `~~` if a task dies,
and say why.
