# Walkthrough: Git Worktrees

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** Workflow Automation

---

## Overview

Git worktrees let you check out multiple branches simultaneously in separate directories. Work on a feature while keeping main ready for hotfixes, or compare implementations side-by-side.

## Prerequisites

- [ ] Git 2.5+ installed
- [ ] An existing Git repository
- [ ] Multiple branches to work with

---

## Step 1: Understanding Worktrees

### Traditional Git
```
project/
├── .git/
└── [current branch only]

Switch branches = lose current state
```

### With Worktrees
```
project/              (main branch)
├── .git/
├── src/
└── ...

project-feature/      (feature branch)
├── src/
└── ...

project-hotfix/       (hotfix branch)
├── src/
└── ...

Multiple branches, simultaneously!
```

---

## Step 2: Create a Worktree

### For Existing Branch
```bash
# Create worktree for existing branch
git worktree add ../project-feature feature/new-login
```

### For New Branch
```bash
# Create new branch and worktree
git worktree add -b feature/api-v2 ../project-api-v2
```

---

## Step 3: List Worktrees

```bash
git worktree list

# Output:
# /home/user/project       abc123 [main]
# /home/user/project-feature def456 [feature/new-login]
# /home/user/project-api-v2  ghi789 [feature/api-v2]
```

---

## Step 4: Work in Parallel

### Terminal Setup
```
Tab 1: cd ~/project         # main branch
Tab 2: cd ~/project-feature # feature branch
Tab 3: cd ~/project-hotfix  # hotfix branch
```

### With Claude
```
Tab 1: cd ~/project && claude        # Work on main
Tab 2: cd ~/project-feature && claude # Separate Claude session
```

---

## Step 5: Practical Workflows

### Pattern A: Feature + Hotfix
```bash
# Working on feature
git worktree add ../project-feature feature/big-feature

# Urgent hotfix comes in
git worktree add ../project-hotfix -b hotfix/critical-bug

# Work on hotfix, merge to main
cd ../project-hotfix
# ... fix bug ...
git commit -m "fix: Critical bug"
git push

# Return to feature work
cd ../project-feature
# ... continue feature ...
```

### Pattern B: Compare Implementations
```bash
# Approach A
git worktree add ../project-approach-a -b feature/approach-a

# Approach B
git worktree add ../project-approach-b -b feature/approach-b

# Compare and choose
diff ../project-approach-a/src ../project-approach-b/src
```

---

## Step 6: Cleanup Worktrees

### Remove Worktree
```bash
# Remove worktree (branch still exists)
git worktree remove ../project-feature

# Or manually delete then prune
rm -rf ../project-feature
git worktree prune
```

### Remove Branch Too
```bash
git worktree remove ../project-feature
git branch -d feature/new-login
```

---

## Step 7: Claude + Worktrees

### Multi-Branch Development
```
I need to work on main and a feature branch simultaneously.

In ~/project (main):
- Apply hotfixes
- Keep stable

In ~/project-feature (feature/auth):
- Develop new authentication
- Safe to break things

Let me know which directory you need to work in for each task.
```

### Comparing Approaches
```
I've created two worktrees to compare approaches:
- ../approach-a: Uses Redux
- ../approach-b: Uses Zustand

Implement the same feature in both, then help me compare.
```

---

## Verification Checklist

- [ ] Created a worktree for existing branch
- [ ] Created a worktree with new branch
- [ ] Listed all worktrees
- [ ] Worked in multiple worktrees simultaneously
- [ ] Removed a worktree cleanly
- [ ] Used worktrees with Claude

---

## Worktree Commands Reference

| Command | Purpose |
|---------|---------|
| `git worktree add <path> <branch>` | Create worktree |
| `git worktree add -b <branch> <path>` | Create with new branch |
| `git worktree list` | List all worktrees |
| `git worktree remove <path>` | Remove worktree |
| `git worktree prune` | Clean up stale references |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| "Branch already checked out" | Each branch can only be in one worktree |
| Forgot which worktree I'm in | Use `pwd` and `git branch` |
| Stale worktree references | Run `git worktree prune` |
| Disk space | Worktrees share .git, minimal overhead |

---

## Pro Tips

1. **Naming Convention:** Use `project-[branch-name]` format
2. **Sibling Directories:** Keep worktrees at same level as main repo
3. **Shared Objects:** Worktrees share .git data, saving space
4. **IDE Support:** Most IDEs can open worktrees as separate projects

---

## Next Challenge

Continue to **[Exponential Backoff](./03-exponential-backoff.md)** for smart polling!
