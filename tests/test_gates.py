"""Gate self-tests: every maintenance gate must pass clean and fail closed.

The happy paths run against the live checkout, read-only: each script exits 0
with its clean line. The failure modes run against one throwaway copy of the
tree (the fixture): a case mutates exactly one thing, asserts exit 1 plus the
failure it named, and restores the file so cases cannot contaminate each other.
Nothing here writes to the live tree.
"""

from __future__ import annotations

import contextlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Callable, Iterator

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
FIXTURE: Path | None = None


def setUpModule() -> None:
    global FIXTURE
    tmp = Path(tempfile.mkdtemp(prefix="animestack-gates-"))
    FIXTURE = tmp / "repo"
    shutil.copytree(
        REPO, FIXTURE, ignore=shutil.ignore_patterns(".git"), symlinks=True
    )


def tearDownModule() -> None:
    global FIXTURE
    if FIXTURE is not None:
        shutil.rmtree(FIXTURE.parent, ignore_errors=True)
        FIXTURE = None


def run_gate(script: str, *args: str, root: Path | None = None) -> subprocess.CompletedProcess:
    command = [sys.executable, str(SCRIPTS / script)]
    if root is not None:
        command += ["--root", str(root)]
    command += list(args)
    return subprocess.run(command, capture_output=True, text=True, timeout=300)


@contextlib.contextmanager
def mutated(path: Path, transform: Callable[[str], str]) -> Iterator[None]:
    original = path.read_bytes()
    try:
        text = path.read_text(encoding="utf-8")
        path.write_text(transform(text), encoding="utf-8")
        yield
    finally:
        path.write_bytes(original)


class GateHappyPathTests(unittest.TestCase):
    def test_every_gate_is_clean_on_the_live_tree(self) -> None:
        cases = (
            ("gen-agent-dialects", ("--check",), "in sync"),
            ("check-lore-consistency", (), "clean"),
            ("check-board", (), "clean"),
            ("check-contract", (), "clean"),
            ("check-measurement", ("--check-doc",), "clean"),
            ("check-voices", (), "clean"),
            ("check-digest", (), "clean"),
        )
        for script, args, marker in cases:
            with self.subTest(script=script):
                proc = run_gate(script, *args)
                self.assertEqual(
                    proc.returncode,
                    0,
                    msg="%s\n%s" % (proc.stdout, proc.stderr),
                )
                self.assertIn(marker, proc.stdout)

    def test_every_gate_is_clean_on_the_fixture_root(self) -> None:
        assert FIXTURE is not None
        cases = (
            ("gen-agent-dialects", ("--check",), "in sync"),
            ("check-lore-consistency", (), "clean"),
            ("check-board", (), "clean"),
            ("check-contract", (), "clean"),
            ("check-measurement", ("--check-doc",), "clean"),
            ("check-voices", (), "clean"),
            ("check-digest", (), "clean"),
        )
        for script, args, marker in cases:
            with self.subTest(script=script):
                proc = run_gate(script, *args, root=FIXTURE)
                self.assertEqual(
                    proc.returncode,
                    0,
                    msg="%s\n%s" % (proc.stdout, proc.stderr),
                )
                self.assertIn(marker, proc.stdout)


