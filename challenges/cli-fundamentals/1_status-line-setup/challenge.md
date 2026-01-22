# Status Line Setup

**Related Tip:** Tip 0: Configure status line with model, Git branch, token usage

## Description

The status line in Claude Code provides critical information at a glance: the current AI model, Git branch, and token usage. Properly configuring and understanding this status line is your first step to mastering Claude Code CLI.

## Objective

Learn to configure and interpret the Claude Code status line to monitor your session's state, including model selection, Git context, and token consumption.

## Steps to Complete

1. Launch Claude Code in a Git repository
2. Locate the status line at the bottom of your terminal
3. Identify the three key components:
   - Current AI model (e.g., Sonnet 4.5, Haiku 4.5, Opus 4.5)
   - Git branch name
   - Token usage (used/total)
4. Switch between different models using the model selector
5. Monitor token usage as you interact with Claude
6. Create a new Git branch and observe the status line update

## Success Criteria

- [ ] Can identify the current model from the status line
- [ ] Can read the active Git branch from the status line
- [ ] Can interpret token usage metrics (percentage used)
- [ ] Understand when you're approaching context window limits
- [ ] Know how to switch models when needed

## Why This Matters

The status line is your dashboard for:
- **Model selection**: Choosing the right model for the task (Haiku for speed, Sonnet for balance, Opus for deep reasoning)
- **Git awareness**: Always knowing which branch you're working on
- **Context management**: Avoiding the last 20% of context window for complex tasks
- **Cost optimization**: Tracking token usage to manage API costs

## Challenge

Configure your Claude Code environment and take a screenshot of your status line showing:
- A custom Git branch (not main/master)
- At least 10% token usage
- The model you prefer for daily development work
