# First task

The first ship. A stranger clones the repo, runs one command, opens one
session, and hands the house a real but small task. This page is that path,
step by step, timed. No theory you do not need.

## The release in five minutes

1. Clone the repo.
2. Run `./setup --host <your host>` once.
3. Open a new session and say `/house`.
4. Give it a real task. Read the seven sentences. Watch Reika close.

That is the whole window. The rest of this page is the walkthrough for each
step.

## Install

```
git clone https://github.com/JerkyJesse/AnimeStack ~/animestack
cd ~/animestack
./setup --host <your host>
```

`--host` names the coding host whose config directory gets the skills. The
supported values are:

| Host | Where skills land | Agents |
| --- | --- | --- |
| `claude` | `~/.claude/skills` | `~/.claude/agents` |
| `cursor` | `~/.cursor/skills` | — |
| `codex` | `${CODEX_HOME:-~/.codex}/skills` | — |
| `factory` | `~/.factory/skills` | — |
| `opencode` | `~/.config/opencode/skills` | `~/.config/opencode/agent` |
| `kiro` | `~/.kiro/skills` | — |
| `slate` | reads `~/.claude/skills` (claude install refreshed) | — |
| `openclaw` | `~/.openclaw/skills/animestack` (digest) | — |
| `hermes` | `~/.hermes/skills/animestack` (digest) | — |
| `gbrain` | `~/.gbrain/skills/animestack` (digest) | — |

`--host all` installs every supported host; `--host auto` installs only the
hosts whose config directories already exist. The default is `claude`. Run
`./setup --help` for the exact list, and check
[`../measurement.md`](../measurement.md) if this table and the script ever
disagree — the script is the truth.

Windows installs by copy, not symlink. Re-run `./setup` after `git pull` to
refresh.

## First task

Open a new session, then hand the house a real but small task:

> Add a `--dry-run` flag to the sync command; it must print what would change
> and touch nothing.

Say `/house`. The router picks a playbook, opens the loop, and descends seven
seats. A realistic transcript:

```
playbook: feature (lead Reika, then Yui)

MEI:    The sync format is the only thing that could obsolete this; pin the
        preview output shape in the test so the flag fails when the format moves.
ELO:    Rank the sample before the build: --dry-run is a measurement when it
        lists exactly the paths that would change, and a hymn when it prints a
        plan.
YUI:    The failure is the missing preview — sync mutates before it reports, so
        every user guesses. Falsifier first: after a dry run the tree is
        byte-identical to before.
NIKO:   The flag lives in the sync module on the write path and touches nothing
        else: one branch, returns before any write, no shared counter.
RIN:    The failure is a dry run that writes anyway — accept only if a test
        asserts the diff is empty after --dry-run.
ARIA:   The release is the test run: pytest green and git status clean after the
        dry run.
REIKA:  Ship the flag with that test. VERDICT: ship. Next failure.

build:  YUI  BUILT: sync.py --dry-run flag + test_sync_dry_run
review: RIN  ACCEPT
ship:   ARIA SHIP
```

Seven sentences, one each, in order. No skips, no merges. Yui builds, Rin
reviews and accepts, Aria releases. Then silence after Reika.

The falsifier was written before the victory lap, and it is in the pack too —
pre-registered in [`../measurement.md`](../measurement.md) §5: run your own
work both ways and count escaped defects under `/house` against the same under
`/simple`. If there is no measured difference, the pack is prose wearing a
coat. Retire it, and say so in your own record.

## What just happened

The loop is the spine. Every material decision descends seven seats in fixed
order — Mei, Elo, Yui, Niko, Rin, Aria, Reika — one sentence each. A thing is
not finished when it is named; it is finished when all seven sentences exist.
Missing one means the house is performing intelligence.

The full spine, the two descents, solo authority, and the waiver are in
[`../loop.md`](../loop.md). The ring is drawn in
[`../images/loop.svg`](../images/loop.svg).

## When to use /simple

`/simple` is the Operator's waiver: one invocation, no seats, no room, no house
voice. It reads, writes, builds, and tests — and it never signs. No `ACCEPT`,
no `SHIP`, no push, no spend. A full-loop act stays a full-loop act.

Use it for a plain build where the loop would be costume: a one-line edit, a
format pass, a quick read. If the task would move state, production,
people, or public words, it is not `/simple` work.

## Tune it

- Seats ship with `mode: all`. Make one seat your primary agent to hold a
  session-long voice without re-reading the room each turn.
- Run `/simple` when the loop is heavier than the task.
- Uninstall cleanly with `./setup --host <name> --uninstall`. It removes only
  items it can prove it owns, and leaves everything else untouched.

## If the first /house fails

- **Skill not found.** Re-run `./setup --host <your host>`. Confirm the skill
  directory landed where the host table above says it should.
- **Windows refresh.** The install copies files, not symlinks. After `git pull`,
  re-run `./setup --host <your host>` before blaming the skill.
- **The room never appears.** Open a *new* session after setup; skills load at
  session start, not mid-session.
- **A count looks wrong.** Run the audit commands in
  [`../measurement.md`](../measurement.md) §2 first. A number that disagrees
  with the table is a defect — report the count that failed, the command you
  ran, and the host. That is the report. A number that agrees is not a defect.

The board never posts a number it cannot check.
