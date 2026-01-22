# Solution: Gemini Fallback for Blocked Sites

## Step-by-Step Solution

### Step 1: Set Up Google Gemini API Access

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key" or "Create API Key"
4. Copy the generated API key

Alternatively, use Google Cloud Console:
```bash
# Install Google Cloud CLI
# Then create a key
gcloud auth application-default login
```

### Step 2: Install Gemini CLI Integration

There are multiple approaches. Here's using a Node.js wrapper:

```bash
# Install Google's Generative AI SDK
npm install -g @google/generative-ai

# Or install locally
npm install @google/generative-ai
```

### Step 3: Create a Custom MCP Server for Gemini

Create a file `gemini-mcp-server.js`:

```javascript
#!/usr/bin/env node

const { GoogleGenerativeAI } = require("@google/generative-ai");
const { Server } = require("@modelcontextprotocol/sdk/server");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio");

const API_KEY = process.env.GEMINI_API_KEY;

if (!API_KEY) {
  console.error("GEMINI_API_KEY environment variable is required");
  process.exit(1);
}

const genAI = new GoogleGenerativeAI(API_KEY);

const server = new Server({
  name: "gemini-research",
  version: "1.0.0"
});

// Define the research tool
server.setRequestHandler("tools/list", async () => {
  return {
    tools: [
      {
        name: "gemini_research",
        description: "Use Gemini to research information from the web, especially for blocked or restricted sites",
        inputSchema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "The research query or question"
            },
            detail_level: {
              type: "string",
              enum: ["brief", "detailed", "comprehensive"],
              description: "How much detail to include in the response"
            }
          },
          required: ["query"]
        }
      },
      {
        name: "gemini_web_search",
        description: "Use Gemini to search and summarize information from specific URLs",
        inputSchema: {
          type: "object",
          properties: {
            url: {
              type: "string",
              description: "The URL to research"
            },
            focus: {
              type: "string",
              description: "What specific information to extract"
            }
          },
          required: ["url"]
        }
      }
    ]
  };
});

// Handle tool calls
server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "gemini_research") {
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const prompt = `Research the following query and provide ${args.detail_level || 'detailed'} information: ${args.query}`;

    try {
      const result = await model.generateContent(prompt);
      const response = await result.response;
      const text = response.text();

      return {
        content: [
          {
            type: "text",
            text: text
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }

  if (name === "gemini_web_search") {
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const prompt = `Access and summarize information from this URL: ${args.url}${args.focus ? `\n\nFocus on: ${args.focus}` : ''}`;

    try {
      const result = await model.generateContent(prompt);
      const response = await result.response;
      const text = response.text();

      return {
        content: [
          {
            type: "text",
            text: text
          }
        ]
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`
          }
        ],
        isError: true
      };
    }
  }

  throw new Error(`Unknown tool: ${name}`);
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Gemini MCP Server running on stdio");
}

main().catch(console.error);
```

### Step 4: Configure Claude to Use Gemini MCP Server

Edit `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
    },
    "gemini-research": {
      "command": "node",
      "args": ["/path/to/gemini-mcp-server.js"],
      "env": {
        "GEMINI_API_KEY": "your-gemini-api-key-here"
      }
    }
  }
}
```

**Better approach using environment variable from system**:

```json
{
  "mcpServers": {
    "gemini-research": {
      "command": "node",
      "args": ["/path/to/gemini-mcp-server.js"],
      "env": {
        "GEMINI_API_KEY": "${GEMINI_API_KEY}"
      }
    }
  }
}
```

Then set the environment variable in your shell:

```bash
# Linux/macOS - Add to ~/.bashrc or ~/.zshrc
export GEMINI_API_KEY="your-gemini-api-key"

