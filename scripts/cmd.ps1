# OpenCode Context Engineering Command Runner (Windows PowerShell)
# This script provides a cross-platform way to execute Context Engineering commands

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Try python3 first, then fallback to python
try {
    & python3 "$ScriptDir\cmd.py" @args
}
catch {
    & python "$ScriptDir\cmd.py" @args
}