#!/usr/bin/env python3
"""
Quick Commit Challenge - Test Suite
Verifies that the participant created a proper conventional commit.
"""

import re
import subprocess
import sys

VALID_TYPES = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'perf', 'ci', 'build']

def get_last_commit():
    """Get the last commit message."""
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--pretty=format:%B'],
            capture_output=True,
            text=True,
            cwd='starter'
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting commit: {e}")
        return None

def test_commit_exists():
    """Test if a commit was made."""
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--oneline'],
            capture_output=True,
            text=True,
            cwd='starter'
        )
        if result.returncode != 0:
            print("FAIL: No commits found")
            return False
        print("PASS: Commit exists")
        return True
    except Exception:
        print("FAIL: Could not check git history")
        return False

def test_commit_type(message):
    """Test if commit has valid type."""
    first_line = message.split('\n')[0]

    # Pattern: type(scope): description OR type: description
    pattern = r'^(' + '|'.join(VALID_TYPES) + r')(\([^)]+\))?:\s+.+'

    if re.match(pattern, first_line):
        match = re.match(r'^(\w+)', first_line)
        commit_type = match.group(1) if match else 'unknown'
        print(f"PASS: Valid commit type '{commit_type}'")
        return 25
    else:
        print(f"FAIL: Invalid commit type or format")
        print(f"  First line: {first_line}")
        print(f"  Expected: <type>[(scope)]: <description>")
        return 0

def test_commit_format(message):
    """Test if commit follows proper format."""
    score = 0
    first_line = message.split('\n')[0]

    # Check length
    if len(first_line) <= 72:
        print("PASS: Subject line under 72 characters")
        score += 10
    else:
        print(f"FAIL: Subject line too long ({len(first_line)} chars)")

    # Check not all caps
    if first_line != first_line.upper():
        score += 5
    else:
        print("FAIL: Subject line should not be all caps")

    # Check starts with lowercase after type
    pattern = r'^[a-z]+(\([^)]+\))?:\s+[a-z]'
    if re.match(pattern, first_line):
        print("PASS: Proper case formatting")
        score += 10
    else:
        print("INFO: Consider starting description with lowercase")
        score += 5

    return score

def test_description_quality(message):
    """Test if description is meaningful."""
    first_line = message.split('\n')[0]

    # Extract description part
    match = re.match(r'^[^:]+:\s+(.+)$', first_line)
    if not match:
        print("FAIL: Could not extract description")
        return 0

    description = match.group(1)

    # Check it's not generic
    generic_phrases = ['update', 'changes', 'stuff', 'fix', 'things', 'misc']
    if description.lower().strip() in generic_phrases:
        print(f"FAIL: Description too generic: '{description}'")
        return 0

    # Check minimum length
    if len(description) < 10:
        print(f"FAIL: Description too short: '{description}'")
        return 10

    print(f"PASS: Descriptive commit message")
    return 25

def test_co_authored_by(message):
    """Test if co-authored-by footer is present."""
    if 'Co-Authored-By:' in message or 'Co-authored-by:' in message:
        if 'Claude' in message or 'claude' in message:
            print("PASS: Co-Authored-By footer present")
            return 25
        else:
            print("PARTIAL: Co-Authored-By present but missing Claude attribution")
            return 15
    else:
        print("FAIL: Missing Co-Authored-By footer")
        return 0

def main():
    print("=" * 50)
    print("Quick Commit Challenge - Test Results")
    print("=" * 50)
    print()

    if not test_commit_exists():
        print("\nNo commit found. Please create a commit first.")
        sys.exit(1)

    message = get_last_commit()
    if not message:
        print("Could not read commit message")
        sys.exit(1)

    print(f"\nCommit message:\n{'-' * 40}")
    print(message)
    print(f"{'-' * 40}\n")

    total_score = 0
    total_score += test_commit_type(message)
    total_score += test_commit_format(message)
    total_score += test_description_quality(message)
    total_score += test_co_authored_by(message)

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/100")
    print("=" * 50)

    if total_score == 100:
        print("Perfect! You've mastered conventional commits!")
    elif total_score >= 75:
        print("Great job! Minor improvements possible.")
    else:
        print("Review conventional commit guidelines.")

    return 0 if total_score >= 75 else 1

if __name__ == "__main__":
    sys.exit(main())
