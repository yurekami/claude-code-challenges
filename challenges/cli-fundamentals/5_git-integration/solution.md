# Solution: Git and GitHub CLI Integration

## Setup: GitHub CLI Installation

### Install GitHub CLI

**macOS**:
```bash
brew install gh
```

**Windows**:
```bash
# Using winget
winget install --id GitHub.cli

# Or using scoop
scoop install gh

# Or download from https://cli.github.com
```

**Linux (Debian/Ubuntu)**:
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### Authenticate GitHub CLI

```bash
gh auth login

# Follow the prompts:
# 1. Choose GitHub.com
# 2. Choose HTTPS or SSH
# 3. Authenticate via browser or token
# 4. Grant permissions

# Verify authentication
gh auth status
```

## Git Delegation Patterns

### Pattern 1: Branch Creation

**Instead of manually**:
```bash
git checkout -b feature/new-feature
```

**Delegate to Claude**:
```
"Create a new branch called feature/user-authentication"
```

**Claude will execute**:
```bash
git checkout -b feature/user-authentication
```

### Pattern 2: Viewing Changes

**Instead of manually**:
```bash
git status
git diff
```

**Delegate to Claude**:
```
"Show me what files have changed and the diff"
```

**Claude will execute**:
```bash
git status
git diff
```

### Pattern 3: Committing Changes

**Instead of manually**:
```bash
git add .
git commit -m "Add user authentication"
```

**Delegate to Claude**:
```
"Commit these changes with an appropriate message"
```

**Claude will**:
1. Review the changes with `git diff`
2. Craft a descriptive commit message
3. Execute commit with proper attribution

Example commit message Claude might generate:
```
feat: Add user authentication system

- Implement JWT-based authentication
- Add login and registration endpoints
- Create auth middleware for protected routes
- Add password hashing with bcrypt

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### Pattern 4: Pull Request Creation

**Instead of manually**:
```bash
git push origin feature-branch
gh pr create --title "..." --body "..."
```

**Delegate to Claude**:
```
"Create a pull request for this feature"
```

**Claude will**:
1. Analyze all commits in the branch
2. Review the code changes
3. Generate comprehensive PR description
4. Create the PR using gh CLI

Example PR description Claude might generate:
```markdown
## Summary
Implements user authentication system using JWT tokens.

## Changes
- Added User model with email/password fields
- Created auth endpoints (login, register, logout)
- Implemented JWT token generation and validation
- Added auth middleware for protected routes
- Included password hashing with bcrypt

## Testing
- All unit tests pass
- Integration tests added for auth flow
- Manual testing completed

## Security Considerations
- Passwords hashed with bcrypt (cost factor: 12)
- JWT tokens expire after 1 hour
- Refresh tokens implemented
- Rate limiting on auth endpoints

🤖 Generated with Claude Code
```

## GitHub Operations Through Claude

### Create an Issue

**Conversation**:
```
"Create a GitHub issue for adding rate limiting to the API.
It should be a high priority feature request."
```

**Claude executes**:
```bash
gh issue create \
  --title "Add rate limiting to API endpoints" \
  --body "## Description
We need to implement rate limiting to prevent abuse.

## Requirements
- 100 requests per minute per API key
- 1000 requests per hour per IP
- Return 429 status when limit exceeded
- Include rate limit headers in responses

## Priority
High" \
  --label "enhancement,high-priority"
```

### List Pull Requests

**Conversation**:
```
"Show me all open pull requests"
```

**Claude executes**:
```bash
gh pr list --state open
```

### Review a Pull Request

**Conversation**:
```
"Review PR #42 and check for security issues"
```

**Claude will**:
1. Fetch PR details: `gh pr view 42`
2. Get the diff: `gh pr diff 42`
3. Analyze the code
4. Provide review comments

### Merge a Pull Request

**Conversation**:
```
"If the tests pass, merge PR #42 using squash merge"
```

**Claude will**:
1. Check PR status: `gh pr checks 42`
2. Verify tests passed
3. Merge: `gh pr merge 42 --squash`

## Complete Workflow Examples

### Example 1: Feature Development

```bash
# Start Claude Code
claude

# Conversation:
You: "I need to add a search feature to the blog.
      Create a branch and let's implement it."

Claude: [Creates branch feature/blog-search]

You: "Implement full-text search for blog posts using the title and content"

Claude: [Implements search functionality]

You: "That looks good. Commit these changes and create a PR."

Claude: [Reviews changes, creates descriptive commit, pushes, creates PR]

You: "Great! Can you also create an issue for adding search filters?"

Claude: [Creates GitHub issue with details]
```

### Example 2: Bug Fix Workflow

```bash
claude

You: "There's a bug in the authentication middleware.
      It's not checking token expiration properly.
      This is issue #127."

Claude: "I'll fix this. Creating a branch fix/auth-token-expiration"
        [Creates branch]

You: "Fix the token expiration check in middleware/auth.ts"

Claude: [Analyzes code, implements fix]

You: "Test this fix"

Claude: [Runs tests, verifies fix]

You: "Commit and create a PR that closes issue #127"

Claude: [Creates commit with proper message, creates PR with "Closes #127"]
```

### Example 3: Code Review

```bash
claude

You: "Review the PR for the new payment integration (PR #89).
      Focus on security and error handling."

Claude: [Fetches PR, analyzes code]
        "I've reviewed PR #89. Here are my findings:

        CRITICAL:
        - Line 45: API key is logged in plain text
        - Line 67: No error handling for network failures

        HIGH:
        - Line 23: Should validate payment amount is positive
        - Line 89: Missing transaction ID in error responses

        MEDIUM:
        - Consider adding retry logic for failed payments
        - Add more descriptive error messages

        Recommendation: Request changes before merging."

