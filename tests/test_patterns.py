"""Pattern and voice gates: every row resolves, every line resolves, both fail closed.

The happy paths run against the live checkout, read-only. The failure modes run
against one throwaway copy of the tree: a case mutates exactly one thing, asserts
exit 1 plus the failure it named, and restores the file so cases cannot
contaminate each other. Nothing here writes to the live tree.
"""

from __future__ import annotations

import contextlib
import json
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
    tmp = Path(tempfile.mkdtemp(prefix="animestack-patterns-"))
    FIXTURE = tmp / "repo"
    shutil.copytree(
        REPO,
        FIXTURE,
        ignore=shutil.ignore_patterns(
            ".git", ".pytest_cache", ".ruff_cache", "__pycache__", "art", "assets"
        ),
        symlinks=True,
    )


def tearDownModule() -> None:
    global FIXTURE
    if FIXTURE is not None:
        shutil.rmtree(FIXTURE.parent, ignore_errors=True)
        FIXTURE = None


def run_gate(
    script: str, *args: str, root: Path | None = None
) -> subprocess.CompletedProcess:
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


def fixture_file(*parts: str) -> Path:
    assert FIXTURE is not None
    return FIXTURE.joinpath(*parts)


class PatternHappyPathTests(unittest.TestCase):
    def test_check_patterns_clean_on_the_live_tree(self) -> None:
        proc = run_gate("check-patterns")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertRegex(proc.stdout, r"check-patterns: clean \(\d+ rows")
        self.assertIn("citations", proc.stdout)

    def test_check_voices_clean_on_the_live_tree(self) -> None:
        proc = run_gate("check-voices")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("check-voices: clean", proc.stdout)

    def test_every_registry_row_is_on_the_archive_page(self) -> None:
        data = json.loads(
            (REPO / "patterns" / "registry.json").read_text(encoding="utf-8")
        )
        page = (REPO / "docs" / "lore" / "ARCHIVE.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(len(data["entries"]), 16)
        for entry in data["entries"]:
            self.assertIn(entry["id"], page)
            self.assertIn(entry["name"], page)

    def test_every_seat_carries_the_register_floor(self) -> None:
        text = (REPO / "docs" / "lore" / "VOICE.md").read_text(encoding="utf-8")
        for display in ("Reika", "Mei", "Elo", "MechaPip", "Yui", "Niko", "Rin", "Aria"):
            section = text.split("## %s\n" % display, 1)
            self.assertEqual(len(section), 2, msg="missing section %s" % display)
            lines = [
                line for line in section[1].splitlines() if line.startswith('- "')
            ]
            self.assertGreaterEqual(
                len(lines), 4, msg="%s carries %d anchored lines" % (display, len(lines))
            )

    def test_count_and_show(self) -> None:
        count = run_gate("check-patterns", "--count")
        self.assertEqual(count.returncode, 0, msg=count.stdout + count.stderr)
        self.assertGreaterEqual(int(count.stdout.strip()), 16)
        show = run_gate("check-patterns", "--show", "P-002")
        self.assertEqual(show.returncode, 0, msg=show.stdout + show.stderr)
        self.assertIn("role-split agent files", show.stdout)
        self.assertIn("RETIRED", show.stdout)


class PatternFailureTests(unittest.TestCase):
    def test_row_without_a_sample_fails(self) -> None:
        target = fixture_file("patterns", "registry.json")

        def drop(text: str) -> str:
            data = json.loads(text)
            for entry in data["entries"]:
                if entry["id"] == "P-002":
                    del entry["sample"]
            return json.dumps(data, indent=2, ensure_ascii=False) + "\n"

        with mutated(target, drop):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("missing field(s): sample", proc.stdout)

    def test_duplicate_id_fails(self) -> None:
        target = fixture_file("patterns", "registry.json")

        def duplicate(text: str) -> str:
            data = json.loads(text)
            data["entries"][-1]["id"] = "P-001"
            return json.dumps(data, indent=2, ensure_ascii=False) + "\n"

        with mutated(target, duplicate):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("duplicate id", proc.stdout)

    def test_renamed_row_fails(self) -> None:
        # Nothing is renamed: a second row with an existing name is a new coat.
        target = fixture_file("patterns", "registry.json")

        def rename(text: str) -> str:
            data = json.loads(text)
            data["entries"][-1]["name"] = "Knight Capital"
            return json.dumps(data, indent=2, ensure_ascii=False) + "\n"

        with mutated(target, rename):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("duplicate name", proc.stdout)

    def test_anchor_out_of_range_fails(self) -> None:
        target = fixture_file("patterns", "registry.json")

        def break_anchor(text: str) -> str:
            data = json.loads(text)
            for entry in data["entries"]:
                if entry["id"] == "P-002":
                    entry["anchor"] = "docs/measurement.md:99999"
            return json.dumps(data, indent=2, ensure_ascii=False) + "\n"

        with mutated(target, break_anchor):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("anchor line out of range", proc.stdout)

    def test_unknown_anchor_host_fails(self) -> None:
        target = fixture_file("patterns", "registry.json")

        def swap_host(text: str) -> str:
            data = json.loads(text)
            for entry in data["entries"]:
                if entry["id"].startswith("A-"):
                    entry["anchor"] = "https://example.invalid/incident"
                    break
            return json.dumps(data, indent=2, ensure_ascii=False) + "\n"

        with mutated(target, swap_host):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("anchor host not on the public allowlist", proc.stdout)

    def test_dangling_citation_fails(self) -> None:
        target = fixture_file("docs", "lore", "ARCHIVE.md")

        with mutated(target, lambda text: text + "\nThe ghost row is P-999.\n"):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("unknown id: P-999", proc.stdout)

    def test_page_missing_a_row_name_fails(self) -> None:
        target = fixture_file("docs", "lore", "ARCHIVE.md")

        with mutated(
            target,
            lambda text: text.replace("the unbacked scene number", "a scene number"),
        ):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("absent from docs/lore/ARCHIVE.md", proc.stdout)

    def test_adopted_row_missing_from_canon_fails(self) -> None:
        target = fixture_file("docs", "lore", "canon.md")

        with mutated(target, lambda text: text.replace("Sarao (2010", "Navinder (2010", 1)):
            proc = run_gate("check-patterns", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("adopted name absent from canon XVI", proc.stdout)


class VoiceFailureTests(unittest.TestCase):
    def test_register_below_the_floor_fails(self) -> None:
        target = fixture_file("docs", "lore", "VOICE.md")

        def drop_line(text: str) -> str:
            lines = text.splitlines()
            drop_at = next(
                index
                for index, line in enumerate(lines)
                if line.startswith('- "Duty at speed."')
            )
            del lines[drop_at]
            return "\n".join(lines) + "\n"

        with mutated(target, drop_line):
            proc = run_gate("check-voices", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("floor 4", proc.stdout)

    def test_phrase_missing_from_its_source_fails(self) -> None:
        target = fixture_file("docs", "lore", "VOICE.md")

        with mutated(
            target,
            lambda text: text.replace(
                '- "Duty at speed." [source: docs/lore/canon.md]',
                '- "Duty at speed." [source: docs/lore/dossiers/mei.md]',
                1,
            ),
        ):
            proc = run_gate("check-voices", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("phrase not found", proc.stdout)

    def test_shared_phrase_fails(self) -> None:
        target = fixture_file("docs", "lore", "VOICE.md")

        with mutated(
            target,
            lambda text: text.replace(
                '- "Duty at speed." [source: docs/lore/canon.md]',
                '- "Craftsman-assassin." [source: docs/lore/canon.md]',
                1,
            ),
        ):
            proc = run_gate("check-voices", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("phrase shared by", proc.stdout)

    def test_bleed_into_another_dossier_fails(self) -> None:
        target = fixture_file("docs", "lore", "dossiers", "mei.md")

        with mutated(
            target,
            lambda text: text + "\nCowardice wearing process.\n",
        ):
            proc = run_gate("check-voices", root=FIXTURE)
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("bleeds into", proc.stdout)


class ArchiveLawTests(unittest.TestCase):
    def test_every_park_card_field_is_documented(self) -> None:
        page = (REPO / "docs" / "lore" / "ARCHIVE.md").read_text(encoding="utf-8")
        for field in (
            "Deleted path",
            "Review date",
            "Killing number",
            "Panel",
            "Anchor",
        ):
            self.assertIn(field, page)

    def test_registry_rows_carry_the_seven_fields(self) -> None:
        data = json.loads(
            (REPO / "patterns" / "registry.json").read_text(encoding="utf-8")
        )
        required = {
            "id",
            "name",
            "kind",
            "shape",
            "sample",
            "regime",
            "verdict",
            "killing",
            "killing_date",
            "anchor",
            "owner",
        }
        for entry in data["entries"]:
            missing = required - set(entry)
            self.assertFalse(missing, msg="%s missing %s" % (entry.get("id"), missing))
            self.assertGreaterEqual(len(entry["sample"]), 40, msg=entry["id"])


if __name__ == "__main__":
    unittest.main()
