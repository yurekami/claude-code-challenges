# Walkthrough: Git Bisect Debug

**Difficulty:** Medium | **Time:** 18 minutes | **Category:** Testing & Verification

---

## Overview

Something broke, but when? Git bisect uses binary search to find the exact commit that introduced a bug. This challenge teaches you to use git bisect with Claude for efficient debugging.

## Prerequisites

- [ ] Git repository with history
- [ ] A bug to track down
- [ ] Knowledge of a "good" commit (before bug)

---

## Step 1: Understand Git Bisect

### The Problem
```
Commit history:
A → B → C → D → E → F → G → H (current, broken)
                    ^
                    Somewhere here the bug was introduced
```

### The Solution
```
Git bisect uses binary search:
1. Mark H as "bad"
2. Mark A as "good"
3. Git checks out middle commit (D)
4. You test: good or bad?
5. Repeat until culprit found

log2(N) tests instead of N tests!
```

---

## Step 2: Start Git Bisect

### Initialize
```bash
# Start bisect session
git bisect start

# Mark current (broken) as bad
git bisect bad

# Mark known good commit
git bisect good abc123  # commit hash or tag
```

### Git Responds
```
Bisecting: 15 revisions left to test after this
[def456...] Commit message of middle commit
```

---

## Step 3: Test Each Commit

### Manual Testing
```bash
# Test the current commit
npm test  # or your test command

# If bug exists
git bisect bad

# If bug doesn't exist
git bisect good
```

### With Claude
```
We're doing a git bisect to find a bug.
Current commit: def456
Test: [run the relevant test]
Tell me if this commit has the bug or not.
```

---

## Step 4: Automate with Test Script

### Create Test Script
```bash
#!/bin/bash
# test-for-bug.sh

# Run the specific test that reveals the bug
npm test -- --grep "failing test name"

# Exit 0 = good, Exit 1+ = bad
```

### Run Automated Bisect
```bash
git bisect start
git bisect bad HEAD
git bisect good abc123
git bisect run ./test-for-bug.sh
```

**Git automatically finds the bad commit!**

---

## Step 5: Analyze the Bad Commit

### When Bisect Completes
```
abc123def456 is the first bad commit
commit abc123def456
Author: developer@example.com
Date:   Mon Jan 15 10:30:00 2024

    feat: Add caching to user service
```

### Examine the Change
```bash
# View the diff
git show abc123def456

# View affected files
git diff abc123def456^..abc123def456 --stat
```

### Ask Claude
```
This commit introduced a bug:
[paste git show output]

The bug is: [describe bug]
What specifically in this change caused it?
```

---

## Step 6: Complete the Session

### End Bisect
```bash
# Return to original branch
git bisect reset
```

### Document Findings
```
Bug Bisect Results:
- Breaking commit: abc123
- Author: developer@example.com
- Change: Added caching to user service
- Root cause: Cache wasn't invalidated on update
```

---

## Step 7: Claude-Assisted Bisect

### Full Workflow with Claude
```
I need to find when this bug was introduced:
[Describe the bug]

Known good commit: [commit or tag]
Current bad commit: HEAD

Please:
1. Start git bisect
2. For each commit, run [test command]
3. Mark as good or bad based on test result
4. Continue until you find the bad commit
5. Show me the breaking change
```

---

## Verification Checklist

- [ ] Started a git bisect session
- [ ] Marked good and bad commits
- [ ] Tested at least 3 intermediate commits
- [ ] Found the breaking commit
- [ ] Analyzed the breaking change
- [ ] Reset bisect when done

---

## Bisect Commands Reference

| Command | Purpose |
|---------|---------|
| `git bisect start` | Begin bisect |
| `git bisect bad [commit]` | Mark commit as broken |
| `git bisect good [commit]` | Mark commit as working |
| `git bisect skip` | Skip untestable commit |
| `git bisect reset` | End bisect, return to HEAD |
| `git bisect run <script>` | Automate testing |
| `git bisect log` | Show bisect history |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Can't build old commits | Use `git bisect skip` |
| Wrong good/bad marked | Use `git bisect reset` and restart |
| Test is flaky | Make test deterministic first |
| Too many commits | Start closer to known good |

---

## Pro Tips

1. **Specific Tests:** Use the most targeted test possible
2. **Clean State:** Reset state between tests if needed
3. **Automate:** Write a test script for `git bisect run`
4. **Skip Broken:** Use `git bisect skip` for unbuildable commits

---

## Advanced: Bisect for Non-Bugs

### Finding Performance Regression
```bash
#!/bin/bash
# test-performance.sh
time=$(npm run benchmark | grep "Time:")
if [ "$time" -gt 1000 ]; then
    exit 1  # bad - too slow
else
    exit 0  # good - fast enough
fi
```

### Finding When Feature Worked
```bash
# Reverse bisect - find when something broke
git bisect start --term-new=broken --term-old=working
```

---

## Next Challenge

Continue to **[Command Audit](./04-command-audit.md)** to review approved commands safely!
