# Model the Domain

Encode the domain in a structure — types, tables, states — instead of scattering the same decision through scattered conditionals. The structure is the documentation that cannot drift.

**Why:** A rule expressed in one place is checked once; the same rule repeated in ten conditionals is ten chances to fall out of sync.

**Pattern:** A state machine replaces a chain of if-else branches. A lookup table replaces repeated mappings. The domain's truth lives in one structure the code reads.

**Steward:** Niko
**Source:** Adapted from pstack `principle-model-the-domain` (MIT, Lauren Tan); translated for software work under the house canon.
