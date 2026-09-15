# Minimize Reader Load

Count the layers a reader must cross from question to answer. Collapse wrappers with a single caller and shrink the mutable scope so the path is short enough to hold in one head.

**Why:** Every hop between a question and its answer is a place the reader loses the thread; load is a cost paid by every future reader, forever.

**Pattern:** A one-caller wrapper is inlined rather than kept. Mutable state is scoped to the smallest block that needs it. A reader can follow the call from entry to result without a map.

**Steward:** Rin
**Source:** Adapted from pstack `principle-minimize-reader-load` (MIT, Lauren Tan); translated for software work under the house canon.
