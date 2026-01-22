# Walkthrough: Skills vs Commands

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** MCP Integrations

---

## Overview

Claude Code has both slash commands and skills. Understanding the difference is key to using Claude effectively. Commands are built-in operations, while skills are extensible prompts that can be customized and shared.

## Prerequisites

- [ ] Basic Claude Code usage
- [ ] Understanding of slash commands
- [ ] Familiarity with CLAUDE.md

---

## Step 1: Understanding the Difference

### Slash Commands
```
Built-in, hardcoded operations
- /help - Show help
- /clear - Clear context
- /model - Switch models
- /usage - Show token usage
```

### Skills
```
Extensible prompt-based capabilities
- /commit - Generate commits (skill)
- /review-pr - Review pull requests (skill)
- Custom skills you create
```

---

## Step 2: Identify Commands vs Skills

### Check Available Commands
```
/help
```

**Commands list:**
- Start with `/`
- Execute immediately
- Cannot be modified
- Part of Claude Code core

### Check Available Skills
The Skill tool shows available skills:
```
Available skills:
- commit
- review-pr
- tdd-workflow
- security-review
- [custom skills]
```

---

## Step 3: How Commands Work

### Commands Are Direct Actions
```
/usage
```
**Result:** Immediately shows token usage

```
/clear
```
**Result:** Immediately clears context

### Commands Cannot Be Customized
You can't change what `/clear` does - it's built into Claude Code.

---

## Step 4: How Skills Work

### Skills Are Prompt Templates
When you invoke `/commit`:
1. Claude loads the "commit" skill definition
2. The skill expands into a detailed prompt
3. Claude follows the prompt instructions

### Skills Are Customizable
```bash
# Create custom skill
mkdir -p ~/.claude/skills
touch ~/.claude/skills/my-review.md
```

```markdown
# My Code Review Skill

When reviewing code, check for:
1. Security vulnerabilities
2. Performance issues
3. Code style violations
4. Test coverage

Provide ratings:
- Critical: Must fix
- Warning: Should fix
- Note: Consider fixing
```

---

## Step 5: Use Skills Effectively

### Invoke a Skill
```
/commit
```
or
```
Use the commit skill to create a commit
```

### Skill with Arguments
```
/review-pr 123
```
Passes "123" as an argument to the skill.

### Skill Chaining
```
After the commit skill completes, run the security-review skill
```

---

## Step 6: Compare Usage Patterns

### Commands for System Operations
| Command | Purpose |
|---------|---------|
| `/help` | Get help |
| `/clear` | Clear context |
| `/reset` | Full reset |
| `/model` | Switch models |
| `/usage` | Token stats |
| `/mcp` | MCP status |

### Skills for Workflows
| Skill | Purpose |
|-------|---------|
| `commit` | Create git commits |
| `review-pr` | Review pull requests |
| `tdd` | Test-driven development |
| `security-review` | Security audit |
| `plan` | Create implementation plan |

---

## Step 7: Create Your Own Skill

### Skill File Structure
```bash
~/.claude/skills/
├── my-skill.md
└── another-skill.md
```

### Example: Debug Skill
```markdown
# Debug Skill

When debugging an issue:

1. **Understand the Problem**
   - What is the expected behavior?
   - What is the actual behavior?
   - Can you reproduce it?

2. **Gather Information**
   - Check error messages
   - Review recent changes
   - Examine logs

3. **Form Hypotheses**
   - List possible causes
   - Rank by likelihood

4. **Test Each Hypothesis**
   - Start with most likely
   - Verify or eliminate

5. **Fix and Verify**
   - Implement fix
   - Test thoroughly
   - Prevent regression
```

### Using Your Skill
```
/debug
```

---

## Verification Checklist

- [ ] Can list available commands
- [ ] Can identify available skills
- [ ] Used at least 3 different skills
- [ ] Created a custom skill
- [ ] Understand when to use commands vs skills

---

## Decision Guide

### Use a Command When:
- You need immediate system action
- The operation is simple and fixed
- You're managing the Claude session itself

### Use a Skill When:
- You need a workflow or process
- You want customizable behavior
- The task requires multiple steps
- You want to share the process

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| "Skill not found" | Check skill file exists and is valid |
| Command doesn't expand | It's a command, not a skill |
| Custom skill ignored | Verify file location and format |
| Too many skills | Organize into categories |

---

## Pro Tips

1. **Naming:** Use clear, action-oriented skill names
2. **Single Purpose:** Each skill should do one thing well
3. **Documentation:** Include usage examples in skills
4. **Sharing:** Skills can be shared via dotfiles repo

---

## Next Challenge

Continue to **[Skill Creation](./05-skill-creation.md)** to build reusable capabilities!
