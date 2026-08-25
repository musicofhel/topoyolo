# Coverage Matrix — 6 Machines × 5 Domains

Updated: 2026-08-24 (derived by scripts/gen_stats.py from papers/annotations/)

## Paper Counts

```
                ChainCmplx    ParamHom    Matching   Stability   JointMarg     NullHyp
──────────────────────────────────────────────────────────────────────────────────────
TDA                   *29*        *29*        *16*        *28*           7        *17*
QEC                   *12*           8           7        *12*           2           9
Dynamics              *10*        *14*           4        *15*           5        *10*
Neuro                 *18*        *21*           5        *14*        *14*        *23*
InfoTheo                 9        *17*           7        *11*        *16*        *17*
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
  DYN["Dynamics"] DYN_CC["10"] DYN_PH["14"] DYN_MA["4"] DYN_ST["15"] DYN_JM["5"] DYN_NH["10"]
  NEU["Neuro"] NEU_CC["18"] NEU_PH["21"] NEU_MA["5"] NEU_ST["14"] NEU_JM["14"] NEU_NH["23"]
  IT["InfoTheo"] IT_CC["9"] IT_PH["17"] IT_MA["7"] IT_ST["11"] IT_JM["16"] IT_NH["17"]
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
  style DYN_NH fill:#9f9,stroke:#333
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

77 fully annotated papers. 20 of 30 cells ≥10 (deep); min cell = 2.
