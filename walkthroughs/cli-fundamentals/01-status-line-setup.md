# Walkthrough: Status Line Setup

**Difficulty:** Easy | **Time:** 10 minutes | **Category:** CLI Fundamentals

---

## Overview

The status line is your command center in Claude Code. It displays critical information at a glance: current AI model, Git branch, and token usage. Mastering this is your first step to becoming a Claude Code power user.

## Prerequisites

- [ ] Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
- [ ] A Git repository to work in
- [ ] Terminal/command prompt access

---

## Step 1: Launch Claude Code in a Git Repository

Open your terminal and navigate to any Git repository:

```bash
cd your-project-directory
claude
```

**Expected Result:** Claude Code launches with a status line at the bottom of your terminal.

---

## Step 2: Identify the Status Line Components

Look at the bottom of your terminal. You should see three key pieces of information:

```
┌─────────────────────────────────────────────────────────┐
│ [Model: Sonnet 4.5] [Branch: main] [Tokens: 1.2k/200k] │
└─────────────────────────────────────────────────────────┘
```

### Component Breakdown:

| Component | Description | Example |
|-----------|-------------|---------|
| **Model** | Currently active AI model | `Sonnet 4.5`, `Opus 4.5`, `Haiku 4.5` |
| **Branch** | Current Git branch | `main`, `feature/auth`, `bugfix-123` |
| **Tokens** | Usage vs limit | `1.2k/200k` (0.6% used) |

---

## Step 3: Switch Between Models

Press the model selector key or use the command:

```
/model
```

**Available Models:**
- **Haiku 4.5** - Fast, cost-effective for simple tasks
- **Sonnet 4.5** - Balanced performance for most coding work
- **Opus 4.5** - Deep reasoning for complex problems

**Pro Tip:** Use Haiku for quick questions, Sonnet for coding, Opus for architecture decisions.

---

## Step 4: Monitor Token Usage

As you interact with Claude, watch the token counter increase:

```
Initial:  [Tokens: 0/200k]
After 1 message: [Tokens: 1.5k/200k]
After 5 messages: [Tokens: 8.2k/200k]
```

**Warning Signs:**
- Above 80% (160k tokens): Consider compacting context
- Above 90% (180k tokens): Start a fresh session soon

---

## Step 5: Create a New Git Branch

Test that the status line updates with Git operations:

```bash
# In another terminal (or use Ctrl+Z to background Claude)
git checkout -b challenge/status-line-test
```

**Expected Result:** Status line updates to show `[Branch: challenge/status-line-test]`

---

## Step 6: Verify Your Understanding

Run the `/usage` command to see detailed token breakdown:

```
/usage
```

**Expected Output:**
```
Session Usage:
  Input tokens: 1,234
  Output tokens: 567
  Total: 1,801

Cost estimate: $0.02
Context window: 0.9% used
```

---

## Verification Checklist

- [ ] Can identify the current model from the status line
- [ ] Can read the active Git branch from the status line
- [ ] Can interpret token usage (percentage used)
- [ ] Understand when approaching context window limits (>80%)
- [ ] Know how to switch models when needed

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Status line not showing | Ensure terminal is wide enough (minimum 80 chars) |
| Git branch shows "detached" | Checkout a named branch: `git checkout main` |
| Token count seems stuck | Token updates after each Claude response |
| Wrong model showing | Use `/model` to switch, then verify |

---

## Pro Tips

1. **Context Window Strategy**: Avoid the last 20% of context for complex tasks - performance degrades
2. **Model Selection**: Start with Sonnet, escalate to Opus only for deep reasoning
3. **Branch Awareness**: Always verify you're on the right branch before making changes
4. **Cost Tracking**: Check `/usage` periodically during long sessions

---

## Next Challenge

Ready to level up? Try **[Slash Commands](./02-slash-commands.md)** to learn power user shortcuts!
