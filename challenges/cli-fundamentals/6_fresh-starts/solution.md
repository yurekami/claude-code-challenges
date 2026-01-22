# Solution: Knowing When to Start Fresh

## Decision Framework

### The Fresh Start Matrix

```
                    Token Usage
                Low        Medium       High
              (0-40%)    (40-70%)    (70-100%)
           ╔═══════════╤═══════════╤═══════════╗
Related    ║ CONTINUE  │ CONTINUE  │ CONSIDER  ║
Work       ║           │           │  FRESH    ║
           ╟───────────┼───────────┼───────────╢
New        ║ CONTINUE  │ CONSIDER  │  FRESH    ║
Feature    ║           │  FRESH    │  START    ║
           ╟───────────┼───────────┼───────────╢
Different  ║ CONSIDER  │  FRESH    │  FRESH    ║
Project    ║  FRESH    │  START    │  START    ║
           ╚═══════════╧═══════════╧═══════════╝
```

### Decision Algorithm

```python
def should_start_fresh():
    token_usage = check_usage()

    # Critical thresholds
    if token_usage > 0.90:
        return True  # Always reset above 90%

    if token_usage > 0.80 and is_complex_task():
        return True  # High usage + complexity = reset

    # Quality indicators
    if repeated_failures > 3:
        return True  # Not making progress

    if context_drift_detected():
        return True  # Lost focus

    # Task boundaries
    if is_different_feature_area():
        return True  # Separate concerns

    if phase_transition():
        return "CONSIDER"  # Might benefit

    # All clear
    if token_usage < 0.60 and making_progress():
        return False  # Keep going

    return "EVALUATE"  # Manual decision needed
```

## Scenario-Based Solutions

### Scenario 1: Token Crisis

**Situation**:
```
Current state:
- Token usage: 85%
- Working on: Authentication refactor
- Next task: Add email verification
```

**Analysis**:
- High token usage ✗
- Related work ✓
- Complex task ahead ✗

**Decision**: START FRESH

**How to transition**:
```bash
# In current conversation
You: "Summarize the authentication refactor we just completed,
     including key architectural decisions and any gotchas."

Claude: [Provides summary]

# Copy summary, start new conversation
claude  # New session

You: "I just completed an authentication refactor.
     Here's the summary: [paste]

     Now I need to add email verification to the system."
```

### Scenario 2: Steady Progress

**Situation**:
```
Current state:
- Token usage: 35%
- Working on: User profile page
- Next task: Add avatar upload to profile
```

**Analysis**:
- Low token usage ✓
- Related work ✓
- Making progress ✓

**Decision**: CONTINUE

**Why**:
- Plenty of token budget
- Avatar upload directly relates to profiles
- Context about profile structure is valuable

### Scenario 3: Failed Attempts

**Situation**:
```
Current state:
- Token usage: 55%
- Working on: WebSocket connection bug
- Attempts: 5 different fixes, none worked
```

**Analysis**:
- Medium token usage ~
- Stuck on same problem ✗
- Accumulating failed approaches ✗

**Decision**: START FRESH

**Why**:
- Fresh perspective needed
- Old failed attempts are cluttering context
- New framing might reveal solution

**How to transition**:
```bash
# Document the problem
You: "Document this WebSocket issue:
     - What we've tried
     - What didn't work
     - What we know
     - What we don't know"

Claude: [Creates detailed doc]

# Save to file
You: "Save this to WEBSOCKET_BUG.md"

# New conversation with clean slate
claude

You: "I'm debugging a WebSocket connection issue.
     See WEBSOCKET_BUG.md for details.
     Let's approach this from first principles."
```

### Scenario 4: Task Switch

**Situation**:
```
Current state:
- Token usage: 45%
- Working on: Frontend components
- Next task: Database migration for new table
```

**Analysis**:
- Medium token usage ~
- Completely different area ✗
- No shared context needed ✗

**Decision**: START FRESH

**Why**:
- Frontend context not useful for backend
- Clean separation of concerns
- Optimize token usage for relevant context

### Scenario 5: Phase Transition

**Situation**:
```
Current state:
- Token usage: 40%
- Working on: Planning architecture
- Next task: Implementation
```

**Analysis**:
- Medium token usage ~
- Related (same feature) ✓
- Plan is valuable context ✓
- Long implementation ahead ~

**Decision**: CONSIDER (both options valid)

**Option A: Continue**
```
Pros:
- Architecture plan in context
- Can reference decisions
- Continuity

Cons:
- Implementation will consume lots of tokens
- May hit limits during implementation
```

