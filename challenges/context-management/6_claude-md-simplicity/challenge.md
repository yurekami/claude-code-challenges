# Challenge 6: CLAUDE.md Simplicity

**Category:** Context Management
**Difficulty:** Easy
**Related Tip:** #30

## Description

The CLAUDE.md file is loaded on every conversation and consumes valuable context window space. This challenge teaches you to keep it minimal and concise while maintaining essential project information.

## Objective

Master the art of creating lean, effective CLAUDE.md files that provide essential context without bloating the context window. Learn what to include, what to exclude, and how to reference external documentation.

## Background

Many developers fall into the trap of treating CLAUDE.md as comprehensive project documentation, including:
- Detailed API documentation
- Complete coding standards
- Extensive examples
- Historical context
- Every possible edge case

This creates massive CLAUDE.md files (5k-10k+ tokens) that eat into the context window. A well-crafted CLAUDE.md should be:
- 500-1500 tokens max
- Quick reference oriented
- Links to external docs when needed
- Updated with project evolution

## Steps to Complete

1. **Audit Existing CLAUDE.md**
   - Identify what's currently included
   - Measure token count
   - Categorize content by necessity

2. **Extract Non-Essential Content**
   - Move detailed docs to separate files
   - Create reference links
   - Keep only high-level essentials

3. **Apply Minimalist Principles**
   - One line per concept where possible
   - Tables over paragraphs
   - Links over duplication

4. **Create Documentation Structure**
   - docs/ directory for details
   - CLAUDE.md as quick reference
   - Clear navigation

## Success Criteria

- [ ] CLAUDE.md under 1500 tokens
- [ ] Contains essential project context
- [ ] No duplicated information
- [ ] Links to external docs where appropriate
- [ ] Quick to scan and understand
- [ ] Updated with current project state

## Example Scenario

You inherit a project with a 8,000 token CLAUDE.md containing:
- Full API documentation
- Complete coding style guide
- Database schema details
- Deployment procedures
- Git workflow
- Testing strategy

Your task: Reduce to <1500 tokens while maintaining usefulness.

## Key Questions

- What's truly essential for every conversation?
- What can be moved to external docs?
- How to maintain scannability?
- When to link vs inline?
- How often to update?

## Anti-Patterns to Avoid

- 📚 Encyclopedia approach (everything in CLAUDE.md)
- 🔄 Duplicating info from other files
- 📝 Detailed implementation guides in CLAUDE.md
- 🗂️ Historical context and decision logs
- 📖 Complete API references
