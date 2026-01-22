# Challenge: Test-Driven Development Workflow

**Related Tip**: Tip 34 - Write lots of tests using TDD

## Description

Learn and practice the Test-Driven Development (TDD) workflow: Write failing tests first (RED), implement code to pass tests (GREEN), then refactor (REFACTOR). This challenge teaches you to use TDD effectively with Claude, ensuring high test coverage and quality code.

## Objective

Master the TDD cycle:
1. **RED**: Write a failing test first
2. **GREEN**: Write minimal code to make the test pass
3. **REFACTOR**: Improve code while keeping tests passing

Learn to maintain 80%+ test coverage, write meaningful tests, and use TDD to drive design decisions.

## Background

Test-Driven Development is a software development methodology where tests are written before implementation code. Benefits include:

- **Better Design**: Tests force you to think about interfaces first
- **Higher Coverage**: Every line has a corresponding test
- **Fewer Bugs**: Issues are caught immediately
- **Confidence**: Refactoring is safer with comprehensive tests
- **Documentation**: Tests serve as executable specifications
- **Faster Debugging**: When tests fail, you know exactly what broke

The TDD mantra: **Red, Green, Refactor**

## TDD Cycle Explained

### RED Phase
Write a test for functionality that doesn't exist yet. The test should fail.

```javascript
// Write this first
test('add should sum two numbers', () => {
  expect(add(2, 3)).toBe(5);  // add() doesn't exist yet
});

// Run test → FAILS (RED)
```

### GREEN Phase
Write the minimal code to make the test pass. Don't worry about perfection.

```javascript
// Minimal implementation
function add(a, b) {
  return a + b;
}

// Run test → PASSES (GREEN)
```

### REFACTOR Phase
Improve the code while keeping tests green. Optimize, simplify, eliminate duplication.

```javascript
// Maybe add type checking, validation, etc.
function add(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new TypeError('Arguments must be numbers');
  }
  return a + b;
}

// Run test → STILL PASSES (GREEN)
// Add more tests for edge cases
```

## Steps to Complete

### Step 1: Set Up Testing Environment

1. Choose a language/framework (JavaScript/Jest, Python/pytest, etc.)
2. Install testing dependencies
3. Configure test runner
4. Create project structure

### Step 2: Practice Basic TDD Cycle

1. Write your first failing test
2. Run the test (should fail)
3. Write minimal code to pass
4. Run the test (should pass)
5. Refactor if needed
6. Run the test again (should still pass)

### Step 3: Implement a Feature Using TDD

Choose a feature to implement (e.g., Calculator, TodoList, StringUtils):

1. Write tests for each method/function before implementing
2. Follow RED-GREEN-REFACTOR for each test
3. Build incrementally, one test at a time
4. Verify coverage stays above 80%

### Step 4: Test-Driven Bug Fixes

1. Reproduce a bug with a failing test
2. Fix the bug to make the test pass
3. Ensure fix doesn't break other tests

### Step 5: Refactoring with TDD Safety Net

1. Start with code that has comprehensive tests
2. Refactor the implementation
3. Verify all tests still pass
4. Measure coverage remains high

### Step 6: Practice with Claude

1. Ask Claude to implement a feature using TDD
2. Verify Claude writes tests first
3. Review test quality and coverage
4. Practice the full RED-GREEN-REFACTOR cycle

## Success Criteria

- [ ] Understand the RED-GREEN-REFACTOR cycle
- [ ] Can write failing tests before implementation
- [ ] Can write minimal code to pass tests
- [ ] Can refactor while maintaining green tests
- [ ] Achieve 80%+ test coverage consistently
- [ ] Write meaningful tests (not just for coverage)
- [ ] Use TDD to drive design decisions
- [ ] Can use TDD for bug fixes
- [ ] Can refactor confidently with test safety net
- [ ] Have practiced TDD with at least 3 different features

## Example TDD Session

```javascript
// Feature: String Reverser

// RED: Write test first
test('reverse should reverse a string', () => {
  expect(reverse('hello')).toBe('olleh');
});
// Run test → FAIL (function doesn't exist)

// GREEN: Minimal implementation
function reverse(str) {
  return str.split('').reverse().join('');
}
// Run test → PASS

// RED: Add edge case test
test('reverse should handle empty string', () => {
  expect(reverse('')).toBe('');
});
// Run test → PASS (implementation already handles it)

// RED: Add another edge case
test('reverse should throw on non-string', () => {
  expect(() => reverse(123)).toThrow();
});
// Run test → FAIL (doesn't throw yet)

// GREEN: Add validation
function reverse(str) {
  if (typeof str !== 'string') {
    throw new TypeError('Argument must be a string');
  }
  return str.split('').reverse().join('');
}
// Run test → PASS

// REFACTOR: Improve with better error message
function reverse(str) {
  if (typeof str !== 'string') {
    throw new TypeError(`Expected string, got ${typeof str}`);
  }
  return str.split('').reverse().join('');
}
// Run tests → ALL PASS
```

## Test Coverage Target

Minimum 80% coverage across:
- **Line Coverage**: 80%+ lines executed
- **Branch Coverage**: 80%+ branches tested
- **Function Coverage**: 80%+ functions tested
- **Statement Coverage**: 80%+ statements executed

## Bonus Challenges

1. **TDD Kata**: Implement FizzBuzz, Roman Numerals, or Prime Factors using strict TDD
2. **Legacy Code**: Add tests to untested code before refactoring
3. **Pair Programming**: Practice TDD with Claude as your pair programmer
4. **Mutation Testing**: Use mutation testing to verify test quality
5. **Performance TDD**: Write performance tests first, then optimize

## Common Pitfalls

1. **Writing implementation before tests**: Defeats the purpose of TDD
2. **Writing too many tests at once**: Work incrementally, one test at a time
3. **Skipping the refactor step**: Code quality degrades without refactoring
4. **Testing implementation details**: Test behavior, not implementation
5. **100% coverage obsession**: Focus on meaningful tests, not arbitrary coverage
6. **Large test jumps**: Small incremental steps are more effective
7. **Not running tests frequently**: Run after every change

## TDD Best Practices

### DO:
- Write the test first
- Start with the simplest test case
- Write one test at a time
- Keep tests independent
- Run tests frequently
- Refactor both code and tests
- Use descriptive test names
- Test edge cases and errors

### DON'T:
- Write implementation before tests
- Write multiple tests without implementing
- Skip failing tests to "come back later"
- Test implementation details
- Have tests depend on each other
- Ignore failing tests
- Write tests just for coverage metrics

## Test Types in TDD

### Unit Tests (Primary Focus)
```javascript
test('add should sum two positive numbers', () => {
  expect(add(2, 3)).toBe(5);
});
```

### Integration Tests
```javascript
test('calculator should handle complex operations', () => {
  const calc = new Calculator();
  const result = calc.add(5).multiply(2).subtract(3);
  expect(result.getValue()).toBe(7);
});
```

### Edge Cases
```javascript
test('divide should throw on division by zero', () => {
  expect(() => divide(10, 0)).toThrow('Division by zero');
});
```

### Error Handling
```javascript
test('should reject invalid input', () => {
  expect(() => processInput(null)).toThrow(TypeError);
});
```

## Related Concepts

- Unit Testing
- Test Coverage
- Behavior-Driven Development (BDD)
- Refactoring
- Continuous Testing
- Test Doubles (Mocks, Stubs, Spies)
- Mutation Testing
- Property-Based Testing
