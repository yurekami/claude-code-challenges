# Git Worktrees - Solution

## Step-by-Step Solution

### 1. Understanding Worktrees

**Directory Structure:**
```
project/
├── .git/                    # Main git directory
├── main/                    # Main worktree (default)
│   ├── src/
│   └── package.json
├── feature-auth/            # Worktree for feature branch
│   ├── src/
│   └── package.json
└── hotfix-login/            # Worktree for hotfix branch
    ├── src/
    └── package.json
```

**Key Concept:** All worktrees share the same `.git` directory, but have separate working directories.

### 2. Basic Worktree Commands

**Create a Worktree:**
```bash
# Create worktree for existing branch
git worktree add ../feature-auth feature-branch

# Create worktree with new branch
git worktree add -b hotfix-login ../hotfix-login main

# Create worktree from remote branch
git worktree add ../feature-payment origin/feature-payment
```

**List Worktrees:**
```bash
git worktree list

# Output:
# C:/Users/creat/project        abc123 [main]
# C:/Users/creat/feature-auth   def456 [feature-branch]
# C:/Users/creat/hotfix-login   ghi789 [hotfix-login]
```

**Remove Worktree:**
```bash
# Remove worktree (after merging branch)
git worktree remove ../feature-auth

# Or manually delete directory and prune
rm -rf ../feature-auth
git worktree prune
```

### 3. Complete Workflow Example

**Scenario:** You're working on a feature when an urgent bug is reported.

**Step 1: Initial Setup**
```bash
# You're working in main directory on feature-auth branch
cd C:\Users\creat\CCC\my-project
git checkout -b feature-auth
# Making changes...

# Bug report comes in!
```

**Step 2: Create Hotfix Worktree**
```bash
# Create worktree for hotfix (from main branch)
git worktree add -b hotfix-login C:\Users\creat\CCC\my-project-hotfix main

# Now you have:
# C:\Users\creat\CCC\my-project - feature-auth branch
# C:\Users\creat\CCC\my-project-hotfix - hotfix-login branch
```

**Step 3: Fix Bug in Parallel**
```bash
# Open new terminal tab (see Challenge 1)
cd C:\Users\creat\CCC\my-project-hotfix

# Fix the bug
code src/auth/login.ts
# Make fixes...

git add .
git commit -m "fix: resolve login timeout issue"
git push origin hotfix-login
```

**Step 4: Continue Feature Development**
```bash
# Switch back to original terminal tab
cd C:\Users\creat\CCC\my-project

# Continue working on feature (no stashing needed!)
# Your changes are still here, untouched
```

**Step 5: Merge and Cleanup**
```bash
# After hotfix is merged to main
cd C:\Users\creat\CCC\my-project-hotfix
git checkout main
git pull origin main

# Remove hotfix worktree
cd C:\Users\creat\CCC\my-project
git worktree remove C:\Users\creat\CCC\my-project-hotfix
git branch -d hotfix-login
```

### 4. Advanced Patterns

**Pattern 1: Parallel Testing**
```bash
# Terminal Tab 1: Development
cd C:\Users\creat\CCC\project
npm run dev

# Terminal Tab 2: Testing different implementation
cd C:\Users\creat\CCC\project-experiment
npm test -- --watch

# Terminal Tab 3: Code comparison
diff -r C:\Users\creat\CCC\project\src C:\Users\creat\CCC\project-experiment\src
```

**Pattern 2: Multiple Feature Branches**
```bash
# Setup
git worktree add -b feature-a ../project-feature-a main
git worktree add -b feature-b ../project-feature-b main
git worktree add -b feature-c ../project-feature-c main

# Work on all three simultaneously in different IDE windows
code ../project-feature-a
code ../project-feature-b
code ../project-feature-c
```

**Pattern 3: Review PRs Without Context Switch**
```bash
# Your current work
cd C:\Users\creat\CCC\my-project
# Working on feature-dashboard...

# PR review needed
git worktree add -b review-pr-123 C:\Users\creat\CCC\my-project-review origin/feature-payment

# Review in separate directory
cd C:\Users\creat\CCC\my-project-review
code .
# Review, test, comment...

# Back to your work instantly
cd C:\Users\creat\CCC\my-project
# Continue where you left off
```

### 5. Integration with Claude Code

**Automated Worktree Creation Script:**
```bash
#!/bin/bash
# create-worktree.sh

BRANCH_NAME=$1
BASE_BRANCH=${2:-main}
PROJECT_NAME=$(basename $(pwd))
WORKTREE_PATH="../${PROJECT_NAME}-${BRANCH_NAME}"

if [ -z "$BRANCH_NAME" ]; then
    echo "Usage: ./create-worktree.sh <branch-name> [base-branch]"
    exit 1
fi

echo "Creating worktree at $WORKTREE_PATH..."
git worktree add -b "$BRANCH_NAME" "$WORKTREE_PATH" "$BASE_BRANCH"

echo "Opening in new terminal tab..."
# Windows Terminal
wt -w 0 nt -d "$WORKTREE_PATH"

# Or open in VS Code
# code "$WORKTREE_PATH"
```

**Usage with Claude Code:**
```bash
# Create worktree
./create-worktree.sh feature-new-ui main

# Use Claude Code in worktree
cd ../my-project-feature-new-ui
claude "implement new dashboard UI"

# Original directory remains unchanged
cd ../my-project
# Your work-in-progress is still here
```

