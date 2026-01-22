# Solution: Terminal Aliases and Shortcuts

## Identify Your Shell

### Check Current Shell

```bash
echo $SHELL

# Common outputs:
# /bin/bash  → Bash
# /bin/zsh   → Zsh (macOS default)
# /usr/bin/fish → Fish
```

### Shell-Specific Config Files

```bash
# Bash
~/.bashrc          # Linux
~/.bash_profile    # macOS
~/.profile         # Alternative

# Zsh
~/.zshrc          # Main config file

# Fish
~/.config/fish/config.fish
```

## Basic Alias Setup

### Step 1: Open Configuration File

```bash
# Bash (Linux)
nano ~/.bashrc

# Bash (macOS)
nano ~/.bash_profile

# Zsh (macOS/Linux)
nano ~/.zshrc

# Fish
nano ~/.config/fish/config.fish

# Or use your preferred editor (vim, code, etc.)
code ~/.zshrc
```

### Step 2: Add Basic Aliases

**For Bash/Zsh**, add to config file:

```bash
# === Claude Code Aliases ===

# Basic launch
alias c='claude'

# Chat history
alias ch='claude --history'

# Debug mode
alias cdebug='claude --debug'

# Clear screen and launch Claude
alias cc='clear && claude'
```

**For Fish**, syntax is slightly different:

```fish
# === Claude Code Aliases ===

# Basic launch
alias c 'claude'

# Chat history
alias ch 'claude --history'

# Debug mode
alias cdebug 'claude --debug'
```

### Step 3: Reload Configuration

```bash
# Bash
source ~/.bashrc      # Linux
source ~/.bash_profile # macOS

# Zsh
source ~/.zshrc

# Fish
source ~/.config/fish/config.fish

# Or simply open a new terminal tab
```

### Step 4: Test Aliases

```bash
# Test basic launch
c

# Test history (if you've used Claude before)
ch

# Verify alias definition
alias c
# Should output: alias c='claude'
```

## Advanced Aliases

### Model Selection Shortcuts

```bash
# Bash/Zsh
alias cs='claude --model sonnet-4.5'
alias chaiku='claude --model haiku-4.5'
alias copus='claude --model opus-4.5'

# Fish
alias cs 'claude --model sonnet-4.5'
alias chaiku 'claude --model haiku-4.5'
alias copus 'claude --model opus-4.5'
```

**Usage**:
```bash
cs     # Launch Claude with Sonnet (best balance)
chaiku # Launch Claude with Haiku (fast & cheap)
copus  # Launch Claude with Opus (deep reasoning)
```

### Project-Specific Aliases

```bash
# Bash/Zsh
alias cproject='cd ~/projects/my-app && claude'
alias cwork='cd ~/work/current-project && claude'
alias cpersonal='cd ~/personal/side-project && claude'

# Fish
alias cproject 'cd ~/projects/my-app && claude'
```

**Usage**:
```bash
cproject  # Jump to project directory and launch Claude
```

### Context-Rich Launches

```bash
# Bash/Zsh
alias cg='git status && claude'  # Show git status before Claude
alias ct='git log --oneline -5 && claude'  # Show recent commits
alias cb='git branch --show-current && claude'  # Show current branch

# Fish
alias cg 'git status && claude'
```

## Shell Functions (More Powerful Than Aliases)

Functions can accept arguments, making them more flexible than aliases.

### Basic Function

**Bash/Zsh**:
```bash
# Add to ~/.zshrc or ~/.bashrc

# Launch Claude in specific project
function cpr() {
    cd ~/projects/$1 && claude
}

# Usage: cpr my-app
```

**Fish**:
```fish
# Add to ~/.config/fish/config.fish

function cpr
    cd ~/projects/$1 && claude
end
```

### Advanced Functions

