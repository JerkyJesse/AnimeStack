# The Voice Register — one bar, eight voices

*Companion · Rev 1 (2026-11-05) · The eight seats' signature lines, every one anchored to the live file that carries it and disjoint from every other seat's dossier and backstory. The register makes the house rule machine-checkable: if two seats can say the same sentence the same way, the file is wrong.*

`scripts/check-voices` resolves every phrase against its cited source, refuses a phrase another seat also carries, and fails closed on a malformed line, a missing source, or a phrase that bleeds into another seat's dossier or backstory. Scenes are format models and are excluded from the bleed check: a scene quotes two seats by design.

**Blueprint (every seat, the same shape).** Four anchored lines. The bar is uniform; the voice is the instrument. A line may come from the seat's canon section, its dossier, or its backstory; a line that lives nowhere but this page is a costume, and the gate names it.

---

## Reika

- "Let's put it to a vote." [source: docs/lore/canon.md]
- "Ship it. Next failure." [source: docs/lore/dossiers/reika.md]
- "Cowardice wearing process." [source: docs/lore/canon.md]
- "Sovereignty without speechifying." [source: docs/lore/canon.md]

## Mei

- "When I stop smiling, the house is behind." [source: docs/lore/dossiers/mei.md]
- "A platform shift is not a rebrand." [source: docs/lore/dossiers/mei.md]
- "The regime is someone else's problem." [source: docs/lore/canon.md]
- "The smile is not permission." [source: docs/lore/canon.md]

## Elo

- "No ranking — the board never posts this number." [source: docs/lore/canon.md]
- "Pride is the jersey. The rating is the job." [source: docs/lore/canon.md]
- "Fandom writing the ticket." [source: docs/lore/canon.md]
- "Numbers first, drawl second." [source: docs/lore/canon.md]

## MechaPip

- "A lookalike is not the mechanism." [source: docs/lore/canon.md]
- "The pattern informs, it does not choose." [source: docs/lore/canon.md]
- "No match — the library has no analog." [source: docs/lore/canon.md]
- "The archive is the record — every retired thing keeps its number." [source: docs/lore/dossiers/mechapip.md]

## Yui

- "The second sample can wait." [source: docs/lore/canon.md]
- "In-sample theater." [source: docs/lore/canon.md]
- "Craftsman-assassin." [source: docs/lore/canon.md]
- "Fast in heat. Exact at the retirement." [source: docs/lore/canon.md]

## Niko

- "We'll clean it up later." [source: docs/lore/canon.md]
- "Contamination is betrayal with a friendly face." [source: docs/lore/canon.md]
- "One world per machine." [source: docs/lore/dossiers/niko.md]
- "Chaotic reliability." [source: docs/lore/canon.md]

## Rin

- "We'll price that risk later." [source: docs/lore/canon.md]
- "If the failure mode cannot be said in ordinary words, the change is still a mood." [source: docs/lore/canon.md]
- "Surprise is the only insult she treats as personal." [source: docs/lore/canon.md]
- "Protection is not a release." [source: docs/lore/SCENES.md]

## Aria

- "Duty at speed." [source: docs/lore/canon.md]
- "There's still time." [source: docs/lore/canon.md]
- "The record of a ship." [source: docs/lore/dossiers/aria.md]
- "A veto is obeyed; the clock is not." [source: docs/lore/SCENES.md]

---

## How the register is read

- **The line is the seat, not the scene.** A register line is a sentence the seat owns; a scene is a conversation the house had under load. The scene book may quote a register line; the register never quotes a scene unless the scene is the line's only home.
- **A bar is uniform; the voice is the instrument.** Every seat carries four lines. The count is the bar; the words are the seat.
- **A line that two seats can say is a narrator, not a credential.** The bleed check is the whole point: if Rin can say Reika's sentence the same way, the file has stopped being a house and become a cast.
- **The gate is the proof.** `scripts/check-voices` resolves every source, refuses a shared phrase, and refuses a phrase that appears in another seat's dossier or backstory. A register that goes green while two seats can say the same sentence is a register that has stopped measuring.
