# Solution: System Prompt Optimization

## Step-by-Step Solution

### Step 1: Audit Current System Prompt

**Locate all system prompt sources:**

```bash
# Main project instructions
cat .claude/CLAUDE.md

# Global rules
ls -la ~/.claude/rules/
cat ~/.claude/rules/*.md

# Project-specific rules
cat .claude/rules/*.md

# Count tokens (rough estimate: chars ÷ 4)
wc -c .claude/CLAUDE.md ~/.claude/rules/*.md
```

**Create an inventory:**

```markdown
# System Prompt Inventory

## Sources
1. `.claude/CLAUDE.md` - 3,200 tokens
   - Project overview
   - Tech stack
   - Coding standards
   - Examples (lots of them)

2. `~/.claude/rules/coding-style.md` - 2,800 tokens
   - Immutability rules
   - Error handling patterns
   - Many code examples

3. `~/.claude/rules/testing.md` - 2,400 tokens
   - TDD requirements
   - Coverage requirements
   - Testing patterns

4. `~/.claude/rules/git-workflow.md` - 1,900 tokens
   - Commit messages
   - PR workflow
   - Examples

5. Other rules files - 8,700 tokens
   - Security, performance, patterns, etc.

**Total: 19,000 tokens**

## Categories
- Instructions: ~7,000 tokens
- Examples: ~8,000 tokens (42% of total!)
- Explanations: ~4,000 tokens
```

### Step 2: Identify Optimization Opportunities

#### Opportunity 1: Redundant Examples

**Before (verbose):**
```markdown
## Immutability

ALWAYS create new objects, NEVER mutate existing ones.

❌ **Wrong Example:**
```javascript
function updateUser(user, name) {
  user.name = name  // MUTATION!
  return user
}

const user = { name: 'John', age: 30 }
const updated = updateUser(user, 'Jane')
console.log(user.name)  // 'Jane' - mutated!
```

✅ **Correct Example:**
```javascript
function updateUser(user, name) {
  return {
    ...user,
    name
  }
}

const user = { name: 'John', age: 30 }
const updated = updateUser(user, 'Jane')
console.log(user.name)  // 'John' - original preserved
console.log(updated.name)  // 'Jane' - new object
```

This is important because mutation causes bugs...
[3 more paragraphs explaining why]
```

**After (concise - 78% reduction):**
```markdown
## Immutability
Create new objects, never mutate.

❌ `user.name = name`
✅ `return { ...user, name }`
```

**Savings: 250 → 55 tokens**

#### Opportunity 2: Consolidate Related Rules

**Before (scattered):**
```markdown
# In coding-style.md
- Functions should be small (<50 lines)

# In patterns.md
- Keep functions focused on single responsibility

# In refactor.md
- Break large functions into smaller ones

# In best-practices.md
- Each function should do one thing well
```

**After (consolidated):**
```markdown
# Functions
- Small (<50 lines)
- Single responsibility
- One thing well
```

**Savings: ~200 → 30 tokens**

#### Opportunity 3: Remove Obvious Information

**Before:**
```markdown
## Error Handling

It is very important to always handle errors in your code.
Unhandled errors can crash your application and create a bad
user experience. You should use try-catch blocks to catch errors
and handle them appropriately. Here are the best practices:

1. Always wrap risky operations in try-catch
2. Log errors for debugging
3. Return user-friendly messages
4. Don't expose sensitive information in errors
```

**After:**
```markdown
## Error Handling
- Try-catch risky operations
- Log errors
- User-friendly messages
- No sensitive data in errors
```

**Savings: 180 → 40 tokens**

#### Opportunity 4: Reference Instead of Repeat

**Before (repeated in multiple files):**
```markdown
# In security.md
Never hardcode API keys. Use environment variables.

# In best-practices.md
Don't commit API keys. Store them in .env files.

# In deployment.md
API keys should be in environment variables, not code.
```

**After (single source of truth):**
```markdown
# In security.md
## Secrets
Never hardcode. Use env vars. Reference: .env.example
```

**In other files:** Remove, or add one-liner: "See security.md for secrets handling"

**Savings: ~300 → 50 tokens across files**

### Step 3: Apply Compression Techniques

#### Technique 1: Bullet Points Over Paragraphs

**Before:**
```markdown
When writing commit messages, you should follow the conventional
commits format. This means starting with a type like 'feat' for
features or 'fix' for bug fixes, followed by a colon and a brief
description. The description should be in imperative mood, meaning
you should write "add feature" instead of "added feature" or
"adds feature". This helps maintain consistency across the project.
```

