"""Tests for the recorded house: scripts/seat_record and scripts/room_scorecard.

Fixture-based: every case runs against a throwaway root (the scripts' --root
test hook), never the live checkout. Red cases watch their own failure: a
refused write writes nothing; a tampered row, a dangling reference, and a
malformed entry each fail their gate with the expected exit code.
"""

from __future__ import annotations

import datetime
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"

GATE_CLEAN = """\
import sys
print("{name}: clean (1 checks)")
sys.exit(0)
"""

GATE_RED = """\
import sys
print("{name}: FAILED (1 issue(s))")
print("  - boom: the fixture gate went red")
sys.exit(1)
"""


def run_script(script: str, root: Path, *args: str) -> subprocess.CompletedProcess:
    command = [sys.executable, str(SCRIPTS / script), "--root", str(root)]
    command += [str(arg) for arg in args]
    return subprocess.run(
        command, capture_output=True, text=True, encoding="utf-8", timeout=300
    )


def utc_today() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


class RecordFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="animestack-record-"))
        self.root = self.tmp / "repo"
        (self.root / "record").mkdir(parents=True)
        self.record = self.root / "record" / "seat_record.jsonl"

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def read_rows(self) -> list[dict]:
        if not self.record.is_file():
            return []
        return [
            json.loads(line)
            for line in self.record.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def write_rows(self, rows: list[dict]) -> None:
        text = "".join(json.dumps(row, separators=(",", ":")) + "\n" for row in rows)
        self.record.write_text(text, encoding="utf-8")

    @staticmethod
    def day(offset: int) -> str:
        moment = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=offset)
        return moment.strftime("%Y-%m-%d")

    def row(self, kind: str, seat: str, delta: int, date: str, ref: str,
            note: str = "") -> dict:
        return {
            "ts": f"{date}T00:00:00Z", "date": date, "kind": kind,
            "seat": seat, "delta": delta, "ref": ref, "note": note,
        }