**Bash/Zsh**:
```bash
# Launch Claude with git context
function cgit() {
    echo "=== Current Branch ==="
    git branch --show-current
    echo ""
    echo "=== Recent Commits ==="
    git log --oneline -5
    echo ""
    echo "=== Working Directory Status ==="
    git status -s
    echo ""
    claude
}

# Launch Claude with model selection
function cmodel() {
    if [ -z "$1" ]; then
        echo "Usage: cmodel [sonnet|haiku|opus]"
        return 1
    fi

    case $1 in
        sonnet|s)
            claude --model sonnet-4.5
            ;;
        haiku|h)
            claude --model haiku-4.5
            ;;
        opus|o)
            claude --model opus-4.5
            ;;
        *)
            echo "Unknown model: $1"
            echo "Use: sonnet, haiku, or opus"
            ;;
    esac
}

# Usage:
# cmodel sonnet
# cmodel haiku
# cmodel opus

# Launch Claude in project with auto-detection
function cp() {
    if [ -f "package.json" ]; then
        echo "📦 Node.js project detected"
    elif [ -f "Cargo.toml" ]; then
        echo "🦀 Rust project detected"
    elif [ -f "go.mod" ]; then
        echo "🐹 Go project detected"
    elif [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
        echo "🐍 Python project detected"
    fi
    claude
}
```

**Fish**:
```fish
# Launch Claude with model selection
function cmodel
    if test (count $argv) -eq 0
        echo "Usage: cmodel [sonnet|haiku|opus]"
        return 1
    end

    switch $argv[1]
        case sonnet s
            claude --model sonnet-4.5
        case haiku h
            claude --model haiku-4.5
        case opus o
            claude --model opus-4.5
        case '*'
            echo "Unknown model: $argv[1]"
            echo "Use: sonnet, haiku, or opus"
    end
end
```

## Complete Starter Configuration

### Recommended Aliases Set

**Bash/Zsh** - Add to `~/.zshrc` or `~/.bashrc`:

```bash
# ============================================
# Claude Code Aliases & Functions
# ============================================

# --- Basic Aliases ---
alias c='claude'                    # Quick launch
alias cc='clear && claude'          # Clear screen first
alias ch='claude --history'         # View chat history

# --- Model Selection ---
alias cs='claude --model sonnet-4.5'    # Sonnet (balanced)
alias chaiku='claude --model haiku-4.5' # Haiku (fast)
alias copus='claude --model opus-4.5'   # Opus (powerful)

# --- Git Integration ---
alias cg='git status && claude'     # Git status before Claude
alias ct='git log --oneline -5 && claude'  # Recent commits

# --- Debug & Development ---
alias cdebug='claude --debug'       # Debug mode
alias cverbose='claude --verbose'   # Verbose output

# --- Functions ---

# Launch Claude in project directory
cpr() {
    if [ -z "$1" ]; then
        echo "Usage: cpr <project-name>"
        echo "Launches Claude in ~/projects/<project-name>"
        return 1
    fi
    cd ~/projects/$1 && claude
}

# Launch Claude with model choice
cmodel() {
    if [ -z "$1" ]; then
        echo "Usage: cmodel [sonnet|haiku|opus]"
        return 1
    fi

    case $1 in
        sonnet|s) claude --model sonnet-4.5 ;;
        haiku|h)  claude --model haiku-4.5 ;;
        opus|o)   claude --model opus-4.5 ;;
        *) echo "Unknown model. Use: sonnet, haiku, or opus" ;;
    esac
}

# Show all Claude aliases
claude-aliases() {
    echo "=== Claude Code Aliases ==="
    alias | grep -E "^(c|ch|cs|chaiku|copus|cg|ct|cdebug|cverbose)"
    echo ""
    echo "=== Claude Code Functions ==="
    echo "cpr <project>  - Launch Claude in project directory"
    echo "cmodel <model> - Launch Claude with specific model"
    echo "claude-aliases - Show this help"
}
```

### Installation Script

Create a file `install-claude-aliases.sh`:

