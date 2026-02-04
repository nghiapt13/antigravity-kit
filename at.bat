@echo off
rem Antigravity CLI Wrapper

if "%1"=="init" (
    python "%~dp0init_project.py" %2
) else (
    python "%~dp0core\engine.py" %*
)
