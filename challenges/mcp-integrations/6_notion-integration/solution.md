# Solution: Notion Integration for Preserving Markdown Links

## Phase 1: Notion Setup

### Step 1: Create Notion Workspace Structure

1. **Log into Notion** at https://www.notion.so
2. **Create a new page** called "Claude Knowledge Base"
3. **Create three databases**:

**Database 1: Conversations**
```
- Create "Conversations" database
- Add properties:
  - Title (title)
  - Date (date)
  - Category (select): Debugging, Implementation, Research, Q&A
  - Tags (multi-select)
  - Model (text): Sonnet 4.5, Opus 4.5, etc.
  - Project (relation to Projects database)
```

**Database 2: Code Snippets**
```
- Create "Code Snippets" database
- Add properties:
  - Title (title)
  - Language (select): JavaScript, Python, TypeScript, etc.
  - Tags (multi-select)
  - Source URL (url)
  - Created (created time)
  - Last Used (date)
```

**Database 3: Documentation**
```
- Create "Documentation" database
- Add properties:
  - Title (title)
  - Type (select): API, Guide, Tutorial, Reference
  - Status (select): Draft, Review, Published
  - Project (relation)
  - Last Updated (last edited time)
```

### Step 2: Create Notion Integration

1. Go to https://www.notion.so/my-integrations
2. Click "**+ New integration**"
3. Fill in details:
   - Name: "Claude Code Integration"
   - Associated workspace: Select your workspace
   - Logo: Optional
4. Click "**Submit**"
5. Copy the "**Internal Integration Token**" (starts with `secret_`)
6. Under "Capabilities", ensure these are enabled:
   - Read content
   - Update content
   - Insert content

### Step 3: Share Databases with Integration

For each database you created:
1. Open the database
2. Click "**...**" (more options)
3. Select "**Connections**"
4. Click "**Connect to**"
5. Select "**Claude Code Integration**"
6. Confirm the connection

Get database IDs:
1. Open each database
2. Copy the URL
3. Database ID is the string between workspace name and `?v=`
   ```
   https://www.notion.so/workspace/<DATABASE_ID>?v=...
   ```

## Phase 2: MCP Integration Setup

### Step 4: Install Notion MCP Server

The Notion MCP server is available as `@modelcontextprotocol/server-notion`:

```bash
# Option 1: Install globally
npm install -g @modelcontextprotocol/server-notion

# Option 2: Use npx (recommended, no install needed)
# Configuration will use npx to run it
```

### Step 5: Configure Claude Settings

Edit `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    }
  }
}
```

### Step 6: Set Environment Variable

**Linux/macOS** - Add to `~/.bashrc` or `~/.zshrc`:
```bash
export NOTION_API_KEY="secret_your_integration_token_here"
```

**Windows** - PowerShell:
```powershell
[Environment]::SetEnvironmentVariable("NOTION_API_KEY", "secret_your_token_here", "User")
```

Or use Windows Environment Variables UI:
1. Search for "Environment Variables"
2. Click "Edit environment variables for your account"
3. Click "New"
4. Variable name: `NOTION_API_KEY`
5. Variable value: `secret_your_token_here`

### Step 7: Test Basic Integration

Restart Claude Code and test:

```
Can you check if the Notion integration is working?
Try listing available Notion pages.
```

Claude should use the Notion MCP tools to connect and list pages.

## Phase 3: Workflow Implementation

### Step 8: Create Save-to-Notion Workflow

Create a custom skill for saving conversations. Create file `~/.claude/skills/save-to-notion.json`:

```json
{
  "name": "save-to-notion",
  "description": "Save conversation or content to Notion with preserved markdown formatting",
  "version": "1.0.0",
  "triggers": [
    "save this to notion",
    "save conversation to notion",
    "store this in notion",
    "add to notion"
  ],
  "parameters": {
    "type": "object",
    "properties": {
      "content": {
        "type": "string",
        "description": "Content to save"
      },
      "title": {
        "type": "string",
        "description": "Page title"
      },
      "database": {
        "type": "string",
        "enum": ["conversations", "snippets", "docs"],
        "description": "Which database to save to"
      },
      "tags": {
        "type": "array",
        "items": { "type": "string" },
        "description": "Tags for categorization"
      }
    },
    "required": ["content", "title"]
  }
}
```

### Step 9: Implement Search and Retrieval

Test searching Notion:

```
Search my Notion workspace for information about React hooks
```

Claude will use the Notion MCP tools:
- `notion_search` - Search across all pages
- `notion_query_database` - Query specific databases
- `notion_get_page` - Retrieve specific pages

### Step 10: Set Up Link Preservation

Create a test page with markdown links:

