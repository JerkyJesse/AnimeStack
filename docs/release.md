# Release: the click

A release is a tag on a tree the gates have already passed. The tag is the
click; a red gate is a hold, never a bypass. This page is the checklist the
release seat runs, the proof the chair can re-run, and the rollback if the live
surface lies.

Nothing here is a permission gate. The team owns the release end to end; the
only human act left is the chair's signature on the art pass, and the
force-class history rewrite is the chair's call because it moves every
revision the public has.

## 1. Preflight (2 minutes)

```
git status --short                  # must be empty
git branch --show-current           # must be main
git tag -l                          # v2.0.0 must be absent before the tag
cat VERSION                         # 2.0.0
python scripts/check-digest         # release and canon revision agree everywhere
```

The release script refuses a dirty tree, a non-main branch, an existing tag,
and a `VERSION` that disagrees with the measurement sample.

## 2. The gate (the body)

Run from the repo root. Every command must exit 0 and print its clean line.

```
python scripts/gen-agent-dialects --check
python scripts/gen-dsh-house --check
python scripts/gen-site --check
python scripts/check-site
python scripts/check-lore-consistency
python scripts/check-board
python scripts/check-contract
python scripts/check-measurement --check-doc
python scripts/check-voices
python scripts/check-digest
python scripts/check-patterns
python scripts/check-claim --check
python scripts/seat_record --check
python scripts/room_scorecard --strict
python -m unittest discover -s tests -q
```

The installer dry run is part of the gate on both entry points:

```
bash setup --host all --check
powershell -ExecutionPolicy Bypass -File .\setup.ps1 -TargetHost all -Check
```

A red line stops the release. The release carries the command and its tail; a
claim without a tail is a hypothesis.

## 3. The leak gate (tree, every push; history, at release)

```
python scripts/check-leak --tree
python scripts/check-leak --sealed-required --history
```

The tree run scans every tracked and untracked file, every path, and the asset
manifest. The history run scans every reachable revision's patch stream, every
commit message, every historical path, and the sealed literals; it fails closed
on a shallow clone. The sealed tier comes from the `LEAK_TOKENS` repository
secret (base64 text, one token per line) or a `--sealed` file outside the tree.
No token value is ever written into the repository, this page, or a command
line in a log.

The history must be rebuilt clean before the tag. The rewrite is a force-class
act and the chair's call: every revision is rewritten with the token map, the
public branch is force-pushed with `--force-with-lease`, and the old revision
ids are named as unreachable. The proof is the second command above returning
`0 hits` over trees, diffs, messages, filenames, and binary blobs, on a fresh
clone, with `git rev-parse --is-shallow-repository` false. Old clones keep
whatever they fetched; no fork exists to chase, and the cached-object purge is
requested from the host after the push.

## 4. The site (generated, never hand-authored)

```
python scripts/gen-site --check      # every page matches its source
python scripts/check-site            # links, metadata, counts, leak boundary
```

Every page is rendered from the canon, the books, the board, the counts, the
record, the claim standard, the security page, the DSH surface, and the guide.
A page that claims a number the measurement lane cannot reproduce is a defect;
a page that links a markdown source is a defect; a page without its social
metadata is a defect. The page set is 27 pages; the sitemap and robots file are
generated in the same run.

The art pass is signed by the chair before the tag. `assets/REVIEW.md` carries
one row per picture; every row is `PASS`, and no row is `HOLD` or `UNREVIEWED`
at release. A picture the text gates cannot read is a human review, and the
review is named, never implied. The withheld renders are named in
`art/README.md` and are not shipped.

## 5. The tag and the publish

The window is the turn of the quarter hour: `:00`, `:15`, `:30`, `:45`. The
tag is annotated and carries the release line.

```
git tag -a v2.0.0 -m "AnimeStack v2.0.0 — the complete public house"
git push origin main
git push origin v2.0.0
gh release create v2.0.0 --title "AnimeStack v2.0.0 — the complete public house" \
  --notes-file CHANGELOG.md
```

`scripts/release 2.0.0 --publish` runs the same chain behind one command after
the gate and the leak gate are green. It prints each stage and stops at the
first red.

The Pages surface builds from `main` at the repository root (the host's legacy
build), so the push to `main` is the deploy. The tag is the release; it does not
deploy anything by itself.

## 6. Live verification (5 minutes)

Fetch the live pages as a stranger and check the stamp, the law count, and the
boundary:

```
https://animestack.jerkyjesse.com/
https://animestack.jerkyjesse.com/lore/canon.html
https://animestack.jerkyjesse.com/lore/board.html
https://animestack.jerkyjesse.com/lore/record.html
https://animestack.jerkyjesse.com/guide.html
https://animestack.jerkyjesse.com/sitemap.xml
```

Each page must return 200, show `v2.0.0` and `canon Rev 9`, show the fourteen
laws on the house page, and resolve every relative link. Record the URL, the
status, the revision printed by `git rev-parse HEAD`, and the time of the read.
An unread page is named unread, never counted as a pass.

The release run also checks that the tag's commit is the commit the gate
measured, and that `VERSION` equals the tag without the `v`.

## 7. Rollback

- **Bad page.** Revert the release commit on `main`; Pages rebuilds from the
  reverted tree. The tag stays as the record of what shipped; the revert is the
  correction.
- **Bad tree gate.** Delete nothing and rename nothing. Reopen the room with
  the failing tail; the release is held, not patched in the tag.
- **Bad tag.** A tag that has not been published can be deleted and re-cut after
  the gate is green. A published tag is never moved; a correction is a new
  version.
- **Bad art.** Restore the previous reviewed asset, re-run the asset manifest
  and `check-leak --tree`; a changed hash needs a new review row and a verdict.

## 8. NEVER

1. Never tag a tree with a red gate, a missing sealed tier, or an unresolved
   asset hold.
2. Never write a secret, a token value, or a key into this repository, the
   site, the changelog, or a command line that reaches a log. The sealed tier
   lives in the repository secret or a file outside the tree.
3. Never hand-edit a generated page, the generated DSH bundle, or the generated
   agent dialects. Edit the source, regenerate, and commit both trees.
4. Never move a published tag or rewrite a public revision without the chair's
   ruling, a clean rewrite proof, and a force-with-lease push.
5. Never publish a number the counts table cannot reproduce.
6. Never let a page link a page that has not landed.

## 9. The contact read (the whole surface)

Every release closes with the contact read, in the open, with stamps:

| Surface | Source | Stamp |
| --- | --- | --- |
| The tree | `git rev-parse HEAD` and `VERSION` | the revision the gates measured |
| The gates | the suite's own tail | each gate's clean or failed line |
| The record | `python scripts/seat_record --read` | the last row's date and the streak |
| The release | the tag, the site, the changelog | the released version and the live URL status |

An unread surface is named unread, never zeroed. A release with nothing in
contact names the one block between the house and contact. A silent zero is not
a virtue, and a loss is never anonymous.

The release is complete when the tag exists, the site verifies, the record
carries the entry, and every gate tail is in the decision log.
