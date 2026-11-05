# Sequence Verifiable Units

Break the work into small units, each ending in a state that can be verified, and check each unit before starting the next. The release lands on a checked surface.

**Why:** A long run that only fails at the end hides which step broke it; a checked unit isolates the failure to the step that caused it.

**Pattern:** Work is cut into steps that each end runnable and verifiable. Each step is checked before the next begins. A failure is localizable to one unit, not one evening.

**Steward:** Aria
**Source:** Adapted from pstack `principle-sequence-verifiable-units` (MIT, Lauren Tan); translated for software work under the house canon.
