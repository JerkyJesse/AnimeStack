# AnimeStack setup.ps1 - install the eight-seat house skills, agents, and the
# /house commands into supported AI coding hosts on Windows, plus the DeepSeek
# Harness surface (seat packs + the preset bundle). The native entry point
# beside ./setup (bash); same contract, same ownership gate, same model rule.
# No network, no admin, no node.
#
# The cage rule: never delete or edit a target without proof that we own it.
# A skill target is ours when it is a link resolving into this repo, or a
# directory carrying the .animestack-owned marker. An agent or seat-pack file is
# ours when its last line is the right ownership marker (HTML comment for
# markdown agents, TOML comment for codex agents). The DSH bundle is a directory
# carrying the same marker. The host profile (package.json, cordis.patch.yml) is
# never written by the default install: -MergeProfile is the explicit opt-in
# that parses, backs up, appends only what is absent, re-parses to validate, and
# uninstalls exactly the three things it added.
#
# The model rule: no shipped agent names a concrete model. claude and factory
# agents carry `model: inherit`; opencode, cursor, and kiro agents omit the
# `model` key; codex agents omit `model` and `model_reasoning_effort`. Setup
# refuses to install from a pack that violates this.

[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [Alias('Host')]
    [string]$TargetHost = 'claude',

    [switch]$Uninstall,
    [switch]$Check,
    [switch]$MergeProfile,
    [switch]$Quiet,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path

$Skills = @('house', 'reika', 'mei', 'elo', 'mechapip', 'yui', 'niko', 'rin', 'aria', 'simple')
$AllHosts = @('claude', 'cursor', 'codex', 'factory', 'opencode', 'kiro', 'slate', 'openclaw', 'hermes', 'gbrain', 'dsh')
$AutoHosts = @('claude', 'cursor', 'codex', 'factory', 'opencode', 'kiro', 'openclaw', 'hermes', 'gbrain', 'dsh')

$OwnMarker = '<!-- animestack-owned -->'
$TomlMarker = '# animestack-owned'
$OwnFlag = '.animestack-owned'
$RootFlag = '.animestack-root'

$script:SkillCount = 0
$script:AgentCount = 0
$script:CommandCount = 0
$script:DigestCount = 0
$script:PackCount = 0
$script:BundleCount = 0
$script:MergeCount = 0
$script:SkipCount = 0
$script:DoneHosts = @()
$Paths = New-Object System.Collections.Generic.List[string]

function Write-Usage {
    Write-Output @'
AnimeStack setup.ps1 - install the eight-seat house skills, agents, and the
/house commands into AI hosts, plus the DeepSeek Harness surface (native
Windows entry point beside ./setup)

Usage: .\setup.ps1 [-TargetHost <name>] [-Uninstall] [-Check] [-MergeProfile] [-Quiet] [-Help]

Options:
  -TargetHost <name>  Target host: claude, cursor, codex, factory, opencode,
                      kiro, slate, openclaw, hermes, gbrain, dsh, all, auto.
                      Default: claude. `dsh` is the DeepSeek Harness surface:
                      the ten skills, the eight seat packs, and the preset
                      bundle, installed under $env:DSH_HOME (else ~\.dsh).
  -Uninstall          Remove only provably-owned AnimeStack items for the
                      selected host(s). Everything else is left untouched.
  -Check              Dry run: validate the pack and print what would be installed per host; writes nothing.
  -MergeProfile       DSH only: also merge the bundle into the host profile
                      (package.json link + bundle entry, and the agent-team row
                      when absent). Parses, backs up, re-parses to validate, and
                      -Uninstall removes exactly what this flag added.
  -Quiet              Suppress progress output; print only the final summary.
  -Help               Show this help and exit.

Examples:
  .\setup.ps1                          # install for Claude Code
  .\setup.ps1 opencode                 # opencode skills + agents + command
  .\setup.ps1 dsh                      # DSH skills + seat packs + bundle (no profile write)
  .\setup.ps1 dsh -MergeProfile        # ...and merge the two profile keys
  .\setup.ps1 -TargetHost all          # every supported host
  .\setup.ps1 -TargetHost auto         # hosts whose config dir already exists
  .\setup.ps1 claude -Uninstall        # remove only owned AnimeStack items
'@
}

function Get-HomeDir {
    if ($env:USERPROFILE) { return $env:USERPROFILE }
    if ($env:HOME) { return $env:HOME }
    return $HOME
}

function Log([string]$Message) {
    if (-not $Quiet) { Write-Output $Message }
}

function Get-HostConfigDir([string]$Name) {
    $h = Get-HomeDir
    switch ($Name) {
        'claude'   { return (Join-Path $h '.claude') }
        'cursor'   { return (Join-Path $h '.cursor') }
        'codex'    { if ($env:CODEX_HOME) { return $env:CODEX_HOME } return (Join-Path $h '.codex') }
        'factory'  { return (Join-Path $h '.factory') }
        'opencode' { return (Join-Path $h '.config\opencode') }
        'kiro'     { return (Join-Path $h '.kiro') }
        'openclaw' { return (Join-Path $h '.openclaw') }
        'hermes'   { return (Join-Path $h '.hermes') }
        'gbrain'   { return (Join-Path $h '.gbrain') }
        'dsh'      { if ($env:DSH_HOME) { return $env:DSH_HOME } return (Join-Path $h '.dsh') }
        default    { return '' }
    }
}

function Get-HostSkillsDir([string]$Name) {
    $d = Get-HostConfigDir $Name
    if ($d) { return (Join-Path $d 'skills') }
    return ''
}

function Get-HostAgentsDir([string]$Name) {
    $h = Get-HomeDir
    switch ($Name) {
        'claude'   { return (Join-Path $h '.claude\agents') }
        'cursor'   { return (Join-Path $h '.cursor\agents') }
        'codex'    { if ($env:CODEX_HOME) { return (Join-Path $env:CODEX_HOME 'agents') } return (Join-Path $h '.codex\agents') }
        'factory'  { return (Join-Path $h '.factory\droids') }
        'opencode' { return (Join-Path $h '.config\opencode\agent') }
        'kiro'     { return (Join-Path $h '.kiro\agents') }
        default    { return '' }
    }
}

function Get-HostAgentsSrc([string]$Name) {
    switch ($Name) {
        'claude'   { return (Join-Path $Root 'agents\claude') }
        'cursor'   { return (Join-Path $Root 'agents\cursor') }
        'codex'    { return (Join-Path $Root 'agents\codex') }
        'factory'  { return (Join-Path $Root 'agents\factory') }
        'opencode' { return (Join-Path $Root 'agents\opencode') }
        'kiro'     { return (Join-Path $Root 'agents\kiro') }
        default    { return '' }
    }
}

function Get-HostCommandsDir([string]$Name) {
    switch ($Name) {
        'factory'  { return (Join-Path (Get-HomeDir) '.factory\commands') }
        'opencode' { return (Join-Path (Get-HomeDir) '.config\opencode\command') }
        default    { return '' }
    }
}

function Get-HostCommandsSrc([string]$Name) {
    switch ($Name) {
        'factory'  { return (Join-Path $Root 'agents\factory\command') }
        'opencode' { return (Join-Path $Root 'agents\opencode\command') }
        default    { return '' }
    }
}

function Get-HostDigestDir([string]$Name) {
    $h = Get-HomeDir
    switch ($Name) {
        'openclaw' { return (Join-Path $h '.openclaw\skills\animestack') }
        'hermes'   { return (Join-Path $h '.hermes\skills\animestack') }
        'gbrain'   { return (Join-Path $h '.gbrain\skills\animestack') }
        default    { return '' }
    }
}

# ─── DeepSeek Harness surface ─────────────────────────────────
# The DSH host is a coding host for the ten skills and, unlike the others, a
# team surface: eight seat packs and one preset bundle. Its home is DSH_HOME
# when the host sets it, else ~\.dsh. The bundle is installed into an owned
# directory; the host profile is only touched by -MergeProfile.
function Get-DshPacksSrc {
    return (Join-Path $Root 'dsh\animestack-team')
}

function Get-DshPacksDir {
    $cfg = Get-HostConfigDir 'dsh'
    if ($cfg) { return (Join-Path $cfg 'animestack-team') }
    return ''
}

function Get-DshBundleSrc {
    return (Join-Path $Root 'dsh\animestack-house')
}

function Get-DshBundleDir {
    $cfg = Get-HostConfigDir 'dsh'
    if ($cfg) { return (Join-Path $cfg 'animestack') }
    return ''
}

# The profile directory: DSH_PROFILE when set, else the only profile on disk,
# else `desktop`. No profile dir means no merge.
function Get-DshProfileDir {
    $cfg = Get-HostConfigDir 'dsh'
    if (-not $cfg) { return '' }
    $root = Join-Path $cfg 'profiles'
    if ($env:DSH_PROFILE) {
        $candidate = Join-Path $root $env:DSH_PROFILE
        if (Test-Path -LiteralPath $candidate) { return $candidate }
    }
    $dirs = @(Get-ChildItem -LiteralPath $root -Directory -ErrorAction SilentlyContinue)
    if ($dirs.Count -eq 1) { return $dirs[0].FullName }
    $desktop = Join-Path $root 'desktop'
    if (Test-Path -LiteralPath $desktop) { return $desktop }
    return $desktop
}

function Install-Packs([string]$SrcDir, [string]$TargetDir) {
    if (-not $SrcDir -or -not $TargetDir) { return }
    if (-not (Test-Path -LiteralPath $SrcDir)) { return }
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    foreach ($src in Get-ChildItem -LiteralPath $SrcDir -File -Filter 'animestack-*.md') {
        $dst = Join-Path $TargetDir $src.Name
        if (Test-Path -LiteralPath $dst) {
            if ((Get-LastLine $dst) -ne $OwnMarker) {
                Log "Not registered (a seat pack you own already uses the name; left untouched): $($src.Name)"
                $script:SkipCount++
                continue
            }
        }
        Copy-Item -LiteralPath $src.FullName -Destination $dst -Force
        $script:PackCount++
        Log "Installed seat pack: $($src.Name) -> $dst"
    }
}

function Uninstall-Packs([string]$TargetDir) {
    if (-not $TargetDir -or -not (Test-Path -LiteralPath $TargetDir)) { return }
    foreach ($file in Get-ChildItem -LiteralPath $TargetDir -File -Filter 'animestack-*.md') {
        if ((Get-LastLine $file.FullName) -eq $OwnMarker) {
            Remove-Item -LiteralPath $file.FullName -Force
            $script:PackCount++
            Log "Removed: $($file.FullName)"
        }
    }
    # The packs directory is ours by name: an empty one is an orphan, not a target.
    if (-not (Get-ChildItem -LiteralPath $TargetDir -Force -ErrorAction SilentlyContinue)) {
        Remove-Item -LiteralPath $TargetDir -Force -ErrorAction SilentlyContinue
    }
}

function Install-Bundle([string]$SrcDir, [string]$TargetDir) {
    if (-not $SrcDir -or -not $TargetDir) { return }
    if (-not (Test-Path -LiteralPath $SrcDir)) { return }
    if (Test-Path -LiteralPath $TargetDir) {
        if (Test-Ours $TargetDir) {
            Remove-Owned $TargetDir | Out-Null
        } else {
            Log "Not registered (a directory you own already uses the name; left untouched): $TargetDir"
            $script:SkipCount++
            return
        }
    }
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    Copy-Item -Path (Join-Path $SrcDir '*') -Destination $TargetDir -Recurse -Force
    Set-Content -LiteralPath (Join-Path $TargetDir $OwnFlag) -Value 'animestack-owned'
    $script:BundleCount++
    $script:Paths.Add("  $TargetDir")
    Log "Installed bundle: $TargetDir"
}

function Uninstall-Bundle([string]$TargetDir) {
    if (-not $TargetDir -or -not (Test-Path -LiteralPath $TargetDir)) { return }
    if (Remove-Owned $TargetDir) {
        $script:BundleCount++
        Log "Removed: $TargetDir"
    } else {
        Log "Skipped (not provably ours; left untouched): $TargetDir"
        $script:SkipCount++
    }
}

function Write-MergePlan {
    $bundleDir = Get-DshBundleDir
    $profileDir = Get-DshProfileDir
    $json = Join-Path $profileDir 'package.json'
    $patch = Join-Path $profileDir 'cordis.patch.yml'
    Log ''
    Log 'The DSH surface is installed. To load it, add two keys to the host profile'
    Log '(the default install never edits a file it cannot prove it owns):'
    Log "  $json"
    Log "    dependencies:  `"animestack-house-presets`": `"link:$bundleDir`""
    Log '    dsh.profile.bundles:  append "animestack-house-presets"'
    Log "  $patch"
    Log "    append the agent-team row from $bundleDir\profile.patch.yml (only when absent)"
    Log '  Re-run with -MergeProfile to perform exactly those edits, or paste them by hand.'
}

function Write-JsonFile([string]$Path, $Data) {
    $text = ($Data | ConvertTo-Json -Depth 12) + "`n"
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $text, $utf8)
    Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json | Out-Null
}

