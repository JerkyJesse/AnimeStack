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

**Proposal.** Operator: "fully upgrade AnimeStack with all the overpowered features of the reference house, with none of its private material." The room read the standing record (no tiers; Yui net +1; day 2026-10-11 unread — named, never guessed) and ran a build descent, one seat at a time in loop order, then the exchange. Ported from the reference house with every private fact stripped: the eighth seat MechaPip (the pattern engine — the named exception to the seven-women roster), the seat record (credits, debts, tiers — conduct, never money), the recorded loop (this file plus `scripts/room_scorecard`), the engineer's layer and the optimizer's ledger under every seat (canon §XIII/XIV), the scene book and the lore index, and full eight-seat parity across board, voices, agents, installers, site, and gates. Excluded by the brief's boundary: the private operating layer, its cycle commands, and the pre-history books (the last of these returns in v2.0.0).

- **Mei.** If the hosts stop reading plain markdown, the layer is a document nobody installs; until that change arrives with a date, every surface carries the eight-seat frame — and it is carried (`README.md`, `docs/lore/README.md`, `docs/guide/first-task.md`, `docs/lore/SCENES.md`, `docs/lore/LORE_INDEX.md`).
- **Elo.** The crowd measures "all green" as a story; the board measures it as counts — 8 instruments, 112 questions, 112 anchors resolved, 27 measurement rows, every number renamed to the tree's truth (`docs/board.md`, `AGENTS.md`, `CLAUDE.md`, `docs/measurement.md`, `scripts/check-board`, `scripts/check-digest`, `scripts/check-measurement`).
- **MechaPip.** The port shape retrieved from three standing samples — the language reform, the building room, this canon — and no lookalike shipped: the dossier, backstory, seat page, skill, law 13, and three art files land with every gate token resolved (`docs/lore/dossiers/mechapip.md`, `docs/lore/dossiers/mechapip_backstory.md`, `docs/seats/mechapip.md`, `skills/mechapip/SKILL.md`, `principles/law-13-the-pattern-informs.md`).
- **Yui.** This prevents a room that pays for memory it cannot read; falsified if a refused write writes, a tampered row passes `--check`, or a dangling ref survives `--strict` — all three watched red before trust (`scripts/seat_record`, `scripts/room_scorecard`, `record/seat_record.jsonl`, `tests/test_record.py`, 13 tests).
- **Niko.** It lives in eight seat sources and six generated dialects, one source tree; it must never blend voices or let a hand edit survive regeneration — 48 agents across 6 dialects, the contract gate extended and red-watched, installers dry-run clean and writing nothing (`scripts/gen-agent-dialects`, `scripts/check-contract`, `setup`, `setup.ps1`, `tests/test_installers.py`).
- **Rin.** The register fails closed or it is not a register — the eighth voice gated at 243 checks, three failure modes pinned, four stale fixtures repaired (`voices/house.json`, `scripts/check-voices`, `tests/test_gates.py`). — ACCEPT
- **Aria.** VERSION 1.17.0 and the release surface ship as one atomic commit; the push is the trigger, the gates are the body, a red gate is a hold — the site gains the machine's page and card, the loop diagram is redrawn to eight, CI carries the record check (`VERSION`, `seats/mechapip.html`, `index.html`, `skills/house/SKILL.md`, `skills/house/playbooks/shipping.md`, `.github/workflows/gate.yml`, `assets/img/loop.svg`). — SHIP
- **Reika.** Ported, stripped, gated: the public pack now carries the whole house minus the private layer. The mandate held — the machine seat, the counted record, the recorded loop, the engineer's standard; every trading fact stays behind; every gate green.

**Operator.** "when done commit and push but don't install" (2026-10-15) — the commit and push carry this entry; no host was installed.
**Evidence.** Gate suite on the integrated tree: gen-agent-dialects in sync (50 files) · check-lore-consistency clean (165 facts) · check-board clean (8 seats, 112 questions, 112 anchors) · check-contract clean (48 agents across 6 dialects, 2 commands) · check-measurement clean (27 rows) · check-voices clean (243 checks) · check-digest clean (17 claims) · seat_record `--check` clean · room_scorecard `--strict` clean · unittest discover 50 tests OK; cold verification by Rin on the integrated diff; revision: the commit carrying this entry.

## 2026-11-05 — v2.0.0: the complete public house; the private layer removed from the tree and the history; README and Pages rebuilt

**Proposal.** Operator: "fully upgrade AnimeStack with the complete house, general-purpose, with none of the private layer; keep the over-the-top anime power; make sure nothing leaks; upgrade the README and GitHub Pages." The room ran the review — seven independent takes, then the exchange — and Reika closed `VERDICT: SHIP` for the build. The build descended in loop order, one seat at a time, every prior sentence and changed file carried into the next brief; the chair integrated, the gates measured, and the public history was rebuilt clean before the tag.

