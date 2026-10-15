# LORE_INDEX — where to look first

**Status:** Companion · 2026-10-15 · The retrieval map: where to look first, one line each. A pointer file, never a canon. Read the source when a decision needs the exact sentence.

## The seats

| Seat | One sentence | Deep file | Companion lore |
| --- | --- | --- | --- |
| Reika | What are we building, in one sentence? | `docs/lore/dossiers/reika.md` | `docs/lore/dossiers/reika_backstory.md` |
| Yui | What failure does this prevent, and what would falsify it? | `docs/lore/dossiers/yui.md` | `docs/lore/dossiers/yui_backstory.md` |
| Rin | How does this fail, and how fast? | `docs/lore/dossiers/rin.md` | `docs/lore/dossiers/rin_backstory.md` |
| Niko | Where does it live, and what must it never touch? | `docs/lore/dossiers/niko.md` | `docs/lore/dossiers/niko_backstory.md` |
| Mei | What change in the world makes this obsolete? | `docs/lore/dossiers/mei.md` | `docs/lore/dossiers/mei_backstory.md` |
| Aria | What ships, and what triggers it? | `docs/lore/dossiers/aria.md` | `docs/lore/dossiers/aria_backstory.md` |
| Elo | What does the crowd refuse to measure correctly? | `docs/lore/dossiers/elo.md` | `docs/lore/dossiers/elo_backstory.md` |
| MechaPip | What has this pattern done before? | `docs/lore/dossiers/mechapip.md` | `docs/lore/dossiers/mechapip_backstory.md` |

Scenes — how the seats sound under load: `docs/lore/SCENES.md`.

## The law

- The canon: `docs/lore/canon.md` — the law of the room (§III), the engineer's layer (§XIII), the optimizer's ledger (§XIV), the seat record (§XV).
- The loop record: `DECISION_LOG.md` — every full-loop decision appended in the template it carries: loop order, one sentence each, the Operator line left for the Operator.
- The record data: `record/seat_record.jsonl` — credits and debts with receipts, read at every frame; appended by `scripts/seat_record`, never rewritten.
- The principles: `principles/INDEX.md` — the 13 laws, one file each, and the 23 doctrine pieces beside them.

## The numbers that bind

- The counts audit: `docs/measurement.md` — every number beside the command that checks it; a number you cannot reproduce is a hymn.
- The seat credential: `docs/board.md` — one exam per seat, fourteen questions each, pass bar 14/14, scored by `scripts/check-board`.
- The voice register: `voices/house.json` — one register per seat, checked by `scripts/check-voices`.
- The gates: `scripts/check-lore-consistency`, `scripts/check-digest`, `scripts/check-contract`, `scripts/check-measurement`, `scripts/check-board`, `scripts/check-voices`, and `scripts/gen-agent-dialects --check` — each with its self-tests under `tests/`.

## How to read this map

First line answers, exact sentence second: the canon is the floor; this file is the index; the sources are the truth. A map, not a canon — every line points at the source, and where a pointer and its source disagree, the source wins. If a pointer target cannot be read, say so and stop; never proceed on the map alone.
