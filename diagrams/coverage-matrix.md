# Coverage Matrix — 6 Machines × 6 Domains

Updated: 2026-08-25 (derived by scripts/gen_stats.py from papers/annotations/)

## Paper Counts

```
                ChainCmplx    ParamHom    Matching   Stability   JointMarg     NullHyp
──────────────────────────────────────────────────────────────────────────────────────
TDA                   *37*        *41*        *35*        *50*           9        *25*
QEC                   *14*        *11*        *14*        *19*           6        *14*
Dynamics              *13*        *21*        *19*        *37*        *16*        *32*
Neuro                 *19*        *29*           7        *25*        *21*        *35*
InfoTheo              *19*        *36*        *27*        *36*        *40*        *51*
StatPhys                 2        *18*        *11*        *25*        *15*        *23*
```

(`*n*` marks deep cells ≥10.)

## Mermaid Heatmap

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px'}}}%%
block-beta
  columns 8

  space:1 CC["ChainCmplx"] PH["ParamHom"] MA["Matching"] ST["Stability"] JM["JointMarg"] NH["NullHyp"]

  TDA["TDA"] TDA_CC["37"] TDA_PH["41"] TDA_MA["35"] TDA_ST["50"] TDA_JM["9"] TDA_NH["25"]
  QEC["QEC"] QEC_CC["14"] QEC_PH["11"] QEC_MA["14"] QEC_ST["19"] QEC_JM["6"] QEC_NH["14"]
  DYN["Dynamics"] DYN_CC["13"] DYN_PH["21"] DYN_MA["19"] DYN_ST["37"] DYN_JM["16"] DYN_NH["32"]
  NEU["Neuro"] NEU_CC["19"] NEU_PH["29"] NEU_MA["7"] NEU_ST["25"] NEU_JM["21"] NEU_NH["35"]
  IT["InfoTheo"] IT_CC["19"] IT_PH["36"] IT_MA["27"] IT_ST["36"] IT_JM["40"] IT_NH["51"]
  SP["StatPhys"] SP_CC["2"] SP_PH["18"] SP_MA["11"] SP_ST["25"] SP_JM["15"] SP_NH["23"]
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
  style DYN_MA fill:#9f9,stroke:#333
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
  style SP_PH fill:#9f9,stroke:#333
  style SP_MA fill:#9f9,stroke:#333
  style SP_ST fill:#9f9,stroke:#333
  style SP_JM fill:#9f9,stroke:#333
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

178 fully annotated papers. 32 of 36 cells ≥10 (deep); min cell = 2.