function Merge-Profile {
    $profileDir = Get-DshProfileDir
    $bundleDir = Get-DshBundleDir
    $json = Join-Path $profileDir 'package.json'
    if (-not (Test-Path -LiteralPath $json)) {
        Log "Skipped profile merge (no package.json at $json)"
        $script:SkipCount++
        return
    }
    try {
        $data = Get-Content -LiteralPath $json -Raw | ConvertFrom-Json
    } catch {
        Log "Skipped profile merge (the profile JSON did not parse); merge by hand."
        $script:SkipCount++
        return
    }
    if (-not $data.PSObject.Properties['dsh']) {
        $data | Add-Member -NotePropertyName dsh -NotePropertyValue ([pscustomobject]@{})
    }
    if (-not $data.dsh.PSObject.Properties['profile']) {
        $data.dsh | Add-Member -NotePropertyName profile -NotePropertyValue ([pscustomobject]@{})
    }
    if (-not $data.dsh.profile.PSObject.Properties['bundles']) {
        $data.dsh.profile | Add-Member -NotePropertyName bundles -NotePropertyValue @()
    }
    if (-not $data.PSObject.Properties['dependencies']) {
        $data | Add-Member -NotePropertyName dependencies -NotePropertyValue ([pscustomobject]@{})
    }
    $link = 'link:' + ($bundleDir -replace '\\', '/')
    $changed = $false
    if (-not $data.dependencies.PSObject.Properties['animestack-house-presets']) {
        $data.dependencies | Add-Member -NotePropertyName 'animestack-house-presets' -NotePropertyValue $link
        $changed = $true
    }
    $bundles = @($data.dsh.profile.bundles)
    if ($bundles -notcontains 'animestack-house-presets') {
        $bundles += 'animestack-house-presets'
        $data.dsh.profile.bundles = $bundles
        $changed = $true
    }
    if (-not $changed) {
        Log 'Profile already carries the bundle; nothing to merge.'
        return
    }
    $backup = $json + '.animestack-bak'
    if (-not (Test-Path -LiteralPath $backup)) {
        Copy-Item -LiteralPath $json -Destination $backup -Force
    }
    Write-JsonFile $json $data
    $script:MergeCount++
    Log "Merged the bundle into $json (backup: $backup)"
}

