# Type System Discipline

Make illegal states impossible to represent. Parse external data into honest types at the boundary, and never lie to the compiler to make a case disappear.

**Why:** A state the type system forbids is a crash that cannot be written; a lie to the compiler is a state the type system was told not to see, and it fires later.

**Pattern:** An invalid combination is not representable in the type, not merely checked at runtime. External payloads are parsed, not cast. Suppressions carry a reason or do not exist.

**Steward:** Niko
**Source:** Adapted from pstack `principle-type-system-discipline` (MIT, Lauren Tan); translated for software work under the house canon.
