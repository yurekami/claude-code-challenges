# MCP Server Setup

## Difficulty: Medium

## Category: MCP Integrations

## Related Tips: 11, 25

## Description

Model Context Protocol (MCP) servers extend Claude Code's capabilities by providing access to external tools and data sources. Setting up an MCP server allows Claude Code to interact with databases, APIs, browsers, and more.

## Objective

Configure and connect an MCP server to Claude Code:
1. Understand MCP server architecture
2. Configure a server in Claude Code settings
3. Verify the connection works
4. Use the new capabilities in a prompt

## Task

Set up the Playwright MCP server to enable browser automation capabilities:

1. Check what MCP servers are currently configured
2. Add the Playwright MCP server configuration
3. Verify the server is connected
4. Test by having Claude navigate to a webpage

## Expected Outcome

- Playwright MCP server appears in /mcp list
- Claude can execute browser automation commands
- Server connection is stable

## Hints

1. MCP servers are configured in ~/.claude/settings.json or via /mcp command
2. The Playwright MCP server requires Node.js
3. Use /mcp to manage server connections

## Constraints

- Use official or well-known MCP servers
- Ensure proper permissions are granted

## Submission

Submit:
1. The configuration you added
2. The commands used to verify the connection
3. Output from a test browser command
