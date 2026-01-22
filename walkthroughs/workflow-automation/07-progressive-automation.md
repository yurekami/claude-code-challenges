# Walkthrough: Progressive Automation

**Difficulty:** Hard | **Time:** 30 minutes | **Category:** Workflow Automation

---

## Overview

Don't automate everything at once. Progressive automation means starting manual, then automating pain points incrementally. This challenge teaches you to identify what to automate and when.

## Prerequisites

- [ ] Manual workflow you repeat
- [ ] Basic scripting knowledge
- [ ] Understanding of task frequency

---

## Step 1: The Automation Ladder

```
Level 0: Fully Manual
         ↓
Level 1: Documented steps
         ↓
Level 2: Helper scripts
         ↓
Level 3: Semi-automated
         ↓
Level 4: Fully automated
         ↓
Level 5: Self-improving
```

---

## Step 2: Identify Automation Candidates

### The Rule of Three
```
Did it once: Just do it
Did it twice: Make a note
Did it thrice: Time to automate
```

### Automation Priority Matrix
```
                High Frequency
                      │
        ┌─────────────┼─────────────┐
        │   AUTOMATE  │  AUTOMATE   │
        │   LATER     │  NOW!       │
Low ────┼─────────────┼─────────────┼──── High
Pain    │   SKIP      │  AUTOMATE   │     Pain
        │             │  SOON       │
        └─────────────┼─────────────┘
                      │
                Low Frequency
```

---

## Step 3: Level 1 - Document

### Before Automating, Document
```markdown
# Deploy Process

1. Run tests: `npm test`
2. Build: `npm run build`
3. Check bundle size: `npm run analyze`
4. Deploy: `npm run deploy`
5. Verify: Check https://myapp.com/health
6. Tag: `git tag v$(date +%Y%m%d)`
```

### Why Document First?
- Understand the process fully
- Identify variations
- Find pain points
- Create checklist for automation

---

## Step 4: Level 2 - Helper Scripts

### Create One-Step Helpers
```bash
#!/bin/bash
# scripts/build-and-test.sh
npm test && npm run build
```

```bash
#!/bin/bash
# scripts/quick-deploy.sh
npm run build && npm run deploy
```

### Add to package.json
```json
{
  "scripts": {
    "preflight": "npm test && npm run lint && npm run typecheck",
    "ship": "npm run preflight && npm run build && npm run deploy"
  }
}
```

---

## Step 5: Level 3 - Semi-Automated

### Add Confirmation Points
```bash
#!/bin/bash
# scripts/deploy.sh

echo "Running tests..."
npm test || exit 1

echo "Building..."
npm run build || exit 1

echo "Current version: $(cat package.json | jq -r .version)"
read -p "Deploy to production? (y/n) " confirm
if [ "$confirm" != "y" ]; then
    echo "Aborted"
    exit 0
fi

npm run deploy
```

### Human-in-the-Loop
```
Automated: Build, test, prepare
Manual: Review and approve
Automated: Deploy, verify
```

---

## Step 6: Level 4 - Fully Automated

### CI/CD Pipeline
```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm test
      - run: npm run build
      - run: npm run deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

---

## Step 7: Level 5 - Self-Improving

### Monitor and Optimize
```bash
#!/bin/bash
# Record metrics
start=$(date +%s)
npm run deploy
end=$(date +%s)
echo "$((end-start))" >> .metrics/deploy-time.log

# Alert if too slow
if [ $((end-start)) -gt 300 ]; then
    echo "Deploy took >5min, investigate!"
fi
```

### With Claude
```
Analyze our deployment script and suggest optimizations:
- Current steps and times
- Parallelization opportunities
- Caching improvements
- Unnecessary steps
```

---

## Step 8: Progressive Approach with Claude

### Step 1: Document Current Process
```
Help me document our deploy process.
I'll describe what I do, you create the checklist.
```

### Step 2: Identify Pain Points
```
Here's our deploy checklist. Which steps:
1. Are most error-prone?
2. Take the longest?
3. Are most tedious?
```

### Step 3: Create Helpers
```
Create a script that handles steps 3-5 of our deploy process.
Keep human confirmation before the risky steps.
```

### Step 4: Integrate
```
Now let's combine our scripts into a complete deploy command
that handles the full workflow.
```

---

## Verification Checklist

- [ ] Identified a manual workflow to automate
- [ ] Documented the workflow steps
- [ ] Created helper scripts for pain points
- [ ] Built semi-automated version with confirmations
- [ ] Know when to fully automate vs. keep manual

---

## Automation Decision Guide

| Frequency | Pain | Action |
|-----------|------|--------|
| Daily | Low | Simple alias |
| Daily | High | Full automation |
| Weekly | Low | Document only |
| Weekly | High | Script with confirmation |
| Monthly | Any | Document, maybe script |
| Rarely | Any | Just document |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Automated too early | Process wasn't stable |
| Automated wrong thing | Focus on frequent pain |
| Over-automated | Keep human oversight for risk |
| Script becomes unmaintainable | Keep scripts simple, documented |

---

## Pro Tips

1. **Start Manual:** Understand before automating
2. **Pain First:** Automate highest pain points
3. **Incremental:** Add automation piece by piece
4. **Measure:** Track time saved to justify investment

---

## Congratulations!

You've completed the **Workflow Automation** category! You now master:

- Terminal cascade patterns
- Git worktrees for parallel work
- Exponential backoff for polling
- CI/CD debugging
- Input navigation shortcuts
- Planning vs prototyping balance
- Progressive automation

**Next:** Move on to **[Advanced Orchestration](../advanced-orchestration/01-writing-assistant.md)** for complex workflows!
