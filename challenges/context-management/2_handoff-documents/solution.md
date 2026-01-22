# Solution: Handoff Documents

## Step-by-Step Solution

### Step 1: Choose Your Template Style

Pick the template that matches your work type:

#### Template A: Development Work
```markdown
# Handoff: [Project] - [Date]

## 🎯 Current Objective
[One sentence: what you're building/fixing]

## ✅ Completed
- [Task with outcome]
- [Task with outcome]

## 🔧 Active Work
[2-3 sentences on what's in progress]

```code
[Only relevant code snippets]
```

## 📋 Next Steps
1. [Specific action]
2. [Specific action]

## 💡 Key Insights
- [Decision + rationale]
- [Pattern discovered]

## ⚠️ Blockers/Issues
- [Issue description]
```

#### Template B: Debugging Work
```markdown
# Debug Handoff: [Issue] - [Date]

## 🐛 Problem
[Clear problem statement]

## 🔍 Investigation Summary
**Tried:**
- [Approach 1] - Result: [Outcome]
- [Approach 2] - Result: [Outcome]

**Root Cause Hypothesis:**
[Current theory]

## 📊 Evidence
- Symptom 1: [Description]
- Symptom 2: [Description]

## 🎯 Next Investigation Steps
1. [Specific test to run]
2. [Code area to examine]

## 🔗 Relevant Code
```code
[Minimal problematic code]
```
```

#### Template C: Research/Planning Work
```markdown
# Research Handoff: [Topic] - [Date]

## 📚 Question
[What you're researching]

## ✅ Findings
- [Finding + source]
- [Finding + source]

## 🤔 Analysis
[Key insights, patterns, tradeoffs]

## ⚖️ Decision Framework
| Option | Pros | Cons | Score |
|--------|------|------|-------|
| A | ... | ... | 8/10 |
| B | ... | ... | 6/10 |

## 🎯 Recommendation
[What to do next + why]

## ❓ Open Questions
- [Question needing more research]
```

### Step 2: Apply the Golden Rules

**Rule 1: Compress Ruthlessly**

❌ **Before compression (verbose):**
```markdown
## Completed Work
I implemented the user authentication system. First, I created
a User model with various fields including id, email, password,
and timestamps. Then I set up bcrypt for password hashing with
a salt round of 12, which provides good security while maintaining
reasonable performance. After that, I created login and signup
endpoints using Express.js. The login endpoint accepts email and
password, validates them against the database, and returns a JWT
token if successful. I also added error handling for cases where
the user doesn't exist or the password is wrong.
```

✅ **After compression (concise):**
```markdown
## ✅ Completed
- User model: id, email, password (bcrypt/12), timestamps
- Auth endpoints: POST /login, POST /signup
- JWT token generation on successful auth
- Error handling: user not found, invalid password
```

**Rule 2: Decisions Over Descriptions**

❌ **Wrong focus:**
```markdown
We're using PostgreSQL for the database.
```

✅ **Right focus:**
```markdown
**PostgreSQL vs MongoDB**: Chose PostgreSQL - Rationale: Need
ACID transactions for financial data, existing team expertise
```

**Rule 3: Code Context Only When Necessary**

Include code only if:
- It's actively being worked on
- It contains a bug being debugged
- It shows a pattern/decision

❌ **Too much code:**
```markdown
## Code Context
```typescript
// Entire 200-line file
import express from 'express';
import bcrypt from 'bcrypt';
// ... everything ...
```
```

✅ **Right amount:**
```markdown
## 🔧 Active Code
```typescript
// Issue: Race condition in token refresh
async refreshToken(token: string) {
  const payload = verify(token);
  // BUG: Multiple concurrent calls create multiple tokens
  return generateNewToken(payload.userId);
}
```
```

### Step 3: Real-World Example

**Scenario:** Debugging React performance issue

```markdown
# Debug Handoff: React App Slow Rendering - 2025-01-21

## 🐛 Problem
Dashboard page takes 3-5 seconds to render with 100+ items. Target: <500ms

## 🔍 Investigation Summary
**Tried:**
- ✅ Added React.memo to DataTable component - Reduced to 2s (33% improvement)
- ✅ Implemented virtual scrolling with react-window - Reduced to 1.2s (40% more)
- ❌ useMemo on filter function - No measurable impact
- 🔄 In progress: Moving data processing to Web Worker

**Root Cause Hypothesis:**
Heavy computation in render cycle. Each item runs 3 transformations
synchronously, blocking main thread.

## 📊 Evidence
- Chrome DevTools: 2.8s scripting time in flamegraph
- 300ms per 100 items in data transformation
- CPU maxed at 100% during render
- No network or memory bottleneck

## 🎯 Next Investigation Steps
1. Profile `transformData()` function - likely culprit
2. Consider memoizing transformation results
3. Test Web Worker approach for computation

## 🔗 Relevant Code
```typescript
// DataTable.tsx - renderItem called 100+ times
function renderItem(item: Item) {
  // BUG: These run on every render
  const formatted = formatCurrency(item.amount);
  const status = calculateStatus(item);
  const trend = analyzeTrend(item.history);
  return <Row data={{formatted, status, trend}} />;
}
```

## 💡 Key Insights
- Virtual scrolling helps, but computation is the bottleneck
- React DevTools Profiler shows renderItem taking 90% of time
- Memoization at component level isn't enough, need data-level caching
```