class SeatRecordTests(RecordFixture):
    def test_event_appends_and_read_round_trips(self) -> None:
        proc = run_script(
            "seat_record", self.root, "--event", "--seat", "Reika",
            "--kind", "note", "--ref", "open:test", "--note", "the seat record opens",
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("appended", proc.stdout)
        proc = run_script(
            "seat_record", self.root, "--event", "--seat", "Yui",
            "--kind", "ship", "--ref", "build:test",
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        rows = self.read_rows()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["kind"], "note")
        self.assertEqual(rows[0]["delta"], 0)
        self.assertEqual(rows[0]["seat"], "Reika")
        self.assertEqual(rows[0]["ref"], "open:test")
        self.assertEqual(rows[0]["note"], "the seat record opens")
        self.assertEqual(rows[1]["delta"], 1)
        self.assertEqual(rows[1]["note"], "")
        proc = run_script("seat_record", self.root, "--read")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        lines = proc.stdout.splitlines()
        reika = next(line for line in lines if line.strip().startswith("Reika"))
        yui = next(line for line in lines if line.strip().startswith("Yui"))
        self.assertIn("net +0", reika)
        self.assertIn("all-time +0", reika)
        self.assertIn("net +1", yui)
        self.assertIn("all-time +1", yui)
        # worst first: the +0 seat rows above the +1 seat
        self.assertLess(lines.index(reika), lines.index(yui))

    def test_read_window_filter_and_worst_first(self) -> None:
        today = utc_today()
        self.write_rows([
            self.row("ship", "Mei", 1, "2020-01-01", "old:ship"),
            self.row("stub", "Mei", -1, today, "new:stub"),
            self.row("stub", "Elo", -1, today, "elo:stub:1"),
            self.row("code_red", "Elo", -1, today, "elo:stub:2"),
            self.row("ship", "Yui", 1, today, "yui:ship:1"),
            self.row("ship", "Yui", 1, today, "yui:ship:2"),
            self.row("ship", "Yui", 1, today, "yui:ship:3"),
            self.row("code_red", "Rin", -1, today, "rin:red"),
        ])
        proc = run_script("seat_record", self.root, "--read", "--window", "7")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        lines = [line for line in proc.stdout.splitlines() if line.startswith("  ")]
        order = [line.strip().split()[0] for line in lines]
        self.assertEqual(
            order, ["Elo", "Mei", "Rin", "MechaPip", "Niko", "Aria", "Reika", "Yui"]
        )
        elo = next(line for line in lines if line.strip().startswith("Elo"))
        self.assertIn("net -2", elo)
        mei = next(line for line in lines if line.strip().startswith("Mei"))
        self.assertIn("net -1", mei)
        self.assertIn("(credit 0 / debt 1)", mei)
        self.assertIn("all-time +0", mei)  # the 2020 ship is outside the window
        proc = run_script("seat_record", self.root, "--read", "--window", "10000")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        lines = [line for line in proc.stdout.splitlines() if line.startswith("  ")]
        mei = next(line for line in lines if line.strip().startswith("Mei"))
        self.assertIn("net +0", mei)  # the wide window holds both rows

    def test_read_names_the_streak(self) -> None:
        today = self.day(0)
        yesterday = self.day(1)
        self.write_rows([
            self.row("green_day", seat, 1, yesterday, "day:yesterday:green")
            for seat in ("Mei", "Elo", "MechaPip", "Yui", "Niko", "Rin", "Aria", "Reika")
        ] + [
            self.row("green_day", seat, 1, today, "day:today:green")
            for seat in ("Mei", "Elo", "MechaPip", "Yui", "Niko", "Rin", "Aria", "Reika")
        ])
        proc = run_script("seat_record", self.root, "--read")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("streak 2", proc.stdout)
        self.assertIn("last green day %s" % today, proc.stdout)

    def test_tiers_move_on_counted_evidence(self) -> None:
        today = self.day(0)
        rows = []
        for _ in range(3):
            rows.append(self.row("ship", "Mei", 1, today, "mei:ship"))
        for _ in range(5):
            rows.append(self.row("ship", "Elo", 1, today, "elo:ship"))
        for _ in range(3):
            rows.append(self.row("code_red", "Rin", -1, today, "rin:red"))
        for _ in range(5):
            rows.append(self.row("code_red", "Niko", -1, today, "niko:red"))
        self.write_rows(rows)
        proc = run_script("seat_record", self.root, "--read")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        lines = {line.strip().split()[0]: line for line in proc.stdout.splitlines()
                 if line.startswith("  ") and line.strip()}
        self.assertIn("[first claim]", lines["Mei"])
        self.assertIn("[the floor]", lines["Elo"])
        self.assertIn("[audit]", lines["Rin"])
        self.assertIn("[bar again]", lines["Niko"])

    def test_read_names_an_empty_record(self) -> None:
        self.record.write_text("", encoding="utf-8")
        proc = run_script("seat_record", self.root, "--read")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("0 row(s)", proc.stdout)
        self.assertIn("[no rows]", proc.stdout)


class SeatRecordChecksTests(RecordFixture):
    GATES = (
        "gen-agent-dialects", "check-contract", "check-lore-consistency",
        "check-board", "check-measurement", "check-digest", "check-voices",
    )

    def make_gates(self, red: str) -> None:
        scripts = self.root / "scripts"
        scripts.mkdir()
        for name in self.GATES:
            body = GATE_RED if name == red else GATE_CLEAN
            (scripts / name).write_text(body.format(name=name), encoding="utf-8")

    def test_checks_books_red_and_green_deduped(self) -> None:
        self.make_gates(red="check-board")
        proc = run_script("seat_record", self.root, "--checks")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        rows = self.read_rows()
        self.assertEqual(len(rows), 7)
        reds = [row for row in rows if row["kind"] == "code_red"]
        greens = [row for row in rows if row["kind"] == "check_green"]
        self.assertEqual(len(reds), 1)
        self.assertEqual(len(greens), 6)
        red = reds[0]
        self.assertEqual(red["seat"], "Elo")
        self.assertEqual(red["ref"], "check:check-board")
        self.assertEqual(red["delta"], -1)
        self.assertIn("FAILED", red["note"])
        green = next(row for row in greens if row["ref"] == "check:check-voices")
        self.assertEqual(green["seat"], "Rin")
        self.assertEqual(green["delta"], 0)
        self.assertIn("clean", green["note"])
        proc = run_script("seat_record", self.root, "--check")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        # the second run of the day is deduped: no new rows
        proc = run_script("seat_record", self.root, "--checks")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertEqual(len(self.read_rows()), 7)
        self.assertIn("already recorded", proc.stdout)


class SeatRecordDayTests(RecordFixture):
    """The day score: conduct booked from the day's own counted facts."""

    def green_week(self, date: str, *, red: str = "") -> list[dict]:
        rows = [
            self.row("check_green", "Rin", 0, date, "check:check-voices"),
            self.row("check_green", "Niko", 0, date, "check:check-contract"),
            self.row("ship", "Mei", 1, date, "build:lane"),
        ]
        if red:
            rows.append(self.row("code_red", red, -1, date, "check:check-board"))
        return rows

    def test_green_day_pays_the_room_once(self) -> None:
        date = self.day(1)
        self.write_rows(self.green_week(date))
        proc = run_script("seat_record", self.root, "--day", "--date", date)
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("8 credit(s) booked", proc.stdout)
        rows = self.read_rows()
        credits = [row for row in rows if row["kind"] == "green_day"]
        self.assertEqual(len(credits), 8)
        self.assertEqual({row["seat"] for row in credits}, {
            "Mei", "Elo", "MechaPip", "Yui", "Niko", "Rin", "Aria", "Reika",
        })
        self.assertTrue(all(row["delta"] == 1 for row in credits))
        self.assertTrue(all(row["date"] == date for row in credits))
        # append-only and deduped: the second run writes nothing
        before = self.record.read_bytes()
        proc = run_script("seat_record", self.root, "--day", "--date", date)
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("already recorded", proc.stdout)
        self.assertEqual(self.record.read_bytes(), before)

    def test_green_suite_without_production_pays_nothing(self) -> None:
        date = self.day(1)
        self.write_rows([row for row in self.green_week(date) if row["kind"] != "ship"])
        proc = run_script("seat_record", self.root, "--day", "--date", date)
        self.assertEqual(proc.returncode, 4, msg=proc.stdout + proc.stderr)
        self.assertIn("no production", proc.stdout)
        self.assertEqual(len(self.read_rows()), 2)  # nothing booked

    def test_red_day_charges_each_seat_in_contact_once(self) -> None:
        date = self.day(2)
        self.write_rows(self.green_week(date, red="Elo"))
        proc = run_script("seat_record", self.root, "--day", "--date", date)
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("contact charged at 0: Elo", proc.stdout)
        books = [row for row in self.read_rows() if row["kind"] == "red_book"]
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["seat"], "Elo")
        self.assertEqual(books[0]["delta"], 0)
        self.assertFalse([row for row in self.read_rows() if row["kind"] == "green_day"])

    def test_unread_day_is_named_never_zeroed(self) -> None:
        proc = run_script("seat_record", self.root, "--day", "--date", self.day(9))
        self.assertEqual(proc.returncode, 3, msg=proc.stdout + proc.stderr)
        self.assertIn("unread", proc.stdout)
        self.assertIn("named, never guessed", proc.stdout)

    def test_day_score_is_machine_only(self) -> None:
        proc = run_script(
            "seat_record", self.root, "--event", "--seat", "Reika",
            "--kind", "green_day", "--ref", "day:test",
        )
        self.assertEqual(proc.returncode, 2, msg=proc.stdout + proc.stderr)
        self.assertIn("invalid kind", proc.stderr)

    def test_red_day_with_unread_contact_charges_no_one(self) -> None:
        # A red row with no readable seat is unread contact: the day is named,
        # nobody is charged, and no phantom row is written.
        date = self.day(3)
        self.write_rows([
            self.row("check_green", "Rin", 0, date, "check:check-voices"),
            {"ts": "%sT00:00:00Z" % date, "date": date, "kind": "code_red",
             "seat": "", "delta": -1, "ref": "check:unknown", "note": "no seat"},
        ])
        proc = run_script("seat_record", self.root, "--day", "--date", date)
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("contact unread", proc.stdout)
        self.assertIn("no seat charged", proc.stdout)
        self.assertFalse([row for row in self.read_rows() if row["kind"] == "red_book"])

    def test_future_day_is_refused(self) -> None:
        future = self.day(-3)
        proc = run_script("seat_record", self.root, "--day", "--date", future)
        self.assertEqual(proc.returncode, 2, msg=proc.stdout + proc.stderr)
        self.assertIn("future", proc.stderr)


