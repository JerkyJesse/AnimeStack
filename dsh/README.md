<!-- animestack canon rev 9 :: inputs sha256=4cb4abe5e46ad8172d874d2af5f40bc5a85a99c7f436dda08fbf6d5c4c0bd9ca -->
# The DSH surface - AnimeStack on DeepSeek Harness

*The eleventh install target, and the only one that ships a team: eight seat packs,
eleven Agent presets, and two operator commands, generated from the public canon.*

AnimeStack installs ten coding-host dialects under `agents/`. This directory is the
DeepSeek Harness surface: it does not add a seventh dialect, it adds a house. The
surface has three parts, and the installer owns all three.

## What lands where

| Part | Source | Installs to |
| --- | --- | --- |
| The ten skills | `skills/` | `$DSH_HOME/skills/<name>/SKILL.md` |
| The eight seat packs | `dsh/animestack-team/` | `$DSH_HOME/animestack-team/<seat>.md` |
| The preset bundle | `dsh/animestack-house/` | `$DSH_HOME/animestack/` |

`$DSH_HOME` is the host's home: `DSH_HOME` when set, else `%USERPROFILE%\.dsh` on
Windows and `~/.dsh` elsewhere. The installer writes nothing outside the host it can
prove it owns: skills carry `.animestack-owned`, packs end with the ownership marker,
and the bundle is a directory carrying `.animestack-owned`.

## Install

```
git clone https://github.com/JerkyJesse/AnimeStack ~/animestack && cd ~/animestack
./setup --host dsh
# Windows: powershell -ExecutionPolicy Bypass -File .\setup.ps1 -TargetHost dsh
```

The default install writes the owned files and prints the two-key merge. It never edits
the host profile: `cordis.patch.yml` is the file a bad write turns into a host with no
presets, so the installer writes only what it can prove it owns.

## The two-key merge

In `$DSH_HOME/profiles/<profile>/package.json`, add the dependency and append to
`dsh.profile.bundles`:

```json
{
  "dsh": { "profile": { "bundles": [
    "... every bundle already listed ...",
    "animestack-house-presets"
  ] } },
  "dependencies": {
    "animestack-house-presets": "link:<repo>/dsh/animestack-house"
  }
}
```

Then raise the roster cap once, in `cordis.patch.yml`, if the profile does not already
carry an `agent-team` row - `dsh/animestack-house/profile.patch.yml` is the exact block:

```yaml
- id: agent-team
  name: '@deepseek-ai/dsh-experimental-agent-team'
  config:
    maxMembers: 9
```

`setup --host dsh --merge-profile` performs both edits for you: it parses the profile
JSON, backs it up beside itself, appends the dependency and the bundle only when
absent, re-parses to validate, and appends the `agent-team` block only when that row is
absent. `--uninstall` removes exactly those three things and nothing else. Every other
key in the profile survives byte-identical; the installer never rewrites a file it did
not write.

## Use

- A thread that names no preset opens on the profile default. Set `default: animestack-team`
  in the `agent-preset-registry` row to make the house the default room.
- `/house` queues the whole-room router; `/simple` queues the waiver for one invocation.
- `animestack-house` is the declared subagent room; `animestack-team` is the Agent Teams
  surface. The two are never mixed in one room, and a missing `spawn_teammate` is named
  in one line, never fallen back from silently.

## Uninstall

```
./setup --host dsh --uninstall
# with the profile merge reversed as well:
./setup --host dsh --uninstall --merge-profile
```

## Prove it

```
python scripts/gen-dsh-house --check      # packs, commands, patch, locale in sync
python scripts/check-contract             # the DSH branch: 8 packs, 11 presets
python -m pytest tests/test_dsh_surface.py -q
```

The generated files are never hand-edited: edit the canon, the seat agents, the seat
pages, or the command sources, run `scripts/gen-agent-dialects` and then
`scripts/gen-dsh-house`, and commit both trees. A stale pack fails `--check`.
