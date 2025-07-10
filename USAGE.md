# Using OpenCode Commands: Inside and Outside

This guide shows how to use the Context Engineering commands both from the terminal and from within OpenCode sessions.

## Prerequisites

**OpenCode Installation:**
```bash
# Quick install (Linux/macOS/Windows with bash)
curl -fsSL https://opencode.ai/install | bash

# Package managers
npm i -g opencode-ai@latest        # Node.js (cross-platform)
brew install sst/tap/opencode      # macOS
paru -S opencode-bin               # Arch Linux

# Windows: Download from https://github.com/sst/opencode/releases
```

> **Note:** Remove versions older than 0.1.x before installing

## Generic Command System

The `scripts/cmd` tool is completely generic and can execute any command defined in the `commands/` directory. It automatically discovers `.md` files and makes them available as commands.

**Cross-platform executables:**
- **Linux/macOS**: `./scripts/cmd` (shell script)
- **Windows**: `scripts\cmd.bat` (batch file) or `scripts\cmd.ps1` (PowerShell)
- **All platforms**: Direct Python execution via `python3 scripts/cmd.py`

**Adding new commands:**
1. Create a new `.md` file in the `commands/` directory (e.g., `commands/my-command.md`)
2. The command will automatically be available as:
   - Linux/macOS: `./scripts/cmd my-command`
   - Windows: `scripts\cmd.bat my-command` or `scripts\cmd.ps1 my-command`
3. Use `$ARGUMENTS` in your `.md` file to substitute command arguments

**Example custom command (`commands/analyze-code.md`):**
```markdown
# Analyze Code

Please analyze the code in $ARGUMENTS and provide:
- Code quality assessment
- Potential improvements
- Security considerations
```

**Usage:**
```bash
# Linux/macOS
./scripts/cmd analyze-code src/main.py

# Windows (Command Prompt)
scripts\cmd.bat analyze-code src\main.py

# Windows (PowerShell)
scripts\cmd.ps1 analyze-code src\main.py
```

## Option 1: From Terminal (External Usage)

### Basic Commands

**Linux/macOS:**
```bash
# List available commands
./scripts/cmd --list

# Generate PRP
./scripts/cmd generate-prp INITIAL.md

# Execute PRP
./scripts/cmd execute-prp PRPs/feature.md

# Get just the prompt (don't execute)
./scripts/cmd generate-prp INITIAL.md --prompt-only
```

**Windows (Command Prompt):**
```cmd
REM List available commands
scripts\cmd.bat --list

REM Generate PRP
scripts\cmd.bat generate-prp INITIAL.md

REM Execute PRP
scripts\cmd.bat execute-prp PRPs\feature.md

REM Get just the prompt (don't execute)
scripts\cmd.bat generate-prp INITIAL.md --prompt-only
```

**Windows (PowerShell):**
```powershell
# List available commands
scripts\cmd.ps1 --list

# Generate PRP
scripts\cmd.ps1 generate-prp INITIAL.md

# Execute PRP
scripts\cmd.ps1 execute-prp PRPs\feature.md

# Get just the prompt (don't execute)
scripts\cmd.ps1 generate-prp INITIAL.md --prompt-only
```

### Advanced Options

**Linux/macOS:**
```bash
# Verbose output
./scripts/cmd generate-prp INITIAL.md --verbose

# Continue previous session
./scripts/cmd execute-prp PRPs/feature.md --continue-session

# Help
./scripts/cmd --help
```

**Windows:**
```cmd
REM Verbose output (batch)
scripts\cmd.bat generate-prp INITIAL.md --verbose

REM PowerShell syntax is similar
scripts\cmd.ps1 generate-prp INITIAL.md --verbose
```

## Option 2: From Within OpenCode (Internal Usage)

When you're already in an OpenCode session, you can import and use the functions directly:

### Import the Module
```python
# Add the scripts directory to Python path (insert at beginning to avoid conflicts)
import sys
sys.path.insert(0, 'scripts')

# Import the generic command executor
from cmd import execute_command
```

### Use the Functions
```python
# List available commands
commands_list = execute_command("--list")
print(commands_list)

# Execute any command generically
prp_prompt = execute_command("generate-prp", "INITIAL.md")
print("Generated PRP prompt:")
print(prp_prompt)

# Execute PRP command
execute_prompt = execute_command("execute-prp", "PRPs/multi-agent-system.md")
print("Execute PRP prompt:")
print(execute_prompt)

# Execute any custom command you've added to commands/
custom_prompt = execute_command("your-custom-command", ["arg1", "arg2"])
```

### Direct Prompt Usage
You can also get the raw prompt and use it directly:

```python
# Get the prompt without executing
import sys
sys.path.insert(0, 'scripts')
from cmd import ContextEngineering, execute_command

ce = ContextEngineering()
prompt = ce.get_command_prompt("generate-prp", "INITIAL.md")

# Now you can use this prompt however you want within OpenCode
print("Execute this prompt:")
print(prompt)

# Or use the generic execute_command function
prompt = execute_command("generate-prp", "INITIAL.md")
```

## Option 3: Hybrid Approach (Copy-Paste)

If you're in OpenCode and want to use the commands without importing, you can:

1. **Get the prompt from terminal:**
   ```bash
   ./scripts/cmd generate-prp INITIAL.md --prompt-only
   ```

2. **Copy the output and paste it into OpenCode**

3. **Execute within your OpenCode session**

## Option 4: Ask OpenCode to Execute the Script

You can also ask OpenCode to run the script for you:

```
"Please run the command: ./scripts/cmd generate-prp INITIAL.md"
```

OpenCode will execute the script and show you the results.

## Examples in Practice

### From Terminal
```bash
$ ./scripts/cmd --list
Available commands:
  generate-prp         - Create PRP
  execute-prp          - Execute BASE PRP

$ ./scripts/cmd generate-prp INITIAL.md
🚀 Executing command: generate-prp
✅ Command 'generate-prp' completed successfully
```

### From Within OpenCode
```python
# In an OpenCode session
import sys
sys.path.insert(0, 'scripts')
from cmd import execute_command

# List available commands
commands_list = execute_command("--list")
print(commands_list)

# Get the prompt for any command
prompt = execute_command("generate-prp", "INITIAL.md")

# OpenCode can now execute this prompt directly
# The prompt contains all the instructions from commands/generate-prp.md

# You can execute any command from the commands/ directory
custom_prompt = execute_command("your-command", "your-args")
```

### Copy-Paste Approach
```bash
# Terminal
$ ./scripts/cmd generate-prp INITIAL.md --prompt-only
You are executing a Context Engineering command: generate-prp

Command Instructions:
# Create PRP

## Feature file: INITIAL.md
...
```
Then copy this output and paste it into your OpenCode session.

## Which Approach to Use?

- **Terminal usage**: Best for standalone execution and automation
- **Import within OpenCode**: Best for interactive development and customization
- **Copy-paste**: Best for one-off usage when you're already in OpenCode
- **Ask OpenCode to run**: Best for quick execution without leaving OpenCode

## Benefits of Each Approach

### Terminal Usage
✅ Full automation capability  
✅ Can be scripted and scheduled  
✅ Independent of OpenCode session state  
✅ Can use all CLI features (verbose, continue-session, etc.)  

### Internal Usage
✅ Integrates with existing OpenCode workflow  
✅ Can customize and modify prompts programmatically  
✅ No need to leave OpenCode interface  
✅ Can combine with other Python code in the session  

Both approaches give you the same powerful Context Engineering workflow, just with different interfaces!