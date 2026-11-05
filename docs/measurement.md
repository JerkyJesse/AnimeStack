# Measurement

The measurement lane of this pack. Every number this repository tells itself lives
here, beside the command that checks it. A number is a measurement when it names its
sample, states its cost, and survives the check. A number is a hymn when it flatters
a story.

The house ranks before it talks. This file is the ranking, in writing, for the GitHub
audience that does not share the room. If you run the commands and they disagree with
the table, the table is wrong.

## 1. The sample

What is ranked: this repository, release `v2.0.0` (`VERSION`), 2026-11-05. The canon
text inside it is this pack's own, first written for v1.3.0; the language reform arrived
in v1.4.0, the credentials in v1.5.0, the six-dialect agent coverage in v1.6.0, the art
and graphics credentials in v1.7.0, the one-file opencode room in v1.8.0, the
one-file-everywhere autonomy collapse in v1.9.0, the collaborative room in v1.10.0, the
House Board and the contract gate in v1.11.0, the opencode provenance stamp in v1.12.0,
the gate self-tests, voice and digest checks, and the `--root` hooks in v1.13.0, the
building room in v1.14.0, the invention surface and the cold verification pass in
v1.15.0, the per-host installer round-trip tests in v1.16.0, the whole-house port in
v1.17.0, and v2.0.0 — the complete public house: the twenty-five-section canon, the
evidence ladder, the claim standard, the work surfaces, the eras, the archive, the two
nights, the seat lanes, the seat packs, and the release surface.

The claims in this pack are claims about this tree, not promises about the outcomes a
user will get. A pack that installs cleanly on your host is a body question, not a
result question. The result question is pre-registered in section 5, and it is scored
on a fresh sample, not on this one.

What the counts do not prove: that the pack makes anyone faster, safer, or correct.
Those are outcome claims, and they are deferred to section 5. The counts prove only
that the tree contains what the table says it contains, at the stated release, on the
stated date.

## 2. The counts

Run each command from the repo root, or run the gate and read every row at once. The
expected value is the v2.0.0 truth; a command that prints anything else is a defect, and
the defect is the tree's number, never the prose. An exact row is a fact; a floor row is a
bar another lane is still landing, and the owner column names the seat accountable for it.

| Count | What | Owner | Audit command |
| --- | --- | --- | --- |
| 8 | seats | Mei | `(Get-ChildItem docs/seats -Filter *.md).Count` |
| 10 | skills | Niko | `(Get-ChildItem skills -Directory).Count` |
| 12 | playbooks | Niko | `(Get-ChildItem skills/house/playbooks).Count` |
| 14 | laws | Reika | `(Get-ChildItem principles -Filter law-*.md).Count` |
| 23 | doctrine pieces | Mei | `(Get-ChildItem principles/doctrine).Count` |
| 11 | install targets | Niko | `python scripts/check-measurement` |
| 8 | agents, claude host | Niko | `(Get-ChildItem agents/claude -Filter animestack-*).Count` |
| 8 | agents, cursor host | Niko | `(Get-ChildItem agents/cursor -Filter animestack-*.md).Count` |
| 8 | agents, factory host | Niko | `(Get-ChildItem agents/factory -Filter animestack-*.md).Count` |
| 8 | agents, codex host | Niko | `(Get-ChildItem agents/codex -Filter animestack-*.toml).Count` |
| 8 | agents, kiro host | Niko | `(Get-ChildItem agents/kiro -Filter animestack-*.md).Count` |
| 8 | agents, opencode host | Niko | `(Get-ChildItem agents/opencode -Filter animestack-*.md).Count` |
| 48 | agent files, all dialects | Niko | `python scripts/check-measurement` |
| 1 | house command, opencode | Niko | `(Get-ChildItem agents/opencode/command -Filter *.md).Count` |
| 1 | house command, factory | Niko | `(Get-ChildItem agents/factory/command -Filter *.md).Count` |
| 2 | commands, all hosts | Niko | `(Get-ChildItem agents/*/command -Filter *.md).Count` |
| 8 | lore pages | MechaPip | `(Get-ChildItem docs/lore -Filter *.md | Where-Object Name -ne README.md).Count` |
| 17 | lore dossiers | Mei | `(Get-ChildItem docs/lore/dossiers -Filter *.md).Count` |
| 25 | lore total | Mei | `python scripts/check-measurement` |
| 25 | canon sections | Mei | `(Select-String docs/lore/canon.md -Pattern '^## [IVX]+[.]').Count` |
| 6 | docs pages | Reika | `(Get-ChildItem docs -Filter *.md).Count` |
| 112 | board questions | Elo | `python scripts/check-board --count` |
| 8 | board seats | Elo | `python scripts/check-board --count` |
| 8 | seat pages | Aria | `(Get-ChildItem seats -Filter *.html).Count` |
| 27 | site pages | Aria | `(Get-ChildItem *.html,seats/*.html,lore/*.html).Count` |
| 20 | site art images | Aria | `(Get-ChildItem assets/img -Include *.jpg,*.png).Count` |
| 32 | site thumbnails | Aria | `(Get-ChildItem assets/thumbs -Recurse -File).Count` |
| 8 | art dossier cards | Aria | `(Get-ChildItem art/dossiers).Count` |
| 8 | art character cards | Aria | `(Get-ChildItem art/sheets).Count` |
| 8 | art wallpapers | Aria | `(Get-ChildItem art/wallpapers).Count` |
| 24 | art library, total | Aria | `(Get-ChildItem art -Recurse -File | Where-Object Name -ne README.md).Count` |
| 1 | voices | Rin | `(Get-ChildItem voices).Count` |
| >=6 | gate scripts | Rin | `(Get-ChildItem scripts -Filter check-*).Count` |
| >=3 | test files | Rin | `(Get-ChildItem tests -Filter *.py).Count` |
| >=8 | record rows | Yui | `python scripts/seat_record --read` |
| >=1 | decisions logged | Yui | `python scripts/room_scorecard` |
| >=1 | claim cards | Yui | `(Get-ChildItem claims -Filter *.md).Count` |
| >=1 | pattern registry entries | MechaPip | `python scripts/check-measurement` |
| >=8 | seat packs | Niko | `(Get-ChildItem dsh\animestack-team -Filter *.md).Count` |
| >=1 | leak patterns | Rin | `(Get-Content security/leak-patterns.txt | Where-Object {$_ -and -not $_.StartsWith('#')}).Count` |

