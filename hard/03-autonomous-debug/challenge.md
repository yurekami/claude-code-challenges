# Challenge: Autonomous Debug

**Difficulty:** Hard
**Category:** Multi-Agent Workflows
**Points:** 250
**Time Limit:** 60 minutes

## Description

A production bug has been reported. Your task is to use Claude Code's autonomous capabilities to find, diagnose, and fix the bug with minimal human intervention.

## The Bug Report

```
Title: Shopping cart total incorrect when discount applied
Priority: High
Reporter: QA Team

Description:
When a percentage discount is applied to the cart, the total
is sometimes calculated incorrectly. The issue seems to occur
with certain combinations of items and discount percentages.

Steps to Reproduce:
1. Add items totaling $100 to cart
2. Apply 20% discount code "SAVE20"
3. Expected total: $80
4. Actual total: $79.99 or $80.01 (varies)

Additional Info:
- Started after last week's deployment
- Affects approximately 5% of orders
- No errors in logs
```

## Objectives

1. **Investigate**: Find the source of the bug
2. **Diagnose**: Understand the root cause
3. **Reproduce**: Create a minimal test case
4. **Fix**: Implement the correct solution
5. **Verify**: Ensure the fix works
6. **Document**: Create a bug fix report

## Autonomous Workflow

You should orchestrate this using Claude Code's agent capabilities:

### Phase 1: Investigation (Use Explore Agent)
- Search for discount-related code
- Find cart calculation logic
- Identify recent changes

### Phase 2: Diagnosis (Use Oracle Agent)
- Analyze the calculation code
- Identify potential issues
- Form hypotheses

### Phase 3: Reproduction (Write Test)
- Create a failing test case
- Verify it catches the bug
- Document exact conditions

### Phase 4: Fix (Implement Solution)
- Apply minimal fix
- Ensure test passes
- Check for side effects

### Phase 5: Verification (Run Tests)
- Run full test suite
- Verify no regressions
- Check edge cases

## The Codebase

```
src/
├── cart/
│   ├── Cart.ts           # Cart class
│   ├── CartItem.ts       # Cart item model
│   ├── discount.ts       # Discount logic (BUG IS HERE)
│   └── cart.test.ts      # Existing tests
├── utils/
│   └── money.ts          # Money utilities
└── types/
    └── index.ts          # Type definitions
```

## Expected Output

### 1. Debug Report (`debug_report.md`)

```markdown
# Bug Fix Report

## Bug Summary
[One-line description]

## Root Cause Analysis
[Detailed explanation of why the bug occurred]

## Files Affected
- `src/cart/discount.ts:42` - [issue description]

## The Fix
[Description of the fix with code snippet]

## Test Coverage
- Added test: `should calculate 20% discount correctly`
- Edge cases covered: [list]

## Verification
- All tests passing: Yes
- Manual verification: Yes

## Prevention
[How to prevent similar bugs in the future]
```

### 2. The Actual Fix
Code changes committed with proper message

### 3. New Test Case
At least one new test that would have caught this bug

## Scoring

| Criteria | Points |
|----------|--------|
| Bug correctly identified | 40 |
| Root cause explained | 40 |
| Minimal, correct fix | 50 |
| Test case added | 40 |
| All tests pass | 30 |
| Report complete | 50 |

## The Actual Bug (Hidden)

The bug is a floating-point precision issue in the discount calculation:

```typescript
// BUG: Floating point precision
const discountedPrice = price * (1 - discountPercent / 100);

// FIX: Round to 2 decimal places
const discountedPrice = Math.round(price * (1 - discountPercent / 100) * 100) / 100;
```

## Agent Usage Guidelines

Use these agents strategically:

| Agent | When to Use |
|-------|------------|
| `Explore` | Finding files, searching code |
| `oracle` | Analyzing code, forming hypotheses |
| `tdd-guide` | Writing tests |
| `code-reviewer` | Reviewing fix |

## Hints

1. Floating-point arithmetic is often the culprit for "sometimes wrong" bugs
2. Look for multiplication/division with decimals
3. The test should use specific values that trigger the bug
4. `toFixed(2)` vs `Math.round()` have different behaviors

## Constraints

- Must write a test that fails before the fix
- Must not break any existing tests
- Fix must be minimal (not a refactor)
- Must document the root cause

## Verification

Run `python tests.py` to verify your debugging workflow.
