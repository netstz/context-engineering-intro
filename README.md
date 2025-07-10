# OpenCode Context Engineering Template

A comprehensive template for getting started with Context Engineering using OpenCode - the discipline of engineering context for AI coding assistants so they have the information necessary to get the job done end to end.

> **Context Engineering is 10x better than prompt engineering and 100x better than vibe coding.**

## 🚀 Quick Start

```bash
# 1. Clone this template
git clone https://github.com/coleam00/Context-Engineering-Intro.git
cd Context-Engineering-Intro

# 2. Install OpenCode
# Choose your preferred installation method:

# Quick install (Linux/macOS/Windows with bash)
curl -fsSL https://opencode.ai/install | bash

# Package managers
npm i -g opencode-ai@latest        # Node.js (cross-platform)
brew install sst/tap/opencode      # macOS
paru -S opencode-bin               # Arch Linux

# Windows direct download (alternative)
# Visit: https://github.com/sst/opencode/releases
# Download latest .exe for Windows

# 3. Describe your feature in INITIAL.md
# Edit INITIAL.md with your specific requirements

# 4. Generate a comprehensive PRP (Product Requirements Prompt)
# Linux/macOS
./scripts/cmd generate-prp INITIAL.md

# Windows (Command Prompt)
scripts\cmd.bat generate-prp INITIAL.md

# Windows (PowerShell)  
scripts\cmd.ps1 generate-prp INITIAL.md

# 5. Execute the PRP to implement your feature
# Linux/macOS
./scripts/cmd execute-prp PRPs/your-feature-name.md

# Windows (Command Prompt)
scripts\cmd.bat execute-prp PRPs\your-feature-name.md

# Windows (PowerShell)
scripts\cmd.ps1 execute-prp PRPs\your-feature-name.md

# Alternative: Use from within OpenCode session
# import sys; sys.path.insert(0, 'scripts')
# from cmd import execute_command
# prompt = execute_command("generate-prp", "INITIAL.md")
```

## 📚 Table of Contents