function Merge-ProfilePatch {
    $profileDir = Get-DshProfileDir
    $block = Join-Path (Get-DshBundleSrc) 'profile.patch.yml'
    $patch = Join-Path $profileDir 'cordis.patch.yml'
    if (-not (Test-Path -LiteralPath $patch)) {
        Log "Skipped the agent-team row (no cordis.patch.yml at $patch)."
        $script:SkipCount++
        return
    }
    $lines = Get-Content -LiteralPath $patch
    if ($lines -contains '# >>> animestack >>>') {
        Log 'Profile patch already carries the animestack block; nothing to merge.'
        return
    }
    if ($lines | Where-Object { $_ -match '^\s*- id: agent-team\s*$' }) {
        Log 'Profile patch already carries an agent-team row; the roster cap is left as the host set it.'
        return
    }
    $blockLines = Get-Content -LiteralPath $block
    $start = [Array]::IndexOf($blockLines, '# >>> animestack >>>')
    $end = [Array]::IndexOf($blockLines, '# <<< animestack <<<')
    if ($start -lt 0 -or $end -lt $start) {
        Log "Skipped the agent-team row (the fragment has no markers): $block"
        $script:SkipCount++
        return
    }
    $append = @('') + $blockLines[$start..$end]
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::AppendAllText($patch, (($append -join "`n") + "`n"), $utf8)
    $script:MergeCount++
    Log "Merged the agent-team roster row into $patch"
}

