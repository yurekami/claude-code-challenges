# Challenge: Parallel Search

**Difficulty:** Medium
**Category:** Multi-Agent Workflows
**Points:** 150
**Time Limit:** 15 minutes

## Description

Large codebases require efficient searching. Claude Code's Task tool can spawn multiple search agents to work in parallel. This challenge tests your ability to orchestrate parallel operations.

## Objectives

1. Launch multiple search agents simultaneously
2. Search for different patterns in parallel
3. Aggregate results from all agents
4. Produce a comprehensive search report

## The Task Tool

```
Task tool parameters:
- description: Short description of the task
- prompt: Detailed instructions for the agent
- subagent_type: Type of agent (e.g., "Explore")
- run_in_background: Run asynchronously (optional)
```

## Search Tasks (Run in Parallel)

1. **Security Scan**: Find potential security issues
   - Search for: `eval(`, `innerHTML`, `dangerouslySetInnerHTML`
   - Search for hardcoded secrets/API keys

2. **Performance Scan**: Find performance concerns
   - Search for: `console.log` in production code
   - Search for: missing `useCallback`/`useMemo` in React

3. **Code Quality Scan**: Find quality issues
   - Search for: `TODO`, `FIXME`, `HACK` comments
   - Search for: `any` type usage in TypeScript

## Constraints

- Must use Task tool with `subagent_type: "Explore"`
- Must launch at least 2 agents in parallel (single message)
- Must aggregate results into a single report
- Do NOT run searches sequentially

## Input

The `starter/` directory contains a medium-sized React/TypeScript codebase.

## Expected Output

Create `parallel_search_report.json`:

```json
{
  "security_issues": [
    {"file": "path", "line": 10, "issue": "eval() usage", "severity": "high"}
  ],
  "performance_issues": [
    {"file": "path", "line": 20, "issue": "console.log in production"}
  ],
  "quality_issues": [
    {"file": "path", "line": 30, "issue": "TODO comment"}
  ],
  "summary": {
    "total_issues": 15,
    "high_severity": 3,
    "medium_severity": 7,
    "low_severity": 5
  }
}
```

## Example: Parallel Agent Launch

```
[In a single message, call Task tool multiple times:]

Task 1: Security search agent
Task 2: Performance search agent
Task 3: Quality search agent

[All three run simultaneously]
```

## Scoring

| Criteria | Points |
|----------|--------|
| Used Task tool correctly | 25 |
| Launched agents in parallel | 30 |
| All search categories covered | 25 |
| Results properly aggregated | 35 |
| Summary statistics correct | 35 |

## Hints

1. Use `subagent_type: "Explore"` for search tasks
2. In your prompt to the agent, be specific about what to find
3. Multiple Task tool calls in ONE message = parallel execution
4. Aggregate results after all agents complete

## Benefits of Parallel Search

- **Speed**: 3x faster than sequential
- **Efficiency**: Uses available resources better
- **Organization**: Each agent has focused scope

## Verification

Run `python tests.py` to check your parallel search workflow.