```bash
#!/bin/bash

# Detect shell
if [ -n "$ZSH_VERSION" ]; then
    CONFIG_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        CONFIG_FILE="$HOME/.bash_profile"
    else
        CONFIG_FILE="$HOME/.bashrc"
    fi
else
    echo "Unsupported shell. Only bash and zsh are supported."
    exit 1
fi

# Backup config file
cp "$CONFIG_FILE" "$CONFIG_FILE.backup.$(date +%Y%m%d)"

# Append Claude aliases
cat >> "$CONFIG_FILE" << 'EOF'

# ============================================
# Claude Code Aliases & Functions
# ============================================

# Basic Aliases
alias c='claude'
alias cc='clear && claude'
alias ch='claude --history'

# Model Selection
alias cs='claude --model sonnet-4.5'
alias chaiku='claude --model haiku-4.5'
alias copus='claude --model opus-4.5'

# Git Integration
alias cg='git status && claude'

# Functions
cpr() {
    if [ -z "$1" ]; then
        echo "Usage: cpr <project-name>"
        return 1
    fi
    cd ~/projects/$1 && claude
}

cmodel() {
    if [ -z "$1" ]; then
        echo "Usage: cmodel [sonnet|haiku|opus]"
        return 1
    fi
    case $1 in
        sonnet|s) claude --model sonnet-4.5 ;;
        haiku|h)  claude --model haiku-4.5 ;;
        opus|o)   claude --model opus-4.5 ;;
        *) echo "Unknown model" ;;
    esac
}

claude-aliases() {
    echo "Claude Aliases:"
    alias | grep -E "^(c|ch|cs|chaiku|copus|cg)"
}

EOF

echo "✅ Claude aliases installed to $CONFIG_FILE"
echo "📄 Backup created at $CONFIG_FILE.backup.$(date +%Y%m%d)"
echo ""
echo "Run: source $CONFIG_FILE"
echo "Or open a new terminal tab"
```

Make it executable and run:
```bash
chmod +x install-claude-aliases.sh
./install-claude-aliases.sh
source ~/.zshrc  # or source ~/.bashrc
```

## Platform-Specific Optimizations

### macOS

```bash
# Add to ~/.zshrc

# Open Claude in new terminal tab (requires iTerm2 or Terminal.app)
alias cn='osascript -e "tell application \"Terminal\" to do script \"cd $(pwd) && claude\""'

# Open with VS Code to the same directory
alias cv='code . && claude'

# Copy current directory path and launch Claude
alias cpwd='pwd | pbcopy && echo "Path copied!" && claude'
```

### Linux

```bash
# Add to ~/.bashrc

# Open Claude in new terminal tab (GNOME Terminal)
alias cn='gnome-terminal --tab --working-directory="$(pwd)" -e "claude"'

# Open with VS Code
alias cv='code . && claude'

# Copy current directory path
alias cpwd='pwd | xclip -selection clipboard && echo "Path copied!" && claude'
```

### Windows (PowerShell)

Add to PowerShell profile (`$PROFILE`):

```powershell
# Basic aliases
Set-Alias -Name c -Value claude

# Functions
function ch { claude --history }
function cs { claude --model sonnet-4.5 }
function chaiku { claude --model haiku-4.5 }
function copus { claude --model opus-4.5 }

function cpr {
    param([string]$project)
    if ($project) {
        Set-Location "C:\Users\$env:USERNAME\projects\$project"
        claude
    } else {
        Write-Host "Usage: cpr <project-name>"
    }
}

# Show aliases
function claude-aliases {
    Write-Host "Claude Aliases:"
    Get-Alias | Where-Object { $_.Name -match '^c' }
}
```

## Troubleshooting

### Issue 1: Alias Not Found After Adding

**Problem**: `c: command not found`

**Solutions**:
```bash
# Did you reload the config?
source ~/.zshrc

# Is the alias in the right file?
cat ~/.zshrc | grep "alias c="

# Check if another alias is conflicting
alias c

# Try in a new terminal tab
```

### Issue 2: Alias Works in One Terminal, Not Another

