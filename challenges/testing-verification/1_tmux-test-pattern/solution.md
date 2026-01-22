# Solution: Tmux Test Pattern for Autonomous Tasks

## Overview

This solution demonstrates how to use tmux for running long-running test suites autonomously, enabling Claude to multitask effectively.

## Step-by-Step Solution

### Step 1: Install tmux

```bash
# macOS
brew install tmux

# Ubuntu/Debian
sudo apt-get update && sudo apt-get install tmux

# RHEL/CentOS
sudo yum install tmux

# Verify installation
tmux -V
```

### Step 2: Create a Test Project

```bash
# Create a sample Node.js project
mkdir tmux-test-demo
cd tmux-test-demo
npm init -y

# Install test dependencies
npm install --save-dev jest

# Create a slow test file
cat > slow-test.spec.js << 'EOF'
describe('Slow Tests', () => {
  test('test 1 takes 10 seconds', async () => {
    await new Promise(resolve => setTimeout(resolve, 10000));
    expect(true).toBe(true);
  });

  test('test 2 takes 10 seconds', async () => {
    await new Promise(resolve => setTimeout(resolve, 10000));
    expect(1 + 1).toBe(2);
  });

  test('test 3 takes 10 seconds', async () => {
    await new Promise(resolve => setTimeout(resolve, 10000));
    expect('hello').toContain('ell');
  });
});
EOF

# Configure jest in package.json
npm pkg set scripts.test="jest"
```

### Step 3: Use Tmux Pattern

```bash
# Basic tmux workflow
# 1. Start a new detached session with test command
tmux new-session -d -s test-run "npm test"

# 2. Verify session is running
tmux list-sessions
# Output: test-run: 1 windows (created Tue Jan 21 10:30:00 2026)

# 3. Continue other work while tests run
# ... edit files, run linters, commit code, etc ...

# 4. Check if tests are still running
tmux list-sessions | grep test-run

# 5. Reattach to see results
tmux attach-session -t test-run

# 6. After reviewing, detach again (Ctrl+B, then D)
# Or kill the session
tmux kill-session -t test-run
```

### Step 4: Advanced Patterns

#### Pattern A: Check Status Without Attaching

```bash
# Capture pane content to check if tests finished
tmux capture-pane -pt test-run -S -100

# Or save output to file
tmux capture-pane -pt test-run -S - > test-output.txt
cat test-output.txt
```

#### Pattern B: Multiple Parallel Test Sessions

```bash
# Run unit tests
tmux new-session -d -s unit-tests "npm run test:unit"

# Run integration tests
tmux new-session -d -s integration-tests "npm run test:integration"

# Run e2e tests
tmux new-session -d -s e2e-tests "npm run test:e2e"

# Monitor all sessions
tmux list-sessions

# Check results of each
tmux capture-pane -pt unit-tests
tmux capture-pane -pt integration-tests
tmux capture-pane -pt e2e-tests
```

#### Pattern C: Helper Script

```bash
# Create run-tests-tmux.sh
cat > run-tests-tmux.sh << 'EOF'
#!/bin/bash
SESSION_NAME="test-${1:-default}"

# Check if session exists
if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
  echo "Session $SESSION_NAME already exists. Attaching..."
  tmux attach-session -t "$SESSION_NAME"
  exit 0
fi

# Create new session
echo "Starting tests in session: $SESSION_NAME"
tmux new-session -d -s "$SESSION_NAME" "$2"

echo "Session created. To attach: tmux attach-session -t $SESSION_NAME"
echo "To check status: tmux capture-pane -pt $SESSION_NAME"
EOF

chmod +x run-tests-tmux.sh

# Use it
./run-tests-tmux.sh my-tests "npm test"
```

#### Pattern D: Auto-Cleanup on Completion

```bash
# Run command and auto-kill session when done
tmux new-session -d -s test-run "npm test; tmux kill-session -t test-run"

# For longer persistence (useful for review)
tmux new-session -d -s test-run "npm test; echo 'Tests complete. Press Enter to exit.'; read"
```

### Step 5: Claude Workflow Integration

When Claude uses this pattern:

```bash
# Claude starts tests
tmux new-session -d -s current-test "npm test -- --coverage"

# Claude continues with other tasks
# - Runs linters
# - Fixes type errors
# - Updates documentation

# Claude checks back periodically
tmux capture-pane -pt current-test -S -50 | tail -20

# When complete, Claude reviews full output
tmux capture-pane -pt current-test -S - > test-results.txt
# Analyze test-results.txt

# Cleanup
tmux kill-session -t current-test
```

## Example Commands Reference

```bash
# Create named session (detached)
tmux new-session -d -s <session-name> "<command>"

# List all sessions
tmux list-sessions
tmux ls

# Attach to session
tmux attach-session -t <session-name>
tmux attach -t <session-name>
tmux a -t <session-name>

# Detach from session (inside tmux)
Ctrl+B, then D

# Kill session
tmux kill-session -t <session-name>

# Capture output
tmux capture-pane -pt <session-name> -S -<num-lines>
tmux capture-pane -pt <session-name> -S -  # entire history

# Check if session exists
tmux has-session -t <session-name> 2>/dev/null && echo "exists" || echo "not found"

# Send keys to session (useful for interactive commands)
tmux send-keys -t <session-name> "ls -la" C-m
```

## Common Mistakes to Avoid

1. **Not naming sessions**: Always use `-s <name>` for easy identification
   ```bash
   # BAD: Anonymous session
   tmux new-session -d "npm test"

   # GOOD: Named session
   tmux new-session -d -s test-run "npm test"
   ```

2. **Forgetting to check if session exists**: Creates duplicates
   ```bash
   # GOOD: Check first
   if ! tmux has-session -t test-run 2>/dev/null; then
     tmux new-session -d -s test-run "npm test"
   fi
   ```

3. **Leaving orphaned sessions**: Clean up after use
   ```bash
   # List and kill old sessions
   tmux kill-session -t old-session
   ```

4. **Using tmux for quick commands**: Overkill for <30 second tasks
   ```bash
   # BAD: tmux for fast command
   tmux new-session -d -s lint "npm run lint"

   # GOOD: Just run it
   npm run lint
   ```

5. **Not capturing output**: Reattaching disturbs the view
   ```bash
   # GOOD: Capture to file for analysis
   tmux capture-pane -pt test-run -S - > results.txt
   ```

## When to Use This Pattern

### Use tmux when:
- Tests take >30 seconds
- Running multiple test suites in parallel
- Need to multitask during test execution
- Working with CI/CD pipelines locally
- Debugging flaky tests that need multiple runs

### Don't use tmux when:
- Tests complete in <30 seconds
- Single quick verification needed
- Interactive test debugging required
- Learning/exploring a new test framework

## Integration with Claude's Workflow

Claude should:
1. **Estimate test duration**: If >30s, suggest tmux
2. **Name sessions descriptively**: `test-unit`, `test-e2e`, `lint-check`
3. **Track sessions**: Keep mental model of running sessions
4. **Check completion**: Periodically capture output
5. **Report results**: Parse output and report to user
6. **Cleanup**: Kill sessions after reviewing results

## Advanced Tips

1. **Configure tmux logging**:
   ```bash
   # Add to ~/.tmux.conf
   bind-key h pipe-pane -o "cat >>$HOME/tmux-#S.log" \; display "Logging toggled"
   ```

2. **Use tmux for build processes too**:
   ```bash
   tmux new-session -d -s build "npm run build"
   ```

3. **Combine with watch for continuous testing**:
   ```bash
   tmux new-session -d -s watch-test "npm run test:watch"
   ```

4. **Use tmux scripting for complex workflows**:
   ```bash
   # Create window with multiple panes
   tmux new-session -d -s dev "npm run dev"
   tmux split-window -t dev "npm run test:watch"
   tmux split-window -t dev "npm run lint:watch"
   ```

## Verification

Test your understanding:

```bash
# Start a test session
tmux new-session -d -s verify-test "sleep 30 && echo 'Test complete'"

# Verify it's running
tmux list-sessions | grep verify-test

# Check output before completion
tmux capture-pane -pt verify-test

# Wait 30 seconds, then check again
sleep 30
tmux capture-pane -pt verify-test | grep "Test complete"

# Cleanup
tmux kill-session -t verify-test
```

Success if you see "Test complete" after the sleep duration.
