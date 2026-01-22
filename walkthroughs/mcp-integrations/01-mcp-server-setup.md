# Walkthrough: MCP Server Setup

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** MCP Integrations

---

## Overview

MCP (Model Context Protocol) servers extend Claude's capabilities by connecting external tools and data sources. This challenge teaches you to configure and connect your first MCP server.

## Prerequisites

- [ ] Claude Code CLI installed
- [ ] Node.js installed (v18+)
- [ ] Basic JSON knowledge

---

## Step 1: Understand MCP Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   Claude Code   │────▶│   MCP Server    │
│    (Client)     │◀────│   (Provider)    │
└─────────────────┘     └─────────────────┘
        │                      │
        │   Tools/Resources    │
        └──────────────────────┘
```

**MCP Servers provide:**
- Tools (actions Claude can take)
- Resources (data Claude can access)
- Prompts (reusable templates)

---

## Step 2: Choose Your First MCP Server

### Recommended Starters

| Server | Purpose | Complexity |
|--------|---------|------------|
| `@modelcontextprotocol/server-filesystem` | File operations | Easy |
| `@modelcontextprotocol/server-memory` | Knowledge graph | Easy |
| `@modelcontextprotocol/server-github` | GitHub integration | Medium |

### Browse Available Servers
```bash
# Official MCP servers
https://github.com/modelcontextprotocol/servers

# Community servers
https://github.com/topics/mcp-server
```

---

## Step 3: Install the MCP Server

### Using npx (Recommended)
```bash
# No installation needed - runs directly
npx @modelcontextprotocol/server-filesystem /path/to/allowed/directory
```

### Global Installation
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

---

## Step 4: Configure Claude to Use the Server

### Locate Your Settings File
```bash
# macOS/Linux
~/.claude/settings.json

# Windows
%USERPROFILE%\.claude\settings.json
```

### Add MCP Server Configuration
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/projects"
      ]
    }
  }
}
```

### Multiple Servers Example
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/projects"]
    },
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}
```

---

## Step 5: Verify the Connection

### Restart Claude Code
```bash
# Exit and restart
exit
claude
```

### Check MCP Status
```
/mcp
```

**Expected Output:**
```
Connected MCP Servers:
  ✓ filesystem (3 tools, 0 resources)

Available Tools:
  - mcp__filesystem__read_file
  - mcp__filesystem__write_file
  - mcp__filesystem__list_directory
```

---

## Step 6: Test the Integration

### Try a Tool
```
List the files in my projects directory using the filesystem MCP server
```

**Claude will:**
1. Identify the appropriate MCP tool
2. Call `mcp__filesystem__list_directory`
3. Return the results

### Verify Output
```
Files in /Users/yourname/projects:
  [DIR] project-a
  [DIR] project-b
  [FILE] notes.md
```

---

## Step 7: Troubleshoot Common Issues

### Server Won't Start
```bash
# Test server directly
npx @modelcontextprotocol/server-filesystem /projects

# Check for errors in output
```

### Connection Timeout
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/projects"],
      "timeout": 30000  // Increase timeout
    }
  }
}
```

### Permission Errors
```bash
# Ensure directory is accessible
ls -la /path/to/directory

# Check Node.js has permission
```

---

## Verification Checklist

- [ ] Installed an MCP server
- [ ] Configured settings.json correctly
- [ ] Claude Code recognizes the MCP server
- [ ] Successfully used an MCP tool
- [ ] Can list available MCP tools

---

## Common MCP Servers Reference

| Server | Tools Provided |
|--------|---------------|
| filesystem | read_file, write_file, list_directory |
| github | search_repos, create_issue, list_prs |
| memory | create_entity, add_relation, search |
| postgres | query, list_tables, describe_table |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| "Server not found" | Check command path is correct |
| "Connection refused" | Server might have crashed, restart |
| "Tool not available" | Verify server loaded with `/mcp` |
| Environment vars not set | Use `env` block in config |

---

## Pro Tips

1. **Start Simple:** Get one server working before adding more
2. **Test Standalone:** Run the server directly first to verify it works
3. **Check Logs:** Look for error messages in Claude's output
4. **Version Lock:** Consider pinning MCP server versions in production

---

## Next Challenge

Continue to **[Gemini Fallback](./02-gemini-fallback.md)** to use Gemini for blocked sites!
