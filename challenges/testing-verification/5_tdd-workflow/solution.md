# Solution: Test-Driven Development Workflow

## Overview

This solution demonstrates how to practice Test-Driven Development (TDD) effectively, from setup to advanced techniques.

## Step-by-Step Solution

### Step 1: Set Up Testing Environment

#### Option A: JavaScript with Jest

```bash
# Create project
mkdir tdd-practice
cd tdd-practice
npm init -y

# Install Jest
npm install --save-dev jest @types/jest

# Configure Jest
npm pkg set scripts.test="jest"
npm pkg set scripts.test:watch="jest --watch"
npm pkg set scripts.test:coverage="jest --coverage"

# Create Jest config
cat > jest.config.js << 'EOF'
module.exports = {
  testEnvironment: 'node',
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/**/*.test.js',
  ]
};
EOF

# Create directory structure
mkdir -p src
```

#### Option B: Python with pytest

```bash
# Create project
mkdir tdd-practice
cd tdd-practice
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install pytest and coverage
pip install pytest pytest-cov

# Create pytest config
cat > pytest.ini << 'EOF'
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = --cov=src --cov-report=term-missing --cov-fail-under=80
EOF

# Create directory structure
mkdir -p src tests
touch src/__init__.py
touch tests/__init__.py
```

### Step 2: Basic TDD Cycle Example

Let's implement a simple calculator using TDD:

#### RED Phase: Write Failing Test

```javascript
// src/calculator.test.js

describe('Calculator', () => {
  test('add should sum two numbers', () => {
    const calc = new Calculator();
    expect(calc.add(2, 3)).toBe(5);
  });
});
```

```bash
# Run test
npm test

# Output: FAIL
# ReferenceError: Calculator is not defined
# ✗ add should sum two numbers
```

#### GREEN Phase: Minimal Implementation

```javascript
// src/calculator.js

class Calculator {
  add(a, b) {
    return a + b;
  }
}

module.exports = Calculator;
```

```javascript
// src/calculator.test.js (update)

const Calculator = require('./calculator');

describe('Calculator', () => {
  test('add should sum two numbers', () => {
    const calc = new Calculator();
    expect(calc.add(2, 3)).toBe(5);
  });
});
```

```bash
# Run test
npm test

# Output: PASS
# ✓ add should sum two numbers
```

#### REFACTOR Phase: Improve (if needed)

```javascript
// src/calculator.js (refactored)

class Calculator {
  add(a, b) {
    // Add validation
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new TypeError('Arguments must be numbers');
    }
    return a + b;
  }
}

module.exports = Calculator;
```

```javascript
// Add test for validation
test('add should throw TypeError for non-numbers', () => {
  const calc = new Calculator();
  expect(() => calc.add('2', 3)).toThrow(TypeError);
  expect(() => calc.add(2, '3')).toThrow(TypeError);
});
```

```bash
# Run tests
npm test

# Output: PASS
# ✓ add should sum two numbers
# ✓ add should throw TypeError for non-numbers
```

### Step 3: Complete Feature Implementation with TDD

Let's build a complete calculator with TDD:

```javascript
// src/calculator.test.js

const Calculator = require('./calculator');

describe('Calculator', () => {
  let calc;

  beforeEach(() => {
    calc = new Calculator();
  });

  describe('add', () => {
    test('should sum two positive numbers', () => {
      expect(calc.add(2, 3)).toBe(5);
    });

    test('should sum negative numbers', () => {
      expect(calc.add(-2, -3)).toBe(-5);
    });

    test('should handle zero', () => {
      expect(calc.add(0, 5)).toBe(5);
      expect(calc.add(5, 0)).toBe(5);
    });

    test('should throw TypeError for non-numbers', () => {
      expect(() => calc.add('2', 3)).toThrow(TypeError);
    });
  });

  describe('subtract', () => {
    test('should subtract two numbers', () => {
      expect(calc.subtract(5, 3)).toBe(2);
    });

    test('should handle negative results', () => {
      expect(calc.subtract(3, 5)).toBe(-2);
    });

    test('should throw TypeError for non-numbers', () => {
      expect(() => calc.subtract(5, '3')).toThrow(TypeError);
    });
  });

  describe('multiply', () => {
    test('should multiply two numbers', () => {
      expect(calc.multiply(3, 4)).toBe(12);
    });

    test('should handle zero', () => {
      expect(calc.multiply(5, 0)).toBe(0);
    });

    test('should handle negative numbers', () => {
      expect(calc.multiply(-3, 4)).toBe(-12);
    });
  });

  describe('divide', () => {
    test('should divide two numbers', () => {
      expect(calc.divide(10, 2)).toBe(5);
    });

    test('should handle decimal results', () => {
      expect(calc.divide(7, 2)).toBe(3.5);
    });

    test('should throw error on division by zero', () => {
      expect(() => calc.divide(10, 0)).toThrow('Division by zero');
    });

    test('should throw TypeError for non-numbers', () => {
      expect(() => calc.divide(10, '2')).toThrow(TypeError);
    });
  });
});
```

