# Solution: Git Bisect for Debugging

## Overview

This solution demonstrates how to use `git bisect` to efficiently find the commit that introduced a bug using binary search.

## Step-by-Step Solution

### Step 1: Set Up Test Repository

```bash
# Create a test repository
mkdir bisect-demo
cd bisect-demo
git init

# Create initial working code
cat > calculator.js << 'EOF'
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = { add, subtract };
EOF

cat > test.js << 'EOF'
const { add, subtract } = require('./calculator');

// Simple test
if (add(2, 3) !== 5) {
  console.error('FAIL: add(2, 3) should be 5');
  process.exit(1);
}

if (subtract(5, 3) !== 2) {
  console.error('FAIL: subtract(5, 3) should be 2');
  process.exit(1);
}

console.log('PASS: All tests passed');
process.exit(0);
EOF

git add .
git commit -m "Initial commit with working calculator"

# Create several good commits
for i in {1..5}; do
  echo "// Comment $i" >> calculator.js
  git add calculator.js
  git commit -m "Add comment $i"
done

# Introduce a bug (this is the commit we want to find)
cat > calculator.js << 'EOF'
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a + b;  // BUG: Changed - to +
}

module.exports = { add, subtract };
EOF

git add calculator.js
git commit -m "Refactor calculator functions"

# Add more commits after the bug
for i in {1..4}; do
  echo "// Post-bug comment $i" >> calculator.js
  git add calculator.js
  git commit -m "Add post-bug comment $i"
done

# Verify bug exists
node test.js
# Output: FAIL: subtract(5, 3) should be 2
```

### Step 2: Manual Bisect Workflow

```bash
# Start bisecting
git bisect start

# Mark current commit as bad (test fails)
git bisect bad

# Find a good commit (check 10 commits back)
git checkout HEAD~10
node test.js
# Output: PASS: All tests passed

# Mark it as good and return to bisect
git bisect good HEAD~10

# Git will checkout a commit in the middle
# Output: Bisecting: 5 revisions left to test after this

# Test the current commit
node test.js

# If test passes:
git bisect good

# If test fails:
git bisect bad

# Repeat until git identifies the bad commit
# Git will output something like:
# a1b2c3d is the first bad commit
# commit a1b2c3d
# Author: Your Name
# Date: ...
# Refactor calculator functions

# View the bad commit
git show

# Reset bisect when done
git bisect reset
```

### Step 3: Automated Bisect with Script

Create a test script that returns 0 for success, 1 for failure:

```bash
# Create automated test script
cat > bisect-test.sh << 'EOF'
#!/bin/bash

# Exit on first error
set -e

# Run the test
node test.js

# If we get here, test passed (exit 0)
# If test failed, it already exited with 1
EOF

chmod +x bisect-test.sh

# Start bisect
git bisect start
git bisect bad HEAD
git bisect good HEAD~10

# Run automated bisect
git bisect run ./bisect-test.sh

# Output will show:
# running ./bisect-test.sh
# Bisecting: 2 revisions left to test after this
# running ./bisect-test.sh
# Bisecting: 0 revisions left to test after this
# running ./bisect-test.sh
# a1b2c3d is the first bad commit
# bisect run success

# Reset when done
git bisect reset
```

### Step 4: Complex Scenarios

#### Scenario A: Skip Commits That Won't Build

```bash
git bisect start
git bisect bad HEAD
git bisect good HEAD~10

# Test a commit
npm test

# If commit has build issues (not related to bug):
git bisect skip

# Continue bisecting
# Git will choose another commit
```

#### Scenario B: Bisect with Build Step

```bash
cat > bisect-with-build.sh << 'EOF'
#!/bin/bash

# Clean previous build
rm -rf dist/

# Try to build
npm run build || exit 125  # 125 = cannot test this commit

# Run tests
npm test
EOF

chmod +x bisect-with-build.sh

git bisect start
git bisect bad HEAD
git bisect good HEAD~10
git bisect run ./bisect-with-build.sh
```

Exit codes for bisect run:
- 0: Good commit
- 1-127 (except 125): Bad commit
- 125: Cannot test (skip this commit)

#### Scenario C: Performance Regression

