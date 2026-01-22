# Understanding Skills vs Slash Commands vs Plugins

**Related Tip**: Tip 25 - Understand Skills vs Slash Commands vs Plugins

## Description

Claude Code has three different extension mechanisms: Skills, Slash Commands, and Plugins. Understanding the differences between these systems is crucial for choosing the right approach when extending Claude's capabilities. This challenge will help you understand when to use each mechanism and how they differ in implementation and use cases.

## Objective

Learn to distinguish between Skills, Slash Commands, and Plugins, understand their respective strengths and use cases, and know how to invoke and manage each type.

## Prerequisites

- Claude Code CLI installed and configured
- Basic understanding of Claude's tool system
- Familiarity with command-line operations
- Completed previous MCP challenges (optional but helpful)

## The Three Extension Mechanisms

### 1. Skills
Reusable workflows that can be invoked by name or triggered automatically based on context.

### 2. Slash Commands
Built-in CLI commands that provide specific functionality (like `/help`, `/clear`).

### 3. Plugins
MCP-based extensions that provide tools, resources, and prompts to Claude.

## Steps to Complete

1. **Understand Skills**
   - What are skills and how do they work?
   - How to invoke skills (using Skill tool)
   - When skills are auto-triggered
   - How to list available skills

2. **Understand Slash Commands**
   - What are slash commands?
   - How do they differ from skills?
   - Common built-in slash commands
   - When to use slash commands vs skills

3. **Understand Plugins**
   - What are MCP plugins?
   - How plugins extend Claude's capabilities
   - How to install and configure plugins
   - Difference between plugins and skills

4. **Compare and Contrast**
   - Create a comparison matrix
   - Identify use cases for each mechanism
   - Understand limitations of each approach

5. **Test Each Mechanism**
   - Invoke a skill
   - Use a slash command
   - Interact with a plugin tool

6. **Create a Decision Framework**
   - When to build a skill vs plugin
   - When to use existing vs create new
   - How to combine multiple mechanisms

## Success Criteria

- [ ] Can explain the difference between skills, slash commands, and plugins
- [ ] Can invoke skills using the Skill tool
- [ ] Understand built-in slash commands and their purposes
- [ ] Can identify whether to use a skill or plugin for a given task
- [ ] Can list available skills, commands, and plugins
- [ ] Understand auto-triggering behavior for skills
- [ ] Know how to install and configure each type

## Comparison Matrix to Complete

| Feature | Skills | Slash Commands | Plugins |
|---------|--------|----------------|---------|
| **Invocation** | ? | ? | ? |
| **Implementation** | ? | ? | ? |
| **Customization** | ? | ? | ? |
| **Auto-trigger** | ? | ? | ? |
| **Installation** | ? | ? | ? |
| **Use Cases** | ? | ? | ? |

## Key Questions to Answer

1. How do you invoke a skill in Claude?
2. What's the difference between a skill and a slash command?
3. Can plugins auto-trigger like skills can?
4. How are plugins different from MCP servers?
5. When would you create a skill vs a plugin?
6. Can skills call other skills?
7. How do slash commands relate to CLI functionality?

## Example Scenarios

For each scenario, determine whether to use a skill, slash command, or plugin:

1. **Scenario A**: You want to implement a TDD workflow that automatically triggers when user asks to implement a feature.

2. **Scenario B**: You need to connect Claude to your company's internal API to fetch data.

3. **Scenario C**: You want to clear the conversation history.

4. **Scenario D**: You want to create a reusable code review workflow that checks for security issues.

5. **Scenario E**: You need to integrate with a third-party service like Notion or GitHub.

## Research Tasks

1. List all available skills in your Claude installation
2. List all built-in slash commands
3. List all installed plugins
4. Find the skill definition for at least one skill
5. Find the configuration for at least one plugin

## Common Confusion Points

- Skills vs plugins: When to use which?
- Auto-triggering: What can and cannot auto-trigger?
- Invocation syntax: How to call each type?
- Customization: What can be modified where?
- Scope: Global vs project-specific configurations

## Documentation to Review

- Skills documentation in Claude Code
- MCP server documentation
- Plugin architecture overview
- Built-in slash commands reference