Now implement each method one by one, following RED-GREEN-REFACTOR:

```javascript
// src/calculator.js (full implementation)

class Calculator {
  _validateNumbers(...args) {
    if (args.some(arg => typeof arg !== 'number')) {
      throw new TypeError('All arguments must be numbers');
    }
  }

  add(a, b) {
    this._validateNumbers(a, b);
    return a + b;
  }

  subtract(a, b) {
    this._validateNumbers(a, b);
    return a - b;
  }

  multiply(a, b) {
    this._validateNumbers(a, b);
    return a * b;
  }

  divide(a, b) {
    this._validateNumbers(a, b);
    if (b === 0) {
      throw new Error('Division by zero');
    }
    return a / b;
  }
}

module.exports = Calculator;
```

### Step 4: TDD for Bug Fixes

Example: Bug reported - "Calculator crashes on very large numbers"

#### RED: Write test that reproduces the bug

```javascript
test('should handle large numbers', () => {
  const result = calc.add(Number.MAX_SAFE_INTEGER, 1);
  expect(result).toBe(Number.MAX_SAFE_INTEGER + 1);
  // This might fail due to floating point precision
});

test('should warn on unsafe integer operations', () => {
  expect(() => {
    calc.add(Number.MAX_SAFE_INTEGER, 10);
  }).toThrow('Result exceeds safe integer range');
});
```

#### GREEN: Fix the bug

```javascript
add(a, b) {
  this._validateNumbers(a, b);
  const result = a + b;

  if (!Number.isSafeInteger(result)) {
    throw new RangeError('Result exceeds safe integer range');
  }

  return result;
}
```

#### REFACTOR: Extract common logic

```javascript
_checkSafeInteger(value) {
  if (!Number.isSafeInteger(value)) {
    throw new RangeError('Result exceeds safe integer range');
  }
  return value;
}

add(a, b) {
  this._validateNumbers(a, b);
  return this._checkSafeInteger(a + b);
}

multiply(a, b) {
  this._validateNumbers(a, b);
  return this._checkSafeInteger(a * b);
}
```

### Step 5: Advanced TDD - Stack Implementation

Let's implement a Stack data structure using strict TDD:

```javascript
// src/stack.test.js

const Stack = require('./stack');

describe('Stack', () => {
  let stack;

  beforeEach(() => {
    stack = new Stack();
  });

  describe('push', () => {
    test('should add item to stack', () => {
      stack.push(1);
      expect(stack.size()).toBe(1);
    });

    test('should add multiple items', () => {
      stack.push(1);
      stack.push(2);
      stack.push(3);
      expect(stack.size()).toBe(3);
    });
  });

  describe('pop', () => {
    test('should remove and return top item', () => {
      stack.push(1);
      stack.push(2);
      expect(stack.pop()).toBe(2);
      expect(stack.size()).toBe(1);
    });

    test('should throw error on empty stack', () => {
      expect(() => stack.pop()).toThrow('Stack is empty');
    });
  });

  describe('peek', () => {
    test('should return top item without removing it', () => {
      stack.push(1);
      stack.push(2);
      expect(stack.peek()).toBe(2);
      expect(stack.size()).toBe(2);
    });

    test('should throw error on empty stack', () => {
      expect(() => stack.peek()).toThrow('Stack is empty');
    });
  });

  describe('isEmpty', () => {
    test('should return true for empty stack', () => {
      expect(stack.isEmpty()).toBe(true);
    });

    test('should return false for non-empty stack', () => {
      stack.push(1);
      expect(stack.isEmpty()).toBe(false);
    });
  });

  describe('size', () => {
    test('should return 0 for empty stack', () => {
      expect(stack.size()).toBe(0);
    });

    test('should return correct size', () => {
      stack.push(1);
      stack.push(2);
      stack.push(3);
      expect(stack.size()).toBe(3);
    });
  });

  describe('clear', () => {
    test('should remove all items', () => {
      stack.push(1);
      stack.push(2);
      stack.clear();
      expect(stack.isEmpty()).toBe(true);
      expect(stack.size()).toBe(0);
    });
  });
});
```

Implement one test at a time:

```javascript
// src/stack.js

class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    if (this.isEmpty()) {
      throw new Error('Stack is empty');
    }
    return this.items.pop();
  }

  peek() {
    if (this.isEmpty()) {
      throw new Error('Stack is empty');
    }
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }

  clear() {
    this.items = [];
  }
}

module.exports = Stack;
```

### Step 6: Check Coverage

```bash
# Run coverage report
npm run test:coverage

# Output:
# ----------|---------|----------|---------|---------|-------------------
# File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
# ----------|---------|----------|---------|---------|-------------------
# All files |     100 |      100 |     100 |     100 |
#  calculator.js |  100 |      100 |     100 |     100 |
#  stack.js  |     100 |      100 |     100 |     100 |
# ----------|---------|----------|---------|---------|-------------------
```

### Step 7: TDD with Claude

Workflow when working with Claude:

```markdown
User: "Implement a binary search function using TDD"

Claude responds with:
1. First, write the test (RED phase)
2. Then implement minimal code (GREEN phase)
3. Finally refactor (REFACTOR phase)

Example:

// Step 1: RED - Write failing test
test('binarySearch should find element in sorted array', () => {
  expect(binarySearch([1, 2, 3, 4, 5], 3)).toBe(2);
});

// Run test → FAILS (function doesn't exist)

// Step 2: GREEN - Minimal implementation
function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

// Run test → PASSES

// Step 3: RED - Add edge cases
test('binarySearch should return -1 for missing element', () => {
  expect(binarySearch([1, 2, 3, 4, 5], 6)).toBe(-1);
});

test('binarySearch should handle empty array', () => {
  expect(binarySearch([], 1)).toBe(-1);
});

test('binarySearch should find first element', () => {
  expect(binarySearch([1, 2, 3, 4, 5], 1)).toBe(0);
});

test('binarySearch should find last element', () => {
  expect(binarySearch([1, 2, 3, 4, 5], 5)).toBe(4);
});

// Run tests → ALL PASS

// Step 4: REFACTOR - Add validation
function binarySearch(arr, target) {
  if (!Array.isArray(arr)) {
    throw new TypeError('First argument must be an array');
  }

  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

// Add validation test
test('binarySearch should throw on non-array input', () => {
  expect(() => binarySearch('not an array', 1)).toThrow(TypeError);
});

// Run all tests → ALL PASS
```

## TDD Best Practices

### Practice 1: Start with the Simplest Test

```javascript
// GOOD: Start simple
test('should create an empty list', () => {
  const list = new TodoList();
  expect(list.items).toEqual([]);
});

// BAD: Start too complex
test('should add, remove, filter, and sort items', () => {
  // Too much at once
});
```

### Practice 2: One Assert Per Test (Generally)

```javascript
// GOOD: Focused test
test('add should return sum', () => {
  expect(add(2, 3)).toBe(5);
});

test('add should handle negatives', () => {
  expect(add(-2, -3)).toBe(-5);
});

// LESS IDEAL: Multiple unrelated asserts
test('add should work', () => {
  expect(add(2, 3)).toBe(5);
  expect(add(-2, -3)).toBe(-5);
  expect(add(0, 0)).toBe(0);
  // Hard to tell which assertion failed
});
```

### Practice 3: Test Behavior, Not Implementation

```javascript
// GOOD: Test behavior
test('should store user data', () => {
  const user = new User('Alice', 'alice@example.com');
  expect(user.getName()).toBe('Alice');
  expect(user.getEmail()).toBe('alice@example.com');
});

// BAD: Test implementation details
test('should use internal _name property', () => {
  const user = new User('Alice', 'alice@example.com');
  expect(user._name).toBe('Alice'); // Testing private details
});
```

### Practice 4: Use Descriptive Test Names

```javascript
// GOOD: Descriptive
test('divide should throw RangeError when dividing by zero', () => {
  expect(() => divide(10, 0)).toThrow(RangeError);
});

// BAD: Vague
test('test divide', () => {
  expect(() => divide(10, 0)).toThrow();
});
```

### Practice 5: Keep Tests Independent

```javascript
// GOOD: Independent tests
describe('TodoList', () => {
  let list;

  beforeEach(() => {
    list = new TodoList();
  });

  test('should add item', () => {
    list.add('Task 1');
    expect(list.size()).toBe(1);
  });

  test('should remove item', () => {
    list.add('Task 1');
    list.remove('Task 1');
    expect(list.size()).toBe(0);
  });
});

// BAD: Dependent tests
let sharedList = new TodoList();

test('should add item', () => {
  sharedList.add('Task 1');
  expect(sharedList.size()).toBe(1);
});

test('should remove item', () => {
  // Depends on previous test having run
  sharedList.remove('Task 1');
  expect(sharedList.size()).toBe(0);
});
```

