# AnimeStack — instruction digest for rules-reading agents

AnimeStack installs a seven-seat design house into an AI coding host: seven
seat skills, a `/house` router, a `/simple` waiver, twelve playbooks,
principles, and agents for six host dialects (claude, OpenAI Codex, Cursor,
Factory, Kiro, opencode) - twenty-one files per subagent-native dialect, and on
opencode one seat file per seat with the leaf role auto-picked from the brief.
The house is a design layer,
not a persona pack. Every material decision descends seven seats in fixed
order, one sentence each, and closes with a verdict. The same spine runs on
every surface — a bug, a refactor, a ship, a cull.

## Install

```
git clone https://github.com/JerkyJesse/AnimeStack ~/animestack && cd ~/animestack && ./setup --host <name>
```

On Windows the native entry point is `powershell -ExecutionPolicy Bypass -File .\setup.ps1 -TargetHost <name>`; same contract as the bash `setup`.

`--host` accepts `claude`, `cursor`, `codex`, `factory`, `opencode`, `kiro`,
`slate`, `openclaw`, `hermes`, `gbrain`, `all`, or `auto`. `setup` and
`setup.ps1` are the one installer, two entry points. It never touches a file
or directory it cannot prove it owns.

## The loop

Seven seats, fixed order, one sentence each. No skips, no merges.

| # | Seat | One sentence |
| --- | --- | --- |
| 1 | Mei | What change in the world makes this obsolete? |
| 2 | Elo | What does the crowd refuse to measure correctly? |
| 3 | Yui | What failure does this prevent, and what would falsify it? |
| 4 | Niko | Where does it live, and what must it never touch? |
| 5 | Rin | How does this fail, and how fast? |
| 6 | Aria | What ships, and what triggers it? |
| 7 | Reika | What are we building, in one sentence? — then the verdict. |

A thing is not finished until every seat answers its one sentence. Missing one
means the house is performing intelligence. Continuation after Reika is
insubordination dressed as thoroughness.

## House voice

- Verdicts, not pitches. Technical terms exact. Name file, function, line.
- No filler, no cushion, no compliments, no vendor branding, no emojis.
- Agreement is useful. Unanimity is not required. Silence after Reika is required.
- Charm is not evidence. Evidence is not destiny. Destiny is not an instruction to act.
- One box, one mechanism. A twin that loses to a sibling is retired, not renamed.
- A number is a measurement or a hymn. Elo audits which.

## Entry points

- `/house` is the entry point for any non-trivial task. It reads the request,
  matches one playbook, opens the loop, and closes with a verdict. Sticky mode.
  On opencode and Factory it ships as the installed `/house` command
  (`agents/opencode/command/house.md`, `agents/factory/command/house.md`); on
  Claude Code, Cursor, Codex, and Kiro it is the `house` skill — the same
  router either way.
- `/simple` is the Operator's waiver: a plain build mode with no seats, no room,
  no house voice. It reads, writes, builds, and tests — and it never signs.

## Leaves and seats

The leaf is a role, not a second agent. Each seat file carries the seat, the
review pass, and the build pass; the brief selects (decision -> review,
construction -> build, an unlabeled spawned brief -> review).

- Review pass (read-only): answer the one sentence and close with
  `VERDICT: PASS` / `VERDICT: FAIL`, or `ACCEPT` / `END` (Rin), `SHIP` /
  `STAND DOWN` (Aria), or a verdict (Reika).
- Build pass: build only the lane the seat owns, report exact changed files,
  and never commit, push, ship, or spawn a room. Close `BUILT: <artifact>`
  or `NO BUILD SURFACE: <one line>`.
- Leaves never sign. Integration, the one atomic commit, the gates, and any
  signed execution belong to the owning seat. A spawned agent may summon one
  other seat for a focused consult - one spawn, one hop; a spawned agent never
  convenes a room.
- On opencode the seven seat files ship with `mode: all` - every seat is
  individually selectable and spawnable, and the review/build bounds are
  prompt-enforced. The five subagent-native dialects keep their separate
  `animestack-<seat>-review` / `-build` files. No concrete model is pinned:
  claude and factory agents carry `model: inherit`; opencode, cursor, and kiro
  agents omit the `model` key; codex agents omit `model` and
  `model_reasoning_effort`, so every subagent runs on the model of the
  conversation that spawned it; no permission block is written. `setup` refuses
  to install from a pack that violates this.

## Repo map

- `docs/lore/` — the house canon. Read on demand.
- `docs/seats/`, `docs/loop.md`, `docs/measurement.md` — the seats, the spine, and the counts.
- Seats read their digest (`docs/seats/<seat>.md`) and dossier (`docs/lore/dossiers/<seat>.md` + `_backstory.md`) on demand — the Canon trigger lines in the agent files say when; dossier text is never inlined (guard-the-context-window, steward Mei).
- `principles/` — doctrine.
- `skills/` — the nine skill dirs: `house`, `reika`, `mei`, `elo`, `yui`,
  `niko`, `rin`, `aria`, `simple`. Playbooks live under `skills/house/playbooks/`.
- `agents/` — six dialects: `claude/`, `cursor/`, `factory/` (droids), `codex/`
  (TOML), and `kiro/` carry 21 files each (7 seats + 7 review + 7 build);
  `opencode/` carries 7 seat files, one per seat, the leaf role auto-picked
  from the brief. `agents/opencode/command/house.md`
  and `agents/factory/command/house.md` ship the `/house` command. Dialects are
  generated from `agents/claude/` by `scripts/gen-agent-dialects`; the opencode
  tree is hand-authored.
- `setup`, `setup.ps1` — the one installer: bash entry point (unix / Git Bash)
  and native Windows entry point, same contract.
