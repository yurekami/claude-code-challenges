# Research Tool Solution

## Step-by-Step Solution

### Task 1: Technology Evaluation

**Step 1: Define research parameters**
```
"I need to choose a state management solution for a React application. Research and compare:
- Redux Toolkit
- Zustand
- Jotai
- Recoil

For each, provide:
- Bundle size
- Learning curve
- Performance characteristics
- Best use cases
- Community support
- Example code"
```

**Step 2: Create comparison matrix**
```markdown
| Feature | Redux Toolkit | Zustand | Jotai | Recoil |
|---------|--------------|---------|-------|--------|
| Bundle Size | 20KB | 3KB | 5KB | 15KB |
| Learning Curve | Steep | Gentle | Gentle | Moderate |
| Boilerplate | Some | Minimal | Minimal | Moderate |
| DevTools | Excellent | Basic | Good | Good |
| Async Support | Built-in | Manual | Atoms | Built-in |
| Best For | Large apps | Simple state | Atomic state | Complex flows |
```

**Step 3: Implementation recommendation**
```
"Based on this research, which would you recommend for a mid-size e-commerce app
with moderate state complexity and a team of 5 developers with React experience?"
```

### Task 2: Best Practices Discovery

**Step 1: Search for patterns**
```
"What are the current best practices for implementing authentication in Next.js 14?
Include:
- Recommended libraries
- Security considerations
- Session management
- Common patterns
- Real-world examples from popular repos"
```

**Step 2: Verify with multiple sources**
```bash
# Search GitHub for real implementations
gh search repos "nextjs auth" --language typescript --sort stars

# Ask Claude to analyze top results
"Analyze auth implementations in these repos: [list top 5]"
```

### Task 3: Open Source Investigation

```
"I want to understand how Vercel implements their edge middleware. Help me:
1. Find the relevant code in their open-source repos
2. Explain the architecture
3. Show practical examples
4. Identify patterns I can apply"
```

### Task 4: Comprehensive Analysis

```
"Research database options for a real-time chat application handling 10k concurrent users:
- Compare PostgreSQL, MongoDB, Redis, Cassandra
- Consider read/write patterns, scaling, cost, complexity
- Provide architecture recommendations
- Show example schemas for each"
```

## Common Mistakes to Avoid

1. **Not verifying information** - Always cross-reference important findings
2. **Analysis paralysis** - Set time limits for research
3. **Missing context** - Provide specifics about your use case
4. **Not documenting** - Save findings for future reference
5. **Ignoring trade-offs** - Every solution has pros and cons

## Best Practices

1. **Start broad, then narrow**
2. **Use specific queries**
3. **Document as you go**
4. **Verify critical information**
5. **Consider your context**

## Success Indicators

- Complete thorough research efficiently
- Make informed technology decisions
- Document findings clearly
- Apply learnings to real projects