function Unmerge-Profile {
    $profileDir = Get-DshProfileDir
    $json = Join-Path $profileDir 'package.json'
    if (-not (Test-Path -LiteralPath $json)) { return }
    try {
        $data = Get-Content -LiteralPath $json -Raw | ConvertFrom-Json
    } catch {
        Log 'Skipped profile unmerge (the profile JSON did not parse); remove the two keys by hand.'
        $script:SkipCount++
        return
    }
    $changed = $false
    if ($data.PSObject.Properties['dependencies'] -and $data.dependencies.PSObject.Properties['animestack-house-presets']) {
        $data.dependencies.PSObject.Properties.Remove('animestack-house-presets')
        $changed = $true
    }
    if ($data.PSObject.Properties['dsh'] -and $data.dsh.PSObject.Properties['profile'] -and $data.dsh.profile.PSObject.Properties['bundles']) {
        $kept = @($data.dsh.profile.bundles | Where-Object { $_ -ne 'animestack-house-presets' })
        if ($kept.Count -ne @($data.dsh.profile.bundles).Count) {
            $data.dsh.profile.bundles = $kept
            $changed = $true
        }
    }
    if (-not $changed) { return }
    Write-JsonFile $json $data
    $script:MergeCount++
    Log "Removed the bundle keys from $json"
}

function Unmerge-ProfilePatch {
    $profileDir = Get-DshProfileDir
    $patch = Join-Path $profileDir 'cordis.patch.yml'
    if (-not (Test-Path -LiteralPath $patch)) { return }
    $lines = Get-Content -LiteralPath $patch
    if ($lines -notcontains '# >>> animestack >>>') { return }
    $kept = New-Object System.Collections.Generic.List[string]
    $inside = $false
    foreach ($line in $lines) {
        if ($line -eq '# >>> animestack >>>') { $inside = $true; continue }
        if ($line -eq '# <<< animestack <<<') { $inside = $false; continue }
        if (-not $inside) { $kept.Add($line) }
    }
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($patch, (($kept -join "`n") + "`n"), $utf8)
    $script:MergeCount++
    Log "Removed the animestack block from $patch"
}

