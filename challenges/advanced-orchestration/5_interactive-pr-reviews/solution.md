# Interactive PR Reviews Solution

## Step-by-Step Solution

### Task 1: Conduct a Comprehensive PR Review

**Step 1: Fetch PR with gh CLI**
```bash
# View PR details
gh pr view 123

# Get diff
gh pr diff 123

# List changed files
gh pr view 123 --json files --jq '.files[].path'
```

**Step 2: Start conversational review**
```
"I'm reviewing PR #123. Here's the diff:
[paste gh pr diff output]

Please review for:
1. Security issues
2. Performance concerns
3. Code quality and maintainability
4. Best practices adherence
5. Test coverage

Provide specific line-by-line feedback where needed."
```

**Step 3: Generate review comment**
```bash
# After Claude provides feedback, add comments
gh pr review 123 --comment -b "$(cat <<'EOF'
Thanks for this PR! Here are some thoughts:

**Security:**
- Line 45: User input should be validated before database query
- Line 78: Passwords should be hashed with bcrypt, not MD5

**Performance:**
- Line 120: This N+1 query could be optimized with a JOIN

**Code Quality:**
- Lines 200-250: This function is doing too much. Consider extracting helper functions.

Overall looking good! Please address the security concerns before merging.
EOF
)"
```

### Task 2: Security-Focused Review

**Step 1: Security checklist**
```
"Review this PR specifically for security issues:
[paste diff]

Check for:
- SQL injection vulnerabilities
- XSS vulnerabilities
- Exposed secrets or credentials
- Improper authentication/authorization
- Insecure dependencies
- Missing input validation
- Insecure file operations
- Missing rate limiting"
```

**Step 2: Deep dive on findings**
```
"You mentioned potential SQL injection at line 45. Can you:
1. Show exactly how this could be exploited
2. Provide the secure version of this code
3. Explain what makes the secure version safe"
```

**Step 3: Create security review template**
```bash
# Save as .github/pr-security-checklist.md
```markdown
## Security Review Checklist

### Input Validation
- [ ] All user inputs are validated
- [ ] Type checking is in place
- [ ] Length limits are enforced

### Authentication/Authorization
- [ ] Routes are properly protected
- [ ] Permission checks are correct
- [ ] Session management is secure

### Data Protection
- [ ] Passwords are hashed
- [ ] Sensitive data is encrypted
- [ ] No secrets in code

### Injection Prevention
- [ ] Parameterized queries used
- [ ] HTML is properly escaped
- [ ] Command injection prevented

### Dependencies
- [ ] No known vulnerabilities
- [ ] Versions are up to date
- [ ] Supply chain is secure
```
```

### Task 3: Performance Review

**Step 1: Performance analysis**
```
"Analyze this PR for performance issues:
[paste diff]

Focus on:
- Database query efficiency
- Loop optimizations
- Memory usage
- API call patterns
- Caching opportunities
- Algorithm complexity"
```

**Step 2: Request benchmarks**
```bash
# Ask in PR
gh pr comment 123 -b "Can you add benchmark results showing the performance impact of this change?"
```

**Step 3: Suggest optimizations**
```
"For the N+1 query issue you found, show me:
1. The current inefficient code
2. The optimized version
3. Expected performance improvement
4. Any trade-offs to consider"
```

### Task 4: Interactive Back-and-Forth

**Example Conversation Flow:**

**Initial Review:**
```bash
gh pr review 123 --comment
```
```
"I see you're refactoring the auth system. Can you explain the reasoning
behind moving from JWT to session-based auth? What problems does this solve?"
```

**Author Response:**
```
"We're seeing issues with JWT token size and revocation. Sessions give us
better control."
```

**Follow-up with Claude:**
```
"The author explained they're moving from JWT to sessions for better revocation.
Given this context, review the session implementation for:
1. Session storage security
2. CSRF protection
3. Session fixation prevention
4. Proper logout handling"
```

**Final Approval:**
```bash
gh pr review 123 --approve -b "LGTM! Session security looks solid. Thanks for addressing the feedback."
```

## Example Commands and Techniques

### Efficient gh CLI Usage

```bash
# View PR in browser
gh pr view 123 --web

# Check status
gh pr checks 123

# View specific file
gh pr diff 123 -- path/to/file.js

# List all comments
gh pr view 123 --json comments --jq '.comments[].body'

# Request changes
gh pr review 123 --request-changes -b "Please address security concerns"

# Approve
gh pr review 123 --approve -b "Great work!"
```

### Review Templates

**Comprehensive Template:**
```markdown
## Code Review: PR #{{number}}

### Summary
[Brief description of what was reviewed]

### Strengths ✅
- [What the PR does well]

### Security 🔒
- [ ] No security issues found
- [ ] Issues: [list any found]

### Performance ⚡
- [ ] No performance concerns
- [ ] Concerns: [list any found]

### Code Quality 📝
- [ ] Follows style guide
- [ ] Well-documented
- [ ] Properly tested
- [ ] Issues: [list any found]

### Suggestions 💡
1. [Suggestion 1]
2. [Suggestion 2]

### Questions ❓
1. [Question 1]
2. [Question 2]

### Verdict
- [ ] Approve
- [ ] Request Changes
- [ ] Comment Only
```

