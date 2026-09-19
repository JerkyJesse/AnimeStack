# Measurement

The measurement lane of this pack. Every number this repo tells itself lives here,
beside the command that checks it. A number is a measurement when it names its sample,
states its cost, and survives the check. A number is a hymn when it flatters a story.

The house ranks before it talks. This file is the ranking, in writing, for the GitHub
audience that does not share the room. If you run the commands and they disagree with
the table, the table is wrong.

## 1. The sample

What is ranked: this repository, release `v1.11.0` (`VERSION`), 2026-09-18. The canon
text inside it is this pack's own, first written for v1.3.0; the language reform arrived in v1.4.0, the credentials in v1.5.0, the six-dialect agent coverage in v1.6.0, the art and graphics credentials in v1.7.0, the one-file opencode room in v1.8.0, the one-file-everywhere autonomy collapse in v1.9.0, the collaborative room in v1.10.0, and the House Board and the contract gate in v1.11.0.

The claims in this pack are claims about this tree, not promises about the outcomes a
user will get. A pack that installs cleanly on your host is a body question, not a result
question. The result question is pre-registered below in section 5, and it is scored on a
fresh sample, not on this one.

What the counts do not prove: that the pack makes anyone faster, safer, or correct.
Those are outcome claims, and they are deferred to section 5. The counts prove only that
the tree contains what the table says it contains, at the stated release, on the stated date.

## 2. The counts table

Run each command from the repo root. The expected count is the v1.10.0 truth; a command
that prints anything else is a defect, and the defect is the tree's number, never the
prose.

| Count | What | Audit command |
| --- | --- | --- |
| 7 | seats | `ls docs/seats \| wc -l` |
| 9 | skills | `ls skills \| wc -l` (house, reika, mei, elo, yui, niko, rin, aria, simple) |
| 12 | playbooks | `ls skills/house/playbooks \| wc -l` |
| 12 | laws | `ls principles/law-*.md \| wc -l` |
| 23 | doctrine pieces | `ls principles/doctrine \| wc -l` |
| 10 | hosts | `grep -oE 'claude\|cursor\|codex\|factory\|opencode\|kiro\|slate\|openclaw\|hermes\|gbrain' setup \| sort -u \| wc -l` |
| 7 | agents, claude host | `ls agents/claude \| wc -l` (one seat file per seat; role picked from the brief) |
| 7 | agents, cursor host | `ls agents/cursor/*.md \| wc -l` |
| 7 | agents, factory host | `ls agents/factory/*.md \| wc -l` |
| 7 | agents, codex host | `ls agents/codex/*.toml \| wc -l` |
| 7 | agents, kiro host | `ls agents/kiro/*.md \| wc -l` |
| 7 | agents, opencode host | `ls agents/opencode/*.md \| wc -l` |
| 42 | agent files, all dialects | `find agents -maxdepth 2 -type f \( -name '*.md' -o -name '*.toml' \) \| wc -l` |
| 1 | house command, opencode | `ls agents/opencode/command/*.md \| wc -l` |
| 1 | house command, factory | `ls agents/factory/command/*.md \| wc -l` |
| 2 | commands, all hosts | `find agents -path '*/command/*.md' \| wc -l` |
| 1 | canon file | `ls docs/lore/*.md \| grep -v README \| wc -l` (canon) |
| 15 | lore dossiers | `ls docs/lore/dossiers \| wc -l` |
| 16 | lore total | the canon + 15 dossiers, the two rows above summed |
| 98 | board questions | `python scripts/check-board --count` |
| 16 | site art images | `ls assets/img/*.jpg \| wc -l` |
| 7 | art dossier cards | `ls art/dossiers \| wc -l` |
| 7 | art character sheets | `ls art/sheets \| wc -l` |
| 7 | art wallpapers | `ls art/wallpapers \| wc -l` |
| 21 | art library, total | `find art -type f -not -name 'README.md' \| wc -l` |
| 28 | site thumbnails | `find assets/thumbs -type f \| wc -l` |

Notes on the rows.

The seats row is seven, not eight. The roster is seven women, no exception, and the
seat pages mirror them one for one. A seat written otherwise has left the tree.

