# Walkthrough: Skill Creation

**Difficulty:** Hard | **Time:** 25 minutes | **Category:** MCP Integrations

---

## Overview

Skills are reusable prompt templates that encode best practices and workflows. This challenge teaches you to create, test, and refine custom skills for your specific needs.

## Prerequisites

- [ ] Understanding of skills vs commands
- [ ] Markdown knowledge
- [ ] Clear workflow to encode

---

## Step 1: Skill Anatomy

### Basic Skill Structure
```markdown
# Skill Name

[Description of what the skill does]

## When to Use
[Triggers and use cases]

## Steps
1. [Step one]
2. [Step two]
3. [Step three]

## Output Format
[Expected output structure]
```

---

## Step 2: Plan Your Skill

### Skill Planning Template
```
Skill Name: ________________

Problem it solves:
[What pain point does this address?]

Trigger phrases:
- "[phrase 1]"
- "[phrase 2]"

Steps involved:
1. [Step]
2. [Step]
3. [Step]

Success criteria:
- [Criterion 1]
- [Criterion 2]
```

---

## Step 3: Create Your First Skill

### Example: Code Review Skill

**File:** `~/.claude/skills/code-review.md`

```markdown
# Code Review Skill

Perform a thorough code review following best practices.

## Trigger
Invoke with `/code-review` or when asked to "review this code"

## Process

### Phase 1: Understanding
- Read the code completely before commenting
- Understand the purpose and context
- Identify the scope of changes

### Phase 2: Analysis
Check for:

**Correctness**
- [ ] Logic is sound
- [ ] Edge cases handled
- [ ] No obvious bugs

**Security**
- [ ] Input validation
- [ ] No injection vulnerabilities
- [ ] Sensitive data protected

**Performance**
- [ ] No obvious inefficiencies
- [ ] Appropriate data structures
- [ ] No N+1 queries

**Maintainability**
- [ ] Code is readable
- [ ] Functions are focused
- [ ] Naming is clear

**Testing**
- [ ] Tests exist for new code
- [ ] Edge cases tested
- [ ] Tests are meaningful

### Phase 3: Feedback

Categorize findings:
- 🔴 **Critical**: Must fix before merge
- 🟡 **Important**: Should fix
- 🟢 **Suggestion**: Nice to have
- 💡 **Question**: Need clarification

## Output Format

```markdown
## Code Review Summary

### Overview
[Brief description of what was reviewed]

### Findings

#### Critical Issues
[List or "None found"]

#### Important Issues
[List or "None found"]

#### Suggestions
[List or "None found"]

### Questions
[List or "None"]

### Recommendation
[ ] Approve
[ ] Approve with minor changes
[ ] Request changes
```
```

---

## Step 4: Advanced Skill Patterns

### Pattern 1: Multi-Phase Skill
```markdown
# Feature Implementation Skill

## Phase 1: Planning
- Understand requirements
- Identify dependencies
- Create implementation plan

## Phase 2: Implementation
- Write tests first
- Implement in small increments
- Commit frequently

## Phase 3: Review
- Self-review changes
- Run tests
- Update documentation
```

### Pattern 2: Checklist Skill
```markdown
# Pre-Commit Checklist Skill

Before committing, verify:

## Code Quality
- [ ] No console.log statements
- [ ] No commented-out code
- [ ] No TODO comments without tickets

## Testing
- [ ] All tests pass
- [ ] New code has tests
- [ ] Coverage maintained

## Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL injection prevented

## Documentation
- [ ] README updated if needed
- [ ] API docs updated if needed
- [ ] Comments for complex logic
```

### Pattern 3: Conversation Skill
```markdown
# Requirements Gathering Skill

Gather requirements through conversation.

## Questions to Ask

1. **Purpose**: What problem are we solving?
2. **Users**: Who will use this?
3. **Scope**: What's in and out of scope?
4. **Constraints**: Technical or business limitations?
5. **Success**: How do we measure success?
6. **Timeline**: Any deadlines?

## After Gathering

Produce a requirements document:
- Summary
- User stories
- Acceptance criteria
- Out of scope items
```

---

## Step 5: Test Your Skill

### Invoke and Verify
```
/code-review
```

### Check Output Quality
- Does it follow the defined format?
- Are all phases covered?
- Is the output useful?

### Iterate
Refine based on results:
```markdown
# Updated Skill

[Add what was missing]
[Remove what wasn't useful]
[Clarify confusing parts]
```

---

## Step 6: Skill Library Organization

### Directory Structure
```
~/.claude/skills/
├── development/
│   ├── code-review.md
│   ├── feature-impl.md
│   └── bug-fix.md
├── git/
│   ├── commit.md
│   ├── pr-create.md
│   └── branch-cleanup.md
└── documentation/
    ├── api-docs.md
    └── readme-update.md
```

---

## Verification Checklist

- [ ] Created at least 2 custom skills
- [ ] Skills follow the structure template
- [ ] Tested skills produce useful output
- [ ] Organized skills into directories
- [ ] Shared a skill with team (optional)

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Skill too vague | Add specific steps and examples |
| Skill too rigid | Allow for context adaptation |
| Output inconsistent | Define clear output format |
| Skill not triggering | Check file location and naming |

---

## Pro Tips

1. **Start Small:** Begin with simple skills, add complexity
2. **Real Workflows:** Encode actual processes you repeat
3. **Examples Help:** Include example outputs in skills
4. **Version Control:** Track skill changes in Git

---

## Next Challenge

Continue to **[Notion Integration](./06-notion-integration.md)** to preserve links when pasting!