### Using Claude for Different Review Types

**Quick Review:**
```
"Quick review of this PR - any critical issues?
[paste small diff]"
```

**Deep Review:**
```
"Thorough review of this PR. Take your time and analyze:
- Architecture decisions
- Error handling patterns
- Edge cases
- Testing strategy
[paste larger diff]"
```

**Focused Review:**
```
"Review only the database migration files in this PR:
[paste migration diffs]

Check for:
- Data loss risks
- Rollback procedures
- Index impacts
- Performance during migration"
```

## Common Mistakes to Avoid

### 1. Surface-Level Reviews
**Wrong:**
"Looks good to me!"

**Right:**
Actually review the code with specific feedback on multiple aspects.

### 2. Too Much Context
**Wrong:**
Pasting entire codebase into Claude.

**Right:**
Paste only relevant diff and necessary context.

### 3. Unclear Feedback
**Wrong:**
"This could be better."

**Right:**
"Line 45: Extract this into a helper function for reusability. Example: ..."

### 4. Missing Follow-Up
**Wrong:**
Leaving comments without checking if they're addressed.

**Right:**
Track feedback and verify fixes before approving.

### 5. Not Being Constructive
**Wrong:**
"This code is terrible."

**Right:**
"This approach works but could be improved for maintainability. Consider..."

## Best Practices

### 1. Structured Review Process

```bash
#!/bin/bash
# pr-review.sh

PR_NUM=$1

echo "📥 Fetching PR #$PR_NUM..."
gh pr view $PR_NUM

echo "\n📝 Getting diff..."
DIFF=$(gh pr diff $PR_NUM)

echo "\n🤖 Starting Claude review..."
# Pass to Claude for analysis

echo "\n✅ Review complete!"
```

### 2. Review Checklist

```markdown
## Before Reviewing
- [ ] Understand the PR's purpose
- [ ] Check linked issues
- [ ] Review previous comments
- [ ] Check test results

## During Review
- [ ] Security analysis
- [ ] Performance check
- [ ] Code quality assessment
- [ ] Test coverage verification
- [ ] Documentation review

## After Review
- [ ] Provide actionable feedback
- [ ] Ask clarifying questions
- [ ] Suggest improvements
- [ ] Approve or request changes
```

### 3. Effective Communication

**Be Specific:**
```
❌ "This function is bad"
✅ "This function has high cyclomatic complexity (15). Consider extracting
    the validation logic into separate functions."
```

**Be Constructive:**
```
❌ "You don't know how to handle errors"
✅ "Consider wrapping this in try-catch. Here's an example:
    [code example]"
```

**Explain Why:**
```
❌ "Use const instead of let"
✅ "Use const instead of let here because the variable is never reassigned.
    This makes the code's intent clearer and prevents accidental mutations."
```

### 4. Collaborative Approach

```bash
# Engage in discussion
gh pr comment 123 -b "Interesting approach! Have you considered using [alternative]? It might provide better [benefit]."

# Offer to help
gh pr comment 123 -b "This is a complex refactoring. Happy to pair on this if you'd like a second set of eyes."

# Acknowledge good work
gh pr comment 123 -b "Nice work on the test coverage! The edge cases you've covered are exactly what we need."
```

### 5. Automation Opportunities

```bash
# Auto-review script
#!/bin/bash
# auto-review.sh

PR_NUM=$1
REVIEW_TYPE=${2:-comprehensive}

# Fetch PR
DIFF=$(gh pr diff $PR_NUM)
FILES=$(gh pr view $PR_NUM --json files --jq '.files[].path')

# Generate review based on type
case $REVIEW_TYPE in
  security)
    echo "🔒 Security Review for PR #$PR_NUM"
    # Focus on security
    ;;
  performance)
    echo "⚡ Performance Review for PR #$PR_NUM"
    # Focus on performance
    ;;
  *)
    echo "📋 Comprehensive Review for PR #$PR_NUM"
    # Full review
    ;;
esac
```

## Advanced Techniques

### Multi-Person Review Coordination

```bash
# Check who else has reviewed
gh pr view 123 --json reviews

# Add review building on others' feedback
gh pr review 123 --comment -b "Adding to @reviewer's security concerns: [additional points]"
```

### Review Analytics

```bash
# Track review patterns
#!/bin/bash
# review-stats.sh

echo "Review Statistics:"
echo "Total PRs reviewed: $(gh pr list --state merged --json number | jq 'length')"
echo "Average review time: ..."
echo "Common issues found: ..."
```

### Integration with CI/CD

```yaml
# .github/workflows/ai-review.yml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Get PR diff
        id: diff
        run: |
          gh pr diff ${{ github.event.pull_request.number }} > diff.txt
      - name: AI Review
        run: |
          # Send to Claude for analysis
          # Post results as comment
```

## Success Indicators

You've mastered this challenge when you can:
- Efficiently review PRs using gh CLI and Claude
- Identify issues across security, performance, and quality
- Provide constructive, actionable feedback
- Engage in productive back-and-forth discussions
- Help improve code through thoughtful reviews
- Automate repetitive review tasks
- Maintain consistent review quality