**After:**
```markdown
Commit format: `<type>: <description>`
- Types: feat, fix, refactor, docs, test
- Imperative mood: "add" not "added"
```

**Savings: 150 → 40 tokens**

#### Technique 2: Tables Over Lists

**Before:**
```markdown
Use Haiku 4.5 for lightweight agents with frequent invocation, as
it provides 90% of Sonnet capability at 3x cost savings.

Use Sonnet 4.5 for main development work and orchestrating multi-agent
workflows, as it's the best coding model.

Use Opus 4.5 for complex architectural decisions and maximum reasoning
requirements.
```

**After:**
```markdown
| Model | Use Case |
|-------|----------|
| Haiku 4.5 | Lightweight, frequent (90% capability, 3x savings) |
| Sonnet 4.5 | Main dev, best coding |
| Opus 4.5 | Complex decisions, max reasoning |
```

**Savings: 120 → 70 tokens (better scanability too)**

#### Technique 3: Abbreviations and Shorthand

**Before:**
```markdown
- Always validate user input before processing
- Never trust data from external sources
- Sanitize HTML to prevent XSS attacks
- Use parameterized queries to prevent SQL injection
```

**After:**
```markdown
Input: validate, never trust external, sanitize HTML (XSS), parameterized queries (SQLi)
```

**Savings: 80 → 30 tokens**

Note: Use sparingly, maintain clarity.

#### Technique 4: Remove Meta-Commentary

**Before:**
```markdown
## Testing (This is Very Important!)

It's absolutely critical that you write tests. This cannot be
stressed enough. Testing is what separates professional code from
amateur code. Let me explain why testing matters...

[2 paragraphs on importance of testing]

Here are the requirements:
- 80% coverage minimum
- Unit, integration, and E2E tests
```

**After:**
```markdown
## Testing (80% coverage required)
- Unit, integration, E2E
- TDD: test first, implement, refactor
```

**Savings: 400 → 50 tokens**

### Step 4: Real-World Optimization Example

**Original CLAUDE.md (3,200 tokens):**

```markdown
# Project: E-commerce Platform

This is an e-commerce platform built with Next.js, TypeScript, and PostgreSQL.
The project follows modern best practices and uses a microservices architecture
where appropriate.

## Technology Stack

We are using the following technologies in this project:

- **Frontend Framework**: Next.js 14 with the App Router. We chose Next.js
  because it provides excellent performance with server-side rendering and
  static generation capabilities. The App Router is the new routing system
  that provides better organization.

- **Language**: TypeScript for type safety. TypeScript helps catch errors at
  compile time rather than runtime, which improves code quality and developer
  productivity.

- **Database**: PostgreSQL for relational data. We chose PostgreSQL because
  it's mature, reliable, and provides ACID guarantees which are important for
  e-commerce transactions.

[... 2,800 more tokens of similar verbose content ...]

## Coding Standards

Please follow these coding standards when working on this project:

### Immutability

It's very important to never mutate objects. Always create new objects.

❌ **Bad Example - Don't do this:**
```javascript
function updateCart(cart, item) {
  cart.items.push(item)  // This is mutation!
  return cart
}
```

✅ **Good Example - Do this instead:**
```javascript
function updateCart(cart, item) {
  return {
    ...cart,
    items: [...cart.items, item]
  }
}
```

Why is immutability important? Because when you mutate objects, you can
introduce bugs that are hard to track down. React relies on immutability
for efficient re-rendering...

[... 500 more tokens explaining immutability ...]

### File Organization

Files should be organized by feature, not by type...

[... continues with similar verbose patterns ...]
```

**Optimized CLAUDE.md (1,200 tokens - 62% reduction):**

```markdown
# E-commerce Platform

Next.js 14 (App Router) + TypeScript + PostgreSQL

## Stack
| Tech | Why |
|------|-----|
| Next.js 14 | SSR, App Router |
| TypeScript | Type safety |
| PostgreSQL | ACID for transactions |
| Prisma | Type-safe ORM |
| Tailwind | Utility CSS |

## Patterns
**Immutability:** `return {...obj, key: val}` not `obj.key = val`
**Files:** Feature-based structure, <800 lines
**Errors:** Try-catch + log + user-friendly message
**State:** Server components default, client only when needed

## Architecture
```
app/
├── (auth)/          # Auth routes
├── (shop)/          # Public shopping
├── (admin)/         # Admin panel
└── api/             # API routes

