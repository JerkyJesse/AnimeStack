# Fix Root Causes

Reproduce the failure first, then ask why until the root is reached. Resist guards that merely silence the crash and leave the cause alive to fire again.

**Why:** A crash silenced is a cause preserved; the symptom goes quiet and the defect keeps its seat, waiting for a worse window.

**Pattern:** A bug is reproduced before it is patched. The fix lands at the cause, not at a nil-check that swallows it. The why-chain ends at a named root, not at a symptom dressed as a fix.

**Steward:** Yui
**Source:** Adapted from pstack `principle-fix-root-causes` (MIT, Lauren Tan); translated for software work under the house canon.
