# Coverage Matrix — 6 Machines × 6 Domains

Updated: 2026-08-25 (derived by scripts/gen_stats.py from papers/annotations/)

## Paper Counts

```
                ChainCmplx    ParamHom    Matching   Stability   JointMarg     NullHyp
──────────────────────────────────────────────────────────────────────────────────────
TDA                   *33*        *40*        *34*        *46*           9        *23*
QEC                   *13*        *11*        *13*        *18*           5        *13*
Dynamics              *13*        *21*           8        *21*        *10*        *17*
Neuro                 *18*        *23*           6        *16*        *17*        *26*
InfoTheo              *11*        *30*        *19*        *26*        *33*        *43*
StatPhys                 2           8           9        *10*           9        *14*
```

(`*n*` marks deep cells ≥10.)

## Mermaid Heatmap

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px'}}}%%
block-beta
  columns 8

  space:1 CC["ChainCmplx"] PH["ParamHom"] MA["Matching"] ST["Stability"] JM["JointMarg"] NH["NullHyp"]

  TDA["TDA"] TDA_CC["33"] TDA_PH["40"] TDA_MA["34"] TDA_ST["46"] TDA_JM["9"] TDA_NH["23"]
  QEC["QEC"] QEC_CC["13"] QEC_PH["11"] QEC_MA["13"] QEC_ST["18"] QEC_JM["5"] QEC_NH["13"]
  DYN["Dynamics"] DYN_CC["13"] DYN_PH["21"] DYN_MA["8"] DYN_ST["21"] DYN_JM["10"] DYN_NH["17"]
  NEU["Neuro"] NEU_CC["18"] NEU_PH["23"] NEU_MA["6"] NEU_ST["16"] NEU_JM["17"] NEU_NH["26"]
  IT["InfoTheo"] IT_CC["11"] IT_PH["30"] IT_MA["19"] IT_ST["26"] IT_JM["33"] IT_NH["43"]
  SP["StatPhys"] SP_CC["2"] SP_PH["8"] SP_MA["9"] SP_ST["10"] SP_JM["9"] SP_NH["14"]
  style TDA_CC fill:#9f9,stroke:#333
  style TDA_PH fill:#9f9,stroke:#333
  style TDA_MA fill:#9f9,stroke:#333
  style TDA_ST fill:#9f9,stroke:#333
  style TDA_NH fill:#9f9,stroke:#333
  style QEC_CC fill:#9f9,stroke:#333
  style QEC_PH fill:#9f9,stroke:#333
  style QEC_MA fill:#9f9,stroke:#333
  style QEC_ST fill:#9f9,stroke:#333
  style QEC_NH fill:#9f9,stroke:#333
  style DYN_CC fill:#9f9,stroke:#333
  style DYN_PH fill:#9f9,stroke:#333
  style DYN_ST fill:#9f9,stroke:#333
  style DYN_JM fill:#9f9,stroke:#333
  style DYN_NH fill:#9f9,stroke:#333
  style NEU_CC fill:#9f9,stroke:#333
  style NEU_PH fill:#9f9,stroke:#333
  style NEU_ST fill:#9f9,stroke:#333
  style NEU_JM fill:#9f9,stroke:#333
  style NEU_NH fill:#9f9,stroke:#333
  style IT_CC fill:#9f9,stroke:#333
  style IT_PH fill:#9f9,stroke:#333
  style IT_MA fill:#9f9,stroke:#333
  style IT_ST fill:#9f9,stroke:#333
  style IT_JM fill:#9f9,stroke:#333
  style IT_NH fill:#9f9,stroke:#333
  style SP_ST fill:#9f9,stroke:#333
  style SP_NH fill:#9f9,stroke:#333
```

## Legend

- **Bold/green cells** (≥10): Deep coverage — multiple independent instantiations documented
- All other cells: Adequate coverage (<10)

Counts cover papers with full annotations under `papers/annotations/`
(one file per paper). Index stubs without a full annotation are not counted.
Regenerate with `python3 scripts/gen_stats.py`; `check_structure.py --check`
fails if these numbers drift from the claims in README.md / docs/index.html.

## Coverage Status

134 fully annotated papers. 28 of 36 cells ≥10 (deep); min cell = 2.