### 6. Worktree Management Script

**list-worktrees.sh:**
```bash
#!/bin/bash
# Enhanced worktree listing with status

echo "Current Worktrees:"
echo "=================="

git worktree list | while IFS= read -r line; do
    path=$(echo $line | awk '{print $1}')
    branch=$(echo $line | grep -o '\[.*\]' | tr -d '[]')

    echo ""
    echo "Path: $path"
    echo "Branch: $branch"

    if [ -d "$path" ]; then
        cd "$path"
        echo "Status: $(git status --short | wc -l) changes"
        echo "Last commit: $(git log -1 --format='%h - %s (%ar)')"
    fi
done
```

### 7. Common Workflows

**Workflow 1: Emergency Hotfix**
```bash
# 1. Create hotfix worktree
git worktree add -b hotfix-critical ../project-hotfix main

# 2. Fix in new terminal
cd ../project-hotfix
# Fix bug
git commit -am "fix: critical security issue"
git push

# 3. Continue main work
cd ../project
# No interruption to your flow
```

**Workflow 2: A/B Testing Implementation**
```bash
# Approach A
git worktree add -b approach-a ../project-a main
cd ../project-a
# Implement approach A

# Approach B
git worktree add -b approach-b ../project-b main
cd ../project-b
# Implement approach B

# Run performance tests in parallel
cd ../project-a && npm run bench &
cd ../project-b && npm run bench &

# Compare results and choose winner
```

**Workflow 3: Long-Running Build**
```bash
# Start build in one worktree
cd C:\Users\creat\CCC\project-release
npm run build:production  # Takes 10 minutes

# Continue development in another
cd C:\Users\creat\CCC\project
# Keep coding while build runs
```

## Common Mistakes to Avoid

### 1. **Creating Worktree for Current Branch**
❌ Creating worktree for a branch that's already checked out
```bash
git checkout feature-a
git worktree add ../other feature-a  # ERROR!
```

✅ Checkout different branch or create new one
```bash
git worktree add ../other feature-b
# or
git worktree add -b feature-new ../other main
```

### 2. **Forgetting to Remove Worktrees**
❌ Leaving worktrees after branches are merged
```bash
# Branch merged, but worktree still exists
# Wastes disk space and causes confusion
```

✅ Clean up regularly
```bash
git worktree list
git worktree remove ../old-feature
git worktree prune
```

### 3. **Not Understanding Shared State**
❌ Expecting complete isolation between worktrees
```bash
# Changes to .git config affect all worktrees
# Branches are shared across all worktrees
```

✅ Remember: separate working directories, shared git history

### 4. **Wrong Directory Structure**
❌ Creating worktrees inside main project
```bash
git worktree add ./feature-branch  # Creates nested directory
```

✅ Create worktrees as siblings
```bash
git worktree add ../project-feature-branch
```

### 5. **Not Using Worktrees with CI/CD**
❌ Running CI locally by switching branches
```bash
git checkout release
npm run ci
git checkout main
```

✅ Use worktree for CI testing
```bash
git worktree add ../project-ci release
cd ../project-ci && npm run ci
# Main directory unaffected
```

## Pro Tips

### 1. **Worktree Naming Convention**
```bash
# Pattern: <project>-<branch-type>-<name>
my-app/              # main worktree
my-app-feature-auth/ # feature branch
my-app-hotfix-login/ # hotfix branch
my-app-release-1.0/  # release branch
```

### 2. **IDE Integration**
```bash
# Open multiple worktrees in VS Code
code ~/project           # Main work
code ~/project-review    # PR review
code ~/project-hotfix    # Emergency fix

# Each has its own window, extensions work normally
```

### 3. **Automated Cleanup Script**
```bash
#!/bin/bash
# cleanup-merged-worktrees.sh

git worktree list | grep -v 'main\|master' | while read -r line; do
    path=$(echo $line | awk '{print $1}')
    branch=$(echo $line | grep -o '\[.*\]' | tr -d '[]')

    # Check if branch is merged
    if git branch --merged main | grep -q "$branch"; then
        echo "Removing merged worktree: $path ($branch)"
        git worktree remove "$path"
        git branch -d "$branch"
    fi
done
```

### 4. **Disk Space Management**
```bash
# Worktrees share .git objects, but check sizes
du -sh ../project*

# Clean up build artifacts in unused worktrees
find ../project-* -name "node_modules" -type d -exec rm -rf {} +
find ../project-* -name "dist" -type d -exec rm -rf {} +
```

## Verification Checklist

- [ ] Created at least 2 worktrees for different branches
- [ ] Made changes in multiple worktrees simultaneously
- [ ] Listed all worktrees with `git worktree list`
- [ ] Removed a worktree and pruned references
- [ ] Ran parallel builds/tests in different worktrees
- [ ] Understand shared vs separate git state
- [ ] Created script to automate worktree creation

## Time Savings

**Traditional Branch Switching:**
- Stash changes: 10s
- Switch branch: 5s
- Pop stash when returning: 10s
- **Total per switch: 25s**

**With Worktrees:**
- Switch directory: 1s
- **Total per switch: 1s**

**Daily savings:** 8-10 minutes on 20+ context switches

## Further Reading

- `git worktree --help`
- https://git-scm.com/docs/git-worktree
- Pro Git book: Chapter on Advanced Merging
