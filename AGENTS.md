# OpenCode Project Configuration

This file configures the Context Engineering workflow for OpenCode. OpenCode reads this file for project context and rules.

## Context Engineering Workflow

This project implements a two-stage Context Engineering workflow:

1. **PRP Generation**: Research and create comprehensive Product Requirements Prompts
2. **PRP Execution**: Implement features from PRPs with validation

## OpenCode Command Implementation

### OpenCode Command Executor (`scripts/cmd`)

This project provides a comprehensive command executor that works both inside and outside OpenCode sessions, offering exact ClaudeCode command compatibility.

**Installation:**
```bash
# Quick install (Linux/macOS/Windows with bash)
curl -fsSL https://opencode.ai/install | bash

# Package managers
npm i -g opencode-ai@latest        # Node.js (cross-platform)
brew install sst/tap/opencode      # macOS
paru -S opencode-bin               # Arch Linux

# Windows: Download from https://github.com/sst/opencode/releases
```

**Terminal Usage:**
```bash
# Linux/macOS
./scripts/cmd --list
./scripts/cmd generate-prp INITIAL.md
./scripts/cmd execute-prp PRPs/your-feature.md

# Windows (Command Prompt)
scripts\cmd.bat --list
scripts\cmd.bat generate-prp INITIAL.md
scripts\cmd.bat execute-prp PRPs\your-feature.md

# Windows (PowerShell)
scripts\cmd.ps1 --list
scripts\cmd.ps1 generate-prp INITIAL.md
scripts\cmd.ps1 execute-prp PRPs\your-feature.md

# Advanced options (all platforms)
./scripts/cmd generate-prp INITIAL.md --verbose
./scripts/cmd execute-prp PRPs/feature.md --continue-session
./scripts/cmd generate-prp INITIAL.md --prompt-only
```

**OpenCode Session Usage:**
```python
# Import the Context Engineering function
import sys
sys.path.insert(0, 'scripts')
from cmd import execute_command

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
```

**Features:**
- ✅ Direct ClaudeCode compatibility - reads original `.md` command files
- ✅ Automatic `$ARGUMENTS` variable substitution
- ✅ Dynamic command discovery from `commands/` directory
- ✅ Works both inside and outside OpenCode sessions
- ✅ Python module import support
- ✅ Comprehensive error handling
- ✅ Verbose output and session continuation
- ✅ Prompt-only mode for copy-paste workflows
- ✅ Cross-platform support (Linux/macOS/Windows)

### Usage Workflows

#### Workflow 1: Generate PRP from Feature Request

**When to use**: You have a feature request in `INITIAL.md` and want to create a comprehensive PRP.

**Terminal approach:**
```bash
# Linux/macOS
./scripts/cmd generate-prp INITIAL.md

# Windows
scripts\cmd.bat generate-prp INITIAL.md
```

**OpenCode session approach:**
```python
import sys
sys.path.insert(0, 'scripts')
from cmd import execute_command
prompt = execute_command("generate-prp", "INITIAL.md")
# Use the prompt within your OpenCode session
```

**Manual approach:**
```
"Please read INITIAL.md and generate a comprehensive PRP following the PRP Generator workflow in AGENTS.md. Research the codebase, find relevant documentation, and create a detailed implementation blueprint."
```

#### Workflow 2: Execute PRP Implementation

**When to use**: You have a PRP file and want to implement the feature.

**Terminal approach:**
```bash
# Linux/macOS
./scripts/cmd execute-prp PRPs/your-prp-file.md

# Windows
scripts\cmd.bat execute-prp PRPs\your-prp-file.md
```

**OpenCode session approach:**
```python
import sys
sys.path.insert(0, 'scripts')
from cmd import execute_command
prompt = execute_command("execute-prp", "PRPs/your-prp-file.md")
# Use the prompt within your OpenCode session
```

**Manual approach:**
```
"Please read PRPs/[your-prp-file].md and implement the feature following the PRP Executor workflow in AGENTS.md. Use the TodoWrite tool to track progress and validate each step."
```

## PRP Generator Workflow

**Role**: Generate a complete PRP for feature implementation with thorough research.

**Process**:

