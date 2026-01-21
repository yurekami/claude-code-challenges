# Terminal Cascade Method

## Difficulty: Medium

## Category: Workflow Automation

## Related Tips: 14

## Description

The cascade method is a terminal organization pattern where new tasks open in tabs to the right, and you sweep left-to-right to check on progress. This enables efficient multitasking with Claude Code across multiple concurrent tasks.

## Objective

Set up and use the cascade method for managing multiple Claude Code tasks:
1. Organize terminal tabs for parallel work
2. Start multiple Claude Code sessions
3. Manage task switching efficiently
4. Track progress across sessions

## Task

You have three independent tasks to complete:
- Task A: Review a pull request
- Task B: Write tests for a new feature
- Task C: Debug a CI/CD failure

Set up a cascade workflow:
1. Open three terminal tabs (left to right: A, B, C)
2. Start Claude Code in each with appropriate context
3. Work on them in parallel, checking progress left-to-right
4. Document your switching pattern

## Expected Outcome

- Three organized terminal sessions
- Each session focused on its task
- Efficient switching between tasks
- Clear progress visibility

## Hints

1. Use terminal shortcuts for tab navigation (Cmd+Shift+] on Mac)
2. Start each session with context: `claude -p "Working on task X"`
3. Keep a mental model of what's running in each tab
4. Check tabs left-to-right periodically

## Constraints

- Maximum 3-4 concurrent tasks (cognitive limit)
- Each task should be independent
- Don't let context bleed between sessions

## Submission

Submit:
1. Your terminal organization approach
2. Commands used to start each session
3. Your checking/switching pattern
4. How you tracked progress
