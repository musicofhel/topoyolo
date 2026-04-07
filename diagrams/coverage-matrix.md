# Coverage Matrix — 6 Machines × 5 Domains

Updated: 2026-04-07 (Session 5)

## Paper Counts

```
              Chain    Param   Match   Stabil  Joint   Null
              Complex  Homol           ity     v Marg  Hyp
─────────────────────────────────────────────────────────────
TDA            6+       7+     ~3      7+      5+      4+
QEC           15+       8+      8+    10+      6+      9+
Dynamics       8+      11+     10+     8+      6+      7+
Neuro          6+      10+      8+     7+     13+     10+
InfoTheo       9+       9+     ~3      6+     12+      8+
```

## Mermaid Heatmap

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px'}}}%%
block-beta
  columns 7

  space:1 CC["Chain\nComplex"] PH["Param\nHomology"] MA["Matching"] ST["Stability"] JM["Joint vs\nMarginal"] NH["Null\nHypothesis"]

  TDA["TDA"] TDA_CC["6+"] TDA_PH["7+"] TDA_MA["~3"] TDA_ST["7+"] TDA_JM["5+"] TDA_NH["4+"]
  QEC["QEC"] QEC_CC["15+"] QEC_PH["8+"] QEC_MA["8+"] QEC_ST["10+"] QEC_JM["6+"] QEC_NH["9+"]
  DYN["Dynamics"] DYN_CC["8+"] DYN_PH["11+"] DYN_MA["10+"] DYN_ST["8+"] DYN_JM["6+"] DYN_NH["7+"]
  NEU["Neuro"] NEU_CC["6+"] NEU_PH["10+"] NEU_MA["8+"] NEU_ST["7+"] NEU_JM["13+"] NEU_NH["10+"]
  IT["InfoTheo"] IT_CC["9+"] IT_PH["9+"] IT_MA["~3"] IT_ST["6+"] IT_JM["12+"] IT_NH["8+"]

  style TDA_MA fill:#ff9,stroke:#333
  style IT_MA fill:#ff9,stroke:#333
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
- **Yellow cells** (~3): Thin coverage — genuine papers exist but cell is inherently sparse
- **All other cells** (4–9): Adequate coverage

## Key Changes (Session 5)

- **Joint×TDA**: ~2 → **5+** (added Varley 2025, Hamilton & Leditzky 2024, Natarajan 2026)
- **Joint×QEC**: 5+ → **6+** (Hamilton & Leditzky cross-listed)
- **Joint×InfoTheo**: 12+ → **12+** (Rosas 2020 added, count already high)

## Remaining Thin Cells

- **Match×TDA (~3)**: Di Rocco, Divol-Lacombe, Adams. Matching is inherently less prevalent in TDA.
- **Match×InfoTheo (~3)**: Mézard-Mora, Wong-Yang, Kolchinsky. Matching is not a natural info-theory operation.

These cells may not need more papers — the thinness reflects genuine domain structure rather than search gaps.
