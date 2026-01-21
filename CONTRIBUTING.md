# Contributing to Claude Code Challenges

Thank you for contributing! We welcome new challenges, improvements, and bug fixes.

## What You Can Contribute

### 1. New Challenges
Add new Claude Code learning challenges to any of the 6 categories.

### 2. Validation Improvements
Improve validation logic for existing challenges to catch more edge cases.

### 3. Documentation
Add hints, learning objectives, or better explanations to challenges.

### 4. Bug Fixes
Fix issues with validation logic or problem descriptions.

## Adding a New Challenge

### Directory Structure

Each challenge should include:

```
challenges/<category>/<number>_<name>/
├── challenge.md      # Problem description (Markdown)
├── challenge.py      # Validation logic
├── solution/         # Reference solution
│   ├── solution.md   # Explanation
│   └── commands.txt  # Commands used (if applicable)
└── starter/          # Starter files (if needed)
    ├── CLAUDE.md     # Pre-configured prompt (if relevant)
    └── scenario/     # Scenario files
```

### Challenge Categories

Choose the appropriate category:
- `cli-fundamentals` - Basic commands, configuration (Easy)
- `context-management` - Token optimization, compaction (Medium)
- `mcp-integrations` - External tools, servers (Medium-Hard)
- `testing-verification` - tmux, TDD, testing (Medium)
- `workflow-automation` - Terminal org, CI/CD (Medium-Hard)
- `advanced-orchestration` - Containers, subagents (Hard)

### Challenge Numbering

Use sequential numbers within each category:
- Check existing challenges for the next available number
- Format: `<number>_<snake_case_name>/`

### Writing challenge.md

```markdown
# Challenge Name

## Difficulty: Easy|Medium|Hard

## Category: Category Name

## Related Tips: 1, 2, 3

## Description
[What this challenge teaches]

## Objective
[What the user should accomplish]

## Task
[Specific steps to complete]

## Expected Outcome
[What success looks like]

## Hints
[Difficulty-appropriate hints]

## Constraints
[Any limitations or requirements]

## Submission
[What to submit for validation]
```

### Writing challenge.py

Inherit from `ChallengeBase`:

```python
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

class Challenge(ChallengeBase):
    def __init__(self):
        super().__init__(
            name="Challenge Name",
            category=Category.CLI_FUNDAMENTALS,  # Choose appropriate
            difficulty=Difficulty.EASY,           # EASY, MEDIUM, or HARD
            validation_type=ValidationType.COMMAND,  # or OUTPUT, ARTIFACT, SCENARIO
            description="Brief description",
            related_tips=[1, 2, 3],
            prerequisites=["category/challenge_name"],  # or []
            time_estimate_minutes=15,
        )

    def validate(self, submission: dict) -> ValidationResult:
        # Implement validation logic
        pass

    def generate_test_cases(self) -> list:
        # Return test cases
        pass

    def get_hints(self) -> list:
        return ["Hint 1", "Hint 2"]

    def get_learning_objectives(self) -> list:
        return ["Objective 1", "Objective 2"]
```

### Validation Types

- **COMMAND**: Validate sequence of commands used
- **OUTPUT**: Validate output/result content
- **ARTIFACT**: Validate created files/configurations
- **SCENARIO**: Validate final state after scenario

### Code Style

#### Python
- **black**: Code formatting (line length: 100)
- **isort**: Import sorting
- **flake8**: Style checking

```bash
pip install black isort flake8
black challenges/ lib/
isort challenges/ lib/
flake8 challenges/ lib/
```

#### Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Testing Your Challenge

1. Run the challenge module directly:
   ```bash
   python challenges/<category>/<number>_<name>/challenge.py
   ```

2. Test all challenges:
   ```bash
   python scripts/validate_all.py
   ```

## Difficulty Guidelines

### Easy (10-15 minutes)
- Single concept
- Clear, direct instructions
- More hints provided
- Basic Claude Code features

### Medium (15-25 minutes)
- 2-3 integrated concepts
- Some problem-solving required
- Moderate hints
- Intermediate features

### Hard (25-40 minutes)
- Complex workflows
- Multiple steps and decisions
- Minimal hints
- Advanced features

## Submission Process

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b challenge/new-challenge-name`
3. **Add your challenge** with all required files
4. **Test validation logic** thoroughly
5. **Run linting**: `pre-commit run --all-files`
6. **Submit a pull request** with:
   - Challenge description
   - Related tip numbers (if applicable)
   - Test results

## Mapping Tips to Challenges

When creating challenges based on [claude-code-tips](https://github.com/ykdojo/claude-code-tips):

1. Identify the core skill being taught
2. Create a practical scenario that exercises that skill
3. Design validation that confirms the skill was applied
4. Add appropriate hints for the difficulty level
5. Note the tip number(s) in `related_tips`

## Getting Help

- Open an issue for questions
- Check existing challenges for examples
- See [CATEGORIES.md](CATEGORIES.md) for tip mappings

## Contributor Terms

By submitting code, documentation, or any other content to this repository
("Contribution"), you confirm that:

1. **Ownership**
   You are the sole author of the Contribution, or have obtained all
   necessary rights and permissions to grant the licenses below.

2. **Dual License to the Project**
   You grant the project maintainers and downstream users **two** non-exclusive,
   worldwide, royalty-free licenses to your Contribution:

   **a.** Under the repository's public license,
   Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
   ("CC BY-NC-ND"), for all public distribution.

   **b.** Under a commercial-friendly license to the project maintainers:
   – **Grant:** Maintainers may reproduce, distribute, adapt, sublicense,
     and create derivative works of your Contribution for any purpose,
     including commercial use.
   – **No further conditions:** Maintainers need not attribute further or
     seek additional permission beyond this agreement.

3. **No Additional Restrictions**
   You may **not** impose any further terms on your Contribution that
   conflict with the licenses granted above.

4. **Pull Request = Acceptance**
   Submitting a Pull Request constitutes acceptance of these terms.
