# Subtract Before You Add

Remove the dead weight first — dead code, redundant validators, stub references — before adding anything new. Subtraction clears the ground the addition will stand on.

**Why:** Adding onto unremoved weight buries the new logic in noise; the reader cannot tell what is live from what is left over.

**Pattern:** A feature lands only after its predecessor's dead branches are gone. Redundant checks are deleted rather than extended. The diff is net-negative when it can be.

**Steward:** Reika
**Source:** Adapted from pstack `principle-subtract-before-you-add` (MIT, Lauren Tan); translated for software work under the house canon.
