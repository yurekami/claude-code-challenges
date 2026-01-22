# Solution: Slash Commands Mastery

## Command Reference

### /usage - Token Usage and Costs

```
/usage
```

**What it shows:**
- Total tokens used in current session
- Percentage of context window consumed
- Estimated API cost
- Input vs output token breakdown

**When to use:**
- Before starting large tasks (check available budget)
- When approaching context limits
- For cost tracking and optimization
- After completing a task (track efficiency)

**Example output:**
```
Token Usage:
  Input:  12,543 tokens
  Output: 8,234 tokens
  Total:  20,777 tokens (10.4% of 200K limit)

Estimated Cost: $0.62
```

### /stats - Detailed Session Statistics

```
/stats
```

**What it shows:**
- Total messages exchanged
- Files read/written
- Tools used
- Commands executed
- Success/failure rates
- Session duration

**When to use:**
- Debugging slow sessions
- Understanding tool usage patterns
- Performance analysis
- Learning your workflow patterns

**Example output:**
```
Session Statistics:
  Duration: 45 minutes
  Messages: 23

Tools Used:
  Read: 15 files
  Write: 8 files
  Bash: 12 commands
  Edit: 5 operations

Success Rate: 94%
```

### /chrome - Browser Integration

```
/chrome
```

**What it enables:**
- Scrape web content
- Take screenshots of websites
- Extract data from web pages
- Test web applications
- Capture rendered HTML/CSS

**When to use:**
- Researching documentation
- Testing web applications
- Extracting data from websites
- Visual verification of UI changes
- Debugging rendering issues

**Example usage:**
```
/chrome

# Then ask Claude:
"Take a screenshot of https://example.com"
"Scrape the pricing information from https://product.com/pricing"
"What does the homepage of my-site.com look like?"
```

### /mcp - Model Context Protocol Servers

```
/mcp
```

**What it shows:**
- Connected MCP servers
- Available tools from each server
- Connection status
- Server capabilities

**When to use:**
- Connecting to databases
- Integrating external APIs
- Adding custom tools
- Extending Claude Code functionality

**Example output:**
```
Connected MCP Servers:

  ✓ postgres-db
    - query: Execute SQL queries
    - schema: View database schema

  ✓ github-integration
    - list-prs: List pull requests
    - create-issue: Create GitHub issues

  ✗ redis-cache (disconnected)
```

### /clear - Clear Conversation History

```
/clear
```

**What it does:**
- Removes conversation messages
- Keeps file context
- Maintains session state
- Preserves tool connections
- Frees up token space

**When to use:**
- Context getting cluttered with debugging
- Too many failed attempts
- Switching focus within same project
- Approaching token limits but not done

**When NOT to use:**
- When you need conversation history
- For complete restart (use `/reset` instead)
- When file context is the problem

### /files - Show Context Files

```
/files
```

**What it shows:**
- All files currently loaded in context
- File paths and sizes
- When files were added
- Token cost of each file

**When to use:**
- Understanding what's in context
- Before using `/clear` (verify what stays)
- Debugging unexpected behavior
- Optimizing context usage

### /model - Switch AI Models

```
/model
```

**What it enables:**
- Switch between Haiku, Sonnet, and Opus
- See current model
- Compare model capabilities
- Optimize cost vs performance

**When to use:**
- Need deeper reasoning → switch to Opus
- Simple edits → switch to Haiku
- Back to balanced work → switch to Sonnet

### /reset - Hard Reset

```
/reset
```

**What it does:**
- Clears ALL context
- Removes all files
- Resets conversation
- Disconnects tools
- Fresh start

**When to use:**
- Complete context corruption
- Starting entirely new task
- Maximum token savings needed
- Testing from clean slate

## Step-by-Step Solutions

### Task 1: Check Token Usage

```bash
# In Claude Code session
/usage

# Analyze the output:
# - Are you below 60%? Safe for any task
# - Between 60-80%? Plan to finish soon
# - Above 80%? Consider /clear or new session
```

### Task 2: View Session Statistics

```bash
/stats

# Review metrics:
# - How many files have been read?
# - Which tools are used most?
# - What's the success rate?
# - How long has this session run?

# Use insights to optimize workflow
```

### Task 3: List Files in Context

```bash
/files

# Review output:
# - Are there files you no longer need?
# - Are large files consuming tokens?
# - Is the context focused on current task?

# If context is bloated, use /clear
```

### Task 4: Clear Context Strategically

```bash
# Before clearing, check what you have
/files

# Clear conversation but keep files
/clear

# Verify files remain
/files

# Continue working with clean message history
# but preserved file context
```

### Task 5: Connect MCP Server

```bash
# Check available servers
/mcp

# If servers are configured in ~/.claude/settings.json
# they'll appear here with their tools

# Example: Using a database MCP server
# "Show me the schema for the users table"
# Claude will use the MCP server's tools
```

### Task 6: Chrome Integration

