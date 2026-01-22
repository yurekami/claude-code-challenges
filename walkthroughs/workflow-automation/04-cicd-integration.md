# Walkthrough: CI/CD Integration

**Difficulty:** Hard | **Time:** 25 minutes | **Category:** Workflow Automation

---

## Overview

CI/CD pipelines often fail with cryptic errors. This challenge teaches you to debug GitHub Actions (and other CI systems) with Claude's help - reading logs, identifying issues, and fixing pipeline problems.

## Prerequisites

- [ ] GitHub repository with Actions enabled
- [ ] Basic YAML knowledge
- [ ] Understanding of CI/CD concepts

---

## Step 1: Access CI/CD Information

### Using gh CLI
```bash
# List recent workflow runs
gh run list

# View specific run
gh run view 12345678

# View run logs
gh run view 12345678 --log

# View failed job logs
gh run view 12345678 --log-failed
```

### With Claude
```
Check the status of our latest GitHub Actions run and show me any failures.
```

---

## Step 2: Common CI Failures

### Category: Dependencies
```
Error: npm ERR! 404 Not Found - GET https://registry.npmjs.org/package
```
**Fix:** Check package name, registry config, or .npmrc

### Category: Tests
```
FAIL tests/user.test.ts
  ✕ should create user (timeout)
```
**Fix:** Increase timeout, check async handling

### Category: Build
```
error TS2304: Cannot find name 'process'
```
**Fix:** Add @types/node or configure tsconfig

### Category: Environment
```
Error: ENOENT: no such file or directory
```
**Fix:** Check file paths, working directory

---

## Step 3: Debug Workflow with Claude

### Fetch and Analyze
```
Fetch the logs from the failed GitHub Actions run and:
1. Identify the exact error
2. Find the root cause
3. Suggest a fix
4. Update the workflow file if needed
```

### Claude's Approach
1. Uses `gh run view --log-failed`
2. Parses error messages
3. Checks workflow YAML
4. Proposes solution

---

## Step 4: Common Workflow Fixes

### Fix: Caching Issues
```yaml
# Before (no cache)
- run: npm install

# After (with cache)
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'
```

### Fix: Environment Variables
```yaml
# Add secrets
- run: npm test
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
    API_KEY: ${{ secrets.API_KEY }}
```

### Fix: Permissions
```yaml
# Add required permissions
permissions:
  contents: read
  pull-requests: write
```

### Fix: Matrix Strategy for Multiple Versions
```yaml
strategy:
  matrix:
    node-version: [18, 20, 22]
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: ${{ matrix.node-version }}
```

---

## Step 5: Debugging Strategies

### Step 1: Get Full Context
```bash
# Download all logs
gh run view 12345678 --log > ci-logs.txt

# Share with Claude
"Here are the full CI logs, find the failure"
```

### Step 2: Enable Debug Logging
```yaml
env:
  ACTIONS_STEP_DEBUG: true
  ACTIONS_RUNNER_DEBUG: true
```

### Step 3: Add Debug Steps
```yaml
- name: Debug info
  run: |
    echo "Node: $(node -v)"
    echo "npm: $(npm -v)"
    echo "Dir: $(pwd)"
    ls -la
```

---

## Step 6: Proactive CI Fixes

### Local CI Reproduction
```bash
# Use act to run Actions locally
brew install act
act -j build
```

### Pre-push Verification
```bash
#!/bin/bash
# pre-push hook
npm run lint && npm run typecheck && npm test
```

---

## Step 7: Monitoring and Alerts

### Check Status in Claude
```
Monitor the GitHub Actions for our PR:
- Run: gh run list --limit 5
- Check: Are any failing?
- If failed: Get logs and diagnose
- Report: Summary of status
```

### Workflow Status Badge
```markdown
![CI](https://github.com/user/repo/actions/workflows/ci.yml/badge.svg)
```

---

## Verification Checklist

- [ ] Used gh CLI to view run status
- [ ] Retrieved logs from failed run
- [ ] Identified root cause of failure
- [ ] Fixed a workflow issue
- [ ] Run passed after fix

---

## Common CI Issues Reference

| Error Pattern | Likely Cause | Fix |
|---------------|--------------|-----|
| `npm ERR! 404` | Wrong package name | Check package.json |
| `ENOENT` | Missing file | Check paths |
| `Permission denied` | File permissions | chmod in workflow |
| `OOM killed` | Memory limit | Reduce parallelism |
| `Timeout` | Slow tests | Increase timeout |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Can't reproduce locally | Use `act` for local testing |
| Secrets not available | Check secret names and scope |
| Cache issues | Clear cache or change key |
| Rate limiting | Add delays or reduce API calls |

---

## Pro Tips

1. **Fail Fast:** Put quick checks (lint) before slow ones (tests)
2. **Cache Everything:** Dependencies, build artifacts, test results
3. **Parallel Jobs:** Use matrix strategy for speed
4. **Clear Errors:** Add meaningful error messages

---

## Next Challenge

Continue to **[Input Navigation](./05-input-navigation.md)** to master readline shortcuts!
