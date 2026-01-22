# MCP Server Setup

**Related Tip**: Tip 11 - Connect first MCP server

## Description

MCP (Model Context Protocol) servers extend Claude's capabilities by connecting external tools and data sources. Setting up your first MCP server opens the door to powerful integrations with databases, APIs, and other services.

## Objective

Successfully configure and connect your first MCP server to Claude, verify the connection, and use the exposed tools.

## Prerequisites

- Claude Code CLI installed
- Node.js installed (for most MCP servers)
- Basic understanding of JSON configuration

## Steps to Complete

1. **Choose an MCP Server**
   - Browse the MCP server directory at https://github.com/modelcontextprotocol/servers
   - Start with something simple like `@modelcontextprotocol/server-filesystem`

2. **Install the MCP Server**
   - Install the server package globally or locally
   - Note the command needed to start the server

3. **Configure Claude to Use the Server**
   - Edit your Claude configuration file (`~/.claude/settings.json`)
   - Add the MCP server configuration in the `mcpServers` section
   - Include the command and any required arguments

4. **Verify the Connection**
   - Restart Claude or reload the configuration
   - Check that the MCP server tools are available
   - Use `ListMcpResourcesTool` to see available resources

5. **Test the Integration**
   - Try using one of the tools provided by the MCP server
   - Verify that it works as expected

## Success Criteria

- [ ] MCP server is properly configured in settings
- [ ] Claude can connect to the MCP server without errors
- [ ] MCP server tools appear in Claude's available tools
- [ ] Successfully execute at least one operation using the MCP server
- [ ] Can list resources from the MCP server using `ListMcpResourcesTool`

## Example Configuration Structure

```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["/path/to/server/index.js"],
      "env": {
        "OPTIONAL_ENV_VAR": "value"
      }
    }
  }
}
```

## Common Issues

- Server fails to start: Check that all dependencies are installed
- Connection timeout: Verify the command and arguments are correct
- Tools not appearing: Restart Claude after configuration changes
- Permission errors: Ensure the server has necessary file/network permissions
