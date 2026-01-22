# Walkthrough: Custom CLAUDE.md

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** MCP Integrations

---

## Overview

CLAUDE.md is your persistent instruction file that shapes Claude's behavior in your projects. This challenge teaches you to craft effective custom prompts for project-specific guidance.

## Prerequisites

- [ ] Basic Claude Code usage
- [ ] Understanding of markdown
- [ ] A project to customize

---

## Step 1: Understanding CLAUDE.md Hierarchy

```
Configuration Loading Order:
1. ~/.claude/CLAUDE.md (global - all projects)
2. .claude/CLAUDE.md (project - this project only)
3. Session prompts (conversation - temporary)

Later files override earlier ones.
```

---

## Step 2: Create Your First CLAUDE.md

### Project-Level Setup
```bash
# In your project root
mkdir -p .claude
touch .claude/CLAUDE.md
```

### Basic Structure
```markdown
# [Project Name]

## Context
[One sentence about what this project is]

## Stack
[Technologies used]

## Conventions
[Project-specific rules]
```

---

## Step 3: Effective CLAUDE.md Patterns

### Pattern 1: Tech Stack Declaration
```markdown
## Stack
- Framework: Next.js 14 (App Router)
- Language: TypeScript (strict)
- Styling: Tailwind CSS
- Database: Prisma + PostgreSQL
- Auth: NextAuth.js
- Testing: Jest + Playwright
```

### Pattern 2: Folder Structure
```markdown
## Structure
```
src/
├── app/          # Next.js routes
├── components/   # React components
│   ├── ui/       # Shared UI components
│   └── features/ # Feature-specific components
├── lib/          # Utilities and helpers
├── types/        # TypeScript types
└── services/     # API and business logic
```
```

### Pattern 3: Coding Standards
```markdown
## Standards
- Components: Functional with TypeScript
- Exports: Named exports (no default exports)
- State: Zustand for global, useState for local
- API: Server Actions preferred over API routes
- Errors: Throw typed errors, catch at boundaries
```

### Pattern 4: Do/Don't Rules
```markdown
## Do
- Use `cn()` for className composition
- Colocate tests with source files
- Add loading/error states to async components

## Don't
- No `any` type
- No console.log in production code
- No inline styles
```

---

## Step 4: Project-Specific Examples

### React/Next.js Project
```markdown
# MyApp - E-commerce Platform

## Stack
Next.js 14, TypeScript, Tailwind, Prisma, Stripe

## Patterns
- Server Components default, 'use client' when needed
- API calls in lib/api.ts
- Shared types in types/index.ts

## Conventions
- Pages: src/app/(pages)/[name]/page.tsx
- Components: PascalCase.tsx
- Hooks: use[Name].ts
- Utils: camelCase.ts

## Important
- Stripe keys in env, never hardcode
- All prices in cents
- Use Prisma transactions for orders
```

### Node/Express Project
```markdown
# API Server - REST Backend

## Stack
Node 20, Express, TypeScript, PostgreSQL, Redis

## Structure
- Routes: src/routes/
- Controllers: src/controllers/
- Services: src/services/
- Models: src/models/

## Conventions
- RESTful naming: /api/v1/[resource]
- Controllers handle HTTP, services handle logic
- Zod for validation
- Custom errors extend BaseError

## Security
- Never expose internal errors
- Rate limiting on all endpoints
- JWT in httpOnly cookies
```

### Python Project
```markdown
# DataPipeline - ETL System

## Stack
Python 3.11, Pandas, SQLAlchemy, Airflow

## Conventions
- Type hints required
- Docstrings for all public functions
- pytest for testing
- Black for formatting

## Structure
- Pipelines: src/pipelines/
- Transformers: src/transformers/
- Loaders: src/loaders/

## Important
- All dates in UTC
- Log every transformation step
- Idempotent operations only
```

---

## Step 5: Global CLAUDE.md

### Create Global Config
```bash
mkdir -p ~/.claude
touch ~/.claude/CLAUDE.md
```

### Example Global Settings
```markdown
# Global Preferences

## Style
- Prefer concise responses
- Show code, then explain
- Use TypeScript when language not specified

## Behavior
- Ask before making destructive changes
- Suggest tests for new features
- Follow existing code patterns

## Tools
- Format with Prettier after edits
- Run relevant tests after changes
```

---

## Verification Checklist

- [ ] Created project-level CLAUDE.md
- [ ] Added stack and conventions
- [ ] Included project structure
- [ ] Set up global CLAUDE.md
- [ ] Verified Claude follows the instructions

---

## Testing Your CLAUDE.md

### Verification Questions
```
What tech stack are we using?
Where should I put a new component?
What's our naming convention for hooks?
```

**Claude should answer based on your CLAUDE.md.**

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Claude ignores rules | Rules may be too vague, be specific |
| Too verbose | Keep under 300 tokens |
| Contradicting rules | Review for consistency |
| Generic advice | Only include project-specific guidance |

---

## Pro Tips

1. **Start Minimal:** Begin with 5-10 lines, add as needed
2. **Test Often:** Verify Claude follows instructions
3. **Version Control:** Commit CLAUDE.md with your project
4. **Team Sharing:** Share CLAUDE.md for consistent AI behavior

---

## CLAUDE.md Template
```markdown
# [Project Name]

## Stack
[List main technologies]

## Structure
[Key directories and their purposes]

## Conventions
[3-5 most important rules]

## Important
[Critical things Claude must know]
```

---

## Next Challenge

Continue to **[Skills vs Commands](./04-skills-vs-commands.md)** to understand the difference!