**Problem**: Aliases work in some terminals but not others

**Solution**: Different terminal applications may load different config files

```bash
# Check which shell is running
echo $SHELL

# Check which config file is loaded
echo $ZDOTDIR
echo $HOME

# Ensure aliases are in the correct file for your shell
```

### Issue 3: Function Not Working

**Problem**: Function gives errors

**Solution**:
```bash
# Check function syntax
type cpr

# Test function with set -x (debug mode)
set -x
cpr myproject
set +x

# Common issues:
# - Missing 'end' in Fish functions
# - Wrong quote types
# - Missing 'function' keyword in Fish
```

### Issue 4: Alias Expansion Issues

**Problem**: Alias expands in unexpected ways

**Solution**: Use functions instead of aliases for complex commands

```bash
# ❌ This won't work as expected
alias cpr='cd ~/projects/$1 && claude'

# ✅ Use a function
cpr() {
    cd ~/projects/$1 && claude
}
```

## Best Practices

### 1. Use Mnemonic Names

```bash
✅ Good:
c      # claude (obvious)
ch     # claude history
cs     # claude sonnet
cg     # claude + git

❌ Bad:
a      # too generic
mycmd  # not descriptive
x      # meaningless
```

### 2. Group Related Aliases

```bash
# In config file, organize by category:

# === Claude Basics ===
alias c='claude'
alias cc='clear && claude'

# === Model Selection ===
alias cs='claude --model sonnet-4.5'
alias chaiku='claude --model haiku-4.5'

# === Git Integration ===
alias cg='git status && claude'
```

### 3. Document Your Aliases

```bash
# Add comments explaining complex aliases

# Launch Claude with git status and branch info
alias cgit='git status && git branch --show-current && claude'

# Or create a help function
claude-help() {
    echo "c      - Launch Claude"
    echo "cg     - Claude with git status"
    echo "cpr    - Claude in project: cpr <name>"
    echo "cmodel - Claude with model: cmodel [s|h|o]"
}
```

### 4. Don't Override System Commands

```bash
❌ Avoid:
alias ls='claude'    # Bad: overrides 'ls'
alias cd='claude'    # Bad: breaks navigation
alias git='claude'   # Bad: breaks git

✅ Safe:
alias c='claude'     # Unique prefix
alias cla='claude'   # Unique command
```

### 5. Test Before Committing

```bash
# Test alias in current shell first
alias c='claude'
c  # Test it

# If it works, add to config file
echo "alias c='claude'" >> ~/.zshrc
source ~/.zshrc
```

## Quick Reference

### Essential Commands

```bash
# Show all aliases
alias

# Show specific alias
alias c

# Show all Claude-related aliases
alias | grep claude

# Remove alias (current session only)
unalias c

# Show function definition
type cpr

# List all functions
declare -F  # Bash
functions   # Zsh
functions   # Fish
```

### Config File Locations

```
Bash (Linux):    ~/.bashrc
Bash (macOS):    ~/.bash_profile
Zsh:             ~/.zshrc
Fish:            ~/.config/fish/config.fish
PowerShell:      $PROFILE (run `$PROFILE` to see path)
```

### Reload Config

```bash
# Bash
source ~/.bashrc        # Linux
source ~/.bash_profile  # macOS

# Zsh
source ~/.zshrc

# Fish
source ~/.config/fish/config.fish

# PowerShell
. $PROFILE
```

## Success Indicators

You've mastered terminal aliases when you:

- Launch Claude with a single letter (`c`)
- Never type the full `claude` command
- Have model selection shortcuts memorized
- Created project-specific aliases
- Can add new aliases without looking up syntax
- Your aliases persist across terminal restarts
- You've shared your best aliases with teammates
- Opening a terminal and typing `c` is muscle memory

## Recommended Starter Pack

```bash
# Minimal setup - just add these 3
alias c='claude'
alias cs='claude --model sonnet-4.5'
alias ch='claude --history'

# That's it! Start here and add more as you need them.
```
