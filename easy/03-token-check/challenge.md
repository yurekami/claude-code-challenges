# Challenge: Token Check

**Difficulty:** Easy
**Category:** Context Management
**Points:** 100
**Time Limit:** 5 minutes

## Description

Understanding token usage is crucial for efficient Claude Code sessions. Your task is to monitor and report on your token consumption using Claude Code's built-in commands.

## Objectives

1. Check your current token usage using `/usage`
2. Check session statistics using `/stats`
3. Report the current context usage percentage
4. Demonstrate understanding of when to use `/compact`

## The Commands

| Command | Purpose |
|---------|---------|
| `/usage` | View current session token consumption |
| `/stats` | View detailed statistics and activity |
| `/compact` | Summarize and reduce context |
| `/context` | Display current context information |

## Constraints

- Use only Claude Code slash commands
- Report accurate numbers from YOUR session
- Explain when compaction would be beneficial

## Expected Output

Create a file `usage_report.md` with:

```markdown
# Token Usage Report

## Current Session
- Input tokens used: [number]
- Output tokens used: [number]
- Total tokens: [number]
- Context window usage: [percentage]%

## Recommendations
- Should compact now: [Yes/No]
- Reason: [explanation]

## When to Compact
[Your explanation of when /compact is useful]
```

## Examples

### Checking Usage
```
User: /usage
Claude: [Shows token statistics]
```

### Good Report Entry
```markdown
## Recommendations
- Should compact now: No
- Reason: Context usage is at 15%, well below the 80% threshold
```

## Scoring

| Criteria | Points |
|----------|--------|
| Accurate token counts | 30 |
| Context percentage reported | 20 |
| Compaction recommendation correct | 25 |
| Clear explanation of /compact usage | 25 |

## Hints

1. Run `/usage` first to see your current stats
2. Context above 80% suggests compaction
3. `/compact` creates a summary and frees context space
4. Long conversations benefit from periodic compaction

## Knowledge Check

When should you use `/compact`?
- Before starting a new major task
- When context exceeds 70-80%
- When switching topics completely
- When you notice slower responses

## Verification

Run `python tests.py` to check your report.
