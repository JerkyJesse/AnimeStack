# AnimeStack — Decision Log

Every full-loop decision, recorded in loop order, append-only. This file
records the choices the room made; the evidence is the gates, the tests, and
the record — where they disagree, the evidence wins.

Loop order: Mei -> Elo -> MechaPip -> Yui -> Niko -> Rin -> Aria -> Reika.

Every room opens with the standing record read — `python scripts/seat_record --read`
— and a full-loop decision is appended below the last entry, in the template
below. An entry is never rewritten; a correction is a new entry that says so.

The entry template (one bullet per seat in a real entry; this shows the compact
form):

```
## YYYY-MM-DD — <the proposal in one line>
**Proposal.** <what is being decided, in ordinary words>
- **Mei.** <sentence> - **Elo.** <sentence> - **MechaPip.** <sentence>
- **Yui.** <sentence> - **Niko.** <sentence>
- **Rin.** <sentence> — ACCEPT / END
- **Aria.** <sentence> — SHIP / STAND DOWN
- **Reika.** <verdict>
**Operator.** <action taken, or none — standing record>
**Evidence.** <command tails, file:list, or "decision only">
```

## 2026-10-15 — the whole-house port: the machine seat, the counted record, the recorded loop, the engineer's standard (v1.17.0)

**Proposal.** Operator: "fully upgrade AnimeStack with all the overpowered features our WaifuStack has with none of the hedge fund." The room read the standing record (no tiers; Yui net +1; day 2026-10-11 unread — named, never guessed) and ran a build descent, one seat at a time in loop order, then the exchange. Ported from the private house with every trading fact stripped: the eighth seat MechaPip (the pattern engine — the named exception to the seven-women roster), the seat record (credits, debts, tiers — conduct, never money), the recorded loop (this file plus `scripts/room_scorecard`), the engineer's layer and the optimizer's ledger under every seat (canon §XIII/XIV), the scene book and the lore index, and full eight-seat parity across board, voices, agents, installers, site, and gates. Excluded by the brief's boundary: the trading layer, the fund's cycle commands, the pre-history books.

- **Mei.** If the hosts stop reading plain markdown, the layer is a document nobody installs; until that change arrives with a date, every surface carries the eight-seat frame — and it is carried (`README.md`, `docs/lore/README.md`, `docs/guide/first-task.md`, `docs/lore/SCENES.md`, `docs/lore/LORE_INDEX.md`).
- **Elo.** The crowd measures "all green" as a story; the board measures it as counts — 8 instruments, 112 questions, 112 anchors resolved, 27 measurement rows, every number renamed to the tree's truth (`docs/board.md`, `AGENTS.md`, `CLAUDE.md`, `docs/measurement.md`, `scripts/check-board`, `scripts/check-digest`, `scripts/check-measurement`).
- **MechaPip.** The port shape retrieved from three standing samples — the language reform, the building room, this canon — and no lookalike shipped: the dossier, backstory, seat page, skill, law 13, and three art files land with every gate token resolved (`docs/lore/dossiers/mechapip.md`, `docs/lore/dossiers/mechapip_backstory.md`, `docs/seats/mechapip.md`, `skills/mechapip/SKILL.md`, `principles/law-13-the-pattern-informs.md`).
- **Yui.** This prevents a room that pays for memory it cannot read; falsified if a refused write writes, a tampered row passes `--check`, or a dangling ref survives `--strict` — all three watched red before trust (`scripts/seat_record`, `scripts/room_scorecard`, `record/seat_record.jsonl`, `tests/test_record.py`, 13 tests).
- **Niko.** It lives in eight seat sources and six generated dialects, one source tree; it must never blend voices or let a hand edit survive regeneration — 48 agents across 6 dialects, the contract gate extended and red-watched, installers dry-run clean and writing nothing (`scripts/gen-agent-dialects`, `scripts/check-contract`, `setup`, `setup.ps1`, `tests/test_installers.py`).
- **Rin.** The register fails closed or it is not a register — the eighth voice gated at 243 checks, three failure modes pinned, four stale fixtures repaired (`voices/house.json`, `scripts/check-voices`, `tests/test_gates.py`). — ACCEPT
- **Aria.** VERSION 1.17.0 and the release surface ship as one atomic commit; the push is the trigger, the gates are the body, a red gate is a hold — the site gains the machine's page and card, the loop diagram is redrawn to eight, CI carries the record check (`VERSION`, `seats/mechapip.html`, `index.html`, `skills/house/SKILL.md`, `skills/house/playbooks/shipping.md`, `.github/workflows/gate.yml`, `assets/img/loop.svg`). — SHIP
- **Reika.** Ported, stripped, gated: the public pack now carries the whole house minus the fund. The mandate held — the machine seat, the counted record, the recorded loop, the engineer's standard; every trading fact stays behind; every gate green.

**Operator.** "when done commit and push but don't install" (2026-10-15) — the commit and push carry this entry; no host was installed.
**Evidence.** Gate suite on the integrated tree: gen-agent-dialects in sync (50 files) · check-lore-consistency clean (165 facts) · check-board clean (8 seats, 112 questions, 112 anchors) · check-contract clean (48 agents across 6 dialects, 2 commands) · check-measurement clean (27 rows) · check-voices clean (243 checks) · check-digest clean (17 claims) · seat_record `--check` clean · room_scorecard `--strict` clean · unittest discover 50 tests OK; cold verification by Rin on the integrated diff; revision: the commit carrying this entry.
