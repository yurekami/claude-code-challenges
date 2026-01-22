# Solution: Context Compaction

## Step-by-Step Solution

### Step 1: Recognize the Need for Compaction

Watch for these indicators:

```
Warning Signs Checklist:
✓ Conversation > 50k tokens
✓ Slow response times
✓ Repeated information
✓ Claude saying "as mentioned earlier..."
✓ Multiple context switches
✓ Conversation spanning 2+ hours
```

### Step 2: Create a Structured Handoff Document

Use this template:

```markdown
# Session Handoff: [Project Name]

## Current Objective
- Primary goal: [What you're trying to accomplish]
- Current phase: [Where you are in the process]

## Completed Work
1. [Task 1] - Completed
2. [Task 2] - Completed
3. [Task 3] - In progress (70%)

## Key Decisions Made
- **Decision 1**: [What] - Rationale: [Why]
- **Decision 2**: [What] - Rationale: [Why]

## Active Code Context
```typescript
// Only include currently relevant snippets
function criticalFunction() {
  // Implementation
}
```

## Remaining Work
- [ ] Task A
- [ ] Task B
- [ ] Task C

## Known Issues
- Issue 1: [Description]
- Issue 2: [Description]

## Important Context
- Constraint 1: [Details]
- Requirement 2: [Details]
```

### Step 3: Execute the Handoff

**In old conversation:**
```
"Please create a concise handoff document summarizing our session.
Include completed tasks, key decisions, active code context, and
remaining work."
```

**In new conversation:**
```
"I'm continuing work from a previous session. Here's the handoff
document with context: [paste handoff doc]

Let's continue with [next task]."
```

### Step 4: Verify Continuity

After starting the new conversation:

1. Ask Claude to summarize their understanding
2. Verify critical context is preserved
3. Confirm next steps are clear
4. Begin work

## Example: Real Handoff Document

```markdown
# Session Handoff: E-commerce Auth System

## Current Objective
Implement OAuth2 authentication with JWT tokens for user login/signup

## Completed Work
1. User model schema - Complete
2. JWT token generation - Complete
3. Login endpoint - Complete
4. Refresh token logic - In progress (80%)

## Key Decisions Made
- **JWT vs Sessions**: Chose JWT for stateless auth and mobile app support
- **Token expiry**: Access tokens 15min, refresh tokens 7 days
- **Password hashing**: bcrypt with 12 rounds (security vs performance)

## Active Code Context
```typescript
// Current refresh token implementation
async function refreshAccessToken(refreshToken: string) {
  const payload = verifyToken(refreshToken);
  if (payload.type !== 'refresh') throw new Error('Invalid token type');
  return generateAccessToken(payload.userId);
}
```

## Remaining Work
- [ ] Complete refresh token rotation
- [ ] Add rate limiting to auth endpoints
- [ ] Write integration tests for auth flow
- [ ] Add password reset functionality

## Known Issues
- Refresh token rotation causing race conditions
- Need to handle concurrent refresh requests

## Important Context
- Must support mobile + web clients
- Rate limit: 5 login attempts per 15min per IP
- Token signing key stored in env var JWT_SECRET
```

## Common Mistakes to Avoid

### Mistake 1: Including Too Much Detail
❌ **Wrong:**
```markdown
## Completed Work
1. Created user model with fields: id (uuid), email (string, unique),
   passwordHash (string, bcrypt), createdAt (timestamp), updatedAt
   (timestamp), lastLogin (nullable timestamp), isVerified (boolean),
   verificationToken (nullable string)...
```

✅ **Correct:**
```markdown
## Completed Work
1. User model schema - Complete (uuid id, email, passwordHash, timestamps)
```

### Mistake 2: Missing Critical Context
❌ **Wrong:**
```markdown
## Key Decisions Made
- Using JWT tokens
- Tokens expire
```

✅ **Correct:**
```markdown
## Key Decisions Made
- **JWT vs Sessions**: JWT for stateless auth - Rationale: Mobile app support
- **Token expiry**: 15min access, 7d refresh - Rationale: Security balance
```

### Mistake 3: No Structure
❌ **Wrong:**
```
We built the login system and it works. Need to add refresh tokens
and rate limiting. Also there was a bug with concurrent requests...
```

✅ **Correct:** Use the template structure with clear sections.

### Mistake 4: Outdated Code Snippets
❌ **Wrong:** Including old implementations that were replaced.

✅ **Correct:** Only include current, active code that's relevant.

## Best Practices

1. **Compact proactively** - Don't wait for Claude to suggest it
2. **Time-based triggers** - Every 90-120 minutes of active work
3. **Token-based triggers** - Around 50k tokens
4. **Task-based triggers** - At natural breakpoints (feature complete)
5. **Keep handoffs scannable** - Use bullet points and headers
6. **Version handoffs** - If project is long-running, date them
7. **Test the handoff** - Verify new session has needed context

## Measuring Success

After compaction, you should observe:
- Faster response times
- No lost context
- Smooth continuation of work
- Reduced token costs
- Easier to stay focused

## Advanced Tip: Incremental Handoffs

For very long projects, maintain a running handoff document:

```bash
# Create handoff directory
mkdir -p .claude/handoffs

# Update after each major milestone
echo "## Session 2025-01-21 14:30" >> .claude/handoffs/auth-system.md
echo "- Completed refresh token rotation" >> .claude/handoffs/auth-system.md
```

Then reference it in new conversations:
```
"Continuing auth system work. Context in .claude/handoffs/auth-system.md"
```
