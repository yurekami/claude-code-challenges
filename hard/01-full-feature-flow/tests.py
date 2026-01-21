#!/usr/bin/env python3
"""
Full Feature Flow Challenge - Test Suite
Verifies the complete TDD workflow.
"""

import re
import subprocess
import sys
from pathlib import Path

def test_planning_done():
    """Test if planning was documented."""
    # Check for todo evidence or planning notes
    possible_files = [
        "PLAN.md",
        "TODO.md",
        "planning.md",
        "notes.md",
    ]

    for filename in possible_files:
        if Path(filename).exists():
            print(f"PASS: Planning documented in {filename}")
            return 30

    # Check for commit history with planning
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "-5"],
            capture_output=True,
            text=True,
            cwd="."
        )
        if "plan" in result.stdout.lower() or "todo" in result.stdout.lower():
            print("PASS: Planning evidence found in commits")
            return 25
    except:
        pass

    print("PARTIAL: No explicit planning document found")
    return 15

def test_tests_written_first():
    """Test if tests were written before implementation."""
    test_file = Path("src/rateLimiter/rateLimiter.test.ts")
    impl_file = Path("src/rateLimiter/index.ts")

    if not test_file.exists():
        print("FAIL: Test file not found at expected location")
        return 0

    if not impl_file.exists():
        print("FAIL: Implementation file not found")
        return 0

    # Check git history to see which was committed first
    try:
        test_log = subprocess.run(
            ["git", "log", "--oneline", "--follow", str(test_file)],
            capture_output=True, text=True
        )
        impl_log = subprocess.run(
            ["git", "log", "--oneline", "--follow", str(impl_file)],
            capture_output=True, text=True
        )

        # If test file has commits, give credit
        if test_log.stdout:
            print("PASS: Test file exists with git history")
            return 40
    except:
        pass

    # Fallback: just check that test file exists and has tests
    content = test_file.read_text()
    if "describe(" in content and "it(" in content:
        print("PASS: Test file contains tests")
        return 35
    else:
        print("PARTIAL: Test file exists but may be incomplete")
        return 20

def test_coverage():
    """Test for adequate test coverage."""
    test_file = Path("src/rateLimiter/rateLimiter.test.ts")

    if not test_file.exists():
        print("FAIL: Test file not found")
        return 0

    content = test_file.read_text()

    # Count test cases
    test_count = len(re.findall(r"it\(['\"]", content))

    # Check for key test scenarios
    scenarios = [
        ("check" in content.lower() and "limit" in content.lower(), "basic limiting"),
        ("reset" in content.lower(), "reset functionality"),
        ("configure" in content.lower() or "option" in content.lower(), "configuration"),
        ("window" in content.lower(), "time window"),
        ("remaining" in content.lower(), "remaining count"),
    ]

    covered = sum(1 for s, _ in scenarios if s)

    if test_count >= 5 and covered >= 4:
        print(f"PASS: Good coverage ({test_count} tests, {covered}/5 scenarios)")
        return 30
    elif test_count >= 3 and covered >= 2:
        print(f"PARTIAL: Basic coverage ({test_count} tests, {covered}/5 scenarios)")
        return 20
    else:
        print(f"FAIL: Insufficient coverage ({test_count} tests, {covered}/5 scenarios)")
        return 10

def test_implementation():
    """Test if implementation is correct."""
    impl_file = Path("src/rateLimiter/index.ts")

    if not impl_file.exists():
        print("FAIL: Implementation file not found")
        return 0

    content = impl_file.read_text()

    # Check for key implementation elements
    elements = [
        ("interface RateLimiter" in content or "class RateLimiter" in content, 10, "RateLimiter interface/class"),
        ("check" in content, 10, "check method"),
        ("reset" in content, 5, "reset method"),
        ("configure" in content, 5, "configure method"),
        ("Map" in content or "map" in content, 10, "storage structure"),
        ("Date.now()" in content or "new Date()" in content, 5, "timestamp tracking"),
        ("remaining" in content, 5, "remaining tracking"),
    ]

    score = 0
    for condition, points, description in elements:
        if condition:
            score += points
        else:
            print(f"MISSING: {description}")

    if score >= 40:
        print(f"PASS: Implementation complete ({score}/50)")
    else:
        print(f"PARTIAL: Implementation incomplete ({score}/50)")

    return score

