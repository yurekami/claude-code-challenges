# Walkthrough: Slash Commands Mastery

**Difficulty:** Easy | **Time:** 12 minutes | **Category:** CLI Fundamentals

---

## Overview

Slash commands are Claude Code's power user shortcuts. They provide quick access to session management, browser integration, MCP connections, and more - all without leaving your conversation flow.

## Prerequisites

- [ ] Claude Code CLI installed and working
- [ ] Completed the Status Line Setup challenge
- [ ] Chrome browser installed (optional, for `/chrome`)

---

## Step 1: Discover Available Commands

Start by seeing all available commands:

```
/help
```

**Expected Output:**
```
Available Commands:
  /usage   - Display token usage and costs
  /stats   - Show session statistics
  /clear   - Clear conversation history
  /reset   - Hard reset (clear everything)
  /model   - Switch AI models
  /files   - Show files in context
  /chrome  - Chrome browser integration
  /mcp     - MCP server management
  ...
```

---

## Step 2: Check Token Usage with `/usage`

Monitor your API consumption:

```
/usage
```

**Expected Output:**
```
═══════════════════════════════════════
        Session Token Usage
═══════════════════════════════════════
  Input tokens:    2,456
  Output tokens:   1,234
  Total tokens:    3,690

  Context used:    1.8%
  Estimated cost:  $0.04
═══════════════════════════════════════
```

**When to use:** Check before starting expensive operations, monitor costs during long sessions.

---

## Step 3: View Session Statistics with `/stats`

Get detailed session metrics:

```
/stats
```

**Expected Output:**
```
═══════════════════════════════════════
        Session Statistics
═══════════════════════════════════════
  Session duration:     45 minutes
  Messages exchanged:   23
  Files modified:       7
  Tools used:           15

  Most used tools:
    1. Read (8 times)
    2. Edit (5 times)
    3. Bash (2 times)
═══════════════════════════════════════
```

---

## Step 4: Manage Files with `/files`

See what's in your context:

```
/files
```

**Expected Output:**
```
Files in context:
  1. src/index.ts (342 lines)
  2. src/utils/helper.ts (89 lines)
  3. package.json (45 lines)
  4. README.md (120 lines)

Total: 4 files, 596 lines
```

---

## Step 5: Clear Context with `/clear`

When context gets cluttered, clean it up:

```
/clear
```

**Important Distinction:**

| Command | What it does | When to use |
|---------|--------------|-------------|
| `/clear` | Clears conversation, keeps file context | Mid-session cleanup |
| `/reset` | Clears everything completely | Starting completely fresh |

**Pro Tip:** Use `/clear` when you want to reduce token usage but keep working on the same files.

---

## Step 6: Switch Models with `/model`

Change AI models based on your task:

```
/model
```

**Interactive Selection:**
```
Select a model:
  [ ] claude-haiku-4-5     (Fast, economical)
  [●] claude-sonnet-4-5    (Balanced)
  [ ] claude-opus-4-5      (Deep reasoning)
```

**Model Selection Guide:**
- **Haiku**: Quick questions, simple edits, code formatting
- **Sonnet**: General coding, debugging, feature implementation
- **Opus**: Architecture decisions, complex algorithms, deep analysis

---

## Step 7: Connect MCP Servers with `/mcp`

View and manage MCP connections:

```
/mcp
```

**Expected Output:**
```
Connected MCP Servers:
  ✓ filesystem - File operations
  ✓ github - GitHub integration
  ○ postgres - Not connected

Available tools: 12
```

---

## Step 8: Chrome Integration with `/chrome`

If Chrome is available, enable browser integration:

```
/chrome
```

**Capabilities Unlocked:**
- Web scraping
- Screenshot capture
- JavaScript execution
- Form interaction

**Example Usage:**
```
Take a screenshot of https://example.com
```

---

## Verification Checklist

- [ ] Can check token usage and costs with `/usage`
- [ ] Can monitor session statistics with `/stats`
- [ ] Understand when to use `/clear` vs `/reset`
- [ ] Can list all files with `/files`
- [ ] Know how to connect MCP servers with `/mcp`
- [ ] Can switch models with `/model`

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| `/chrome` not working | Ensure Chrome is installed and in PATH |
| `/mcp` shows no servers | Configure MCP servers in `~/.claude/settings.json` |
| `/clear` didn't help | Try `/reset` for a completely fresh start |
| Commands not recognized | Ensure you're using the latest Claude Code version |

---

## Challenge Tasks

Complete these using only slash commands:

1. [ ] Check current token usage
2. [ ] View session statistics
3. [ ] List files in context
4. [ ] Clear conversation history
5. [ ] Switch to a different model
6. [ ] View MCP server status
7. [ ] Get help on all commands

---

## Pro Tips

1. **Keyboard Shortcut:** Most slash commands have keyboard equivalents - check `/help` for mappings
2. **Cost Monitoring:** Run `/usage` after every 10-15 exchanges during long sessions
3. **Context Hygiene:** Use `/clear` when you notice Claude repeating itself
4. **Model Hopping:** Switch to Haiku for quick tasks, then back to Sonnet

---

## Next Challenge

Continue to **[Voice Input](./03-voice-input.md)** to learn hands-free Claude interaction!
