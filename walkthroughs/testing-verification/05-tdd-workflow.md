# Walkthrough: TDD Workflow

**Difficulty:** Medium | **Time:** 25 minutes | **Category:** Testing & Verification

---

## Overview

Test-Driven Development (TDD) means writing tests BEFORE implementation. This challenge teaches you the Red-Green-Refactor cycle with Claude, ensuring high test coverage and quality code.

## Prerequisites

- [ ] Testing framework installed (Jest, pytest, etc.)
- [ ] Understanding of unit testing
- [ ] Feature or function to implement

---

## Step 1: The TDD Cycle

### Red → Green → Refactor

```
┌─────────────────────────────────────────────────┐
│                    TDD Cycle                     │
├─────────────────────────────────────────────────┤
│  🔴 RED                                          │
│     Write a failing test                        │
│              ↓                                   │
│  🟢 GREEN                                        │
│     Write minimal code to pass                  │
│              ↓                                   │
│  🔵 REFACTOR                                     │
│     Improve code, tests stay green              │
│              ↓                                   │
│     ← Back to RED for next test                 │
└─────────────────────────────────────────────────┘
```

---

## Step 2: RED - Write Failing Test First

### Tell Claude the Pattern
```
We're using TDD. Write the test FIRST, before any implementation.

Feature: Calculate the total price of items in a cart

Write a failing test for this functionality.
```

### Claude Writes Test
```typescript
// cart.test.ts
describe('calculateTotal', () => {
  it('should return 0 for empty cart', () => {
    expect(calculateTotal([])).toBe(0);
  });

  it('should sum item prices', () => {
    const items = [
      { name: 'Apple', price: 1.50 },
      { name: 'Banana', price: 0.75 }
    ];
    expect(calculateTotal(items)).toBe(2.25);
  });
});
```

### Run Test (Should Fail)
```bash
npm test

# Expected: FAIL - calculateTotal is not defined
```

---

## Step 3: GREEN - Minimal Implementation

### Write Just Enough Code
```
Now write the MINIMAL code to make these tests pass.
Don't over-engineer - just make the tests green.
```

### Claude Implements
```typescript
// cart.ts
interface CartItem {
  name: string;
  price: number;
}

function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

### Run Tests Again
```bash
npm test

# Expected: PASS
```

---

## Step 4: REFACTOR - Improve While Green

### Clean Up the Code
```
Tests pass. Now refactor if needed:
- Improve naming
- Extract helpers
- Add types
- Optimize

Keep running tests after each change!
```

### Verify Tests Still Pass
```bash
npm test  # After each refactor step

# Must stay: PASS
```

---

## Step 5: Add More Tests (Next Red)

### Continue the Cycle
```
Add tests for:
- Quantity support
- Discount codes
- Tax calculation

Remember: Write tests FIRST!
```

### New Failing Test
```typescript
it('should apply quantity multiplier', () => {
  const items = [
    { name: 'Apple', price: 1.00, quantity: 3 }
  ];
  expect(calculateTotal(items)).toBe(3.00);
});
```

---

## Step 6: Edge Cases and Error Handling

### Test Edge Cases
```
Write tests for edge cases:
- Negative prices (should error)
- Missing quantity (default to 1)
- Null items (should handle gracefully)
```

```typescript
it('should throw on negative price', () => {
  const items = [{ name: 'Bad', price: -1 }];
  expect(() => calculateTotal(items)).toThrow('Invalid price');
});

it('should default quantity to 1', () => {
  const items = [{ name: 'Apple', price: 2.00 }];
  expect(calculateTotal(items)).toBe(2.00);
});
```

---

## Step 7: TDD with Claude Workflow

### Full TDD Prompt
```
Let's implement [feature] using TDD:

1. First, write failing tests that define the behavior
2. Show me the tests and confirm they fail
3. Write minimal implementation to pass
4. Refactor while keeping tests green
5. Add edge case tests
6. Continue until feature is complete

Start with the tests.
```

### Add to CLAUDE.md
```markdown
## Development
- Always use TDD for new features
- Write tests before implementation
- Aim for 80%+ coverage
- Run tests after every change
```

---

## Verification Checklist

- [ ] Wrote tests before implementation
- [ ] Saw tests fail (RED phase)
- [ ] Wrote minimal code to pass (GREEN phase)
- [ ] Refactored while tests passed
- [ ] Added edge case tests
- [ ] Achieved 80%+ coverage

---

## TDD Benefits

| Benefit | Description |
|---------|-------------|
| Better Design | Tests force you to think about interface first |
| Higher Coverage | Every line has a test by design |
| Fewer Bugs | Issues caught immediately |
| Safe Refactoring | Tests catch regressions |
| Documentation | Tests show how to use code |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Writing impl first | Discipline! Always test first |
| Tests too complex | Start with simplest case |
| Skipping refactor | Schedule refactoring time |
| Testing implementation | Test behavior, not internals |

---

## Pro Tips

1. **Smallest Step:** Each test should add minimal new behavior
2. **One Assert:** Generally one assertion per test
3. **Descriptive Names:** Test names are documentation
4. **Continuous Running:** Keep tests running in watch mode

---

## TDD Mantras

```
"Write a test that doesn't pass"
"Make it pass in the simplest way"
"Refactor to remove duplication"
"Repeat"
```

---

## Congratulations!

You've completed the **Testing & Verification** category! You now know:

- tmux test pattern for long-running tests
- Output verification for Claude's code
- Git bisect for finding bugs
- Command auditing for safety
- TDD workflow for quality code

**Next:** Move on to **[Workflow Automation](../workflow-automation/01-terminal-cascade.md)** to multiply your productivity!
