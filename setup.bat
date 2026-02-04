@echo off
setlocal EnableExtensions

echo ==========================================
echo      Antigravity Kit Setup by NghiaPT
echo ==========================================

REM --------------------------------------------------
REM Step 0: Check Python
REM --------------------------------------------------
echo.
echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found.
    echo Please install Python and ensure it is added to PATH.
    pause
    exit /b 1
)

REM --------------------------------------------------
REM Step 1: Install Python dependencies
REM --------------------------------------------------
if not exist "%~dp0requirements.txt" (
    echo [ERROR] requirements.txt not found.
    pause
    exit /b 1
)

echo.
echo [1/3] Installing Python dependencies...
python -m pip install -r "%~dp0requirements.txt"
if errorlevel 1 (
    echo [ERROR] Failed to install Python dependencies.
    pause
    exit /b 1
)

REM --------------------------------------------------
REM Step 2: Run PowerShell installer
REM --------------------------------------------------
if not exist "%~dp0install.ps1" (
    echo [ERROR] install.ps1 not found.
    pause
    exit /b 1
)

echo.
echo [2/3] Running PowerShell installer...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1"
if errorlevel 1 (
    echo [ERROR] PowerShell installer failed.
    pause
    exit /b 1
)

REM --------------------------------------------------
REM Step 3: Verify Core Engine
REM --------------------------------------------------
if not exist "%~dp0core\engine.py" (
    echo [ERROR] Core engine not found.
    pause
    exit /b 1
)

echo.
echo [3/3] Verifying core engine...
python "%~dp0core\engine.py" --help >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Core engine failed to run.
    pause
    exit /b 1
)

REM --------------------------------------------------
REM Step 4: Verify CLI wrapper (no PATH dependency)
REM --------------------------------------------------
echo.
echo Verifying CLI wrapper...
call "%~dp0at.bat" --help >nul 2>&1
if errorlevel 1 (
    echo [ERROR] CLI wrapper failed.
    pause
    exit /b 1
)


REM --------------------------------------------------
REM Done
REM --------------------------------------------------
echo.
echo ==========================================
echo  Antigravity Kit installed successfully!
echo ==========================================
echo You can now use the 'at' command anywhere.
echo (If this is your first install, restart your terminal.)
echo.

pause
endlocal