```bash
# Enable Chrome integration
/chrome

# Take a screenshot
"Take a screenshot of https://github.com/trending"

# Scrape content
"What are the top 5 trending repos on GitHub today?"

# Test your own site
"Screenshot localhost:3000 and check if the navbar looks correct"
```

### Task 7: Model Switching

```bash
# Check current model (in status line or)
/model

# Switch to Haiku for quick edit
/model
# Select: Haiku 4.5

# Switch to Opus for complex reasoning
/model
# Select: Opus 4.5

# Switch back to Sonnet for balanced work
/model
# Select: Sonnet 4.5
```

## Complete Workflow Example

```bash
# 1. Start session
cd ~/projects/my-app
claude

# 2. Check initial state
/usage
/files

# Result: 0 tokens, no files

# 3. Start working
"Help me refactor the authentication system"

# Claude reads files, makes suggestions

# 4. Check token usage periodically
/usage
# Result: 25,000 tokens (12.5%)

# 5. Continue working, context gets messy
# Multiple debugging attempts, lots of back-and-forth

# 6. Check usage again
/usage
# Result: 85,000 tokens (42.5%)

# 7. Context is cluttered but files are good
/files
# Shows: auth.ts, users.ts, middleware.ts (still needed)

# 8. Clear conversation clutter
/clear

# 9. Verify files preserved
/files
# Still shows: auth.ts, users.ts, middleware.ts

# 10. Continue with clean context
"Now let's add rate limiting to the auth endpoints"

# 11. Final check
/stats
# Review session metrics

/usage
# Verify token budget looks good
```

## Common Mistakes to Avoid

### Mistake 1: Using /reset Instead of /clear
**Problem**: Lost all file context and had to reload everything
**Solution**: Use `/clear` to keep files, `/reset` only for complete restart

### Mistake 2: Not Checking /usage Before Big Tasks
**Problem**: Started large refactor at 75% token usage, ran out of context
**Solution**: Always `/usage` before starting multi-step operations

### Mistake 3: Ignoring /stats Insights
**Problem**: Repeatedly using inefficient workflows
**Solution**: Review `/stats` to identify optimization opportunities

### Mistake 4: Not Using /files to Audit Context
**Problem**: Bloated context with unnecessary files
**Solution**: Regularly `/files` and clear context when needed

## Advanced Tips

### Tip 1: Pre-Task Checklist
```bash
/usage   # Check token budget
/files   # Verify context is clean
/stats   # Review session state
# Now start your task
```

### Tip 2: Mid-Task Maintenance
```bash
# Every 20-30 minutes of work:
/usage   # Track consumption
/stats   # Check success rate

# If approaching 60% tokens or lots of clutter:
/clear   # Clean up while preserving files
```

### Tip 3: Post-Task Cleanup
```bash
/stats   # Review what was done
/usage   # Final cost check
# Document lessons learned
# Start fresh for next task if needed
```

### Tip 4: MCP Server Discovery
```bash
# Check configured servers
/mcp

# Test server capabilities
"What can the [server-name] server do?"

# Use server tools
"Use [server-name] to [specific action]"
```

### Tip 5: Chrome Automation Patterns
```bash
/chrome

# Research pattern:
"Scrape the React docs for useState hook examples"

# Testing pattern:
"Screenshot localhost:3000/login and verify the form layout"

# Monitoring pattern:
"Check if my deployed site at example.com is showing the new header"
```

## Verification Checklist

You've mastered slash commands when you can:

- [ ] Check token usage without thinking (`/usage`)
- [ ] Clear context strategically (`/clear` vs `/reset`)
- [ ] Monitor session health (`/stats`)
- [ ] Audit file context (`/files`)
- [ ] Switch models for different tasks (`/model`)
- [ ] Integrate Chrome when needed (`/chrome`)
- [ ] Connect to MCP servers (`/mcp`)
- [ ] Know which command to use in any situation

## Best Practices

1. **Start Every Session**: `/usage` and `/files` to baseline
2. **Regular Monitoring**: `/usage` every 15-20 minutes on long tasks
3. **Strategic Clearing**: `/clear` when messages are cluttered, files are good
4. **Complete Restart**: `/reset` only when changing tasks entirely
5. **Stats Review**: `/stats` at end of session to learn patterns
6. **Context Audit**: `/files` before and after major operations
7. **Tool Integration**: `/mcp` and `/chrome` to extend capabilities

## Quick Reference Card

```
Command     Purpose                          When to Use
-------     -------                          -----------
/usage      Token usage & costs              Before/during/after tasks
/stats      Session statistics               Performance analysis
/files      List context files               Context auditing
/clear      Clear messages, keep files       Declutter context
/reset      Full reset                       Complete restart
/model      Switch AI models                 Optimize for task
/chrome     Browser integration              Web scraping/testing
/mcp        MCP server management            External tool integration
/help       List all commands                Discovery
```
