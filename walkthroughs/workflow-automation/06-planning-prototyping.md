# Walkthrough: Planning & Prototyping

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** Workflow Automation

---

## Overview

When should you plan extensively vs. just start building? This challenge teaches you to balance upfront planning with rapid prototyping, knowing when each approach serves you best.

## Prerequisites

- [ ] Experience with both planning and coding
- [ ] Understanding of project complexity levels
- [ ] Willingness to experiment

---

## Step 1: The Planning Spectrum

```
No Planning                            Heavy Planning
     │────────────────────────────────────────│
     │                                        │
  Hack it    Quick      Balanced   Detailed   Waterfall
  together   sketch     approach   planning   design
     │                                        │
   Minutes   30 min     1-2 hours  Days       Weeks
```

---

## Step 2: When to Plan More

### Plan First When:
- [ ] Multiple systems involved
- [ ] Team coordination needed
- [ ] Breaking changes required
- [ ] Security-critical features
- [ ] External dependencies
- [ ] High cost of mistakes

### Planning Signals
```
Complexity Indicators:
- Touches 5+ files
- Involves database schema changes
- Affects multiple team members
- Has non-obvious edge cases
- Requires external APIs
```

---

## Step 3: When to Prototype First

### Prototype When:
- [ ] Requirements unclear
- [ ] Novel technology involved
- [ ] Need to prove feasibility
- [ ] Learning new patterns
- [ ] UI/UX exploration

### Prototyping Signals
```
Uncertainty Indicators:
- "I'm not sure if this is possible"
- "Which library should we use?"
- "What should the API look like?"
- "How will this feel to use?"
```

---

## Step 4: The Balanced Approach

### Quick Planning (30 minutes)
```
Ask Claude:
"I want to implement [feature]. Before we start:
1. What are the main components needed?
2. What could go wrong?
3. What's the order of implementation?
4. What's the simplest version we can build first?"
```

### Then Prototype
```
"Let's build a minimal version that:
- Does the core thing
- Ignores edge cases for now
- Uses simple implementations
- Can be thrown away if wrong"
```

### Then Iterate
```
"The prototype works. Now let's:
- Add proper error handling
- Handle edge cases
- Improve performance
- Add tests"
```

---

## Step 5: Planning with Claude

### Feature Planning Prompt
```
I need to implement [feature].

Create a brief implementation plan:
1. Components needed (max 5)
2. Order of implementation
3. Key decision points
4. Risks to watch for

Keep it to one screen of text.
```

### Spike/Prototype Prompt
```
I'm not sure how to approach [problem].

Create a quick spike to:
1. Prove it's feasible
2. Find the tricky parts
3. Learn the API/library

This is throwaway code, prioritize learning over quality.
```

---

## Step 6: The Planning Document

### Minimal Plan Template
```markdown
# [Feature Name]

## Goal
One sentence describing success.

## Approach
3-5 bullet points of how we'll build it.

## Order
1. Build X first
2. Then add Y
3. Finally implement Z

## Questions
- [ ] Decision 1?
- [ ] Decision 2?

## First Step
The very next thing to do.
```

---

## Step 7: Adaptive Planning

### Start Building, Plan When Stuck
```
1. Start implementing
2. When you hit a decision point: pause
3. Think/discuss the decision
4. Continue building
5. Repeat
```

### Prompt for Adaptive Planning
```
I started building [feature] and hit a decision point:
[Describe the decision]

Help me think through:
1. What are my options?
2. Tradeoffs of each?
3. Which fits our situation?
```

---

## Verification Checklist

- [ ] Identified a feature's complexity level
- [ ] Created a minimal plan for a medium feature
- [ ] Built a prototype for an unclear requirement
- [ ] Used adaptive planning (planned while building)
- [ ] Knew when to stop planning and start coding

---

## Decision Framework

| Situation | Approach |
|-----------|----------|
| Know exactly what to build | Light planning, start coding |
| Unsure about feasibility | Prototype first |
| Multiple valid approaches | Quick spike each approach |
| Team needs to coordinate | Plan and document |
| High risk/cost | Detailed planning |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Planning paralysis | Set a time limit |
| Prototype becomes production | Explicitly label as throwaway |
| No planning, big mess | Quick plan for 5+ file changes |
| Plan becomes outdated | Keep plans minimal |

---

## Pro Tips

1. **Time Box Planning:** Max 30 min for most features
2. **Plan to Throw Away:** First attempt often teaches, rarely ships
3. **Validate Early:** Build the risky part first
4. **Document Decisions:** Remember why, not just what

---

## Next Challenge

Continue to **[Progressive Automation](./07-progressive-automation.md)** to automate the automation!