**Why this works:**
- Quickly scannable sections
- Shows what was tried and outcomes
- Clear hypothesis
- Specific next steps
- Minimal but relevant code
- Evidence-based reasoning

### Step 4: Test Your Handoff

Start a new conversation with:

```
I'm continuing work from a previous session. Here's the context:

[paste handoff document]

Let's continue with [next step from document].
```

Claude should:
- Not ask for clarification on already-provided info
- Understand the problem/goal immediately
- Jump straight into the next step
- Reference decisions from the handoff appropriately

### Step 5: Iterate Your Template

After each handoff, ask:
- What information was missing?
- What information was unnecessary?
- How long did it take to resume productivity?
- Could the structure be clearer?

Refine your template based on these answers.

## Common Mistakes to Avoid

### Mistake 1: Timeline Dumps
❌ **Wrong:**
```markdown
First I did X, then I did Y, then we discussed Z, after that I tried A...
```

✅ **Correct:**
```markdown
## Completed
- X - Result: [outcome]
- Y - Result: [outcome]

## Current Focus
Z - because [rationale]
```

### Mistake 2: Missing the "Why"
❌ **Wrong:**
```markdown
Using Redux for state management.
```

✅ **Correct:**
```markdown
**Redux vs Context API**: Redux - Rationale: Complex state with
time-travel debugging needed, team familiar with Redux patterns
```

### Mistake 3: Vague Next Steps
❌ **Wrong:**
```markdown
## Next Steps
- Finish the feature
- Test it
- Deploy
```

✅ **Correct:**
```markdown
## Next Steps
1. Complete refresh token rotation logic (see marked TODO in auth.ts line 45)
2. Add integration test for concurrent refresh scenario
3. Deploy to staging, monitor token refresh metrics for 24h
```

### Mistake 4: No Prioritization
❌ **Wrong:** Everything listed equally.

✅ **Correct:** Use emojis or tags:
- 🔥 Critical/Blocking
- 🎯 High Priority
- 💡 Nice-to-have
- ⚠️ Known issue to watch

## Advanced Techniques

### Technique 1: Progressive Handoffs

For multi-day projects, maintain a cumulative handoff:

```markdown
# Project Handoff: E-commerce Platform

## Overall Status
Week 2 of 6 - Auth system complete, starting checkout flow

## Session History
### 2025-01-21 PM - Checkout Cart
- [Details for this session]

### 2025-01-21 AM - Auth System
- [Archived, less detail]

### 2025-01-20 - User Models
- [Archived, minimal detail]
```

### Technique 2: Decision Log

Maintain a separate decisions file:

```markdown
# Decision Log

## 2025-01-21: JWT vs Sessions
**Decision:** JWT
**Rationale:** Stateless auth for mobile apps
**Implications:** Need refresh token rotation, can't revoke immediately

## 2025-01-20: PostgreSQL vs MongoDB
**Decision:** PostgreSQL
**Rationale:** ACID transactions required for payments
**Implications:** Need migration strategy for schema changes
```

Reference in handoffs: "See decision log for JWT rationale"

### Technique 3: Visual Status

Use ASCII progress bars or tables:

```markdown
## Feature Status
[████████░░] 80% - Auth System
[████░░░░░░] 40% - Checkout Flow
[░░░░░░░░░░]  0% - Admin Panel

## Test Coverage
Unit:        [██████████] 85%
Integration: [████░░░░░░] 45%
E2E:         [██░░░░░░░░] 20%
```

## Measuring Success

Good handoff documents result in:
- ✅ Resume work in <2 minutes
- ✅ No repeated questions
- ✅ Clear action items
- ✅ Preserved decision context
- ✅ <2000 tokens
- ✅ 5-minute read time

## Template Library

Save your templates:

```bash
mkdir -p ~/.claude/templates

# Create template files
cat > ~/.claude/templates/handoff-dev.md << 'EOF'
# Handoff: [Project] - [Date]
## 🎯 Current Objective
## ✅ Completed
## 🔧 Active Work
## 📋 Next Steps
## 💡 Key Insights
## ⚠️ Blockers/Issues
EOF
```

Then copy-paste and fill in when needed.