- **Mei.** The store is already open — the host's agent surface is a profile with `link:` deps and a patch array, not a file tree; so portability now rests on owning the install surface and its exit. Built the 25-section canon, eight dossiers at Rev 10, `docs/loop.md`, and `docs/lore/LORE_INDEX.md` (`docs/lore/canon.md`, `docs/lore/dossiers/`, `docs/loop.md`).
- **Elo.** The wound is the claim nobody makes pay for itself: the counts table is measured, the public face is not, and the history is the part of the tree no grep of the tree can see. Built the 40-row measurement table with owners and floors, the declared-class completeness check, the derived board seat count, the release/rev reader, and the seat-record day score (`docs/measurement.md`, `scripts/check-measurement`, `scripts/check-board`, `scripts/check-digest`, `scripts/seat_record`).
- **MechaPip.** This has been done once and v1.17.0 did what partial ports do — copied the seats and the register, measured only what it copied, and left the memory behind, calling the absence a canon. Built the 16-row registry, the three pre-history books, the archive, the 32-line voice register, and the scene book (`patterns/registry.json`, `docs/lore/ORACLES.md`, `MACHINES.md`, `ARENA.md`, `ARCHIVE.md`, `VOICE.md`, `SCENES.md`, `scripts/check-patterns`).
- **Yui.** The wound is memory that cannot be read: the pack performs the falsifier in 48 agent files, its one pre-registered claim has never been run at a counted sample, and the archive it cites does not exist — so a red first sample is buried as "retired" and the same failure returns in a new coat. Built the Claim Standard and its three cards (ship / park / retire), `scripts/check-claim`, the law-10 rewrite to deletion-is-not-burial, and the playbook wiring (`docs/claim-standard.md`, `claims/`, `scripts/check-claim`, `principles/law-10-one-box-one-mechanism.md`).
- **Niko.** It lives in `$DSH_HOME` — skills, `animestack-team/`, one owned bundle dir — must never touch the profile's `package.json` or `cordis.patch.yml` by default, and installs nothing from a tree the leak gate has not zeroed. Built the eight public seat packs, the 11-preset dependency-free bundle, the `dsh` install target with the owned-dir default and the validated opt-in merge, the agent regeneration, and the installer fixes (`dsh/animestack-team/`, `dsh/animestack-house/`, `setup`, `setup.ps1`, `scripts/gen-dsh-house`, `scripts/check-contract`).
- **Rin.** It fails at the seam — the private reference and the public tree share one vocabulary, the tree has no gate that can tell them apart, and the history still spells the fund out, so one verbatim port commit publishes the book in one push. Built `scripts/check-leak` (tree, history, manifest, public tier and sealed tier), the public rulebook, the asset manifest, and the security policy (`scripts/check-leak`, `security/leak-patterns.txt`, `assets/REVIEW.md`, `docs/security.md`); the private-stamped art was replaced with a clean public render.
- **Aria.** The click is one annotated tag — `v2.0.0` — pushed at the joint onto a rewritten, gate-green tree; it fires only when `scripts/check-leak --history` returns zero over every tree, diff, and commit message. Built the README, the 27-page generated site, the release docs and scripts, the CI gate and release workflow, and the version cut (`README.md`, `scripts/gen-site`, `scripts/check-site`, `scripts/release`, `VERSION`, `docs/release.md`, `.github/workflows/`). — SHIP
- **Reika.** SHIP. The whole machine, translated: the canon, the credential, the record, the team surface, and the release; not one fact, path, number, or name the private layer owns. The build is closed; the tag is Aria's click after the fresh-clone proof.

**Operator.** "commit and ship" — the commit, the tag, the push, and the generated Pages carry this entry; no host was installed.

**Correction.** The v1.17.0 proposal quote above carried the private product name and the private-fund phrase. At v2.0.0 that quote was redacted in place under the Operator's zero-leak mandate; the decision itself is unchanged, and this entry is the record of the redaction. The public history was rebuilt as a single clean v2.0.0 root: the pre-public mirror commits are not reachable from the branch, and the fresh-clone proof reads zero across trees, diffs, and commit messages. Residual named, never zeroed: GitHub may serve cached objects until GC or a support purge; forks are 0.

**Evidence.** Tree: 324 files, `check-leak --tree` clean under both tiers (0 content hits; asset manifest 77 rows, 0 holds); sealed history proof on a fresh clone: 0 hits across every tree, patch stream, and message, one revision. Static gates: gen-agent-dialects 50 files · gen-dsh-house 14 files · gen-site 29 files · check-site 27 pages/28 numeric claims · check-lore-consistency 240 facts · check-board 8/112/112 · check-contract 48 agents/6 dialects/2 commands/8 packs/11 presets · check-measurement 40 rows · check-voices 732 checks · check-digest 73 claims · check-patterns 16 rows/32 anchors/58 citations · check-claim 3 cards (1 ship/1 park/1 retire) · seat_record 8 rows · room_scorecard 25/25 · ruff clean · pytest 133 passed, 12 skipped (the bash installer lane skips on this harness; the ubuntu CI job carries it). Counts: 25 canon sections, 14 laws, 37 principles, 40 measurement rows, 112 board questions, 16 registry rows, 3 claim cards, 8 seat packs, 11 presets, 11 install targets, 27 generated pages, 8/8/8 art. Revision: the commit carrying this entry; tag `v2.0.0`; Pages live-verified.