**Option B: Fresh Start**
```
Pros:
- Full token budget for implementation
- Can focus on code without plan clutter
- Cleaner context

Cons:
- Need to preserve key decisions
- Extra step to transfer context
```

**Recommendation**: Save plan to file, start fresh
```bash
You: "Save this architecture plan to ARCHITECTURE.md"

# New session
claude

You: "Implement the architecture in ARCHITECTURE.md"
```

## Context Preservation Techniques

### Technique 1: File-Based Handoff

**Best for**: Complex state, architectural decisions

```bash
# Current conversation
You: "Save our discussion about the API design to API_DESIGN.md"

Claude: [Creates file with details]

# New conversation
claude

You: "Implement the API design from API_DESIGN.md"
```

**Pros**:
- Permanent record
- Can reference later
- Shareable with team

**Cons**:
- Extra step
- Need to write good docs

### Technique 2: Summary Transfer

**Best for**: Moderate context, key decisions

```bash
# Current conversation
You: "Summarize what we've accomplished and key decisions in 5 bullet points"

Claude:
"Summary:
- Chose PostgreSQL for data persistence
- Decided on JWT for authentication (1 hour expiry)
- Implemented rate limiting: 100 req/min
- Used Redis for caching frequently accessed data
- Adopted Repository pattern for data access"

# Copy bullets, new conversation
claude

You: "Continuing from previous work. Context:
[paste 5 bullets]

Now let's implement the caching layer."
```

**Pros**:
- Quick and efficient
- Only preserves essentials
- Easy to communicate

**Cons**:
- May lose some nuance
- Need to identify key points

### Technique 3: Code Artifact Anchoring

**Best for**: When files tell the story

```bash
# Current conversation has modified 10 files
# All changes committed

# New conversation
claude

You: "Review the last commit and continue with the next feature"

Claude: [Reads commit, understands context from code]
```

**Pros**:
- Code is the truth
- No manual summary needed
- Git history preserves decisions

**Cons**:
- Only works if code is committed
- May miss non-code context

### Technique 4: Checklist Continuation

**Best for**: Multi-phase projects

```bash
# Current conversation
You: "Create a checklist of remaining tasks for this feature"

Claude:
"Remaining Tasks:
- [ ] Implement user settings page
- [ ] Add email notification preferences
- [ ] Create admin dashboard
- [ ] Add analytics tracking
- [ ] Write integration tests"

# Copy checklist, new conversation
claude

You: "Working on the user management feature.

Completed:
- [x] User registration
- [x] Login/logout
- [x] Password reset

Next steps:
[paste remaining checklist]

Let's start with the user settings page."
```

**Pros**:
- Clear progress tracking
- Easy to resume
- Explicit about status

**Cons**:
- Manual maintenance
- Can get stale

## Token Usage Patterns

### Low Usage (0-40%): Continue Freely

```
Typical conversations:
- Quick questions
- Single file edits
- Code reviews
- Small features

Strategy: Keep going unless task switching
```

### Medium Usage (40-70%): Evaluate Context

```
Typical conversations:
- Multi-file changes
- Feature implementations
- Debugging sessions
- Architecture discussions

Strategy:
- Continue if related work
- Consider fresh if switching areas
- Monitor quality
```

### High Usage (70-90%): Prepare to Reset

```
Typical conversations:
- Large refactors
- Multiple features
- Long debugging
- Deep rabbit holes

Strategy:
- Plan to wrap up soon
- Use /clear to reduce clutter
- Start fresh for next major task
```

### Critical Usage (90-100%): Reset Immediately

```
At this level:
- Claude's responses may degrade
- Complex reasoning suffers
- Context conflicts increase

Strategy:
- Stop what you're doing
- Document current state
- Start fresh ASAP
```

## Quality Indicators

### Signs of Healthy Context

✓ **Claude remembers**:
  "As we discussed earlier..."

✓ **References specific details**:
  "In the authenticate() function we wrote..."

✓ **Builds on previous work**:
  "Building on the auth system, let's add..."

✓ **Catches inconsistencies**:
  "Wait, this conflicts with our earlier decision to..."

### Signs of Context Degradation

✗ **Generic responses**:
  "You could implement it this way..." (what way?)

✗ **Forgets decisions**:
  Suggests approach you already rejected

✗ **Asks for info you provided**:
  "What database are you using?" (told it 3 times)

✗ **Contradicts earlier work**:
  "Let's use MySQL" (but we chose PostgreSQL)

✗ **Slower responses**:
  Taking significantly longer to respond

## Advanced Strategies

### Strategy 1: Conversation Checkpoints

