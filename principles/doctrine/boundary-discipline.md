# Boundary Discipline

Put the guards at the system boundaries and trust the internal types. Keep business logic in pure functions so the edges are the only places the world can get in.

**Why:** When every layer re-validates, the checks contradict each other and the real guard drowns in noise; one defended boundary is a floor, many scattered ones are a rumor.

**Pattern:** External input is validated once at entry, then trusted internally. Business rules sit in pure functions, not in I/O glue. The boundary is named and single.

**Steward:** Rin
**Source:** Adapted from pstack `principle-boundary-discipline` (MIT, Lauren Tan); translated for software work under the house canon.
