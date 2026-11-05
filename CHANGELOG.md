# Changelog

Every release is a recorded decision; the evidence is the gate suite, the
counts table, and the tag. A number here is true at the tag or it is a defect.

## v2.0.0 — 2026-11-05 — the complete public house

The whole house, translated: every instrument the private reference could stand
without a fund, and not one fact the fund owns. The tree and the history are
clean; the site is generated; the release is a tag on a gate-green tree.

### Added

- **The 25-section canon** (`docs/lore/canon.md`): the law of the room, the
  seven and the machine, how Elo sits, the design loop, the compounding spine,
  the work surfaces, the rites, the eras, the archive, the vocabulary, the two
  nights, the seat lanes, the evidence ladder, the subagent room, the claim
  standard, the engineer's layer, the optimizer's ledger, and the seat record.
- **The pre-history books**: `docs/lore/ORACLES.md`, `MACHINES.md`, `ARENA.md`.
- **The archive and the park law** (`docs/lore/ARCHIVE.md`) and the
  machine-readable registry (`patterns/registry.json`, 16 entries), checked by
  `scripts/check-patterns`.
- **The voice register** (`docs/lore/VOICE.md`) and the widened voice gate
  (`scripts/check-voices`, four anchored lines per seat, no bleed).
- **The claim standard** (`docs/claim-standard.md`), three claim cards
  (`claims/`), and `scripts/check-claim`.
- **The seat record's day score and tiers**: green day and red book kinds in
  `scripts/seat_record`, the streak line in `--read`, and the tier path in the
  canon.
- **The DSH team surface** (`dsh/`): eight seat packs, eleven Agent presets,
  two operator commands, the owned-dir install, and the opt-in profile merge —
  the eleventh install target.
- **The generated GitHub Pages site** (`scripts/gen-site`, `scripts/check-site`):
  27 pages rendered from the sources, with metadata, navigation, sitemaps, and
  a numeric-claim gate.
- **The zero-leak gate** (`scripts/check-leak`, `security/leak-patterns.txt`,
  `docs/security.md`) with the public pattern tier and the sealed tier.
- **The asset review manifest** (`assets/REVIEW.md`) and the human review rule.
- **The release surface**: `VERSION` 2.0.0, this changelog, `docs/release.md`,
  `scripts/release`, and the tag-triggered release verification workflow.

### Changed

- The measurement lane is 40 rows, each with an owner and a computer; the
  completeness assertion fails on an undeclared artifact class.
- The board's seat count is derived from the board itself; the digest reader
  now reads the release and canon revision off every rendered surface.
- The laws are 14 (law 14: the evidence record decides); the principles index is
  14 laws plus 23 doctrine pieces.
- The installer ships 11 install targets: ten coding hosts plus the DSH surface.
- The agent trees are 48 files across six dialects; the DSH surface is 8 seat
  packs and 11 presets.
- The site is generated, never hand-authored; the old hand-built pages and their
  stale counts are gone.

### Removed

- Every channel line, channel variable, and private-reference residue from the
  dossiers, seat pages, canon, and operator page.
- The two burned-in art renders on hold (a dossier card and a wallpaper), with
  their thumbnails; the withheld set is named in `art/README.md`.
- The stale hand-authored site claims (a twelve-law page against fourteen, a
  seven-seat line, mismatched canon revisions).

### Security

- The tree is clean under `scripts/check-leak --tree`.
- The history is rebuilt clean; the release gate is
  `python scripts/check-leak --sealed-required --history`.
- The site and every generated page are scanned by `scripts/check-site` with
  the public pattern tier.
- No credential, key, token, or machine path is committed.

### Evidence

- `python scripts/check-measurement --check-doc`
- `python scripts/check-lore-consistency`
- `python scripts/check-board`
- `python scripts/check-contract`
- `python scripts/check-voices`
- `python scripts/check-patterns`
- `python scripts/check-claim --check`
- `python scripts/check-digest`
- `python scripts/check-leak --tree`
- `python scripts/gen-site --check`
- `python scripts/check-site`
- `python scripts/gen-agent-dialects --check`
- `python scripts/gen-dsh-house --check`
- `python scripts/seat_record --check`
- `python scripts/room_scorecard --strict`
- `python -m pytest -q`

## v1.17.0 — 2026-10-15 — the whole-house port

The eighth seat MechaPip, the recorded loop, the seat record, and the engineer's
and optimizer's layers; eight seats across board, voices, agents, installers,
and site. Every trading fact stripped.

## v1.16.0 — per-host installer round-trip tests

All ten hosts tested; coexistence guards added.

## v1.15.0 — the invention line and cold verification

The invention surface and the cold verification pass in all 42 seat files; the
contract, lore, and measurement gates extended.

## v1.14.0 — the building room

The build descent relay and the working exchange.

## v1.13.0 — gate self-tests

Gate self-tests, voice and digest checks, `--root` hooks; CI runs the suite.

## v1.12.0 — opencode provenance

Provenance stamps on the hand-authored opencode tree; `--check` verifies.

## v1.11.0 — the board and the contract gate

The House Board, the contract gate, the counts gate, and setup dry runs.

## v1.10.0 — the collaborative room

The selected seat leads; two rounds (takes, exchange); visible seat names.

## v1.9.0 — one file per seat, every dialect

The one-file room everywhere; roles picked from the brief.

## v1.8.0 — the opencode room

One-file opencode agents; leaf role picked from the brief.

## v1.7.0 — art and graphics credentials

The art and graphics credentials for the eight seats.

## v1.6.0 — six dialect coverage

Six host dialects, eight agents each.

## v1.5.0 — credentials

The seat credentials.

## v1.4.0 — the language reform

The house voice, rewritten.

## v1.3.0 — the software house

The software-native lore rewrite and the site rebuild.

## v1.2.0 — the seat pages

The site and the seat pages.

## v1.1.0 — the House Board and the lore mirror

The board, the seat credentials, and the agent protocol sync.

## v1.0.0 — the seven-seat house

The house as a portable skill pack.
