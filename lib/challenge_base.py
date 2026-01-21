"""
Challenge Base - Core validation framework for Claude Code challenges.

This module provides the base class and utilities for creating and validating
Claude Code learning challenges.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Union
import difflib
import json
import re


class ValidationType(Enum):
    """Types of validation supported for challenges."""
    COMMAND = "command"      # Validate sequence of commands used
    OUTPUT = "output"        # Validate output/result content
    ARTIFACT = "artifact"    # Validate created files/configurations
    SCENARIO = "scenario"    # Validate final state after scenario


class Difficulty(Enum):
    """Challenge difficulty levels."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Category(Enum):
    """Challenge categories mapping to Claude Code skill areas."""
    CLI_FUNDAMENTALS = "cli-fundamentals"
    CONTEXT_MANAGEMENT = "context-management"
    MCP_INTEGRATIONS = "mcp-integrations"
    TESTING_VERIFICATION = "testing-verification"
    WORKFLOW_AUTOMATION = "workflow-automation"
    ADVANCED_ORCHESTRATION = "advanced-orchestration"


@dataclass
class ValidationResult:
    """Result of validating a challenge submission."""
    passed: bool
    score: float  # 0.0 to 1.0
    feedback: str
    details: Dict[str, Any] = field(default_factory=dict)
    partial_credit: List[str] = field(default_factory=list)


@dataclass
class TestCase:
    """A single test case for a challenge."""
    name: str
    description: str
    input_data: Dict[str, Any]
    expected: Any
    weight: float = 1.0
    hints: List[str] = field(default_factory=list)


