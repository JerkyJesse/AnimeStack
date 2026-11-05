"""The DSH surface: seat packs, preset bundle, generator, contract.

Every assertion here is a fact the tree must hold at this release: eight packs
with the full protocol set and the ownership marker last, a bundle whose
manifest the host can read and whose patch names exactly the eleven presets, a
generator whose `--check` regenerates the committed bytes, and no private token
anywhere in the surface. The drift test watches the generator fail on a changed
pack, so the check is proven able to fail before it is trusted.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DSH = REPO / "dsh"
TEAM = DSH / "animestack-team"
HOUSE = DSH / "animestack-house"
GEN = REPO / "scripts" / "gen-dsh-house"
CONTRACT = REPO / "scripts" / "check-contract"

SEATS = ("mei", "elo", "mechapip", "yui", "niko", "rin", "aria", "reika")
SENTENCES = {
    "mei": "What change in the world makes this obsolete?",
    "elo": "What does the crowd refuse to measure correctly?",
    "mechapip": "What has this pattern done before?",
    "yui": "What failure does this prevent, and what would falsify it?",
    "niko": "Where does it live, and what must it never touch?",
    "rin": "How does this fail, and how fast?",
    "aria": "What ships, and what triggers it?",
    "reika": "What are we building, in one sentence?",
}
CLOSES = {
    "mei": ("VERDICT: PASS", "VERDICT: FAIL"),
    "elo": ("VERDICT: PASS", "VERDICT: FAIL"),
    "mechapip": ("VERDICT: MATCH", "VERDICT: NO MATCH"),
    "yui": ("VERDICT: PASS", "VERDICT: FAIL"),
    "niko": ("VERDICT: PASS", "VERDICT: FAIL"),
    "rin": ("VERDICT: ACCEPT", "VERDICT: END"),
    "aria": ("VERDICT: SHIP", "VERDICT: STAND DOWN"),
    "reika": ("VERDICT: SHIP", "VERDICT: RETIRE", "VERDICT: STAND DOWN"),
}
SECTIONS = (
    "## Seat protocol",
    "## Review protocol (team seat)",
    "## Build protocol (team seat)",
    "## Team protocol (Agent Teams surface)",
    "## The close",
)
STAMP = re.compile(r"^<!-- animestack canon rev \d+ :: inputs sha256=[0-9a-f]{64} -->$")
OWN = "<!-- animestack-owned -->"
PRESETS = (
    ("animestack-house", "animestack-team")
    + tuple("animestack-%s" % seat for seat in SEATS)
    + ("animestack-simple",)
)
# Assembled from fragments so this test does not itself carry the literals it
# refuses; the sealed leak gate scans this file like every other.
PRIVATE = re.compile(
    "DIS" + "CORD_|Hedge" + "Fund" + "Lore|Kal" + "shi|KX[A-Z]15M|No" + "vig|"
    "Poly" + "market|mecha" + "box|eth" + "box|silver" + "box|gold" + "box|"
    "Ph" + "ipps|TRADING" + "IDEAS|HEDGE" + "_FUND|mirror" + " seat|The " + "Belt|"
    "profit" + "/hr|cents per " + "entry|15-minute " + "binary"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run(args: list[str], cwd: Path = REPO) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, *args], cwd=str(cwd), capture_output=True, text=True, timeout=300
    )


class SeatPackTests(unittest.TestCase):
    def test_eight_packs_exactly(self) -> None:
        found = sorted(path.name for path in TEAM.glob("animestack-*.md"))
        expected = sorted("animestack-%s.md" % seat for seat in SEATS)
        self.assertEqual(found, expected, "the pack roster is not the eight seats")

    def test_pack_protocols_and_marker(self) -> None:
        for seat in SEATS:
            with self.subTest(seat=seat):
                path = TEAM / ("animestack-%s.md" % seat)
                text = read(path)
                lines = [line for line in text.splitlines() if line.strip()]
                self.assertTrue(STAMP.match(text.splitlines()[0]), "stamp missing on line 1")
                self.assertIn("# SEAT: %s" % seat, text)
                self.assertIn(SENTENCES[seat], text)
                for section in SECTIONS:
                    self.assertIn(section, text, "missing section %r" % section)
                for token in CLOSES[seat]:
                    self.assertIn(token, text, "missing close %r" % token)
                self.assertIn("do not sign for another seat", text)
                self.assertIn("team_task_update", text)
                self.assertIn("`SEAT: <id>`", text)
                self.assertEqual(lines[-1].strip(), OWN, "the marker is not the last line")

    def test_pack_has_no_model_pin_or_permission_block(self) -> None:
        for seat in SEATS:
            with self.subTest(seat=seat):
                text = read(TEAM / ("animestack-%s.md" % seat))
                self.assertIsNone(re.search(r"(?m)^model\s*:", text))
                self.assertNotIn("permission:", text)
                self.assertNotIn(": deny", text)

    def test_pack_carries_the_seat_voice(self) -> None:
        """The theatre is a requirement, not decoration: the pack carries the seat."""
        niko = read(TEAM / "animestack-niko.md")
        self.assertIn("Contamination", niko)
        self.assertIn("We'll clean it up later.", niko)
        self.assertIn("Keeper of the Body", niko)
        reika = read(TEAM / "animestack-reika.md")
        self.assertIn("Cowardice wearing process", reika)


class BundleTests(unittest.TestCase):
    def test_bundle_files(self) -> None:
        for name in (
            "package.json",
            "index.js",
            "commands.generated.js",
            "cordis.patch.yml",
            "profile.patch.yml",
            "locale/en.json",
            "icon.svg",
        ):
            self.assertTrue((HOUSE / name).is_file(), "missing %s" % name)

    def test_package_manifest(self) -> None:
        data = json.loads(read(HOUSE / "package.json"))
        self.assertEqual(data["name"], "animestack-house-presets")
        self.assertEqual(data["dsh"]["bundle"]["patch"], "./cordis.patch.yml")
        self.assertEqual(data["main"], "./index.js")

    def test_plugin_is_dependency_free_and_injects_commands(self) -> None:
        body = read(HOUSE / "index.js")
        self.assertIn('export const inject = ["commands"]', body)
        self.assertIn("export function apply(ctx)", body)
        self.assertNotIn("import ", body.split("import commands", 1)[1])

    def test_commands_are_the_two_router_specs(self) -> None:
        body = read(HOUSE / "commands.generated.js")
        self.assertIn("export default [", body)
        self.assertIn('name: "house"', body)
        self.assertIn('name: "simple"', body)
        self.assertIn("$ARGUMENTS", body)

    def test_patch_has_eleven_presets_and_the_command_row(self) -> None:
        body = read(HOUSE / "cordis.patch.yml")
        found = re.findall(r"(?m)^    - id: preset-([a-z0-9-]+)$", body)
        self.assertEqual(found, list(PRESETS))
        self.assertIn("- id: animestack-house-commands", body)
        self.assertIn("name: 'animestack-house-presets'", body)
        self.assertIn("@deepseek-ai/dsh-agent-preset", body)
        self.assertIn("@deepseek-ai/dsh-persona", body)

    def test_patch_parses_as_yaml(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML not installed")
        class Loader(yaml.SafeLoader):
            pass
        Loader.add_multi_constructor(
            "tag:yaml.org,2002:",
            lambda loader, suffix, node: loader.construct_scalar(node)
            if isinstance(node, yaml.ScalarNode)
            else None,
        )
        doc = yaml.load(read(HOUSE / "cordis.patch.yml"), Loader=Loader)
        self.assertIsInstance(doc, list)
        rows = doc[0]["insert"]
        self.assertEqual(len(rows), 12)  # one command row + eleven presets
        for row in rows:
            self.assertIn("id", row)
            self.assertIn("name", row)

    def test_team_chair_speaks_the_surface(self) -> None:
        body = read(HOUSE / "cordis.patch.yml")
        team = body.split("- id: preset-animestack-team", 1)[1].split("- id: preset-animestack-mei", 1)[0]
        for phrase in ("spawn_teammate", "`SEAT: <id>`", "Round 1", "Round 2", "signing seat"):
            self.assertIn(phrase, team)
        for seat in SEATS:
            self.assertIn("`SEAT: <id>`", body)

    def test_locale_covers_every_preset(self) -> None:
        data = json.loads(read(HOUSE / "locale" / "en.json"))
        self.assertEqual(sorted(data["presets"]), sorted(PRESETS))

    def test_profile_fragment_raises_the_cap(self) -> None:
        body = read(HOUSE / "profile.patch.yml")
        self.assertIn("# >>> animestack >>>", body)
        self.assertIn("# <<< animestack <<<", body)
        self.assertIn("- id: agent-team", body)
        self.assertIn("maxMembers: 9", body)

    def test_readme_names_the_two_key_merge_and_never_the_profile_write(self) -> None:
        body = read(DSH / "README.md")
        self.assertIn("--merge-profile", body)
        self.assertIn("dsh.profile.bundles", body)
        self.assertIn("never edits", body)


class GeneratorTests(unittest.TestCase):
    def test_generator_is_in_sync(self) -> None:
        proc = run([str(GEN), "--check"])
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("in sync", proc.stdout)

    def test_generator_fails_on_a_changed_pack(self) -> None:
        """Red once: the drift check watches its own failure."""
        with tempfile.TemporaryDirectory(prefix="animestack-drift-") as tmp:
            fixture = Path(tmp) / "repo"
            shutil.copytree(
                REPO,
                fixture,
                ignore=shutil.ignore_patterns(
                    ".git", "art", "assets", "__pycache__",
                    ".pytest_cache", ".ruff_cache", "*.pyc",
                ),
            )
            pack = fixture / "dsh" / "animestack-team" / "animestack-niko.md"
            pack.write_text(read(pack) + "\nhand edit\n", encoding="utf-8")
            proc = run([str(fixture / "scripts" / "gen-dsh-house"), "--check", "--root", str(fixture)])
            self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
            self.assertIn("drift: dsh/animestack-team/animestack-niko.md", proc.stdout)

    def test_contract_is_clean(self) -> None:
        proc = run([str(CONTRACT)])
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        self.assertIn("8 packs, 11 presets", proc.stdout)


class LeakTests(unittest.TestCase):
    def test_no_private_token_in_the_surface(self) -> None:
        for path in sorted(DSH.rglob("*")):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            match = PRIVATE.search(text)
            self.assertIsNone(
                match,
                "%s carries a private token: %r" % (path.relative_to(REPO).as_posix(), match.group(0) if match else ""),
            )

    def test_no_absolute_host_path(self) -> None:
        for path in sorted(DSH.rglob("*")):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            self.assertNotIn("C:\\Users", text, "%s carries a host path" % path)
            self.assertNotIn("/Users/", text)


if __name__ == "__main__":
    unittest.main()
