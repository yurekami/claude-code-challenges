# Status Line Setup

## Difficulty: Easy

## Category: CLI Fundamentals

## Related Tips: 0

## Description

The Claude Code status line provides real-time information about your session including the model being used, current directory, git branch, and token usage. Customizing this display helps you stay informed and work more efficiently.

## Objective

Configure your Claude Code status line to display:
1. The current model name
2. Current working directory (shortened)
3. Git branch (when in a repository)
4. Token usage (used/remaining)

## Task

Run the appropriate Claude Code command to access status line settings and configure a custom status line format that includes all four elements listed above.

## Expected Outcome

Your status line should display information similar to:
```
claude-3-opus | ~/projects/myapp | main | 2.5k/100k tokens
```

## Hints

1. Claude Code has a dedicated command for configuring the status line
2. The format string uses placeholders like `{model}`, `{cwd}`, `{branch}`, `{tokens}`
3. You can test your configuration by observing the status line update

## Constraints

- Use only built-in Claude Code commands
- The configuration should persist across sessions

## Submission

Submit the command(s) you used to configure the status line.
