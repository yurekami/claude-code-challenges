#!/usr/bin/env python3
"""
File Explorer Challenge - Test Suite
Verifies that the participant correctly used Claude Code file tools.
"""

import json
import os
import sys
from pathlib import Path

EXPECTED = {
    "typescript_files": [
        "src/index.ts",
        "src/utils/helpers.ts",
        "src/utils/math.ts",
        "src/components/Button.ts",
        "src/components/Modal.ts",
    ],
    "calculateTotal_location": "src/utils/math.ts:42",
    "database_config": {
        "host": "localhost",
        "port": 5432,
        "database": "challenge_db",
        "ssl": False
    },
    "helpers_line_count": 156
}

def load_results():
    """Load the participant's results.json file."""
    results_path = Path("results.json")
    if not results_path.exists():
        print("FAIL: results.json not found")
        print("  Create results.json with your findings")
        return None

    try:
        with open(results_path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"FAIL: Invalid JSON in results.json: {e}")
        return None

def test_typescript_files(results):
    """Test if all TypeScript files were found."""
    score = 0
    found = set(results.get("typescript_files", []))
    expected = set(EXPECTED["typescript_files"])

    if found == expected:
        print("PASS: All TypeScript files found correctly")
        score = 25
    else:
        missing = expected - found
        extra = found - expected
        print("FAIL: TypeScript files mismatch")
        if missing:
            print(f"  Missing: {missing}")
        if extra:
            print(f"  Extra: {extra}")

    return score

def test_calculate_total_location(results):
    """Test if calculateTotal location is correct."""
    score = 0
    location = results.get("calculateTotal_location", "")
    expected = EXPECTED["calculateTotal_location"]

    if location == expected:
        print("PASS: calculateTotal location correct")
        score = 25
    else:
        print(f"FAIL: calculateTotal location incorrect")
        print(f"  Expected: {expected}")
        print(f"  Got: {location}")

    return score

def test_database_config(results):
    """Test if database config was extracted correctly."""
    score = 0
    config = results.get("database_config", {})
    expected = EXPECTED["database_config"]

    if config == expected:
        print("PASS: Database config extracted correctly")
        score = 25
    else:
        print("FAIL: Database config mismatch")
        print(f"  Expected: {json.dumps(expected, indent=2)}")
        print(f"  Got: {json.dumps(config, indent=2)}")

    return score

def test_line_count(results):
    """Test if line count is accurate."""
    score = 0
    count = results.get("helpers_line_count", 0)
    expected = EXPECTED["helpers_line_count"]

    if count == expected:
        print("PASS: Line count accurate")
        score = 25
    elif abs(count - expected) <= 5:
        print(f"PARTIAL: Line count close (within 5)")
        print(f"  Expected: {expected}, Got: {count}")
        score = 15
    else:
        print(f"FAIL: Line count incorrect")
        print(f"  Expected: {expected}, Got: {count}")

    return score

def main():
    print("=" * 50)
    print("File Explorer Challenge - Test Results")
    print("=" * 50)
    print()

    results = load_results()
    if results is None:
        sys.exit(1)

    total_score = 0
    total_score += test_typescript_files(results)
    total_score += test_calculate_total_location(results)
    total_score += test_database_config(results)
    total_score += test_line_count(results)

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/100")
    print("=" * 50)

    if total_score == 100:
        print("Congratulations! Challenge completed perfectly!")
    elif total_score >= 75:
        print("Good job! Minor issues to address.")
    elif total_score >= 50:
        print("Partial success. Review the failed tests.")
    else:
        print("Keep practicing! Review Claude Code file tools.")

    return 0 if total_score >= 75 else 1

if __name__ == "__main__":
    sys.exit(main())
