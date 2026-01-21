# tmux Test Pattern

## Difficulty: Medium

## Category: Testing & Verification

## Related Tips: 9

## Description

The tmux test pattern enables Claude Code to run long-running processes autonomously while capturing and verifying output. This is essential for test-driven development workflows where tests may take time to complete.

## Objective

Master the tmux test pattern for autonomous testing:
1. Start a tmux session for test execution
2. Send test commands to the session
3. Capture and parse test output
4. Verify test results programmatically

## Task

Implement a complete write-test cycle using tmux:

1. Create a tmux session named "test-runner"
2. Send a command to run your project's test suite
3. Wait for completion and capture the output
4. Parse the output to determine pass/fail status
5. Report the results back

## Expected Outcome

- tmux session created and managed correctly
- Test output captured completely
- Pass/fail status determined accurately
- Session cleaned up after use

## Hints

1. `tmux new-session -d -s name` creates a detached session
2. `tmux send-keys -t name 'command' Enter` sends commands
3. `tmux capture-pane -t name -p` captures output
4. Parse output for test framework's success/failure indicators

## Constraints

- Must use tmux (not just background processes)
- Must capture complete output (not truncated)
- Clean up sessions after use

## Submission

Submit:
1. The sequence of tmux commands used
2. How you captured and parsed the output
3. The method used to determine pass/fail
