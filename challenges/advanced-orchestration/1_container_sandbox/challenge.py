"""
Challenge: Container Sandbox

Run Claude Code safely in containers for risky operations.
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
    """Container Sandbox - Advanced Orchestration Challenge 1."""

    def __init__(self):
        super().__init__(
            name="Container Sandbox",
            category=Category.ADVANCED_ORCHESTRATION,
            difficulty=Difficulty.HARD,
            validation_type=ValidationType.ARTIFACT,
            description="Run Claude Code in containers for safe execution of risky operations",
            related_tips=[21],
            prerequisites=[
                "testing-verification/1_tmux_test_pattern",
                "workflow-automation/1_terminal_cascade"
            ],
            time_estimate_minutes=30,
        )

    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate container sandbox implementation.

        Expected submission format:
        {
            "dockerfile": "Dockerfile content",
            "docker_run_command": "docker run command used",
            "claude_command": "claude command inside container",
            "review_method": "how results were reviewed before applying"
        }
        """
        dockerfile = submission.get("dockerfile", "")
        docker_run = submission.get("docker_run_command", "")
        claude_cmd = submission.get("claude_command", "")
        review = submission.get("review_method", "")

        feedback_items = []
        score = 0.0

        # Validate Dockerfile
        dockerfile_lower = dockerfile.lower()

        # Check for base image
        if re.search(r"from\s+(node|npm)", dockerfile_lower):
            score += 0.1
            feedback_items.append("Good: Node.js base image for Claude Code")
        elif "from" in dockerfile_lower:
            score += 0.05
            feedback_items.append("Note: Consider Node.js base image for Claude Code")
        else:
            feedback_items.append("Missing: Dockerfile needs FROM statement")

        # Check for Claude Code installation
        if re.search(r"npm\s+(install|i).*claude|@anthropic", dockerfile_lower):
            score += 0.15
            feedback_items.append("Good: Claude Code installation found")
        else:
            feedback_items.append("Missing: Claude Code npm installation")

        # Validate docker run command
        run_lower = docker_run.lower()

        # Check for volume mounts
        if "-v" in run_lower or "--volume" in run_lower or "--mount" in run_lower:
            score += 0.15
            feedback_items.append("Good: Volume mounts configured")

            # Check for read-only credentials
            if ":ro" in run_lower or "readonly" in run_lower:
                score += 0.05
                feedback_items.append("Good: Read-only mount for sensitive data")
        else:
            feedback_items.append("Missing: Volume mounts for work directory")

        # Check for environment variables
        if "-e" in run_lower or "--env" in run_lower:
            score += 0.1
            feedback_items.append("Good: Environment variables passed")
        else:
            feedback_items.append("Tip: Pass credentials via environment variables")

        # Check for cleanup flag
        if "--rm" in run_lower:
            score += 0.05
            feedback_items.append("Good: Auto-cleanup with --rm")

        # Validate Claude command
        claude_lower = claude_cmd.lower()
        if "--dangerously-skip-permissions" in claude_lower:
            score += 0.2
            feedback_items.append("Good: Using --dangerously-skip-permissions in sandbox")
        elif "claude" in claude_lower:
            score += 0.1
            feedback_items.append("Partial: Claude command found, but skip-permissions recommended in sandbox")
        else:
            feedback_items.append("Missing: Claude command for container execution")

        # Validate review method
        review_lower = review.lower()
        review_indicators = ["diff", "git", "review", "check", "compare", "before", "apply"]
        if any(ind in review_lower for ind in review_indicators):
            score += 0.2
            feedback_items.append("Good: Review method before applying changes")
        else:
            feedback_items.append("Missing: Method for reviewing changes before applying")

        passed = score >= 0.6

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_items),
            details={
                "has_dockerfile": bool(dockerfile),
                "has_volume_mounts": "-v" in run_lower,
                "has_skip_permissions": "--dangerously-skip-permissions" in claude_lower,
            },
        )

    def generate_test_cases(self) -> List[TestCase]:
        return [
            TestCase(
                name="Complete sandbox setup",
                description="Full container sandbox implementation",
                input_data={
                    "dockerfile": """
FROM node:20-slim
WORKDIR /workspace
RUN npm install -g @anthropic-ai/claude-code
ENV ANTHROPIC_API_KEY=""
ENTRYPOINT ["claude"]
""",
                    "docker_run_command": """docker run --rm -it \
  -v $(pwd)/work:/workspace \
  -v ~/.anthropic:/root/.anthropic:ro \
  -e ANTHROPIC_API_KEY \
  claude-sandbox --dangerously-skip-permissions""",
                    "claude_command": "claude --dangerously-skip-permissions 'Refactor all files in /workspace'",
                    "review_method": "After container exits, use git diff to review all changes. Only commit after manual review of each file modification."
                },
                expected={"passed": True},
            ),
        ]

    def get_hints(self) -> List[str]:
        return [
            "Use Node.js LTS as base image (Claude Code requires Node)",
            "Mount work directory read-write, credentials read-only",
            "Pass API key via environment variable",
            "Use --rm for automatic container cleanup",
            "Always review changes before applying to main system",
        ]

    def get_learning_objectives(self) -> List[str]:
        return [
            "Understand container isolation for safe execution",
            "Configure volume mounts for data access",
            "Use --dangerously-skip-permissions safely",
            "Implement review-before-apply workflows",
        ]
