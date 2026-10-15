# Shipping

## When

- "ship it"
- "open the PR and merge"
- a feature or fix is green and the room has not yet reviewed it for contact

## The loop

Lead: Aria.

- **Rin** — How does this fail, and how fast? REVIEW the diff first: failure modes in ordinary words, the bugs CI misses, the trust boundaries. No ship without an ACCEPT. Produces ACCEPT or END.
- **Aria** — What ships, and what triggers it? SHIP: run the land chain below — sweep, cold verification, one atomic commit, push. Produces the release, SHIP or STAND DOWN.
- **Reika** — What are we building, in one sentence? Close: the ship goes or it does not. `VERDICT: ...`.

## The land chain

One invocation, one chain, evidence at every stage. A red gate is a hold: stop at the red stage, report it, and never reach for a flag that skips it. There are no skip flags. Every stage pastes its command and its result — a claim without a command is a hypothesis, not a landing.

### Stage 0 — preconditions (read-only)

- `git status --short` and `git rev-parse --abbrev-ref HEAD`.
- Nothing secret is staged: inspect `git diff --cached --name-only`; credentials, keys, and env files never enter git.
- A tree dirty with unrelated work is named and the chain stops — one intention per branch.

### Stage 1 — debug + audit sweep (read-only, paste every tail)

| Check | Command |
| --- | --- |
| agent dialects | `python scripts/gen-agent-dialects --check` |
| lore consistency | `python scripts/check-lore-consistency` |
| the board | `python scripts/check-board` |
| the contract | `python scripts/check-contract` |
| measurement | `python scripts/check-measurement --check-doc` |
| voices | `python scripts/check-voices` |
| digests | `python scripts/check-digest` |
| record integrity | `python scripts/seat_record --check` |
| the suite | `python -m unittest discover -s tests -v` |
| setup dry run | `bash setup --host all --check` (writes nothing; `.\setup.ps1 -Check` on Windows) |

Write the sweep as a table: check, command, result, PASS/FAIL.

### Stage 2 — fix

For every FAIL make the smallest correct change, re-run exactly the failing check, paste the new result. Fixing by widening a threshold is a gate change — a full-loop act, not a stage in this chain. Hold instead.

### Stage 3 — cold verification (mandatory)

Spawn **Rin Takamiya — Keeper of Failure** with a decision (review) brief carrying only the requirement, the diff (`git diff`), and the sweep table — never the reasoning. Rin runs the gates herself, attempts one falsification, and closes `VERIFIED:` or `FAILED:` with pasted evidence. One fix round on FAILED, then one re-verify; a second FAILED holds the ship and goes to Reika.

### Stage 4 — land

- One atomic commit for one intention. Stage only the intended paths; inspect `git diff --cached` before committing. Never commit a secret.
- Push = deploy with the gates green: the push reports the SHA the gates measured, and the revision is reported by that SHA, not a wave number.
- Confirm on the default branch: `git log --oneline -3`; record the pushed SHA.

### Stage 5 — the version (only when the invocation asks for a release)

- `VERSION` and `docs/measurement.md`'s sample line move together; `check-digest` is the tie that fails closed.
- Report the version and the pushed SHA. A version is spent once and never reused.

## Gates

- Rin ACCEPTs before the release. A ship with an END is refused.
- Tests green. One accepted unit per commit. No force-push to a default branch.
- The revision is reported by the SHA the gates measured, not a wave number.

## Close

Reika closes: `VERDICT: ...` after Rin's ACCEPT and Aria's SHIP.

## Notes

Rin reviews before the release. A ship that skips the failure review is a deploy waiting to become a failure surface. The release is the exact window and action — contact, not a speech. A full-loop ship is appended to `DECISION_LOG.md` in its template.
