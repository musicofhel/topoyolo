# Coverage Matrix — 6 Machines × 5 Domains

Updated: 2026-08-24 (derived by scripts/gen_stats.py from papers/annotations/)

## Paper Counts

```
                ChainCmplx    ParamHom    Matching   Stability   JointMarg     NullHyp
──────────────────────────────────────────────────────────────────────────────────────
TDA                   *29*        *29*        *16*        *28*           7        *17*
QEC                   *12*           8           7        *12*           2           9
Dynamics              *10*        *13*           2        *12*           4           7
Neuro                 *15*        *19*           4        *14*        *10*        *19*
InfoTheo                 7        *16*           5        *10*        *13*        *13*
```

(`*n*` marks deep cells ≥10.)

## Mermaid Heatmap

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px'}}}%%
block-beta
  columns 7

  space:1 CC["ChainCmplx"] PH["ParamHom"] MA["Matching"] ST["Stability"] JM["JointMarg"] NH["NullHyp"]

  TDA["TDA"] TDA_CC["29"] TDA_PH["29"] TDA_MA["16"] TDA_ST["28"] TDA_JM["7"] TDA_NH["17"]
  QEC["QEC"] QEC_CC["12"] QEC_PH["8"] QEC_MA["7"] QEC_ST["12"] QEC_JM["2"] QEC_NH["9"]
  DYN["Dynamics"] DYN_CC["10"] DYN_PH["13"] DYN_MA["2"] DYN_ST["12"] DYN_JM["4"] DYN_NH["7"]
  NEU["Neuro"] NEU_CC["15"] NEU_PH["19"] NEU_MA["4"] NEU_ST["14"] NEU_JM["10"] NEU_NH["19"]
  IT["InfoTheo"] IT_CC["7"] IT_PH["16"] IT_MA["5"] IT_ST["10"] IT_JM["13"] IT_NH["13"]
  style TDA_CC fill:#9f9,stroke:#333
  style TDA_PH fill:#9f9,stroke:#333
  style TDA_MA fill:#9f9,stroke:#333
  style TDA_ST fill:#9f9,stroke:#333
  style TDA_NH fill:#9f9,stroke:#333
  style QEC_CC fill:#9f9,stroke:#333
  style QEC_ST fill:#9f9,stroke:#333
  style DYN_CC fill:#9f9,stroke:#333
  style DYN_PH fill:#9f9,stroke:#333
  style DYN_ST fill:#9f9,stroke:#333
  style NEU_CC fill:#9f9,stroke:#333
  style NEU_PH fill:#9f9,stroke:#333
  style NEU_ST fill:#9f9,stroke:#333
  style NEU_JM fill:#9f9,stroke:#333
  style NEU_NH fill:#9f9,stroke:#333
  style IT_PH fill:#9f9,stroke:#333
  style IT_ST fill:#9f9,stroke:#333
  style IT_JM fill:#9f9,stroke:#333
  style IT_NH fill:#9f9,stroke:#333
```

## Legend

- **Bold/green cells** (≥10): Deep coverage — multiple independent instantiations documented
- All other cells: Adequate coverage (<10)

Counts cover papers with full annotations under `papers/annotations/`
(one file per paper). Index stubs without a full annotation are not counted.
Regenerate with `python3 scripts/gen_stats.py`; `check_structure.py --check`
fails if these numbers drift from the claims in README.md / docs/index.html.

## Coverage Status

69 fully annotated papers. 19 of 30 cells ≥10 (deep); min cell = 2.
