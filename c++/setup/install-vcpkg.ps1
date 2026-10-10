<#
.SYNOPSIS
    Automated installation script for vcpkg in the current project workspace.
.DESCRIPTION
    Clones Microsoft's vcpkg package manager repository and runs the bootstrap
    script to compile or acquire the vcpkg binary executable.
#>

[CmdletBinding()]
param (
    [string]$TargetDir = ""
)

if ([string]::IsNullOrWhiteSpace($TargetDir)) {
    if ($PSScriptRoot) {
        $TargetDir = Join-Path $PSScriptRoot "vcpkg"
    } else {
        $TargetDir = Join-Path (Get-Location) "vcpkg"
    }
}

$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   Installing vcpkg in: $TargetDir" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Verify Git is available
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git is required to install vcpkg. Please install Git and try again."
    exit 1
}

# 2. Clone vcpkg if directory does not exist
if (-not (Test-Path $TargetDir)) {
    Write-Host "`n[1/3] Cloning vcpkg repository..." -ForegroundColor Yellow
    git clone --depth 1 https://github.com/microsoft/vcpkg.git $TargetDir
} else {
    Write-Host "`n[1/3] vcpkg directory already exists at $TargetDir. Skipping clone." -ForegroundColor Green
}

# 3. Bootstrap vcpkg
$BootstrapScript = Join-Path $TargetDir "bootstrap-vcpkg.bat"
$VcpkgExe = Join-Path $TargetDir "vcpkg.exe"

if (-not (Test-Path $VcpkgExe)) {
    Write-Host "`n[2/3] Running bootstrap script to build/download vcpkg executable..." -ForegroundColor Yellow
    & $BootstrapScript -disableMetrics
} else {
    Write-Host "`n[2/3] vcpkg.exe already exists. Skipping bootstrap." -ForegroundColor Green
}

# 4. Verification
if (Test-Path $VcpkgExe) {
    Write-Host "`n[3/3] vcpkg successfully installed!" -ForegroundColor Green
    & $VcpkgExe version
    Write-Host "`nIntegration with CMake:" -ForegroundColor Cyan
    Write-Host "Toolchain file path: $TargetDir\scripts\buildsystems\vcpkg.cmake" -ForegroundColor Yellow
    Write-Host "Configure command:   cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE=""$TargetDir\scripts\buildsystems\vcpkg.cmake""" -ForegroundColor White
} else {
    Write-Error "Bootstrap completed but vcpkg.exe was not found. Please check logs."
    exit 1
}
