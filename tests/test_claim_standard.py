"""The claim standard's red-once suite: every refusal watched before it is trusted.

The cases run against a synthetic checkout - `claims/`, `patterns/registry.json`,
and the two files a receipt can resolve - so a case mutates exactly one thing and
the live tree is never touched. The clean case runs the live cards.

Run: python -m pytest tests/test_claim_standard.py -q
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "check-claim"

GOOD_CARD = """# claim-900 — the fixture claim

```yaml
id: claim-900
claim: The fixture claim asserts one sentence the gate can check.
failure: The fixture failure is a red first sample with no card.
mechanism: docs/measurement.md:3
sample: three fixture cases, run on 2026-11-05; floor three cases, stated before the run.
control: the same fixture with the change stripped, which did not reproduce.
halves: formed=green (the fixture watched red first); fresh=green (the fixture run)
falsifier: If the fixture cannot fail, the fixture is decoration.
carved: 2026-11-05
receipt: python scripts/check-claim --check
disposition: SHIP pattern=P-001
```
"""


def make_repo(root: Path) -> Path:
    (root / "claims").mkdir(parents=True)
    (root / "docs").mkdir()
    (root / "scripts").mkdir()
    (root / "patterns").mkdir()
    (root / "docs" / "measurement.md").write_text(
        "\n".join("measurement line %d" % index for index in range(1, 201)) + "\n",
        encoding="utf-8",
    )
    (root / "scripts" / "check-claim").write_text("#!/usr/bin/env python3\n", encoding="utf-8")
    (root / "patterns" / "registry.json").write_text(
        json.dumps(
            {
                "entries": [
                    {"id": "P-001", "name": "the unseated memory"},
                    {"id": "P-005", "name": "the unbacked number"},
                ]
            }
        ),
        encoding="utf-8",
    )
    (root / "claims" / "claim-900-the-fixture.md").write_text(GOOD_CARD, encoding="utf-8")
    return root


class ClaimStandardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="animestack-claim-"))
        self.root = make_repo(self.tmp / "repo")
        self.card = self.root / "claims" / "claim-900-the-fixture.md"

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_gate(self, *args: str) -> subprocess.CompletedProcess:
        command = [sys.executable, str(SCRIPT), *args, "--root", str(self.root)]
        return subprocess.run(command, capture_output=True, text=True, timeout=120)

    def mutate(self, old: str, new: str) -> None:
        text = self.card.read_text(encoding="utf-8")
        self.assertIn(old, text)
        self.card.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_clean_fixture_passes(self) -> None:
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("check-claim: clean (1 cards", proc.stdout)

    def test_missing_falsifier_fails_closed(self) -> None:
        text = self.card.read_text(encoding="utf-8")
        self.card.write_text(
            "\n".join(line for line in text.splitlines() if not line.startswith("falsifier:")),
            encoding="utf-8",
        )
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("missing or empty field: falsifier", proc.stdout)

    def test_carved_after_sample_fails_closed(self) -> None:
        self.mutate("carved: 2026-11-05", "carved: 2026-11-06")
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("after the sample", proc.stdout)

    def test_red_half_marked_ship_fails_closed(self) -> None:
        self.mutate("fresh=green (the fixture run)", "fresh=red (the fixture run)")
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("SHIP with a fresh half", proc.stdout)

    def test_park_without_review_fails_closed(self) -> None:
        self.mutate("disposition: SHIP pattern=P-001", "disposition: PARK pattern=P-001")
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("PARK with no review", proc.stdout)

    def test_retire_without_counted_refusal_fails_closed(self) -> None:
        self.mutate(
            "disposition: SHIP pattern=P-001",
            "disposition: RETIRE pattern=P-001",
        )
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("RETIRE with no refusal", proc.stdout)

    def test_control_is_the_mechanism_fails_closed(self) -> None:
        self.mutate(
            "control: the same fixture with the change stripped, which did not reproduce.",
            "control: docs/measurement.md:3",
        )
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("control is identical to the mechanism", proc.stdout)

    def test_thin_quoting_a_result_fails_closed(self) -> None:
        self.mutate(
            "disposition: SHIP pattern=P-001",
            "disposition: THIN pattern=P-001",
        )
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("THIN quotes a result", proc.stdout)

    def test_dead_receipt_path_fails_closed(self) -> None:
        self.mutate(
            "receipt: python scripts/check-claim --check",
            "receipt: docs/missing.md",
        )
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("receipt path does not resolve", proc.stdout)

    def test_hymn_token_fails_closed(self) -> None:
        text = self.card.read_text(encoding="utf-8")
        self.card.write_text(text + "\n\nThis obviously works.\n", encoding="utf-8")
        proc = self.run_gate("--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("hymn token", proc.stdout)

    def test_count_and_list_modes(self) -> None:
        count = self.run_gate("--count")
        self.assertEqual(count.returncode, 0, msg=count.stdout + count.stderr)
        self.assertEqual(count.stdout.strip(), "1")
        listing = self.run_gate("--list")
        self.assertEqual(listing.returncode, 0, msg=listing.stdout + listing.stderr)
        self.assertIn("claim-900", listing.stdout)
        self.assertIn("SHIP", listing.stdout)


if __name__ == "__main__":
    unittest.main()
