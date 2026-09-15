# Make Operations Idempotent

An operation converges to the same end state whether it runs once, twice, or after a partial failure. Re-running is safe, not a second guess.

**Why:** A partial run that leaves a different state than a full run is a trap for the next run; idempotence is what makes recovery a rerun instead of a rescue.

**Pattern:** A setup step detects its own prior work and lands on the same result. Retry after a crash resumes instead of corrupting. Running the operation again changes nothing it should not.

**Steward:** Niko
**Source:** Adapted from pstack `principle-make-operations-idempotent` (MIT, Lauren Tan); translated for software work under the house canon.