function Expand-Hosts([string]$Name) {
    if ($Name -eq 'all') { return $AllHosts }
    if ($Name -eq 'auto') {
        $matched = @()
        foreach ($candidate in $AutoHosts) {
            $d = Get-HostConfigDir $candidate
            if ($d -and (Test-Path -LiteralPath $d)) { $matched += $candidate }
        }
        return $matched
    }
    return @($Name)
}

function Test-Ours([string]$Target) {
    if (-not (Test-Path -LiteralPath $Target)) { return $false }
    $item = Get-Item -LiteralPath $Target -Force
    if ($item.LinkType) {
        $linkTarget = $item.Target
        if ($linkTarget -is [array]) { $linkTarget = $linkTarget[0] }
        if (-not $linkTarget) { return $false }
        try { $resolved = (Resolve-Path -LiteralPath $linkTarget).Path } catch { $resolved = $linkTarget }
        $prefix = $Root.TrimEnd('\', '/') + [IO.Path]::DirectorySeparatorChar
        return $resolved.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)
    }
    if ($item.PSIsContainer) {
        return (Test-Path -LiteralPath (Join-Path $Target $OwnFlag) -PathType Leaf)
    }
    return $false
}

function Remove-Owned([string]$Target) {
    if (-not (Test-Ours $Target)) { return $false }
    $item = Get-Item -LiteralPath $Target -Force
    if ($item.LinkType) {
        $item.Delete()
    } elseif ($item.PSIsContainer) {
        Remove-Item -LiteralPath $Target -Recurse -Force
    } else {
        Remove-Item -LiteralPath $Target -Force
    }
    return $true
}

function Copy-Skill([string]$Name, [string]$Target) {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Target) | Out-Null
    Copy-Item -LiteralPath (Join-Path $Root "skills\$Name") -Destination $Target -Recurse -Force
    Set-Content -LiteralPath (Join-Path $Target $RootFlag) -Value $Root
    Set-Content -LiteralPath (Join-Path $Target $OwnFlag) -Value 'animestack-owned'
}

function Install-Skill([string]$Name, [string]$Target) {
    if (Test-Path -LiteralPath $Target) {
        if (Test-Ours $Target) {
            Remove-Owned $Target | Out-Null
        } else {
            Log "Not registered (a skill you own already uses the name; left untouched): $Name"
            $script:SkipCount++
            return
        }
    }
    Copy-Skill $Name $Target
    $script:SkillCount++
    $script:Paths.Add("  $Target")
    Log "Installed (copy): $Name -> $Target"
}

function Install-Digest([string]$HostName, [string]$Target) {
    $source = Join-Path $Root 'AGENTS.md'
    if (-not (Test-Path -LiteralPath $source) -or (Get-Item -LiteralPath $source).Length -eq 0) {
        throw "the digest source $source is missing or empty; refusing to install a digest that claims a file it does not carry ($HostName)"
    }
    if (Test-Path -LiteralPath $Target) {
        if (Test-Ours $Target) {
            Remove-Owned $Target | Out-Null
        } else {
            Log "Not registered (a directory you own already uses the name; left untouched): $HostName/animestack"
            $script:SkipCount++
            return
        }
    }
    New-Item -ItemType Directory -Force -Path $Target | Out-Null
    Copy-Item -LiteralPath $source -Destination (Join-Path $Target 'AGENTS.md') -Force
    $readme = @"
# AnimeStack (digest for $HostName)

AnimeStack is installed here as a rules-only digest: the house voice lives in
AGENTS.md, and the full skill pack (eight seat skills, the /house router, the
/simple waiver, playbooks, principles, and agents) lives in the source repo.

Repo: https://github.com/JerkyJesse/AnimeStack

Refresh: re-run setup.ps1 -TargetHost $HostName from a clone of the repo.
"@
    Set-Content -LiteralPath (Join-Path $Target 'README.md') -Value $readme
    Set-Content -LiteralPath (Join-Path $Target $OwnFlag) -Value 'animestack-owned'
    $script:DigestCount++
    $script:Paths.Add("  $Target")
    Log "Installed digest: $HostName -> $Target"
}

function Get-OwnMarker([string]$File) {
    if ($File.EndsWith('.toml', [StringComparison]::OrdinalIgnoreCase)) { return $TomlMarker }
    return $OwnMarker
}

function Get-LastLine([string]$File) {
    $last = Get-Content -LiteralPath $File -Tail 1 -ErrorAction SilentlyContinue
    if ($null -eq $last) { return '' }
    return $last.TrimEnd()
}

