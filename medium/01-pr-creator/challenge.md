# Challenge: PR Creator

**Difficulty:** Medium
**Category:** Git Mastery
**Points:** 150
**Time Limit:** 15 minutes

## Description

Create a complete pull request workflow using Claude Code and the GitHub CLI (`gh`). This challenge tests your ability to manage branches, commits, and PR creation with proper descriptions.

## Objectives

1. Create a new feature branch from `main`
2. Make code changes and commit them properly
3. Push the branch to the remote
4. Create a PR with a comprehensive description
5. Include test plan and summary

## PR Description Format

```markdown
## Summary
- [1-3 bullet points describing the change]

## Changes
- [List specific code changes]

## Test Plan
- [ ] [Test case 1]
- [ ] [Test case 2]

## Screenshots (if applicable)
[Screenshots here]

---
Generated with Claude Code
```

## Constraints

- Use `gh` CLI for PR creation (not GitHub web UI)
- Branch name must follow: `feat/description` or `fix/description`
- All commits must follow conventional commit format
- PR title must be descriptive (not just "Update")
- Must push with `-u` flag for new branches

## Input

The `starter/` directory is a git repository connected to a GitHub remote with an existing `main` branch.

## Task

Implement a new feature: Add a `validateEmail` function to `src/utils/validation.ts`

The function should:
- Take an email string as input
- Return `true` for valid emails, `false` otherwise
- Use a reasonable regex pattern

## Expected Output

1. A new branch `feat/email-validation`
2. A commit with message like `feat(validation): add email validation function`
3. A PR created via `gh pr create`
4. PR description following the format above

## Example Commands

### Creating Branch
```bash
git checkout -b feat/email-validation
```

### Creating PR with gh
```bash
gh pr create --title "feat: Add email validation" --body "$(cat <<'EOF'
## Summary
- Add validateEmail function to validation utilities

## Test Plan
- [ ] Test valid emails
- [ ] Test invalid emails
EOF
)"
```

## Scoring

| Criteria | Points |
|----------|--------|
| Correct branch naming | 20 |
| Valid conventional commit | 25 |
| Function implemented correctly | 30 |
| PR created with gh CLI | 25 |
| PR description complete | 25 |
| Push with -u flag | 25 |

## Hints

1. Use `git checkout -b` to create and switch to a new branch
2. Use `git push -u origin branch-name` for new branches
3. Use HEREDOC for multi-line PR body in `gh pr create`
4. Check `gh pr view` to verify your PR

## Verification

Run `python tests.py` to check your workflow.
