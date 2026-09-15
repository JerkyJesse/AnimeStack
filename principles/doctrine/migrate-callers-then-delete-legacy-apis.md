# Migrate Callers Then Delete Legacy APIs

Migrate every caller and delete the legacy path in the same wave. A compatibility layer is a second codebase kept alive because the first was not finished.

**Why:** A legacy API left standing after its callers move is a ghost that still gets maintained and still gets called by accident; deletion is the only migration that completes.

**Pattern:** The new API and the caller migration land together. The old path is removed in the same change, not deprecated for later. No bridge survives the wave.

**Steward:** Reika
**Source:** Adapted from pstack `principle-migrate-callers-then-delete-legacy-apis` (MIT, Lauren Tan); translated for software work under the house canon.
