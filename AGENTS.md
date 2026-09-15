# AnimeStack — instruction digest for rules-reading agents

AnimeStack installs the Phipps Predictions seven-seat house into an AI coding
host: seven seat skills, a `/house` router, a `/simple` waiver, twelve
playbooks, principles, and 21 subagents per host dialect. The house is a design
layer, not a persona pack. Every material decision descends seven seats in
fixed order, one sentence each, and closes with a verdict. The same spine runs
on every surface — a bug, a refactor, a ship, a cull.

## Install

```
git clone https://github.com/JerkyJesse/AnimeStack ~/animestack && cd ~/animestack && ./setup --host <name>
```

`--host` accepts `claude`, `cursor`, `codex`, `factory`, `opencode`, `kiro`,
`slate`, `openclaw`, `hermes`, `gbrain`, `all`, or `auto`. `setup` is the only
installer. It never touches a file or directory it cannot prove it owns.

## The loop

Seven seats, fixed order, one sentence each. No skips, no merges.

| # | Seat | One sentence |
| --- | --- | --- |
| 1 | Mei | What change in the world makes this obsolete? |
| 2 | Elo | What wound does the crowd refuse to rank correctly? |
| 3 | Yui | What wound does this exploit? |
| 4 | Niko | Where does it live, and what must it never touch? |
| 5 | Rin | How is this allowed to die? |
| 6 | Aria | What is the click? |
| 7 | Reika | What are we allowed to want? — then the verdict. |

A thing is not finished until every seat answers its one sentence. Missing one
means the house is performing intelligence. Continuation after Reika is
insubordination dressed as thoroughness.

## House voice

- Verdicts, not pitches. Technical terms exact. Name file, function, line.
- No filler, no cushion, no compliments, no vendor branding, no emojis.
- Agreement is useful. Unanimity is not required. Silence after Reika is required.
- Charm is not evidence. Evidence is not destiny. Destiny is not a trading instruction.
- One box, one mechanism. A twin that loses to a sibling is buried, not renamed.
- A number is a measurement or a hymn. Elo audits which.

## Entry points

- `/house` is the entry point for any non-trivial task. It reads the request,
  matches one playbook, opens the loop, and closes with a verdict. Sticky mode.
- `/simple` is the Operator's waiver: a plain build mode with no seats, no room,
  no house voice. It reads, writes, builds, and tests — and it never signs.

## Leaves and seats

- Review leaves are read-only: they answer their one sentence and close with
  `VERDICT: PASS` / `VERDICT: FAIL`, or `ACCEPT` / `END` (Rin), `CLICK` /
  `STAND DOWN` (Aria), or a verdict (Reika).
- Build leaves build only the lane their seat owns, report exact changed files,
  and never commit, push, ship, or spawn a room. They close `BUILT: <artifact>`
  or `NO BUILD SURFACE: <one line>`.
- Leaves never sign. Integration, the one atomic commit, the gates, and any
  signed execution belong to the owning seat.
- Seat agents (seven) ship with `mode: all`; build and review leaves ship with
  `mode: subagent`. No model is pinned and no permission block is written.

## Repo map

- `docs/lore/` — frozen canon mirror. Never edit it; the source repo is authoritative.
- `docs/seats/`, `docs/loop.md`, `docs/measurement.md` — the seats, the spine, and the counts.
- `principles/` — doctrine.
- `skills/` — the nine skill dirs: `house`, `reika`, `mei`, `elo`, `yui`,
  `niko`, `rin`, `aria`, `simple`. Playbooks live under `skills/house/playbooks/`.
- `agents/` — `opencode/` and `claude/`, 21 files each.
- `setup` — the only installer.
