## eLife.03476 — Dabaghian, Brandt & Frank (2014)
**"Reconceiving the hippocampal map as a topological template"**

**Domain(s)**: neuroscience

**Abstract machines instantiated**:
- **Chain complex**: Place cell activity is analyzed via the simplicial complex / nerve theorem framework established in Dabaghian et al. (2012). Place fields form a cover of the environment; co-firing defines simplices. The topological invariants of this complex (connectivity, loops = H_0, H_1) encode the environment's topology. The key experimental finding: these invariants are preserved when the track geometry changes but topology is held constant.
- **Stability**: Place fields preserve the relative sequence of places visited (topology) but do NOT vary with metrical features of the track or direction of movement. The topological representation is stable under geometric deformations — morphing the track (changing distances, angles, curvature) does not change the place cell representation. This is a strong stability result: the topological invariant (spatial ordering) survives arbitrary smooth deformations.
- **Null hypothesis**: The geometric hypothesis — that place cells encode distances and angles — is the null that is rejected. If place cells were geometric, their fields should change when the track is morphed. They don't. The place cell representation is topological (invariant under homeomorphism), not geometric (invariant only under isometry).

**What is genuinely new (not reducible to shared abstraction)**:
- The experimental dissociation of topology from geometry in place cell coding. Morphing linear tracks allowed independent manipulation of topology (connectivity of the path) and geometry (distances, curvatures), revealing that place cells track the former, not the latter.
- The reinterpretation of place cells: not "location-specifiers" but "topology-encoders." This challenges decades of place cell research that assumed geometric coding.
- Direction-independence: place fields do not vary with direction of movement on the track, further supporting a topological (not geometric) representation.
- Extends Dabaghian et al. 2012 (already in Rosetta) from computational model to experimental validation. The 2012 paper showed topology CAN be recovered from place cells; this 2014 paper shows topology IS what place cells encode.

**Connections the authors acknowledge**: Cite Dabaghian et al. 2012 (their own computational model), O'Keefe & Dostrovsky (1971) for place cells. Do NOT cite TDA formalism directly (though the underlying framework is PH via nerve complexes). Entirely within systems/computational neuroscience.

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| Place field | Cover element (nerve complex vertex) |
| Co-firing | Simplex (nerve construction) |
| Topological template | Chain complex invariant of the environment |
| Track morphing | Geometric perturbation (homeomorphism) |
| Preserved sequence | Topological invariant (stable under deformation) |
| Direction-independence | Additional stability (invariant under orientation reversal) |
| Geometric coding (rejected) | Null hypothesis (metric structure without topological content) |

**See also**: `by-domain/neuroscience.md`, `by-structure/boundary_operators.md`, `by-structure/phase_transitions.md`
