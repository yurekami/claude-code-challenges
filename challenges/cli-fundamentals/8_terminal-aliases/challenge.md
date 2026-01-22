# Terminal Aliases and Shortcuts

**Related Tip:** Tip 7: Create shortcuts like `c` and `ch`

## Description

Typing `claude` repeatedly adds friction to your workflow. Creating terminal aliases and shortcuts eliminates this friction, making it effortless to launch Claude Code, access chat history, and execute common operations. This challenge teaches you to optimize your terminal environment for maximum productivity.

## Objective

Master terminal customization by creating aliases and shortcuts that streamline your Claude Code workflow. Transform `claude --some-long-flag` into simple, memorable commands.

## Why Aliases Matter

### Reduce Friction
- `claude` → `c` (5 keystrokes saved every launch)
- Launch Claude 20 times/day = 100 keystrokes saved daily
- Over a year: 36,500 keystrokes saved

### Mental Load
- Short commands = faster recall
- Muscle memory develops quicker
- Less context switching

### Customization
- Aliases can include default flags
- Can chain commands
- Can add helpful defaults

## Essential Aliases

### Basic Launch
```bash
alias c='claude'
```

### Chat History
```bash
alias ch='claude --history'
```

### Debug Mode
```bash
alias cd='claude --debug'
```

### Model Selection
```bash
alias cs='claude --model sonnet-4.5'
alias ch='claude --model haiku-4.5'
alias co='claude --model opus-4.5'
```

## Steps to Complete

1. Identify your shell (bash, zsh, fish)
2. Open your shell configuration file
3. Create aliases for common Claude Code operations
4. Reload shell configuration
5. Test all aliases
6. Iterate and refine based on usage

## Success Criteria

- [ ] Can launch Claude with a single letter command
- [ ] Have aliases for 3+ common operations
- [ ] Aliases persist across terminal sessions
- [ ] Know where your aliases are defined
- [ ] Can add new aliases easily
- [ ] Understand alias vs function vs script

## Challenge Tasks

1. **Basic Setup**: Create `c` alias for `claude`
2. **History Access**: Create `ch` alias for chat history
3. **Model Shortcuts**: Create aliases for each model
4. **Project Launch**: Create alias that cd's to project and launches Claude
5. **Custom Workflow**: Create alias for your personal workflow

## Bonus Challenges

1. **Function Creation**: Write a function that takes arguments
2. **Conditional Alias**: Different behavior based on directory
3. **Alias Discovery**: Create command to list all your Claude aliases
4. **Team Sharing**: Share your best aliases with team

## Common Patterns

### Pattern 1: Simple Replacement
```bash
alias c='claude'
```

### Pattern 2: With Flags
```bash
alias cd='claude --debug --verbose'
```

### Pattern 3: With Function
```bash
function cpr() {
    cd ~/projects/$1 && claude
}
# Usage: cpr myproject
```

### Pattern 4: Chained Commands
```bash
alias cg='git status && claude'
```