The skills row is nine: the seven seats plus the `house` skill and the `simple` waiver.
If a new skill appears without a row here, the table is stale, not the skill.

The playbooks and laws are both twelve, and they are not the same twelve. The playbooks
live under `skills/house/playbooks`; the laws live under `principles/law-*.md`. Count
each with its own command and do not let the matching numbers fool you into merging them.

The hosts row counts the ten host names the setup script ships for, not a README
heading. `grep -c '^### ' README.md` is a hymn: it counts headings, not hosts. Use the
setup list; it prints 10. The ten names are claude, cursor, codex, factory, opencode,
kiro, slate, openclaw, hermes, gbrain.

The agents rows: every dialect ships seven seat files - one file per seat, the
seat, review, and build roles in one file, picked from the brief - forty-two
agent files total. Codex ships TOML custom agents; the others ship markdown. A
host that ships the wrong roster is a defect, not a rounding error.

The commands rows count two: `agents/opencode/command/house.md` and
`agents/factory/command/house.md`, installed by setup to
`~/.config/opencode/command/house.md` and `~/.factory/commands/house.md` so
`/house` is a real slash command on those hosts. Claude Code, Cursor, Codex,
and Kiro need no command file — the `house` skill is already the slash command
there.

The lore rows are two that sum to sixteen: one canon file at the top of `docs/lore`
(`canon.md`), and fifteen dossiers in `docs/lore/dossiers`. The policy page
`docs/lore/README.md` is authored, not canon, and is not one of the sixteen. The canon
is the law; the dossiers are the deep lore. They are kept separate because a dossier
deepens a seat and never contradicts it, and the count is the proof they are both present.

The site-art row is the sixteen jpgs in `assets/img/` — seven portraits, seven roster cards,
the team composite, and the social card; the loop diagram and the favicon are svg and are
not counted. One copy of each picture ships in the repo; the README and `docs/seats/*.md`
render these same files.

The art library rows are the pack's own art set at the repo root, in `art/` — one picture
per seat per set, no variants: seven dossier cards, seven character sheets, seven 4K
wallpapers. The library total is the three rows summed, `find art -type f`, minus the
library's own `README.md`. The thumbnails row counts the site's pre-rendered thumbnails
under `assets/thumbs/` — one per library piece plus the seven primary portraits; every
thumbnail is generated from the source picture, never the other way around. A thumbnail
set that drifts from the library is a defect; re-run the count before believing the tour.

The seat pages and the first row are the same seven files. They are not counted twice
as different things; seven seats, seven pages, one row.

## 3. The rule of the lane

A number is a measurement when it names its sample, states its cost, and survives being
checked against the tree. The sample is named (section 1). The fee is the command: if a
count has no command that reproduces it, the count is unpaid. The check is the command
run against the tree.

A number is a hymn when it flatters a story. Stars on this repo are a hymn. Downloads
are a hymn. A review that says the pack "works great" without running the counts is a
hymn. The counts table is the measurement, and the two are not the same instrument.

This lane audits the ordering, not the bar. The falsifier in section 5 is Yui's
mechanism. The bar on when to retire the pack is Rin's. The counts table is mine.

## 4. How the audit runs

Run each command in section 2 from the repo root. Where the doc and the tree disagree,
the doc is wrong, not the tree. Fix the number to match the tree, then note the change;
never edit the prose so the old number can stay comfortable. If a count cannot be
reproduced at all, there is no ranking to post, and the lane owes the sentence.

The stand-down sentence, verbatim:

> No ranking — the board never posts this number.

## 5. The falsifier

Pre-registered, before the victory lap. The pack's real claim is not the counts. The
counts are a body check. The claim is: a session run through `/house` catches a defect
before it escapes, where a plain `/simple` session ships it, and a seat can end a bad
plan, a Rin END or an Aria STAND DOWN, before a live bug proves it.

Test on a fresh second sample: run your own work both ways and count escaped defects and
pre-merge catches under `/house` against the same under `/simple`. If there is no measured
difference, the pack is prose wearing a coat. Retire it, and say so in your own record.

This falsifier is written now so it cannot be written after the result.

## 6. Close

The stand-down is the floor, never the ceiling. With something rankable, rank it. With
nothing rankable, say the sentence and stop. The board never posts a number it cannot
check.
