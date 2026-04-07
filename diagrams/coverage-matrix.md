# Coverage Matrix — 6 Machines × 5 Domains

Updated: 2026-04-07 (Session 6)

## Paper Counts

```
              Chain    Param   Match   Stabil  Joint   Null
              Complex  Homol           ity     v Marg  Hyp
─────────────────────────────────────────────────────────────
TDA            6+       7+      5+     7+      5+      4+
QEC           15+       8+      8+    10+      6+      9+
Dynamics       8+      11+     10+     8+      6+      7+
Neuro          6+      10+      8+     7+     13+     10+
InfoTheo       9+       9+      4+     6+     12+      8+
```

## Mermaid Heatmap

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px'}}}%%
block-beta
  columns 7

  space:1 CC["Chain\nComplex"] PH["Param\nHomology"] MA["Matching"] ST["Stability"] JM["Joint vs\nMarginal"] NH["Null\nHypothesis"]

  TDA["TDA"] TDA_CC["6+"] TDA_PH["7+"] TDA_MA["5+"] TDA_ST["7+"] TDA_JM["5+"] TDA_NH["4+"]
  QEC["QEC"] QEC_CC["15+"] QEC_PH["8+"] QEC_MA["8+"] QEC_ST["10+"] QEC_JM["6+"] QEC_NH["9+"]
  DYN["Dynamics"] DYN_CC["8+"] DYN_PH["11+"] DYN_MA["10+"] DYN_ST["8+"] DYN_JM["6+"] DYN_NH["7+"]
  NEU["Neuro"] NEU_CC["6+"] NEU_PH["10+"] NEU_MA["8+"] NEU_ST["7+"] NEU_JM["13+"] NEU_NH["10+"]
  IT["InfoTheo"] IT_CC["9+"] IT_PH["9+"] IT_MA["4+"] IT_ST["6+"] IT_JM["12+"] IT_NH["8+"]
  style QEC_CC fill:#9f9,stroke:#333
  style NEU_JM fill:#9f9,stroke:#333
  style IT_JM fill:#9f9,stroke:#333
  style DYN_PH fill:#9f9,stroke:#333
  style DYN_MA fill:#9f9,stroke:#333
  style QEC_ST fill:#9f9,stroke:#333
  style NEU_NH fill:#9f9,stroke:#333
  style QEC_NH fill:#9f9,stroke:#333
```

## Legend

- **Green cells** (≥10): Deep coverage — multiple independent instantiations documented
- **All other cells** (4–9): Adequate coverage
- All 30 cells now ≥ 4 (no thin cells remain)

## Key Changes (Session 6)

- **Match×TDA**: ~3 → **5+** (added Bubenik & Elchesen 2019, Chen & Wang 2021)
- **Match×InfoTheo**: ~3 → **4+** (added Blahut 1972 / Arimoto 1972)

## Coverage Status

All 30 cells now ≥ 4. No remaining thin cells. The matrix is fully covered.
