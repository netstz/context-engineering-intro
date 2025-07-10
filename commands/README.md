# OpenCode Command Executor

A Python script that mimics ClaudeCode's command system by reading command markdown files and executing them with OpenCode.

## Features

- **Direct ClaudeCode Compatibility**: Reads original `.md` command files
- **Variable Substitution**: Handles `$ARGUMENTS` and other variables
- **Command Discovery**: Automatically finds commands in the `commands/` directory
- **OpenCode Integration**: Uses `opencode run` for execution
- **Rich CLI**: Verbose output, session continuation, help system

## Usage

### Basic Commands

```bash
# List available commands
python3 opencode-cmd.py --list

# Execute generate-prp command
python3 opencode-cmd.py generate-prp INITIAL.md

# Execute execute-prp command
python3 opencode-cmd.py execute-prp PRPs/feature.md
```

### Advanced Options

```bash
# Verbose output
python3 opencode-cmd.py generate-prp INITIAL.md --verbose

# Continue previous OpenCode session
python3 opencode-cmd.py execute-prp PRPs/feature.md --continue-session

# Use custom commands directory
python3 opencode-cmd.py generate-prp INITIAL.md --commands-dir ./my-commands

# Get help
python3 opencode-cmd.py --help
```

## Command File Format

Command files are markdown files that follow this structure:

```markdown
# Command Title

Brief description of what the command does.

## Section with $ARGUMENTS

The $ARGUMENTS variable will be replaced with the arguments passed to the command.

## Instructions

Detailed instructions for the AI agent to follow.
```

### Variable Substitution

- `$ARGUMENTS` - Replaced with all command-line arguments joined by spaces
- `${ARGUMENTS}` - Alternative syntax for the same substitution

## Available Commands

The script automatically discovers commands from the `commands/` directory:

- `generate-prp.md` → `generate-prp` command
- `execute-prp.md` → `execute-prp` command

## Examples

### Generate PRP Example

```bash
python3 opencode-cmd.py generate-prp INITIAL.md
```

This will:
1. Read `commands/generate-prp.md`
2. Replace `$ARGUMENTS` with `INITIAL.md`
3. Construct a comprehensive prompt
4. Execute via `opencode run`

### Execute PRP Example

```bash
python3 opencode-cmd.py execute-prp PRPs/multi-agent-system.md --verbose
```

This will:
1. Read `commands/execute-prp.md`
2. Replace `$ARGUMENTS` with `PRPs/multi-agent-system.md`
3. Show verbose output during execution
4. Execute the PRP implementation via `opencode run`

## Error Handling

The script includes comprehensive error handling:

- ✅ Validates OpenCode installation
- ✅ Checks command file existence
- ✅ Validates arguments
- ✅ Provides helpful error messages
- ✅ Graceful handling of interruptions

## Installation Requirements

- Python 3.6+
- OpenCode installed and in PATH
- Command files in `commands/` directory

## Comparison with Original Scripts

| Feature | Original Scripts | opencode-cmd.py |
|---------|-----------------|-----------------|
| Command source | Hardcoded prompts | Reads .md files |
| Flexibility | Fixed implementation | Dynamic command discovery |
| ClaudeCode compatibility | Approximation | Direct translation |
| Variable substitution | Manual | Automatic |
| Command management | Static | Dynamic discovery |

This approach provides the closest possible emulation of ClaudeCode's command system while working with OpenCode.