lib/
├── db/              # Database utilities
├── auth/            # Auth helpers
└── utils/           # Shared utilities
```

## Key Constraints
- All mutations via server actions
- Client components minimal
- Auth: JWT, 15m access / 7d refresh
- Rate limit: 100 req/hr per user
- Cache: 5m TTL for product data

## Commands
- `npm run dev` - Development server
- `npm run build` - Production build
- `npm run test` - Run all tests
- `npx prisma studio` - Database GUI

## Context
- Migration from v1 monolith in progress
- Product/User APIs complete, Orders in progress
- See `docs/migration.md` for status
```

**Key optimizations applied:**
1. Table for tech stack (more scannable, fewer tokens)
2. Removed verbose explanations
3. One-line pattern examples instead of full code blocks
4. Removed obvious information
5. Visual structure instead of paragraphs
6. Reference external docs instead of repeating

**Result: 3,200 → 1,200 tokens (62% reduction)**

### Step 5: Optimize Global Rules

**Original ~/.claude/rules/coding-style.md (2,800 tokens):**

```markdown
# Coding Style

This document describes the coding style you should follow...

## Immutability (CRITICAL)

[Long explanation with multiple examples - 800 tokens]

## File Organization

[Detailed explanation with directory trees - 600 tokens]

## Error Handling

[Multiple examples and patterns - 700 tokens]

## Input Validation

[Examples with zod schemas - 500 tokens]

## Code Quality Checklist

[Detailed checklist with explanations - 200 tokens]
```

**Optimized (1,000 tokens - 64% reduction):**

```markdown
# Coding Style

## Core Rules
- **Immutable:** New objects always: `{...obj, key}` not `obj.key=`
- **Small files:** <800 lines, extract utilities
- **Errors:** Try-catch all risky ops, log + user message
- **Validate:** Zod schemas for all user input
- **Quality:** Readable names, <50 line fns, <4 nesting levels

## File Structure
Feature-based, not type-based:
```
feature/
├── component.tsx
├── hooks.ts
├── utils.ts
└── types.ts
```

## Patterns
```typescript
// Error handling
try { await op() } catch(e) { log(e); throw new Error("User msg") }

// Validation
const schema = z.object({ email: z.string().email() })
const data = schema.parse(input)

// Immutability
return { ...user, name } // not user.name = name
```

## Before Completing Task
- [ ] Readable code
- [ ] Small functions
- [ ] Proper errors
- [ ] No console.logs
- [ ] No mutations
```

### Step 6: Test Optimized Prompts

**Testing methodology:**

1. **Use optimized prompts for a session**
2. **Monitor Claude's behavior:**
   - Does it follow critical rules?
   - Does it ask for clarification more?
   - Is code quality maintained?

3. **Test specific scenarios:**
   ```markdown
   Test 1: Immutability
   Prompt: "Update the user's email in this object: {name: 'John', email: 'old@ex.com'}"
   Expected: Uses spread operator, doesn't mutate

   Test 2: Error handling
   Prompt: "Write a function to fetch user data from API"
   Expected: Includes try-catch

   Test 3: File organization
   Prompt: "Create a new feature with components, hooks, and utilities"
   Expected: Feature-based structure
   ```

4. **Compare results:**
   - Optimized prompt: Does Claude follow rules?
   - If not, identify which rules were lost
   - Restore critical missing rules
   - Re-test

**Example test:**

```markdown
Session with optimized prompts:

Me: "Create a function to update user cart"

Claude:
```typescript
function updateCart(cart: Cart, item: Item) {
  return {
    ...cart,
    items: [...cart.items, item]
  }
}
```

✅ Immutability preserved - optimization successful!
```

### Step 7: Measure and Document

**Create optimization report:**

```markdown
# System Prompt Optimization Report

## Results
**Before:** 19,000 tokens
**After:** 9,500 tokens
**Reduction:** 50% (9,500 tokens saved)

## Changes Made

### 1. Removed Redundant Examples
- Kept 1 example per concept instead of 3-5
- **Savings:** 4,200 tokens

### 2. Consolidated Rules
- Merged overlapping instructions
- **Savings:** 1,800 tokens

### 3. Compressed Explanations
- Bullet points over paragraphs
- **Savings:** 2,200 tokens

### 4. Removed Meta-Commentary
- Deleted "This is important!" type statements
- **Savings:** 1,300 tokens

## Verification
Tested with 10 common scenarios:
- ✅ Immutability rules followed
- ✅ Error handling correct
- ✅ File organization proper
- ✅ Security practices maintained
- ✅ Git workflow correct

## Critical Rules Preserved
All essential rules maintained:
- Immutability requirement
- Error handling patterns
- Security guidelines
- Testing requirements
- Git commit format

## Trade-offs
- **Lost:** Detailed explanations of "why"
- **Lost:** Multiple examples per rule
- **Lost:** Hand-holding for beginners
- **Gained:** 50% more context window
- **Gained:** Faster to read/scan
- **Gained:** Less repetition

## Recommendation
Deploy optimized prompts. Original preserved at:
- `.claude/backup/CLAUDE.md.original`
- `~/.claude/rules.backup/`
```

