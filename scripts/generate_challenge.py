#!/usr/bin/env python3
"""
Generate a new challenge skeleton.

Usage:
    python scripts/generate_challenge.py <category> <challenge_name>

Example:
    python scripts/generate_challenge.py cli-fundamentals alias_setup
"""

import os
import sys
from pathlib import Path

CATEGORIES = [
    "cli-fundamentals",
    "context-management",
    "mcp-integrations",
    "testing-verification",
    "workflow-automation",
    "advanced-orchestration",
]

DIFFICULTY_MAP = {
    "cli-fundamentals": "EASY",
    "context-management": "MEDIUM",
    "mcp-integrations": "MEDIUM",
    "testing-verification": "MEDIUM",
    "workflow-automation": "MEDIUM",
    "advanced-orchestration": "HARD",
}

CATEGORY_ENUM = {
    "cli-fundamentals": "CLI_FUNDAMENTALS",
    "context-management": "CONTEXT_MANAGEMENT",
    "mcp-integrations": "MCP_INTEGRATIONS",
    "testing-verification": "TESTING_VERIFICATION",
    "workflow-automation": "WORKFLOW_AUTOMATION",
    "advanced-orchestration": "ADVANCED_ORCHESTRATION",
}

CHALLENGE_MD_TEMPLATE = '''# {title}

## Difficulty: {difficulty}

## Category: {category_display}

## Related Tips:

## Description

[Describe what this challenge teaches]

## Objective

[What the user should accomplish]

## Task

[Specific steps to complete]

## Expected Outcome

[What success looks like]

## Hints

1. [Hint 1]
2. [Hint 2]

## Constraints

- [Any limitations]

## Submission

[What to submit for validation]
'''

CHALLENGE_PY_TEMPLATE = '''"""
Challenge: {title}

[Brief description]
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


class Challenge(ChallengeBase):
    """{title} - {category_display} Challenge."""

    def __init__(self):
        super().__init__(
            name="{title}",
            category=Category.{category_enum},
            difficulty=Difficulty.{difficulty},
            validation_type=ValidationType.COMMAND,  # TODO: Choose appropriate type
            description="",  # TODO: Add description
            related_tips=[],  # TODO: Add related tip numbers
            prerequisites=[],  # TODO: Add prerequisites if any
            time_estimate_minutes=15,
        )

    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate the user's submission.

        Expected submission format:
        {{
            "commands": ["command1", "command2", ...]
        }}
        """
        commands = submission.get("commands", [])

        # TODO: Implement validation logic
        passed = False
        score = 0.0
        feedback = "Validation not implemented"

        return ValidationResult(
            passed=passed,
            score=score,
            feedback=feedback,
        )

    def generate_test_cases(self) -> List[TestCase]:
        """Generate test cases for this challenge."""
        return [
            TestCase(
                name="Basic test",
                description="TODO: Describe test",
                input_data={{"commands": []}},
                expected={{"passed": True}},
            ),
        ]

    def get_hints(self) -> List[str]:
        return [
            # TODO: Add hints
        ]

    def get_learning_objectives(self) -> List[str]:
        return [
            # TODO: Add learning objectives
        ]


if __name__ == "__main__":
    challenge = Challenge()
    print(f"Challenge: {{challenge.name}}")
    print(f"Category: {{challenge.category.value}}")
    print(f"Difficulty: {{challenge.difficulty.value}}")
'''


def get_next_number(category_path: Path) -> int:
    """Get the next available challenge number in a category."""
    if not category_path.exists():
        return 1

    existing = [
        d.name for d in category_path.iterdir()
        if d.is_dir() and d.name[0].isdigit()
    ]

    if not existing:
        return 1

    numbers = []
    for name in existing:
        try:
            num = int(name.split("_")[0])
            numbers.append(num)
        except ValueError:
            continue

    return max(numbers) + 1 if numbers else 1


def to_title(name: str) -> str:
    """Convert snake_case to Title Case."""
    return " ".join(word.capitalize() for word in name.split("_"))


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_challenge.py <category> <challenge_name>")
        print(f"Categories: {', '.join(CATEGORIES)}")
        sys.exit(1)

    category = sys.argv[1].lower()
    name = sys.argv[2].lower().replace("-", "_").replace(" ", "_")

    if category not in CATEGORIES:
        print(f"Invalid category: {category}")
        print(f"Valid categories: {', '.join(CATEGORIES)}")
        sys.exit(1)

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    challenges_dir = project_root / "challenges"
    category_path = challenges_dir / category

    # Get next number
    num = get_next_number(category_path)

    # Create challenge directory
    challenge_dir = category_path / f"{num}_{name}"
    challenge_dir.mkdir(parents=True, exist_ok=True)
    (challenge_dir / "solution").mkdir(exist_ok=True)
    (challenge_dir / "starter").mkdir(exist_ok=True)

    # Get metadata
    title = to_title(name)
    difficulty = DIFFICULTY_MAP[category]
    category_enum = CATEGORY_ENUM[category]
    category_display = category.replace("-", " ").title()

    # Write challenge.md
    md_content = CHALLENGE_MD_TEMPLATE.format(
        title=title,
        difficulty=difficulty.capitalize(),
        category_display=category_display,
    )
    (challenge_dir / "challenge.md").write_text(md_content)

    # Write challenge.py
    py_content = CHALLENGE_PY_TEMPLATE.format(
        title=title,
        difficulty=difficulty,
        category_enum=category_enum,
        category_display=category_display,
    )
    (challenge_dir / "challenge.py").write_text(py_content)

    print(f"Created challenge: {challenge_dir}")
    print(f"  - challenge.md")
    print(f"  - challenge.py")
    print(f"  - solution/")
    print(f"  - starter/")
    print()
    print("Next steps:")
    print("  1. Edit challenge.md with problem description")
    print("  2. Implement validation in challenge.py")
    print("  3. Add solution files")
    print("  4. Test with: python challenge.py")


if __name__ == "__main__":
    main()
'''
