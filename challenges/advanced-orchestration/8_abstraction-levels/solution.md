# Abstraction Levels Solution

## Choosing the Right Level

### High-Level (Vibe Coding)
**When to use:** New features, prototypes, exploration
```
"Build a user authentication system with JWT tokens, refresh tokens, and password reset."
```

### Medium-Level (Guided)
**When to use:** Most tasks, refactoring, optimization
```
"Refactor the UserService to use dependency injection. Keep the existing API but make it testable."
```

### Low-Level (Detailed)
**When to use:** Bug fixes, complex logic, critical sections
```
"In UserService.ts line 45, the password hashing uses MD5. Change it to bcrypt with a cost factor of 12."
```

## Abstraction Level Guide

| Task Type | Abstraction | Example |
|-----------|-------------|---------|
| New feature | High | "Add dark mode support" |
| Refactoring | Medium | "Extract validation into separate module" |
| Bug fix | Low | "Fix off-by-one error on line 123" |
| Optimization | Medium | "Reduce API response time" |
| Documentation | High | "Document the auth flow" |
| Testing | Medium | "Add tests for edge cases" |

## Iterative Refinement

**Start High:**
```
"Create a REST API for a blog"
```

**Review Output, Add Detail:**
```
"Good start. Now add:
- Rate limiting
- Pagination
- Search functionality"
```

**Refine Specific Parts:**
```
"The search is too slow. Optimize it using database indexes."
```

## Common Mistakes

1. **Too Vague** - "Make it better" - Claude can't read your mind
2. **Too Specific** - "Change this character here" - Inefficient use
3. **Wrong Level** - High-level for critical bugs, low-level for exploration

## Success Indicators

- Tasks complete in fewer iterations
- Less back-and-forth clarification
- Better first-attempt results
- Efficient token usage