```bash
cat > bisect-performance.sh << 'EOF'
#!/bin/bash

# Run benchmark
DURATION=$(node benchmark.js 2>&1 | grep "Duration:" | awk '{print $2}')

# Threshold: 100ms
THRESHOLD=100

if [ "$DURATION" -gt "$THRESHOLD" ]; then
  echo "SLOW: $DURATION ms (threshold: $THRESHOLD ms)"
  exit 1  # Bad (slow)
else
  echo "FAST: $DURATION ms"
  exit 0  # Good (fast)
fi
EOF

chmod +x bisect-performance.sh

git bisect start
git bisect bad HEAD
git bisect good v1.0.0
git bisect run ./bisect-performance.sh
```

### Step 5: Advanced Bisect Techniques

#### Technique 1: Bisect Log and Replay

```bash
# Start bisecting and log decisions
git bisect start
git bisect bad HEAD
git bisect good HEAD~10

# As you test, git logs your decisions
git bisect bad
git bisect good
# ... etc

# Save the log
git bisect log > bisect-log.txt

# Reset
git bisect reset

# Replay the log later
git bisect replay bisect-log.txt
```

#### Technique 2: Visualize Bisect Progress

```bash
# During bisect, view remaining commits
git bisect visualize --oneline

# Or more detailed
git bisect visualize --graph --pretty=oneline
```

#### Technique 3: Bisect Terms (Custom Good/Bad)

```bash
# Use custom terms instead of good/bad
git bisect start --term-old=fast --term-new=slow

# Now use your terms
git bisect slow HEAD
git bisect fast HEAD~10

# Continue with 'fast' and 'slow' instead of 'good' and 'bad'
```

### Step 6: Claude Integration

When Claude uses git bisect:

```bash
# 1. Claude identifies a regression
echo "Tests passing in v1.2.0 but failing in v1.3.0"

# 2. Claude starts bisect
git bisect start
git bisect bad v1.3.0
git bisect good v1.2.0

# 3. Claude creates test script
cat > test-regression.sh << 'EOF'
#!/bin/bash
set -e

# Install dependencies (if needed)
npm ci --silent

# Run specific test
npm test -- --testNamePattern="user authentication"
EOF

chmod +x test-regression.sh

# 4. Claude runs automated bisect
git bisect run ./test-regression.sh

# 5. Claude analyzes result
git show  # View the breaking commit
git diff HEAD~1  # See what changed

# 6. Claude reports findings
echo "Bug introduced in commit abc123: Changed auth logic"

# 7. Claude resets
git bisect reset

# 8. Claude plans fix based on findings
```

## Bisect Workflow Cheatsheet

```bash
# Basic workflow
git bisect start
git bisect bad [commit]   # Usually HEAD
git bisect good [commit]  # Last known good
# Test current commit
git bisect good|bad       # Mark result
# Repeat until found
git bisect reset          # Exit bisect mode

# Automated workflow
git bisect start
git bisect bad [commit]
git bisect good [commit]
git bisect run [script]   # Script must exit 0 (good) or 1 (bad)
git bisect reset

# Other commands
git bisect skip           # Can't test this commit
git bisect log            # View bisect history
git bisect replay [file]  # Replay saved bisect session
git bisect visualize      # Show remaining commits
```

## Common Mistakes to Avoid

### Mistake 1: Not Resetting After Bisect

```bash
# BAD: Leave repo in detached HEAD state
git bisect start
# ... bisecting ...
# Found bad commit
# Forget to reset - repo is now in detached HEAD!

# GOOD: Always reset
git bisect start
# ... bisecting ...
git bisect reset  # Returns to original branch
```

### Mistake 2: Inconsistent Testing

```bash
# BAD: Different test commands
git bisect good  # After running 'npm test'
git bisect bad   # After running 'npm test -- --coverage'

# GOOD: Same test every time
cat > test.sh << 'EOF'
#!/bin/bash
npm test -- --testNamePattern="specific test"
EOF

git bisect run ./test.sh
```

### Mistake 3: Not Cleaning Build Artifacts

```bash
# BAD: Old build files interfere
git bisect run npm test

# GOOD: Clean before testing
cat > test.sh << 'EOF'
#!/bin/bash
rm -rf dist/ node_modules/.cache
npm test
EOF

git bisect run ./test.sh
```

### Mistake 4: Testing Flaky Tests