You: "Post these as review comments on the PR"

Claude: [Uses gh pr review to post comments]
```

## Best Practices for Git Delegation

### 1. Clear Instructions

❌ **Vague**:
```
"Do some Git stuff"
```

✓ **Clear**:
```
"Create a new branch called feature/email-notifications,
implement the feature, then commit and create a PR"
```

### 2. Provide Context

❌ **No context**:
```
"Create a PR"
```

✓ **With context**:
```
"Create a PR for the authentication feature.
This closes issue #45 and includes JWT implementation,
password hashing, and rate limiting."
```

### 3. Review Before Push

❌ **Blind push**:
```
"Commit everything and push"
```

✓ **Review first**:
```
"Show me the diff, then commit with an appropriate message"
```

### 4. Use Semantic Commit Messages

Claude will use conventional commits by default:
- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code refactoring
- `docs:` - Documentation
- `test:` - Tests
- `chore:` - Maintenance

### 5. Link Issues and PRs

✓ **Always link related issues**:
```
"Create a PR that closes issue #42"
```

Claude will include "Closes #42" in the PR description.

## Advanced Techniques

### Technique 1: Branch Management

```
"Show me all branches and delete any that are merged"

Claude executes:
git branch -a
gh pr list --state merged
git branch -d [merged-branches]
```

### Technique 2: Cherry-Picking

```
"Cherry-pick commit abc123 from main into this branch"

Claude executes:
git cherry-pick abc123
```

### Technique 3: Interactive Rebase Guidance

```
"I need to squash the last 3 commits. Guide me through it."

Claude:
1. Shows you: git log --oneline -5
2. Explains: "Run git rebase -i HEAD~3"
3. Guides: "Change 'pick' to 'squash' for last 2 commits"
4. Helps: Write combined commit message
```

### Technique 4: Release Management

```
"Create a new release v2.0.0 with a changelog"

Claude:
1. Gets commits since last release
2. Generates changelog
3. Creates tag: git tag -a v2.0.0
4. Pushes: git push origin v2.0.0
5. Creates release: gh release create v2.0.0
```

## Limitations and Manual Operations

### When to Do It Yourself

1. **Complex interactive rebases**: Git's interactive mode isn't scriptable
2. **Merge conflicts**: May need manual resolution
3. **Sensitive operations**: Force pushes, history rewrites
4. **Fine-grained control**: When you need precise commit granularity

### When Claude Excels

1. **Routine operations**: Branch creation, commits, pushes
2. **PR creation**: Generates comprehensive descriptions
3. **Code review**: Analyzes diffs for issues
4. **Issue management**: Creates well-structured issues
5. **Commit messages**: Writes descriptive, conventional messages

## Troubleshooting

### Issue 1: gh CLI Not Authenticated

**Error**: `gh: not authenticated`

**Solution**:
```bash
gh auth login
gh auth status
```

### Issue 2: Permission Denied

**Error**: `Permission denied (publickey)`

**Solution**:
```bash
# Check SSH keys
gh ssh-key list

# Add SSH key if needed
gh ssh-key add ~/.ssh/id_ed25519.pub
```

### Issue 3: Branch Already Exists

**Error**: `fatal: A branch named 'feature/x' already exists`

**Solution**:
```
"Switch to the existing feature/x branch"

Claude: git checkout feature/x
```

### Issue 4: Merge Conflicts

**Error**: `Automatic merge failed; fix conflicts and then commit`

**Solution**:
```
"Show me the merge conflicts"

Claude: git status

You manually resolve conflicts, then:
"Commit the merge resolution"
```

## Quick Reference

### Git Operations Claude Can Do

```bash
# Branches
"Create branch feature/x"         → git checkout -b feature/x
"Switch to main"                   → git checkout main
"List all branches"                → git branch -a
"Delete branch feature/x"          → git branch -d feature/x

# Viewing
"Show status"                      → git status
"Show diff"                        → git diff
"Show commit history"              → git log
"Show branches"                    → git branch -v

# Committing
"Commit changes"                   → git add . && git commit
"Amend last commit"                → git commit --amend

# Remote operations
"Push to origin"                   → git push origin [branch]
"Pull latest"                      → git pull origin [branch]
"Fetch all"                        → git fetch --all
```

### GitHub Operations Claude Can Do

```bash
# Pull Requests
"Create PR"                        → gh pr create
"List PRs"                         → gh pr list
"View PR #42"                      → gh pr view 42
"Merge PR #42"                     → gh pr merge 42
"Close PR #42"                     → gh pr close 42

# Issues
"Create issue"                     → gh issue create
"List issues"                      → gh issue list
"View issue #42"                   → gh issue view 42
"Close issue #42"                  → gh issue close 42

# Repositories
"Fork repo"                        → gh repo fork
"Clone repo"                       → gh repo clone
"View repo"                        → gh repo view

# Releases
"Create release"                   → gh release create
"List releases"                    → gh release list
```

## Success Indicators

You've mastered Git/GitHub delegation when you:

- Never manually type git commands during Claude sessions
- Create PRs through conversation, not gh CLI
- Get comprehensive PR descriptions automatically
- Manage issues conversationally
- Trust Claude's commit messages
- Know when to delegate vs when to do manually
- Use GitHub CLI features you didn't know existed
- Maintain flow state during development

## Final Tips

1. **Trust but verify**: Review changes before committing
2. **Be specific**: Clear instructions = better results
3. **Provide context**: Help Claude write better messages
4. **Use issues**: Link PRs to issues for traceability
5. **Review PRs**: Have Claude review code before merging
6. **Stay in flow**: Let Claude handle Git operations
7. **Learn gh CLI**: Understanding what Claude can do helps you delegate better
