# Walkthrough: Input Navigation

**Difficulty:** Easy | **Time:** 10 minutes | **Category:** Workflow Automation

---

## Overview

Readline shortcuts let you navigate and edit command-line input at lightning speed. Master these to type less and accomplish more in your Claude Code sessions.

## Prerequisites

- [ ] Terminal/CLI access
- [ ] Basic typing skills
- [ ] Willingness to build muscle memory

---

## Step 1: Essential Movement

### Character Movement
| Shortcut | Action | Notes |
|----------|--------|-------|
| `Ctrl+B` | Back one character | Same as ← |
| `Ctrl+F` | Forward one character | Same as → |

### Word Movement
| Shortcut | Action |
|----------|--------|
| `Alt+B` | Back one word |
| `Alt+F` | Forward one word |
| `Ctrl+Left` | Back one word (alternative) |
| `Ctrl+Right` | Forward one word (alternative) |

### Line Movement
| Shortcut | Action |
|----------|--------|
| `Ctrl+A` | Go to beginning of line |
| `Ctrl+E` | Go to end of line |
| `Home` | Go to beginning |
| `End` | Go to end |

---

## Step 2: Deletion Shortcuts

### Character Deletion
| Shortcut | Action |
|----------|--------|
| `Ctrl+D` | Delete character under cursor |
| `Ctrl+H` | Delete character before cursor (backspace) |

### Word Deletion
| Shortcut | Action |
|----------|--------|
| `Ctrl+W` | Delete word before cursor |
| `Alt+D` | Delete word after cursor |
| `Alt+Backspace` | Delete word before cursor |

### Line Deletion
| Shortcut | Action |
|----------|--------|
| `Ctrl+U` | Delete from cursor to beginning |
| `Ctrl+K` | Delete from cursor to end |

---

## Step 3: Editing Shortcuts

### Undo/Redo
| Shortcut | Action |
|----------|--------|
| `Ctrl+_` | Undo last edit |
| `Ctrl+X, Ctrl+U` | Undo |

### Case Changes
| Shortcut | Action |
|----------|--------|
| `Alt+U` | Uppercase word |
| `Alt+L` | Lowercase word |
| `Alt+C` | Capitalize word |

### Transpose
| Shortcut | Action |
|----------|--------|
| `Ctrl+T` | Swap current and previous character |
| `Alt+T` | Swap current and previous word |

---

## Step 4: History Navigation

### Basic History
| Shortcut | Action |
|----------|--------|
| `Ctrl+P` | Previous command (same as ↑) |
| `Ctrl+N` | Next command (same as ↓) |
| `Ctrl+R` | Reverse search history |
| `Ctrl+S` | Forward search history |

### History Search
```
Type: Ctrl+R
Prompt: (reverse-i-search)`git':
Type: git com
Match: git commit -m "last message"
Press: Enter to execute, Right to edit
```

---

## Step 5: Special Operations

### Clear and Execute
| Shortcut | Action |
|----------|--------|
| `Ctrl+L` | Clear screen (keep current line) |
| `Ctrl+C` | Cancel current input |
| `Ctrl+Z` | Suspend process |

### Paste
| Shortcut | Action |
|----------|--------|
| `Ctrl+Y` | Yank (paste) last killed text |
| `Alt+Y` | Cycle through kill ring |

---

## Step 6: Practice Exercises

### Exercise 1: Quick Fix
```
Type: git commit -m "wrong messge"
Fix:  1. Ctrl+A (go to start)
      2. Alt+F (forward 3 words)
      3. Alt+B (back to "messge")
      4. Fix typo
      5. Ctrl+E (go to end)
      6. Enter
```

### Exercise 2: Command Modification
```
Type: npm install lodash --save
Change to: npm install lodash --save-dev

1. Ctrl+E (end of line)
2. Alt+B (back one word)
3. Add "-dev"
```

### Exercise 3: Quick Delete
```
Type: npm run test:unit && npm run test:integration
Want: npm run test:integration

1. Ctrl+A
2. Alt+D (delete "npm")
3. Alt+D (delete "run")
4. Alt+D (delete "test:unit")
5. Alt+D (delete "&&")
```

---

## Verification Checklist

- [ ] Can move by character, word, and line
- [ ] Can delete by character, word, and line
- [ ] Can search command history (Ctrl+R)
- [ ] Can undo edits
- [ ] Completed practice exercises

---

## Shortcut Cheat Sheet

```
Movement:
Ctrl+A/E     ←────────────────→    Start/End of line
Alt+B/F      ←word──word──→        By word
Ctrl+B/F     ←─→                   By character

Deletion:
Ctrl+U       ←═══╳ cursor          Delete to start
Ctrl+K              cursor ╳═══→   Delete to end
Ctrl+W       ←word╳                Delete word back
Alt+D              ╳word→          Delete word forward

History:
Ctrl+R       Search backward
Ctrl+P/N     Previous/Next command
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Alt not working (macOS) | Terminal → Preferences → Use Option as Meta |
| Ctrl+S freezes terminal | Press Ctrl+Q to unfreeze |
| Can't remember shortcuts | Practice 5 minutes daily |

---

## Pro Tips

1. **Start with 5:** Learn Ctrl+A, Ctrl+E, Ctrl+W, Ctrl+R, Ctrl+C first
2. **Daily Practice:** Use shortcuts instead of arrow keys
3. **Muscle Memory:** Takes 2-3 weeks of consistent use
4. **Combine:** Ctrl+A then Ctrl+K = delete entire line

---

## Next Challenge

Continue to **[Planning & Prototyping](./06-planning-prototyping.md)** to balance planning with action!
