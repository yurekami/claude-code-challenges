# Challenge 5: System Prompt Optimization

**Category:** Context Management
**Difficulty:** Hard
**Related Tip:** #15

## Description

System prompts can consume significant context window space. This challenge teaches you to optimize system prompts from verbose (19k tokens) to concise (9k tokens) while maintaining effectiveness and clarity.

## Objective

Learn to analyze, trim, and optimize system prompts and CLAUDE.md files to reduce token usage while preserving essential instructions and context.

## Background

System prompts are instructions that set Claude's behavior and context. They consume valuable context window space. Many system prompts contain:
- Redundant information
- Overly verbose explanations
- Duplicated instructions
- Unnecessary examples
- Outdated rules

Optimizing these can free up significant context for actual work.

## Steps to Complete

1. **Audit Current System Prompt**
   - Identify all sources (CLAUDE.md, ~/.claude/rules/, etc.)
   - Calculate total token count
   - Categorize content

2. **Identify Redundancy**
   - Find duplicated instructions
   - Spot overlapping rules
   - Identify contradictions

3. **Compress Without Losing Meaning**
   - Remove verbose explanations
   - Keep essential instructions
   - Use concise language
   - Consolidate related rules

4. **Test Optimized Prompt**
   - Verify behavior unchanged
   - Confirm critical instructions preserved
   - Measure token savings

## Success Criteria

- [ ] Reduce system prompt tokens by 30-50%
- [ ] Maintain critical instructions
- [ ] No loss of essential context
- [ ] Improved readability
- [ ] Documented optimization decisions

## Example Scenario

Your current system prompt stack:
- CLAUDE.md: 8,000 tokens
- ~/.claude/rules/*.md: 11,000 tokens
- Total: 19,000 tokens

Target: Reduce to 9,000 tokens (53% reduction) while maintaining effectiveness.

## Challenges to Consider

- What's essential vs nice-to-have?
- How to compress without losing nuance?
- Which examples are truly needed?
- How to handle conflicting rules?
- How to maintain readability?

## Token Counting

Use Claude to count tokens:
```
"Please count the tokens in the following text: [paste text]"
```

Or estimate: ~4 characters = 1 token (rough approximation)
