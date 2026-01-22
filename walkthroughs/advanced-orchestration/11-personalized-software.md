# Walkthrough: Personalized Software

**Difficulty:** Hard | **Time:** 30 minutes | **Category:** Advanced Orchestration

---

## Overview

Why use generic tools when Claude can build exactly what you need? Personalized software is custom-built to your specific workflow, preferences, and problems. This challenge teaches you to create bespoke tools and utilities with Claude.

## Prerequisites

- [ ] A workflow pain point to solve
- [ ] Clear understanding of your needs
- [ ] Basic programming knowledge

---

## Step 1: The Custom Tool Mindset

### Generic vs. Personalized
```
Generic Tool:
- Built for everyone
- Has features you don't need
- Missing features you do need
- Generic UI/workflow

Personalized Tool:
- Built for you
- Exactly the features you need
- Nothing extra
- Fits your workflow perfectly
```

### Examples of Personalized Software
```
- Custom CLI for your deployment workflow
- Script that formats data exactly how you need it
- Dashboard showing exactly your metrics
- Automation for your specific repetitive tasks
```

---

## Step 2: Identify Opportunities

### Find Pain Points
```
Questions to ask yourself:
1. What do I do repeatedly that feels tedious?
2. What existing tools do I wish worked differently?
3. What workflow is unique to me/my team?
4. What data do I frequently transform manually?
```

### Good Candidates for Custom Tools
```
✅ Repeated 5+ times per week
✅ Follows consistent pattern
✅ Would save significant time
✅ Generic tools don't fit

❌ One-time tasks
❌ Highly variable process
❌ Existing tools work fine
```

---

## Step 3: Describe Your Tool

### Clear Specification
```
I need a tool that:

Purpose: [what it does]

Inputs:
- [what goes in]

Outputs:
- [what comes out]

Workflow:
1. [step 1]
2. [step 2]
3. [step 3]

Example:
Input: [example input]
Output: [expected output]
```

### Example Request
```
I need a tool that:

Purpose: Convert our Jira export to weekly report format

Inputs:
- CSV export from Jira
- Week number

Outputs:
- Markdown report grouped by team member
- Summary statistics

Workflow:
1. Parse CSV
2. Group by assignee
3. Format as markdown
4. Add summary section

Example:
Input: jira-export-2024-01-15.csv, week 3
Output: weekly-report-w3.md with formatted issues
```

---

## Step 4: Iterative Development

### Start Simple
```
Build version 1:
- Core functionality only
- No error handling
- Basic output

Let's test it and iterate.
```

### Add Features Incrementally
```
Version 2: Add error handling
Version 3: Add configuration options
Version 4: Add better formatting
Version 5: Add edge case handling
```

### Get It Working First
```
"Make it work, make it right, make it fast"

1. Working prototype (ugly is okay)
2. Clean up and improve
3. Optimize if needed
```

---

## Step 5: Types of Custom Tools

### CLI Tools
```
Create a CLI tool called 'proj' that:
- proj new <name>    → Create project from template
- proj deploy        → Deploy to staging
- proj status        → Show all service statuses
- proj logs <svc>    → Tail service logs

Use my preferred stack and deployment target.
```

### Data Transformers
```
Create a script that:
- Reads our analytics JSON export
- Calculates the metrics we actually care about
- Outputs a clean summary table
- Saves to our reports folder
```

### Workflow Automators
```
Create an automation that:
- Watches for new PRs in our repos
- Runs our custom validation checks
- Posts results as PR comments
- Notifies relevant team members
```

---

## Step 6: Personalization Details

### Preferences to Specify
```
When building my tools, always:
- Use TypeScript over JavaScript
- Use pnpm not npm
- Follow our team's naming conventions
- Output in our preferred formats
- Match our directory structure
```

### Workflow Integration
```
This tool should integrate with:
- Our existing config at ~/.mycompany/config.json
- Our deployment scripts in /scripts
- Our logging to DataDog
- Our alerts to Slack
```

### Error Handling Style
```
On errors:
- Log to our standard format
- Send to our error tracking
- Exit with meaningful codes
- Show helpful recovery messages
```

---

## Step 7: Maintenance and Evolution

### Keep Tools Updated
```
My custom tool needs an update:
- Add support for new field 'priority'
- Change output format to include totals
- Fix the edge case when input is empty
```

### Document for Yourself
```
Add a simple README that explains:
- What this tool does
- How to run it
- What the options are
- Examples of common uses
```

### Share (Optionally)
```
This tool might be useful to others.
Generalize it slightly:
- Make hardcoded values configurable
- Add input validation
- Improve error messages
- Create proper documentation
```

---

## Example: Complete Custom Tool

### The Request
```
I need a tool to prepare my daily standup.

It should:
1. Fetch my GitHub activity from yesterday
2. Check my calendar for today
3. Pull my Jira assigned tasks
4. Format into standup template:
   - What I did yesterday
   - What I'm doing today
   - Any blockers

Output to clipboard ready to paste.
```

### Claude Builds
```javascript
#!/usr/bin/env node
// standup.js - Daily standup preparation

const { execSync } = require('child_process');

async function generateStandup() {
  const yesterday = await getGitHubActivity();
  const today = await getCalendar();
  const tasks = await getJiraTasks();

  const standup = formatStandup(yesterday, today, tasks);
  copyToClipboard(standup);

  console.log('Standup ready! Pasted to clipboard.');
}

generateStandup();
```

### Usage
```bash
# Every morning
standup

# Output in clipboard:
# Yesterday: Merged PR #123, reviewed PR #124
# Today: Finish feature X, team meeting at 2pm
# Blockers: Waiting on API spec from backend team
```

---

## Verification Checklist

- [ ] Identified a workflow pain point
- [ ] Wrote clear specification for custom tool
- [ ] Built working version with Claude
- [ ] Iterated to improve the tool
- [ ] Integrated into daily workflow

---

## Tool Ideas by Category

| Category | Example |
|----------|---------|
| Reports | Weekly summary generator |
| Data | CSV transformer for your format |
| Deployment | Custom deploy command |
| Communication | Standup/status formatters |
| Organization | Project scaffolding |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Over-engineering | Start minimal, add features as needed |
| Under-specifying | Give concrete examples |
| Not testing | Try with real data early |
| Forgetting edge cases | Add them in iterations |

---

## Pro Tips

1. **Solve Real Pain:** Build tools for problems you actually have
2. **Start Small:** One function, working, is better than many broken
3. **Iterate Fast:** Get feedback, improve, repeat
4. **Make It Yours:** Don't compromise on your workflow

---

## Next Challenge

Continue to **[Code Simplification](./12-code-simplification.md)** for making complex code simple!