class SeatRecordRefusalTests(RecordFixture):
    def test_bad_kind_exits_two_and_writes_nothing(self) -> None:
        proc = run_script(
            "seat_record", self.root, "--event", "--seat", "Reika",
            "--kind", "party", "--ref", "x",
        )
        self.assertEqual(proc.returncode, 2, msg=proc.stdout + proc.stderr)
        self.assertIn("invalid kind", proc.stderr)
        self.assertFalse(self.record.exists())

    def test_bad_seat_exits_two_and_writes_nothing(self) -> None:
        proc = run_script(
            "seat_record", self.root, "--event", "--seat", "Grak",
            "--kind", "note", "--ref", "x",
        )
        self.assertEqual(proc.returncode, 2, msg=proc.stdout + proc.stderr)
        self.assertIn("invalid seat", proc.stderr)
        self.assertFalse(self.record.exists())

    def test_missing_ref_exits_two_and_writes_nothing(self) -> None:
        proc = run_script(
            "seat_record", self.root, "--event", "--seat", "Reika", "--kind", "note",
        )
        self.assertEqual(proc.returncode, 2, msg=proc.stdout + proc.stderr)
        self.assertIn("ref is required", proc.stderr)
        self.assertFalse(self.record.exists())

    def test_tampered_delta_fails_check(self) -> None:
        self.write_rows([self.row("code_red", "Rin", 1, "2026-10-15", "tampered")])
        proc = run_script("seat_record", self.root, "--check")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("delta", proc.stderr)
        self.assertIn("line 1", proc.stderr)

    def test_clean_record_passes_check(self) -> None:
        self.write_rows([self.row("ship", "Yui", 1, "2026-10-15", "ok")])
        proc = run_script("seat_record", self.root, "--check")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("clean", proc.stdout)


class RoomScorecardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="animestack-scorecard-"))
        self.root = self.tmp / "repo"
        self.root.mkdir(parents=True)
        (self.root / "docs").mkdir()
        (self.root / "docs" / "loop.md").write_text("# loop\n", encoding="utf-8")
        self.log = self.root / "DECISION_LOG.md"

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_log(self, entries: str, template: bool = True) -> None:
        parts = ["# Decision Log\n"]
        if template:
            parts.append(
                "```\n## YYYY-MM-DD — <the proposal in one line>\n"
                "- **Mei.** <sentence>\n```\n"
            )
        parts.append(entries)
        self.log.write_text("\n".join(parts), encoding="utf-8")

    def run_card(self, *args: str) -> subprocess.CompletedProcess:
        command = [sys.executable, str(SCRIPTS / "room_scorecard"),
                   "--root", str(self.root)]
        command += [str(arg) for arg in args]
        return subprocess.run(
            command, capture_output=True, text=True, encoding="utf-8", timeout=300
        )

    def test_parses_entries_and_prints_seats_table(self) -> None:
        entry_one = "\n".join([
            "## 2026-10-15 — the recorded house opens",
            "**Proposal.** Record every full-loop decision.",
            "- **Mei.** calm. - **Elo.** measured.",
            "- **MechaPip.** no analog. - **Yui.** memory.",
            "- **Niko.** scripts. - **Rin.** ACCEPT",
            "- **Aria.** SHIP - **Reika.** record it.",
            "**Evidence.** `docs/loop.md` carries the loop.",
            "",
        ])
        entry_two = "\n".join([
            "## 2026-10-16 — the card prints",
            "- **Mei.** still calm. - **Reika.** sign.",
            "**Evidence.** decision only.",
            "",
        ])
        self.write_log(entry_one + entry_two)
        proc = self.run_card()
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("2 decision(s)", proc.stdout)
        self.assertIn("0 malformed", proc.stdout)
        self.assertIn("refs 1/1", proc.stdout)
        self.assertIn("seats 8/8", proc.stdout)
        self.assertIn("seats 2/8", proc.stdout)
        proc = self.run_card("--seats")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("room_scorecard --seats", proc.stdout)
        elo = next(line for line in proc.stdout.splitlines()
                   if line.strip().startswith("Elo"))
        self.assertIn("1/2", elo)
        reika = next(line for line in proc.stdout.splitlines()
                     if line.strip().startswith("Reika"))
        self.assertIn("2/2", reika)
        proc = self.run_card("--strict")
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)

    def test_strict_fails_on_dangling_ref(self) -> None:
        entry = "\n".join([
            "## 2026-10-15 — a dangling ref",
            "- **Mei.** calm. - **Reika.** sign.",
            "**Evidence.** `docs/missing.md` is not in the tree.",
            "",
        ])
        self.write_log(entry)
        proc = self.run_card()
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("absent", proc.stdout)
        proc = self.run_card("--strict")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("docs/missing.md", proc.stderr)

    def test_strict_fails_on_malformed_entry(self) -> None:
        self.write_log("## Not a dated entry\n\n- **Reika.** oh no.\n")
        proc = self.run_card("--strict")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("without a date", proc.stderr)
        # the fenced template must not be counted as an entry
        self.assertNotIn("YYYY-MM-DD", proc.stderr)
        proc = self.run_card()
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("1 malformed", proc.stdout)

    def test_strict_fails_on_entry_without_reika(self) -> None:
        entry = "\n".join([
            "## 2026-10-15 — no sign-off",
            "- **Mei.** calm. - **Yui.** memory.",
            "**Evidence.** decision only.",
            "",
        ])
        self.write_log(entry)
        proc = self.run_card("--strict")
        self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
        self.assertIn("no Reika line", proc.stderr)


if __name__ == "__main__":
    unittest.main()