## Common Mistakes to Avoid

### Mistake 1: Over-Optimization

❌ **Too aggressive:**
```markdown
Rules: immut, <800line, try-catch, zod, qual
```

✅ **Right balance:**
```markdown
## Core Rules
- **Immutable:** `{...obj}` not `obj.prop=`
- **Small files:** <800 lines
- **Errors:** try-catch + log
- **Validate:** Zod schemas
- **Quality:** readable, <50 line fns
```

### Mistake 2: Losing Critical Context

❌ **Too concise:**
```markdown
JWT auth
```

✅ **Sufficient detail:**
```markdown
Auth: JWT (15m access, 7d refresh), see auth.ts
```

### Mistake 3: Removing All Examples

Sometimes examples are essential:

❌ **Too abstract:**
```markdown
Use immutable patterns
```

✅ **Concrete example:**
```markdown
Immutable: `{...obj, key}` not `obj.key=`
```

### Mistake 4: Not Testing

Always test optimization:
1. Use optimized prompt
2. Verify behavior unchanged
3. Check critical rules still followed

## Advanced Techniques

### Technique 1: Layered Prompts

Create tiers of detail:

**Tier 1: Always Loaded (minimal)**
```markdown
# Quick Ref
- Immutable: `{...obj}`
- Small files: <800
- Errors: try-catch
- Validate: Zod
```

**Tier 2: Load on Demand**
```markdown
For detailed patterns, see:
- `docs/immutability.md` - Full immutability guide
- `docs/error-handling.md` - Error patterns
```

Load Tier 2 only when needed.

### Technique 2: External References

Instead of including everything:

```markdown
## Coding Style
See `STYLE.md` for full guidelines.

**TL;DR:**
- Immutable
- Small files
- Try-catch
- Validate inputs
```

Then have Claude read `STYLE.md` only when needed.

### Technique 3: Progressive Disclosure

Start minimal, add context as needed:

```markdown
# Phase 1: Core setup
Minimal instructions here

# Phase 2: Feature development
Load additional rules when starting features

# Phase 3: Deployment
Load deployment-specific rules
```

## Token Counting Tools

### Method 1: Claude Direct
```
"Count tokens in this text: [paste]"
```

### Method 2: Estimation
```
Characters ÷ 4 ≈ Tokens (rough)
```

### Method 3: Online Tools
- OpenAI Tokenizer: platform.openai.com/tokenizer
- tiktoken library

### Method 4: CLI
```bash
# Using tiktoken (Python)
pip install tiktoken
echo "Your text" | python -c "import tiktoken; import sys; enc=tiktoken.get_encoding('cl100k_base'); print(len(enc.encode(sys.stdin.read())))"
```

## Measuring Success

Successful optimization achieves:
- ✅ 30-50% token reduction
- ✅ Critical rules still followed
- ✅ No increase in clarification questions
- ✅ Code quality maintained
- ✅ Improved readability/scanability
- ✅ More context available for actual work

## Best Practices Summary

1. **Audit first** - Know what you have before optimizing
2. **Categorize** - Separate essential from nice-to-have
3. **Remove redundancy** - One source of truth per rule
4. **Compress ruthlessly** - Bullet points, tables, shorthand
5. **Keep examples minimal** - 1 per concept, not 5
6. **Test thoroughly** - Verify behavior unchanged
7. **Document changes** - Know what was removed and why
8. **Backup originals** - Easy to restore if needed
9. **Iterate** - Optimize → test → refine
10. **Balance** - Clarity vs conciseness

## Template: Optimization Checklist

```markdown
## Optimization Checklist

### Analysis
- [ ] Inventoried all prompt sources
- [ ] Counted total tokens
- [ ] Categorized content
- [ ] Identified redundancy

### Optimization
- [ ] Removed redundant examples
- [ ] Consolidated overlapping rules
- [ ] Compressed verbose explanations
- [ ] Converted paragraphs to bullets
- [ ] Used tables where appropriate
- [ ] Removed meta-commentary
- [ ] Created external references

### Verification
- [ ] Tested critical scenarios
- [ ] Verified rule adherence
- [ ] Measured token savings
- [ ] Documented changes
- [ ] Backed up originals

### Results
- Before: [X] tokens
- After: [Y] tokens
- Reduction: [Z]%
- Rules preserved: [list]
```
