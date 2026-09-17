# Outcome-Oriented Execution

Converge on the target. Do not spend code preserving smooth intermediate states with throwaway compatibility shims that the destination will discard.

**Why:** Scaffolding kept alive past its purpose is a second codebase pretending to be progress; the target, not the journey's staging, is the artifact.

**Pattern:** A migration moves directly to the new shape rather than running both shapes through a bridge. Intermediate helpers fail in the same change that reaches the outcome. The end state is the only state kept.

**Steward:** Reika
**Source:** Adapted from pstack `principle-outcome-oriented-execution` (MIT, Lauren Tan); translated for software work under the house canon.
