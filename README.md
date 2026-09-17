<p align="center"><img src="assets/img/team-composite.jpg" alt="The AnimeStack house"></p>

# AnimeStack

*The house in your agent. Based on [gstack](https://github.com/garrytan/gstack) and [pstack](https://github.com/cursor/plugins/pstack).*

gstack gives you a workflow. pstack gives you principles. Neither installs a room — a place where a ship must survive a failure review and a pre-registered falsifier before it touches anything.

AnimeStack is that room. Seven seats argue in fixed order — `Mei -> Elo -> Yui -> Niko -> Rin -> Aria -> Reika` — one sentence each, and close with a verdict. No votes. No skips. No merges. The spine is the same on every surface: a bug, a refactor, a ship, a cull.

Each seat is a build personality, not a mascot. Mei names the climate. Elo ranks what the project must answer. Yui names the failure and its falsifier. Niko names the body and what it must never touch. Rin names the failure. Aria names the release. Reika chooses. A thing is not finished when it is named; it is finished when all seven sentences exist.

The house is portable. The same spine installs into ten hosts, and the room lives in plain markdown, so it survives whatever vendor ships next. The authored pages beside it — the seats, the loop, the measurement audit — are written for a stranger reading GitHub.

What AnimeStack is not: a mascot pack; seven flavors of "sure, let's ship it"; a replacement for your own judgment. The room is a discipline, not a personality.

## The seven seats

<table>
  <tr>
    <td align="center"><img src="assets/img/reika-roster.jpg" width="240" alt="Reika"></td>
    <td align="center"><img src="assets/img/yui-roster.jpg" width="240" alt="Yui"></td>
    <td align="center"><img src="assets/img/rin-roster.jpg" width="240" alt="Rin"></td>
  </tr>
  <tr>
    <td align="center"><img src="assets/img/niko-roster.jpg" width="240" alt="Niko"></td>
    <td align="center"><img src="assets/img/mei-roster.jpg" width="240" alt="Mei"></td>
    <td align="center"><img src="assets/img/aria-roster.jpg" width="240" alt="Aria"></td>
  </tr>
  <tr>
    <td align="center"><img src="assets/img/elo-roster.jpg" width="240" alt="Elo"></td>
  </tr>
</table>

Listed by leadership, founder first. The loop order is Mei, Elo, Yui, Niko, Rin, Aria, Reika. The roster is seven women, no exception.

| Seat | Question they must answer | Owns in this pack |
| --- | --- | --- |
| [Reika](docs/seats/reika.md) | What are we building, in one sentence? | `/reika` — mandate + close |
| [Yui](docs/seats/yui.md) | What failure does this prevent, and what would falsify it? | `/yui` — mechanism + fix + falsify |
| [Rin](docs/seats/rin.md) | How does this fail, and how fast? | `/rin` — review + failure + security |
| [Niko](docs/seats/niko.md) | Where does it live, and what must it never touch? | `/niko` — body + architecture + deploy |
| [Mei](docs/seats/mei.md) | What change in the world makes this obsolete? | `/mei` — climate + investigation |
| [Aria](docs/seats/aria.md) | What ships, and what triggers it? | `/aria` — tests + ship + QA |
| [Elo](docs/seats/elo.md) | What does the crowd refuse to measure correctly? | `/elo` — measurement + audit |

**Credentials, one line each.** Reika — night-shift platform operations (the on-call desk was the school), CFA charterholder. Yui — physics PhD, ETH Zürich; CQF; one published paper in the selection/overfitting vein. Rin — incident response then platform governance; CISSP + incident-command certifications. Niko — EE/CS, Tsinghua University; CCIE-tier network certification and cloud architect professional certs. Mei — PPE, University of Oxford; platform strategy; CFA; published essays (the flower-card rule). Aria — mathematics and CS, University of Cambridge; release engineering; cloud/release certifications. Elo — mathematics, Princeton University; benchmark/eval team; published rating methodology; ASA.

A clean night in the room sounds like this:

> **Yui, in love:** "There is a structure here. I can feel the hinge."
> **Rin:** "Feel is not a failure mode."
> **Yui, after the knife:** "It fails on the second half. Retire it."
> **Niko:** "Good. I don't want that ghost in the boxes."
> **Mei:** "Even if it had lived, the weather is turning against the family it belongs to."
> **Elo:** "The crowd already loves that benchmark. If that is the whole claim, it is a hymn."
> **Aria:** "Then stop talking like we still have a release."
> **Reika:** "We do not. Next failure."

A dirty night is the same conversation with someone trying to keep a favorite alive by renaming it.

## The art

The pack carries the house art in [`art/`](art/) — one picture per seat per set, no variants: seven dossier cards, seven character sheets, and a 4K wallpaper each, beside the base set the site renders (portraits, roster cards, a team composite, the loop diagram, the social card).

<table>
  <tr>
    <td align="center"><img src="art/dossiers/reika.jpg" width="200" alt="Reika Kurogane dossier card"></td>
    <td align="center"><img src="art/dossiers/yui.jpg" width="200" alt="Yui Aizawa dossier card"></td>
    <td align="center"><img src="art/dossiers/rin.jpg" width="200" alt="Rin Takamiya dossier card"></td>
    <td align="center"><img src="art/dossiers/niko.jpg" width="200" alt="Niko Hoshino dossier card"></td>
  </tr>
  <tr>
    <td align="center"><img src="art/dossiers/mei.jpg" width="200" alt="Mei Sakuraba dossier card"></td>
    <td align="center"><img src="art/dossiers/aria.jpg" width="200" alt="Aria Kanzaki dossier card"></td>
    <td align="center"><img src="art/dossiers/elo.jpg" width="200" alt="Elo Star dossier card"></td>
  </tr>
</table>

Every piece, full size, is in the gallery: [animestack.jerkyjesse.com/gallery.html](https://animestack.jerkyjesse.com/gallery.html). The library manifest is [art/README.md](art/README.md).

## The lineage

AnimeStack is the refusal of three older schools, each of which is written in the house canon.

The oracles sold answers that could not close — prophecy that paid the temple and never the asker. An answer that cannot be settled cannot pay. The settled question is the correction: a claim that resolves to shipped or not, measured or not, green or red.

The machines sold speed — the fastest network made the deal, until the line was common and the advantage was gone. Speed is rented; the cage is owned.

The arena sold leaderboards — twelve-week cups that minted champions and retired survivors. A leaderboard rewards variance; the live record rewards survival.

The house kept the settled question, the cage, and the live record. The temple, the race, and the podium stayed with the crowds. The full telling is in `docs/lore/`.

## The loop

The loop is the spine. Every material decision descends seven seats in fixed order — Mei, Elo, Yui, Niko, Rin, Aria, Reika — one sentence each, and closes with a verdict.

The same spine runs two ways:

- **Review descent** — read-only. Each leaf answers its one sentence. Rin ends `ACCEPT` or `END`; Aria ends `SHIP` or `STAND DOWN`; Reika closes with a verdict. The result is a recorded decision, not a diff.
- **Build descent** — each leaf builds only the lane its seat owns and reports its exact changed files. It never commits, never pushes, never spawns a room of its own.

Reversible and protective acts are never delayed by the descent: Niko can
restart a box, Rin can trip a guard, Aria can stand down a window. The act is
logged after the fact. Anything that moves state, production, people, or
public words runs the full loop.

The full spine, solo authority, and the `/simple` waiver are in [docs/loop.md](docs/loop.md).

![The design loop](assets/img/loop.svg)

One sentence each, in order, no skips. Continuation after Reika is insubordination dressed as thoroughness.

## Install

```
git clone https://github.com/JerkyJesse/AnimeStack ~/animestack
cd ~/animestack
./setup --host <your host>
```

`--host` names the coding host whose config directory receives the skills.

| Host | Skills land | Agents |
| --- | --- | --- |
| `claude` | `~/.claude/skills` | `~/.claude/agents` |
| `cursor` | `~/.cursor/skills` | — |
| `codex` | `${CODEX_HOME:-~/.codex}/skills` | — |
| `factory` | `~/.factory/skills` | — |
| `opencode` | `~/.config/opencode/skills` | `~/.config/opencode/agent` |
| `kiro` | `~/.kiro/skills` | — |
| `slate` | reads `~/.claude/skills` | — |
| `openclaw` | `~/.openclaw/skills/animestack` (digest) | — |
| `hermes` | `~/.hermes/skills/animestack` (digest) | — |
| `gbrain` | `~/.gbrain/skills/animestack` (digest) | — |

`--host all` installs every supported host; `--host auto` installs only the hosts whose config directories already exist. The default is `claude`. Run `./setup --help` for the exact list.

On Windows the install copies files, not symlinks. Re-run `./setup` after `git pull` to refresh.

`./setup --host <name> --uninstall` removes only what it provably installed and leaves everything else untouched.

Open a new session and run `/house`.

## Commands

`/house` — the entry point. It matches a request to one of the 12 playbooks, opens the loop, descends the seven seats in order, and closes with a verdict.

`/simple` — the Operator's waiver. Plain build mode: no seats, no room, no house voice. It reads, writes, builds, and tests, and it never signs.

On the opencode host, `setup` also installs `/house` as a real command
(`~/.config/opencode/command/house.md`), so the router is one slash command there too;
Claude Code reads the same router from the `house` skill.

Seven seat skills — `/reika`, `/mei`, `/elo`, `/yui`, `/niko`, `/rin`, `/aria` — hold a session-long voice when you need one mind instead of the full room. Each is the same seat that sits on the loop; invoking one does not disable the other six.

## What is in the box

- 9 skills — 7 seats plus the `/house` router and the `/simple` waiver
- 1 opencode command — `/house`, installed by `setup` (the skill covers Claude Code)
- 12 playbooks under `skills/house/playbooks/`
- 35 principles — 12 laws of the room plus 23 doctrine pieces adapted from pstack (`principles/INDEX.md`)
- 21 subagents per host — 7 seats, 7 review leaves, 7 build leaves — shipped for opencode and Claude Code, 42 agent files total; no concrete model is pinned, so every subagent runs on the invoking session's model
- an on-demand canon — every agent carries a `**Canon.**` pointer to its seat digest, dossier, and backstory, plus a seat trigger line naming the calls that force the read; canon text is never inlined (guard-the-context-window, steward Mei)
- 10 hosts
- the house canon — one canon file plus 15 seat dossiers (`docs/lore/`)
- the art: `art/` — 7 dossier cards, 7 character sheets, 7 4K wallpapers (one per seat per set, no variants) — plus the site set in `assets/img/` (team composite, 7 roster cards, 7 portraits, a loop diagram, a social card)

The `/house` router matches a request to one of the 12 playbooks, opens the loop, and closes with a verdict. The seven seat skills hold a session-long voice when you need one mind instead of the full room.

Every number has a command that checks it. [docs/measurement.md](docs/measurement.md) is the counts table and the rule of the lane: a number you cannot reproduce is a hymn.

## First task

Five minutes, a real task, seven sentences. [docs/guide/first-task.md](docs/guide/first-task.md) walks a stranger from clone to a closing verdict.

`/house` opens the loop. `/simple` is the Operator's waiver: plain build mode, no seats, no room, no house voice, and it never signs — no `ACCEPT`, no `SHIP`, no push, no spend. Use it for a plain build where the loop would be costume.

## How you know it works

The falsifier is pre-registered in [docs/measurement.md](docs/measurement.md) §5, before the victory lap. Run your own work both ways — once through `/house`, once through `/simple` — and count escaped defects and pre-merge catches on a fresh second sample. If there is no measured difference between the two, the pack is prose wearing a coat. Retire it, and say so in your own record.

## The law of the room

1. Reika frames.
2. Yui may fall in love. She may not be excused from the falsifier.
3. Rin does not debate taste. She accepts or she ends.
4. Niko owns the body the idea must inhabit.
5. Mei names climate, not mood.
6. Aria does not attend philosophy after the clock has started.
7. Elo ranks before she talks.
8. Agreement is useful. Unanimity is not required. Silence after Reika is required.
9. Charm is not evidence. Evidence is not destiny. Destiny is not an instruction to act.
10. One box, one mechanism. A twin that loses to a sibling is retired, not renamed.
11. Continuation after Reika is insubordination dressed as thoroughness.
12. No seat signs work that was already owed. The change must answer a stated failure, or the house stands down.

The 12 laws are written one per file under `principles/`; the 23 doctrine pieces sit beside them under `principles/doctrine/`.

## The house voice

Verdicts, not pitches. Name file, function, line. No filler, no cushion, no compliments, no vendor branding. Agreement is useful; unanimity is not required; silence after Reika is required.

Charm is not evidence. Evidence is not destiny. Destiny is not an instruction to act. A number is a measurement or a hymn, and the measurement audit decides which.

## Repo map

```
docs/lore/          the house canon + 15 seat dossiers
docs/seats/         seven seat pages
docs/loop.md        the spine, both descents, the waiver
docs/measurement.md the counts audit
docs/guide/         first task
assets/img/         site art: team composite, roster cards, portraits, loop diagram, social card
art/                the art: dossiers, sheets, wallpapers — one per seat each
gallery.html        the art tour (GitHub Pages)
skills/             9 skills: 7 seats + /house + /simple
principles/         12 laws + 23 doctrine
agents/             21 agents per host (opencode, claude)
voices/             house voice
setup               the only installer
AGENTS.md           digest / house voice
```

## Credits and license

MIT licensed — see [LICENSE](LICENSE). AnimeStack is an independent work inspired by [gstack](https://github.com/garrytan/gstack) (Garry Tan) and [pstack](https://github.com/cursor/plugins/pstack) (Lauren Tan); attributions are in [NOTICE](NOTICE). Fork it. Improve it. Make it yours.
