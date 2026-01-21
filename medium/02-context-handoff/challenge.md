# Challenge: Context Handoff

**Difficulty:** Medium
**Category:** Context Management
**Points:** 150
**Time Limit:** 15 minutes

## Description

Long Claude Code sessions accumulate context. Before it becomes unwieldy, you need to create a handoff document that preserves critical information, then compact the conversation. This challenge tests session management skills.

## Objectives

1. Review the current session state
2. Create a comprehensive handoff document
3. Use `/compact` to summarize the conversation
4. Verify the handoff document captures essential information

## Handoff Document Format

```markdown
# Session Handoff

## Date
[Current date]

## Session Summary
[2-3 sentence summary of what was accomplished]

## Files Modified
- `path/to/file1.ts` - [what was changed]
- `path/to/file2.ts` - [what was changed]

## Decisions Made
1. [Key decision and rationale]
2. [Another decision]

## Outstanding Tasks
- [ ] [Task not yet completed]
- [ ] [Another pending task]

## Key Context
[Any important context the next session needs]

## Commands Used
- `/command` - [what it did]

## Notes for Next Session
[Anything important to remember]
```

## Constraints

- Handoff document must be in `handoff.md`
- Must include all sections from the format
- Must be specific, not generic
- Must use `/compact` after creating handoff

## Scenario

You've been working on adding a user authentication feature. During the session:
- You discussed OAuth vs JWT and chose JWT
- Modified `src/auth/login.ts` and `src/auth/middleware.ts`
- Decided to use bcrypt for password hashing
- Still need to implement password reset
- Used `/config` to check settings and `/usage` for tokens

## Expected Output

1. `handoff.md` file with complete handoff document
2. Evidence of using `/compact` command
3. Handoff accurately reflects the scenario above

## Scoring

| Criteria | Points |
|----------|--------|
| All sections present | 25 |
| Session summary accurate | 25 |
| Files and changes listed | 25 |
| Decisions documented | 25 |
| Outstanding tasks clear | 25 |
| Used /compact | 25 |

## Why Handoffs Matter

> "AI context is like milk; it's best served fresh and condensed"
> - ykdojo/claude-code-tips

Benefits:
- Preserves decisions and rationale
- Enables seamless session continuation
- Reduces repeated explanations
- Documents progress for review

## Hints

1. Be specific about what changed, not just "updated files"
2. Include WHY decisions were made, not just what
3. Outstanding tasks should be actionable
4. Use `/context` to see current context usage before compact

## Verification

Run `python tests.py` to check your handoff document.
