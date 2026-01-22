# Walkthrough: Background Execution

**Difficulty:** Hard | **Time:** 25 minutes | **Category:** Advanced Orchestration

---

## Overview

Long-running tasks shouldn't block your workflow. Background execution lets you run builds, tests, and deployments while continuing to work on other things. This challenge teaches you to manage asynchronous workflows with Claude.

## Prerequisites

- [ ] Terminal multiplexer (tmux) installed
- [ ] Long-running tasks to manage
- [ ] Understanding of process management

---

## Step 1: Why Background Execution?

### The Blocking Problem
```
Traditional flow:
→ Run build (5 min wait)
→ Run tests (3 min wait)
→ Deploy (2 min wait)
Total: 10 minutes of waiting
```

### Background Flow
```
Parallel flow:
→ Start build in background
→ Continue working
→ Get notified when done
→ Review results
Total: 0 minutes waiting
```

---

## Step 2: Using tmux for Background Tasks

### Basic tmux Commands
```bash
# Create new session
tmux new-session -d -s build

# Send command to session
tmux send-keys -t build 'npm run build' Enter

# Check session status
tmux list-sessions

# View session output
tmux attach -t build

# Detach from session
Ctrl+B, then D
```

### Ask Claude to Use tmux
```
Run these commands in the background:
1. npm run build
2. npm test
3. npm run lint

Use separate tmux sessions for each.
Notify me when any completes.
```

---

## Step 3: Claude's Background Execution

### Using Bash with run_in_background
```
Claude can run commands with the run_in_background parameter.
This allows monitoring while continuing to work.

Example:
"Run the full test suite in background"
→ Claude uses background execution
→ Returns task ID
→ You can check status later
```

### Checking Background Tasks
```
"What's the status of my background tasks?"
→ Claude checks running processes
→ Reports completion or progress
```

---

## Step 4: Multiple Parallel Tasks

### Launch Parallel Builds
```
I need to:
1. Run tests on Node 18
2. Run tests on Node 20
3. Run the linter
4. Generate documentation

Run all four in parallel, report results when done.
```

### Monitor Progress
```
┌─────────────────────────────────────┐
│  Background Task Status             │
├─────────────────────────────────────┤
│  [✓] Node 18 tests - PASSED         │
│  [⋯] Node 20 tests - Running...     │
│  [✓] Linter - 0 errors              │
│  [⋯] Docs generation - Running...   │
└─────────────────────────────────────┘
```

---

## Step 5: Long-Running Workflows

### CI-like Pipeline
```
Run this deployment pipeline in background:

1. Install dependencies
2. Run linter
3. Run unit tests
4. Run integration tests
5. Build production bundle
6. Deploy to staging
7. Run smoke tests

Continue even if early steps pass.
Stop and alert if any step fails.
```

### Database Migrations
```
Run this migration in background:
- Apply migration scripts
- Validate data integrity
- Generate migration report

This might take 15+ minutes.
Let me know when done or if errors occur.
```

---

## Step 6: Notification Patterns

### After Long Task Completes
```
When the build completes:
1. Summarize the results
2. Highlight any warnings/errors
3. Show total time taken
4. Suggest next steps
```

### Error Alerting
```
If any background task fails:
1. Stop immediately
2. Show the error
3. Show relevant logs
4. Suggest fixes
```

---

## Step 7: Advanced Patterns

### Watch Mode
```bash
# Start file watcher in background
tmux new-session -d -s watch 'npm run watch'

# Meanwhile, continue working
# Watcher rebuilds on changes automatically
```

### Scheduled Checks
```
Every 5 minutes, check:
1. Are services still running?
2. Any new errors in logs?
3. Resource usage normal?

Alert if anything abnormal.
```

### Parallel Development
```
While I work on feature A:
- Run feature A tests continuously
- Keep the dev server running
- Watch for TypeScript errors

All in background, alert on failures.
```

---

## Background Task Management

### List Active Tasks
```
Show me all running background tasks:
- What's running
- How long it's been running
- Current status/output
```

### Kill Task
```
Stop the build task - I found an issue
and need to restart with fixes.
```

### Resume Monitoring
```
Show me the output of the test run
that started 10 minutes ago.
```

---

## Verification Checklist

- [ ] Started a task in background using tmux
- [ ] Ran multiple tasks in parallel
- [ ] Monitored background task progress
- [ ] Received completion notification
- [ ] Managed (listed/killed) background tasks

---

## Background Execution Commands

| Action | Command/Approach |
|--------|------------------|
| Start background | `tmux new-session -d -s name 'command'` |
| Check status | `tmux list-sessions` |
| View output | `tmux attach -t name` |
| Detach | `Ctrl+B, D` |
| Kill session | `tmux kill-session -t name` |
| Send command | `tmux send-keys -t name 'cmd' Enter` |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Lost output | Use tmux to preserve session |
| Zombie processes | Always clean up with kill-session |
| Forgetting tasks | List sessions regularly |
| Output too verbose | Use logging to file instead |

---

## Pro Tips

1. **Name Sessions:** Use descriptive names like `build-main`, `test-unit`
2. **Log to File:** Redirect output for later review
3. **Set Timeouts:** Kill tasks that run too long
4. **Clean Up:** Remove completed sessions periodically

---

## Session Management Script

```bash
#!/bin/bash
# bg-tasks.sh - Manage background tasks

case "$1" in
  list)
    tmux list-sessions 2>/dev/null || echo "No active sessions"
    ;;
  kill-all)
    tmux kill-server 2>/dev/null
    echo "All sessions killed"
    ;;
  *)
    echo "Usage: bg-tasks.sh [list|kill-all]"
    ;;
esac
```

---

## Next Challenge

Continue to **[Personalized Software](./11-personalized-software.md)** for building custom tools!
