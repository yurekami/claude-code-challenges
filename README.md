# Claude Code Challenges

> Master Claude Code CLI through hands-on challenges. Inspired by [LeetGPU](https://leetgpu.com/challenges).

## Challenge Categories

| Category | Skills Tested |
|----------|--------------|
| **File Operations** | Read, Write, Edit, Glob, Grep tools |
| **Git Mastery** | Commits, branches, PRs, gh CLI |
| **Context Management** | /compact, /clear, handoffs, token optimization |
| **MCP Integration** | Server setup, tool usage, resource management |
| **Multi-Agent Workflows** | Task tool, parallel agents, orchestration |
| **Advanced Techniques** | Playwright, browser testing, web research |

## Difficulty Levels

- **Easy** (5 challenges): Single skill focus, clear instructions
- **Medium** (5 challenges): Multi-skill combination, workflow integration
- **Hard** (3 challenges): Complex workflows, autonomous decision-making

## Challenge Structure

Each challenge contains:
```
challenge-name/
├── challenge.md      # Problem description, examples, constraints
├── tests.py          # Verification script and test cases
├── starter/          # Template files to work with
└── solution/         # Reference solution (hidden during challenge)
```

## Scoring System

| Criteria | Points |
|----------|--------|
| Correctness | 40 |
| Efficiency (token usage) | 20 |
| Best Practices | 20 |
| Time to Complete | 20 |

## Quick Start

1. Clone this repository
2. Navigate to a challenge: `cd easy/01-file-explorer`
3. Read `challenge.md` for instructions
4. Use Claude Code to complete the challenge
5. Run `python tests.py` to verify

## Challenges

### Easy
1. [File Explorer](easy/01-file-explorer/) - Navigate and read files
2. [Quick Commit](easy/02-quick-commit/) - Create conventional commits
3. [Token Check](easy/03-token-check/) - Monitor usage with /usage
4. [Simple Edit](easy/04-simple-edit/) - Targeted file modifications
5. [Search Master](easy/05-search-master/) - Pattern searching with Grep

### Medium
1. [PR Creator](medium/01-pr-creator/) - Full PR workflow
2. [Context Handoff](medium/02-context-handoff/) - Session management
3. [Parallel Search](medium/03-parallel-search/) - Multi-agent searching
4. [Config Detective](medium/04-config-detective/) - Setup diagnosis
5. [Refactor Safely](medium/05-refactor-safely/) - Multi-file refactoring

### Hard
1. [Full Feature Flow](hard/01-full-feature-flow/) - End-to-end development
2. [MCP Orchestra](hard/02-mcp-orchestra/) - Multi-server orchestration
3. [Autonomous Debug](hard/03-autonomous-debug/) - Self-directed debugging

## Resources

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [Claude Code Tips by ykdojo](https://github.com/ykdojo/claude-code-tips)
- [LeetGPU Challenges](https://github.com/AlphaGPU/leetgpu-challenges)

## License

CC BY-NC-SA 4.0
