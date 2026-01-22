# Git Worktrees for Parallel Development - Medium

**Related Tip:** #16 - Use git worktrees for parallel branch work

## Description

Master git worktrees to work on multiple branches simultaneously without the context-switching overhead of stashing, committing, or switching branches. This enables true parallel development workflows.

## Objective

Set up and use git worktrees to:
1. Work on a feature branch and a bugfix simultaneously
2. Run tests on one branch while developing on another
3. Compare implementations across branches
4. Manage multiple CI/CD pipelines in parallel

## Background

Traditional git workflow requires switching branches:
```bash
git checkout feature-branch
# make changes
git stash
git checkout bugfix-branch
# fix bug
git checkout feature-branch
git stash pop
```

Worktrees allow each branch to exist in a separate directory simultaneously.

## Steps to Complete

1. **Create Main Worktree Structure**
   - Set up a main repository
   - Create 2-3 worktrees for different branches
   - Understand worktree directory organization

2. **Parallel Development Workflow**
   - Make changes in one worktree
   - Switch to another worktree (different directory)
   - Run builds/tests in parallel
   - Compare code across worktrees

3. **Cleanup and Maintenance**
   - Remove worktrees when branches are merged
   - Understand shared git objects
   - Manage disk space efficiently

4. **Integration with Claude Code**
   - Use Claude Code in different worktrees
   - Leverage parallel terminal tabs (from Challenge 1)
   - Automate worktree creation

## Success Criteria

- [ ] Create at least 2 worktrees for different branches
- [ ] Make simultaneous changes in separate worktrees
- [ ] Run parallel builds/tests in different worktrees
- [ ] Successfully merge work from both branches
- [ ] Clean up worktrees after branch merges
- [ ] Demonstrate time savings vs traditional branch switching

## Real-World Application

- Emergency hotfix while working on a feature
- Testing performance improvements on separate branch
- Reviewing pull requests without losing work-in-progress
- Running long CI builds on one branch while continuing development

## Time Estimate

25-35 minutes

## Prerequisites

- Basic git knowledge
- Understanding of branches and commits
- Completed Challenge 1 (Terminal Cascade) recommended
