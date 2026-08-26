## PRL 85:461 --- Schreiber (2000)
**"Measuring information transfer"**

**Domain(s)**: Information theory, dynamical systems

**Abstract machines instantiated**:
- **Joint-vs-marginal excess**: Transfer entropy T_{Y→X} = H(X_{t+1} | X_t^(k)) - H(X_{t+1} | X_t^(k), Y_t^(l)). This IS conditional mutual information: how much does the joint history (X,Y) improve prediction of X's future beyond the marginal history (X alone)? The excess quantifies directed information flow from Y to X.
- **Null hypothesis**: Shuffled surrogates destroy the temporal coupling between X and Y while preserving marginal statistics. TE under the null should be zero (up to finite-sample bias). Significance = observed TE exceeds null distribution.
- **Parameterized homology** (weak): The embedding dimensions k, l and prediction horizon parameterize the TE estimate. Different parameter choices reveal different timescales of information transfer.

**What is genuinely new (not reducible to shared abstraction)**:
- Asymmetry: unlike MI, TE is inherently directional. T_{Y→X} ≠ T_{X→Y} in general. This distinguishes it from symmetric measures and connects to causality.
- Non-parametric: unlike Granger causality, TE makes no model assumptions (linear, Gaussian). It measures information transfer in arbitrary nonlinear systems.
- The connection to dynamical systems: TE is defined on state-space reconstructions, linking naturally to Takens embedding and attractor geometry.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Transfer entropy | Directed joint-vs-marginal excess |
| Conditional MI | Excess prediction from joint history |
| Shuffled surrogate | Null model (destroys temporal coupling) |
| Embedding dimension k, l | Parameterization of estimator |
| Information flow direction | Asymmetry of joint-vs-marginal |
