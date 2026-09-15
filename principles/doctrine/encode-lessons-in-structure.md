# Encode Lessons in Structure

Encode each lesson as a lint, a flag, a runtime check, or a script instead of another paragraph. Prose is read once; a check runs every time.

**Why:** A lesson written down is honored only when someone remembers to read it; a check fires on every future run and cannot be skipped by attention.

**Pattern:** A bug class is closed with a lint or a test, not a note in a doc. An invariant is enforced by a check, not a comment. The guard lives in the machine, where the failure lived.

**Steward:** Rin
**Source:** Adapted from pstack `principle-encode-lessons-in-structure` (MIT, Lauren Tan); translated for software work under the house canon.
