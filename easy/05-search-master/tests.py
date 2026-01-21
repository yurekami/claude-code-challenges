#!/usr/bin/env python3
"""
Search Master Challenge - Test Suite
Verifies that search results are accurate.
"""

import json
import sys
from pathlib import Path

EXPECTED = {
    "todo_files": [
        "starter/src/api.ts",
        "starter/src/utils/helpers.ts",
        "starter/src/components/Form.tsx"
    ],
    "async_function_count": 4,
    "util_import_count": 3,
    "console_log_count": 12
}

def load_results():
    """Load the participant's search results."""
    results_path = Path("search_results.json")
    if not results_path.exists():
        print("FAIL: search_results.json not found")
        return None

    try:
        with open(results_path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"FAIL: Invalid JSON: {e}")
        return None

def normalize_paths(paths):
    """Normalize file paths for comparison."""
    normalized = set()
    for p in paths:
        # Remove leading ./ and normalize separators
        p = p.replace('\\', '/').lstrip('./')
        # Handle with or without starter/ prefix
        if not p.startswith('starter/'):
            p = 'starter/' + p
        normalized.add(p)
    return normalized

def test_todo_files(results):
    """Test if TODO files were found correctly."""
    found = results.get("todo_files", [])
    found_normalized = normalize_paths(found)
    expected_normalized = normalize_paths(EXPECTED["todo_files"])

    matches = found_normalized & expected_normalized
    score = len(matches) / len(expected_normalized) * 25

    if found_normalized == expected_normalized:
        print("PASS: All TODO files found correctly")
        return 25
    else:
        missing = expected_normalized - found_normalized
        extra = found_normalized - expected_normalized
        print(f"PARTIAL: Found {len(matches)}/{len(expected_normalized)} TODO files")
        if missing:
            print(f"  Missing: {missing}")
        if extra:
            print(f"  Extra (may be valid): {extra}")
        return int(score)

def test_async_functions(results):
    """Test if async functions were found."""
    async_funcs = results.get("async_functions", [])

    if not async_funcs:
        print("FAIL: No async functions found")
        return 0

    # Check structure
    has_file = all('file' in f for f in async_funcs)
    has_line = all('line' in f for f in async_funcs)

    score = 0
    if len(async_funcs) >= EXPECTED["async_function_count"]:
        print(f"PASS: Found {len(async_funcs)} async functions")
        score += 15
    else:
        print(f"PARTIAL: Found {len(async_funcs)}, expected at least {EXPECTED['async_function_count']}")
        score += 8

    if has_file and has_line:
        print("PASS: Results include file and line numbers")
        score += 10
    else:
        print("FAIL: Missing file or line number information")

    return score

def test_util_imports(results):
    """Test if @/utils imports were found."""
    imports = results.get("util_imports", [])

    if not imports:
        print("FAIL: No @/utils imports found")
        return 0

    if len(imports) >= EXPECTED["util_import_count"]:
        print(f"PASS: Found {len(imports)} @/utils imports")
        return 25
    else:
        print(f"PARTIAL: Found {len(imports)}, expected at least {EXPECTED['util_import_count']}")
        return 15

def test_console_count(results):
    """Test if console.log count is accurate."""
    count = results.get("console_log_count", 0)
    expected = EXPECTED["console_log_count"]

    if count == expected:
        print(f"PASS: Console.log count correct ({count})")
        return 25
    elif abs(count - expected) <= 2:
        print(f"PARTIAL: Count close ({count}, expected {expected})")
        return 15
    else:
        print(f"FAIL: Count incorrect ({count}, expected {expected})")
        return 0

def main():
    print("=" * 50)
    print("Search Master Challenge - Test Results")
    print("=" * 50)
    print()

    results = load_results()
    if results is None:
        print("\nCreate search_results.json with your findings.")
        sys.exit(1)

    total_score = 0
    total_score += test_todo_files(results)
    total_score += test_async_functions(results)
    total_score += test_util_imports(results)
    total_score += test_console_count(results)

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/100")
    print("=" * 50)

    if total_score == 100:
        print("Excellent! You've mastered the search tools!")
    elif total_score >= 75:
        print("Good job! Minor search improvements possible.")
    else:
        print("Review Grep and Glob tool documentation.")

    return 0 if total_score >= 75 else 1

if __name__ == "__main__":
    sys.exit(main())