function Install-Agents([string]$HostName, [string]$SrcDir, [string]$TargetDir) {
    if (-not (Test-Path -LiteralPath $SrcDir)) { return }
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    foreach ($src in Get-ChildItem -LiteralPath $SrcDir -File) {
        $base = $src.Name
        $dst = Join-Path $TargetDir $base
        $marker = Get-OwnMarker $dst
        if (Test-Path -LiteralPath $dst) {
            if ((Get-LastLine $dst) -ne $marker) {
                Log "Not registered (an agent file you own already uses the name; left untouched): $base"
                $script:SkipCount++
                continue
            }
        }
        Copy-Item -LiteralPath $src.FullName -Destination $dst -Force
        $script:AgentCount++
        Log "Installed agent: $base -> $dst"
    }
}

function Uninstall-Skill([string]$Name, [string]$Target) {
    if (Test-Path -LiteralPath $Target) {
        if (Remove-Owned $Target) {
            $script:SkillCount++
            Log "Removed: $Target"
        } else {
            Log "Skipped (not provably ours; left untouched): $Target"
            $script:SkipCount++
        }
    }
}

function Uninstall-Digest([string]$Target) {
    if (Test-Path -LiteralPath $Target) {
        if (Remove-Owned $Target) {
            $script:DigestCount++
            Log "Removed: $Target"
        } else {
            Log "Skipped (not provably ours; left untouched): $Target"
            $script:SkipCount++
        }
    }
}

function Uninstall-Agents([string]$TargetDir) {
    if (-not (Test-Path -LiteralPath $TargetDir)) { return }
    foreach ($file in Get-ChildItem -LiteralPath $TargetDir -File) {
        $marker = Get-OwnMarker $file.FullName
        if ((Get-LastLine $file.FullName) -eq $marker) {
            Remove-Item -LiteralPath $file.FullName -Force
            $script:AgentCount++
            Log "Removed: $($file.FullName)"
        }
    }
}

function Install-Commands([string]$HostName, [string]$SrcDir, [string]$TargetDir) {
    if (-not (Test-Path -LiteralPath $SrcDir)) { return }
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    foreach ($src in Get-ChildItem -LiteralPath $SrcDir -File) {
        $base = $src.Name
        $dst = Join-Path $TargetDir $base
        if (Test-Path -LiteralPath $dst) {
            if ((Get-LastLine $dst) -ne $OwnMarker) {
                Log "Not registered (a command file you own already uses the name; left untouched): $base"
                $script:SkipCount++
                continue
            }
        }
        Copy-Item -LiteralPath $src.FullName -Destination $dst -Force
        $script:CommandCount++
        Log "Installed command: $base -> $dst"
    }
}

function Uninstall-Commands([string]$TargetDir) {
    if (-not (Test-Path -LiteralPath $TargetDir)) { return }
    foreach ($file in Get-ChildItem -LiteralPath $TargetDir -File) {
        if ((Get-LastLine $file.FullName) -eq $OwnMarker) {
            Remove-Item -LiteralPath $file.FullName -Force
            $script:CommandCount++
            Log "Removed: $($file.FullName)"
        }
    }
}

function Do-Host([string]$HostName) {
    # One host, one install: slate is a compatibility alias for claude, and a
    # host already installed in this run is not installed twice (that was how
    # -TargetHost all printed 70 skills and 56 agents against a tree of 60/48).
    if ($script:DoneHosts -contains $HostName) { return }
    $script:DoneHosts += $HostName
    if ($HostName -eq 'slate') {
        Do-Host 'claude'
        Log 'Slate reads .claude/skills; claude install refreshed.'
        return
    }
    if ($HostName -eq 'openclaw' -or $HostName -eq 'hermes' -or $HostName -eq 'gbrain') {
        if ($Uninstall) { Uninstall-Digest (Get-HostDigestDir $HostName) }
        else { Install-Digest $HostName (Get-HostDigestDir $HostName) }
        return
    }
    if ($HostName -eq 'dsh') {
        $skillsDir = Get-HostSkillsDir 'dsh'
        if ($Uninstall) {
            if ($skillsDir) { foreach ($skill in $Skills) { Uninstall-Skill $skill (Join-Path $skillsDir $skill) } }
            Uninstall-Packs (Get-DshPacksDir)
            Uninstall-Bundle (Get-DshBundleDir)
            if ($MergeProfile) {
                Unmerge-Profile
                Unmerge-ProfilePatch
            }
            return
        }
        if ($skillsDir) { foreach ($skill in $Skills) { Install-Skill $skill (Join-Path $skillsDir $skill) } }
        Install-Packs (Get-DshPacksSrc) (Get-DshPacksDir)
        Install-Bundle (Get-DshBundleSrc) (Get-DshBundleDir)
        Write-MergePlan
        if ($MergeProfile) {
            Merge-Profile
            Merge-ProfilePatch
        }
        return
    }

    $skillsDir = Get-HostSkillsDir $HostName
    $agentsDir = Get-HostAgentsDir $HostName
    $agentsSrc = Get-HostAgentsSrc $HostName
    $commandsDir = Get-HostCommandsDir $HostName
    $commandsSrc = Get-HostCommandsSrc $HostName

    if ($Uninstall) {
        if ($skillsDir) {
            foreach ($skill in $Skills) { Uninstall-Skill $skill (Join-Path $skillsDir $skill) }
        }
        if ($agentsDir) { Uninstall-Agents $agentsDir }
        if ($commandsDir) { Uninstall-Commands $commandsDir }
        return
    }

    if ($skillsDir) {
        foreach ($skill in $Skills) { Install-Skill $skill (Join-Path $skillsDir $skill) }
    }
    if ($agentsSrc -and $agentsDir) { Install-Agents $HostName $agentsSrc $agentsDir }
    if ($commandsSrc -and $commandsDir) { Install-Commands $HostName $commandsSrc $commandsDir }
}