```
Create a new Notion page titled "Testing Link Preservation" with this content:

# Link Preservation Test

## External Links
- [Claude Documentation](https://docs.anthropic.com)
- [Notion API](https://developers.notion.com)

## Internal Links
- [[Related Page Name]]

## Code Block
```javascript
const example = "with syntax highlighting";
```

## Lists
1. First item
2. Second item
   - Nested item
   - Another nested item
```

Verify that:
- External links are clickable
- Code blocks have syntax highlighting
- Formatting is preserved
- Lists maintain structure

## Phase 4: Automation and Optimization

### Step 11: Create Advanced Skills

**Skill 1: Quick Conversation Checkpoint**

```
Save this conversation checkpoint to Notion:
- Title: [Current task summary]
- Category: [Auto-detect from context]
- Tags: [Extract from conversation]
```

**Skill 2: Smart Code Snippet Extraction**

```
When I say "save this snippet", automatically:
1. Detect programming language
2. Extract code blocks
3. Create snippet title from context
4. Tag with relevant technologies
5. Save to Code Snippets database
```

**Skill 3: Documentation Updater**

```
When documentation changes:
1. Find existing Notion page
2. Update specific sections
3. Preserve other content
4. Update "Last Modified" timestamp
```

### Step 12: Optimize with Templates

Create Notion templates for common content types:

**Conversation Template**:
```markdown
# [Conversation Topic]

**Date**: [Date]
**Model**: [Claude Version]
**Category**: [Category]

## Context
[What led to this conversation]

## Problem
[What we were trying to solve]

## Solution
[The approach we took]

## Key Insights
- [Insight 1]
- [Insight 2]

## Code Samples
```language
[code]
```

## Related Resources
- [[Link to related page]]
- [External resource](url)

## Follow-up Questions
- [ ] [Question 1]
- [ ] [Question 2]
```

**Code Snippet Template**:
```markdown
# [Snippet Name]

**Language**: [Language]
**Tags**: [Tags]
**Source**: [Link to conversation]

## Purpose
[What this code does]

## Usage
```language
[example usage]
```

## Implementation
```language
[actual code]
```

## Notes
- [Important consideration 1]
- [Important consideration 2]

## Related Snippets
- [[Related snippet 1]]
- [[Related snippet 2]]
```

## Complete Usage Examples

### Example 1: Save Current Conversation

```
User: "We just solved a complex React state management issue.
Can you save this conversation to Notion?"

Claude: I'll save this conversation to your Notion database.

[Uses Notion MCP tools to create a new page in Conversations database]

Result:
✓ Saved to Notion
- Title: "React State Management Solution"
- Database: Conversations
- Category: Implementation
- Tags: React, State Management, Hooks
- Link: [View in Notion](https://notion.so/...)
```

### Example 2: Save Code Snippet

```
User: "Save this React hook as a snippet:

```javascript
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(handler);
  }, [value, delay]);

  return debouncedValue;
}
```"

Claude: I'll save this to your Code Snippets database.

[Creates snippet in Notion with proper formatting]

Result:
✓ Snippet Saved
- Title: "useDebounce Hook"
- Language: JavaScript
- Tags: React, Hooks, Performance
- Link: [View in Notion](https://notion.so/...)
```

### Example 3: Search and Retrieve

```
User: "What did we learn about React performance optimization last week?"

Claude: Let me search your Notion workspace...

[Searches Notion databases]

Found 3 relevant pages:
1. "React Performance Best Practices" (Dec 15, 2024)
   - Use React.memo for expensive components
   - Implement useMemo for heavy calculations
   - [View full page](https://notion.so/...)

2. "Debugging Slow React App" (Dec 18, 2024)
   - Identified unnecessary re-renders
   - Solution: useCallback for event handlers
   - [View full page](https://notion.so/...)

3. "Code Review: Performance Issues" (Dec 20, 2024)
   - Review of optimization techniques
   - Before/after benchmarks
   - [View full page](https://notion.so/...)
```

### Example 4: Update Documentation

```
User: "Add this new API endpoint to our documentation in Notion:

GET /api/users/:id/posts
Returns all posts by a specific user"

Claude: I'll update the API documentation page...

[Searches for API docs page]
[Appends new endpoint to appropriate section]
[Preserves existing formatting and links]

Result:
✓ Documentation Updated
- Page: "API Reference"
- Section: "User Endpoints"
- Added: GET /api/users/:id/posts
- Link: [View in Notion](https://notion.so/...)
```

## Common Mistakes and Solutions

### Mistake 1: Not Granting Database Permissions

**Problem**: "Access denied" errors when trying to create pages.

**Solution**:
```
1. Open the database in Notion
2. Click "..." → "Connections"
3. Add "Claude Code Integration"
4. Verify integration appears in connections list
```

### Mistake 2: Incorrect Database IDs

**Problem**: Can't find or access specific databases.

**Solution**:
```
1. Open database in Notion
2. Copy URL
3. Extract ID from URL format:
   https://notion.so/workspace/DATABASE_ID?v=VIEW_ID
4. Update configuration with correct ID
```

