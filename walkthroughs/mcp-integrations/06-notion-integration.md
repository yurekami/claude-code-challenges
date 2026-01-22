# Walkthrough: Notion Integration

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** MCP Integrations

---

## Overview

Copying from Notion loses hyperlinks and formatting. This challenge teaches you to integrate Notion with Claude to preserve links, access databases, and work seamlessly with your Notion workspace.

## Prerequisites

- [ ] Notion account with content
- [ ] Notion API key (integration token)
- [ ] Basic MCP setup knowledge

---

## Step 1: Understand the Problem

### The Copy-Paste Issue
```
From Notion:
"Check out the [Project Plan](https://notion.so/...) for details"

After pasting to Claude:
"Check out the Project Plan for details"
← Link lost!
```

### The Solution
Use Notion MCP to access content with links preserved.

---

## Step 2: Create Notion Integration

### In Notion
1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click "New integration"
3. Name: "Claude Code Integration"
4. Select workspace
5. Copy the "Internal Integration Token"

### Grant Access
1. Open the Notion page you want Claude to access
2. Click "..." menu → "Add connections"
3. Select your "Claude Code Integration"

---

## Step 3: Install Notion MCP Server

```bash
# Using npx
npx @notionhq/mcp-server

# Or install globally
npm install -g @notionhq/mcp-server
```

---

## Step 4: Configure Claude Settings

### Add to settings.json
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@notionhq/mcp-server"],
      "env": {
        "NOTION_API_KEY": "secret_your_notion_api_key"
      }
    }
  }
}
```

### Secure Configuration
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@notionhq/mcp-server"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    }
  }
}
```

Set environment variable:
```bash
export NOTION_API_KEY="secret_your_notion_api_key"
```

---

## Step 5: Verify Connection

### Restart Claude
```bash
exit
claude
```

### Check MCP Status
```
/mcp
```

**Expected:**
```
Connected MCP Servers:
  ✓ notion (3 tools)
    - notion_search
    - notion_read_page
    - notion_query_database
```

---

## Step 6: Use Notion Integration

### Search Notion
```
Search my Notion workspace for "project roadmap"
```

### Read a Page (with links preserved!)
```
Read the Notion page at: https://notion.so/myworkspace/Project-Plan-abc123
```

**Result:**
```markdown
# Project Plan

## Overview
Check out the [Technical Spec](https://notion.so/...) for details.
← Links preserved!

## Milestones
- [Milestone 1](https://notion.so/...)
- [Milestone 2](https://notion.so/...)
```

### Query Database
```
Query my Notion Tasks database and show me all items with status "In Progress"
```

---

## Step 7: Common Workflows

### Import Requirements from Notion
```
Read the product requirements from our Notion PRD page and
create a technical implementation plan
```

### Sync Meeting Notes
```
Search Notion for today's meeting notes and summarize the action items
```

### Reference Documentation
```
Look up the API documentation in our Notion workspace and
help me implement the authentication endpoint
```

---

## Verification Checklist

- [ ] Created Notion integration
- [ ] Granted access to relevant pages
- [ ] Configured Notion MCP server
- [ ] Successfully searched Notion from Claude
- [ ] Read a page with links preserved
- [ ] Queried a Notion database

---

## Common Operations

| Task | Command |
|------|---------|
| Search pages | "Search Notion for [query]" |
| Read specific page | "Read Notion page [url]" |
| Query database | "Query [database] where [filter]" |
| List databases | "List my Notion databases" |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| "Page not found" | Ensure integration has access to page |
| "Invalid token" | Check API key is correct |
| Links still lost | Use MCP read, not copy-paste |
| Database query fails | Check integration has database access |

---

## Pro Tips

1. **Share Pages:** Must explicitly share pages with your integration
2. **Database Access:** Grant access at database level, not just page
3. **Rate Limits:** Notion API has limits, don't query too frequently
4. **Workspace Scope:** One integration per workspace needed

---

## Notion + Claude Workflow

```
Best Practice Workflow:

1. Store documentation in Notion
2. Use MCP to read when needed
3. Claude works with full context (links included)
4. Output can be written back to Notion
```

---

## Congratulations!

You've completed the **MCP Integrations** category! You now know:

- MCP server setup
- Gemini fallback for blocked sites
- Custom CLAUDE.md creation
- Skills vs commands
- Skill creation
- Notion integration

**Next:** Move on to **[Testing & Verification](../testing-verification/01-tmux-test-pattern.md)** to ensure quality!
