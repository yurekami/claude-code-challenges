# Walkthrough: Terminal Cascade

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** Workflow Automation

---

## Overview

Multiple terminal tabs in a cascade pattern let you run parallel processes - dev server, logs, git, and commands - all simultaneously. This challenge teaches you to set up an efficient multi-terminal workflow.

## Prerequisites

- [ ] Terminal with tab support (iTerm2, Windows Terminal, etc.)
- [ ] A project with dev server
- [ ] Understanding of basic terminal commands

---

## Step 1: The Cascade Pattern

```
┌─────────────────────────────────────────────────────┐
│ Tab 1: DEV          │ Tab 2: LOGS                   │
│ npm run dev         │ tail -f app.log               │
├─────────────────────┼───────────────────────────────┤
│ Tab 3: GIT          │ Tab 4: CLAUDE/GENERAL         │
│ git operations      │ Claude Code / commands        │
└─────────────────────┴───────────────────────────────┘
```

---

## Step 2: Set Up Your Tabs

### Tab 1: Development Server
```bash
# Label: DEV
cd ~/project
npm run dev
```

### Tab 2: Log Monitoring
```bash
# Label: LOGS
tail -f logs/app.log  # or
npm run dev 2>&1 | tee logs/dev.log
```

### Tab 3: Git Operations
```bash
# Label: GIT
cd ~/project
# Ready for git commands
```

### Tab 4: Claude / General
```bash
# Label: CLAUDE
cd ~/project
claude
```

---

## Step 3: Keyboard Navigation

### macOS (iTerm2/Terminal)
| Shortcut | Action |
|----------|--------|
| `Cmd+T` | New tab |
| `Cmd+1-9` | Go to tab N |
| `Cmd+Shift+[` | Previous tab |
| `Cmd+Shift+]` | Next tab |
| `Cmd+W` | Close tab |

### Windows Terminal
| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+T` | New tab |
| `Ctrl+Alt+1-9` | Go to tab N |
| `Ctrl+Tab` | Next tab |
| `Ctrl+Shift+Tab` | Previous tab |

### Linux (various)
| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+T` | New tab |
| `Alt+1-9` | Go to tab N |

---

## Step 4: Real Workflow Example

### Starting Your Day
```
Tab 1 (DEV): npm run dev
Tab 2 (LOGS): npm run dev 2>&1 | grep -E "(error|warn)"
Tab 3 (GIT): git fetch && git status
Tab 4 (CLAUDE): claude
```

### During Development
```
1. Write code with Claude (Tab 4)
2. See live reload (Tab 1)
3. Monitor for errors (Tab 2)
4. Commit changes (Tab 3)
```

---

## Step 5: Advanced Patterns

### Pattern A: Frontend + Backend
```
Tab 1: cd frontend && npm run dev
Tab 2: cd backend && npm run dev
Tab 3: docker-compose logs -f
Tab 4: Claude Code
```

### Pattern B: Testing Workflow
```
Tab 1: npm run dev
Tab 2: npm test -- --watch
Tab 3: Git operations
Tab 4: Claude Code
```

### Pattern C: Microservices
```
Tab 1: Service A
Tab 2: Service B
Tab 3: Service C
Tab 4: Claude + Git
```

---

## Step 6: Tab Naming (Optional)

### iTerm2
Right-click tab → Edit Session → Set title

### Windows Terminal
Edit `settings.json`:
```json
{
  "profiles": {
    "list": [
      {
        "name": "Dev Server",
        "startingDirectory": "~/project"
      }
    ]
  }
}
```

---

## Verification Checklist

- [ ] Created 4+ terminal tabs
- [ ] Running dev server in one tab
- [ ] Monitoring logs in another
- [ ] Using Claude in a dedicated tab
- [ ] Can switch tabs with keyboard only
- [ ] Completed full dev cycle without closing tabs

---

## Common Patterns

| Workflow | Tab Layout |
|----------|------------|
| Web Dev | Dev, Logs, Git, Claude |
| Full Stack | Frontend, Backend, DB, Claude |
| Testing | Dev, Tests, Coverage, Claude |
| DevOps | Logs, Metrics, Deploy, Claude |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Tabs get confusing | Name them clearly |
| Process dies, tab closes | Use `; bash` to keep open |
| Too many tabs | Group by concern, max 4-5 |
| Forget which tab is which | Use consistent positions |

---

## Pro Tips

1. **Consistent Layout:** Always use same tab order
2. **Quick Access:** Learn numeric tab shortcuts
3. **Keep Alive:** Add ` || read` to keep tabs open on error
4. **Split Panes:** Use splits for related processes

---

## Next Challenge

Continue to **[Git Worktrees](./02-git-worktrees.md)** to work on multiple branches!