```bash
# BAD: Unreliable test (sometimes passes, sometimes fails)
git bisect run npm test  # Results will be meaningless

# GOOD: Ensure test is reliable
# Run test multiple times to verify consistency
for i in {1..10}; do npm test || exit 1; done

# Or use a retry mechanism
cat > test.sh << 'EOF'
#!/bin/bash
for i in {1..3}; do
  if npm test; then
    exit 0
  fi
  sleep 1
done
exit 1
EOF
```

### Mistake 5: Wrong Good Commit

```bash
# BAD: "Good" commit also has the bug
git bisect good HEAD~5  # Bug was introduced at HEAD~8

# Result: Git won't find the bug because it's looking
# in the wrong range

# GOOD: Verify the "good" commit first
git checkout HEAD~10
npm test  # Verify it actually passes
git bisect good HEAD~10
```

## Example Scenarios

### Scenario 1: Find When Feature Was Added

```bash
# Find when user authentication was added
git bisect start --term-old=without --term-new=with

# Current commit has the feature
git bisect with HEAD

# Old commit doesn't have the feature
git bisect without v1.0.0

# Test script checks for feature existence
cat > check-feature.sh << 'EOF'
#!/bin/bash
if grep -q "authenticateUser" src/auth.js; then
  exit 0  # Feature exists (with)
else
  exit 1  # Feature doesn't exist (without)
fi
EOF

git bisect run ./check-feature.sh
# Finds first commit that added the feature
```

### Scenario 2: Performance Regression

```bash
# Find when app became slow
cat > perf-test.sh << 'EOF'
#!/bin/bash

# Warm up
node app.js --warmup

# Run benchmark 5 times, take average
total=0
for i in {1..5}; do
  duration=$(node benchmark.js | grep "Time:" | awk '{print $2}')
  total=$((total + duration))
done

average=$((total / 5))

# Threshold: 500ms
if [ "$average" -gt 500 ]; then
  echo "SLOW: ${average}ms"
  exit 1
else
  echo "FAST: ${average}ms"
  exit 0
fi
EOF

git bisect start
git bisect bad HEAD
git bisect good v2.0.0
git bisect run ./perf-test.sh
```

### Scenario 3: Dependency Issue

```bash
# Find when dependency broke build
cat > build-test.sh << 'EOF'
#!/bin/bash

# Clean install
rm -rf node_modules package-lock.json
npm install --silent || exit 125  # Can't test if install fails

# Try to build
npm run build
EOF

git bisect start
git bisect bad HEAD
git bisect good HEAD~20
git bisect run ./build-test.sh
```

## Bisect Best Practices

1. **Always have a reliable test**
   - Test must be deterministic (same result every time)
   - Test must be specific to the bug
   - Test should be fast (you'll run it multiple times)

2. **Verify your endpoints**
   - Confirm current commit is bad: `npm test` → fails
   - Confirm old commit is good: `git checkout HEAD~10 && npm test` → passes

3. **Use automation when possible**
   - Manual bisecting is error-prone
   - Automated bisecting is faster and more reliable

4. **Clean between tests**
   - Remove build artifacts
   - Clear caches
   - Reset database state if needed

5. **Document your findings**
   ```bash
   # Save bisect results
   git bisect log > bisect-results.txt
   git show [bad-commit] > breaking-commit.patch
   ```

6. **Handle edge cases**
   - Skip unbuildable commits (exit 125)
   - Handle merge commits carefully
   - Deal with commits that require different build steps

## Integration with Development Workflow

```bash
# 1. Discover regression
npm test
# FAIL: 3 tests failing

# 2. Find last known good version
git tag --list
# v1.2.0 (released last week, tests passing)

# 3. Bisect to find breaking commit
git bisect start
git bisect bad HEAD
git bisect good v1.2.0
git bisect run npm test

# 4. Analyze breaking commit
git show [commit-hash]
git log -p [commit-hash]

# 5. Create fix
git bisect reset
git checkout -b fix/broken-test
# ... make fixes ...

# 6. Verify fix
npm test  # Should pass now

# 7. Commit and document
git commit -m "fix: Repair broken test

Found via git bisect that commit [hash] broke the test.
Root cause: [explanation]
Fix: [what you changed]"
```

## Summary

Git bisect is a powerful debugging tool that:
- Uses binary search to find breaking commits (O(log n) vs O(n))
- Can be manual or automated
- Works best with deterministic tests
- Requires careful setup but saves significant time
- Integrates well with Claude's debugging workflow

Master git bisect to quickly identify when and where bugs were introduced.
