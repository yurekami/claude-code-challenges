# Walkthrough: Context Compaction

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** Context Management

---

## Overview

As conversations grow, your context window fills with outdated information. This challenge teaches you to proactively compact context before hitting token limits, maintaining conversation efficiency and quality.

## Prerequisites

- [ ] Understanding of token limits (~200k tokens)
- [ ] Completed basic CLI challenges
- [ ] Experience with longer Claude sessions

---

## Step 1: Recognize Warning Signs

### Context Bloat Indicators

| Sign | Token Range | Action Needed |
|------|-------------|---------------|
| Everything smooth | 0-50k | Continue normally |
| Slight slowdown | 50k-100k | Consider cleanup |
| Claude repeats itself | 100k-150k | Compact now |
| Truncation warnings | 150k-180k | Urgent compaction |
| Session failing | 180k+ | Start fresh |

### Check Current Usage
```
/usage
```

**Example Output:**
```
Context: 72,450 / 200,000 tokens (36%)
```

---

## Step 2: Identify What to Keep

Before compacting, categorize your context:

### Essential (KEEP)
- [ ] Current task objectives
- [ ] Recent key decisions and rationale
- [ ] Active code snippets being worked on
- [ ] Unresolved issues/bugs
- [ ] Important constraints discovered

### Optional (SUMMARIZE)
- [ ] Completed subtasks (just outcomes)
- [ ] Debugging sessions (just conclusions)
- [ ] Architecture discussions (just decisions)

### Noise (REMOVE)
- [ ] Failed attempts and dead ends
- [ ] Superseded code versions
- [ ] Repetitive explanations
- [ ] Off-topic tangents

---

## Step 3: Create a Compaction Summary

Ask Claude to help:

```
Create a concise summary of our session for context compaction:

1. What we set out to do
2. Key decisions made
3. What's completed
4. What's still in progress
5. Important code/config to preserve
6. Next immediate steps

Keep it under 2000 tokens.
```

**Example Output:**
```markdown
## Session Summary

### Objective
Implement JWT authentication for the REST API

### Key Decisions
- Using RS256 algorithm for tokens
- Access tokens expire in 15 minutes
- Refresh tokens expire in 7 days
- Storing refresh tokens in Redis

### Completed
✅ JWT utility functions (src/utils/jwt.ts)
✅ Auth middleware (src/middleware/auth.ts)
✅ Login endpoint (POST /api/auth/login)

### In Progress
🔄 Refresh token endpoint (50% done)

### Critical Code
```typescript
// Token signing config
const JWT_CONFIG = {
  algorithm: 'RS256',
  accessExpiresIn: '15m',
  refreshExpiresIn: '7d'
};
```

### Next Steps
1. Complete refresh endpoint
2. Add logout functionality
3. Write integration tests
```

---

## Step 4: Execute Compaction

### Option A: Clear and Resume
```
/clear
```
Then paste your summary:
```
Continuing from previous session:

[Paste summary here]

Let's continue with the refresh token endpoint.
```

### Option B: Start Fresh Session
```bash
# Exit current session
exit

# Start new session
claude
```

Then provide context:
```
I'm continuing work on JWT authentication. Here's where we left off:

[Paste summary]
```

---

## Step 5: Verify Successful Compaction

After resuming, test that Claude retained the essentials:

```
What authentication algorithm are we using and why?
```

**Expected:** Claude correctly recalls RS256 and the reasoning.

```
What's the current state of the refresh endpoint?
```

**Expected:** Claude knows it's 50% complete and what remains.

---

## Step 6: Establish Compaction Cadence

### Time-Based
- Every 2 hours of active work
- Before starting a major new subtask
- Before taking a break

### Token-Based
- At 50% usage: Consider compaction
- At 70% usage: Definitely compact
- At 80%+ usage: Compact immediately

### Event-Based
- After completing major milestones
- When switching contexts/files
- Before complex reasoning tasks

---

## Verification Checklist

- [ ] Can identify when context needs compaction (3+ signs)
- [ ] Created a concise summary (<2000 tokens)
- [ ] Successfully resumed work after compaction
- [ ] Maintained productivity across the transition
- [ ] No critical information was lost

---

## Compaction Templates

### Bug Fix Session
```markdown
## Bug Fix Summary

**Bug:** [Description]
**Root Cause:** [What we found]
**Fix Applied:** [Solution]
**Files Modified:** [List]
**Tests:** [Pass/Fail status]
**Remaining:** [Any follow-up]
```

### Feature Development
```markdown
## Feature Progress

**Feature:** [Name]
**Objective:** [Goal]
**Progress:** [X]%

**Completed:**
- [List items]

**In Progress:**
- [Current item]

**Key Code:**
```
[Critical snippets]
```

**Decisions:**
- [Important choices made]
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Lost critical detail | Always verify summary before clearing |
| Summary too long | Focus on decisions, not discussions |
| Repeated compaction | Set a schedule, don't compact too frequently |
| Wrong information restored | Be specific about what matters |

---

## Pro Tips

1. **Preemptive Summaries:** Create summaries every 30 minutes even if not compacting
2. **Version Your Summaries:** Save summaries to files for future reference
3. **Critical Code First:** Always include code snippets that are actively being modified
4. **Test After Compaction:** Verify Claude understands the context with quick questions

---

## Next Challenge

Continue to **[Handoff Documents](./02-handoff-documents.md)** for perfect session continuity!
