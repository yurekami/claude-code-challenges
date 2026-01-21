# Challenge: Quick Commit

**Difficulty:** Easy
**Category:** Git Mastery
**Points:** 100
**Time Limit:** 5 minutes

## Description

You have made changes to a codebase and need to create a proper git commit following conventional commit standards. Claude Code excels at analyzing changes and crafting appropriate commit messages.

## Objectives

1. Stage the modified files
2. Analyze the changes to understand what was modified
3. Create a commit with a properly formatted conventional commit message
4. The commit message should accurately describe the changes

## Conventional Commit Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:** feat, fix, docs, style, refactor, test, chore, perf, ci

## Constraints

- Commit message must follow conventional commit format
- Do NOT use `--amend` flag
- Do NOT use `-m` with placeholder text
- The commit description must be accurate to the actual changes
- Include `Co-Authored-By: Claude <noreply@anthropic.com>` footer

## Input

The `starter/` directory is a git repository with uncommitted changes.

## Expected Output

A git commit with:
- Correct type (feat, fix, etc.)
- Appropriate scope (if applicable)
- Descriptive message under 72 characters
- Co-authored-by footer

## Examples

### Good Commit Message
```
feat(auth): add password reset functionality

Implement forgot password flow with email verification.
Users can now reset their password via email link.

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Bad Commit Messages
```
update files              # Too vague
fix: stuff                # Not descriptive
FEAT: ADD FEATURE         # Wrong case
```

## Scoring

| Criteria | Points |
|----------|--------|
| Correct commit type | 25 |
| Proper format (scope optional) | 25 |
| Accurate description | 25 |
| Co-authored-by footer | 25 |

## Hints

1. Use `git diff` to see what changed
2. Use `git status` to see which files are modified
3. Analyze the nature of changes (new feature? bug fix? refactor?)
4. Keep the subject line under 72 characters

## Verification

Run `python tests.py` to check your commit.
