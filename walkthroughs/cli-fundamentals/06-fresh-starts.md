# Walkthrough: Fresh Starts

**Difficulty:** Easy | **Time:** 8 minutes | **Category:** CLI Fundamentals

---

## Overview

Knowing when to start fresh is as important as knowing how to continue. Long conversations accumulate noise, outdated context, and can lead Claude astray. This challenge teaches you to recognize when a fresh start will be more productive.

## Prerequisites

- [ ] Experience with multi-turn Claude conversations
- [ ] Completed context management basics
- [ ] Understanding of token usage

---

## Step 1: Recognize the Warning Signs

**Start fresh when you notice:**

| Sign | What's Happening |
|------|------------------|
| Claude repeats itself | Context is polluted with old info |
| Responses get slower | Approaching token limits |
| Claude forgets recent context | Earlier context being truncated |
| Suggestions contradict earlier decisions | Conflicting information in context |
| You're on a completely different task | Old context is now noise |

---

## Step 2: The Fresh Start Decision Tree

```
┌─────────────────────────────────────┐
│     Should I Start Fresh?           │
└────────────────┬────────────────────┘
                 │
       ┌─────────▼─────────┐
       │ Token usage > 50%? │
       └─────────┬─────────┘
            YES  │  NO
       ┌─────────▼──────┐   │
       │ Same task as   │   │
       │ when started?  │   │
       └────────────────┘   │
            NO   │  YES     │
                 │          │
    ┌────────────▼────┐     │
    │  START FRESH    │     │
    └─────────────────┘     │
                            │
              ┌─────────────▼─────────────┐
              │ Getting confused responses?│
              └─────────────┬─────────────┘
                       YES  │  NO
              ┌─────────────▼──────┐      │
              │    START FRESH     │      │
              └────────────────────┘      │
                                          │
                            ┌─────────────▼───┐
                            │    CONTINUE     │
                            └─────────────────┘
```

---

## Step 3: The Clean Exit

Before starting fresh, preserve important context:

### Option A: Quick Summary
```
Summarize our progress so far in a format I can paste into a new session
```

**Claude provides:**
```
## Session Summary

### Completed:
- Implemented user authentication API
- Added JWT token validation
- Created login/logout endpoints

### In Progress:
- Password reset flow (50% done)

### Key Decisions:
- Using bcrypt for password hashing
- Tokens expire after 24 hours
- Refresh tokens stored in httpOnly cookies

### Files Modified:
- src/auth/jwt.ts
- src/routes/auth.ts
- src/middleware/auth.ts
```

### Option B: Handoff Document
```
Create a handoff document for the next session
```

---

## Step 4: Execute the Fresh Start

### Method 1: New Terminal Session
```bash
# Close current session
exit

# Start fresh
claude
```

### Method 2: Reset Command
```
/reset
```

### Method 3: Clear and Continue
```
/clear
```
Then paste your summary.

---

## Step 5: Resume Productively

Start the new session with context:

```
I'm continuing work on user authentication. Here's where we left off:

[Paste summary from previous session]

Let's continue with the password reset flow.
```

**Pro Tip:** Be specific about what's next - don't make Claude re-discover the task.

---

## Verification Checklist

- [ ] Identified at least 3 warning signs for needing a fresh start
- [ ] Created a session summary before ending
- [ ] Successfully started a new session
- [ ] Resumed work with preserved context
- [ ] Understand difference between `/clear` and `/reset`

---

## When to Use Each Option

| Situation | Action |
|-----------|--------|
| Quick cleanup, same task | `/clear` |
| Major topic switch | `/reset` or new session |
| End of work session | Exit and summarize |
| Claude is very confused | `/reset` + fresh context |
| Token usage > 80% | New session |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Lost important decisions | Always summarize before fresh start |
| New session is worse | Provide more initial context |
| Forgot what was done | Use handoff documents consistently |
| Starting fresh too often | Trust `/clear` for minor issues |

---

## Fresh Start Templates

### For Bug Fixes
```
Continuing a bug fix session:
- Bug: [Description]
- Root cause: [What we found]
- Attempted fixes: [List]
- Next step: [What to try]
- Relevant files: [List]
```

### For Feature Development
```
Continuing feature development:
- Feature: [Name]
- Progress: [X]% complete
- Completed: [List]
- Remaining: [List]
- Key decisions: [List]
```

### For Refactoring
```
Continuing refactoring:
- Goal: [What we're improving]
- Approach: [Strategy]
- Files touched: [List]
- Tests status: [Passing/Failing]
- Next step: [Specific task]
```

---

## Pro Tips

1. **Preemptive Summaries:** Every 30 minutes, ask Claude to summarize progress
2. **Lightweight Context:** New sessions need less than you think - be concise
3. **Trust Fresh Starts:** A clean context often produces better results than a cluttered one
4. **Session Boundaries:** Natural breaks (lunch, meetings) are good fresh start points

---

## The Fresh Start Mindset

Think of conversations like Git branches:
- **Long-running conversations** = Feature branches that get stale
- **Fresh starts** = Rebasing onto main
- **Summaries** = Commit messages preserving history

A fresh start isn't losing progress - it's maintaining quality.

---

## Next Challenge

Continue to **[Output Extraction](./07-output-extraction.md)** to learn how to get data out of Claude efficiently!
