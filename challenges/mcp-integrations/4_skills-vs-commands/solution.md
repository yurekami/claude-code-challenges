# Solution: Understanding Skills vs Slash Commands vs Plugins

## Comprehensive Explanation

### Skills

**Definition**: Skills are reusable, composable workflows that can be triggered explicitly or automatically based on context. They are implemented as tool calls that execute predefined processes.

**Key Characteristics**:
- Invoked using the `Skill` tool
- Can auto-trigger based on user intent
- Support parameters and arguments
- Can chain multiple operations
- Defined in skill directories or plugins

**Invocation Examples**:
```
# Explicit invocation
Run the /commit skill

# With arguments
Run the /review-pr skill for PR #123

# Auto-triggered
"Can you help me commit my changes?" → commit skill auto-triggers
```

**Implementation Location**:
- Built-in skills: Part of Claude Code
- Plugin skills: In `oh-my-claude-*` plugins
- Custom skills: Can be created in skill directories

### Slash Commands

**Definition**: Slash commands are built-in CLI commands that provide core functionality for managing the Claude Code session.

**Key Characteristics**:
- Built into Claude Code (not extensible)
- Start with `/` in the CLI
- Execute immediately without AI interpretation
- Provide system-level functionality
- No auto-triggering

**Common Slash Commands**:
```bash
/help         # Show help information
/clear        # Clear conversation history
/exit         # Exit Claude Code
/settings     # Show or modify settings
/context      # Manage context window
/model        # Switch AI models
```

**Invocation**:
```
# Direct command in CLI
/help

# NOT invoked through Skill tool
# These are system commands, not AI-powered workflows
```

### Plugins

**Definition**: Plugins are MCP-based extensions that provide tools, resources, and prompts to Claude. They extend Claude's capabilities by adding new functions.

**Key Characteristics**:
- Implemented using MCP protocol
- Installed and configured in settings.json
- Provide tools that appear in Claude's tool list
- Can include multiple related tools
- Support resources and prompts

**Implementation**:
- MCP servers configured in `~/.claude/settings.json`
- Can bundle multiple tools together
- Can include skills as part of the plugin

**Invocation**:
- Tools are called automatically by Claude when needed
- Users don't directly "invoke" plugins
- Skills within plugins can be invoked using Skill tool

## Completed Comparison Matrix

| Feature | Skills | Slash Commands | Plugins |
|---------|--------|----------------|---------|
| **Invocation** | `Skill` tool or auto-trigger | `/command` in CLI | Tools called by Claude automatically |
| **Implementation** | Python/TypeScript workflows | Built-in to Claude Code | MCP servers (Node.js, Python, etc.) |
| **Customization** | Can create custom skills | Not customizable | Fully customizable (create your own) |
| **Auto-trigger** | Yes, based on user intent | No | Tools can be used automatically |
| **Installation** | Plugins or built-in | Built-in only | Configure in settings.json |
| **Use Cases** | Workflows, processes, checklists | System operations, session mgmt | External integrations, tool bundles |
| **Scope** | Task-level automation | CLI-level operations | Capability extension |
| **Parameters** | Supports arguments | Limited parameters | Defined by tool schema |
| **Chainable** | Yes, can call other skills | No | Tools can call each other |
| **Context-aware** | Yes, understands user intent | No | Depends on implementation |

## Answers to Key Questions

### 1. How do you invoke a skill in Claude?

**Method 1: Explicit invocation**
```
User: "Run the /commit skill"
Claude: [Uses Skill tool with skill: "commit"]
```

**Method 2: Natural language (auto-trigger)**
```
User: "Can you commit my changes?"
Claude: [Automatically recognizes intent and uses Skill tool]
```

**Method 3: Direct skill reference**
```
User: "Use the tdd-workflow skill to implement this feature"
Claude: [Uses Skill tool with skill: "tdd-workflow"]
```

### 2. What's the difference between a skill and a slash command?

**Skills**:
- AI-powered workflows
- Can auto-trigger based on context
- Extensible and customizable
- Handle complex, multi-step processes
- Example: `/commit` skill analyzes changes and creates commit

**Slash Commands**:
- System-level operations
- Must be explicitly typed
- Not AI-powered
- Handle simple, direct actions
- Example: `/clear` clears conversation history

### 3. Can plugins auto-trigger like skills can?

**No, but with nuance**:
- Plugins provide tools that Claude uses automatically when appropriate
- Skills within plugins CAN auto-trigger
- Plugin tools are used based on task requirements, not explicit triggering

