# Walkthrough: Session Recovery

**Difficulty:** Medium | **Time:** 12 minutes | **Category:** Context Management

---

## Overview

Sessions end unexpectedly - terminals close, computers restart, or you simply forget to save state. This challenge teaches you to find, recover, and resume any Claude Code conversation.

## Prerequisites

- [ ] Multiple previous Claude sessions
- [ ] Understanding of session storage
- [ ] Access to command history

---

## Step 1: Understanding Session Storage

Claude Code stores session data in:

**macOS/Linux:**
```
~/.claude/
├── sessions/           # Session transcripts
├── conversations/      # Conversation history
└── cache/             # Temporary data
```

**Windows:**
```
%USERPROFILE%\.claude\
├── sessions\
├── conversations\
└── cache\
```

---

## Step 2: List Recent Sessions

### Using Claude Code
```
/sessions
```

**Expected Output:**
```
Recent Sessions:
  1. [2h ago]  auth-feature (src/auth/) - 45 messages
  2. [1d ago]  bug-fix-123 (src/api/) - 23 messages
  3. [2d ago]  refactoring (src/utils/) - 67 messages
  4. [3d ago]  documentation (docs/) - 12 messages
```

### Using Command Line
```bash
# List session files by date
ls -la ~/.claude/sessions/ | head -20

# Find sessions from specific project
grep -l "your-project-name" ~/.claude/sessions/*
```

---

## Step 3: Resume a Previous Session

### By Session ID
```
/resume [session-id]
```

### By Continue Flag
```bash
# Continue most recent session
claude --continue

# Or in short form
claude -c
```

### By Project Directory
```bash
# Claude remembers sessions by directory
cd ~/projects/my-app
claude --continue
```

---

## Step 4: Search Session History

Find sessions by content:

```bash
# Search for sessions mentioning specific topic
grep -r "authentication" ~/.claude/sessions/

# Find sessions that modified a file
grep -r "src/api/users.ts" ~/.claude/sessions/

# Find sessions with errors
grep -r "error\|Error\|ERROR" ~/.claude/sessions/
```

---

## Step 5: Recover from Crash

If a session ended unexpectedly:

### Check for Recovery Data
```
/recover
```

### Manual Recovery
```bash
# Find the most recent session file
ls -lt ~/.claude/sessions/ | head -5

# View session content
cat ~/.claude/sessions/[most-recent-session-file]
```

### Resume with Context
```
I was working on [task] when my session ended unexpectedly.
Here's what I remember:
- [Last thing completed]
- [What was in progress]
- [Files being modified]

Let's resume from there.
```

---

## Step 6: Session Bookmarking

### Create Named Checkpoints
```
/bookmark auth-complete
```

### Resume from Bookmark
```
/resume auth-complete
```

### List Bookmarks
```
/bookmarks
```

---

## Step 7: Prevent Session Loss

### Auto-Save Strategy
```bash
# Add to your workflow - save progress periodically
alias csave='claude "Summarize current progress for recovery" >> ~/claude-progress.md'
```

### Pre-Session Checklist
- [ ] Note current working directory
- [ ] Record the main objective
- [ ] Consider creating a handoff after major milestones

### Session Hygiene
```
Every 30 minutes:
1. Check /usage for token consumption
2. Consider if a checkpoint makes sense
3. Create mini-handoff if > 50% context used
```

---

## Verification Checklist

- [ ] Located session storage directory
- [ ] Listed previous sessions
- [ ] Successfully resumed a past session
- [ ] Searched sessions for specific content
- [ ] Recovered from a simulated crash
- [ ] Created a session bookmark

---

## Recovery Strategies by Scenario

### Scenario 1: Terminal Closed Accidentally
```bash
# Immediately
claude --continue

# If that doesn't work
ls -lt ~/.claude/sessions/ | head -1
# Resume using that session ID
```

### Scenario 2: Computer Restarted
```bash
# Navigate to project directory
cd ~/projects/my-app

# Try continue
claude --continue

# If no match, list recent sessions
claude
/sessions
```

### Scenario 3: It's Been Days
```bash
# Search by topic
grep -l "feature-name" ~/.claude/sessions/*

# Or by date range
find ~/.claude/sessions/ -mtime -7 -type f | head -10
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Session not found | Check you're in the right directory |
| Too many sessions listed | Use date/content filtering |
| Session corrupted | Fall back to handoff documents |
| Old session missing | Sessions may be pruned after 30 days |

---

## Pro Tips

1. **Same Directory:** Return to the original working directory for best session matching
2. **Descriptive Work:** Mention project names during sessions for easier searching
3. **Regular Handoffs:** Don't rely solely on session recovery
4. **Backup Important Sessions:** Copy critical session files before they're pruned

---

## Session Recovery Quick Reference

| Command | Purpose |
|---------|---------|
| `/sessions` | List recent sessions |
| `/resume [id]` | Resume specific session |
| `claude --continue` | Continue last session |
| `/recover` | Attempt crash recovery |
| `/bookmark [name]` | Save named checkpoint |
| `/bookmarks` | List all bookmarks |

---

## Next Challenge

Continue to **[Fork Strategies](./04-fork-strategies.md)** to learn how to branch your conversations!
