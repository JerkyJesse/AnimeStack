"""The zero-leak gate's red-once suite: every refusal watched before it is trusted.

Each case builds a throwaway checkout - a rulebook, one clean document, and
nothing else - so a case adds exactly the one thing it is about. The live tree is
never mutated and never asserted clean: the known open reds belong to the
regeneration lanes, and a test that pins them would have to be deleted when they
close.

The sealed literals in these fixtures are synthetic. A test that carried a real
token would be the leak it exists to catch.

Run: python -m pytest tests/test_leak_gate.py -q
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "check-leak"
RULEBOOK = REPO / "security" / "leak-patterns.txt"

# Synthetic sealed literals: they exist only in the fixtures.
SEALED_ONE = "ALPHA-SECRET-ONE"
SEALED_TWO = "BETA-SECRET-TWO"


def shape(*parts: str) -> str:
    """A synthetic pattern-shaped token, assembled so this file does not match
    the rule it tests. A test source that carries the literal its own gate
    forbids is the leak wearing a lab coat."""
    return "".join(parts)


CHANNEL_SHAPE = shape("HOUSE_ARIA_", "URL")


def run_gate(root: Path, *args: str, sealed: Path | None = None, tokens: str | None = None):
    environment = dict(os.environ)
    environment.pop("LEAK_TOKENS", None)
    if tokens is not None:
        environment["LEAK_TOKENS"] = tokens
    command = [sys.executable, str(SCRIPT), "--root", str(root)]
    if sealed is not None:
        command += ["--sealed", str(sealed)]
    command += list(args)
    return subprocess.run(command, capture_output=True, text=True, timeout=300, env=environment)


def write_tokens(path: Path, *literals: str) -> Path:
    path.write_text("\n".join(literals) + "\n", encoding="utf-8")
    return path


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-c", "user.email=fixture@example.invalid", "-c", "user.name=fixture", *args],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=300,
    )


def make_repo(root: Path, *, with_manifest: bool = False) -> Path:
    """A tiny clean checkout: the live rulebook, one doc, one seat name."""
    (root / "security").mkdir(parents=True)
    (root / "docs").mkdir()
    (root / "docs" / "seats").mkdir()
    shutil.copy(RULEBOOK, root / "security" / "leak-patterns.txt")
    (root / "docs" / "measurement.md").write_text(
        "# Measurement\n\nThe claim is pre-registered in §5 and read again in §2.\n",
        encoding="utf-8",
    )
    (root / "docs" / "seats" / "mechapip.md").write_text(
        "# MechaPip\n\nThe machine seat answers the pattern question, and nothing else.\n",
        encoding="utf-8",
    )
    (root / "README.md").write_text(
        "A portable eight-seat design house. The room answers, the record decides.\n",
        encoding="utf-8",
    )
    if with_manifest:
        (root / "art").mkdir()
        (root / "art" / "card.jpg").write_bytes(b"\xff\xd8\xff\xe0fixture\xff\xd9")
        (root / "assets").mkdir()
        (root / "assets" / "REVIEW.md").write_text(
            "# Asset review manifest\n\n| File | sha256 | Reviewer | Date | Verdict |\n"
            "| --- | --- | --- | --- | --- |\n",
            encoding="utf-8",
        )
    return root


class LeakGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="animestack-leak-"))
        self.root = make_repo(self.tmp / "repo")
        self.tokens = write_tokens(self.tmp / "tokens.txt", SEALED_ONE)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    # -- the clean case -----------------------------------------------------

    def test_clean_tree_passes_and_section_refs_do_not_trip(self) -> None:
        proc = run_gate(self.root)
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("check-leak: clean", proc.stdout)
        self.assertIn("§5", (self.root / "docs" / "measurement.md").read_text(encoding="utf-8"))

    def test_seat_name_does_not_trip(self) -> None:
        (self.root / "docs" / "seats" / "mechapip.md").write_text(
            "# MechaPip\n\nThe seat is named MechaPip in every dialect and every page.\n",
            encoding="utf-8",
        )
        proc = run_gate(self.root)
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)

    # -- the sealed tier ----------------------------------------------------

    def test_sealed_literal_in_markdown_fails_with_file_and_line(self) -> None:
        target = self.root / "docs" / "notes.md"
        target.write_text("# Notes\n\nthe %s leaked\n" % SEALED_ONE, encoding="utf-8")
        proc = run_gate(self.root, sealed=self.tokens)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("docs/notes.md:3: sealed", proc.stdout)

    def test_sealed_literal_in_image_bytes_fails(self) -> None:
        figure = self.root / "docs" / "figure.jpg"
        figure.write_bytes(b"\xff\xd8\xff\xe0\x00" + SEALED_ONE.encode() + b"\xff\xd9")
        proc = run_gate(self.root, sealed=self.tokens)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("docs/figure.jpg:byte", proc.stdout)

    def test_sealed_literal_in_filename_fails(self) -> None:
        (self.root / "docs" / ("%s.md" % SEALED_ONE)).write_text("clean body\n", encoding="utf-8")
        proc = run_gate(self.root, sealed=self.tokens)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("%s.md:1: sealed (path)" % SEALED_ONE, proc.stdout)

    def test_sealed_literal_in_claims_and_patterns_fail(self) -> None:
        (self.root / "claims").mkdir()
        (self.root / "claims" / "claim-900.md").write_text("%s\n" % SEALED_TWO, encoding="utf-8")
        (self.root / "patterns").mkdir()
        (self.root / "patterns" / "registry.json").write_text(
            '{"entries": [{"id": "P-001", "note": "%s"}]}\n' % SEALED_TWO, encoding="utf-8"
        )
        tokens = write_tokens(self.tmp / "tokens-2.txt", SEALED_TWO)
        proc = run_gate(self.root, sealed=tokens)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("claims/claim-900.md:1: sealed", proc.stdout)
        self.assertIn("patterns/registry.json:1: sealed", proc.stdout)

    # -- the pattern tier ---------------------------------------------------

    def test_pattern_shape_in_a_generated_seat_pack_fails(self) -> None:
        (self.root / "dsh" / "animestack-team").mkdir(parents=True)
        (self.root / "dsh" / "animestack-team" / "animestack-rin.md").write_text(
            "Channel: `%s`\n" % CHANNEL_SHAPE, encoding="utf-8"
        )
        proc = run_gate(self.root)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("dsh/animestack-team/animestack-rin.md:1: rule:channel-env", proc.stdout)

    def test_rulebook_with_no_rules_fails_closed(self) -> None:
        (self.root / "security" / "leak-patterns.txt").write_text("# empty\n", encoding="utf-8")
        proc = run_gate(self.root)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("no rules", proc.stdout)

    # -- the sealed requirement ---------------------------------------------

    def test_absent_sealed_tier_is_named_unread(self) -> None:
        proc = run_gate(self.root)
        self.assertIn("sealed: unread", proc.stdout)

    def test_absent_sealed_tier_fails_when_required(self) -> None:
        proc = run_gate(self.root, "--sealed-required")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("sealed: required but absent", proc.stdout)

    def test_token_file_inside_the_tree_is_refused(self) -> None:
        inside = write_tokens(self.root / "docs" / "tokens.txt", SEALED_ONE)
        proc = run_gate(self.root, sealed=inside)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("token file is inside the tree", proc.stdout)

    # -- history ------------------------------------------------------------

    def test_literal_in_a_commit_fails_history(self) -> None:
        self.assertEqual(git(self.root, "init", "-q").returncode, 0)
        (self.root / "docs" / "history.md").write_text("a %s line\n" % SEALED_ONE, encoding="utf-8")
        self.assertEqual(git(self.root, "add", "-A").returncode, 0)
        self.assertEqual(git(self.root, "commit", "-qm", "fixture with a literal").returncode, 0)
        proc = run_gate(self.root, "--history", sealed=self.tokens)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("history:", proc.stdout)
        self.assertIn("1 revision(s)", proc.stdout)

    def test_shallow_clone_fails_history_closed(self) -> None:
        # A `--depth 1` checkout leaves `.git/shallow` behind; the case writes
        # the same marker directly so it needs no network and no clone.
        source = self.root
        self.assertEqual(git(source, "init", "-q").returncode, 0)
        self.assertEqual(git(source, "add", "-A").returncode, 0)
        self.assertEqual(git(source, "commit", "-qm", "fixture").returncode, 0)
        head = git(source, "rev-parse", "HEAD")
        self.assertEqual(head.returncode, 0, msg=head.stderr)
        (source / ".git" / "shallow").write_text(head.stdout.strip() + "\n", encoding="ascii")
        proc = run_gate(source, "--history", sealed=self.tokens)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("history: unread (shallow clone", proc.stdout)

    # -- the asset manifest -------------------------------------------------

    def test_manifest_row_hash_must_match_the_file(self) -> None:
        root = make_repo(self.tmp / "manifest", with_manifest=True)
        proc = run_gate(root)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("art/card.jpg: no review row", proc.stdout)
        digest = "0" * 64
        (root / "assets" / "REVIEW.md").write_text(
            "# Asset review manifest\n\n| File | sha256 | Reviewer | Date | Verdict |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| `art/card.jpg` | `%s` | nobody | 2026-11-05 | UNREVIEWED |\n" % digest,
            encoding="utf-8",
        )
        proc = run_gate(root)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("art/card.jpg: sha256 mismatch", proc.stdout)

    def test_unresolved_hold_fails_the_release_run(self) -> None:
        root = make_repo(self.tmp / "hold", with_manifest=True)
        import hashlib

        digest = hashlib.sha256((root / "art" / "card.jpg").read_bytes()).hexdigest()
        (root / "assets" / "REVIEW.md").write_text(
            "# Asset review manifest\n\n| File | sha256 | Reviewer | Date | Verdict |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| `art/card.jpg` | `%s` | seat | 2026-11-05 | HOLD |\n" % digest,
            encoding="utf-8",
        )
        tree = run_gate(root)
        self.assertEqual(tree.returncode, 0, msg=tree.stdout + tree.stderr)
        self.assertIn("1 hold(s)", tree.stdout)
        self.assertEqual(git(root, "init", "-q").returncode, 0)
        self.assertEqual(git(root, "add", "-A").returncode, 0)
        self.assertEqual(git(root, "commit", "-qm", "fixture").returncode, 0)
        release = run_gate(root, "--history", sealed=self.tokens)
        self.assertEqual(release.returncode, 1, msg=release.stdout + release.stderr)
        self.assertIn("hold(s) unresolved at release", release.stdout)


if __name__ == "__main__":
    unittest.main()
