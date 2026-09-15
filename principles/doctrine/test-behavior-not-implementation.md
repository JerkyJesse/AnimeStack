# Test Behavior, Not Implementation

Call the code the way a user reaches it, and assert on the observable result. If a test still passes with every import undefined, it proves nothing — rewrite it or delete it.

**Why:** A test wired to internals survives a refactor that broke the behavior, and a test with no imports is a ceremony, not a check.

**Pattern:** Tests invoke the public surface and assert observable outcomes. A test that passes with its imports undefined is rewritten or removed. The test fails when the behavior fails, not when the internals move.

**Steward:** Elo
**Source:** Adapted from pstack `principle-test-behavior-not-implementation` (MIT, Lauren Tan); translated for software work under the house canon.
