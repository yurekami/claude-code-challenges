# Claude Code Challenge Format Specification

This document defines the standard format for all Claude Code challenges.

## Directory Structure

```
challenge-name/
├── challenge.md      # Problem description (required)
├── tests.py          # Verification script (required)
├── starter/          # Initial files (optional)
│   └── ...
└── solution/         # Reference solution (hidden)
    └── ...
```

## Challenge.md Format

```markdown
# Challenge: [Name]

**Difficulty:** Easy | Medium | Hard
**Category:** [Category Name]
**Points:** [100 | 150 | 250]
**Time Limit:** [X minutes]

## Description
[2-3 paragraphs explaining the challenge context and goals]

## Objectives
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

## Constraints
- [Constraint 1]
- [Constraint 2]

## Input
[Description of starter files or setup]

## Expected Output
[Clear description of what the solution should produce]

## Examples
[Code examples showing expected behavior]

## Scoring
| Criteria | Points |
|----------|--------|
| [Criterion 1] | XX |
| [Criterion 2] | XX |

## Hints
1. [Hint 1]
2. [Hint 2]

## Verification
Run `python tests.py` to check your solution.
```

## tests.py Format

```python
#!/usr/bin/env python3
"""
[Challenge Name] - Test Suite
[Brief description of what is tested]
"""

import sys

def test_criterion_1():
    """Test description."""
    # Test logic
    return score  # 0 to max points

def test_criterion_2():
    """Test description."""
    # Test logic
    return score

def main():
    print("=" * 50)
    print("[Challenge Name] - Test Results")
    print("=" * 50)

    total_score = 0
    total_score += test_criterion_1()
    total_score += test_criterion_2()

    print()
    print("=" * 50)
    print(f"TOTAL SCORE: {total_score}/100")
    print("=" * 50)

    return 0 if total_score >= 75 else 1

if __name__ == "__main__":
    sys.exit(main())
```

## Categories

| Category | Focus Area |
|----------|------------|
| File Operations | Read, Write, Edit, Glob, Grep |
| Git Mastery | Commits, branches, PRs, gh CLI |
| Context Management | /compact, /clear, tokens, handoffs |
| MCP Integration | Server setup, tools, resources |
| Multi-Agent Workflows | Task tool, parallel agents |
| Advanced Techniques | Playwright, testing, research |

## Difficulty Guidelines

### Easy (100 points, 5-10 min)
- Single skill focus
- Clear, step-by-step instructions
- One main objective
- Minimal prerequisites

### Medium (150 points, 15-20 min)
- Multiple skills combined
- Some decision-making required
- 3-5 objectives
- Requires planning

### Hard (250 points, 45-60 min)
- Complex workflows
- Autonomous decision-making
- Multi-phase execution
- Requires orchestration

## Scoring Guidelines

- **Correctness**: 40% of points
- **Best Practices**: 20% of points
- **Efficiency**: 20% of points
- **Completeness**: 20% of points

## Passing Threshold

- 75% minimum to pass
- 90%+ for "excellent" rating
- 100% for "perfect" rating

## Test Output Format

```
==================================================
[Challenge Name] - Test Results
==================================================

PASS: [Test description]
FAIL: [Test description]
  Expected: [value]
  Got: [value]
PARTIAL: [Test description] (X/Y points)

==================================================
TOTAL SCORE: XX/100
==================================================
[Feedback message based on score]
```
