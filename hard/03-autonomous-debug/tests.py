#!/usr/bin/env python3
"""
Autonomous Debug Challenge - Test Suite
Verifies the complete debugging workflow.
"""

import re
import sys
from pathlib import Path

def test_bug_identified():
    """Test if the bug was correctly identified."""
    report_path = Path("debug_report.md")

    if not report_path.exists():
        print("FAIL: debug_report.md not found")
        return 0

    content = report_path.read_text().lower()

    # Check for key indicators of correct identification
    indicators = [
        ("floating" in content and "point" in content, 15, "floating point issue mentioned"),
        ("precision" in content, 10, "precision mentioned"),
        ("round" in content, 10, "rounding solution mentioned"),
        ("discount.ts" in content, 5, "correct file identified"),
    ]

    score = 0
    for condition, points, description in indicators:
        if condition:
            print(f"PASS: {description} (+{points})")
            score += points

    if score == 0:
        print("FAIL: Bug not correctly identified")

    return score

def test_root_cause_explained():
    """Test if root cause is properly explained."""
    report_path = Path("debug_report.md")

    if not report_path.exists():
        return 0

    content = report_path.read_text()

    # Check for root cause section
    if "## Root Cause" in content or "### Root Cause" in content:
        # Check explanation quality
        explanation_keywords = [
            "javascript", "ieee", "754", "binary", "decimal",
            "representation", "0.1", "0.2", "precision", "floating"
        ]

        found = sum(1 for kw in explanation_keywords if kw.lower() in content.lower())

        if found >= 3:
            print(f"PASS: Root cause well explained ({found} key concepts)")
            return 40
        elif found >= 1:
            print(f"PARTIAL: Root cause mentioned but could be more detailed")
            return 20
        else:
            print("FAIL: Root cause section exists but lacks technical detail")
            return 10
    else:
        print("FAIL: No root cause section found")
        return 0

def test_fix_implemented():
    """Test if the fix was correctly implemented."""
    discount_path = Path("starter/src/cart/discount.ts")

    if not discount_path.exists():
        print("FAIL: discount.ts not found")
        return 0

    content = discount_path.read_text()

    # Check for rounding fix
    fix_patterns = [
        (r"Math\.round\(.+\*\s*100\)\s*/\s*100", "Math.round pattern"),
        (r"\.toFixed\(2\)", "toFixed(2) pattern"),
        (r"Number\(.+\.toFixed", "Number(toFixed) pattern"),
    ]

    for pattern, description in fix_patterns:
        if re.search(pattern, content):
            print(f"PASS: Fix implemented using {description}")
            return 50

    # Check if at least something changed
    if "round" in content.lower() or "toFixed" in content:
        print("PARTIAL: Some rounding added but may not be correct")
        return 25

    print("FAIL: No fix detected in discount.ts")
    return 0

def test_new_test_added():
    """Test if a new test case was added."""
    test_path = Path("starter/src/cart/cart.test.ts")

    if not test_path.exists():
        print("FAIL: cart.test.ts not found")
        return 0

    content = test_path.read_text()

    # Check for new test that specifically tests the bug
    new_test_indicators = [
        "SAVE20" in content and "100" in content,
        "80" in content and "expect" in content,
        "precision" in content.lower(),
        "toBeCloseTo" in content,
    ]

    if sum(new_test_indicators) >= 2:
        print("PASS: New test case added for the specific bug")
        return 40
    elif sum(new_test_indicators) >= 1:
        print("PARTIAL: Test added but may not fully cover the bug")
        return 20
    else:
        print("FAIL: No new test case for the reported bug")
        return 0

def test_all_tests_pass():
    """Test if all tests pass (simulated)."""
    # In real scenario, would run: npm test
    # For now, check if solution section exists and makes sense

    test_path = Path("starter/src/cart/cart.test.ts")
    discount_path = Path("starter/src/cart/discount.ts")

    if not test_path.exists() or not discount_path.exists():
        print("FAIL: Required files missing")
        return 0

    # Check that the fix doesn't break the test structure
    test_content = test_path.read_text()

    if "describe(" in test_content and "it(" in test_content:
        print("PASS: Test file structure intact")
        return 30
    else:
        print("FAIL: Test file structure damaged")
        return 0

def test_report_complete():
    """Test if the debug report is comprehensive."""
    report_path = Path("debug_report.md")

    if not report_path.exists():
        print("FAIL: debug_report.md not found")
        return 0

    content = report_path.read_text()

    sections = [
        ("## Bug Summary" in content or "# Bug" in content, 10, "Bug Summary"),
        ("## Root Cause" in content, 10, "Root Cause"),
        ("## Files Affected" in content or "Files:" in content, 10, "Files Affected"),
        ("## The Fix" in content or "Fix:" in content, 10, "The Fix"),
        ("## Test" in content, 5, "Test Coverage"),
        ("## Prevention" in content, 5, "Prevention"),
    ]

    score = 0
    for condition, points, section_name in sections:
        if condition:
            score += points
        else:
            print(f"MISSING: {section_name} section")

    if score >= 40:
        print(f"PASS: Report has most required sections ({score}/50)")
    else:
        print(f"PARTIAL: Report incomplete ({score}/50)")

    return score

def main():
    print("=" * 50)
    print("Autonomous Debug Challenge - Test Results")
    print("=" * 50)
    print()

    total_score = 0
    total_score += test_bug_identified()
    total_score += test_root_cause_explained()
    total_score += test_fix_implemented()
    total_score += test_new_test_added()
    total_score += test_all_tests_pass()
    total_score += test_report_complete()

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/250")
    print("=" * 50)

    if total_score >= 225:
        print("Excellent! You've mastered autonomous debugging!")
    elif total_score >= 187:
        print("Good debugging skills! Minor improvements possible.")
    else:
        print("Review the debugging workflow and try again.")

    return 0 if total_score >= 187 else 1

if __name__ == "__main__":
    sys.exit(main())
