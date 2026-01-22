# Walkthrough: Interactive PR Reviews

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** Advanced Orchestration

---

## Overview

Code reviews are conversations, not just approvals. This challenge teaches you to have interactive, productive PR discussions with Claude - asking questions, discussing tradeoffs, and improving code together.

## Prerequisites

- [ ] Pull request to review
- [ ] Understanding of the codebase
- [ ] GitHub CLI installed (gh)

---

## Step 1: Fetch PR Context

### Get PR Information
```bash
# View PR details
gh pr view 123

# Get changed files
gh pr view 123 --json files

# Get the diff
gh pr diff 123
```

### Ask Claude to Review
```
Review this pull request:

gh pr view 123

Show me:
1. Summary of changes
2. Potential issues
3. Questions I should ask the author
```

---

## Step 2: Interactive Review Flow

### Start Broad
```
What is this PR trying to accomplish?
Is the approach reasonable?
```

### Zoom Into Details
```
I'm concerned about the change to auth.ts.
What are the implications of removing this check?
```

### Discuss Tradeoffs
```
The author used Strategy pattern here.
Is this over-engineering, or appropriate for this case?
```

---

## Step 3: Ask Better Questions

### Instead of Just Flagging Issues
```
❌ "This is wrong"
✅ "I see you're doing X. Did you consider Y?
   What's the tradeoff you're making here?"
```

### Understand Intent
```
"What problem were you solving with this change?"
"Why did you choose this approach over [alternative]?"
"Is there a reason this isn't using [existing pattern]?"
```

---

## Step 4: Review Categories

### Architecture Review
```
Look at the overall architecture of these changes:
- Does this fit our existing patterns?
- Are there any abstraction level issues?
- Is the coupling appropriate?
```

### Security Review
```
Check for security issues:
- Input validation
- Authentication/authorization
- Sensitive data handling
- SQL/XSS injection vectors
```

### Performance Review
```
Analyze performance implications:
- Any N+1 queries?
- Unnecessary iterations?
- Memory concerns?
- Caching opportunities?
```

### Maintainability Review
```
Evaluate maintainability:
- Will future developers understand this?
- Is there adequate error handling?
- Are there tests for new behavior?
- Is the code self-documenting?
```

---

## Step 5: Discussion Templates

### Requesting Clarification
```markdown
## Question on line 45

I see you're creating a new instance inside the loop:

```typescript
for (const item of items) {
  const processor = new Processor(); // Here
}
```

Was this intentional? I'd expect the processor to be reusable.
Could you help me understand the design decision?
```

### Suggesting Alternatives
```markdown
## Alternative Approach

Current:
```typescript
if (type === 'a') { ... }
else if (type === 'b') { ... }
else if (type === 'c') { ... }
```

Have you considered using a strategy map?
```typescript
const handlers = { a: handleA, b: handleB, c: handleC };
handlers[type]?.();
```

This might be easier to extend. Thoughts?
```

---

## Step 6: Collaborative Problem Solving

### When You Find an Issue
```
I found a potential race condition in the caching logic.

Let's think through solutions:
1. What happens if two requests hit simultaneously?
2. What locking mechanism would be appropriate?
3. How would this affect performance?
```

### When You're Unsure
```
I'm not sure if this is actually a problem:
[describe concern]

Help me think through:
1. When would this fail?
2. Is this scenario realistic?
3. Is the fix worth the complexity?
```

---

## Step 7: Complete Review Workflow

### Full PR Review Prompt
```
I need to review PR #123. Let's do this systematically:

1. First, summarize what this PR does
2. List the files changed and categorize changes
3. For each significant change, analyze:
   - What it does
   - Potential issues
   - Questions for author
4. Security quick-check
5. Test coverage assessment
6. Suggest my review verdict (approve/request changes/comment)
```

---

## Verification Checklist

- [ ] Fetched PR diff and context
- [ ] Got summary of changes from Claude
- [ ] Asked probing questions about implementation
- [ ] Discussed at least one tradeoff
- [ ] Formulated constructive feedback

---

## Review Communication

| Tone | Example |
|------|---------|
| Curious | "I'm wondering why you chose..." |
| Collaborative | "What if we tried..." |
| Constructive | "This could be improved by..." |
| Appreciative | "Nice handling of..." |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Nitpicking too much | Focus on significant issues |
| Missing the big picture | Start with architecture review |
| Being too harsh | Frame as questions, not criticisms |
| Rubber stamping | Take time, be thorough |

---

## Pro Tips

1. **Understand First:** Ask about intent before critiquing
2. **Be Specific:** Point to exact lines and explain why
3. **Offer Solutions:** Don't just identify problems
4. **Praise Good Work:** Acknowledge improvements

---

## Next Challenge

Continue to **[Research Tool](./06-research-tool.md)** for deep dives into any topic!
