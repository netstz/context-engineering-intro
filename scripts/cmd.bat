@echo off
REM OpenCode Context Engineering Command Runner (Windows Batch)
REM This script provides a cross-platform way to execute Context Engineering commands

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Try python3 first, then fallback to python
python3 "%SCRIPT_DIR%cmd.py" %* 2>nul
if %errorlevel% neq 0 (
    python "%SCRIPT_DIR%cmd.py" %*
)