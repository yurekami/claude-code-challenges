# Solution: MCP Server Setup

## Step-by-Step Solution

### Step 1: Choose and Install an MCP Server

For this example, we'll use the filesystem MCP server as it's one of the most useful and straightforward to set up.

```bash
# Install the filesystem MCP server globally
npm install -g @modelcontextprotocol/server-filesystem
```

Alternatively, install it locally in a project:

```bash
npm install @modelcontextprotocol/server-filesystem
```

### Step 2: Locate the Server Executable

Find where the server was installed:

```bash
# For global installation
which mcp-server-filesystem

# Or for npm packages
npm list -g @modelcontextprotocol/server-filesystem
```

### Step 3: Configure Claude Settings

Edit `~/.claude/settings.json` (or `%USERPROFILE%\.claude\settings.json` on Windows):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    }
  }
}
```

**Windows Example**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\YourName\\Documents"
      ]
    }
  }
}
```

**macOS/Linux Example**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/Documents"
      ]
    }
  }
}
```

### Step 4: Restart Claude

After saving the configuration:

```bash
# Exit Claude completely and restart it
# Or use the reload command if available
```

### Step 5: Verify the Connection

In Claude, you can now test the integration:

```
Can you list the available MCP resources from the filesystem server?
```

Claude should respond using the `ListMcpResourcesTool` and show available filesystem resources.

### Step 6: Test the Integration

Try a simple operation:

```
Using the filesystem MCP server, can you list the contents of the directory you have access to?
```

Claude should use the filesystem tools to read and display directory contents.

## Example Commands

### Listing Available MCP Resources

```
Please use ListMcpResourcesTool to show all available MCP resources.
```

Expected response will include tools like:
- `read_file`
- `write_file`
- `list_directory`
- `search_files`
- etc.

### Reading a File via MCP

```
Can you read the file "example.txt" using the MCP filesystem server?
```

### Writing a File via MCP

```
Create a new file called "test.txt" with the content "Hello MCP" using the filesystem server.
```

## Common Mistakes to Avoid

### 1. Incorrect Path Separators on Windows

**Wrong**:
```json
"args": ["/path/to/server", "C:/Users/Name/Documents"]
```

**Correct**:
```json
"args": ["/path/to/server", "C:\\Users\\Name\\Documents"]
```

Use double backslashes in JSON on Windows.

### 2. Forgetting to Install the Server

```bash
# This will fail if the server isn't installed
"command": "mcp-server-filesystem"

# Use npx to auto-install if needed
"command": "npx",
"args": ["-y", "@modelcontextprotocol/server-filesystem"]
```

### 3. Not Providing Required Arguments

Some servers require specific arguments like directory paths or API keys. Check the server's documentation.

### 4. Permission Issues

Ensure the directory you're granting access to has appropriate read/write permissions for the user running Claude.

### 5. Not Restarting After Configuration

Configuration changes require a full restart of Claude to take effect.

## Advanced Configuration

### Multiple MCP Servers

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-github-token"
      }
    },
    "database": {
      "command": "node",
      "args": ["/path/to/custom-db-server/index.js"],
      "env": {
        "DATABASE_URL": "postgresql://localhost/mydb"
      }
    }
  }
}
```

### With Environment Variables

```json
{
  "mcpServers": {
    "api-server": {
      "command": "node",
      "args": ["/path/to/server/index.js"],
      "env": {
        "API_KEY": "your-api-key",
        "API_ENDPOINT": "https://api.example.com",
        "LOG_LEVEL": "debug"
      }
    }
  }
}
```

## Troubleshooting

### Server Won't Start

Check logs:
```bash
# Run the server command manually to see errors
npx -y @modelcontextprotocol/server-filesystem /path/to/directory
```

### Tools Not Appearing

1. Verify JSON syntax in settings.json
2. Check that the server command is correct
3. Ensure all dependencies are installed
4. Restart Claude completely

### Connection Timeouts

- Increase timeout values if specified in configuration
- Check network connectivity for remote servers
- Verify firewall settings aren't blocking the connection

## Verification Checklist

- [ ] MCP server package installed successfully
- [ ] Configuration added to `~/.claude/settings.json`
- [ ] JSON syntax is valid (no trailing commas, proper escaping)
- [ ] Claude restarted after configuration
- [ ] `ListMcpResourcesTool` shows the server's resources
- [ ] Successfully executed a command using the MCP server
- [ ] No error messages in Claude's output

## Next Steps

Once you have one MCP server working:
1. Try adding multiple MCP servers
2. Explore more complex MCP servers (database, API integrations)
3. Consider building your own custom MCP server
4. Set up environment variables for sensitive credentials