Notes on the rows.

The seats row is eight: seven women and the machine — the named exception, written down so
no session reads it as a costume or as a precedent. The seat pages mirror the roster one
for one.

The skills row is ten: the eight seats plus the `house` skill and the `simple` waiver. The
playbooks row is twelve and the laws row is fourteen; they are not the same set, and each
counts its own way. The playbooks live under `skills/house/playbooks`; the laws live under
`principles/law-*.md`.

The install targets row counts the host names the setup script ships for, not a README
heading: `grep -c '^### ' README.md` is a hymn, because it counts headings. The row reads
the installer's own host list, so a host the installer cannot install is not a target.

The agents rows count seat files per dialect, one file per seat with the seat, review, and
build roles in one file, picked from the brief. Codex ships TOML custom agents; the others
ship markdown. A host that ships the wrong roster is a defect, not a rounding error.

The lore rows count the pages at the top of `docs/lore` — the canon, the scenes, the
retrieval map, and the pre-history books — plus the seventeen seat dossiers. The policy
page `docs/lore/README.md` is authored, not canon, and is not one of them.

The canon sections row counts the `## <numeral>.` headings in the canon: twenty-five, which
is the whole house. A section that exists in prose but not as a heading is not a section a
reader can find, and a heading with no section body is a broken promise.

The board rows are the credential: eight seats, fourteen questions each, every key carrying
a source anchor resolved against the live tree. The `board seats` row is derived from the
board's own `## <seat>` headings, never from a literal.

The site and art rows count rendered surfaces and the library that feeds them: one copy of
each picture ships in the repo, the README and the seat pages render the same files, and a
thumbnail is generated from the source picture, never the other way around. A set that
drifts from the library is a defect. The generated site is 27 pages at v2.0.0; the row is exact and moves only with the generator.

The floor rows — `gate scripts`, `test files`, `record rows`, `decisions
logged`, `claim cards`, `pattern registry entries`, `seat packs`, `leak patterns` — are the
descent's bars, each with its owner. A floor is met or it is red; it is never rounded up.

## 3. The rule of the lane

A number is a measurement when it names its sample, states its cost, and survives being
checked against the tree. The sample is named (section 1). The fee is the command: if a
count has no command that reproduces it, the count is unpaid. The check is the command
run against the tree.

The counts are two kinds, and the kind is in the cell:

- An **exact** cell (`8`) is a fact of this tree at this release. It must equal the
  command's output exactly; a doc that disagrees is the defect, and the tree's number
  wins.
- A **floor** cell (`>=8`) is a bar the release must meet, never a count. It exists for a
  class another lane is still landing: the floor cannot be born lying, and it does not go
  stale between lanes. The command still prints the fact every run.

The completeness assertion is the third instrument: a declared class with no row, a row
with no computer, a duplicated row, an owner that disagrees with the declared owner, or a
top-level directory the table never names all fail the gate. A new artifact class with no
row is unmeasured, not free — that is how a count silently stops meaning anything.

A number is a hymn when it flatters a story. Stars on this repo are a hymn. Downloads are
a hymn. A review that says the pack "works great" without running the counts is a hymn.
The counts table is the measurement, and the two are not the same instrument.

This lane audits the ordering, not the bar. The falsifier in section 5 is Yui's
mechanism. The bar on when to retire the pack is Rin's. The counts table is mine.

## 4. How the audit runs

The gate is the command. From the repo root:

```
python scripts/check-measurement --check-doc
```