function Get-FrontmatterLines([string]$File) {
    $lines = Get-Content -LiteralPath $File
    $inFrontmatter = $false
    $result = New-Object System.Collections.Generic.List[string]
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i].TrimEnd() -eq '---') {
            if (-not $inFrontmatter) { $inFrontmatter = $true; continue }
            break
        }
        if ($inFrontmatter) { $result.Add($lines[$i]) }
    }
    return $result
}

function Assert-NoModelPins {
    $bad = 0
    $rootPrefix = $Root.TrimEnd('\', '/') + '\'

    $omitMd = @(
        (Join-Path $Root 'agents\opencode'),
        (Join-Path $Root 'agents\opencode\command'),
        (Join-Path $Root 'agents\factory\command')
    )
    $inheritMd = @(
        (Join-Path $Root 'agents\claude'),
        (Join-Path $Root 'agents\factory')
    )

    foreach ($dir in @((Join-Path $Root 'agents\cursor'), (Join-Path $Root 'agents\kiro'))) {
        if (-not (Test-Path -LiteralPath $dir)) { continue }
        foreach ($file in Get-ChildItem -LiteralPath $dir -File -Filter '*.md') {
            foreach ($line in Get-FrontmatterLines $file.FullName) {
                if ($line -match '^\s*model\s*:') {
                    Write-Error -ErrorAction Continue "model pin in shipped agent (omit the key; the host inherits the session model): $($file.FullName.Replace($rootPrefix, ''))"
                    $bad++
                }
            }
        }
    }
    foreach ($dir in $omitMd) {
        if (-not (Test-Path -LiteralPath $dir)) { continue }
        foreach ($file in Get-ChildItem -LiteralPath $dir -File -Filter '*.md') {
            foreach ($line in Get-FrontmatterLines $file.FullName) {
                if ($line -match '^\s*model\s*:') {
                    Write-Error -ErrorAction Continue "model pin in shipped agent (omit the key; the host inherits the session model): $($file.FullName.Replace($rootPrefix, ''))"
                    $bad++
                }
            }
        }
    }
    foreach ($dir in $inheritMd) {
        if (-not (Test-Path -LiteralPath $dir)) { continue }
        foreach ($file in Get-ChildItem -LiteralPath $dir -File -Filter '*.md') {
            $modelLines = @(Get-FrontmatterLines $file.FullName | Where-Object { $_ -match '^\s*model\s*:' })
            $where = $file.FullName.Replace($rootPrefix, '')
            if ($modelLines.Count -ne 1) {
                Write-Error -ErrorAction Continue "shipped agent needs exactly one 'model: inherit' line (found $($modelLines.Count)): $where"
                $bad++
            } elseif ($modelLines[0] -notmatch '^\s*model\s*:\s*inherit\s*$') {
                Write-Error -ErrorAction Continue "concrete model pin in shipped agent (only 'model: inherit' is allowed): $where"
                $bad++
            }
        }
    }
    $codexDir = Join-Path $Root 'agents\codex'
    if (Test-Path -LiteralPath $codexDir) {
        foreach ($file in Get-ChildItem -LiteralPath $codexDir -File -Filter '*.toml') {
            foreach ($line in Get-Content -LiteralPath $file.FullName) {
                if ($line -match '^\s*model(_reasoning_effort)?\s*=') {
                    Write-Error -ErrorAction Continue "model pin in shipped codex agent (omit model and model_reasoning_effort; codex inherits the spawning session's model): $($file.FullName.Replace($rootPrefix, ''))"
                    $bad++
                }
            }
        }
    }

    if ($bad -ne 0) {
        Write-Output 'Refusing to install from this pack: fix the agent frontmatter first.'
        exit 1
    }
}

if ($Help) {
    Write-Usage
    exit 0
}

if ($TargetHost -notin @('claude', 'cursor', 'codex', 'factory', 'opencode', 'kiro', 'slate', 'openclaw', 'hermes', 'gbrain', 'dsh', 'all', 'auto')) {
    Write-Output "Error: unknown -TargetHost value: $TargetHost"
    Write-Usage
    exit 1
}

if ($MergeProfile -and $TargetHost -notin @('dsh', 'all')) {
    Write-Output 'Error: -MergeProfile only applies to the dsh host'
    exit 1
}

function Write-DryRun {
    Log 'AnimeStack check: no files will be written.'
    Log "Root: $Root"
    Log ''
    $hosts = Expand-Hosts $TargetHost
    if ($hosts.Count -eq 0) {
        Log 'No hosts matched (auto found no existing config dirs). Nothing would be done.'
        Log ''
        Log 'check: pack valid; nothing written.'
        return
    }
    foreach ($h in $hosts) {
        switch ($h) {
            'slate' { Log 'host slate: delegates to claude' }
            { $_ -in @('openclaw', 'hermes', 'gbrain') } {
                Log "host ${h}: digest -> $(Get-HostDigestDir $h)"
            }
            'dsh' {
                $cfg = Get-HostConfigDir 'dsh'
                $packs = @(Get-ChildItem -LiteralPath (Get-DshPacksSrc) -File -Filter 'animestack-*.md' -ErrorAction SilentlyContinue).Count
                $bundle = @(Get-ChildItem -LiteralPath (Get-DshBundleSrc) -Recurse -File -ErrorAction SilentlyContinue).Count
                Log "host dsh: skills $($Skills.Count) -> $(Join-Path $cfg 'skills'); packs $packs -> $(Join-Path $cfg 'animestack-team'); bundle $bundle -> $(Join-Path $cfg 'animestack')"
                Log 'host dsh: profile merge printed only (no writes); -MergeProfile performs it'
            }
            default {
                $asrc = Get-HostAgentsSrc $h
                $adir = Get-HostAgentsDir $h
                $acount = 0
                if ($asrc -and (Test-Path -LiteralPath $asrc)) {
                    $acount = @(Get-ChildItem -LiteralPath $asrc -File).Count
                }
                $csrc = Get-HostCommandsSrc $h
                $cdir = Get-HostCommandsDir $h
                $ccount = 0
                if ($csrc -and (Test-Path -LiteralPath $csrc)) {
                    $ccount = @(Get-ChildItem -LiteralPath $csrc -File -Filter '*.md').Count
                }
                Log "host ${h}: skills $($Skills.Count) -> $(Get-HostSkillsDir $h); agents $acount -> $adir; commands $ccount -> $cdir"
            }
        }
    }
    Log ''
    Log 'check: pack valid; nothing written.'
}

if ((-not $Uninstall) -or $Check) {
    Assert-NoModelPins
}

if ($Check) {
    Write-DryRun
    exit 0
}

Log "AnimeStack: root $Root"
Log ''

$Hosts = Expand-Hosts $TargetHost

if ($Hosts.Count -eq 0) {
    Log 'No hosts matched (auto found no existing config dirs). Nothing to do.'
}

foreach ($entry in $Hosts) {
    Do-Host $entry
}

Log ''
Log 'Copied (no symlinks). Re-run setup.ps1 after git pull to refresh.'
Log ''

if ($Uninstall) {
    Write-Output 'AnimeStack uninstall complete.'
    Write-Output "  skills removed:   $script:SkillCount"
    Write-Output "  agents removed:   $script:AgentCount"
    Write-Output "  commands removed: $script:CommandCount"
    Write-Output "  digests removed:  $script:DigestCount"
    Write-Output "  seat packs removed: $script:PackCount"
    Write-Output "  bundles removed:  $script:BundleCount"
    Write-Output "  profile edits reversed: $script:MergeCount"
    Write-Output "  skipped (not ours): $script:SkipCount"
} else {
    Write-Output 'AnimeStack setup complete.'
    Write-Output "  skills installed:  $script:SkillCount"
    Write-Output "  agents installed:  $script:AgentCount"
    Write-Output "  commands installed: $script:CommandCount"
    Write-Output "  digests installed: $script:DigestCount"
    Write-Output "  seat packs installed: $script:PackCount"
    Write-Output "  bundles installed: $script:BundleCount"
    Write-Output "  profile edits made: $script:MergeCount"
    Write-Output "  skipped (not ours): $script:SkipCount"
    if ($Paths.Count -gt 0) {
        Write-Output 'Targets:'
        foreach ($path in $Paths) { Write-Output $path }
    }
    Write-Output 'Open a new session and run /house.'
}
