"""
Challenge: tmux Test Pattern

Master the tmux test pattern for autonomous test execution.
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
    """tmux Test Pattern - Testing & Verification Challenge 1."""

    def __init__(self):
        super().__init__(
            name="tmux Test Pattern",
            category=Category.TESTING_VERIFICATION,
            difficulty=Difficulty.MEDIUM,
            validation_type=ValidationType.COMMAND,
            description="Use tmux for autonomous test execution and output capture",
            related_tips=[9],
            prerequisites=["cli-fundamentals/1_status_line_setup"],
            time_estimate_minutes=20,
        )

    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate tmux test pattern implementation.

        Expected submission format:
        {
            "commands": ["tmux command 1", "tmux command 2", ...],
            "capture_method": "how output was captured",
            "parse_method": "how pass/fail was determined"
        }
        """
        commands = submission.get("commands", [])
        capture = submission.get("capture_method", "")
        parse = submission.get("parse_method", "")

        feedback_items = []
        score = 0.0
        commands_text = " ".join(commands).lower()

        # Check for tmux session creation
        session_patterns = [
            r"tmux\s+new-session",
            r"tmux\s+new\s+-s",
            r"tmux\s+new\s+-d",
        ]
        has_session = any(re.search(p, commands_text) for p in session_patterns)

        if has_session:
            score += 0.2
            feedback_items.append("Good: tmux session creation found")
        else:
            feedback_items.append("Missing: tmux session creation (new-session)")

        # Check for detached mode
        if "-d" in commands_text:
            score += 0.1
            feedback_items.append("Good: Using detached mode (-d)")
        else:
            feedback_items.append("Tip: Use -d for detached sessions")

        # Check for send-keys
        if "send-keys" in commands_text:
            score += 0.2
            feedback_items.append("Good: Using send-keys to run commands")
        else:
            feedback_items.append("Missing: send-keys for command execution")

        # Check for output capture
        capture_patterns = [
            r"capture-pane",
            r"save-buffer",
            r"pipe-pane",
        ]
        has_capture = any(re.search(p, commands_text) for p in capture_patterns)

        if has_capture:
            score += 0.2
            feedback_items.append("Good: Output capture method found")
        else:
            feedback_items.append("Missing: capture-pane or equivalent")

        # Check capture method description
        if capture and len(capture) > 10:
            capture_lower = capture.lower()
            if "capture-pane" in capture_lower or "buffer" in capture_lower:
                score += 0.1
                feedback_items.append("Good: Capture method explained")
        else:
            feedback_items.append("Tip: Explain how you captured the output")

        # Check parse method
        if parse and len(parse) > 10:
            parse_lower = parse.lower()
            parse_indicators = ["pass", "fail", "exit", "code", "grep", "pattern", "regex"]
            if any(ind in parse_lower for ind in parse_indicators):
                score += 0.2
                feedback_items.append("Good: Parse method for pass/fail detection")
        else:
            feedback_items.append("Missing: Method for determining pass/fail")

        passed = score >= 0.7

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_items),
            details={
                "has_session_create": has_session,
                "has_send_keys": "send-keys" in commands_text,
                "has_capture": has_capture,
            },
        )

    def generate_test_cases(self) -> List[TestCase]:
        return [
            TestCase(
                name="Complete tmux workflow",
                description="Full test pattern implementation",
                input_data={
                    "commands": [
                        "tmux new-session -d -s test-runner",
                        "tmux send-keys -t test-runner 'npm test' Enter",
                        "sleep 30",
                        "tmux capture-pane -t test-runner -p > test_output.txt",
                        "tmux kill-session -t test-runner"
                    ],
                    "capture_method": "Used capture-pane with -p flag to print to stdout, redirected to file",
                    "parse_method": "Grep for 'PASS' or 'FAIL' in output, check exit code patterns"
                },
                expected={"passed": True},
            ),
        ]

    def get_hints(self) -> List[str]:
        return [
            "tmux new-session -d -s name creates a detached session",
            "tmux send-keys -t name 'cmd' Enter sends commands",
            "tmux capture-pane -t name -p captures output",
            "Don't forget to kill sessions when done",
        ]

    def get_learning_objectives(self) -> List[str]:
        return [
            "Understand tmux session management",
            "Master autonomous test execution",
            "Learn output capture and parsing techniques",
        ]
