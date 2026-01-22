# Walkthrough: Terminal Aliases

**Difficulty:** Easy | **Time:** 10 minutes | **Category:** CLI Fundamentals

---

## Overview

Terminal aliases supercharge your Claude Code workflow. Create shortcuts for common commands, reduce typing, and maintain consistency. This challenge teaches you to set up productive aliases for AI-assisted development.

## Prerequisites

- [ ] Shell access (bash, zsh, or PowerShell)
- [ ] Understanding of shell configuration files
- [ ] Claude Code CLI installed

---

## Step 1: Identify Your Shell

Find your shell and config file:

**macOS/Linux:**
```bash
echo $SHELL
# /bin/zsh → use ~/.zshrc
# /bin/bash → use ~/.bashrc
```

**Windows PowerShell:**
```powershell
$PROFILE
# Shows profile location
```

---

## Step 2: Essential Claude Code Aliases

Add these to your shell configuration:

### Bash/Zsh (~/.bashrc or ~/.zshrc)
```bash
# Quick Claude Code launch
alias c='claude'
alias cc='claude --continue'
alias cn='claude --new'

# Claude with specific models
alias ch='claude --model haiku'
alias cs='claude --model sonnet'
alias co='claude --model opus'

# Project-aware Claude
alias ccode='cd $(git rev-parse --show-toplevel) && claude'

# Quick prompts
alias cfix='claude "Fix any issues in the current file"'
alias creview='claude "Review this code for issues"'
alias ctest='claude "Write tests for the recent changes"'
```

### PowerShell ($PROFILE)
```powershell
# Quick Claude Code launch
function c { claude $args }
function cc { claude --continue $args }
function cn { claude --new $args }

# Claude with specific models
function ch { claude --model haiku $args }
function cs { claude --model sonnet $args }
function co { claude --model opus $args }

# Quick prompts
function cfix { claude "Fix any issues in the current file" }
function creview { claude "Review this code for issues" }
```

---

## Step 3: Apply Your Aliases

**Bash/Zsh:**
```bash
source ~/.zshrc  # or ~/.bashrc
```

**PowerShell:**
```powershell
. $PROFILE
```

---

## Step 4: Test Your Aliases

Try each alias:

```bash
# Start Claude quickly
c

# Start with Haiku model
ch

# Start with a code review prompt
creview
```

---

## Step 5: Advanced Aliases

### Git + Claude Combinations
```bash
# Review staged changes
alias grc='git diff --staged | claude "Review these changes"'

# Generate commit message
alias gcm='git diff --staged | claude "Generate a commit message for these changes"'

# Explain last commit
alias gec='git show HEAD | claude "Explain this commit"'
```

### Project-Specific Aliases
```bash
# Run tests and ask Claude about failures
alias tfix='npm test 2>&1 | claude "Analyze these test failures and suggest fixes"'

# Lint and fix
alias lfix='npm run lint 2>&1 | claude "Fix these lint errors"'

# Build and debug
alias bfix='npm run build 2>&1 | claude "Debug this build error"'
```

### Quick File Operations
```bash
# Explain current file
alias cexplain='claude "Explain what this file does: $(cat)"'

# Document current file
alias cdoc='claude "Add comprehensive documentation to: $(cat)"'
```

---

## Step 6: Workflow Aliases

Create aliases for common workflows:

```bash
# Morning startup
alias morning='cd ~/projects/main && git pull && c'

# Quick bug fix workflow
alias bugfix='git checkout -b fix/$(date +%s) && c "Help me fix a bug"'

# Feature start workflow
alias feature='git checkout -b feature/$1 && c "Help me implement a new feature"'

# End of day cleanup
alias eod='claude "Summarize today'\''s progress and what'\''s left to do"'
```

---

## Verification Checklist

- [ ] Created at least 5 aliases for Claude Code
- [ ] Tested aliases work correctly
- [ ] Added Git + Claude combination aliases
- [ ] Created workflow aliases for common patterns
- [ ] Aliases persist after terminal restart

---

## Alias Organization

Organize aliases in your config file:

```bash
# ===========================================
# Claude Code Aliases
# ===========================================

# Core shortcuts
alias c='claude'
alias cc='claude --continue'

# Model selection
alias ch='claude --model haiku'
alias cs='claude --model sonnet'
alias co='claude --model opus'

# Quick tasks
alias cfix='claude "Fix issues"'
alias creview='claude "Review code"'
alias ctest='claude "Write tests"'

# Git integration
alias grc='git diff --staged | claude "Review"'
alias gcm='git diff --staged | claude "Commit message"'

# Workflows
alias morning='cd ~/work && git pull && c'
alias eod='claude "Summary"'
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Alias conflicts | Use unique prefixes like `c` for Claude |
| Aliases not loading | Verify correct config file for your shell |
| Quotes breaking | Use escaped quotes or single quotes |
| Path issues | Use absolute paths in aliases |

---

## Pro Tips

1. **Prefix Convention:** Use `c` prefix for Claude-related aliases
2. **Document Aliases:** Add comments explaining each alias
3. **Version Control:** Keep aliases in a dotfiles repo
4. **Team Sharing:** Share productive aliases with your team

---

## Recommended Alias Sets

### For Frontend Developers
```bash
alias ccomp='claude "Create a React component"'
alias cstyle='claude "Add styling to this component"'
alias ca11y='claude "Check accessibility issues"'
```

### For Backend Developers
```bash
alias capi='claude "Create an API endpoint"'
alias cdb='claude "Help with database query"'
alias cauth='claude "Add authentication"'
```

### For DevOps
```bash
alias cdocker='claude "Help with Docker configuration"'
alias ck8s='claude "Help with Kubernetes"'
alias cci='claude "Help with CI/CD pipeline"'
```

---

## Next Challenge

Continue to **[Copy-Paste Power](./09-copy-paste-power.md)** to master efficient data transfer!
