#!/usr/bin/env python3
"""
OpenCode Context Engineering Integration

This module provides integration between OpenCode and the Context Engineering workflow.
It can be used both as a standalone script and imported within OpenCode sessions.
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Union

class ContextEngineering:
    """Context Engineering workflow implementation for OpenCode"""
    
    def __init__(self, commands_dir: str = "commands"):
        self.commands_dir = Path(commands_dir)
        self.available_commands = self._discover_commands()
    
    def _discover_commands(self) -> Dict[str, Path]:
        """Discover available command markdown files"""
        commands = {}
        if self.commands_dir.exists():
            for md_file in self.commands_dir.glob("*.md"):
                command_name = md_file.stem
                if command_name.lower() != 'readme':  # Skip README files
                    commands[command_name] = md_file
        return commands
    
    def _load_command_content(self, command_name: str) -> str:
        """Load command content from markdown file"""
        if command_name not in self.available_commands:
            raise ValueError(f"Command '{command_name}' not found")
        
        command_file = self.available_commands[command_name]
        try:
            with open(command_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise RuntimeError(f"Failed to read command file {command_file}: {e}")
    
    def _substitute_variables(self, content: str, arguments: Union[str, List[str]]) -> str:
        """Substitute variables in the command content"""
        if isinstance(arguments, str):
            args_string = arguments
        else:
            args_string = ' '.join(arguments) if arguments else ''
        
        # Handle $ARGUMENTS substitution
        content = content.replace('$ARGUMENTS', args_string)
        content = content.replace('${ARGUMENTS}', args_string)
        
        return content
    
    def get_command_prompt(self, command_name: str, arguments: Union[str, List[str]] = None) -> str:
        """Get the full prompt for a command with arguments substituted"""
        if arguments is None:
            arguments = []
        
        # Load command content
        command_content = self._load_command_content(command_name)
        
        # Substitute variables
        processed_content = self._substitute_variables(command_content, arguments)
        
        # Construct full prompt
        prompt = f"""You are executing a Context Engineering command: {command_name}

Command Instructions:
{processed_content}

Please follow the instructions above exactly as specified. Pay attention to:
- All research and analysis steps
- File paths and naming conventions  
- Validation requirements
- Output format and location
- Quality checklist items

Execute this command thoroughly and completely."""
        
        return prompt
    
    def list_commands(self) -> Dict[str, str]:
        """List all available commands with descriptions"""
        commands_info = {}
        for command_name, command_file in self.available_commands.items():
            try:
                with open(command_file, 'r') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('#'):
                        description = first_line.lstrip('#').strip()
                    else:
                        description = "No description available"
                commands_info[command_name] = description
            except:
                commands_info[command_name] = "Error reading file"
        return commands_info
    
    def execute_via_opencode_run(self, command_name: str, arguments: Union[str, List[str]] = None,
                                verbose: bool = False, continue_session: bool = False) -> None:
        """Execute command using opencode run (for external script usage)"""
        
        # Check if opencode is available
        try:
            subprocess.run(['opencode', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError("opencode not found. Please install it first: curl -fsSL https://opencode.ai/install | bash")
        
        # Get the prompt
        prompt = self.get_command_prompt(command_name, arguments)
        
        if verbose:
            print(f"📋 Executing command: {command_name}")
            print(f"📝 Arguments: {arguments}")
            print(f"🔧 Prompt preview: {prompt[:200]}...")
        
        # Prepare OpenCode command
        cmd = ['opencode', 'run']
        if continue_session:
            cmd.append('--continue')
        cmd.append(prompt)
        
        print(f"🚀 Executing command: {command_name}")
        
        # Execute with OpenCode
        try:
            subprocess.run(cmd, check=True)
            print(f"✅ Command '{command_name}' completed successfully")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error executing OpenCode: {e}")

# Generic function for executing any command within OpenCode
def execute_command(command_name: str, arguments: Union[str, List[str]] = None) -> str:
    """Execute any command and return the prompt (for use within OpenCode)"""
    ce = ContextEngineering()
    
    # Handle special --list command
    if command_name == "--list":
        commands_info = ce.list_commands()
        if not commands_info:
            return "No commands found in the commands directory."
        
        result = "Available commands:\n"
        for cmd_name, description in commands_info.items():
            result += f"  {cmd_name:<20} - {description}\n"
        return result.strip()
    
    return ce.get_command_prompt(command_name, arguments)

def _list_available_commands() -> Dict[str, str]:
    """Internal function to list available commands"""
    ce = ContextEngineering()
    return ce.list_commands()

# Main script functionality (for external usage)
def main():
    """Main entry point for external script usage"""
    parser = argparse.ArgumentParser(
        description='Execute Context Engineering commands with OpenCode',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  ./scripts/cmd generate-prp INITIAL.md
  ./scripts/cmd execute-prp PRPs/feature.md
  ./scripts/cmd --list
        '''
    )
    
    parser.add_argument('command', nargs='?', help='Command to execute')
    parser.add_argument('arguments', nargs='*', help='Arguments for the command')
    parser.add_argument('--list', '-l', action='store_true', help='List available commands')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--continue-session', '-c', action='store_true', 
                       help='Continue last OpenCode session')
    parser.add_argument('--commands-dir', '-d', default='commands',
                       help='Directory containing command files (default: commands)')
    parser.add_argument('--prompt-only', '-p', action='store_true',
                       help='Only output the prompt (don\'t execute)')
    
    args = parser.parse_args()
    
    # Initialize Context Engineering
    ce = ContextEngineering(args.commands_dir)
    
    # Handle list command
    if args.list:
        commands_info = _list_available_commands()
        if not commands_info:
            print("No commands found in the commands directory.")
            return
        
        print("Available commands:")
        for command_name, description in commands_info.items():
            print(f"  {command_name:<20} - {description}")
        return
    
    # Validate command argument
    if not args.command:
        print("❌ Error: No command specified")
        parser.print_help()
        sys.exit(1)
    
    try:
        # Handle prompt-only mode
        if args.prompt_only:
            prompt = ce.get_command_prompt(args.command, args.arguments)
            print(prompt)
            return
        
        # Execute command
        ce.execute_via_opencode_run(
            args.command, 
            args.arguments, 
            verbose=args.verbose,
            continue_session=args.continue_session
        )
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()