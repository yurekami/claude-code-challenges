# Challenge: Config Detective

**Difficulty:** Medium
**Category:** MCP Integration
**Points:** 150
**Time Limit:** 15 minutes

## Description

Claude Code's power comes from its configuration and MCP (Model Context Protocol) servers. This challenge tests your ability to diagnose setup issues and understand the configuration system.

## Objectives

1. Inspect current Claude Code configuration using `/config`
2. List configured MCP servers using `/mcp`
3. Diagnose a configuration problem
4. Document the configuration state

## Key Commands

| Command | Purpose |
|---------|---------|
| `/config` | View and modify Claude Code settings |
| `/mcp` | List and manage MCP servers |
| `/help` | Get help on available commands |

## Configuration Locations

```
~/.claude/
├── settings.json      # Global settings
├── CLAUDE.md         # Global instructions
└── projects/
    └── <project>/
        └── CLAUDE.md  # Project-specific instructions

.claude/
├── settings.json      # Project settings
└── CLAUDE.md         # Project instructions (local)
```

## Scenario

A developer reports that:
1. Their MCP server for GitHub isn't working
2. Custom slash commands aren't appearing
3. Auto-formatting on save isn't triggering

Your task: Investigate and document what's configured.

## Expected Output

Create `config_report.md`:

```markdown
# Configuration Report

## Global Settings
- Auto-compact: [enabled/disabled]
- Default model: [model name]
- Theme: [theme]

## MCP Servers
| Server | Status | Tools Available |
|--------|--------|-----------------|
| github | [running/stopped] | [list tools] |
| filesystem | [running/stopped] | [list tools] |

## Project Settings
- Has local CLAUDE.md: [yes/no]
- Custom instructions: [summary]

## Hooks Configured
- PreToolUse: [list]
- PostToolUse: [list]
- Stop: [list]

## Diagnosis
### GitHub MCP Issue
- Likely cause: [your diagnosis]
- Solution: [recommendation]

### Custom Slash Commands
- Likely cause: [your diagnosis]
- Solution: [recommendation]

### Auto-formatting
- Likely cause: [your diagnosis]
- Solution: [recommendation]
```

## Scoring

| Criteria | Points |
|----------|--------|
| Used /config correctly | 20 |
| Used /mcp correctly | 20 |
| Settings documented | 30 |
| MCP servers listed | 30 |
| Reasonable diagnoses | 50 |

## Common Configuration Issues

1. **MCP Server Not Working**
   - API key not set
   - Server not in allowlist
   - Connection timeout

2. **Custom Commands Missing**
   - Not defined in settings.json
   - Syntax error in definition
   - Wrong file location

3. **Hooks Not Triggering**
   - Hook command failing
   - Wrong event type
   - Path issues

## Hints

1. `/config` shows current settings interactively
2. `/mcp` lists all configured servers and their status
3. Check both global (`~/.claude/`) and local (`.claude/`) configs
4. MCP server issues often relate to authentication

## Verification

Run `python tests.py` to check your report.
