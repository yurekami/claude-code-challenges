# Walkthrough: Realpath Mastery

**Difficulty:** Easy | **Time:** 10 minutes | **Category:** CLI Fundamentals

---

## Overview

File paths cause endless confusion: relative vs absolute, symlinks, platform differences. This challenge teaches you to use `realpath` and related tools to always work with unambiguous, absolute paths - essential for reliable Claude Code operations.

## Prerequisites

- [ ] Command line access
- [ ] Understanding of file system basics
- [ ] A project with some file structure

---

## Step 1: Understand Path Types

### Relative Paths
```
./src/index.ts           # From current directory
../config/settings.json  # Up one level
components/Button.tsx    # Implicit relative
```

### Absolute Paths
```
/Users/dev/project/src/index.ts     # macOS/Linux
C:\Users\dev\project\src\index.ts   # Windows
```

**Problem:** Relative paths break when working directory changes.
**Solution:** Use absolute paths with `realpath`.

---

## Step 2: Master `realpath`

### Basic Usage
```bash
# Get absolute path of a file
realpath src/index.ts
# Output: /Users/dev/project/src/index.ts

# Get absolute path of current directory
realpath .
# Output: /Users/dev/project
```

### Handle Non-existent Paths
```bash
# Works even if file doesn't exist yet
realpath -m src/new-file.ts
# Output: /Users/dev/project/src/new-file.ts
```

### Resolve Symlinks
```bash
# Follow symlinks to real location
realpath --physical node_modules/.bin/tsc
# Output: /Users/dev/project/node_modules/typescript/bin/tsc
```

---

## Step 3: Platform-Specific Alternatives

### macOS
```bash
# Built-in realpath (from coreutils)
realpath file.ts

# Alternative using Python
python -c "import os; print(os.path.realpath('file.ts'))"
```

### Windows (PowerShell)
```powershell
# Resolve-Path for existing files
(Resolve-Path .\src\index.ts).Path

# Convert-Path for UNC paths
Convert-Path .\src\index.ts

# Full path from relative (even non-existent)
[System.IO.Path]::GetFullPath(".\src\new-file.ts")
```

### Windows (Git Bash/WSL)
```bash
# Standard realpath works
realpath src/index.ts
```

---

## Step 4: Use in Claude Workflows

### Giving Claude Precise Paths
```
Edit the file at:
/Users/dev/project/src/components/Button.tsx

Not just "Button.tsx" which could be ambiguous.
```

### Quick Path Copying
```bash
# Copy file's absolute path to clipboard
realpath src/index.ts | pbcopy  # macOS
realpath src/index.ts | clip    # Windows
```

### Reference in Prompts
```bash
# Generate Claude-ready file reference
echo "Edit $(realpath src/index.ts)"
```

---

## Step 5: Path Manipulation Patterns

### Get Directory of a File
```bash
dirname $(realpath src/components/Button.tsx)
# Output: /Users/dev/project/src/components
```

### Get Filename Only
```bash
basename $(realpath src/components/Button.tsx)
# Output: Button.tsx
```

### Combine with File Operations
```bash
# Create file with absolute path
touch $(realpath -m src/new-feature/index.ts)

# Read file with guaranteed path
cat $(realpath config/settings.json)
```

---

## Step 6: Shell Integration

Add path helpers to your shell config:

```bash
# ~/.zshrc or ~/.bashrc

# Get absolute path and copy to clipboard
rp() {
    local path=$(realpath "$1")
    echo "$path"
    echo "$path" | pbcopy
    echo "Copied to clipboard!"
}

# Open file in editor with absolute path
ve() {
    code $(realpath "$1")
}

# Print project root
root() {
    realpath $(git rev-parse --show-toplevel)
}
```

**Usage:**
```bash
rp src/index.ts
# Output: /Users/dev/project/src/index.ts
# Also copied to clipboard!
```

---

## Verification Checklist

- [ ] Can use `realpath` to get absolute paths
- [ ] Know platform-specific alternatives
- [ ] Can copy absolute paths to clipboard
- [ ] Created shell helpers for path operations
- [ ] Understand when to use absolute vs relative paths

---

## When to Use Absolute Paths

| Situation | Use Absolute Path? |
|-----------|-------------------|
| Telling Claude which file to edit | YES |
| Git operations | Usually relative is fine |
| Build configurations | YES |
| Symlinked files | YES (with --physical) |
| Same-directory references | Relative is OK |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| `realpath: command not found` | Install coreutils or use alternatives |
| Path has spaces | Quote the path: `"$(realpath "my file.ts")"` |
| Symlink confusion | Use `realpath --physical` |
| Windows backslashes | Use forward slashes or quote properly |

---

## Pro Tips

1. **Always Absolute for Claude:** When referencing files for Claude, use absolute paths
2. **Path Variables:** Store common paths in variables
3. **Tab Completion:** Most shells complete paths - combine with `realpath`
4. **Clipboard Integration:** Set up quick copy-to-clipboard commands

---

## Path Resolution Reference

```bash
# File exists
realpath existing-file.ts     # Works perfectly

# File doesn't exist
realpath -m future-file.ts    # Still works with -m flag

# Directory
realpath .                    # Current directory
realpath ..                   # Parent directory
realpath ~                    # Home directory

# Symlinks
realpath --physical symlink   # Follow symlink
realpath --logical symlink    # Keep symlink in path

# From anywhere
realpath ~/project/src/file.ts  # Absolute from any directory
```

---

## Congratulations!

You've completed the **CLI Fundamentals** category! You now have a solid foundation in:

- Status line monitoring
- Slash commands
- Voice input
- Problem decomposition
- Git integration
- Fresh starts
- Output extraction
- Terminal aliases
- Copy-paste efficiency
- Path mastery

**Next:** Move on to **[Context Management](../context-management/01-context-compaction.md)** to optimize your 200k token window!
