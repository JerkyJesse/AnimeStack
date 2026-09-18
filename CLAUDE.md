# AnimeStack — repo guidance for Claude Code

AnimeStack is a skill pack that installs the seven-seat house into this host.
Use `/house` for any non-trivial change: it runs the seven-seat loop and closes
with a verdict (setup installs it as a real command on the opencode host). `/simple` is the Operator's waiver — a plain build mode with no
seats, no room, no house voice — and it never signs.

## Rules for working in this repo

- Counts are facts. The canonical counts (nine skill dirs, seven seats, twelve
  playbooks, two commands, 21 agent files per subagent-native dialect and 7
  opencode seat files, 112 agent files total) live in
  `docs/measurement.md`. A doc
  that disagrees with the tree is a defect; fix the doc or fix the tree, never
  paper over the disagreement.
- `docs/lore/` is the house canon. It is part of this repo and is edited here
  like any other doc; the canon is the law the pack ships with.
- No secrets in this repo, ever. No channel URLs, no keys, no tokens, no
  machine paths. A secret belongs in an env file outside git.
- `setup` and `setup.ps1` are the one installer, two entry points (bash /
  native Windows). It never touches a file or directory it cannot
  prove it owns, and it is the single path that registers skills and agents.

## Build discipline

- Build leaves answer their one sentence, build only their lane, report exact
  changed files, and never commit, push, ship, or spawn a room.
- Leaves never sign. Integration, the one atomic commit, the gates, and any
  signed execution belong to the owning seat.
- A number is a measurement or a hymn. Elo audits which. Continuation after
  Reika is insubordination dressed as thoroughness.