class GenAgentDialectsTests(unittest.TestCase):
    def test_body_drift_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "agents" / "cursor" / "animestack-reika.md"
        with mutated(target, lambda text: text + "\ndrift\n"):
            proc = run_gate("gen-agent-dialects", "--check", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("drift", proc.stdout)
        self.assertIn("animestack-reika.md", proc.stdout)

    def test_missing_dialect_file_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "agents" / "kiro" / "animestack-elo.md"
        original = target.read_bytes()
        try:
            target.unlink()
            proc = run_gate("gen-agent-dialects", "--check", root=FIXTURE)
        finally:
            target.write_bytes(original)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("missing", proc.stdout)

    def test_extra_dialect_file_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "agents" / "cursor" / "zzz-extra.md"
        try:
            target.write_text("---\nname: zzz\n---\n", encoding="utf-8")
            proc = run_gate("gen-agent-dialects", "--check", root=FIXTURE)
        finally:
            target.unlink(missing_ok=True)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("extra", proc.stdout)


class LoreConsistencyTests(unittest.TestCase):
    def test_dropped_credential_key_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "agents" / "opencode" / "animestack-mei.md"
        with mutated(target, lambda text: text.replace("art: ", "artX: ", 1)):
            proc = run_gate("check-lore-consistency", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("missing 'art:", proc.stdout)

    def test_rotted_path_pointer_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "CLAUDE.md"
        with mutated(target, lambda text: text.replace("docs/measurement.md", "docs/measurementX.md")):
            proc = run_gate("check-lore-consistency", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("path missing: docs/measurementX.md", proc.stdout)


class BoardTests(unittest.TestCase):
    def test_unresolvable_anchor_phrase_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "docs" / "board.md"

        def break_phrase(text: str) -> str:
            return re.sub(
                r"(\[source:\s*[^:\]]+::\s*)([^\]]+)(\])",
                r"\1zzz does not exist \2\3",
                text,
                count=1,
            )

        with mutated(target, break_phrase):
            proc = run_gate("check-board", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("anchor not found", proc.stdout)

    def test_malformed_key_line_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "docs" / "board.md"
        with mutated(target, lambda text: text.replace("[source:", "[sourceX:", 1)):
            proc = run_gate("check-board", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("missing key line", proc.stdout)

    def test_count_path_is_clean(self) -> None:
        proc = run_gate("check-board", "--count")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("98 questions", proc.stdout)


class ContractTests(unittest.TestCase):
    def test_model_pin_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "agents" / "cursor" / "animestack-yui.md"
        with mutated(target, lambda text: text.replace("name:", "model: test-pin\nname:", 1)):
            proc = run_gate("check-contract", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("must omit the model key", proc.stdout)

    def test_lost_ownership_marker_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "agents" / "claude" / "animestack-rin.md"
        with mutated(target, lambda text: text.replace("<!-- animestack-owned -->", "<!-- not-owned -->")):
            proc = run_gate("check-contract", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("last line is not the ownership marker", proc.stdout)


class MeasurementTests(unittest.TestCase):
    def test_doc_count_mismatch_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "docs" / "measurement.md"
        with mutated(target, lambda text: text.replace("| 12 | laws |", "| 13 | laws |", 1)):
            proc = run_gate("check-measurement", "--check-doc", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("laws: doc says 13", proc.stdout)


class VoicesTests(unittest.TestCase):
    def test_sentence_bleed_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "docs" / "seats" / "mei.md"
        with mutated(
            target,
            lambda text: text + '\n\n"What are we building, in one sentence?"\n',
        ):
            proc = run_gate("check-voices", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("bleeds", proc.stdout)

    def test_rewritten_sentence_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "voices" / "house.json"
        with mutated(
            target,
            lambda text: text.replace(
                "What change in the world makes this obsolete?",
                "What change NOW?",
                1,
            ),
        ):
            proc = run_gate("check-voices", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("one sentence missing", proc.stdout)


class DigestTests(unittest.TestCase):
    def test_loop_row_out_of_order_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "AGENTS.md"
        with mutated(target, lambda text: text.replace("| 3 | Yui |", "| 8 | Yui |", 1)):
            proc = run_gate("check-digest", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("Yui sits at row 8", proc.stdout)

    def test_stale_count_claim_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "CLAUDE.md"
        with mutated(target, lambda text: text.replace("twelve", "thirteen", 1)):
            proc = run_gate("check-digest", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("thirteen playbooks", proc.stdout)

    def test_version_sample_mismatch_fails_closed(self) -> None:
        assert FIXTURE is not None
        target = FIXTURE / "docs" / "measurement.md"
        version = (FIXTURE / "VERSION").read_text(encoding="utf-8").strip()
        with mutated(target, lambda text: text.replace("`v%s`" % version, "`v9.9.9`", 1)):
            proc = run_gate("check-digest", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("sample says v9.9.9", proc.stdout)


if __name__ == "__main__":
    unittest.main()
