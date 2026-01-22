# Walkthrough: Output Verification

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** Testing & Verification

---

## Overview

Claude generates code, but how do you verify it works? This challenge teaches systematic approaches to verifying Claude's output - from quick checks to comprehensive validation.

## Prerequisites

- [ ] Working development environment
- [ ] Test framework available
- [ ] Code Claude has generated

---

## Step 1: The Verification Mindset

### Trust but Verify
```
Claude's code may:
✅ Work perfectly
⚠️  Work with edge case issues
❌ Have subtle bugs
❌ Not compile/run

Always verify before committing!
```

---

## Step 2: Quick Verification Checks

### Level 1: Syntax Check
```bash
# TypeScript
npx tsc --noEmit

# Python
python -m py_compile file.py

# JavaScript
node --check file.js
```

### Level 2: Lint Check
```bash
# ESLint
npx eslint file.ts

# Pylint
pylint file.py

# Prettier (format check)
npx prettier --check file.ts
```

### Level 3: Type Check
```bash
# TypeScript strict
npx tsc --strict --noEmit

# Python with mypy
mypy file.py --strict
```

---

## Step 3: Runtime Verification

### Run the Code
```
Ask Claude: "Now run this code and show me the output"
```

### Test with Sample Input
```
Test the function with these inputs:
- Normal case: [example]
- Edge case: [example]
- Invalid input: [example]
```

### Interactive Testing
```
Create a quick test script that exercises the main functionality:
- Call function with test data
- Print results
- Verify expected output
```

---

## Step 4: Verification Patterns

### Pattern A: Test-First Verification
```
Before implementing:
1. Write test cases
2. Have Claude implement
3. Run tests
4. Fix failures
```

### Pattern B: Post-Implementation Tests
```
After implementing:
1. Review code visually
2. Ask Claude to write tests
3. Run tests
4. Add edge case tests
5. Fix any failures
```

### Pattern C: Manual + Automated
```
1. Quick manual test (happy path)
2. Run automated test suite
3. Manual edge case testing
4. Performance check if needed
```

---

## Step 5: Systematic Verification Checklist

### Functionality
```
- [ ] Main feature works
- [ ] All code paths tested
- [ ] Edge cases handled
- [ ] Error cases handled
```

### Code Quality
```
- [ ] No syntax errors
- [ ] No type errors
- [ ] Linting passes
- [ ] No console.log/print statements
```

### Integration
```
- [ ] Works with existing code
- [ ] No breaking changes
- [ ] APIs match expectations
- [ ] Data formats correct
```

---

## Step 6: Verification Commands

### Run Full Verification Suite
```
After implementing, run these verification steps:

1. Type check: npm run typecheck
2. Lint: npm run lint
3. Unit tests: npm test
4. Build: npm run build

Report any failures.
```

### Quick Verification Script
Create a `verify.sh`:
```bash
#!/bin/bash
set -e

echo "🔍 Type checking..."
npx tsc --noEmit

echo "📝 Linting..."
npx eslint . --ext .ts,.tsx

echo "🧪 Testing..."
npm test

echo "🏗️  Building..."
npm run build

echo "✅ All verification passed!"
```

---

## Step 7: Handling Verification Failures

### When Tests Fail
```
The test for [function] failed with:
Expected: [expected]
Actual: [actual]

Fix the implementation to match the expected behavior.
```

### When Types Fail
```
Getting TypeScript error:
[error message]

Fix the type issue while maintaining functionality.
```

### When Build Fails
```
Build error:
[error message]

Diagnose and fix the build issue.
```

---

## Verification Checklist

- [ ] Ran syntax/type checks
- [ ] Ran linting
- [ ] Executed unit tests
- [ ] Tested manually with sample input
- [ ] Verified edge cases
- [ ] Confirmed build succeeds

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Tests pass, production breaks | Add integration tests |
| Edge case missed | Ask Claude for edge cases |
| Type errors at runtime | Enable strict TypeScript |
| Silent failures | Add error logging |

---

## Pro Tips

1. **Automate:** Create scripts for verification steps
2. **CI Integration:** Run verification on every commit
3. **Edge Cases:** Always test boundaries and nulls
4. **Error Paths:** Test what happens when things fail

---

## Next Challenge

Continue to **[Git Bisect Debug](./03-git-bisect-debug.md)** to find breaking commits!
