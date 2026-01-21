#!/usr/bin/env python3
"""
PR Creator Challenge - Test Suite
Verifies the complete PR workflow.
"""

import re
import subprocess
import sys
from pathlib import Path

def run_git(args, cwd="starter"):
    """Run a git command and return output."""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        return result.stdout.strip(), result.returncode
    except Exception as e:
        return str(e), 1

def test_branch_name():
    """Test if branch follows naming convention."""
    output, code = run_git(["branch", "--show-current"])

    if code != 0:
        print("FAIL: Could not get current branch")
        return 0

    branch = output.strip()

    # Check naming convention
    if re.match(r'^(feat|fix|refactor|docs|test|chore)/.+', branch):
        print(f"PASS: Branch name follows convention ({branch})")
        return 20
    elif branch != "main" and branch != "master":
        print(f"PARTIAL: Branch exists but naming could be better ({branch})")
        return 10
    else:
        print(f"FAIL: Still on main/master branch")
        return 0

def test_commit_format():
    """Test if commit follows conventional format."""
    output, code = run_git(["log", "-1", "--pretty=format:%s"])

    if code != 0 or not output:
        print("FAIL: No commits found")
        return 0

    # Check conventional commit pattern
    pattern = r'^(feat|fix|refactor|docs|test|chore)(\([^)]+\))?:\s+.+'
    if re.match(pattern, output):
        print(f"PASS: Commit follows conventional format")
        return 25
    else:
        print(f"FAIL: Commit message doesn't follow format")
        print(f"  Got: {output}")
        return 0

def test_function_implemented():
    """Test if validateEmail function was implemented."""
    file_path = Path("starter/src/utils/validation.ts")

    if not file_path.exists():
        print("FAIL: validation.ts not found")
        return 0

    content = file_path.read_text()

    if "validateEmail" in content:
        # Check for basic implementation
        if "function validateEmail" in content or "const validateEmail" in content:
            if "return" in content and ("true" in content.lower() or "false" in content.lower()):
                print("PASS: validateEmail function implemented")
                return 30
            else:
                print("PARTIAL: Function exists but implementation incomplete")
                return 15

    print("FAIL: validateEmail function not found")
    return 0

def test_pr_created():
    """Test if PR was created (simulated check)."""
    # In real scenario, would use gh pr list
    # For testing, check if remote tracking is set up
    output, code = run_git(["remote", "-v"])

    if "origin" in output:
        # Check if branch was pushed
        branch, _ = run_git(["branch", "--show-current"])
        remote_check, _ = run_git(["ls-remote", "--heads", "origin", branch])

        if branch in str(remote_check):
            print("PASS: Branch pushed to remote (PR likely created)")
            return 25
        else:
            print("PARTIAL: Remote configured but branch not pushed")
            return 10
    else:
        print("INFO: No remote configured (skipping PR check)")
        return 15  # Give partial credit in test environment

def test_push_with_tracking():
    """Test if push used -u flag (tracking set up)."""
    output, code = run_git(["branch", "-vv"])

    if "[origin/" in output:
        print("PASS: Branch has upstream tracking")
        return 25
    else:
        print("FAIL: No upstream tracking (did you use -u flag?)")
        return 0

def test_pr_description():
    """Test PR description format (simulated)."""
    # Would use gh pr view in real scenario
    # Check for a PR description file as proxy
    pr_file = Path("starter/PR_DESCRIPTION.md")

    if pr_file.exists():
        content = pr_file.read_text()
        score = 0

        if "## Summary" in content:
            score += 10
        if "## Test Plan" in content or "## Testing" in content:
            score += 10
        if "- [" in content:  # Checklist items
            score += 5

        if score > 0:
            print(f"PASS: PR description contains required sections ({score}/25)")
        return score
    else:
        print("INFO: No PR_DESCRIPTION.md found (checking via gh in real scenario)")
        return 15  # Partial credit

def main():
    print("=" * 50)
    print("PR Creator Challenge - Test Results")
    print("=" * 50)
    print()

    total_score = 0
    total_score += test_branch_name()
    total_score += test_commit_format()
    total_score += test_function_implemented()
    total_score += test_pr_created()
    total_score += test_push_with_tracking()
    total_score += test_pr_description()

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/150")
    print("=" * 50)

    if total_score >= 135:
        print("Excellent! You've mastered the PR workflow!")
    elif total_score >= 112:
        print("Good job! Minor improvements possible.")
    else:
        print("Review the git and gh CLI workflow.")

    return 0 if total_score >= 112 else 1

if __name__ == "__main__":
    sys.exit(main())