# Windows - Add to environment variables or use PowerShell
$env:GEMINI_API_KEY="your-gemini-api-key"
```

### Step 5: Restart Claude and Verify

```bash
# Restart Claude completely
# Then test the integration
```

### Step 6: Test the Gemini Fallback

In Claude, try these commands:

**Basic Research Query**:
```
Can you use Gemini to research the latest papers on transformer models?
```

**Specific URL Research**:
```
There's a research paper at https://arxiv.org/abs/2304.12345 that I can't access.
Can you use Gemini to summarize it for me?
```

**Cross-Reference Research**:
```
Compare information about GPT-4 from multiple sources using both your
knowledge and Gemini's research capabilities.
```

## Simplified Alternative: Using Existing MCP Servers

If building a custom server is too complex, use the Maestro MCP server which includes Gemini support:

```bash
# Install Maestro MCP
npm install -g @modelcontextprotocol/server-maestro
```

Configure in `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "maestro": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-maestro"],
      "env": {
        "GEMINI_API_KEY": "your-gemini-api-key",
        "ANTHROPIC_API_KEY": "your-anthropic-key"
      }
    }
  }
}
```

## Common Mistakes to Avoid

### 1. Exposing API Keys in Configuration

**Wrong**:
```json
{
  "env": {
    "GEMINI_API_KEY": "AIzaSyDcX123456789..."  // Never hardcode keys!
  }
}
```

**Correct**:
```json
{
  "env": {
    "GEMINI_API_KEY": "${GEMINI_API_KEY}"  // Reference system env var
  }
}
```

### 2. Not Handling Rate Limits

Add rate limiting to your MCP server:

```javascript
let lastCallTime = 0;
const MIN_INTERVAL = 1000; // 1 second between calls

async function rateLimitedCall(fn) {
  const now = Date.now();
  const timeSinceLastCall = now - lastCallTime;

  if (timeSinceLastCall < MIN_INTERVAL) {
    await new Promise(resolve =>
      setTimeout(resolve, MIN_INTERVAL - timeSinceLastCall)
    );
  }

  lastCallTime = Date.now();
  return await fn();
}
```

### 3. Not Validating API Responses

Always check for errors:

```javascript
try {
  const result = await model.generateContent(prompt);
  const response = await result.response;

  if (!response || !response.text) {
    throw new Error("Invalid response from Gemini");
  }

  const text = response.text();
  return { content: [{ type: "text", text }] };
} catch (error) {
  console.error("Gemini API error:", error);
  return {
    content: [{ type: "text", text: `Failed to fetch: ${error.message}` }],
    isError: true
  };
}
```

### 4. Forgetting to Install Dependencies

```bash
# Make sure all dependencies are installed
npm install @google/generative-ai
npm install @modelcontextprotocol/sdk
```

### 5. Not Testing Error Cases

Test with invalid API key, rate limits, and network failures to ensure graceful degradation.

## Advanced Usage Patterns

### Pattern 1: Automatic Fallback

Have Claude automatically try Gemini when direct access fails:

```
System: When you encounter access errors or blocked content,
automatically try using the Gemini research tool as a fallback.
```

### Pattern 2: Parallel Research

Research from multiple sources simultaneously:

```
Research quantum computing developments using:
1. Your built-in knowledge
2. Gemini web research
3. Direct web search if available

Then synthesize all sources into a comprehensive summary.
```

### Pattern 3: Specialized Research Queries

Create specialized prompts for Gemini:

```javascript
const specializedPrompts = {
  academic: "Search academic sources and papers about: ",
  news: "Find the latest news and developments about: ",
  technical: "Research technical documentation and specifications for: ",
  regional: "Find region-specific information about: "
};
```

## Troubleshooting

### API Key Issues

```bash
# Test API key directly
curl "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=YOUR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Hello"}]}]}'
```

### Connection Timeouts

Increase timeout in MCP server configuration:

```javascript
const result = await Promise.race([
  model.generateContent(prompt),
  new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Timeout')), 30000)
  )
]);
```

### Rate Limit Errors

Implement exponential backoff:

```javascript
async function withRetry(fn, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (error.message.includes('rate limit') && i < maxRetries - 1) {
        await new Promise(resolve =>
          setTimeout(resolve, Math.pow(2, i) * 1000)
        );
        continue;
      }
      throw error;
    }
  }
}
```

## Verification Checklist

- [ ] Gemini API key obtained and stored securely
- [ ] MCP server created and executable
- [ ] Dependencies installed (`@google/generative-ai`, MCP SDK)
- [ ] Configuration added to `~/.claude/settings.json`
- [ ] Environment variables set correctly
- [ ] Claude restarted and MCP server connected
- [ ] Successfully executed research query via Gemini
- [ ] Error handling works for failed requests
- [ ] Rate limiting implemented
- [ ] API costs monitored

## Next Steps

1. Set up monitoring for API usage and costs
2. Create more specialized research tools
3. Implement caching to reduce API calls
4. Add support for multiple AI models (Gemini, GPT-4, etc.)
5. Build a unified research interface that tries multiple sources
