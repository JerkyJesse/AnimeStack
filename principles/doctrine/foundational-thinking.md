# Foundational Thinking

Choose the core types and data structures before writing any logic. When the structures are right, the downstream code becomes obvious instead of fought for.

**Why:** Logic built on a misshapen foundation fights itself at every call site; getting the structure right once makes a hundred decisions free.

**Pattern:** Model the core record first, then write functions against it. Refuse a patch that papers over a wrong-shaped type. Name the structure before naming the behavior.

**Steward:** Niko
**Source:** Adapted from pstack `principle-foundational-thinking` (MIT, Lauren Tan); translated for software work under the house canon.