## Common TDD Mistakes and Fixes

### Mistake 1: Writing Implementation First

```javascript
// WRONG ORDER
// 1. Write function
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

// 2. Then write tests
test('fibonacci should work', () => {
  expect(fibonacci(5)).toBe(5);
});

// CORRECT ORDER
// 1. Write test (RED)
test('fibonacci should return 0 for n=0', () => {
  expect(fibonacci(0)).toBe(0);
});

// 2. Run test (FAIL)
// 3. Write minimal code (GREEN)
function fibonacci(n) {
  return 0; // Just enough to pass
}

// 4. Add next test (RED)
test('fibonacci should return 1 for n=1', () => {
  expect(fibonacci(1)).toBe(1);
});

// 5. Update code (GREEN)
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

### Mistake 2: Skipping Refactor Step

```javascript
// After getting tests green, code might be messy
function processData(data) {
  if (data === null) throw new Error('null');
  if (data === undefined) throw new Error('undefined');
  if (typeof data !== 'object') throw new Error('not object');
  if (Array.isArray(data)) throw new Error('is array');
  // ... duplicate validation code ...
  return Object.keys(data).length;
}

// REFACTOR: Extract validation
function validateData(data) {
  if (data === null || data === undefined) {
    throw new Error('Data cannot be null or undefined');
  }
  if (typeof data !== 'object' || Array.isArray(data)) {
    throw new Error('Data must be a plain object');
  }
}

function processData(data) {
  validateData(data);
  return Object.keys(data).length;
}
```

### Mistake 3: Testing Too Much at Once

```javascript
// BAD: Giant test
test('full user workflow', () => {
  const user = new User();
  user.register('alice', 'password');
  user.login('alice', 'password');
  user.updateProfile({ bio: 'Developer' });
  user.addFriend('bob');
  user.sendMessage('bob', 'Hi');
  // ... 50 more lines
});

// GOOD: Incremental tests
test('should register user', () => {
  const user = new User();
  user.register('alice', 'password');
  expect(user.isRegistered()).toBe(true);
});

test('should login registered user', () => {
  const user = new User();
  user.register('alice', 'password');
  expect(user.login('alice', 'password')).toBe(true);
});

// ... one test per feature
```

## TDD Kata Examples

### Kata 1: FizzBuzz

```javascript
// Write tests first, implement one by one
test('returns "1" for 1', () => {
  expect(fizzBuzz(1)).toBe('1');
});

test('returns "2" for 2', () => {
  expect(fizzBuzz(2)).toBe('2');
});

test('returns "Fizz" for 3', () => {
  expect(fizzBuzz(3)).toBe('Fizz');
});

test('returns "Buzz" for 5', () => {
  expect(fizzBuzz(5)).toBe('Buzz');
});

test('returns "FizzBuzz" for 15', () => {
  expect(fizzBuzz(15)).toBe('FizzBuzz');
});

// Implementation
function fizzBuzz(n) {
  if (n % 15 === 0) return 'FizzBuzz';
  if (n % 3 === 0) return 'Fizz';
  if (n % 5 === 0) return 'Buzz';
  return String(n);
}
```

### Kata 2: String Calculator

```javascript
// RED-GREEN-REFACTOR for each test
test('returns 0 for empty string', () => {
  expect(add('')).toBe(0);
});

test('returns number for single number', () => {
  expect(add('5')).toBe(5);
});

test('returns sum of two numbers', () => {
  expect(add('1,2')).toBe(3);
});

test('handles multiple numbers', () => {
  expect(add('1,2,3,4,5')).toBe(15);
});

test('handles newlines as delimiters', () => {
  expect(add('1\n2,3')).toBe(6);
});

// Implementation (built incrementally)
function add(numbers) {
  if (numbers === '') return 0;

  const nums = numbers.split(/[,\n]/).map(Number);
  return nums.reduce((sum, n) => sum + n, 0);
}
```

## Summary

Effective TDD requires:

1. **Discipline**: Always write tests first
2. **Small Steps**: One test at a time
3. **Full Cycle**: RED → GREEN → REFACTOR
4. **Coverage**: Aim for 80%+ meaningful coverage
5. **Fast Feedback**: Run tests frequently
6. **Refactoring**: Don't skip this step
7. **Independence**: Tests don't depend on each other
8. **Clarity**: Descriptive test names and clear assertions

TDD takes practice but leads to better design, fewer bugs, and more confidence in your code.
