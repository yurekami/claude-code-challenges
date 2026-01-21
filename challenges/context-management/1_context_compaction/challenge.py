"""
Challenge: Context Compaction

Master manual context compaction to maintain Claude Code performance.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "lib"))

from challenge_base import (
    ChallengeBase,
    Category,
    Difficulty,
    ValidationType,
    ValidationResult,
    TestCase,
)
from typing import Any, Dict, List
import re


class Challenge(ChallengeBase):
    """Context Compaction - Context Management Challenge 1."""

    def __init__(self):
        super().__init__(
            name="Context Compaction",
            category=Category.CONTEXT_MANAGEMENT,
            difficulty=Difficulty.MEDIUM,
            validation_type=ValidationType.COMMAND,
            description="Learn to effectively compact context while preserving critical information",
            related_tips=[8],
            prerequisites=["cli-fundamentals/1_status_line_setup"],
            time_estimate_minutes=15,
        )

    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate the user's context compaction workflow.

        Expected submission format:
        {
            "commands": ["command1", "command2", ...],
            "before_tokens": 150000,
            "after_tokens": 45000,
            "preserved_info": ["item1", "item2", ...]
        }
        """
        commands = submission.get("commands", [])
        before = submission.get("before_tokens", 0)
        after = submission.get("after_tokens", 0)
        preserved = submission.get("preserved_info", [])

        feedback_items = []
        score = 0.0

        # Check for usage command
        commands_text = " ".join(commands).lower()
        has_usage = bool(re.search(r"/usage|tokens?|context", commands_text))
        if has_usage:
            score += 0.2
            feedback_items.append("Good: Checked token usage")
        else:
            feedback_items.append("Missing: Token usage check before/after")

        # Check for compact command with instructions
        has_compact = bool(re.search(r"/compact", commands_text))
        has_instructions = bool(re.search(r"preserve|keep|maintain|save", commands_text))

        if has_compact:
            score += 0.2
            feedback_items.append("Good: Used /compact command")
            if has_instructions:
                score += 0.2
                feedback_items.append("Good: Provided compaction instructions")
            else:
                feedback_items.append("Tip: Add specific instructions to /compact about what to preserve")
        else:
            feedback_items.append("Missing: /compact command not detected")

        # Check token reduction
        if before > 0 and after > 0:
            reduction = (before - after) / before
            if reduction >= 0.5:  # At least 50% reduction
                score += 0.2
                feedback_items.append(f"Great: Achieved {reduction:.0%} token reduction")
            elif reduction > 0:
                score += 0.1
                feedback_items.append(f"Partial: Only {reduction:.0%} reduction (target: 50%+)")
            else:
                feedback_items.append("Issue: Token count did not decrease")
        else:
            feedback_items.append("Missing: Before/after token counts not provided")

        # Check preserved information
        expected_preserved = ["bug", "hypothesis", "file", "path", "test", "result"]
        preserved_text = " ".join(preserved).lower()
        preserved_count = sum(1 for item in expected_preserved if item in preserved_text)

        if preserved_count >= 3:
            score += 0.2
            feedback_items.append(f"Good: Preserved {preserved_count} key context items")
        elif preserved_count > 0:
            score += 0.1
            feedback_items.append(f"Partial: Only preserved {preserved_count}/3 key items")
        else:
            feedback_items.append("Missing: Specify what information was preserved")

        passed = score >= 0.7

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_items),
            details={
                "has_usage_check": has_usage,
                "has_compact": has_compact,
                "has_instructions": has_instructions,
                "token_reduction": (before - after) / before if before > 0 else 0,
            },
        )

    def generate_test_cases(self) -> List[TestCase]:
        return [
            TestCase(
                name="Complete workflow",
                description="Full compaction with all elements",
                input_data={
                    "commands": [
                        "/usage",
                        "/compact preserve the current bug hypothesis about null pointer, "
                        "keep file paths src/main.py and tests/test_main.py, "
                        "and maintain the test results showing 3 failures",
                        "/usage"
                    ],
                    "before_tokens": 150000,
                    "after_tokens": 45000,
                    "preserved_info": [
                        "bug hypothesis: null pointer in data processing",
                        "files: src/main.py, tests/test_main.py",
                        "test results: 3 failures"
                    ]
                },
                expected={"passed": True},
            ),
        ]

    def get_hints(self) -> List[str]:
        return [
            "Check token usage with /usage before and after",
            "The /compact command accepts natural language instructions",
            "Be specific about what debugging context to preserve",
        ]

    def get_learning_objectives(self) -> List[str]:
        return [
            "Understand context window limits and their impact",
            "Master manual context compaction",
            "Learn to preserve critical information during compaction",
        ]
