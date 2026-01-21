#!/usr/bin/env python3
"""
Token Check Challenge - Test Suite
Verifies that the participant understands token management.
"""

import os
import re
import sys
from pathlib import Path

def load_report():
    """Load the participant's usage report."""
    report_path = Path("usage_report.md")
    if not report_path.exists():
        print("FAIL: usage_report.md not found")
        return None

    with open(report_path) as f:
        return f.read()

def test_token_counts(report):
    """Test if token counts are present and reasonable."""
    score = 0

    # Check for input tokens
    input_match = re.search(r'[Ii]nput tokens[^:]*:\s*(\d+)', report)
    if input_match:
        input_tokens = int(input_match.group(1))
        if input_tokens > 0:
            print(f"PASS: Input tokens reported ({input_tokens})")
            score += 10
        else:
            print("FAIL: Input tokens should be > 0")
    else:
        print("FAIL: Input tokens not found")

    # Check for output tokens
    output_match = re.search(r'[Oo]utput tokens[^:]*:\s*(\d+)', report)
    if output_match:
        output_tokens = int(output_match.group(1))
        if output_tokens > 0:
            print(f"PASS: Output tokens reported ({output_tokens})")
            score += 10
        else:
            print("FAIL: Output tokens should be > 0")
    else:
        print("FAIL: Output tokens not found")

    # Check for total tokens
    total_match = re.search(r'[Tt]otal tokens[^:]*:\s*(\d+)', report)
    if total_match:
        print(f"PASS: Total tokens reported")
        score += 10
    else:
        print("INFO: Total tokens not explicitly listed")
        score += 5

    return score

def test_context_percentage(report):
    """Test if context usage percentage is reported."""
    pattern = r'[Cc]ontext[^:]*:\s*(\d+(?:\.\d+)?)\s*%'
    match = re.search(pattern, report)

    if match:
        percentage = float(match.group(1))
        if 0 <= percentage <= 100:
            print(f"PASS: Context usage reported ({percentage}%)")
            return 20
        else:
            print(f"FAIL: Invalid percentage ({percentage}%)")
            return 5
    else:
        print("FAIL: Context percentage not found")
        return 0

def test_compaction_recommendation(report):
    """Test if compaction recommendation is reasonable."""
    score = 0

    # Check for Yes/No recommendation
    compact_match = re.search(r'[Ss]hould compact[^:]*:\s*(Yes|No|yes|no)', report)
    if compact_match:
        print("PASS: Compaction recommendation provided")
        score += 10

        # Check for reason
        reason_match = re.search(r'[Rr]eason:\s*(.+)', report)
        if reason_match and len(reason_match.group(1)) > 10:
            print("PASS: Reason provided")
            score += 15
        else:
            print("PARTIAL: Reason missing or too brief")
            score += 5
    else:
        print("FAIL: Compaction recommendation not found")

    return score

def test_compact_explanation(report):
    """Test if explanation of /compact is clear."""
    score = 0

    # Check for section about when to compact
    has_section = bool(re.search(r'[Ww]hen to [Cc]ompact', report))

    # Keywords that should appear in a good explanation
    keywords = ['context', 'token', 'summarize', 'conversation', 'space', 'memory']
    keyword_count = sum(1 for kw in keywords if kw.lower() in report.lower())

    if has_section:
        score += 10
        print("PASS: 'When to Compact' section found")

    if keyword_count >= 3:
        print(f"PASS: Good explanation with {keyword_count} relevant concepts")
        score += 15
    elif keyword_count >= 1:
        print(f"PARTIAL: Basic explanation ({keyword_count} concepts)")
        score += 8
    else:
        print("FAIL: Explanation lacks key concepts")

    return score

def main():
    print("=" * 50)
    print("Token Check Challenge - Test Results")
    print("=" * 50)
    print()

    report = load_report()
    if report is None:
        print("\nCreate usage_report.md with your findings.")
        sys.exit(1)

    print("Report content preview:")
    print("-" * 40)
    print(report[:500] + "..." if len(report) > 500 else report)
    print("-" * 40)
    print()

    total_score = 0
    total_score += test_token_counts(report)
    total_score += test_context_percentage(report)
    total_score += test_compaction_recommendation(report)
    total_score += test_compact_explanation(report)

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/100")
    print("=" * 50)

    if total_score == 100:
        print("Excellent! You understand Claude Code context management!")
    elif total_score >= 75:
        print("Good understanding! Minor details to improve.")
    else:
        print("Review the /usage and /compact commands.")

    return 0 if total_score >= 75 else 1

if __name__ == "__main__":
    sys.exit(main())
