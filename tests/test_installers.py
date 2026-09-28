"""Installer round-trip tests: both entry points deliver the pack per host.

Every host target the installers ship for is exercised against a throwaway
HOME: the expected skills, agents, commands, and digests must land, the
uninstall must remove only what AnimeStack owns, and files another pack owns
must survive both directions. The repo is only ever read; every install
target is a temp directory.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SETUP = REPO / "setup"
SETUP_PS = REPO / "setup.ps1"

MD_MARKER = "<!-- animestack-owned -->"
TOML_MARKER = "# animestack-owned"

SKILL_NAMES = sorted(p.name for p in (REPO / "skills").iterdir() if p.is_dir())

# host -> (skills dir, agents dir, agent extension, command dir or None)
NORMAL_HOSTS = {
    "claude": (".claude/skills", ".claude/agents", "md", None),
    "cursor": (".cursor/skills", ".cursor/agents", "md", None),
    "codex": (".codex/skills", ".codex/agents", "toml", None),
    "factory": (".factory/skills", ".factory/droids", "md", ".factory/commands"),
    "opencode": (
        ".config/opencode/skills",
        ".config/opencode/agent",
        "md",
        ".config/opencode/command",
    ),
    "kiro": (".kiro/skills", ".kiro/agents", "md", None),
}
DIGEST_HOSTS = {
    "openclaw": ".openclaw/skills/animestack",
    "hermes": ".hermes/skills/animestack",
    "gbrain": ".gbrain/skills/animestack",
}
ALL_HOSTS = list(NORMAL_HOSTS) + ["slate"] + list(DIGEST_HOSTS)

DIALECT_OF = {
    "claude": "claude",
    "cursor": "cursor",
    "codex": "codex",
    "factory": "factory",
    "opencode": "opencode",
    "kiro": "kiro",
    "slate": "claude",
}


def _probe_bash(candidate: str) -> bool:
    try:
        proc = subprocess.run(
            [candidate, "-c", "printf ok"],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return proc.returncode == 0 and proc.stdout == "ok"


def find_bash() -> str | None:
    candidates: list[str] = []
    which = shutil.which("bash")
    if which:
        candidates.append(which)
    if os.name == "nt":
        for env_name in ("ProgramFiles", "ProgramFiles(x86)"):
            base = os.environ.get(env_name)
            if base:
                candidates.append(str(Path(base) / "Git" / "bin" / "bash.exe"))
        local = os.environ.get("LOCALAPPDATA")
        if local:
            candidates.append(
                str(Path(local) / "Programs" / "Git" / "bin" / "bash.exe")
            )
    seen: set[str] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if Path(candidate).is_file() and _probe_bash(candidate):
            return candidate
    return None


def _probe_ps(candidate: str) -> bool:
    try:
        proc = subprocess.run(
            [candidate, "-NoProfile", "-Command", "exit 0"],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return proc.returncode == 0


def find_ps() -> str | None:
    for candidate in (shutil.which("pwsh"), shutil.which("powershell")):
        if candidate and _probe_ps(candidate):
            return candidate
    return None


BASH = find_bash()
PS = find_ps() if os.name == "nt" else None


def source_agents(host: str) -> list[Path]:
    dialect = DIALECT_OF[host]
    ext = "toml" if dialect == "codex" else "md"
    return sorted((REPO / "agents" / dialect).glob(f"animestack-*.{ext}"))


def last_line(path: Path) -> str:
    lines = [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return lines[-1].strip() if lines else ""


def run_bash_script(
    script: Path, home: Path, *args: str
) -> subprocess.CompletedProcess:
    if BASH is None:
        raise unittest.SkipTest("no working bash found")
    env = dict(os.environ)
    env["HOME"] = home.as_posix()
    env.pop("CODEX_HOME", None)
    return subprocess.run(
        [BASH, script.as_posix(), *args],
        env=env,
        capture_output=True,
        text=True,
        timeout=300,
    )


def run_bash(home: Path, *args: str) -> subprocess.CompletedProcess:
    return run_bash_script(SETUP, home, *args)


def run_ps_script(
    script: Path, home: Path, *args: str
) -> subprocess.CompletedProcess:
    if PS is None:
        raise unittest.SkipTest("no PowerShell found")
    env = dict(os.environ)
    env["USERPROFILE"] = str(home)
    env["HOME"] = str(home)
    env.pop("CODEX_HOME", None)
    return subprocess.run(
        [PS, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script), *args],
        env=env,
        capture_output=True,
        text=True,
        timeout=600,
    )


def run_ps(home: Path, *args: str) -> subprocess.CompletedProcess:
    return run_ps_script(SETUP_PS, home, *args)


class FootprintChecks(unittest.TestCase):
    """Shared footprint assertions for the bash and PowerShell lanes."""

    HOST_DIRS = (
        ".claude",
        ".cursor",
        ".codex",
        ".factory",
        ".config",
        ".kiro",
        ".openclaw",
        ".hermes",
        ".gbrain",
    )

    def assert_no_host_dirs(self, home: Path) -> None:
        for rel in self.HOST_DIRS:
            self.assertFalse((home / rel).exists(), f"unexpected host dir: {rel}")

    def assert_installed_footprint(self, home: Path, host: str) -> None:
        if host in DIGEST_HOSTS:
            target = home / DIGEST_HOSTS[host]
            self.assertTrue(
                (target / "AGENTS.md").is_file(), f"{host}: AGENTS.md missing"
            )
            self.assertEqual(
                (target / "AGENTS.md").read_bytes(),
                (REPO / "AGENTS.md").read_bytes(),
                f"{host}: digest AGENTS.md differs from the repo's",
            )
            self.assertTrue(
                (target / "README.md").is_file(), f"{host}: README.md missing"
            )
            self.assertTrue(
                (target / ".animestack-owned").is_file(),
                f"{host}: digest marker missing",
            )
            for name in SKILL_NAMES:
                self.assertFalse(
                    (target.parent / name).exists(),
                    f"{host}: skill {name} leaked into a digest host",
                )
            return
        slug = "claude" if host == "slate" else host
        skills_rel, agents_rel, ext, command_rel = NORMAL_HOSTS[slug]
        skills_dir = home / skills_rel
        agents_dir = home / agents_rel
        for name in SKILL_NAMES:
            self.assertTrue(
                (skills_dir / name / "SKILL.md").is_file(),
                f"{host}: skill {name} missing",
            )
        expected = source_agents(host)
        found = sorted(agents_dir.glob(f"animestack-*.{ext}"))
        self.assertEqual(
            len(found),
            len(expected),
            f"{host}: expected {len(expected)} agents, found {len(found)}",
        )
        marker = TOML_MARKER if ext == "toml" else MD_MARKER
        for path in found:
            self.assertEqual(
                last_line(path),
                marker,
                f"{host}: {path.name} lost the ownership marker",
            )
        if command_rel:
            command = home / command_rel / "house.md"
            self.assertTrue(command.is_file(), f"{host}: house command missing")
            self.assertEqual(
                last_line(command),
                MD_MARKER,
                f"{host}: house command lost the ownership marker",
            )

    def assert_uninstalled_footprint(self, home: Path, host: str) -> None:
        if host in DIGEST_HOSTS:
            self.assertFalse(
                (home / DIGEST_HOSTS[host]).exists(),
                f"{host}: digest survived uninstall",
            )
            return
        slug = "claude" if host == "slate" else host
        skills_rel, agents_rel, _ext, command_rel = NORMAL_HOSTS[slug]
        for name in SKILL_NAMES:
            self.assertFalse(
                (home / skills_rel / name).exists(),
                f"{host}: skill {name} survived uninstall",
            )
        self.assertEqual(
            sorted((home / agents_rel).glob("animestack-*")),
            [],
            f"{host}: agents survived uninstall",
        )
        if command_rel:
            self.assertFalse(
                (home / command_rel / "house.md").exists(),
                f"{host}: command survived uninstall",
            )


class SetupScriptTests(unittest.TestCase):
    def test_setup_script_is_lf(self) -> None:
        self.assertNotIn(
            b"\r",
            SETUP.read_bytes(),
            "setup has CR line endings; unix/WSL bash will fail; refresh: "
            "Remove-Item setup; git checkout -- setup",
        )


@unittest.skipUnless(BASH, "no working bash found")
class BashInstallerTests(FootprintChecks):
    def test_check_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            proc = run_bash(home, "--host", "all", "--check")
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
            self.assertIn("check: pack valid", proc.stdout)
            self.assertEqual(list(home.iterdir()), [])

    def test_auto_installs_only_existing_configs(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            proc = run_bash(home, "--host", "auto")
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
            self.assertIn("No hosts matched", proc.stdout)
            self.assertEqual(list(home.iterdir()), [])

        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            (home / ".claude").mkdir()
            proc = run_bash(home, "--host", "auto")
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
            self.assert_installed_footprint(home, "claude")
            self.assertFalse((home / ".cursor").exists())
            self.assertFalse((home / ".config").exists())
            self.assertFalse((home / ".kiro").exists())

    def test_every_host_installs_expected_files(self) -> None:
        for host in ALL_HOSTS:
            with self.subTest(host=host):
                with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
                    home = Path(tmp)
                    proc = run_bash(home, "--host", host)
                    self.assertEqual(
                        proc.returncode,
                        0,
                        msg=f"{host}\n{proc.stdout}\n{proc.stderr}",
                    )
                    self.assert_installed_footprint(home, host)

    def test_every_host_uninstalls_clean(self) -> None:
        for host in ALL_HOSTS:
            with self.subTest(host=host):
                with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
                    home = Path(tmp)
                    install = run_bash(home, "--host", host)
                    self.assertEqual(
                        install.returncode, 0, msg=install.stdout + install.stderr
                    )
                    uninstall = run_bash(home, "--host", host, "--uninstall")
                    self.assertEqual(
                        uninstall.returncode,
                        0,
                        msg=uninstall.stdout + uninstall.stderr,
                    )
                    self.assert_uninstalled_footprint(home, host)

    def test_foreign_files_survive(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            foreign_agent = home / ".claude" / "agents" / "aria.md"
            foreign_agent.parent.mkdir(parents=True)
            foreign_agent.write_text("---\nname: aria\n---\n", encoding="utf-8")
            foreign_command = home / ".config" / "opencode" / "command" / "house.md"
            foreign_command.parent.mkdir(parents=True)
            foreign_command.write_text(
                "---\ndescription: another pack owns this name\n---\n",
                encoding="utf-8",
            )
            agent_bytes = foreign_agent.read_bytes()
            command_bytes = foreign_command.read_bytes()

            claude = run_bash(home, "--host", "claude")
            self.assertEqual(claude.returncode, 0, msg=claude.stdout + claude.stderr)
            opencode = run_bash(home, "--host", "opencode")
            self.assertEqual(
                opencode.returncode, 0, msg=opencode.stdout + opencode.stderr
            )
            self.assertIn("Not registered", opencode.stdout)
            self.assertEqual(foreign_agent.read_bytes(), agent_bytes)
            self.assertEqual(foreign_command.read_bytes(), command_bytes)
            self.assertEqual(
                len(list((home / ".claude" / "agents").glob("animestack-*"))),
                len(source_agents("claude")),
            )
            self.assertEqual(
                len(list((home / ".config" / "opencode" / "agent").glob("animestack-*"))),
                len(source_agents("opencode")),
            )

            claude_un = run_bash(home, "--host", "claude", "--uninstall")
            self.assertEqual(claude_un.returncode, 0, msg=claude_un.stdout + claude_un.stderr)
            opencode_un = run_bash(home, "--host", "opencode", "--uninstall")
            self.assertEqual(
                opencode_un.returncode, 0, msg=opencode_un.stdout + opencode_un.stderr
            )
            self.assertEqual(foreign_agent.read_bytes(), agent_bytes)
            self.assertEqual(foreign_command.read_bytes(), command_bytes)
            self.assertEqual(
                list((home / ".claude" / "agents").glob("animestack-*")), []
            )
            self.assertEqual(
                list((home / ".config" / "opencode" / "agent").glob("animestack-*")),
                [],
            )

    def test_refuses_model_pin(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-pin-") as tmp:
            fixture = Path(tmp) / "repo"
            (fixture / "agents" / "cursor").mkdir(parents=True)
            shutil.copy2(SETUP, fixture / "setup")
            text = (REPO / "agents" / "cursor" / "animestack-yui.md").read_text(
                encoding="utf-8"
            )
            text = text.replace("\r\n", "\n").replace(
                "---\n", "---\nmodel: test-pin\n", 1
            )
            (fixture / "agents" / "cursor" / "animestack-yui.md").write_text(
                text, encoding="utf-8"
            )
            with tempfile.TemporaryDirectory(prefix="animestack-home-") as home_tmp:
                proc = run_bash_script(
                    fixture / "setup", Path(home_tmp), "--host", "claude", "--check"
                )
            self.assertEqual(proc.returncode, 1, msg=proc.stdout + proc.stderr)
            self.assertIn("model pin", proc.stderr)


@unittest.skipUnless(os.name == "nt" and PS, "setup.ps1 lane needs Windows PowerShell")
class PwshInstallerTests(FootprintChecks):
    def test_check_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            proc = run_ps(home, "-TargetHost", "all", "-Check")
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
            self.assertIn("nothing written", proc.stdout)
            self.assert_no_host_dirs(home)

    def test_auto_installs_only_existing_configs(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            proc = run_ps(home, "-TargetHost", "auto")
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
            self.assertIn("No hosts matched", proc.stdout)
            self.assert_no_host_dirs(home)

        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            (home / ".claude").mkdir()
            proc = run_ps(home, "-TargetHost", "auto")
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
            self.assert_installed_footprint(home, "claude")
            self.assertFalse((home / ".cursor").exists())

    def test_every_host_installs_expected_files(self) -> None:
        for host in ALL_HOSTS:
            with self.subTest(host=host):
                with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
                    home = Path(tmp)
                    proc = run_ps(home, "-TargetHost", host)
                    self.assertEqual(
                        proc.returncode,
                        0,
                        msg=f"{host}\n{proc.stdout}\n{proc.stderr}",
                    )
                    self.assert_installed_footprint(home, host)

    def test_every_host_uninstalls_clean(self) -> None:
        for host in ALL_HOSTS:
            with self.subTest(host=host):
                with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
                    home = Path(tmp)
                    install = run_ps(home, "-TargetHost", host)
                    self.assertEqual(
                        install.returncode, 0, msg=install.stdout + install.stderr
                    )
                    uninstall = run_ps(home, "-TargetHost", host, "-Uninstall")
                    self.assertEqual(
                        uninstall.returncode,
                        0,
                        msg=uninstall.stdout + uninstall.stderr,
                    )
                    self.assert_uninstalled_footprint(home, host)

    def test_foreign_files_survive(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-home-") as tmp:
            home = Path(tmp)
            foreign_agent = home / ".claude" / "agents" / "aria.md"
            foreign_agent.parent.mkdir(parents=True)
            foreign_agent.write_text("---\nname: aria\n---\n", encoding="utf-8")
            foreign_command = home / ".config" / "opencode" / "command" / "house.md"
            foreign_command.parent.mkdir(parents=True)
            foreign_command.write_text(
                "---\ndescription: another pack owns this name\n---\n",
                encoding="utf-8",
            )
            agent_bytes = foreign_agent.read_bytes()
            command_bytes = foreign_command.read_bytes()

            claude = run_ps(home, "-TargetHost", "claude")
            self.assertEqual(claude.returncode, 0, msg=claude.stdout + claude.stderr)
            opencode = run_ps(home, "-TargetHost", "opencode")
            self.assertEqual(
                opencode.returncode, 0, msg=opencode.stdout + opencode.stderr
            )
            self.assertIn("Not registered", opencode.stdout)
            self.assertEqual(foreign_agent.read_bytes(), agent_bytes)
            self.assertEqual(foreign_command.read_bytes(), command_bytes)
            self.assertEqual(
                len(list((home / ".claude" / "agents").glob("animestack-*"))),
                len(source_agents("claude")),
            )
            self.assertEqual(
                len(list((home / ".config" / "opencode" / "agent").glob("animestack-*"))),
                len(source_agents("opencode")),
            )

            claude_un = run_ps(home, "-TargetHost", "claude", "-Uninstall")
            self.assertEqual(claude_un.returncode, 0, msg=claude_un.stdout + claude_un.stderr)
            opencode_un = run_ps(home, "-TargetHost", "opencode", "-Uninstall")
            self.assertEqual(
                opencode_un.returncode, 0, msg=opencode_un.stdout + opencode_un.stderr
            )
            self.assertEqual(foreign_agent.read_bytes(), agent_bytes)
            self.assertEqual(foreign_command.read_bytes(), command_bytes)
            self.assertEqual(
                list((home / ".claude" / "agents").glob("animestack-*")), []
            )
            self.assertEqual(
                list((home / ".config" / "opencode" / "agent").glob("animestack-*")),
                [],
            )

    def test_refuses_model_pin(self) -> None:
        with tempfile.TemporaryDirectory(prefix="animestack-pin-") as tmp:
            fixture = Path(tmp) / "repo"
            (fixture / "agents" / "cursor").mkdir(parents=True)
            shutil.copy2(SETUP_PS, fixture / "setup.ps1")
            text = (REPO / "agents" / "cursor" / "animestack-yui.md").read_text(
                encoding="utf-8"
            )
            text = text.replace("\r\n", "\n").replace(
                "---\n", "---\nmodel: test-pin\n", 1
            )
            (fixture / "agents" / "cursor" / "animestack-yui.md").write_text(
                text, encoding="utf-8"
            )
            with tempfile.TemporaryDirectory(prefix="animestack-home-") as home_tmp:
                proc = run_ps_script(
                    fixture / "setup.ps1",
                    Path(home_tmp),
                    "-TargetHost",
                    "claude",
                    "-Check",
                )
            output = proc.stdout + proc.stderr
            self.assertEqual(proc.returncode, 1, msg=output)
            self.assertIn("model pin", output)


if __name__ == "__main__":
    unittest.main()