Example:
```
User: "Search the web for Python tutorials"

# If firecrawl plugin is installed:
Claude: [Automatically uses firecrawl search tool]

# If plugin includes a skill:
User: "Run vulnerability research"
Claude: [Uses vuln-toolkit:hunt skill if it auto-triggers]
```

### 4. How are plugins different from MCP servers?

**They're essentially the same thing**:
- "Plugin" is the user-facing term
- "MCP Server" is the technical implementation
- Plugins = MCP servers with specific branding/packaging

**Subtle distinction**:
- MCP Server: Generic term for any MCP protocol server
- Plugin: Branded, packaged MCP servers (e.g., oh-my-claude-sisyphus)

### 5. When would you create a skill vs a plugin?

**Create a Skill when**:
- You want a reusable workflow or process
- You want auto-triggering based on user intent
- You want to combine existing tools in a specific order
- You want to encode best practices or checklists
- You want something lightweight and focused

**Create a Plugin when**:
- You need to integrate with external services/APIs
- You need to add entirely new capabilities
- You want to bundle multiple related tools together
- You need to manage resources (files, data)
- You need persistent state or configuration

**Example Decision Tree**:
```
Need external API access? → Plugin
Need multi-step workflow? → Skill
Need new data source? → Plugin
Need standardized process? → Skill
Need both? → Plugin with skills included
```

### 6. Can skills call other skills?

**Yes**, skills can invoke other skills:

```python
# Within a skill implementation
async def run_skill():
    # Call another skill
    await invoke_skill("tdd-workflow")

    # Continue with current skill
    await run_tests()

    # Call another skill conditionally
    if tests_failed:
        await invoke_skill("debug")
```

Example from built-in skills:
- `maestro-workflow` skill calls individual stage skills
- `update-docs` might call `code-review` skill first

### 7. How do slash commands relate to CLI functionality?

**Slash commands ARE CLI functionality**:
- They provide direct access to system features
- They bypass AI interpretation for speed
- They're the "escape hatch" for system operations

**Relationship**:
```
CLI Session
  ├── Natural Language → AI interprets → Uses tools/skills
  └── /command → Direct execution → System operation
```

## Scenario Solutions

### Scenario A: TDD Workflow Auto-trigger
**Answer: Skill**

**Reason**: You want a workflow that automatically triggers based on user intent.

**Implementation**:
```
Skill name: tdd-workflow
Trigger patterns: "implement feature", "build new", "create component"
Workflow:
  1. Analyze requirements
  2. Write tests first
  3. Implement to pass tests
  4. Refactor
  5. Verify coverage
```

### Scenario B: Internal API Integration
**Answer: Plugin (MCP Server)**

**Reason**: Need to connect to external service with authentication, API calls, etc.

**Implementation**:
```json
{
  "mcpServers": {
    "company-api": {
      "command": "node",
      "args": ["/path/to/company-api-server.js"],
      "env": {
        "API_KEY": "${COMPANY_API_KEY}",
        "API_ENDPOINT": "https://internal.company.com/api"
      }
    }
  }
}
```

### Scenario C: Clear Conversation History
**Answer: Slash Command**

**Reason**: Simple system operation, no AI needed.

**Implementation**:
```
Just type: /clear
```

### Scenario D: Code Review Workflow
**Answer: Skill (possibly within a plugin)**

**Reason**: Reusable workflow with specific steps and checks.

**Implementation**:
```
Skill name: code-review
Steps:
  1. Analyze recent changes
  2. Check security issues
  3. Verify test coverage
  4. Check code style
  5. Generate review report
```

### Scenario E: Third-party Service Integration
**Answer: Plugin**

**Reason**: External service integration with authentication and API calls.

**Implementation**:
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

## Research Task Solutions

### 1. List All Available Skills

```
Ask Claude: "Can you list all available skills?"

Claude will use the Skill tool with available skills showing:
- Built-in skills (commit, review-pr, etc.)
- Plugin skills (oh-my-claude-sisyphus:*, vuln-toolkit:*, etc.)
```

### 2. List All Built-in Slash Commands

```bash
# In Claude CLI
/help

# Common commands:
/help         # Show help
/clear        # Clear history
/exit         # Exit Claude
/settings     # Manage settings
/context      # Context management
/model        # Switch models
```

### 3. List All Installed Plugins

```
Ask Claude: "Can you show me all configured MCP servers?"

# Or check directly:
cat ~/.claude/settings.json | grep -A 10 "mcpServers"
```

### 4. Find Skill Definition

