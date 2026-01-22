# Walkthrough: Knowledge Sharing

**Difficulty:** Easy | **Time:** 10 minutes | **Category:** Advanced Orchestration

---

## Overview

Knowledge trapped in one person's head doesn't scale. Claude can help you document, explain, and share what you know with others. This challenge teaches you to create effective knowledge transfer materials.

## Prerequisites

- [ ] Knowledge worth sharing
- [ ] Target audience in mind
- [ ] Platform for sharing (docs, wiki, etc.)

---

## Step 1: Why Share Knowledge?

### The Bus Factor
```
Bus Factor = 1
→ Only you know how this works
→ You're a bottleneck
→ Team can't function without you
→ You can't take vacation

Bus Factor = Team
→ Everyone understands the system
→ Work continues smoothly
→ Faster onboarding
→ Better collaboration
```

---

## Step 2: Types of Knowledge to Share

### Tacit Knowledge
```
Things you know but haven't documented:
- "Always restart the cache after deploys"
- "The API returns 200 even on errors, check the body"
- "This config file is actually in the old repo"
```

### Decision Context
```
Why things are the way they are:
- "We use X because Y didn't work for Z reason"
- "This workaround is for a bug in library version N"
- "We chose this architecture because of constraint C"
```

### Process Knowledge
```
How to do things:
- Deployment procedures
- Debugging workflows
- Setup instructions
- Troubleshooting guides
```

---

## Step 3: Creating Documentation

### Have Claude Help
```
I need to document [topic] for new team members.

Audience: Junior developers
Their context: They know [X], don't know [Y]

Create documentation that includes:
- Overview (what and why)
- Key concepts
- Step-by-step guide
- Common issues and solutions
- Where to get help
```

### Example
```
Document our deployment process:

Audience: Any developer on the team
Context: They have repo access, basic CLI skills

Cover:
- What happens during deployment
- How to deploy to staging/production
- How to rollback
- Common deployment issues
```

---

## Step 4: Explaining Complex Concepts

### Layer the Explanation
```
Explain [complex topic] at three levels:

Level 1 (5 seconds): One-sentence summary
Level 2 (30 seconds): Core concepts
Level 3 (5 minutes): Full explanation with examples
```

### Use Analogies
```
Explain [technical concept] using an analogy
that someone without technical background would understand.
```

### Create Visuals
```
Create an ASCII diagram that explains
how our authentication flow works.
```

---

## Step 5: Documentation Formats

### README Template
```markdown
# Project Name

One-line description.

## Quick Start

```bash
npm install
npm start
```

## Overview

What this project does and why.

## Architecture

Key components and how they connect.

## Development

How to set up and run locally.

## Deployment

How to deploy to production.

## Troubleshooting

Common issues and solutions.
```

### How-To Guide Template
```markdown
# How to [Task]

## Prerequisites

- [ ] What you need before starting

## Steps

1. First step with explanation
2. Second step with explanation
3. Third step with explanation

## Verification

How to confirm it worked.

## Troubleshooting

What to do if it doesn't work.
```

### ADR Template (Architecture Decision Record)
```markdown
# ADR-001: [Decision Title]

## Status

Accepted | Proposed | Deprecated

## Context

What situation led to this decision.

## Decision

What we decided to do.

## Consequences

What happens as a result of this decision.
```

---

## Step 6: Making Knowledge Findable

### Organize by Task
```
Instead of:
- technical-documentation.md
- api-docs.md
- misc-notes.md

Use:
- how-to-deploy.md
- how-to-debug-api.md
- how-to-add-new-endpoint.md
```

### Link Related Docs
```
Always add "See also" sections:

## See Also

- [Related Guide 1](link)
- [Related Guide 2](link)
- [Troubleshooting](link)
```

---

## Step 7: Keeping Knowledge Fresh

### Review Regularly
```
Add to your calendar:
- Monthly: Review recent doc changes
- Quarterly: Update stale documentation
- After incidents: Document learnings
```

### Make Updates Easy
```
When you fix something undocumented:
1. Fix the issue
2. Document the solution
3. Link from relevant places

Small, continuous updates > big documentation projects
```

### Encourage Contributions
```
When someone asks a question:
1. Answer them
2. Ask: "Would you document this for others?"
3. Review their doc
4. Merge

Asker becomes documenter.
```

---

## Verification Checklist

- [ ] Identified knowledge worth sharing
- [ ] Created at least one piece of documentation
- [ ] Organized it to be findable
- [ ] Shared with at least one person
- [ ] Got feedback and improved

---

## Knowledge Sharing Prompts

| Task | Prompt |
|------|--------|
| New docs | "Document [topic] for [audience]" |
| Explain | "Explain [concept] at three levels" |
| Troubleshoot | "Create troubleshooting guide for [issue]" |
| Onboard | "Write onboarding doc for new [role]" |
| Decision | "Document why we chose [decision]" |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Too technical | Know your audience, add context |
| Too long | Start with summary, details after |
| Out of date | Update when things change |
| Hard to find | Organize by task, add links |

---

## Pro Tips

1. **Start Now:** Imperfect docs today beat perfect docs never
2. **Audience First:** Write for who will read it
3. **Examples:** Show don't tell
4. **Update Often:** Small updates are easier than big rewrites

---

## The Knowledge Flywheel

```
Document → Share → Get Feedback → Improve → Document more
    ↑                                              |
    └──────────────────────────────────────────────┘
```

The more you share, the easier it becomes, and the more valuable it is.

---

## Congratulations!

You've completed the **Advanced Orchestration** track!

You've learned to:
- Use Claude as a writing assistant
- Master Markdown for documentation
- Create container sandboxes
- Learn by doing
- Conduct interactive PR reviews
- Use Claude as a research tool
- Build universal interfaces
- Work at the right abstraction level
- Solve problems iteratively
- Run background tasks
- Build personalized software
- Simplify complex code
- Share knowledge effectively

---

## What's Next?

Return to the challenge dashboard to explore other tracks or revisit challenges you want to master further.
