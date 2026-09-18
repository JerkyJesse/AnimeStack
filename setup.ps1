# AnimeStack setup.ps1 - install the seven-seat house skills, agents, and the
# /house commands into supported AI coding hosts on Windows. The native entry
# point beside ./setup (bash); same contract, same ownership gate, same model
# rule. No network, no admin, no node.
#
# The cage rule: never delete or edit a target without proof that we own it.
# A skill target is ours when it is a link resolving into this repo, or a
# directory carrying the .animestack-owned marker. An agent file is ours when
# its last line is the right ownership marker (HTML comment for markdown
# agents, TOML comment for codex agents). Everything else is left untouched.
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
    [switch]$Quiet,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path

$Skills = @('house', 'reika', 'mei', 'elo', 'yui', 'niko', 'rin', 'aria', 'simple')
$AllHosts = @('claude', 'cursor', 'codex', 'factory', 'opencode', 'kiro', 'slate', 'openclaw', 'hermes', 'gbrain')
$AutoHosts = @('claude', 'cursor', 'codex', 'factory', 'opencode', 'kiro', 'openclaw', 'hermes', 'gbrain')

$OwnMarker = '<!-- animestack-owned -->'
$TomlMarker = '# animestack-owned'
$OwnFlag = '.animestack-owned'
$RootFlag = '.animestack-root'

$SkillCount = 0
$AgentCount = 0
$CommandCount = 0
$DigestCount = 0
$SkipCount = 0
$Paths = New-Object System.Collections.Generic.List[string]

function Write-Usage {
    Write-Output @'
AnimeStack setup.ps1 - install the seven-seat house skills, agents, and the
/house commands into AI hosts (native Windows entry point beside ./setup)

Usage: .\setup.ps1 [-TargetHost <name>] [-Uninstall] [-Quiet] [-Help]

Options:
  -TargetHost <name>  Target host: claude, cursor, codex, factory, opencode,
                      kiro, slate, openclaw, hermes, gbrain, all, auto.
                      Default: claude. (-Host is an alias.)
  -Uninstall          Remove only provably-owned AnimeStack items for the
                      selected host(s). Everything else is left untouched.
  -Quiet              Suppress progress output; print only the final summary.
  -Help               Show this help and exit.

Examples:
  .\setup.ps1                          # install for Claude Code
  .\setup.ps1 opencode                 # opencode skills + agents + command
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
    Copy-Item -LiteralPath (Join-Path $Root 'AGENTS.md') -Destination (Join-Path $Target 'AGENTS.md') -Force
    $readme = @"
# AnimeStack (digest for $HostName)

AnimeStack is installed here as a rules-only digest: the house voice lives in
AGENTS.md, and the full skill pack (seven seat skills, the /house router, the
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

if ($TargetHost -notin @('claude', 'cursor', 'codex', 'factory', 'opencode', 'kiro', 'slate', 'openclaw', 'hermes', 'gbrain', 'all', 'auto')) {
    Write-Output "Error: unknown -TargetHost value: $TargetHost"
    Write-Usage
    exit 1
}

if (-not $Uninstall) {
    Assert-NoModelPins
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
    Write-Output "  skills removed:   $SkillCount"
    Write-Output "  agents removed:   $AgentCount"
    Write-Output "  commands removed: $CommandCount"
    Write-Output "  digests removed:  $DigestCount"
    Write-Output "  skipped (not ours): $SkipCount"
} else {
    Write-Output 'AnimeStack setup complete.'
    Write-Output "  skills installed:  $SkillCount"
    Write-Output "  agents installed:  $AgentCount"
    Write-Output "  commands installed: $CommandCount"
    Write-Output "  digests installed: $DigestCount"
    Write-Output "  skipped (not ours): $SkipCount"
    if ($Paths.Count -gt 0) {
        Write-Output 'Targets:'
        foreach ($path in $Paths) { Write-Output $path }
    }
    Write-Output 'Open a new session and run /house.'
}
