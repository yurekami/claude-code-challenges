# Walkthrough: Fork Strategies

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** Context Management

---

## Overview

Sometimes you need to explore multiple approaches simultaneously. Fork strategies let you branch your conversations like Git branches - try different solutions, compare results, and merge the best approach back.

## Prerequisites

- [ ] Understanding of context management
- [ ] Experience with multi-session workflows
- [ ] Familiarity with Git branching concepts

---

## Step 1: Understand When to Fork

### Good Reasons to Fork

| Scenario | Why Fork? |
|----------|-----------|
| Multiple solution approaches | Compare implementations |
| Risk-free experimentation | Try without affecting main work |
| A/B testing code | Generate alternatives |
| Parallel development | Work on independent features |
| What-if analysis | Explore consequences |

### Fork Decision Checklist
- [ ] Am I about to try something experimental?
- [ ] Are there 2+ valid approaches to consider?
- [ ] Would I lose valuable context if this fails?
- [ ] Do I need to compare outcomes?

---

## Step 2: Create a Fork Point

Before forking, establish your baseline:

```
Create a checkpoint summary for forking:
- Current state of the code
- The decision point we're at
- Options we're considering
- Criteria for choosing the winner
```

**Example:**
```markdown
## Fork Point: Authentication Strategy

### Current State
- User model is complete
- Basic routes are set up
- No auth implemented yet

### Options to Explore
A. JWT with refresh tokens (stateless)
B. Session-based with Redis (stateful)
C. OAuth only (delegated)

### Decision Criteria
- Performance under load
- Implementation complexity
- Security requirements
- Scalability needs
```

---

## Step 3: Execute the Fork

### Method 1: Multiple Terminal Sessions
```bash
# Terminal 1 - Approach A
cd ~/project
claude
"Let's implement JWT authentication with refresh tokens"

# Terminal 2 - Approach B
cd ~/project
claude
"Let's implement session-based authentication with Redis"
```

### Method 2: Named Sessions
```bash
# Create named session for approach A
claude --session jwt-auth
"Implement JWT authentication"

# Create named session for approach B
claude --session session-auth
"Implement session-based authentication"
```

### Method 3: Git Worktrees + Claude
```bash
# Create worktree for approach A
git worktree add ../project-jwt feature/jwt-auth
cd ../project-jwt
claude

# Create worktree for approach B
git worktree add ../project-session feature/session-auth
cd ../project-session
claude
```

---

## Step 4: Develop in Parallel

Run both approaches to comparable completion:

### Track Progress in Each Fork
```
Fork A Progress:
- ✅ Token generation
- ✅ Token validation middleware
- 🔄 Refresh token rotation

Fork B Progress:
- ✅ Session creation
- ✅ Session middleware
- 🔄 Redis integration
```

### Keep Notes for Comparison
```markdown
## Fork Observations

### Fork A (JWT)
- Pros: Stateless, easy to scale
- Cons: Token revocation is complex
- Implementation time: 2 hours
- Lines of code: ~150

### Fork B (Sessions)
- Pros: Easy revocation, familiar pattern
- Cons: Redis dependency, session storage
- Implementation time: 2.5 hours
- Lines of code: ~200
```

---

## Step 5: Compare and Evaluate

### Generate Comparison Report
```
Compare the two authentication approaches we've implemented:

Fork A (JWT): [Summary of implementation]
Fork B (Sessions): [Summary of implementation]

Evaluate based on:
1. Code complexity
2. Performance implications
3. Security considerations
4. Maintenance burden
5. Scalability
```

### Side-by-Side Analysis
```
/compare fork-a fork-b
```

---

## Step 6: Merge the Winner

### Adopt the Winning Approach
```bash
# If Fork A wins
git checkout main
git merge feature/jwt-auth

# Clean up
git worktree remove ../project-session
git branch -d feature/session-auth
```

### Extract Best of Both
Sometimes you want elements from multiple forks:

```
Take the token validation from Fork A and combine it with
the session storage pattern from Fork B. Create a hybrid approach.
```

---

## Step 7: Document Fork Outcomes

```markdown
# Fork Resolution: Authentication

## Decision
Chose JWT with refresh tokens (Fork A)

## Rationale
- Better scalability (stateless)
- Cleaner implementation
- Lower infrastructure requirements

## Rejected Alternative
Session-based auth was considered but rejected due to:
- Redis dependency
- Session synchronization complexity

## Lessons Learned
- Refresh token rotation was more complex than expected
- Consider hybrid approach for future high-security features
```

---

## Verification Checklist

- [ ] Identified a decision point worth forking
- [ ] Created checkpoint summary before forking
- [ ] Developed two approaches in parallel
- [ ] Compared outcomes systematically
- [ ] Merged winning approach successfully
- [ ] Documented the fork resolution

---

## Fork Patterns

### Exploration Fork
```
Quick spike to test feasibility
├── Fork: Try approach
└── Main: Continue if works, abandon if not
```

### Competition Fork
```
Full implementation comparison
├── Fork A: Complete implementation
├── Fork B: Complete implementation
└── Evaluate and choose winner
```

### Safety Fork
```
Risky change protection
├── Fork: Make risky changes
└── Main: Preserved safe state
    ↑ Merge if successful
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Forks diverge too much | Set clear scope and stopping points |
| Lost track of differences | Document as you go |
| Merge conflicts | Use Git worktrees for clean separation |
| Wasted effort | Set time limits on exploration forks |

---

## Pro Tips

1. **Time-Box Forks:** Set a limit (e.g., 2 hours) for exploration forks
2. **Clear Criteria:** Define "winner" criteria before starting
3. **Document Everything:** What you learn from rejected approaches is valuable
4. **Use Git:** Always back forks with version control

---

## Next Challenge

Continue to **[System Prompt Optimization](./05-system-prompt-optimization.md)** to slim down token overhead!
