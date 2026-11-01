# OdissRea Clean-Room Installer for Windows / PowerShell
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $scriptDir) { $scriptDir = (Get-Location).Path }

Write-Host "Installing OdissRea Clean-Room Suite..." -ForegroundColor Cyan

# 1. Target Skills Directories
$targetDirs = @(
    "$HOME\.gemini\config\skills",
    "$HOME\.claude\skills",
    "$HOME\.config\opencode\skills"
)

foreach ($dir in $targetDirs) {
    Get-ChildItem -Path "$scriptDir\skills" -Directory | ForEach-Object {
        $dest = Join-Path $dir $_.Name
        New-Item -ItemType Directory -Force -Path $dest | Out-Null
        # Copying the contents, not the folder: Copy-Item nests into an existing destination
        Copy-Item -Path (Join-Path $_.FullName "*") -Destination $dest -Recurse -Force
    }
    Write-Host "[OK] Installed Skills -> $dir" -ForegroundColor Green
}

# 2. Merge MCP Server into ~/.gemini/config/mcp_config.json
& python (Join-Path $scriptDir "mcp\install_mcp_config.py")
if ($LASTEXITCODE -ne 0) { throw "MCP configuration failed" }

Write-Host "Installation complete. The server path points to this clone: keep it in place." -ForegroundColor Green