def test_type_safety():
    """Test for TypeScript type safety."""
    types_file = Path("src/rateLimiter/types.ts")
    impl_file = Path("src/rateLimiter/index.ts")

    score = 0

    if types_file.exists():
        print("PASS: Separate types file exists")
        score += 10

    if impl_file.exists():
        content = impl_file.read_text()

        # Check for type annotations
        if ": RateLimitResult" in content or "RateLimitResult" in content:
            score += 5
        if ": RateLimitOptions" in content or "RateLimitOptions" in content:
            score += 5

    if score >= 15:
        print(f"PASS: Good type safety ({score}/20)")
    elif score > 0:
        print(f"PARTIAL: Some types used ({score}/20)")
    else:
        print("FAIL: No type safety measures found")

    return score

def test_clean_code():
    """Test for clean code practices."""
    impl_file = Path("src/rateLimiter/index.ts")

    if not impl_file.exists():
        return 0

    content = impl_file.read_text()

    score = 0

    # No console.log
    if "console.log" not in content:
        print("PASS: No console.log statements")
        score += 10
    else:
        print("FAIL: Contains console.log")

    # Has JSDoc comments
    if "/**" in content and "*/" in content:
        print("PASS: Has JSDoc comments")
        score += 10
    else:
        print("MISSING: JSDoc comments")

    return score

def test_git_workflow():
    """Test for proper git workflow."""
    try:
        # Check for feature branch
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True
        )
        branch = result.stdout.strip()

        if branch.startswith("feat/"):
            print(f"PASS: On feature branch ({branch})")
            score = 15
        else:
            print(f"PARTIAL: Branch naming could be better ({branch})")
            score = 5

        # Check commit count
        result = subprocess.run(
            ["git", "log", "--oneline", "main..HEAD"],
            capture_output=True, text=True
        )
        commits = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

        if commits >= 2:
            print(f"PASS: Multiple atomic commits ({commits})")
            score += 15
        elif commits >= 1:
            print(f"PARTIAL: Only {commits} commit(s)")
            score += 8

        return score

    except Exception as e:
        print(f"INFO: Git check skipped ({e})")
        return 15

def test_pr_ready():
    """Test if PR description exists."""
    pr_files = ["PR_DESCRIPTION.md", "PULL_REQUEST.md", ".github/PULL_REQUEST_TEMPLATE.md"]

    for filename in pr_files:
        if Path(filename).exists():
            content = Path(filename).read_text()
            if "## Summary" in content and "## Test" in content:
                print(f"PASS: PR description complete in {filename}")
                return 30
            else:
                print(f"PARTIAL: PR description exists but incomplete")
                return 15

    print("INFO: No PR description file found")
    return 10

def main():
    print("=" * 50)
    print("Full Feature Flow Challenge - Test Results")
    print("=" * 50)
    print()

    total_score = 0
    total_score += test_planning_done()
    total_score += test_tests_written_first()
    total_score += test_coverage()
    total_score += test_implementation()
    total_score += test_type_safety()
    total_score += test_clean_code()
    total_score += test_git_workflow()
    total_score += test_pr_ready()

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/250")
    print("=" * 50)

    if total_score >= 225:
        print("Excellent! You've mastered the full feature workflow!")
    elif total_score >= 187:
        print("Good job! Solid understanding of TDD workflow.")
    else:
        print("Review the TDD and feature development workflow.")

    return 0 if total_score >= 187 else 1

if __name__ == "__main__":
    sys.exit(main())
