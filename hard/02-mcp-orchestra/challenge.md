# Challenge: MCP Orchestra

**Difficulty:** Hard
**Category:** MCP Integration
**Points:** 250
**Time Limit:** 45 minutes

## Description

MCP (Model Context Protocol) servers extend Claude Code's capabilities. This challenge tests your ability to configure, coordinate, and use multiple MCP servers together.

## Scenario

You're building a documentation automation workflow that requires:
1. **GitHub MCP**: Fetch repository information
2. **Filesystem MCP**: Read and write local files
3. **Memory MCP**: Store extracted information
4. **Sequential Thinking MCP**: Plan complex operations

## Objectives

1. Verify MCP server availability using `/mcp`
2. Use multiple MCP servers in a coordinated workflow
3. Handle server failures gracefully
4. Document the orchestration pattern

## The Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  GitHub MCP │────▶│ Memory MCP  │────▶│ Filesystem  │
│ (fetch repo)│     │ (store data)│     │ (write docs)│
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
       └───────────────────┴───────────────────┘
                           │
                    ┌──────▼──────┐
                    │  Sequential │
                    │  Thinking   │
                    │ (coordinate)│
                    └─────────────┘
```

## Tasks

### Task 1: MCP Inventory
List all available MCP servers and their tools.

### Task 2: Repository Analysis
Use GitHub MCP to:
- Fetch repository metadata
- List recent commits
- Get contributor information

### Task 3: Data Storage
Use Memory MCP to:
- Create entities for repo info
- Store relationships between data
- Query stored information

### Task 4: Documentation Generation
Use Filesystem MCP to:
- Create a docs directory
- Write analysis report
- Generate contributor list

### Task 5: Orchestration
Use Sequential Thinking to:
- Plan the workflow steps
- Handle dependencies
- Verify completion

## Expected Output

Create `orchestration_report.md`:

```markdown
# MCP Orchestration Report

## Servers Used
| Server | Tools Used | Operations |
|--------|-----------|------------|
| github | get_file_contents, list_commits | 5 |
| memory | create_entities, search_nodes | 8 |
| filesystem | write_file, create_directory | 3 |
| sequential-thinking | sequentialthinking | 10 |

## Workflow Execution
1. [Step description and result]
2. [Step description and result]
...

## Data Flow
[Diagram or description of how data moved between servers]

## Error Handling
- [Any errors encountered and how they were handled]

## Generated Files
- `docs/repo-analysis.md`
- `docs/contributors.md`
```

## Scoring

| Criteria | Points |
|----------|--------|
| MCP inventory complete | 30 |
| GitHub operations successful | 40 |
| Memory storage working | 40 |
| Files generated correctly | 40 |
| Sequential thinking used | 40 |
| Error handling demonstrated | 30 |
| Report comprehensive | 30 |

## MCP Server Reference

### GitHub MCP
```
Tools: search_repositories, get_file_contents,
       create_issue, list_commits, etc.
```

### Memory MCP
```
Tools: create_entities, create_relations,
       search_nodes, read_graph
```

### Filesystem MCP
```
Tools: read_file, write_file, list_directory,
       create_directory, search_files
```

### Sequential Thinking MCP
```
Tools: sequentialthinking
Parameters: thought, thoughtNumber, totalThoughts,
            nextThoughtNeeded
```

## Hints

1. Use `/mcp` to see available servers
2. Sequential thinking helps plan multi-step operations
3. Memory MCP persists data between operations
4. Handle cases where a server might be unavailable

## Graceful Degradation

If a server is unavailable:
- Document the unavailability
- Provide alternative approach
- Continue with available servers

## Verification

Run `python tests.py` to check your orchestration.
