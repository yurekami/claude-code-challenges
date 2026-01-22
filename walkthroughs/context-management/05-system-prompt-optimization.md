# Walkthrough: System Prompt Optimization

**Difficulty:** Hard | **Time:** 25 minutes | **Category:** Context Management

---

## Overview

Every Claude session starts with a system prompt that consumes tokens. Large CLAUDE.md files, verbose instructions, and redundant MCP tool descriptions eat into your 200k token budget. This challenge teaches you to optimize your system prompt for minimal overhead.

## Prerequisites

- [ ] Understanding of CLAUDE.md files
- [ ] Access to Claude configuration
- [ ] Knowledge of token counting

---

## Step 1: Measure Current Overhead

### Check System Prompt Size
```
/stats
```

Look for "System prompt tokens" or similar metric.

### Estimate CLAUDE.md Impact
```bash
# Count tokens in your CLAUDE.md
wc -w ~/.claude/CLAUDE.md
# Rough estimate: words × 1.3 ≈ tokens
```

### Identify All Contributing Sources
```
System Prompt Components:
├── Base Claude instructions (fixed)
├── ~/.claude/CLAUDE.md (user global)
├── .claude/CLAUDE.md (project local)
├── MCP tool descriptions
└── Active skill prompts
```

---

## Step 2: Audit Your CLAUDE.md

### Before Optimization
```markdown
# My CLAUDE.md (Before - 2500 tokens)

## About This Project
This project is a web application built with React and TypeScript.
We use Redux for state management because it provides predictable
state updates and makes debugging easier. The application connects
to a REST API backend built with Node.js and Express...

[500 more words of background]

## Coding Standards
When writing code, always use descriptive variable names that
clearly indicate the purpose of the variable. For example, instead
of using 'x' or 'temp', use names like 'userAccountBalance' or
'temporaryStorageBuffer'. This makes the code more readable...

[300 more words of explanation]

## Error Handling
Always wrap async operations in try-catch blocks. When catching
errors, log them appropriately and provide user-friendly messages.
Never expose internal error details to users as this could be a
security risk...

[200 more words]
```

### After Optimization
```markdown
# Project: React/TS Web App + Node/Express API

## Stack
- Frontend: React 18, TypeScript, Redux Toolkit
- Backend: Node.js, Express, PostgreSQL
- Testing: Jest, React Testing Library

## Standards
- Descriptive variable names (not x, temp)
- Try-catch for async operations
- No internal errors exposed to users
- JSDoc for public functions

## Patterns
- Functional components with hooks
- API calls in services/ directory
- Feature-based folder structure
```

**Result:** 2500 tokens → 150 tokens

---

## Step 3: Apply Optimization Techniques

### Technique 1: Use Bullet Points
```markdown
# Before (verbose)
When working with the database, always use parameterized queries
to prevent SQL injection attacks. Make sure to validate all input
before passing it to the database layer.

# After (concise)
## Database
- Use parameterized queries (no string concat)
- Validate input before DB layer
```

### Technique 2: Remove Explanations
```markdown
# Before (explains why)
We use TypeScript strict mode because it catches more errors
at compile time and provides better type safety.

# After (just the rule)
## Config
- TypeScript strict mode: ON
```

### Technique 3: Consolidate Redundancy
```markdown
# Before (repetitive)
- Use consistent naming for components
- Use consistent naming for functions
- Use consistent naming for variables
- Use consistent naming for files

# After (consolidated)
- Consistent naming: PascalCase components, camelCase functions/vars
```

### Technique 4: Reference External Docs
```markdown
# Before (inline docs)
[100 lines of API documentation]

# After (reference)
## Docs
- API spec: docs/api.md
- Architecture: docs/architecture.md
```

---

## Step 4: Optimize MCP Tool Descriptions

### Review Active MCP Servers
```
/mcp
```

### Disable Unused Servers
Edit `~/.claude/settings.json`:
```json
{
  "mcpServers": {
    "filesystem": { "enabled": true },
    "github": { "enabled": true },
    "postgres": { "enabled": false },  // Disable if not using
    "unused-tool": { "enabled": false }
  }
}
```

### Reduce Tool Verbosity
Some MCP servers have verbose descriptions. Check if alternatives exist with leaner prompts.

---

## Step 5: Create Minimal CLAUDE.md Templates

### Minimal Template (50 tokens)
```markdown
Stack: React/TS, Node/Express, PostgreSQL
Style: Functional, TypeScript strict, Jest tests
```

### Standard Template (150 tokens)
```markdown
# [Project Name]

## Stack
[One line per tech]

## Standards
[3-5 bullet points]

## Patterns
[2-3 key patterns]
```

### Comprehensive Template (300 tokens max)
```markdown
# [Project Name]

## Overview
[One sentence]

## Stack & Tools
[Categorized list]

## Standards
[Essential rules only]

## Patterns
[Key patterns]

## Gotchas
[Non-obvious things]
```

---

## Step 6: Measure Improvement

### Before/After Comparison
```
/usage
```

Compare "System prompt" token count before and after optimization.

### Calculate Savings
```
Before: 2500 tokens
After: 150 tokens
Savings: 2350 tokens (94% reduction!)

Context available: 200,000 - 150 = 199,850 tokens
vs. previously: 200,000 - 2500 = 197,500 tokens
```

---

## Verification Checklist

- [ ] Measured current system prompt size
- [ ] Identified all contributing sources
- [ ] Reduced CLAUDE.md by 50%+ tokens
- [ ] Removed unnecessary MCP servers
- [ ] Verified Claude still understands project context
- [ ] Created reusable minimal template

---

## Optimization Checklist for CLAUDE.md

- [ ] No paragraphs (use bullets)
- [ ] No explanations (just rules)
- [ ] No redundancy (consolidated)
- [ ] No inline documentation (use references)
- [ ] No examples unless essential
- [ ] Under 300 tokens total

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Too aggressive | Keep essential context |
| Claude forgets rules | Rules might have been needed |
| Different behavior | Test after each optimization |
| Lost project context | Keep critical architecture notes |

---

## Pro Tips

1. **Test Each Change:** Verify Claude still works after each reduction
2. **Project-Specific:** Keep global minimal, put detail in project CLAUDE.md
3. **Seasonal Cleanup:** Revisit CLAUDE.md monthly for cleanup
4. **Measure ROI:** Track if shorter prompts improve or degrade quality

---

## Next Challenge

Continue to **[CLAUDE.md Simplicity](./06-claude-md-simplicity.md)** to keep your config minimal!
