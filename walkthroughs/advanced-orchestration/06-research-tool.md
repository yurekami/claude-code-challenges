# Walkthrough: Research Tool

**Difficulty:** Medium | **Time:** 25 minutes | **Category:** Advanced Orchestration

---

## Overview

Claude can be a powerful research assistant - gathering information, comparing options, synthesizing findings, and producing recommendations. This challenge teaches you to use Claude for deep research on any technical topic.

## Prerequisites

- [ ] Research question or topic
- [ ] Web access for Claude (or documentation sources)
- [ ] Note-taking system

---

## Step 1: Define Research Scope

### Good Research Questions
```
✅ "Compare state management options for React (Redux, Zustand, Jotai)"
✅ "What are the tradeoffs of microservices vs monolith for a 5-person team?"
✅ "How do modern bundlers (Vite, esbuild, Parcel) compare for performance?"
```

### Scoping Prompt
```
I need to research: [topic]

Help me scope this:
1. What are the key dimensions to compare?
2. What sources should we consult?
3. What's the decision criteria?
4. What's out of scope?
```

---

## Step 2: Gather Information

### Multi-Source Research
```
Research [topic] using:
1. Official documentation
2. Recent articles (2024+)
3. GitHub issues/discussions
4. Community consensus

For each source, note the date and credibility.
```

### Comparison Matrix
```
Create a comparison matrix for [options]:

Columns:
- Feature set
- Learning curve
- Performance
- Ecosystem/community
- Maintenance status
- Enterprise adoption

Use ✅/⚠️/❌ for quick scanning.
```

---

## Step 3: Deep Dive Pattern

### Layer by Layer
```
Let's research [topic] in layers:

Layer 1: Overview
- What is it?
- What problem does it solve?

Layer 2: How it works
- Core concepts
- Architecture

Layer 3: Tradeoffs
- Pros and cons
- When to use/avoid

Layer 4: Practical
- Getting started
- Common patterns
- Gotchas
```

---

## Step 4: Synthesize Findings

### Summary Structure
```
Create a research summary:

## Executive Summary
[1-2 paragraphs for decision makers]

## Detailed Analysis
[Section per option/aspect]

## Comparison
[Table or matrix]

## Recommendations
[Specific guidance based on context]

## Next Steps
[Action items]
```

---

## Step 5: Research Workflows

### Technology Evaluation
```
Evaluate [technology] for our use case:

Our context:
- Team size: X
- Current stack: Y
- Performance needs: Z

Research:
1. Does it fit our constraints?
2. What's the migration path?
3. What problems will we face?
4. What's the community like?

Recommend: adopt, evaluate further, or skip.
```

### Best Practices Research
```
Research best practices for [topic]:

1. What do experts recommend?
2. What are common mistakes?
3. What's changed recently?
4. What's debated/controversial?

Synthesize into actionable guidelines.
```

### Problem Investigation
```
Investigate: [problem we're facing]

1. What causes this problem?
2. How do others solve it?
3. What solutions exist?
4. What's the recommended approach?
```

---

## Step 6: Document Research

### Research Note Template
```markdown
# Research: [Topic]

**Date:** [Date]
**Question:** [Original research question]

## Key Findings

1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

## Options Compared

| Option | Pros | Cons | Fit |
|--------|------|------|-----|
| A | ... | ... | ⭐⭐⭐ |
| B | ... | ... | ⭐⭐ |

## Recommendation

[Clear recommendation with reasoning]

## Sources

- [Source 1]
- [Source 2]

## Open Questions

- [ ] Still need to understand...
- [ ] Should investigate...
```

---

## Step 7: Research Quality Checks

### Verify Information
```
For the key claims in this research:
1. What's the source?
2. How recent is this info?
3. Is there consensus, or is it debated?
4. Can we verify independently?
```

### Challenge Assumptions
```
Devil's advocate this research:
1. What are we assuming?
2. What would change our conclusion?
3. What are we missing?
4. What's the counterargument?
```

---

## Verification Checklist

- [ ] Scoped research question clearly
- [ ] Gathered information from multiple angles
- [ ] Created comparison matrix
- [ ] Synthesized into recommendations
- [ ] Documented research notes
- [ ] Verified key claims

---

## Research Commands

| Task | Approach |
|------|----------|
| Compare options | Comparison matrix |
| Understand deeply | Layer-by-layer |
| Make decision | Evaluate with context |
| Stay current | Recent sources only |
| Verify claims | Cross-reference |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Outdated info | Specify recent sources |
| Biased comparison | Include counterarguments |
| Information overload | Stay focused on decision |
| Unverified claims | Always fact-check |

---

## Pro Tips

1. **Scope First:** Define boundaries before diving in
2. **Decision Focus:** Research to decide, not just learn
3. **Document:** Capture findings for future reference
4. **Verify:** Cross-check important claims

---

## Next Challenge

Continue to **[Universal Interface](./07-universal-interface.md)** for Claude Code as your everything tool!
