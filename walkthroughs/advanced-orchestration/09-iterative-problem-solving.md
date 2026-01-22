# Walkthrough: Iterative Problem Solving

**Difficulty:** Medium | **Time:** 25 minutes | **Category:** Advanced Orchestration

---

## Overview

Complex problems rarely have single-step solutions. Iterative problem solving breaks down challenges into cycles of hypothesis, test, learn, and refine. This challenge teaches you to use Claude for systematic debugging and problem resolution.

## Prerequisites

- [ ] A problem to solve
- [ ] Patience for iteration
- [ ] Willingness to explore multiple approaches

---

## Step 1: The Iteration Loop

```
┌─────────────────────────────────────┐
│        Iterative Solving Loop       │
├─────────────────────────────────────┤
│   1. Observe                        │
│      ↓                              │
│   2. Hypothesize                    │
│      ↓                              │
│   3. Test                           │
│      ↓                              │
│   4. Learn                          │
│      ↓                              │
│   5. Refine (or Solve!)             │
│      ↓                              │
│   ← Repeat until solved             │
└─────────────────────────────────────┘
```

---

## Step 2: Starting the Loop

### Initial Observation
```
I'm facing this problem:
[describe the issue]

Current behavior:
[what's happening]

Expected behavior:
[what should happen]

What I've tried:
[previous attempts]
```

### Example
```
Problem: API requests timeout after 30 seconds
Current: Requests hang, then fail with ETIMEDOUT
Expected: Responses return within 2 seconds
Tried: Increased timeout, checked network
```

---

## Step 3: Hypothesis Generation

### Ask Claude for Theories
```
Based on this problem, what are possible causes?
Rank them by likelihood.
```

### Structure Hypotheses
```
Claude might respond:
1. Database query is slow (70% likely)
2. Network latency issue (20% likely)
3. Memory leak causing slowdown (10% likely)

Let's test hypothesis #1 first.
```

---

## Step 4: Testing Hypotheses

### Design Tests
```
How can we test if the database query is slow?
What data would confirm or refute this hypothesis?
```

### Run Tests
```
Test 1: Add timing logs around the query
Result: Query takes 28 seconds

Hypothesis confirmed! The query is the bottleneck.
Now let's find why.
```

### Iterate Deeper
```
The query is slow. New hypotheses:
1. Missing index
2. Inefficient query plan
3. Table needs optimization

Test: Run EXPLAIN ANALYZE on the query
```

---

## Step 5: Learning from Each Iteration

### Document Findings
```
Iteration 1:
- Hypothesis: DB query slow
- Test: Added timing logs
- Result: Confirmed, 28s query time
- Learning: Problem is in the query layer

Iteration 2:
- Hypothesis: Missing index
- Test: EXPLAIN ANALYZE
- Result: Full table scan on 10M rows
- Learning: Need index on search columns
```

### Build Understanding
```
Each iteration should:
1. Narrow the problem space
2. Reveal new information
3. Guide the next hypothesis
```

---

## Step 6: Refinement Strategies

### When Hypothesis Is Wrong
```
Test showed network is fast (5ms latency).
Cross off network hypothesis.
Move to next most likely cause.
```

### When Hypothesis Is Partially Right
```
Query is slow, but indexing didn't fully fix it.
Refine: Maybe it's the query structure itself.
New test: Optimize the query, compare performance.
```

### When You're Stuck
```
I've tested these hypotheses and none fully explain the problem:
[list what you've tested]

What am I missing?
What other factors could cause this?
```

---

## Step 7: Complete Example

### The Problem
```
User: Builds take 10 minutes, should take 2 minutes
```

### Iteration 1
```
Claude: Let's hypothesize causes:
1. Large dependency installs
2. Slow test suite
3. Inefficient bundling

Test: Add build phase timing

Result:
- Install: 30s
- Tests: 8 minutes  ← Bottleneck!
- Build: 90s
```

### Iteration 2
```
Claude: Tests are slow. Sub-hypotheses:
1. Too many tests
2. Tests not parallelized
3. Slow test setup

Test: Identify slowest tests

Result: 5 tests take 6 of the 8 minutes
```

### Iteration 3
```
Claude: These 5 tests are slow because they:
- Hit real database
- Don't clean up properly

Solution: Mock database, fix cleanup

Result: Tests now run in 45 seconds!
```

---

## Iteration Templates

### For Bugs
```
Bug: [description]
Reproduction: [steps]
Hypothesis: [theory]
Test: [how to verify]
Result: [what happened]
Next: [continue or solved]
```

### For Performance
```
Symptom: [what's slow]
Measurement: [baseline numbers]
Hypothesis: [bottleneck theory]
Test: [profiling approach]
Result: [findings]
Optimization: [fix]
New measurement: [improved numbers]
```

### For Architecture
```
Challenge: [design problem]
Option A: [approach 1]
Option B: [approach 2]
Test: [prototype or analysis]
Learning: [pros/cons discovered]
Decision: [chosen approach]
```

---

## Verification Checklist

- [ ] Identified a problem to solve
- [ ] Generated multiple hypotheses
- [ ] Tested at least 3 iterations
- [ ] Documented learnings from each iteration
- [ ] Reached a solution or significantly narrowed the problem

---

## Iteration Mindset

| Instead of | Try |
|------------|-----|
| Jumping to solutions | Testing hypotheses systematically |
| Giving up after one failure | Treating failures as data |
| Random changes | Structured experiments |
| "I don't know why" | "Let's find out why" |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Jumping to solutions too fast | Force yourself to hypothesize first |
| Not documenting iterations | Keep a log of tests and results |
| Ignoring unexpected results | Unexpected = learning opportunity |
| Testing multiple things at once | Change one variable at a time |

---

## Pro Tips

1. **One Variable:** Test one thing at a time for clear results
2. **Write It Down:** Document each iteration, even failures
3. **Time Box:** Set limits on how long to pursue each hypothesis
4. **Fresh Eyes:** After 3 failed iterations, step back and reassess

---

## Next Challenge

Continue to **[Background Execution](./10-background-execution.md)** for running long tasks efficiently!