That prints every row and fails closed on any disagreement between this file, the tree,
the declared owner, or the artifact roots. `python scripts/check-measurement` prints the
same rows and exits 0 — the read without the verdict. `--json` emits the same counts for
a generator or a page, so no site renders a number this file cannot reproduce.

The shell forms in the table are conveniences for a human at a prompt, and they are
written for a PowerShell host because the pack ships a native Windows entry point
(`setup.ps1`) beside the bash one. A count that only reproduces on one of the two hosts
is not portable; the Python gate is the portable form, and it is the one CI runs.

Where the doc and the tree disagree, the doc is wrong, not the tree. Fix the number to
match the tree, then note the change; never edit the prose so the old number can stay
comfortable. If a count cannot be reproduced at all, there is no ranking to post, and the
lane owes the sentence.

The stand-down sentence, verbatim:

> No ranking — the board never posts this number.

## 5. The falsifier

Pre-registered, before the victory lap. The pack's real claim is not the counts. The
counts are a body check. The claim is: a session run through `/house` catches a defect
before it escapes, where a plain `/simple` session ships it, and a seat can end a bad
plan — a Rin END or an Aria STAND DOWN — before a live bug proves it.

The claim is measured the way every claim in this house is measured: against a control,
on both halves, with a receipt.

- **Sample.** A fresh set of your own tasks, at least ten, run after this file was read.
  The sample is your work, not this pack's history; the pack's own counts are not the
  sample.
- **Control.** The same tasks run through `/simple`, by the same hand, in the same week.
  The control is the change with the mechanism removed: if the plain session catches the
  same defects, the room was not the mechanism.
- **Both halves.** Split the sample in time order and score each half. If the two halves
  disagree, the result is not a result yet — it is one half and a story.
- **Falsifier.** Written before the first run: the count that would make you retire the
  pack. "If `/house` does not raise pre-merge catches by at least one per ten tasks in
  both halves, the room is prose wearing a coat."
- **Receipt.** The count, the sample, and the command tail, kept where the next reader
  can check it. A result with no receipt is an anecdote with a number.

If there is no measured difference, the pack is prose wearing a coat. Retire it, and say
so in your own record. This falsifier is written now so it cannot be written after the
result.

## 6. The claim standard, in this lane's words

The pack may ship a claim. It may not ship a claim with a shape it cannot account for.
A claim that reaches a reader carries five fields, and a claim missing one is a hymn:

1. **The claim, one sentence** — the failure the change removes.
2. **The sample** — what was counted, how many, over what window.
3. **The control** — the same work with the mechanism removed.
4. **Both halves** — first half and second half, each scored, each agreeing.
5. **The receipt** — the command, its tail, and the date it ran.

The bar is a shape, never a number the pack owns. A threshold imported from another
house's ledger would be a private fact wearing a public coat, and this pack carries none.
The bar sizes the surface a claim earns; it does not bury the claim, and it does not
promote it on a first look. A first-sample miss parks the claim with a dated review; only
a counted refusal closes it. That is canon section XXII and law 14, and this table is
where the count lives.

## 7. The evidence ladder

Every instrument in this pack sits on one of three tiers, and only the record moves a
name between them. The tier is not a mood; each one has an instrument that can be run.

- **Measured.** The instrument has a counted sample, a control, both halves, and a
  receipt. Its tier is this table: a row is a measured class, and the gate that computes
  it is the receipt. A measured instrument can be evicted by a better one.
- **Parked.** The instrument has a claim and no verdict yet. It lives forward, dated, with
  the sample it must count and the date it is reviewed. A park is alive; a park is not a
  pass, and it is not a burial. The park's row carries its review date in the record.
- **Retired.** The record refused it: both halves red, a sibling dominated it, or the
  counted sample closed. It keeps its name, its entry, its number, and its reason, and it
  does not come back under a new coat.

The ladder orders instruments, not people. No seat's sentence is ranked here, and no
credit or debt in the seat record moves a row in this table.

## 8. The contact read

Every room closes with the contact read, and the contact read is measured, not narrated.
The house works four surfaces (canon section XIII), and each one is read on its own line
with its source and its stamp:

| Surface | Source | Stamp |
| --- | --- | --- |
| The tree | `git rev-parse HEAD` and `VERSION` | the revision the gates measured |
| The gates | the suite's own tail | each gate's clean or FAILED line |
| The record | `python scripts/seat_record --read` | the last row's date and the streak |
| The release | the tag, the site, the changelog | the released version |

An unread surface is named unread, never zeroed, and no delta is taken across a changed
basis: a tree that moved between two reads is two reads, not one number. A room with
nothing in contact names the one block between the house and contact. A silent zero is
not a virtue, and a loss is never anonymous. A contact read is written render-safe as
canon section XXV requires, so no renderer can pair two characters into a formula the
record never wrote.

## 9. Close

The stand-down is the floor, never the ceiling. With something rankable, rank it. With
nothing rankable, say the sentence and stop. The board never posts a number it cannot
check.
