# Realpath Mastery: Converting Relative to Absolute Paths

**Related Tip:** Tip 24: Convert relative to absolute paths

## Description

Claude Code works best with absolute paths. When you provide relative paths like `./src/file.ts` or `../config.json`, Claude must infer the full path based on context, which can lead to confusion. The `realpath` command (and platform equivalents) converts any relative path to its absolute form, eliminating ambiguity.

## Objective

Master path resolution techniques to always provide Claude Code with unambiguous absolute paths. Learn to use `realpath`, `readlink`, and platform-specific equivalents to convert relative paths on the fly.

## Why Absolute Paths Matter

### Clarity
- No ambiguity about file location
- Works from any working directory
- Prevents "file not found" errors

### Claude's Perspective
- Claude sees: `./src/auth.ts`
- Claude thinks: "Relative to where?"
- Better: `C:\Users\creat\project\src\auth.ts`
- Claude knows: Exact file location

### Multi-Directory Work
- Working across multiple projects
- Referencing files in parent directories
- Symlinking and complex structures

## The Problem

```
You: "Review the code in ../api/auth.ts"

Claude: [Confused - relative to what?]
        [May read wrong file or fail]

Better:
You: "Review the code in /home/user/project/api/auth.ts"

Claude: [Reads exact file with confidence]
```

## Path Resolution Tools

### Unix/Linux/macOS: `realpath`
Converts relative paths to absolute paths

### macOS (alternative): `greadlink -f`
GNU readlink, more powerful

### Windows: `realpath` (PowerShell 6+)
Or use Python one-liner as alternative

### Cross-platform: Python
Works everywhere Python is installed

## Steps to Complete

1. Learn your platform's path resolution command
2. Practice converting relative to absolute paths
3. Create aliases or functions for quick conversion
4. Integrate into Claude Code workflow
5. Understand edge cases (symlinks, .., ~)

## Success Criteria

- [ ] Can convert any relative path to absolute
- [ ] Know the right command for your platform
- [ ] Have a quick method (alias/function) set up
- [ ] Understand how symlinks are resolved
- [ ] Can handle paths with spaces and special characters
- [ ] Always provide absolute paths to Claude

## Challenge Tasks

### Task 1: Basic Conversion
Convert `./src/index.ts` to absolute path

### Task 2: Parent Directory
Convert `../../config/database.json` to absolute path

### Task 3: Home Directory
Convert `~/projects/myapp/main.py` to absolute path

### Task 4: Symlink Resolution
Create a symlink and resolve it to target's absolute path

### Task 5: Batch Conversion
Convert a list of 10 relative paths to absolute paths

### Task 6: Integration
Create a workflow where you always copy absolute paths

## Common Scenarios

### Scenario 1: File Reference
```bash
# Instead of:
"Review ./src/auth.ts"

# Use:
realpath ./src/auth.ts
# Output: /home/user/project/src/auth.ts

"Review /home/user/project/src/auth.ts"
```

### Scenario 2: Multiple Files
```bash
# Instead of listing relative paths
"Review these files:
./src/auth.ts
./src/user.ts
./tests/auth.test.ts"

# Convert all to absolute
realpath src/auth.ts src/user.ts tests/auth.test.ts

# Then paste absolute paths
```

### Scenario 3: Cross-Project Reference
```bash
# Working in project A, referencing project B
cd ~/projects/project-a
"Compare my auth.ts with ~/projects/project-b/auth.ts"

# Better:
realpath ~/projects/project-b/auth.ts
"Compare my auth.ts with /home/user/projects/project-b/auth.ts"
```

## Bonus Challenges

1. **Alias Creation**: Create `abs` alias that converts and copies to clipboard
2. **Editor Integration**: Configure editor to copy absolute paths
3. **Shell Function**: Function that converts and echoes, ready to paste
4. **Batch Script**: Script that converts all paths in a file
