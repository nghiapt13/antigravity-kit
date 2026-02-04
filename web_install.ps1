<#
.SYNOPSIS
    Antigravity Kit Web Installer
    Usage: iex (irm raw_url_to_this_script)
#>

$ErrorActionPreference = "Stop"

$RepoUrl = "https://github.com/hungpixi/antigravity-kit/archive/refs/heads/main.zip"
$InstallDir = "$env:USERPROFILE\.gemini\antigravity\antigravity-kit"
$TempZip = "$env:TEMP\antigravity-kit.zip"

Write-Host "🚀 Starting Antigravity Kit Installation..." -ForegroundColor Cyan

# 1. Clean old install
if (Test-Path $InstallDir) {
    Write-Host "   Cleaning previous installation..." -ForegroundColor Gray
    Remove-Item -Path $InstallDir -Recurse -Force
}

# 2. Download Repository
Write-Host "   Downloading latest version..." -ForegroundColor Gray
try {
    Invoke-WebRequest -Uri $RepoUrl -OutFile $TempZip
} catch {
    Write-Error "Failed to download from GitHub. Check internet or Repo URL."
}

# 3. Extract
Write-Host "   Extracting files..." -ForegroundColor Gray
Expand-Archive -Path $TempZip -DestinationPath "$env:USERPROFILE\.gemini\antigravity" -Force
$ExtractedName = "$env:USERPROFILE\.gemini\antigravity\antigravity-kit-main"

# 4. Rename/Move to final location
if (Test-Path $ExtractedName) {
    Move-Item -Path $ExtractedName -Destination $InstallDir
}

# 5. Run Local Installer
$LocalInstaller = "$InstallDir\install.ps1"
if (Test-Path $LocalInstaller) {
    Write-Host "   Running configuration..." -ForegroundColor Gray
    & $LocalInstaller
} else {
    Write-Error "Installer script not found in downloaded package!"
}

# 6. Cleanup
Remove-Item $TempZip -Force

Write-Host "`n✅ Antigravity Kit Installed Successfully!" -ForegroundColor Green
Write-Host "   Run 'python $InstallDir\init_project.py .' to bootstrap a new project." -ForegroundColor Yellow