1. **Read Feature Request**
   - Read the specified feature request file (usually INITIAL.md)
   - Understand requirements, examples, documentation, and considerations
   - Identify what needs to be built and how examples should guide implementation

2. **Research Phase**
   - **Codebase Analysis**: Search for similar features/patterns, identify files to reference, note existing conventions, check test patterns
   - **External Research**: Search for similar features online, find library documentation with URLs, locate implementation examples, identify best practices and pitfalls
   - **Clarification**: Ask user for specific patterns to mirror or integration requirements if needed

3. **PRP Generation**
   - Use PRPs/templates/prp_base.md as template
   - Include **Critical Context**: Documentation URLs, code examples from codebase, library quirks, existing patterns
   - Create **Implementation Blueprint**: Pseudocode approach, file references, error handling strategy
   - List **Ordered Tasks**: Tasks to complete the PRP in implementation order
   - Define **Validation Gates**: Executable commands (e.g., `ruff check --fix && mypy .`, `uv run pytest tests/ -v`)

4. **Quality Check**
   - Ensure all necessary context included
   - Verify validation gates are executable
   - Confirm references to existing patterns
   - Validate clear implementation path
   - Document error handling
   - Score confidence level (1-10) for one-pass implementation success

5. **Output**
   - Save as `PRPs/{feature-name}.md`
   - Goal: One-pass implementation success through comprehensive context

## PRP Executor Workflow

**Role**: Implement a feature using the PRP file with comprehensive validation and error correction.

**Process**:

1. **Load PRP**
   - Read the specified PRP file completely
   - Understand all context and requirements
   - Note all instructions and extend research if needed
   - Ensure complete context for implementation
   - Perform additional web searches and codebase exploration as needed

2. **Plan Implementation**
   - Create comprehensive plan addressing all requirements
   - Break down complex tasks using TodoWrite tool
   - Use TodoWrite to create and track implementation plan
   - Identify implementation patterns from existing code

3. **Execute Implementation**
   - Execute PRP requirements step by step
   - Implement all code following existing patterns
   - Follow existing codebase patterns and conventions
   - Ensure proper error handling and logging
   - Mark todos as in_progress/completed as you work

4. **Validate Continuously**
   - Run each validation command from the PRP
   - Fix any failures immediately
   - Re-run until all validation passes
   - Run linting and type checking
   - Execute all tests

5. **Complete and Verify**
   - Ensure all checklist items are completed
   - Run final validation suite
   - Report completion status
   - Re-read the PRP to ensure everything was implemented

6. **Reference PRP Throughout**
   - Always reference the PRP during implementation
   - Follow the exact specifications provided

**Validation Requirements**:
- All code must pass linting (ruff, mypy, etc.)
- All tests must pass
- No syntax errors
- Follow project conventions from this AGENTS.md file

**Error Handling**: If validation fails, use error patterns in PRP to fix and retry. Always provide clear error messages and fix attempts.

**Note**: Never commit changes unless explicitly requested.

## Project Configuration

### Global Rules (Applied to all OpenCode interactions)

#### 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn't listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.
- **Use appropriate virtual environments** when executing Python commands, including for unit tests.

#### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Use clear, consistent imports** (prefer relative imports within packages).
- **Use python_dotenv and load_env()** for environment variables when applicable.

#### 🧪 Testing & Reliability
- **Always create Pytest unit tests for new features** (functions, classes, routes, etc).
- **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
- **Tests should live in a `/tests` folder** mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case  
    - 1 failure case

#### ✅ Task Completion
- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a "Discovered During Work" section.

#### 📎 Style & Conventions
- **Use Python** as the primary language.
- **Follow PEP8**, use type hints, and format with `black`.
- **Use `pydantic` for data validation**.
- Use `FastAPI` for APIs and `SQLAlchemy` or `SQLModel` for ORM if applicable.
- Write **docstrings for every function** using the Google style:
  ```python
  def example():
      """
      Brief summary.

      Args:
          param1 (type): Description.

      Returns:
          type: Description.
      """
  ```

#### 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.

#### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified Python packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.

## Validation Commands

When implementing features, always run these validation commands:

```bash
# Python projects
ruff check --fix
mypy .
uv run pytest tests/ -v

# Project-specific commands
# Check package.json, pyproject.toml, etc. for additional linting/testing commands
```