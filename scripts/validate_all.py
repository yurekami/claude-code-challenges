#!/usr/bin/env python3
"""
Validate all challenges in the repository.

Usage:
    python scripts/validate_all.py
"""

import sys
from pathlib import Path

# Add lib to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "lib"))

from challenge_base import load_challenge


def find_challenges(challenges_dir: Path):
    """Find all challenge directories."""
    challenges = []

    for category_dir in sorted(challenges_dir.iterdir()):
        if not category_dir.is_dir():
            continue

        for challenge_dir in sorted(category_dir.iterdir()):
            if not challenge_dir.is_dir():
                continue

            challenge_py = challenge_dir / "challenge.py"
            if challenge_py.exists():
                challenges.append(challenge_dir)

    return challenges


def validate_challenge(challenge_dir: Path) -> tuple[bool, str]:
    """Validate a single challenge."""
    try:
        challenge = load_challenge(str(challenge_dir))

        # Run test cases
        test_cases = challenge.generate_test_cases()
        passed = 0
        failed = 0

        for test in test_cases:
            result = challenge.validate(test.input_data)
            expected_pass = test.expected.get("passed", True)

            if result.passed == expected_pass:
                passed += 1
            else:
                failed += 1

        if failed == 0:
            return True, f"All {passed} tests passed"
        else:
            return False, f"{failed}/{passed + failed} tests failed"

    except Exception as e:
        return False, f"Error: {e}"


def main():
    challenges_dir = project_root / "challenges"

    if not challenges_dir.exists():
        print("No challenges directory found")
        sys.exit(1)

    challenges = find_challenges(challenges_dir)
    print(f"Found {len(challenges)} challenges\n")

    results = []
    for challenge_dir in challenges:
        rel_path = challenge_dir.relative_to(challenges_dir)
        success, message = validate_challenge(challenge_dir)
        results.append((rel_path, success, message))

        status = "PASS" if success else "FAIL"
        print(f"[{status}] {rel_path}: {message}")

    # Summary
    print()
    passed = sum(1 for _, success, _ in results if success)
    failed = len(results) - passed

    print(f"Summary: {passed} passed, {failed} failed")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
