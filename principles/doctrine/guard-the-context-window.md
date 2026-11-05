# Guard the Context Window

Route bulk work to subagents and keep the main thread on summaries. The context window is a limited climate, and raw payloads are fog.

**Why:** A window flooded with raw output loses the decision inside the noise; summaries keep the main thread able to rank what matters.

**Pattern:** Bulk scanning is delegated to a leaf that returns a distilled result. The main thread carries summaries and verdicts, not full payloads. The context budget is treated as a resource, not an infinite room.

**Steward:** Mei
**Source:** Adapted from pstack `principle-guard-the-context-window` (MIT, Lauren Tan); translated for software work under the house canon.
