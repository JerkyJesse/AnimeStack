# LORE_INDEX — where to look first

**Status:** Companion · v2.0.0 · The retrieval map: where to look first, one line each. A pointer file, never a canon. Read the source when a decision needs the exact sentence.

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

Scenes — how the seats sound under load: [SCENES.md](SCENES.md).

## The law

- The canon: [canon.md](canon.md) — twenty-five sections: the law of the room
  (III), how the measurement seat sits among the eight (V), the compounding
  spine (X), the operator (XII), the work surfaces (XIII), the rites (XIV), the
  eras (XV), the archive (XVI), the two nights (XVIII), the seat lanes (XIX),
  the evidence ladder (XX), the subagent room (XXI), the claim standard (XXII),
  the engineer's layer (XXIII), the optimizer's ledger (XXIV), and the seat
  record (XXV).
- The loop record: [DECISION_LOG.md](../DECISION_LOG.md) — every full-loop
  decision appended in the template it carries: loop order, one sentence each,
  the Operator line left for the Operator.
- The record data: `record/seat_record.jsonl` — credits and debts with receipts,
  read at every frame; appended by `scripts/seat_record`, never rewritten.
- The principles: [principle index](../principles/INDEX.md) — the fourteen laws,
  one file each, and the doctrine pieces beside them.

## The instruments beside the canon

| Instrument | Answers | File |
| --- | --- | --- |
| The pre-history — the first question | why an answer that cannot close cannot pay | `docs/lore/ORACLES.md` |
| The pre-history — the speed religion | why speed is rented and the cage is owned | `docs/lore/MACHINES.md` |
| The pre-history — the leaderboard and the ladder | why a leaderboard rewards variance and the record keeps survivors | `docs/lore/ARENA.md` |
| The archive | what a counted sample refused, and other people's failures | `docs/lore/ARCHIVE.md` |
| The voice register | four anchored lines per seat, disjoint by design | `docs/lore/VOICE.md` |
| The pattern registry | the machine-readable pattern archive, checked by `scripts/check-patterns` | `patterns/registry.json` |
| The claim standard | the claim card, the control, both halves, the falsifier, the receipt, the park | [docs/claim-standard.md](../claim-standard.md) |
| The board | the seat credential: one exam per seat, pass bar 14/14 | `docs/board.md` |
| The counts | every number beside the command that checks it | `docs/measurement.md` |
| The gates | the suite that proves the tree, with its self-tests under `tests/` | `scripts/check-board`, `scripts/check-contract`, `scripts/check-digest`, `scripts/check-lore-consistency`, `scripts/check-measurement`, `scripts/check-patterns`, `scripts/check-voices`, `scripts/gen-agent-dialects --check`, and `scripts/check-leak` (pending — Rin's lane) |
| The team surface | the room in a host that runs the seats as durable teammates | [the DSH surface](../../dsh/README.md) |

## How to read this map

First line answers, exact sentence second: the canon is the floor; this file is
the index; the sources are the truth. A map, not a canon — every line points at
the source, and where a pointer and its source disagree, the source wins. If a
pointer target cannot be read, say so and stop; never proceed on the map alone.
