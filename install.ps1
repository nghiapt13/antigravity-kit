Write-Host "Installing Antigravity Kit..."

$GeminiDir = "$env:USERPROFILE\.gemini\antigravity"
$KitDir = $PSScriptRoot
$WorkflowDir = "$GeminiDir\global_workflows"

# Ensure directories exist
New-Item -ItemType Directory -Force -Path $WorkflowDir | Out-Null

# Copy Workflows
Copy-Item -Path "$KitDir\workflows\*.md" -Destination $WorkflowDir -Force


# Add to PATH (User)
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($CurrentPath -notlike "*$KitDir*") {
    Write-Host "Adding $KitDir to User PATH..."
    [Environment]::SetEnvironmentVariable("Path", "$CurrentPath;$KitDir", "User")
    Write-Host "✅ Added to PATH. PLEASE RESTART YOUR TERMINAL."
} else {
    Write-Host "✅ Already in PATH."
}

Write-Host "✅ Workflows installed to $WorkflowDir"
Write-Host "✅ Core Engine located at $KitDir\core"
Write-Host "Installation Complete! You can now use 'at' command from anywhere (after restart)."
