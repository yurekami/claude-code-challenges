# Git and GitHub CLI Integration

**Related Tip:** Tip 4: Git and GitHub CLI delegation

## Description

Claude Code has powerful Git integration. You can delegate Git operations and GitHub management directly to Claude, who will use git commands and GitHub CLI (gh) to handle branches, commits, pull requests, issues, and more. This eliminates context switching and keeps you in flow.

## Objective

Master delegating Git and GitHub operations to Claude Code, enabling seamless version control and collaboration workflows without leaving your conversation.

## Prerequisites

- Git installed and configured
- GitHub CLI (gh) installed and authenticated
- A GitHub repository to practice with

## What Claude Can Do

### Git Operations
- Create branches
- Stage and commit changes
- View diffs and status
- Merge branches
- Rebase commits
- View commit history
- Create tags

### GitHub Operations
- Create and list pull requests
- Create and manage issues
- View PR status and checks
- Review pull requests
- Merge pull requests
- Fork repositories
- Manage releases

## Steps to Complete

1. Install and authenticate GitHub CLI
2. Practice basic Git delegation (branch, commit)
3. Create a pull request through Claude
4. Manage GitHub issues via delegation
5. Review PR workflow with Claude
6. Understand when to delegate vs when to do manually

## Success Criteria

- [ ] GitHub CLI installed and authenticated
- [ ] Can delegate branch creation to Claude
- [ ] Can ask Claude to commit changes with good messages
- [ ] Can create pull requests through conversation
- [ ] Can manage issues via Claude
- [ ] Know the limitations of delegation
- [ ] Understand Git/GitHub best practices for AI collaboration

## Why This Matters

Git delegation enables:
- **Flow state**: Stay in conversation, no context switching
- **Better commit messages**: Claude writes descriptive messages
- **Automated PR creation**: Comprehensive PR descriptions
- **Issue management**: Create/update issues conversationally
- **Code review**: Claude can analyze diffs and review changes

## Challenge Tasks

1. **Setup**: Install gh CLI and authenticate
2. **Branch workflow**: Ask Claude to create a feature branch
3. **Commit**: Have Claude commit your changes with a good message
4. **Pull request**: Ask Claude to create a PR with proper description
5. **Issue creation**: Have Claude create an issue for a bug or feature
6. **PR review**: Ask Claude to review a pull request and provide feedback

## Bonus Challenges

1. **Complex workflow**: Feature branch → commits → PR → review → merge (all via delegation)
2. **Issue-driven development**: Create issue → create branch → implement → PR → link issue
3. **Release management**: Ask Claude to create a release with changelog

## Common Use Cases

### Use Case 1: Feature Development
```
"Create a new branch called feature/user-authentication.
Implement basic login functionality.
When done, commit the changes and create a PR."
```

### Use Case 2: Bug Fix
```
"I found a bug in the payment processing.
Create a branch, fix the issue,
commit with a proper message,
and create a PR linking to issue #42."
```

### Use Case 3: Code Review
```
"Review the latest PR on the main branch.
Check for security issues, code quality,
and adherence to our coding standards."
```
