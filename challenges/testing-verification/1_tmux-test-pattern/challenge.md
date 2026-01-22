# Challenge: Tmux Test Pattern for Autonomous Tasks

**Related Tip**: Tip 9 - Complete write-test cycle with tmux for autonomous tasks

## Description

Learn to use tmux sessions for running long-running tests and verification processes that Claude can monitor autonomously. This pattern enables Claude to kick off test suites, continue working on other tasks, and check back on results without blocking your workflow.

## Objective

Set up and use tmux sessions to run test suites in the background, allowing Claude to work autonomously while tests execute. Master the pattern of starting tests, detaching, working on other tasks, and reattaching to check results.

## Background

Long-running tests can block Claude's workflow if executed synchronously. Using tmux allows Claude to:
- Start test execution in a named session
- Detach and continue other work
- Reattach later to check results
- Maintain multiple parallel test sessions
- Avoid timeout issues on lengthy test suites

## Steps to Complete

1. **Install tmux** (if not already installed):
   - macOS: `brew install tmux`
   - Linux: `apt-get install tmux` or `yum install tmux`
   - Windows: Use WSL or alternatives like screen

2. **Create a test project** with a long-running test suite:
   - Set up a simple Node.js/Python project
   - Add tests that take 30+ seconds to complete
   - Include both passing and failing tests

3. **Implement the tmux pattern**:
   - Create a named tmux session for test execution
   - Run the test suite in the session
   - Detach from the session
   - List active sessions to verify it's running
   - Reattach to check results

4. **Practice the complete cycle**:
   - Start tests in tmux
   - Work on unrelated tasks while tests run
   - Check test results after completion
   - Handle both success and failure scenarios

5. **Document your workflow**:
   - List the tmux commands used
   - Explain when this pattern is most valuable
   - Note any limitations or gotchas

## Success Criteria

- [ ] tmux is installed and functional
- [ ] Test project created with long-running tests
- [ ] Successfully start tests in a named tmux session
- [ ] Can detach from session while tests continue running
- [ ] Can list active sessions to monitor status
- [ ] Can reattach to session and view test results
- [ ] Understand when to use this pattern vs. direct execution
- [ ] Document the complete workflow with commands

## Example Scenario

```bash
# Start a test session
tmux new-session -d -s test-run "npm test"

# Continue other work...
# (edit files, run linters, etc.)

# Check if session is still running
tmux list-sessions

# Reattach to see results
tmux attach-session -t test-run

# If tests are complete, check output and close session
```

## Bonus Challenges

1. Create a helper script that starts tests in tmux and polls for completion
2. Use tmux to run multiple test suites in parallel sessions
3. Configure tmux logging to capture test output to files
4. Set up tmux key bindings for quick session management

## Common Pitfalls

- Forgetting to name sessions (makes reattaching difficult)
- Not checking if session exists before creating a new one
- Leaving orphaned sessions running indefinitely
- Using tmux for short-running commands that don't need it

## Related Concepts

- Background processes with `&`
- Process management with `jobs` and `fg`
- Screen as an alternative to tmux
- CI/CD pipeline test execution
- Test parallelization strategies
