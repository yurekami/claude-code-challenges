#!/usr/bin/env python3
"""
Simple Edit Challenge - Test Suite
Verifies that all edits were made correctly.
"""

import sys
from pathlib import Path

def load_file():
    """Load the edited app.ts file."""
    file_path = Path("starter/app.ts")
    if not file_path.exists():
        print("FAIL: starter/app.ts not found")
        return None

    with open(file_path) as f:
        return f.read()

def test_variable_name(content):
    """Test if variable name was fixed."""
    if 'const userName' in content and 'usrName' not in content:
        print("PASS: Variable name fixed (usrName -> userName)")
        return 25
    elif 'userName' in content:
        print("PARTIAL: userName found but usrName still exists")
        return 10
    else:
        print("FAIL: Variable name not fixed")
        print("  Expected: const userName")
        return 0

def test_return_type(content):
    """Test if return type was updated."""
    if 'function getData(): Promise<Data>' in content:
        print("PASS: Return type updated to Promise<Data>")
        return 25
    elif 'Promise<Data>' in content:
        print("PARTIAL: Promise<Data> found but format may be off")
        return 15
    elif ': any' in content and 'getData' in content:
        print("FAIL: Return type still 'any'")
        return 0
    else:
        print("FAIL: Return type not correctly updated")
        return 0

def test_parameter_type(content):
    """Test if parameter type was added."""
    if 'function processItem(item: Item)' in content:
        print("PASS: Parameter type added (item: Item)")
        return 25
    elif 'item: Item' in content:
        print("PARTIAL: Type found but format may differ")
        return 15
    elif 'function processItem(item)' in content:
        print("FAIL: Parameter still untyped")
        return 0
    else:
        print("FAIL: processItem function not found or malformed")
        return 0

def test_import_statement(content):
    """Test if import was updated."""
    if "import { helper, utils }" in content:
        print("PASS: Import updated to include utils")
        return 25
    elif "utils" in content and "import" in content:
        # Check various valid import formats
        if "helper" in content and "utils" in content:
            print("PARTIAL: Both helper and utils imported (format may vary)")
            return 20
    elif "import { helper }" in content:
        print("FAIL: Import not updated - still only 'helper'")
        return 0

    print("FAIL: Import statement issue")
    return 0

def test_no_major_changes(content):
    """Verify the file wasn't completely rewritten."""
    expected_elements = [
        'interface Data',
        'interface Item',
        'async function main()',
        'fetch(\'/api/data\')',
        "console.log(`Hello,"
    ]

    missing = [elem for elem in expected_elements if elem not in content]

    if not missing:
        print("INFO: File structure preserved (good!)")
        return True
    else:
        print(f"WARNING: Some expected content missing: {missing}")
        print("  The Edit tool should make minimal changes")
        return False

def main():
    print("=" * 50)
    print("Simple Edit Challenge - Test Results")
    print("=" * 50)
    print()

    content = load_file()
    if content is None:
        sys.exit(1)

    total_score = 0
    total_score += test_variable_name(content)
    total_score += test_return_type(content)
    total_score += test_parameter_type(content)
    total_score += test_import_statement(content)

    print()
    test_no_major_changes(content)

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/100")
    print("=" * 50)

    if total_score == 100:
        print("Perfect! You've mastered the Edit tool!")
    elif total_score >= 75:
        print("Great work! Minor edits needed.")
    else:
        print("Review the Edit tool documentation.")

    return 0 if total_score >= 75 else 1

if __name__ == "__main__":
    sys.exit(main())
