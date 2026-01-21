"""
Claude Code Challenges - Library module.

This module provides the core infrastructure for challenge validation.
"""

from .challenge_base import (
    ChallengeBase,
    Category,
    Difficulty,
    ValidationType,
    ValidationResult,
    TestCase,
    load_challenge,
    validate_submission,
)

__all__ = [
    "ChallengeBase",
    "Category",
    "Difficulty",
    "ValidationType",
    "ValidationResult",
    "TestCase",
    "load_challenge",
    "validate_submission",
]
