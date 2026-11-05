# Separate Before Serializing Shared State

Eliminate the sharing first; serialize only when a single shared writer is a genuine invariant. A lock is a bandage over a structure that should have been divided.

**Why:** Serializing shared state keeps the sharing alive and pays for it on every access; removing the sharing is the fix, the lock is the tax.

**Pattern:** Two components with shared mutable state are split to own their own state. A lock is added only when one writer across threads is truly required. The default answer to contention is separation, not synchronization.

**Steward:** Niko
**Source:** Adapted from pstack `principle-separate-before-serializing-shared-state` (MIT, Lauren Tan); translated for software work under the house canon.
