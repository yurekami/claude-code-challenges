# Walkthrough: CLAUDE.md Simplicity

**Difficulty:** Easy | **Time:** 12 minutes | **Category:** Context Management

---

## Overview

A simple CLAUDE.md beats a complex one. This challenge focuses on the philosophy and practice of keeping your Claude configuration minimal, focused, and effective. Less is more when it comes to AI instructions.

## Prerequisites

- [ ] Basic understanding of CLAUDE.md
- [ ] Completed system prompt optimization
- [ ] A project with existing CLAUDE.md (or create one)

---

## Step 1: The Simplicity Principle

### Why Simple Wins
```
Complex CLAUDE.md:
- More tokens consumed
- More rules to conflict
- More for Claude to misinterpret
- Harder to maintain

Simple CLAUDE.md:
- Minimal token overhead
- Clear, unambiguous guidance
- Easy to update
- Consistent behavior
```

### The Golden Rule
> If Claude would do it correctly without the instruction, don't include it.

---

## Step 2: What Doesn't Belong in CLAUDE.md

### Remove These:
```markdown
# ❌ Generic programming advice
"Use meaningful variable names"
"Write clean code"
"Handle errors properly"
# Claude knows this already

# ❌ Language documentation
"In TypeScript, interfaces define contracts..."
# Claude knows TypeScript

# ❌ Obvious behaviors
"Save files after editing"
"Test code before committing"
# Claude does this naturally

# ❌ Lengthy explanations
"We use Redux because it provides..."
# Just say "Uses Redux"
```

### Keep These:
```markdown
# ✅ Project-specific conventions
"API endpoints in src/api/, not src/services/"

# ✅ Non-obvious decisions
"Use date-fns (not moment.js) for dates"

# ✅ Team standards that differ from defaults
"Tabs, not spaces (team preference)"

# ✅ Critical warnings
"Never commit .env files"
```

---

## Step 3: The Ideal CLAUDE.md

### Structure (Maximum)
```markdown
# [Project Name]

## Stack
[3-5 items]

## Conventions
[3-5 bullet points]

## Don't
[2-3 critical warnings]
```

### Example: E-commerce App
```markdown
# ShopApp

## Stack
React 18, TypeScript, Tailwind, Zustand, Supabase

## Conventions
- Components: src/components/[Feature]/
- API calls: src/lib/api.ts
- Types: colocate with components
- Tests: *.test.tsx beside source

## Don't
- No console.log in commits
- No any type
- No inline styles
```

**Total: ~60 tokens**

---

## Step 4: Simplicity Audit

### Audit Your Current CLAUDE.md

Score each line:
- **Essential (Keep):** Would Claude get it wrong without this?
- **Nice-to-have (Maybe):** Slightly helpful but not critical
- **Obvious (Remove):** Claude would do this anyway

### Example Audit
```markdown
# Before audit
"Always use TypeScript strict mode" ← Essential (config-specific)
"Write descriptive variable names" ← Obvious (remove)
"Components in src/components" ← Essential (project structure)
"Use React hooks properly" ← Obvious (remove)
"Format code consistently" ← Obvious (remove)
"API types in src/types/api.ts" ← Essential (project-specific)
```

### After Audit
```markdown
# After audit (kept only essentials)
- TypeScript strict mode
- Components: src/components/
- API types: src/types/api.ts
```

---

## Step 5: The Minimal Viable CLAUDE.md

### For a New Project
```markdown
# [Name] - [One line description]

Stack: [comma-separated list]
```

**That's it.** Add more only when Claude gets something wrong.

### Evolution Pattern
```
Week 1: Stack only (10 tokens)
Week 2: Add convention Claude violated (20 tokens)
Week 3: Add specific warning needed (30 tokens)
...
Never exceed 150 tokens
```

---

## Step 6: Hierarchy of CLAUDE.md Files

### Global (~/.claude/CLAUDE.md)
```markdown
# Global Preferences
- Concise responses
- Show code, not explanations
- TypeScript preferred
```

### Project (.claude/CLAUDE.md)
```markdown
# ProjectName
Stack: React, Node
Structure: feature-based folders
```

### Combine Effect
Global settings apply everywhere, project overrides for specifics.

---

## Verification Checklist

- [ ] CLAUDE.md is under 100 tokens
- [ ] Every line is project-specific (not generic)
- [ ] No explanatory paragraphs
- [ ] No redundant instructions
- [ ] Tested that Claude still works correctly

---

## Simplicity Test

Ask yourself for each line:

1. **Is this project-specific?**
   - No → Remove it

2. **Would Claude get it wrong without this?**
   - No → Remove it

3. **Is this the shortest way to say it?**
   - No → Shorten it

4. **Can this be combined with another line?**
   - Yes → Combine them

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Claude ignores rules | Rule might be too vague, make specific |
| Too minimal, lost context | Add back one critical item at a time |
| Rules conflict | Simplify to remove ambiguity |
| Forgot project conventions | Add them when you notice issues |

---

## Anti-Patterns to Avoid

### The Novel
```markdown
❌ This is a comprehensive guide to working with our codebase.
We believe in clean code principles and follow industry best
practices. Our team values collaboration and clear communication...
[500 more words]
```

### The Rulebook
```markdown
❌ Rule 1: Always...
Rule 2: Never...
Rule 3: Ensure...
[50 more rules]
```

### The Tutorial
```markdown
❌ TypeScript is a typed superset of JavaScript...
[Explanation of TypeScript]
```

---

## Pro Tips

1. **Start Empty:** Begin with no CLAUDE.md, add only when needed
2. **One Issue, One Line:** Each correction = one concise line
3. **Review Monthly:** Remove lines that haven't been relevant
4. **Project-Only:** Global CLAUDE.md should be nearly empty

---

## Congratulations!

You've completed the **Context Management** category! You now master:

- Context compaction
- Handoff documents
- Session recovery
- Fork strategies
- System prompt optimization
- CLAUDE.md simplicity

**Next:** Move on to **[MCP Integrations](../mcp-integrations/01-mcp-server-setup.md)** to extend Claude's capabilities!
