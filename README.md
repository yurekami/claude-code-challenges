# Claude Code Challenges

Interactive coding challenges to master Claude Code - Anthropic's official CLI for Claude.

Based on the comprehensive tips from [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips).

## Overview

Claude Code Challenges is a structured learning platform with hands-on challenges organized into 6 skill categories. Each challenge teaches practical Claude Code techniques through real-world scenarios.

## Categories

| Category | Focus Area | Difficulty Range |
|----------|------------|------------------|
| **CLI Fundamentals** | Basic commands, configuration, navigation | Easy |
| **Context Management** | Token optimization, compaction, handoffs | Medium |
| **MCP Integrations** | External tools, Playwright, custom servers | Medium-Hard |
| **Testing & Verification** | tmux patterns, TDD, automated testing | Medium |
| **Workflow Automation** | Terminal organization, git worktrees, CI/CD | Medium-Hard |
| **Advanced Orchestration** | Containers, subagents, multi-model coordination | Hard |

## Getting Started

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed
- Python 3.10+ for validation scripts
- Basic terminal familiarity

### Running a Challenge

1. Navigate to a challenge directory:
   ```bash
   cd challenges/cli-fundamentals/1_status_line_setup/
   ```

2. Read the challenge description:
   ```bash
   cat challenge.md
   ```

3. Complete the challenge using Claude Code

4. Validate your solution:
   ```bash
   python challenge.py
   ```

## Challenge Structure

Each challenge contains:

```
challenges/<category>/<number>_<name>/
├── challenge.md      # Problem description and requirements
├── challenge.py      # Validation logic
├── solution/         # Reference solution (spoilers!)
└── starter/          # Any starter files needed
```

## Difficulty Levels

- **Easy**: 10-15 minutes, single concept
- **Medium**: 15-25 minutes, integrated concepts
- **Hard**: 25-40 minutes, complex workflows

## Challenges by Category

### CLI Fundamentals (Easy)
1. [Status Line Setup](challenges/cli-fundamentals/1_status_line_setup/) - Configure status display

### Context Management (Medium)
1. [Context Compaction](challenges/context-management/1_context_compaction/) - Manual context optimization

### MCP Integrations (Medium-Hard)
1. [MCP Server Setup](challenges/mcp-integrations/1_mcp_server_setup/) - Configure external tools

### Testing & Verification (Medium)
1. [tmux Test Pattern](challenges/testing-verification/1_tmux_test_pattern/) - Autonomous test execution

### Workflow Automation (Medium-Hard)
1. [Terminal Cascade](challenges/workflow-automation/1_terminal_cascade/) - Multi-session organization

### Advanced Orchestration (Hard)
1. [Container Sandbox](challenges/advanced-orchestration/1_container_sandbox/) - Safe execution environments

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new challenges.

### Quick Start for Contributors

1. Use the challenge generator:
   ```bash
   python scripts/generate_challenge.py <category> <name>
   ```

2. Fill in the challenge template

3. Add validation logic

4. Test thoroughly

5. Submit PR

## Learning Path

Recommended progression:

1. **Week 1**: CLI Fundamentals (all)
2. **Week 2**: Context Management + Testing
3. **Week 3**: MCP Integrations + Workflow Automation
4. **Week 4**: Advanced Orchestration

## Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Code Tips](https://github.com/ykdojo/claude-code-tips)
- [r/ClaudeAI](https://reddit.com/r/ClaudeAI)

## License

CC BY-NC-ND 4.0 - See [LICENSE](LICENSE) for details.

## Acknowledgments

Challenge content inspired by [ykdojo's Claude Code tips](https://github.com/ykdojo/claude-code-tips) - a comprehensive collection of 43+ tips for mastering Claude Code.
