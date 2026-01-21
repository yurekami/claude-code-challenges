"""
Challenge: MCP Server Setup

Configure and use MCP servers to extend Claude Code capabilities.
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
import json


class Challenge(ChallengeBase):
    """MCP Server Setup - MCP Integrations Challenge 1."""

    def __init__(self):
        super().__init__(
            name="MCP Server Setup",
            category=Category.MCP_INTEGRATIONS,
            difficulty=Difficulty.MEDIUM,
            validation_type=ValidationType.ARTIFACT,
            description="Configure MCP servers to extend Claude Code with external tools",
            related_tips=[11, 25],
            prerequisites=["cli-fundamentals/1_status_line_setup"],
            time_estimate_minutes=20,
        )

    def validate(self, submission: Dict[str, Any]) -> ValidationResult:
        """
        Validate MCP server configuration.

        Expected submission format:
        {
            "configuration": "{ json config }",
            "verification_commands": ["cmd1", "cmd2"],
            "test_output": "output from browser test"
        }
        """
        config = submission.get("configuration", "")
        verify_cmds = submission.get("verification_commands", [])
        test_output = submission.get("test_output", "")

        feedback_items = []
        score = 0.0

        # Validate configuration
        try:
            if isinstance(config, str):
                config_data = json.loads(config)
            else:
                config_data = config

            # Check for MCP server configuration
            mcp_servers = config_data.get("mcpServers", config_data.get("mcp", {}))

            if mcp_servers:
                score += 0.3
                feedback_items.append("Good: MCP server configuration found")

                # Check for Playwright specifically
                has_playwright = any(
                    "playwright" in str(v).lower()
                    for v in mcp_servers.values()
                ) or "playwright" in str(mcp_servers).lower()

                if has_playwright:
                    score += 0.2
                    feedback_items.append("Good: Playwright MCP configured")
                else:
                    feedback_items.append("Note: Playwright not detected, but other MCP servers work too")
            else:
                feedback_items.append("Missing: No MCP server configuration detected")

        except json.JSONDecodeError:
            feedback_items.append("Error: Configuration is not valid JSON")
        except Exception as e:
            feedback_items.append(f"Error parsing configuration: {e}")

        # Check verification commands
        verify_text = " ".join(verify_cmds).lower()
        if re.search(r"/mcp|mcp\s+list|mcp\s+status", verify_text):
            score += 0.2
            feedback_items.append("Good: Used MCP verification command")
        else:
            feedback_items.append("Tip: Use /mcp to verify server connections")

        # Check test output
        if test_output:
            browser_indicators = ["navigate", "page", "browser", "url", "screenshot", "html"]
            if any(ind in test_output.lower() for ind in browser_indicators):
                score += 0.3
                feedback_items.append("Good: Browser automation test successful")
            else:
                score += 0.1
                feedback_items.append("Partial: Test output provided but browser action not clear")
        else:
            feedback_items.append("Missing: No test output provided")

        passed = score >= 0.7

        return ValidationResult(
            passed=passed,
            score=score,
            feedback="\n".join(feedback_items),
            details={
                "has_mcp_config": score >= 0.3,
                "has_verification": "/mcp" in verify_text.lower() if verify_cmds else False,
            },
        )

    def generate_test_cases(self) -> List[TestCase]:
        return [
            TestCase(
                name="Playwright setup",
                description="Complete Playwright MCP configuration",
                input_data={
                    "configuration": json.dumps({
                        "mcpServers": {
                            "playwright": {
                                "command": "npx",
                                "args": ["@anthropic/mcp-server-playwright"]
                            }
                        }
                    }),
                    "verification_commands": ["/mcp", "/mcp list"],
                    "test_output": "Navigated to https://example.com, page title: Example Domain"
                },
                expected={"passed": True},
            ),
        ]

    def get_hints(self) -> List[str]:
        return [
            "MCP config goes in ~/.claude/settings.json under mcpServers",
            "Each server needs a command and args",
            "Use /mcp to check connection status",
        ]

    def get_learning_objectives(self) -> List[str]:
        return [
            "Understand MCP server architecture",
            "Configure external tool integrations",
            "Verify and troubleshoot MCP connections",
        ]