```
Ask Claude: "Show me the definition for the commit skill"

# Or for plugin skills:
"Show me the oh-my-claude-sisyphus:ralph-loop skill details"
```

### 5. Find Plugin Configuration

```bash
# View settings file
cat ~/.claude/settings.json

# Look for mcpServers section
{
  "mcpServers": {
    "filesystem": { ... },
    "github": { ... },
    "oh-my-claude-sisyphus": { ... }
  }
}
```

## Common Confusion Points - Clarified

### Skills vs Plugins

**Confusion**: "Aren't skills just plugins?"

**Clarity**:
- Plugins CAN include skills, but plugins primarily provide tools
- Skills are workflows, plugins are capability extensions
- You use Skill tool to invoke skills
- Plugin tools are used automatically by Claude

### Auto-triggering

**Confusion**: "Why does `/commit` sometimes work without explicitly calling it?"

**Clarity**:
- `/commit` is a skill that can auto-trigger
- When you say "commit my changes", Claude recognizes intent
- It's not a slash command (doesn't need `/` prefix)
- Skills have trigger patterns that activate them

### Invocation Syntax

**Confusion**: "Do I type `/commit` or use the Skill tool?"

**Clarity**:
```
# For users:
"Run /commit"  or  "Commit my changes"

# What Claude does internally:
Uses Skill tool with skill: "commit"

# NOT a slash command:
/commit  ← This won't work (not a CLI command)
```

### Customization

**Confusion**: "Can I create my own slash commands?"

**Clarity**:
- No, slash commands are built-in and not extensible
- Create a skill instead for custom workflows
- Create a plugin for custom tool integrations

### Scope

**Confusion**: "Where do I configure skills vs plugins?"

**Clarity**:
```
Skills:
  - Built-in: Come with Claude Code
  - Plugin skills: Defined in plugin packages
  - Custom: Can be created (advanced)

Plugins:
  - Configured in ~/.claude/settings.json
  - Installed as npm packages or custom servers

Slash Commands:
  - Built-in only, no configuration needed
```

## Practical Examples

### Using Skills

```
# Commit workflow
"I've made changes to my code, please commit them"
→ Claude uses commit skill

# TDD workflow
"Implement a user authentication feature"
→ Claude uses tdd-workflow skill (if configured)

# Code review
"Review my recent changes"
→ Claude uses code-review skill
```

### Using Slash Commands

```
# Clear history
/clear

# Exit Claude
/exit

# Show settings
/settings
```

### Using Plugin Tools

```
# With filesystem plugin
"Read the file /path/to/file.txt"
→ Claude uses mcp__filesystem__read_file

# With GitHub plugin
"Create a new repository called my-project"
→ Claude uses mcp__github__create_repository

# With search plugin
"Search the web for React tutorials"
→ Claude uses mcp__firecrawl__firecrawl_search
```

## Decision Framework

### Should I create a Skill or Plugin?

```
┌─────────────────────────────────────┐
│ Does it need external integration? │
└────────────┬────────────────────────┘
             │
       Yes ──┴── No
       │          │
    Plugin     ┌─┴────────────────────────┐
               │ Is it a multi-step       │
               │ workflow or process?     │
               └──┬────────────────────┬──┘
                  │                    │
               Yes│                    │No
                  │                    │
               Skill              Simple tool
                                (Consider plugin
                                 or built-in tool)
```

### Should I use existing or create new?

```
1. Search existing skills/plugins first
   ↓
2. Found something close?
   ├─ Yes → Use it or extend it
   └─ No → Continue
   ↓
3. Is it generally useful?
   ├─ Yes → Create plugin/skill for reuse
   └─ No → One-off tool call or script
```

## Verification Checklist

- [ ] Understand what skills are and how they're invoked
- [ ] Understand what slash commands are
- [ ] Understand what plugins/MCP servers are
- [ ] Can explain differences between all three
- [ ] Can invoke a skill using natural language
- [ ] Can use a slash command in CLI
- [ ] Can identify plugin tools in tool list
- [ ] Know when to create skill vs plugin
- [ ] Understand auto-triggering behavior
- [ ] Can list available skills, commands, and plugins
- [ ] Understand scope and configuration locations

## Next Steps

1. **Explore Built-in Skills**: Try using different skills
2. **Create Custom Skill**: Build your own workflow skill
3. **Install More Plugins**: Add useful MCP servers
4. **Combine Mechanisms**: Use skills that leverage plugin tools
5. **Build a Plugin**: Create your own MCP server with skills
