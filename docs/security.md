# Security: the zero-leak gate

The pack is public. Nothing from the private reference repository may cross into
it: no name, path, ticker, venue, strategy, money unit, credential, fleet, desk,
ledger number, channel variable, or record number. That boundary is not a habit
and not a review note. It is `scripts/check-leak`, and it is the gate every other
gate is a special case of.

## 1. What runs

```
python scripts/check-leak --tree                     # every push
python scripts/check-leak --sealed-required --history # release
```

`--tree` is the default. `--history` adds the git history, and it is the release
gate. Both are read-only, stdlib only, and never touch the network.

Exit `0` clean; `1` a hit, an unreadable history, a required tier that is absent,
or an asset manifest that does not account for the tree; `2` usage.

The gate scans tracked files plus untracked, non-ignored files, and every path:
bytes for binary files, lines for text, path strings for both. `--history` scans
every reachable revision's full patch stream (which carries each tree's added
lines, including a root commit's entire content), every commit message, every
historical path, and - when the sealed tier is present - `git grep` over every
revision so binary blobs are included too.

## 2. The two tiers

A rulebook is a liability if it spells what it forbids. This gate keeps the
rulebook and the facts apart.

**The pattern tier** is `security/leak-patterns.txt`, public by design. One rule
per line: `rule-id`, a tab, a Python regular expression. The rules are *shapes* a
later commit could reintroduce - a series identifier, a guard variable, a channel
variable, a machine home path, an upper-case ledger filename, a chat platform, a
decimal money figure, a credential file. A shape names no fact. The rulebook
counts as a measurement row (`docs/measurement.md`, floor of one rule) because a
gate with no rule cannot fail.

**The sealed tier** is never committed. The literal tokens of the private
reference arrive as base64 in `LEAK_TOKENS` (a CI repository secret) or as a
`--sealed <file>` outside the tree. A literal pasted into this repository is the
leak the tier exists to catch, so the gate refuses a token file that resolves
inside the checkout: `sealed: the token file is inside the tree`.

When the sealed tier is absent, the gate says so - `sealed: unread (no
LEAK_TOKENS, no --sealed)` - and a run with `--sealed-required` exits `1`. A fork
pull request has no secret and prints `sealed: unread`; it never prints a clean
zero for a tier it could not read. The house's own workflow requires the tier on
every push to the default branch.

The rulebook itself is scanned by the sealed tier only: a pattern rule matching
its own source text is noise, but a literal pasted among the rules is a leak.

## 3. The asset class

No text gate reads pixels. A name, a path, a ticker, a money figure, or a channel
burned into a render is invisible to every scanner here, so the asset class has
its own instrument: `assets/REVIEW.md`, one row per file under `art/` and
`assets/` with path, sha256, reviewer, date, and verdict.

The machine checks the facts: every shipped file has exactly one row, every row
names a file, every sha256 matches the bytes, and every verdict is `PASS`,
`HOLD`, or `UNREVIEWED`. The human checks the picture. `UNREVIEWED` is named in
every run and is never counted as a pass; `HOLD` fails the release run until the
chair resolves it - regenerate the render, or accept it on the record and flip
the verdict with a date.

## 4. The history

The tree is the easy case. The history is the one that keeps leaking after a
rewrite, because the company a repository keeps is every blob it ever wrote.

The gate treats an unreadable history as a failure, not a pass: a shallow clone
cannot see history, so `--history` exits `1` with `history: unread (shallow
clone; a history gate needs the full graph - fetch-depth 0)`. CI must check out
with `fetch-depth: 0`. An unread history is named, never zeroed.

At the v2.0.0 build the live history is **not clean**: 38 revisions, hundreds of
pattern hits, concentrated in the releases before the first public rewrite. That
is a fact, not a backlog item.

### The rewrite (a force-class act)

The chair signs this; the build seat does not. It is one act, in this order:

1. Choose the last tree that is clean under `--sealed-required --history` (the
   release whose rewrite removed the private material). Take that tree as a new
   root: `git commit-tree <tree> -m "<the release message>"`.
2. Replay every commit after it onto the new root: `git rebase --onto <new-root>
   <old-release> main`. Because the new root's tree is byte-identical to the
   old release tree, every later patch applies unchanged. Fallback with no
   external tooling: `git replace --graft <old-release>` to make it a root, then
   `git filter-branch -- --all` to bake the graft in.
3. The lineage before that release is dropped, not scrubbed: those commits *are*
   the leak. Losing them loses release lore, not release truth.
4. Force-push with `--force-with-lease`. This is the force-class step.

### What proves it

The working checkout is not the proof: a rewritten branch leaves the old blobs
unreachable-but-present until reflog expiry. The proof is a fresh clone of the
rewritten remote, because a clone fetches only reachable objects:

```
git clone --no-local <remote> /tmp/proof && cd /tmp/proof
python scripts/check-leak --sealed-required --history    # 0 hits, exit 0
git log --all -p --format='%H %s' | grep -Eci '<rule set and literals>'  # 0
```

Then, in the house checkout, `git reflog expire --expire=now --all` and
`git gc --prune=now` so an archive of the working directory cannot carry the old
objects either.

**The residual, named.** A rewrite does not retract what was already fetched. Any
clone, fork, mirror, or cached page that read the repository before the rewrite
keeps the copy; a hosting provider may keep unreachable objects addressable by
their old identifiers. The rewrite removes the *future* copy. It does not remove
the *past* exposure, and no report may say it did.

## 5. CI

In `.github/workflows/gate.yml`, checkout must carry history and the release run
must require the sealed tier:

```
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - run: python scripts/check-leak --tree
      - run: python scripts/check-leak --sealed-required --history
        env:
          LEAK_TOKENS: ${{ secrets.LEAK_TOKENS }}
```

The tree run is cheap and runs on every push and pull request. The history run is
the release gate; without `fetch-depth: 0` it fails closed by design.

## 6. Limits

A gate is a claim about what it can see. These are the edges:

- **Prose.** A paraphrase carries no token: a sentence describing the private
  book in ordinary words passes. The pattern tier catches shapes, the sealed tier
  catches literals, and a reviewer catches the rest.
- **Pixels.** Covered by the manifest and a human, never by a scan.
- **Encodings.** A token base64-encoded, hex-encoded, or split across lines is
  not caught. The tier matches text.
- **Outside the tree.** Repository description, topics, release notes, pull
  request bodies, and hosting settings are not files. The gate cannot see them;
  they are reviewed by hand at release.
- **Reachable refs.** History mode reads `git rev-list --all`. A ref deleted
  before the run is unreachable and therefore invisible - which is why the proof
  is a fresh clone and why the rewrite is done once, in the open.

## 7. The red-first rule

Every rule and every mode has a case in `tests/test_leak_gate.py` that watches it
fail before it is trusted: a token in a markdown body, in an image's bytes, in a
filename, in a generated seat pack, in a claim card, in the pattern registry, and
in a commit; a clean tree where `§5` and a seat name must not trip; a shallow
clone and an absent required tier that must both exit `1`.

A rule that cannot be made to fail is deleted. A gate that has never been red is
a rumor with a green line.