```bash
# Every 20-30 minutes
/usage  # Check token level
/stats  # Review activity

# If >50%, create checkpoint
You: "Create a checkpoint document summarizing:
     1. What we've built
     2. Key decisions
     3. Next steps"

# Save checkpoint
# Continue or restart as needed
```

### Strategy 2: Parallel Conversations

```bash
# Terminal 1: Main feature work
claude

# Terminal 2: Quick questions/experiments
claude

# Keep contexts separate, focused
```

### Strategy 3: Session Planning

```bash
# Before starting
You: "I have 3 tasks:
     1. Fix login bug (30 min)
     2. Add password reset (45 min)
     3. Refactor auth module (60 min)

     Given token limits, should I split these into separate sessions?"

Claude: "Yes, I recommend:
         Session 1: Tasks 1 & 2 (related, should fit)
         Session 2: Task 3 (major refactor needs full context)"
```

### Strategy 4: Progressive Complexity

```bash
# Start fresh for complex work
# Use tail end for simple tasks

Session start (0%):    Complex refactoring
Session middle (50%):  Related improvements
Session end (75%):     Simple docs, comments
```

## Common Mistakes

### Mistake 1: Context Hoarding

**Symptom**: Pushing to 95% tokens because "I don't want to restart"

**Problem**: Quality suffers, responses slow, errors increase

**Solution**: Reset at 80% for complex work, 90% for simple tasks

### Mistake 2: Premature Optimization

**Symptom**: Starting fresh at 25% tokens "just to be safe"

**Problem**: Loses valuable context, unnecessary overhead

**Solution**: Continue until 60%+ or natural break point

### Mistake 3: No Transition Plan

**Symptom**: Starting fresh without preserving critical context

**Problem**: Repeats questions, loses decisions, wastes time

**Solution**: Always document or summarize before resetting

### Mistake 4: Too Many Fragments

**Symptom**: 20 conversations in one day, each 5% tokens

**Problem**: Context switching overhead, hard to track progress

**Solution**: Group related work into sessions

## Practical Guidelines

### Daily Work Pattern

```
Morning Session (0-60%):
- Review yesterday's work
- Main feature implementation
- Related improvements

Afternoon Session 1 (0-60%):
- Different feature area
- Fresh context, fresh thinking

Afternoon Session 2 (0-60%):
- Bug fixes, small tasks
- Documentation, cleanup

End of Day (any%):
- Quick questions
- Planning tomorrow
```

### Project Phases

```
Planning Phase:
- 1-2 long conversations
- Document thoroughly
- START FRESH for implementation

Implementation Phase:
- Feature-sized conversations
- Reset between unrelated features
- Continue for related work

Debugging Phase:
- Reset after 3-5 failed attempts
- Fresh perspective helps

Polish Phase:
- Can continue longer
- Simpler tasks, less context needed
```

## Success Metrics

Track these to optimize your reset strategy:

```
Metric 1: Average token usage at session end
Target: 60-75% (maximizing usage without degradation)

Metric 2: Number of resets per day
Target: 3-5 (not too many, not too few)

Metric 3: Tasks completed per session
Target: 2-4 related tasks (focused but productive)

Metric 4: Context preservation success rate
Target: >90% (rarely lose important context)
```

## Quick Reference

### Reset Decision Tree

```
1. Check token usage (/usage)

   If >80% → START FRESH
   If <40% → CONTINUE
   If 40-80% → Go to step 2

2. Evaluate task relatedness

   Related work → CONTINUE
   Different area → GO to step 3

3. Check progress quality

   Making progress → CONTINUE
   Stuck/failing → START FRESH

4. Consider complexity ahead

   Simple tasks → CONTINUE
   Complex tasks → START FRESH
```

### Conversation Lifecycle

```
START (0-20%):
- Complex tasks
- Deep reasoning
- Architecture

MIDDLE (20-60%):
- Implementation
- Related features
- Iterations

LATE (60-80%):
- Finishing touches
- Documentation
- Simple tasks

END (80%+):
- Wrap up
- Commit work
- START FRESH next
```

## Final Tips

1. **Monitor actively**: Check `/usage` every 20-30 minutes
2. **Trust your gut**: If it feels slow/confused, reset
3. **Document liberally**: Makes resets painless
4. **Embrace resets**: Not a failure, it's a tool
5. **Plan ahead**: Know when you'll reset before you need to
6. **Stay organized**: Good file structure makes resets easier
7. **Learn your patterns**: Track what works for you

You've mastered conversation management when resetting feels natural, not disruptive.
