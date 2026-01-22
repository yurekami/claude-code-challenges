# Walkthrough: Gemini Fallback

**Difficulty:** Medium | **Time:** 18 minutes | **Category:** MCP Integrations

---

## Overview

Some websites block Claude's web fetching. Gemini MCP provides an alternative - use Google's AI to fetch and summarize web content that Claude can't access directly. This challenge teaches you to set up and use Gemini as a fallback.

## Prerequisites

- [ ] Google AI Studio API key
- [ ] Basic MCP setup knowledge
- [ ] Understanding of web fetching limitations

---

## Step 1: Understand the Problem

### When Claude Can't Fetch
```
Claude: I encountered an error fetching that URL. The site
may be blocking automated access.

Common blocked sites:
- Twitter/X
- LinkedIn
- Some news sites
- Sites with aggressive bot protection
```

### The Solution
```
User Request → Claude WebFetch fails → Gemini MCP → Success
```

---

## Step 2: Get Gemini API Access

### Create API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with Google account
3. Click "Get API Key"
4. Create new API key
5. Copy and save securely

---

## Step 3: Install Gemini MCP Server

### Using npx
```bash
npx @anthropic/gemini-mcp-server
```

### Or Global Install
```bash
npm install -g @anthropic/gemini-mcp-server
```

---

## Step 4: Configure Claude Settings

### Add to settings.json
```json
{
  "mcpServers": {
    "gemini": {
      "command": "npx",
      "args": ["@anthropic/gemini-mcp-server"],
      "env": {
        "GEMINI_API_KEY": "your-gemini-api-key-here"
      }
    }
  }
}
```

### Secure API Key (Recommended)
```json
{
  "mcpServers": {
    "gemini": {
      "command": "npx",
      "args": ["@anthropic/gemini-mcp-server"],
      "env": {
        "GEMINI_API_KEY": "${GEMINI_API_KEY}"
      }
    }
  }
}
```

Then set environment variable:
```bash
export GEMINI_API_KEY="your-key-here"
```

---

## Step 5: Verify Gemini Connection

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
  ✓ gemini (2 tools)
    - gemini_web_fetch
    - gemini_web_search
```

---

## Step 6: Use Gemini Fallback

### Automatic Fallback Pattern
```
Fetch the content from https://twitter.com/anthropikiAI

If the primary fetch fails, use the Gemini MCP to access it.
```

### Direct Gemini Request
```
Use the Gemini MCP server to fetch and summarize the content at:
https://example-blocked-site.com/article
```

### Web Search via Gemini
```
Use Gemini to search the web for "Claude Code latest features 2024"
and summarize the results.
```

---

## Step 7: Configure Fallback Workflow

### Create a Smart Fetch Pattern

Tell Claude your preference:
```
When fetching web content:
1. First, try the standard WebFetch tool
2. If that fails with a blocking error, automatically use Gemini MCP
3. Summarize the key points from whatever source succeeded
```

### Add to CLAUDE.md
```markdown
## Web Fetching
- Primary: Use WebFetch
- Fallback: Use Gemini MCP for blocked sites
- Always summarize key points
```

---

## Verification Checklist

- [ ] Obtained Gemini API key
- [ ] Configured Gemini MCP server
- [ ] Verified connection with `/mcp`
- [ ] Successfully fetched content via Gemini
- [ ] Tested with a previously blocked site

---

## When to Use Each

| Scenario | Tool |
|----------|------|
| Normal websites | WebFetch (default) |
| Blocked/protected sites | Gemini MCP |
| Web search needed | Gemini MCP or WebSearch |
| Speed critical | WebFetch (faster) |
| Complex sites | Gemini (better rendering) |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| "Invalid API key" | Verify key in Google AI Studio |
| "Quota exceeded" | Check Gemini usage limits |
| Gemini not appearing | Restart Claude after config change |
| Still can't access site | Some sites block all AI access |

---

## Pro Tips

1. **Key Security:** Never commit API keys, use environment variables
2. **Rate Limits:** Gemini has usage limits, don't overuse
3. **Summarize:** Ask Gemini to summarize, not just fetch raw content
4. **Combine:** Use Gemini for research, Claude for implementation

---

## Cost Considerations

```
Gemini API Pricing (approximate):
- Free tier: Limited requests/month
- Paid tier: Pay per token

Optimize by:
- Using only when WebFetch fails
- Asking for summaries instead of full content
- Caching results when possible
```

---

## Next Challenge

Continue to **[Custom CLAUDE.md](./03-custom-claude-md.md)** to craft your default prompt!