class ChallengeBase(ABC):
    """
    Base class for all Claude Code challenges.

    Subclasses must implement:
    - validate(): Main validation logic
    - generate_test_cases(): Generate test scenarios

    Optional overrides:
    - get_hints(): Provide difficulty-appropriate hints
    - get_learning_objectives(): What users will learn
    """

    def __init__(
        self,
        name: str,
        category: Category,
        difficulty: Difficulty,
        validation_type: ValidationType,
        description: str = "",
        related_tips: Optional[List[int]] = None,
        prerequisites: Optional[List[str]] = None,
        time_estimate_minutes: int = 15,
    ):
        self.name = name
        self.category = category
        self.difficulty = difficulty
        self.validation_type = validation_type
        self.description = description
        self.related_tips = related_tips or []
        self.prerequisites = prerequisites or []
        self.time_estimate_minutes = time_estimate_minutes

    @abstractmethod
    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate a user's submission.

        Args:
            submission: Dict containing the user's submission data.
                       Structure depends on validation_type.

        Returns:
            ValidationResult with pass/fail, score, and feedback.
        """
        pass

    @abstractmethod
    def generate_test_cases(self) -> List[TestCase]:
        """
        Generate test cases for this challenge.

        Returns:
            List of TestCase objects defining the validation scenarios.
        """
        pass

    def get_hints(self) -> List[str]:
        """Return hints appropriate for the difficulty level."""
        return []

    def get_learning_objectives(self) -> List[str]:
        """Return what users will learn from this challenge."""
        return []

    def get_starter_files(self) -> Dict[str, str]:
        """Return starter files needed for the challenge."""
        return {}

    # --- Validation Helpers ---

    def validate_commands(
        self,
        submitted: List[str],
        expected: List[str],
        strict_order: bool = True,
        allow_alternatives: Optional[Dict[str, List[str]]] = None,
    ) -> ValidationResult:
        """
        Validate a sequence of commands.

        Args:
            submitted: Commands the user reported using
            expected: Expected correct commands
            strict_order: Whether order matters
            allow_alternatives: Map of command -> acceptable alternatives
        """
        allow_alternatives = allow_alternatives or {}
        matched = 0
        feedback_items = []
        partial_credit = []

        if strict_order:
            for i, (sub, exp) in enumerate(zip(submitted, expected)):
                normalized_sub = self._normalize_command(sub)
                normalized_exp = self._normalize_command(exp)
                alternatives = [self._normalize_command(a)
                               for a in allow_alternatives.get(exp, [])]

                if normalized_sub == normalized_exp or normalized_sub in alternatives:
                    matched += 1
                    partial_credit.append(f"Step {i+1}: Correct")
                else:
                    feedback_items.append(
                        f"Step {i+1}: Expected '{exp}', got '{sub}'"
                    )
        else:
            expected_set = set(self._normalize_command(e) for e in expected)
            submitted_set = set(self._normalize_command(s) for s in submitted)
            matched = len(expected_set & submitted_set)
            missing = expected_set - submitted_set
            if missing:
                feedback_items.append(f"Missing commands: {missing}")

        score = matched / len(expected) if expected else 0.0
        passed = score >= 0.8  # 80% threshold

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_items) if feedback_items else "All commands correct!",
            partial_credit=partial_credit,
            details={"matched": matched, "total": len(expected)}
        )

    def validate_output_contains(
        self,
        output: str,
        required_patterns: List[str],
        forbidden_patterns: Optional[List[str]] = None,
    ) -> ValidationResult:
        """
        Validate that output contains required patterns.

        Args:
            output: The output text to validate
            required_patterns: Regex patterns that must be present
            forbidden_patterns: Regex patterns that must NOT be present
        """
        forbidden_patterns = forbidden_patterns or []
        found = []
        missing = []
        forbidden_found = []

        for pattern in required_patterns:
            if re.search(pattern, output, re.IGNORECASE | re.MULTILINE):
                found.append(pattern)
            else:
                missing.append(pattern)

        for pattern in forbidden_patterns:
            if re.search(pattern, output, re.IGNORECASE | re.MULTILINE):
                forbidden_found.append(pattern)

        score = len(found) / len(required_patterns) if required_patterns else 1.0
        if forbidden_found:
            score *= 0.5  # Penalty for forbidden patterns

        passed = len(missing) == 0 and len(forbidden_found) == 0

        feedback_parts = []
        if missing:
            feedback_parts.append(f"Missing required elements: {missing}")
        if forbidden_found:
            feedback_parts.append(f"Found forbidden elements: {forbidden_found}")
        if passed:
            feedback_parts.append("Output validation passed!")

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_parts),
            details={"found": found, "missing": missing, "forbidden_found": forbidden_found}
        )

    def validate_file_content(
        self,
        content: str,
        expected_content: str,
        similarity_threshold: float = 0.8,
    ) -> ValidationResult:
        """
        Validate file content against expected content.

        Args:
            content: Actual file content
            expected_content: Expected file content
            similarity_threshold: Minimum similarity ratio (0.0-1.0)
        """
        # Normalize whitespace for comparison
        content_lines = content.strip().splitlines()
        expected_lines = expected_content.strip().splitlines()

        # Calculate similarity
        matcher = difflib.SequenceMatcher(None, content_lines, expected_lines)
        similarity = matcher.ratio()

        passed = similarity >= similarity_threshold

        # Generate diff for feedback
        diff = list(difflib.unified_diff(
            expected_lines, content_lines,
            fromfile='expected', tofile='submitted',
            lineterm=''
        ))

        feedback = f"Similarity: {similarity:.1%}"
        if not passed:
            feedback += f"\nRequired: {similarity_threshold:.1%}"
            if diff:
                feedback += f"\nDiff:\n" + "\n".join(diff[:20])  # Limit diff length

        return ValidationResult(
            passed=passed,
            score=similarity,
            feedback=feedback,
            details={"similarity": similarity, "diff_lines": len(diff)}
        )

    def validate_json_structure(
        self,
        data: Union[str, Dict],
        required_keys: List[str],
        optional_keys: Optional[List[str]] = None,
    ) -> ValidationResult:
        """
        Validate JSON structure has required keys.

        Args:
            data: JSON string or dict to validate
            required_keys: Keys that must be present
            optional_keys: Keys that are allowed but not required
        """
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError as e:
                return ValidationResult(
                    passed=False,
                    score=0.0,
                    feedback=f"Invalid JSON: {e}"
                )

        if not isinstance(data, dict):
            return ValidationResult(
                passed=False,
                score=0.0,
                feedback=f"Expected object, got {type(data).__name__}"
            )

        present_keys = set(data.keys())
        required_set = set(required_keys)
        optional_set = set(optional_keys or [])
        allowed_keys = required_set | optional_set

        missing = required_set - present_keys
        extra = present_keys - allowed_keys

        score = len(required_set & present_keys) / len(required_set) if required_set else 1.0
        passed = len(missing) == 0

        feedback_parts = []
        if missing:
            feedback_parts.append(f"Missing required keys: {missing}")
        if extra:
            feedback_parts.append(f"Unexpected keys: {extra}")
        if passed:
            feedback_parts.append("JSON structure valid!")

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_parts),
            details={"missing": list(missing), "extra": list(extra)}
        )

    # --- Private Helpers ---

    def _normalize_command(self, cmd: str) -> str:
        """Normalize a command for comparison."""
        # Remove extra whitespace
        cmd = " ".join(cmd.split())
        # Remove common variations
        cmd = cmd.replace("'", '"')
        return cmd.lower().strip()

    def to_dict(self) -> Dict[str, Any]:
        """Serialize challenge metadata to dict."""
        return {
            "name": self.name,
            "category": self.category.value,
            "difficulty": self.difficulty.value,
            "validation_type": self.validation_type.value,
            "description": self.description,
            "related_tips": self.related_tips,
            "prerequisites": self.prerequisites,
            "time_estimate_minutes": self.time_estimate_minutes,
            "learning_objectives": self.get_learning_objectives(),
            "hints": self.get_hints(),
        }


# --- Utility Functions ---

def load_challenge(path: str) -> ChallengeBase:
    """Load a challenge from its directory path."""
    import importlib.util
    import os

    challenge_file = os.path.join(path, "challenge.py")
    spec = importlib.util.spec_from_file_location("challenge", challenge_file)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load challenge from {challenge_file}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "Challenge"):
        raise AttributeError(f"Challenge class not found in {challenge_file}")

    return module.Challenge()


def validate_submission(challenge_path: str, submission: Dict[str, Any]) -> ValidationResult:
    """Convenience function to validate a submission against a challenge."""
    challenge = load_challenge(challenge_path)
    return challenge.validate(submission)
