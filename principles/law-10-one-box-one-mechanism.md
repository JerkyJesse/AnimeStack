# Law 10 — One Box, One Mechanism

**One box, one mechanism.** A twin that loses to a sibling is buried, not renamed.

**Translated.** One concern per module: a unit of code does one thing, and a second implementation of the same thing that loses to the first is deleted, not kept under a new name.

**Why.** Two mechanisms in one cell produce noise and confusion about which one earned the result; a loser kept under a new name is a cull avoided, and the debt collects.

**Pattern.**
- Two modules solve the same problem and both ship because deleting one felt wasteful.
- A failed approach is renamed and kept instead of buried with a record.
- A module grows a second unrelated responsibility rather than splitting.

**Steward.** Niko.
**Source.** `docs/lore/canon.md` §III law 10.
