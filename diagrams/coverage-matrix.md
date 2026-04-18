# Coverage Matrix — 6 Machines × 5 Domains

Updated: 2026-04-17 (Wave 10)

## Paper Counts

```
              Chain    Param   Match   Stabil  Joint   Null
              Complex  Homol           ity     v Marg  Hyp
─────────────────────────────────────────────────────────────
TDA           10+      11+      7+    11+      5+      4+
QEC           16+       8+      8+    11+      6+      9+
Dynamics      13+      16+     11+    13+      6+      9+
Neuro         11+      12+      8+     9+     14+     12+
InfoTheo      10+      10+      5+     8+     13+      9+
```

## Mermaid Heatmap

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px'}}}%%
block-beta
  columns 7

  space:1 CC["Chain\nComplex"] PH["Param\nHomology"] MA["Matching"] ST["Stability"] JM["Joint vs\nMarginal"] NH["Null\nHypothesis"]

  TDA["TDA"] TDA_CC["10+"] TDA_PH["11+"] TDA_MA["7+"] TDA_ST["11+"] TDA_JM["5+"] TDA_NH["4+"]
  QEC["QEC"] QEC_CC["16+"] QEC_PH["8+"] QEC_MA["8+"] QEC_ST["11+"] QEC_JM["6+"] QEC_NH["9+"]
  DYN["Dynamics"] DYN_CC["13+"] DYN_PH["16+"] DYN_MA["11+"] DYN_ST["13+"] DYN_JM["6+"] DYN_NH["9+"]
  NEU["Neuro"] NEU_CC["11+"] NEU_PH["12+"] NEU_MA["8+"] NEU_ST["9+"] NEU_JM["14+"] NEU_NH["12+"]
  IT["InfoTheo"] IT_CC["10+"] IT_PH["10+"] IT_MA["5+"] IT_ST["8+"] IT_JM["13+"] IT_NH["9+"]
  style TDA_CC fill:#9f9,stroke:#333
  style TDA_PH fill:#9f9,stroke:#333
  style TDA_ST fill:#9f9,stroke:#333
  style QEC_CC fill:#9f9,stroke:#333
  style QEC_ST fill:#9f9,stroke:#333
  style DYN_CC fill:#9f9,stroke:#333
  style DYN_PH fill:#9f9,stroke:#333
  style DYN_MA fill:#9f9,stroke:#333
  style DYN_ST fill:#9f9,stroke:#333
  style NEU_CC fill:#9f9,stroke:#333
  style NEU_PH fill:#9f9,stroke:#333
  style NEU_JM fill:#9f9,stroke:#333
  style NEU_NH fill:#9f9,stroke:#333
  style IT_CC fill:#9f9,stroke:#333
  style IT_PH fill:#9f9,stroke:#333
  style IT_JM fill:#9f9,stroke:#333
```

## Legend

- **Green cells** (≥10): Deep coverage — multiple independent instantiations documented
- **All other cells** (4–9): Adequate coverage
- All 30 cells now ≥ 4 (no thin cells remain)

## Key Changes (Wave 10)

- **Wave 10a** (5 papers): Baudot TIDA, Ghorbanchian sync, Dey Conley-Morse, Petri scaffolds, Chaudhuri ring attractor
- **Wave 10b** (5 papers): Chung density-void, Dabaghian template, Donato phase transitions, Batko Conley sampled, Panaretos Wasserstein
- **Wave 10c** (5 papers): Lord scaffolds (neuro), Jost-Zhang Cheeger (TDA), Trinca n-D toric (QEC), Curry DMT (TDA), Méndez directed PH (TDA)
- 16 green cells (≥10) — up from 8 in Session 7
- Chain Complex now ≥10 in ALL 5 domains; Param Homology ≥10 in 4/5
- Stability taxonomy expanded to 7 flavors (added: dimensional)

## Coverage Status

All 30 cells ≥ 4. 16 cells ≥ 10. ~219 unique papers.