- [Installation](#installation)
- [What is Context Engineering?](#what-is-context-engineering)
- [Template Structure](#template-structure)
- [OpenCode Command Implementation](#opencode-command-implementation)
- [Step-by-Step Guide](#step-by-step-guide)
- [Writing Effective INITIAL.md Files](#writing-effective-initialmd-files)
- [The PRP Workflow](#the-prp-workflow)
- [Using Examples Effectively](#using-examples-effectively)
- [Best Practices](#best-practices)

## Installation

OpenCode can be installed using several methods depending on your platform and preferences:

### Quick Install (Recommended)
```bash
# Works on Linux, macOS, and Windows (with bash/WSL)
curl -fsSL https://opencode.ai/install | bash
```

### Package Managers
```bash
# Node.js (cross-platform)
npm i -g opencode-ai@latest

# macOS
brew install sst/tap/opencode

# Arch Linux
paru -S opencode-bin
```

### Windows Direct Download
For Windows users who prefer a direct executable download:

1. Visit [OpenCode Releases](https://github.com/sst/opencode/releases)
2. Download the latest Windows executable (`.exe`)
3. Add to your PATH or run directly

### Verification
After installation, verify OpenCode is working:
```bash
opencode --version
```

> **Note:** Remove any versions older than 0.1.x before installing the latest version.

## What is Context Engineering?

Context Engineering represents a paradigm shift from traditional prompt engineering:

### Prompt Engineering vs Context Engineering

**Prompt Engineering:**
- Focuses on clever wording and specific phrasing
- Limited to how you phrase a task
- Like giving someone a sticky note

**Context Engineering:**
- A complete system for providing comprehensive context
- Includes documentation, examples, rules, patterns, and validation
- Like writing a full screenplay with all the details

### Why Context Engineering Matters

1. **Reduces AI Failures**: Most agent failures aren't model failures - they're context failures
2. **Ensures Consistency**: AI follows your project patterns and conventions
3. **Enables Complex Features**: AI can handle multi-step implementations with proper context
4. **Self-Correcting**: Validation loops allow AI to fix its own mistakes

## Template Structure

```
opencode-context-engineering/
├── AGENTS.md                  # OpenCode workflows and project rules
├── scripts/
│   ├── cmd.py                 # Command executor (Python importable)
│   ├── cmd                    # Shell script for Linux/macOS
│   ├── cmd.bat                # Batch script for Windows
│   └── cmd.ps1                # PowerShell script for Windows
├── USAGE.md                  # Detailed usage guide
├── commands/                  # ClaudeCode-compatible command files
│   ├── generate-prp.md       # PRP generation command
│   ├── execute-prp.md        # PRP execution command
│   └── README.md             # Command system documentation
├── PRPs/
│   ├── templates/
│   │   └── prp_base.md       # Base template for PRPs
│   └── EXAMPLE_multi_agent_prp.md  # Example of a complete PRP
├── examples/                  # Your code examples (critical!)
├── INITIAL.md               # Template for feature requests
├── INITIAL_EXAMPLE.md       # Example feature request
└── README.md                # This file
```

This template focuses on the foundational context engineering patterns that work with OpenCode.

## OpenCode Command Implementation

This template provides a comprehensive command executor that works both inside and outside OpenCode sessions:

### Terminal Usage

**Linux/macOS:**
```bash
# List available commands
./scripts/cmd --list

# Generate PRP (equivalent to ClaudeCode's /generate-prp)
./scripts/cmd generate-prp INITIAL.md

# Execute PRP (equivalent to ClaudeCode's /execute-prp)  
./scripts/cmd execute-prp PRPs/your-feature.md
```

**Windows (Command Prompt):**
```cmd
REM List available commands
scripts\cmd.bat --list

REM Generate PRP
scripts\cmd.bat generate-prp INITIAL.md

REM Execute PRP
scripts\cmd.bat execute-prp PRPs\your-feature.md
```

**Windows (PowerShell):**
```powershell
# List available commands
scripts\cmd.ps1 --list

# Generate PRP
scripts\cmd.ps1 generate-prp INITIAL.md

# Execute PRP
scripts\cmd.ps1 execute-prp PRPs\your-feature.md
```

**Advanced options (all platforms):**
./scripts/cmd generate-prp INITIAL.md --verbose
./scripts/cmd execute-prp PRPs/feature.md --continue-session
./scripts/cmd generate-prp INITIAL.md --prompt-only
```

### OpenCode Session Usage
```python
# Import the Context Engineering function
import sys
sys.path.insert(0, 'scripts')
from cmd import execute_command

# Use directly in your OpenCode session
commands_list = execute_command("--list")
prp_prompt = execute_command("generate-prp", "INITIAL.md")
execute_prompt = execute_command("execute-prp", "PRPs/feature.md")

# You can execute any command from the commands/ directory
custom_prompt = execute_command("your-custom-command", ["arg1", "arg2"])
```

### Key Features

- ✅ **Works both inside AND outside OpenCode**
- ✅ **Direct ClaudeCode compatibility** - reads original command markdown files
- ✅ **Automatic variable substitution** (`$ARGUMENTS`)
- ✅ **Dynamic command discovery** from `commands/` directory
- ✅ **Python module import support** for OpenCode sessions
- ✅ **Comprehensive error handling**
- ✅ **Multiple usage patterns** (terminal, import, prompt-only, copy-paste)

## Step-by-Step Guide

### 1. Set Up Agent Configuration (AGENTS.md)

The `AGENTS.md` file contains OpenCode agent configurations and project-wide rules that the AI assistant will follow in every conversation. The template includes:

- **Project awareness**: Reading planning docs, checking tasks
- **Code structure**: File size limits, module organization
- **Testing requirements**: Unit test patterns, coverage expectations
- **Style conventions**: Language preferences, formatting rules
- **Documentation standards**: Docstring formats, commenting practices

**The provided template works out-of-the-box, or you can customize it for your project.**

### 2. Create Your Initial Feature Request

Edit `INITIAL.md` to describe what you want to build:

```markdown
## FEATURE:
[Describe what you want to build - be specific about functionality and requirements]

## EXAMPLES:
[List any example files in the examples/ folder and explain how they should be used]

## DOCUMENTATION:
[Include links to relevant documentation, APIs, or resources]

## OTHER CONSIDERATIONS:
[Mention any gotchas, specific requirements, or things AI assistants commonly miss]
```

**See `INITIAL_EXAMPLE.md` for a complete example.**

### 3. Generate the PRP

PRPs (Product Requirements Prompts) are comprehensive implementation blueprints that include:

- Complete context and documentation
- Implementation steps with validation
- Error handling patterns
- Test requirements

They are similar to PRDs (Product Requirements Documents) but are crafted specifically to instruct an AI coding assistant.

**Option 1: Terminal Usage**
```bash
./scripts/cmd generate-prp INITIAL.md
```

**Option 2: OpenCode Session Usage**
```python
import sys
sys.path.insert(0, 'scripts')
from cmd import execute_command
prp_prompt = execute_command("generate-prp", "INITIAL.md")
print("Generated PRP prompt:")
print(prp_prompt)
```

**Option 3: Manual Interaction**
```
"Please read INITIAL.md and generate a comprehensive PRP following the PRP Generator workflow in AGENTS.md. Research the codebase for similar patterns, search for relevant documentation, and create a detailed implementation blueprint in the PRPs/ folder."
```

This will:
1. Read your feature request from INITIAL.md
2. Research the codebase for patterns
3. Search for relevant documentation
4. Create a comprehensive PRP in `PRPs/your-feature-name.md`

### 4. Execute the PRP

Once generated, execute the PRP to implement your feature:

**Option 1: Terminal Usage**
```bash
./scripts/cmd execute-prp PRPs/your-feature-name.md
```

**Option 2: OpenCode Session Usage**
```python
import sys
sys.path.insert(0, 'scripts')
from cmd import execute_command
execute_prompt = execute_command("execute-prp", "PRPs/your-feature-name.md")
print("Execute PRP prompt:")
print(execute_prompt)
```

**Option 3: Manual Interaction**
```
"Please read PRPs/your-feature-name.md and implement the feature following the PRP Executor workflow in AGENTS.md. Use TodoWrite to track your progress and ensure all validation gates pass."
```

OpenCode will:
1. Read all context from the PRP
2. Create a detailed implementation plan
3. Execute each step with validation
4. Run tests and fix any issues
5. Ensure all success criteria are met

## Writing Effective INITIAL.md Files

The `INITIAL.md` file is your feature request template. It serves as the input to the `generate-prp` agent and should contain all the information needed to understand what you want to build.

### Key Sections Explained

**FEATURE**: Be specific and comprehensive
- ❌ "Build a web scraper"
- ✅ "Build an async web scraper using BeautifulSoup that extracts product data from e-commerce sites, handles rate limiting, and stores results in PostgreSQL"

**EXAMPLES**: Leverage the examples/ folder
- Place relevant code patterns in `examples/`
- Reference specific files and patterns to follow
- Explain what aspects should be mimicked

**DOCUMENTATION**: Include all relevant resources
- API documentation URLs
- Library guides
- Database schemas
- Authentication requirements

**OTHER CONSIDERATIONS**: Capture important details
- Rate limits or quotas
- Common pitfalls
- Performance requirements
- Integration constraints

### INITIAL.md Template Structure

```markdown
# Feature Request: [Brief Title]

## FEATURE:
Detailed description of what you want to build. Include:
- Specific functionality requirements
- Technical constraints
- Integration requirements
- Performance expectations

## EXAMPLES:
Reference files in the examples/ folder:
- `examples/cli.py` - Follow this pattern for CLI implementation
- `examples/agent/agent.py` - Use this agent structure
- `examples/tests/test_*.py` - Follow these testing patterns

## DOCUMENTATION:
Links to relevant documentation:
- [API Documentation](https://api.example.com/docs)
- [Library Guide](https://library.readthedocs.io)
- [Authentication Flow](https://auth.example.com)

## OTHER CONSIDERATIONS:
Important details that might be missed:
- Rate limiting: 100 requests per minute
- Authentication: OAuth2 required
- Error handling: Retry logic for network failures
- Testing: Must include integration tests
```

## The PRP Workflow

### How the PRP Generator Works

The PRP Generator workflow follows this process:

1. **Research Phase**
   - Analyzes your codebase for patterns
   - Searches for similar implementations
   - Identifies conventions to follow

2. **Documentation Gathering**
   - Fetches relevant API docs
   - Includes library documentation
   - Adds gotchas and quirks

3. **Blueprint Creation**
   - Creates step-by-step implementation plan
   - Includes validation gates
   - Adds test requirements

4. **Quality Check**
   - Scores confidence level (1-10)
   - Ensures all context is included

### How the PRP Executor Works

The PRP Executor workflow follows this process:

1. **Load Context**: Reads the entire PRP
2. **Plan**: Creates detailed task list using TodoWrite
3. **Execute**: Implements each component
4. **Validate**: Runs tests and linting
5. **Iterate**: Fixes any issues found
6. **Complete**: Ensures all requirements met

See `PRPs/EXAMPLE_multi_agent_prp.md` for a complete example of what gets generated.

## Using Examples Effectively

The `examples/` folder is **critical** for success. AI coding assistants perform much better when they can see patterns to follow.

### What to Include in Examples

1. **Code Structure Patterns**
   - How you organize modules
   - Import conventions
   - Class/function patterns

2. **Testing Patterns**
   - Test file structure
   - Mocking approaches
   - Assertion styles

3. **Integration Patterns**
   - API client implementations
   - Database connections
   - Authentication flows

4. **CLI Patterns**
   - Argument parsing
   - Output formatting
   - Error handling

### Example Structure

```
examples/
├── README.md           # Explains what each example demonstrates
├── cli.py             # CLI implementation pattern
├── agent/             # Agent architecture patterns
│   ├── agent.py      # Agent creation pattern
│   ├── tools.py      # Tool implementation pattern
│   └── providers.py  # Multi-provider pattern
└── tests/            # Testing patterns
    ├── test_agent.py # Unit test patterns
    └── conftest.py   # Pytest configuration
```

## Best Practices

### 1. Be Explicit in INITIAL.md
- Don't assume the AI knows your preferences
- Include specific requirements and constraints
- Reference examples liberally

### 2. Provide Comprehensive Examples
- More examples = better implementations
- Show both what to do AND what not to do
- Include error handling patterns

### 3. Use Validation Gates
- PRPs include test commands that must pass
- AI will iterate until all validations succeed
- This ensures working code on first try

### 4. Leverage Documentation
- Include official API docs
- Add specific documentation sections
- Reference implementation examples

### 6. Choose Your Usage Pattern
- **Terminal usage**: Best for automation and standalone execution
- **OpenCode session usage**: Best for interactive development
- **Manual interaction**: Best for one-off usage
- **Prompt-only mode**: Best for copy-paste workflows

## Resources

- [OpenCode Documentation](https://opencode.ai)
- [Context Engineering Best Practices](https://www.philschmid.de/context-engineering)
- [USAGE.md](USAGE.md) - Detailed usage guide for all approaches