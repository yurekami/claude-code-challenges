"""
Challenge: Status Line Setup

Configure Claude Code's status line to display model, directory, git branch, and tokens.
"""

import sys
from pathlib import Path

# Add lib to path for imports
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


class Challenge(ChallengeBase):
    """Status Line Setup - CLI Fundamentals Challenge 1."""

    def __init__(self):
        super().__init__(
            name="Status Line Setup",
            category=Category.CLI_FUNDAMENTALS,
            difficulty=Difficulty.EASY,
            validation_type=ValidationType.COMMAND,
            description="Configure Claude Code status line with model, directory, git, and tokens",
            related_tips=[0],
            prerequisites=[],
            time_estimate_minutes=10,
        )

    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate the user's status line configuration commands.

        Expected submission format:
        {
            "commands": ["command1", "command2", ...]
        }
        """
        commands = submission.get("commands", [])

        if not commands:
            return ValidationResult(
                passed=False,
                score=0.0,
                feedback="No commands submitted. Please provide the commands you used.",
            )

        # Check for status line related commands
        valid_patterns = [
            r"/config\s+statusline",
            r"/settings?\s+status",
            r"claude\s+config\s+set\s+statusline",
            r"/terminal-setup",
            r"statusline",
        ]

        required_elements = {
            "model": False,
            "directory": False,
            "branch": False,
            "tokens": False,
        }

        feedback_items = []
        commands_text = " ".join(commands).lower()

        # Check for status line command usage
        import re
        has_statusline_cmd = any(
            re.search(pattern, commands_text, re.IGNORECASE)
            for pattern in valid_patterns
        )

        if not has_statusline_cmd:
            feedback_items.append(
                "Did not detect a status line configuration command. "
                "Try using /config or checking Claude Code's status line settings."
            )

        # Check for required elements in configuration
        element_patterns = {
            "model": [r"\{model\}", r"model", r"claude-\d"],
            "directory": [r"\{cwd\}", r"\{dir\}", r"directory", r"cwd", r"pwd"],
            "branch": [r"\{branch\}", r"\{git\}", r"branch", r"git"],
            "tokens": [r"\{tokens?\}", r"token", r"usage"],
        }

        for element, patterns in element_patterns.items():
            for pattern in patterns:
                if re.search(pattern, commands_text, re.IGNORECASE):
                    required_elements[element] = True
                    break

        # Calculate score based on elements found
        found_count = sum(required_elements.values())
        score = found_count / 4

        if has_statusline_cmd:
            score = min(1.0, score + 0.2)  # Bonus for correct command

        # Generate feedback
        missing = [k for k, v in required_elements.items() if not v]
        if missing:
            feedback_items.append(
                f"Configuration may be missing: {', '.join(missing)}. "
                "Make sure your status line format includes placeholders for all elements."
            )

        found = [k for k, v in required_elements.items() if v]
        if found:
            feedback_items.append(f"Good! Detected configuration for: {', '.join(found)}")

        passed = has_statusline_cmd and found_count >= 3

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_items) if feedback_items else "Status line configured!",
            details={
                "has_statusline_command": has_statusline_cmd,
                "elements_configured": required_elements,
            },
            partial_credit=[f"{k}: {'configured' if v else 'missing'}"
                          for k, v in required_elements.items()],
        )

    def generate_test_cases(self) -> List[TestCase]:
        """Generate test cases for validation."""
        return [
            TestCase(
                name="Basic configuration",
                description="Configure status line with all four elements",
                input_data={
                    "commands": [
                        "/config statusline format '{model} | {cwd} | {branch} | {tokens}'"
                    ]
                },
                expected={"passed": True},
                weight=1.0,
            ),
            TestCase(
                name="Alternative commands",
                description="Use alternative method to configure",
                input_data={
                    "commands": [
                        "claude config set statusline.format '{model} {dir} {git} {usage}'"
                    ]
                },
                expected={"passed": True},
                weight=1.0,
            ),
            TestCase(
                name="Missing elements",
                description="Configuration missing some elements",
                input_data={
                    "commands": ["/config statusline format '{model}'"]
                },
                expected={"passed": False},
                weight=1.0,
            ),
        ]

    def get_hints(self) -> List[str]:
        """Return hints for this challenge."""
        return [
            "Claude Code has a /config command for settings",
            "Status line format uses placeholders like {model}",
            "The format string is customizable with separators",
        ]

    def get_learning_objectives(self) -> List[str]:
        """Return learning objectives."""
        return [
            "Understand Claude Code's configuration system",
            "Learn to customize the status line display",
            "Know what information is available in the status line",
        ]


if __name__ == "__main__":
    # Test the challenge
    challenge = Challenge()
    print(f"Challenge: {challenge.name}")
    print(f"Category: {challenge.category.value}")
    print(f"Difficulty: {challenge.difficulty.value}")
    print()

    # Run test cases
    for test in challenge.generate_test_cases():
        result = challenge.validate(test.input_data)
        status = "PASS" if result.passed == test.expected.get("passed") else "FAIL"
        print(f"Test '{test.name}': {status}")
        print(f"  Score: {result.score:.2f}")
        print(f"  Feedback: {result.feedback}")
        print()
