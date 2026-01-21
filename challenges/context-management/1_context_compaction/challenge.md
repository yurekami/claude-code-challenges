# Context Compaction

## Difficulty: Medium

## Category: Context Management

## Related Tips: 8

## Description

Claude Code has a 200k token context window, but performance degrades as context fills up. Manual context compaction allows you to summarize the conversation while preserving important information, keeping your session responsive and focused.

## Objective

Learn to effectively manage context through manual compaction:
1. Identify when context compaction is needed
2. Use the /compact command with custom instructions
3. Preserve critical information while reducing token usage
4. Verify compaction preserved necessary context

## Task

You're in a long coding session where you've been debugging a complex issue. Your context is at 150k tokens. Perform the following:

1. Check your current token usage
2. Compact the context with instructions to preserve:
   - The current bug hypothesis
   - File paths that were modified
   - Test results from the last run
3. Verify the compaction worked by checking token usage again

## Expected Outcome

- Token usage should decrease significantly (target: under 50k)
- Essential debugging context should be preserved
- Session should remain functional

## Hints

1. Use /usage to check token consumption
2. The /compact command accepts natural language instructions
3. Be specific about what to preserve vs summarize

## Constraints

- Do not start a new session (that defeats the purpose)
- Ensure the compaction instructions are specific enough to preserve working context

## Submission

Submit the commands you used and the before/after token counts.
