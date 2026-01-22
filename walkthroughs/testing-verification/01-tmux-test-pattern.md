# Walkthrough: tmux Test Pattern

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** Testing & Verification

---

## Overview

Long-running tests and processes can block your Claude session. The tmux test pattern allows Claude to execute tests in a detached session, monitor progress, and retrieve results - enabling autonomous test execution.

## Prerequisites

- [ ] tmux installed (`brew install tmux` or `apt install tmux`)
- [ ] Basic terminal knowledge
- [ ] A project with tests

---

## Step 1: Understanding the Pattern

### The Problem
```
Claude runs: npm test
→ Tests take 5 minutes
→ Claude session is blocked
→ You can't do anything else
```

### The Solution
```
Claude runs: tmux new-session -d "npm test"
→ Tests run in background
→ Claude continues working
→ Check results when ready
```

---

## Step 2: tmux Basics

### Essential Commands
```bash
# Create detached session
tmux new-session -d -s test-session "npm test"

# List sessions
tmux ls

# Attach to session (view output)
tmux attach -t test-session

# Capture output from session
tmux capture-pane -t test-session -p

# Kill session
tmux kill-session -t test-session
```

---

## Step 3: The Test Pattern

### Step-by-Step
```
1. Claude starts tests in tmux
2. Claude periodically checks status
3. When tests complete, Claude analyzes results
4. Claude reports findings or fixes issues
```

### Ask Claude to Use It
```
Run the test suite in a tmux session so we can continue working.
Check the results every 30 seconds and let me know when done.
```

---

## Step 4: Implement the Pattern

### Start Tests
```bash
# Create session and run tests
tmux new-session -d -s tests "npm test 2>&1"
```

### Monitor Progress
```bash
# Check if still running
tmux has-session -t tests 2>/dev/null && echo "Running" || echo "Finished"

# View last 50 lines of output
tmux capture-pane -t tests -p | tail -50
```

### Capture Full Results
```bash
# Get all output
tmux capture-pane -t tests -p -S - > test-results.txt
```

---

## Step 5: Advanced Patterns

### Pattern A: Continuous Integration Style
```
Run tests in tmux, wait for completion, then:
1. If pass: Proceed with commit
2. If fail: Show me the failures and suggest fixes
```

### Pattern B: Watch Mode
```
Start tests in watch mode:
tmux new-session -d -s watch "npm test -- --watch"

Then check periodically as I make changes.
```

### Pattern C: Multiple Test Suites
```bash
# Unit tests
tmux new-session -d -s unit "npm run test:unit"

# Integration tests
tmux new-session -d -s integration "npm run test:integration"

# Check both
tmux capture-pane -t unit -p
tmux capture-pane -t integration -p
```

---

## Step 6: Error Handling

### Detect Failures
```bash
# Check exit code (requires capturing)
tmux send-keys -t tests "echo Exit: $?" Enter
tmux capture-pane -t tests -p | grep "Exit:"
```

### Timeout Handling
```bash
# Kill if running too long
timeout 300 tmux wait-for tests || tmux kill-session -t tests
```

---

## Step 7: Integration with Claude Workflow

### Prompt Template
```
When running long tests:
1. Start in tmux: tmux new-session -d -s [name] "[command]"
2. Continue other work
3. Check periodically: tmux capture-pane -t [name] -p | tail -20
4. When complete, analyze results
5. Report or fix issues
6. Clean up: tmux kill-session -t [name]
```

### Add to CLAUDE.md
```markdown
## Testing
- Long-running tests: Use tmux pattern
- Check status: tmux capture-pane -t [session] -p
- Always clean up sessions when done
```

---

## Verification Checklist

- [ ] tmux is installed and working
- [ ] Started tests in a detached tmux session
- [ ] Monitored test progress
- [ ] Captured test output
- [ ] Analyzed results after completion
- [ ] Cleaned up tmux session

---

## tmux Quick Reference

| Command | Purpose |
|---------|---------|
| `tmux new -d -s name "cmd"` | Start detached session |
| `tmux ls` | List sessions |
| `tmux attach -t name` | View session |
| `Ctrl+B, D` | Detach from session |
| `tmux capture-pane -t name -p` | Get output |
| `tmux kill-session -t name` | End session |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| "Session not found" | Check session name with `tmux ls` |
| Output truncated | Use `-S -` flag for full history |
| Session persists | Always kill-session when done |
| Can't see output | Attach to session or capture-pane |

---

## Pro Tips

1. **Naming:** Use descriptive session names (test-unit, test-e2e)
2. **Logging:** Redirect output to files for persistence
3. **Cleanup:** Always kill sessions when done
4. **Parallel:** Run multiple test suites simultaneously

---

## Next Challenge

Continue to **[Output Verification](./02-output-verification.md)** for systematic result checking!
