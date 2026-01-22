# Walkthrough: Copy-Paste Power

**Difficulty:** Easy | **Time:** 8 minutes | **Category:** CLI Fundamentals

---

## Overview

Effective copy-paste is crucial for AI-assisted development. This challenge teaches you to efficiently transfer code, error messages, and context between your editor, terminal, and Claude Code.

## Prerequisites

- [ ] Terminal with clipboard support
- [ ] Text editor/IDE configured
- [ ] Understanding of your system's clipboard

---

## Step 1: Master Terminal Selection

### Select All Output
Most terminals support selecting large outputs:

**macOS Terminal/iTerm2:**
- `Cmd+A` - Select all visible text
- Triple-click - Select entire line
- `Cmd+Shift+Click` - Select range

**Windows Terminal:**
- `Ctrl+Shift+A` - Select all
- Right-click + Select - Rectangular selection
- `Ctrl+Shift+C` - Copy selection

**Linux (various):**
- `Ctrl+Shift+A` - Select all
- Middle-click - Paste primary selection

---

## Step 2: Copy Efficiently to Claude

### Error Messages
When you encounter an error:

```bash
npm run build 2>&1 | pbcopy  # macOS
npm run build 2>&1 | clip    # Windows
npm run build 2>&1 | xclip   # Linux
```

Then paste directly into Claude:
```
Here's the build error:

[Paste error output]

How do I fix this?
```

### Stack Traces
```bash
# Capture last command output (zsh)
# Install with: brew install pbcopy
echo "$last_output" | pbcopy
```

---

## Step 3: Paste Into Claude Effectively

### Large Code Blocks
When pasting large amounts of code:

```
Here's the complete file (250 lines):

```typescript
[Paste your code here]
```

Focus on the authentication logic starting at line 45.
```

**Pro Tip:** Tell Claude what to focus on after large pastes.

### Multi-File Paste
```
I'm pasting 3 related files:

File 1: src/api/user.ts
```typescript
[Paste]
```

File 2: src/types/user.ts
```typescript
[Paste]
```

File 3: tests/user.test.ts
```typescript
[Paste]
```

These files need to work together. Find any inconsistencies.
```

---

## Step 4: Smart Paste Formatting

### Preserve Formatting
```
Pasting code with preserved formatting:

```python
def calculate_tax(income: float) -> float:
    if income <= 10000:
        return 0
    elif income <= 50000:
        return income * 0.1
    else:
        return income * 0.2
```
```

### Strip Formatting (plain paste)
When pasting from rich text sources:
- Use "Paste as Plain Text" (Ctrl+Shift+V)
- This removes unwanted formatting

---

## Step 5: Clipboard Integration Patterns

### Quick Debug Loop
```bash
# 1. Copy error to clipboard
npm test 2>&1 | pbcopy

# 2. Paste to Claude
[Paste error in Claude]
"Fix this test failure"

# 3. Copy Claude's fix
[Select code, Cmd+C]

# 4. Apply to file
pbpaste > src/fixed-file.ts
```

### Editor Integration
Most editors support:
- Select code → Right-click → "Ask Claude" (with extensions)
- Copy to clipboard → Paste in Claude terminal

---

## Step 6: Multi-Clipboard Power

### macOS (with Flycut or Paste app)
- Keep history of clipboard items
- Quickly access previous copies
- Paste multiple items in sequence

### Windows (built-in)
- `Win+V` - Clipboard history
- Pin frequently used items
- Paste from history

---

## Verification Checklist

- [ ] Can select all terminal output efficiently
- [ ] Used clipboard piping (pbcopy/clip/xclip)
- [ ] Pasted multi-file context to Claude
- [ ] Applied Claude's output via clipboard
- [ ] Used clipboard history (if available)

---

## Efficient Copy Patterns

### Copy Error Context
```
Error + surrounding lines + file info
```

### Copy Relevant Code Only
```
Don't paste 1000 lines when 50 will do
```

### Copy with Metadata
```
// File: src/auth/login.ts
// Lines: 45-67
// Issue: TypeError on line 52

[Paste specific code section]
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Copied too much | Be selective, paste only relevant code |
| Formatting broken | Use code fences (```) for code |
| Special characters mangled | Check terminal encoding settings |
| Large paste truncated | Break into smaller chunks |

---

## Pro Tips

1. **Context Matters:** Include file path and line numbers when pasting
2. **Code Fences:** Always wrap code in proper markdown fences
3. **Error Complete:** Include the full error, not just the message
4. **Clipboard Apps:** Use clipboard managers for complex workflows

---

## Quick Reference

| Action | macOS | Windows | Linux |
|--------|-------|---------|-------|
| Copy | Cmd+C | Ctrl+C | Ctrl+Shift+C |
| Paste | Cmd+V | Ctrl+V | Ctrl+Shift+V |
| Select All | Cmd+A | Ctrl+A | Ctrl+Shift+A |
| Pipe to clipboard | `\| pbcopy` | `\| clip` | `\| xclip` |
| Paste from clipboard | `pbpaste` | `PowerShell: Get-Clipboard` | `xclip -o` |

---

## Next Challenge

Continue to **[Realpath Mastery](./10-realpath-mastery.md)** to become an expert at file path handling!
