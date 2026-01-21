# Challenge: Full Feature Flow

**Difficulty:** Hard
**Category:** Advanced Workflows
**Points:** 250
**Time Limit:** 45 minutes

## Description

This challenge simulates a complete feature development workflow using Claude Code. You'll plan, implement with TDD, create tests, and submit a PR - all using best practices.

## The Feature

Implement a **Rate Limiter** utility for an API server.

### Requirements
- Limit requests per IP address
- Configurable window (default: 1 minute)
- Configurable max requests (default: 100)
- Return remaining requests in response
- Thread-safe implementation

### API
```typescript
interface RateLimiter {
  check(ip: string): RateLimitResult;
  reset(ip: string): void;
  configure(options: RateLimitOptions): void;
}

interface RateLimitResult {
  allowed: boolean;
  remaining: number;
  resetAt: Date;
}

interface RateLimitOptions {
  windowMs: number;
  maxRequests: number;
}
```

## Workflow Stages

### Stage 1: Planning (Use TodoWrite)
- Break down the implementation into tasks
- Identify edge cases
- Plan the file structure

### Stage 2: Test First (TDD)
- Write tests BEFORE implementation
- Cover: basic limiting, window reset, configuration
- Tests should fail initially (RED)

### Stage 3: Implementation
- Implement to make tests pass (GREEN)
- Keep implementation minimal
- Follow TypeScript best practices

### Stage 4: Refactor (IMPROVE)
- Clean up code
- Add JSDoc comments
- Ensure no console.logs

### Stage 5: Git & PR
- Create feature branch
- Make atomic commits
- Create PR with full description

## Scoring

| Stage | Criteria | Points |
|-------|----------|--------|
| Planning | Clear task breakdown | 30 |
| Testing | Tests written first | 40 |
| Testing | Good coverage (>80%) | 30 |
| Implementation | Correct functionality | 50 |
| Implementation | Type-safe | 20 |
| Refactor | Clean code | 20 |
| Git | Proper commits | 30 |
| PR | Complete description | 30 |

## Constraints

- Must write tests BEFORE implementation
- Must use TodoWrite to track progress
- Must create feature branch
- No external dependencies (use native APIs)
- TypeScript strict mode

## File Structure

```
src/
├── rateLimiter/
│   ├── index.ts           # Main implementation
│   ├── types.ts           # TypeScript interfaces
│   └── rateLimiter.test.ts # Tests
```

## Expected Deliverables

1. Working rate limiter implementation
2. Test file with >80% coverage
3. Feature branch with atomic commits
4. PR with description following template

## TDD Flow Reminder

```
1. RED: Write failing test
2. GREEN: Minimal code to pass
3. REFACTOR: Clean up
4. REPEAT
```

## Hints

1. Start by creating the types.ts file
2. Use `Map` for storing IP request counts
3. `Date.now()` for timestamp tracking
4. Consider sliding window vs fixed window

## Verification

Run `python tests.py` to check all stages.
