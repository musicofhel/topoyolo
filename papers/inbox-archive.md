# Inbox — Archive (Waves 1-3)

Archived annotations from sessions 1-3. For current annotations (Waves 4+), see [inbox.md](inbox.md).

Full-depth annotations of papers in the topo-rosetta corpus. Each paper is cross-referenced in the dual index (by-domain + by-structure) and relevant atlas files.

---

## Wave 1-2 annotations — migrated to per-paper files

Each annotation below is verbatim-migrated to `papers/annotations/` (A3 slice 1):

- [de la Fuente et al. (2025) — non-Pauli decoding](annotations/2604.02033.md) — `annotations/2604.02033.md`
- [Takens (1981)](annotations/takens-1981.md) — `annotations/takens-1981.md`
- [Sauer, Yorke, Casdagli (1991)](annotations/sauer-1991.md) — `annotations/sauer-1991.md`
- [Bauer (2021) — Ripser](annotations/2108.03831.md) — `annotations/2108.03831.md`
- [Peek et al. (2025) — TE + directed PH](annotations/2508.19048.md) — `annotations/2508.19048.md`
- [Schreiber (2000) — transfer entropy](annotations/schreiber-2000.md) — `annotations/schreiber-2000.md`
- [Tort et al. (2010) — PAC modulation index](annotations/tort-2010.md) — `annotations/tort-2010.md`
- [Giusti et al. (2015) — clique topology](annotations/1502.06172.md) — `annotations/1502.06172.md`
- [Reimann et al. (2017) — directed cliques/cavities](annotations/10.3389-fncom.2017.00048.md) — `annotations/10.3389-fncom.2017.00048.md`
- [Dabaghian et al. (2012) — hippocampal PH](annotations/10.1371-journal.pcbi.1002581.md) — `annotations/10.1371-journal.pcbi.1002581.md`
- [Curto & Itskov (2008) — cell groups](annotations/10.1371-journal.pcbi.1000205.md) — `annotations/10.1371-journal.pcbi.1000205.md`
- [Divol & Lacombe (2019) — PD space as OT](annotations/1901.03048.md) — `annotations/1901.03048.md`
- [Vejdemo-Johansson & Mukherjee (2018)](annotations/1812.06491.md) — `annotations/1812.06491.md`
- [Harrington et al. (2017) — multiparameter PH](annotations/1708.07390.md) — `annotations/1708.07390.md`
- [Wong & Yang (2019) — info geometry ↔ OT](annotations/1906.00030.md) — `annotations/1906.00030.md`

## Core ATT papers (annotated)

### Cohen-Steiner, Edelsbrunner, Harer (2007) — "Stability of persistence diagrams"
**Domain**: TDA. **Machines**: Stability (bottleneck ≤ Hausdorff), parameterized homology. **Full annotation**: [annotations/math-0604068.md](annotations/math-0604068.md).

### Adams et al. (2017) — "Persistence images"
**Domain**: TDA. **Machines**: Parameterized homology (vectorized), stability (W_1 Lipschitz bounds, Theorems 1-4), matching (implicit via Wasserstein optimal bijection), chain complex (implicit, Appendix A). **Full annotation**: [annotations/1507.06217.md](annotations/1507.06217.md).

### Giusti, Curto et al. (2015) — "Clique topology reveals intrinsic geometric structure"
**Domain**: Neuroscience + TDA. **Machines**: Chain complex (clique complex on correlations), parameterized homology, null hypothesis. **Full annotation**: [annotations/1502.06172.md](annotations/1502.06172.md).

### Gardner et al. (2022) — "Toroidal topology of population activity in grid cells"
**Domain**: Neuroscience, TDA. **Machines**: Chain complex, parameterized homology, stability, null hypothesis, joint-vs-marginal. The torus IS the neural manifold — same object as the toric code's base space, different interpretation. **Full annotation**: [annotations/10.1038-s41586-021-04268-7.md](annotations/10.1038-s41586-021-04268-7.md). **See also**: `cross_domain_bridges.md` (neuro ↔ QEC via shared T²).

### Sugihara et al. (2012) — CCM (Science, DOI: 10.1126/science.1227079)
**Domain**: Dynamical systems + causal inference. **Machines**: Joint-vs-marginal (manifold cross-prediction), stability (convergence criterion), null hypothesis (no-coupling null + surrogates), parameterized homology (weak — library size L as filtration). **Full annotation**: [annotations/10.1126-science.1227079.md](annotations/10.1126-science.1227079.md).

### Tsuda (2001) — "Chaotic itinerancy"
**Domain**: Neuroscience + dynamical systems. **Machines**: Parameterized homology (attractor switching = path through topology space), stability (quasi-stability via attractor ruins), null hypothesis (fixed-point/limit-cycle as non-itinerant null), chain complex (weak — sequence of ruins with heteroclinic connections). **Full annotation**: [annotations/10.1017-S0140525X01000097.md](annotations/10.1017-S0140525X01000097.md).

## Found and annotated (Wave 4b)

Each annotation below is verbatim-migrated to `papers/annotations/` (A3 slice 2):

- [Kitaev (1997) — fault-tolerant quantum computation by anyons](annotations/quant-ph-9707021.md)
- [Dennis, Kitaev, Landahl, Preskill (2002) — topological quantum memory](annotations/quant-ph-0110143.md)
- [Perea & Harer (2013) — SW1PerS sliding-window persistence](annotations/1307.6188.md)
- [Cohen-Steiner, Edelsbrunner, Harer (2007) — stability of persistence diagrams](annotations/math-0604068.md)

## Wave 3 triage annotations

Migrated verbatim to `papers/annotations/` (A3 slice 2):

- [Baudot & Bennequin (2015) — the homological nature of entropy](annotations/baudot-2015.md)
- [Bradley (2021) — entropy as a topological operad derivation](annotations/2107.09581.md)
- [Kolchinsky (2024) — PID redundancy as information bottleneck](annotations/2405.07665.md)

## Phase 2 annotations (2026-04-06, session 2)

Migrated verbatim to `papers/annotations/` (A3 slice 3):

- [Freedman, Kitaev, Larsen, Wang (2001) — topological quantum computation](annotations/quant-ph-0101025.md)
- [Barannikov et al. (2021) — manifold topology divergence](annotations/2106.04024.md)
- [Bombin & Martin-Delgado (2007) — topological subsystem codes / color code lattice gauge](annotations/0711.0468.md)
- [Oizumi, Albantakis, Tononi (2014) — IIT 3.0 / phi](annotations/10.1371-journal.pcbi.1003588.md)
- [Gardner et al. (2022) — toroidal topology of grid cells](annotations/10.1038-s41586-021-04268-7.md)
- [Sugihara et al. (2012) — CCM convergent cross mapping](annotations/10.1126-science.1227079.md)
- [Adams et al. (2017) — persistence images](annotations/1507.06217.md)
- [Shwartz-Ziv & Tishby (2017) — information bottleneck / deep learning](annotations/1703.00810.md)
- [Tsuda (2001) — chaotic itinerancy](annotations/10.1017-S0140525X01000097.md)
