# Challenge: Git Bisect for Debugging

**Related Tip**: Tip 28 - Use git bisect to find breaking commits

## Description

Learn to use `git bisect` to efficiently identify the exact commit that introduced a bug or regression. This binary search technique dramatically reduces debugging time when you know something worked before but is broken now.

## Objective

Master the `git bisect` workflow to pinpoint breaking changes in version history. Understand when to use automated vs. manual bisecting, and how to integrate this tool into your debugging workflow with Claude.

## Background

When a bug appears in your codebase and you know it worked previously, `git bisect` uses binary search to find the problematic commit. Instead of checking every commit linearly, it intelligently narrows down the search space, reducing the number of tests needed from O(n) to O(log n).

For example:
- 100 commits to check linearly: 100 tests worst case
- 100 commits with bisect: 7 tests maximum

## When to Use Git Bisect

Use `git bisect` when:
- A test that used to pass now fails
- A feature that worked is now broken
- You know roughly when it worked (have a "good" commit)
- You have a reliable way to test if a commit is good/bad
- The commit history is relatively linear (or you understand the branching)

Don't use `git bisect` when:
- The bug is intermittent/flaky
- The codebase structure changed dramatically (major refactoring)
- You can't easily build/test intermediate commits
- The issue is in uncommitted changes

## Steps to Complete

1. **Set up a test scenario**:
   - Create a git repository with a linear history
   - Introduce a bug in a commit (you know which one)
   - Verify the bug exists in HEAD
   - Verify the bug doesn't exist in an earlier commit

2. **Manual bisect workflow**:
   - Start a bisect session with `git bisect start`
   - Mark the current commit as bad
   - Mark an earlier commit as good
   - Test each commit git bisect provides
   - Mark each as good or bad until bisect identifies the culprit

3. **Automated bisect workflow**:
   - Create a test script that exits 0 (good) or 1 (bad)
   - Use `git bisect run` with your script
   - Let git automatically find the breaking commit

4. **Complex scenarios**:
   - Handle commits that can't be tested (skip them)
   - Deal with commits that won't build
   - Bisect across merge commits
   - Use bisect to find when a feature was added

5. **Document your findings**:
   - Identify the exact breaking commit
   - Understand what changed in that commit
   - Plan the fix based on bisect results

## Success Criteria

- [ ] Understand how git bisect uses binary search
- [ ] Can start a bisect session and mark good/bad commits
- [ ] Can manually bisect through a commit history
- [ ] Can create a test script for automated bisecting
- [ ] Can use `git bisect run` with a test script
- [ ] Can handle skipped commits and build failures
- [ ] Can interpret bisect results and identify the breaking change
- [ ] Know when git bisect is appropriate vs. other debugging methods

## Example Scenario

```bash
# You discover tests are failing
npm test
# FAIL: 15 tests failed

# You know tests passed 10 commits ago
git log --oneline -10

# Start bisecting
git bisect start
git bisect bad                    # Current commit is bad
git bisect good HEAD~10          # 10 commits ago was good

# Git checks out a middle commit
# Test it
npm test && git bisect good || git bisect bad

# Repeat until git identifies the exact commit
```

## Bonus Challenges

1. Create a bisect script that works with your CI/CD pipeline
2. Use bisect with a performance regression (threshold-based)
3. Bisect across multiple branches or a complex merge history
4. Create a wrapper script that automates the entire bisect process
5. Use bisect to find when a specific line of code was added

## Common Pitfalls

- Forgetting to run `git bisect reset` after completing (leaves repo in detached HEAD)
- Marking commits incorrectly (good/bad reversed)
- Testing inconsistently between commits
- Not cleaning build artifacts between commits
- Using bisect on a flaky test (unreliable results)
- Starting bisect with bad "good" commit (bug existed then too)

## Bisect Workflow Diagram

```
Commits:  A - B - C - D - E - F - G - H (HEAD)
          ✓   ✓   ✓   ✗   ✗   ✗   ✗   ✗

Start:    good            unknown       bad
          |                              |
Step 1:   A -------- test E -------- H
                      ↓
                      ✗ (bad)

Step 2:   A --- test C --- E
                ↓
                ✓ (good)

Step 3:   C - test D - E
              ↓
              ✗ (bad, first bad commit!)

Result: Commit D introduced the bug
```

## Related Concepts

- Binary search algorithms
- Regression testing
- Git history investigation (git log, git blame)
- Continuous Integration
- Automated testing