### Mistake 3: Environment Variable Not Loaded

**Problem**: "Authentication failed" even with correct token.

**Solution**:
```bash
# Test if variable is set
echo $NOTION_API_KEY  # Should show your token

# If empty, reload shell configuration
source ~/.bashrc  # or ~/.zshrc

# Or restart terminal completely
```

### Mistake 4: Lost Markdown Formatting

**Problem**: Code blocks and formatting not preserved.

**Solution**:
Use proper markdown syntax when creating pages:

```javascript
// Instead of plain text code
Use proper markdown code blocks with language specification

// For links
Use [text](url) format, not plain URLs

// For headers
Use # Header, not just bold text
```

### Mistake 5: Rate Limiting Issues

**Problem**: "Rate limit exceeded" errors.

**Solution**:
```javascript
// Implement batching for multiple operations
const pages = [page1, page2, page3];

// Instead of: pages.forEach(createPage)
// Use: Create pages with delays

for (const page of pages) {
  await createPage(page);
  await new Promise(resolve => setTimeout(resolve, 333)); // 3 requests/sec
}
```

## Advanced Patterns

### Pattern 1: Bidirectional Sync

Keep certain content synced between Claude conversations and Notion:

```javascript
// When page updated in Notion
notion.onPageUpdate(pageId, async (page) => {
  // Notify Claude of changes
  await claude.notify(`Notion page "${page.title}" was updated`);
});

// When content saved from Claude
claude.onSave(async (content) => {
  // Update corresponding Notion page
  await notion.updatePage(pageId, content);
});
```

### Pattern 2: Smart Tagging

Automatically extract and apply tags:

```javascript
function extractTags(content) {
  const tags = new Set();

  // Extract from code blocks
  const languages = content.match(/```(\w+)/g);
  languages?.forEach(lang => tags.add(lang.slice(3)));

  // Extract from content
  const keywords = ['react', 'node', 'python', 'api', 'database'];
  keywords.forEach(keyword => {
    if (content.toLowerCase().includes(keyword)) {
      tags.add(keyword);
    }
  });

  return Array.from(tags);
}
```

### Pattern 3: Knowledge Graph

Build interconnected pages:

```javascript
// When saving new content
async function saveWithLinks(content, title) {
  // Find related existing pages
  const related = await findRelatedPages(content);

  // Create new page
  const newPage = await notion.createPage({
    title,
    content,
    properties: {
      Related: related.map(p => p.id)  // Link to related pages
    }
  });

  // Update related pages to link back
  for (const page of related) {
    await notion.addLink(page.id, newPage.id);
  }
}
```

### Pattern 4: Version Control

Track changes over time:

```javascript
// Save versions when updating
async function updateWithHistory(pageId, newContent) {
  // Get current version
  const currentPage = await notion.getPage(pageId);

  // Archive current version
  await notion.createPage({
    title: `${currentPage.title} (v${version})`,
    database: 'Archive',
    content: currentPage.content
  });

  // Update main page
  await notion.updatePage(pageId, {
    content: newContent,
    version: version + 1
  });
}
```

## Verification Checklist

- [✓] Notion integration created and token obtained
- [✓] MCP server configured in settings.json
- [✓] Environment variable set and accessible
- [✓] Databases shared with integration
- [✓] Can create pages from Claude
- [✓] Can search Notion from Claude
- [✓] Can update existing pages
- [✓] Markdown formatting preserved (headers, lists, code)
- [✓] Links remain functional (external and internal)
- [✓] Code blocks maintain syntax highlighting
- [✓] Tags and properties set correctly
- [✓] Search returns relevant results
- [✓] Workflow is efficient and user-friendly

## Troubleshooting

### Integration Not Connecting

```bash
# Check if MCP server is installed
npx @modelcontextprotocol/server-notion --version

# Test API connection manually
curl https://api.notion.com/v1/users/me \
  -H "Authorization: Bearer ${NOTION_API_KEY}" \
  -H "Notion-Version: 2022-06-28"

# Check Claude logs for errors
tail -f ~/.claude/logs/mcp-notion.log
```

### Pages Not Appearing

```
1. Verify database is shared with integration
2. Check database ID is correct
3. Ensure integration has "Insert content" permission
4. Try creating page manually in Notion to verify permissions
```

### Formatting Issues

```
# Test with minimal example
Create a Notion page with:
- One header
- One code block
- One link

Verify each element renders correctly before adding complexity
```

## Next Steps

1. **Create Custom Workflows**: Build skills for your specific use cases
2. **Set Up Automation**: Auto-save important conversations
3. **Build Knowledge Graph**: Link related content together
4. **Team Integration**: Share knowledge base with team
5. **Advanced Search**: Implement semantic search across saved content
6. **Analytics**: Track what content is most referenced
7. **Export System**: Build backup/export functionality
