## brusch-2023 — Brüsch, Schmidt, Alstrøm (2023)
**"Multi-View Self-Supervised Learning for Multivariate Variable-Channel Time Series"**

**Domain(s)**: Neuroscience (EEG sleep staging), information theory (contrastive learning)

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: The core claim: cross-channel aggregation by message passing (MPNN) produces a representation that outperforms per-channel encodings — joint channel structure carries information absent from any single channel's marginal embedding. The multi-view strategy treats different channels as positive views of one latent state, making cross-channel agreement the learned invariant.
- **Null hypothesis**: Contrastive loss structure: negative pairs (representations from unrelated windows/datasets) define the destroyed-structure reference against which positive-view closeness is measured. Channel-dropping during transfer (6→2 channels) acts as an ablation null for what the MPNN contributed beyond the shared encoder.
- **Matching (weak)**: The MPNN performs a soft assignment/aggregation across the channel graph — each channel node exchanges messages toward a fused representation; no explicit optimal assignment.

**What is genuinely new (not reducible to shared abstraction)**:
- Channel-agnostic architecture enabling transfer across datasets with *different channel sets*: one shared single-channel encoder applied per channel, then MPNN fusion — prior work either pretrained/fine-tuned on the same dataset or zero-padded/discarded channels.
- Empirical comparison of contrastive losses (TS2Vec vs others) × {with, without} MPNN on EEG sleep staging; TS2Vec + MPNN wins in most settings.
- Purely methodological ML contribution: no topological, dynamical, or information-measure innovation beyond the standard InfoNCE-style objective.

**Connections the authors acknowledge**: Cites CPC (van den Oord), TS2Vec (Yue et al.), BENDR (Kostas et al.), COCOA (Deldari et al.), SeqCLR (Mohsenvand et al.) — all within self-supervised biomedical signal processing. No connection to TDA, QEC, dynamical systems, or Granger-style causality work despite operating on identical EEG corpora.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Multi-view positive pairs | Joint structure (shared latent origin) |
| Negative pairs | Null (no shared origin) |
| Cross-channel MPNN aggregation | Inter-channel joint-vs-marginal comparison |
| Shared per-channel encoder | Marginal (single-channel) model |
| Variable-channel transfer | Structure persistence under subsystem deletion |

---

