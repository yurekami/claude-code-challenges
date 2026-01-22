# Walkthrough: Git Integration

**Difficulty:** Easy | **Time:** 15 minutes | **Category:** CLI Fundamentals

---

## Overview

Claude Code integrates seamlessly with Git, understanding your repository structure, branches, and history. This challenge teaches you to leverage Git-aware features for efficient version control workflows.

## Prerequisites

- [ ] Git installed and configured
- [ ] Working in a Git repository
- [ ] Basic Git knowledge (commit, branch, merge)

---

## Step 1: Verify Git Integration

Claude automatically detects Git repositories. Check the status line:

```
[Branch: main] ← Indicates Git is detected
```

Verify Claude can access Git:

```
What branch am I on and what were the last 3 commits?
```

**Expected Response:** Claude uses Git commands internally and provides the information.

---

## Step 2: Git-Aware File Operations

Claude understands Git-tracked files:

```
Show me all modified files since the last commit
```

**Claude runs internally:**
```bash
git status --short
git diff --name-only
```

**Example Response:**
```
Modified files since last commit:
  M src/api/users.ts (23 lines changed)
  M tests/users.test.ts (15 lines changed)
  A src/utils/validation.ts (new file)
```

---

## Step 3: Commit Message Generation

Let Claude write commit messages:

```
Generate a commit message for my current changes
```

**Claude analyzes:**
1. `git diff --staged`
2. Files changed
3. Nature of changes

**Example Output:**
```
Suggested commit message:

feat(api): Add user validation middleware

- Add validateUserInput function with Zod schema
- Update user routes to use validation
- Add comprehensive test coverage for edge cases

Closes #123
```

---

## Step 4: Branch-Aware Development

Create feature branches with Claude's help:

```
Create a new feature branch for adding email notifications
```

**Claude suggests and can execute:**
```bash
git checkout -b feature/email-notifications
```

**Best Practice:** Let Claude name branches following your project's conventions.

---

## Step 5: Review Changes Before Commit

Ask Claude to review your work:

```
Review my changes before I commit
```

**Claude will:**
1. Run `git diff`
2. Analyze each change
3. Flag potential issues
4. Suggest improvements

**Example Review:**
```
Reviewing staged changes...

✅ users.ts: Good - Added proper error handling
⚠️ config.ts: Warning - Hardcoded API key on line 23
❌ utils.ts: Issue - console.log left on line 45
📝 Suggestion: Add JSDoc to the new validateEmail function
```

---

## Step 6: Handle Merge Conflicts

When conflicts occur, Claude can help:

```
I have a merge conflict in src/api/users.ts, help me resolve it
```

**Claude will:**
1. Read the conflicting file
2. Understand both versions
3. Suggest a resolution
4. Explain the reasoning

---

## Step 7: Git History Analysis

Leverage Git history for debugging:

```
When was the login function last modified and why?
```

**Claude runs:**
```bash
git log -p --follow -S "login" -- src/auth/login.ts
```

**Response:**
```
The login function was last modified:
  Commit: abc123
  Author: developer@example.com
  Date: 3 days ago
  Message: "fix: Handle expired session tokens"

The change added token expiration checking...
```

---

## Verification Checklist

- [ ] Claude detects your Git repository
- [ ] Can view modified files through Claude
- [ ] Generated at least one commit message
- [ ] Created a branch with Claude's help
- [ ] Had Claude review changes before commit
- [ ] Used Git history to understand code changes

---

## Common Git Workflows with Claude

### Feature Development
```
1. "Create a branch for the new dashboard feature"
2. [Make changes with Claude's help]
3. "Generate a commit message for these changes"
4. "Review my changes before I push"
5. "Create a pull request for this branch"
```

### Bug Fix
```
1. "Find when this bug was introduced using git bisect"
2. "Create a fix branch from main"
3. [Fix the bug with Claude]
4. "Write a commit message mentioning the issue number"
5. "Cherry-pick this to the release branch"
```

### Code Review
```
1. "Show me what changed in PR #123"
2. "Review these changes for potential issues"
3. "Summarize the PR for the team"
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Claude can't see Git status | Ensure you're in a Git repo directory |
| Wrong branch shown | Run `git status` to verify, Claude will update |
| Commit message style wrong | Specify your convention: "Use conventional commits format" |
| Can't push | Check remote configuration and permissions |

---

## Pro Tips

1. **Conventional Commits:** Tell Claude your commit style: "Use type(scope): message format"
2. **Pre-commit Review:** Always ask Claude to review before committing
3. **Branch Protection:** Claude won't force push to protected branches by default
4. **Atomic Commits:** Ask Claude to suggest logical commit boundaries

---

## Advanced Git Commands

Claude can help with advanced Git operations:

```
# Interactive rebase
"Help me squash the last 3 commits"

# Cherry pick
"Cherry-pick commit abc123 to the release branch"

# Bisect
"Use git bisect to find when the tests started failing"

# Stash management
"Stash my changes, switch to main, then pop the stash"
```

---

## Next Challenge

Continue to **[Fresh Starts](./06-fresh-starts.md)** to learn when and how to begin new Claude sessions!
