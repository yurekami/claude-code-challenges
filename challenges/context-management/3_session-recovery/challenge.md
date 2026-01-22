# Challenge 3: Session Recovery

**Category:** Context Management
**Difficulty:** Medium
**Related Tip:** #13

## Description

Sometimes you need to recover context from previous conversations. This challenge teaches you to effectively search and extract information from conversation history stored in `~/.claude/projects/` to recover lost context or reference past work.

## Objective

Learn to navigate and search conversation history, extract relevant information, and reconstruct context from previous sessions.

## Background

Claude Code stores conversation history in `~/.claude/projects/`. Each project has a conversation history with messages, tool calls, and results. Being able to search this history is crucial for:
- Recovering from lost context
- Referencing past decisions
- Finding code snippets from previous sessions
- Understanding project evolution

## Steps to Complete

1. **Locate Conversation History**
   - Find the projects directory
   - Identify your project's conversation files
   - Understand the structure

2. **Search Effectively**
   - Use grep/ripgrep for text search
   - Search by keyword, date, or topic
   - Filter relevant conversations

3. **Extract Context**
   - Identify relevant messages
   - Reconstruct decision timeline
   - Gather code snippets

4. **Reconstruct Session State**
   - Create a recovery document
   - Summarize findings
   - Resume work with recovered context

## Success Criteria

- [ ] Successfully locate conversation history files
- [ ] Search history for specific keywords/topics
- [ ] Extract relevant context from multiple messages
- [ ] Create a context recovery document
- [ ] Resume work using recovered information

## Example Scenario

Yesterday you implemented an authentication system with Claude. Today, you can't remember:
- Why you chose JWT over sessions
- What the token expiry times were set to
- What the rate limiting configuration was

Your task: Search conversation history to recover these decisions and their rationale.

## Technical Skills Required

- Basic command line navigation
- Text search tools (grep, ripgrep, or native search)
- JSON/text file reading
- Pattern matching

## Challenges to Consider

- Conversation files may be large
- Information may be spread across multiple messages
- Need to distinguish between different topics in same conversation
- Date/time correlation
