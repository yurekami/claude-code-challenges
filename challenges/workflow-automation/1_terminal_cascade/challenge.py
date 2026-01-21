"""
Challenge: Terminal Cascade Method

Organize multiple Claude Code sessions using the cascade method.
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
    """Terminal Cascade - Workflow Automation Challenge 1."""

    def __init__(self):
        super().__init__(
            name="Terminal Cascade Method",
            category=Category.WORKFLOW_AUTOMATION,
            difficulty=Difficulty.MEDIUM,
            validation_type=ValidationType.OUTPUT,
            description="Organize multiple Claude Code sessions efficiently",
            related_tips=[14],
            prerequisites=["cli-fundamentals/1_status_line_setup"],
            time_estimate_minutes=15,
        )

    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate cascade method implementation.

        Expected submission format:
        {
            "organization": "description of terminal organization",
            "session_commands": ["cmd for session A", "cmd for B", "cmd for C"],
            "switching_pattern": "description of how you switch between tabs",
            "progress_tracking": "how you tracked progress"
        }
        """
        org = submission.get("organization", "")
        sessions = submission.get("session_commands", [])
        switching = submission.get("switching_pattern", "")
        tracking = submission.get("progress_tracking", "")

        feedback_items = []
        score = 0.0

        # Check organization description
        org_lower = org.lower()
        org_indicators = ["tab", "left", "right", "window", "terminal", "order"]
        if any(ind in org_lower for ind in org_indicators):
            score += 0.2
            feedback_items.append("Good: Terminal organization described")
        else:
            feedback_items.append("Tip: Describe your terminal tab organization")

        # Check for multiple sessions
        if len(sessions) >= 3:
            score += 0.2
            feedback_items.append(f"Good: {len(sessions)} sessions configured")

            # Check if sessions have context
            sessions_text = " ".join(sessions).lower()
            if "claude" in sessions_text:
                score += 0.1
                feedback_items.append("Good: Claude Code commands found")

            # Check for context-specific sessions
            context_patterns = ["review", "test", "debug", "pr", "ci", "feature"]
            contexts_found = sum(1 for p in context_patterns if p in sessions_text)
            if contexts_found >= 2:
                score += 0.1
                feedback_items.append("Good: Sessions have distinct contexts")
        else:
            feedback_items.append("Missing: Need at least 3 session commands")

        # Check switching pattern
        switching_lower = switching.lower()
        switch_indicators = ["left", "right", "tab", "check", "sweep", "cmd", "ctrl", "shortcut"]
        if any(ind in switching_lower for ind in switch_indicators):
            score += 0.2
            feedback_items.append("Good: Switching pattern explained")
        else:
            feedback_items.append("Tip: Describe how you navigate between tabs")

        # Check progress tracking
        tracking_lower = tracking.lower()
        track_indicators = ["status", "check", "output", "result", "done", "complete", "progress"]
        if any(ind in tracking_lower for ind in track_indicators):
            score += 0.2
            feedback_items.append("Good: Progress tracking method described")
        else:
            feedback_items.append("Tip: Explain how you monitor task progress")

        passed = score >= 0.6

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_items),
            details={
                "session_count": len(sessions),
                "has_organization": score >= 0.2,
            },
        )

    def generate_test_cases(self) -> List[TestCase]:
        return [
            TestCase(
                name="Three-task cascade",
                description="Complete cascade with three tasks",
                input_data={
                    "organization": "Three terminal tabs ordered left-to-right: PR review, tests, CI debug",
                    "session_commands": [
                        "claude -p 'Review PR #123 for security issues'",
                        "claude -p 'Write unit tests for auth module'",
                        "claude -p 'Debug failing CI workflow'"
                    ],
                    "switching_pattern": "Cmd+Shift+] to move right, Cmd+Shift+[ to move left. Sweep left-to-right every 10 minutes.",
                    "progress_tracking": "Check each session's output, look for completion indicators or blocking issues"
                },
                expected={"passed": True},
            ),
        ]

    def get_hints(self) -> List[str]:
        return [
            "New tabs should open to the right of current tab",
            "Use keyboard shortcuts for quick tab navigation",
            "Check tabs in a consistent left-to-right pattern",
            "Keep each session focused on one task",
        ]

    def get_learning_objectives(self) -> List[str]:
        return [
            "Organize multiple concurrent Claude Code sessions",
            "Develop efficient task-switching habits",
            "Track progress across parallel work streams",
        ]
