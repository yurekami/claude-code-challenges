# Master Input Navigation - Solution

## Complete Readline Shortcuts Reference

### 1. Navigation Shortcuts

| Shortcut | Action | Example Use Case |
|----------|--------|------------------|
| `Ctrl+A` | Jump to beginning of line | Fix typo at start of long command |
| `Ctrl+E` | Jump to end of line | Add argument to end of command |
| `Alt+B` or `Alt+←` | Move backward one word | Navigate to specific word |
| `Alt+F` or `Alt+→` | Move forward one word | Skip to next argument |
| `Ctrl+X Ctrl+X` | Toggle between current position and line start | Quick back-and-forth editing |

**Practice Exercise 1:**
```bash
# Type this command:
$ docker run -d --name myapp -p 8080:8080 -e NODE_ENV=production -v /data:/app/data myimage:latest

# Tasks (use only shortcuts):
1. Ctrl+A - Jump to beginning
2. Alt+F Alt+F - Jump to "myapp"
3. Ctrl+E - Jump to end
4. Alt+B Alt+B - Jump to "myimage:latest"
```

### 2. Deletion Shortcuts

| Shortcut | Action | What Gets Deleted |
|----------|--------|-------------------|
| `Ctrl+W` | Delete word before cursor | Previous word |
| `Alt+D` | Delete word after cursor | Next word |
| `Ctrl+U` | Delete to beginning of line | Everything before cursor |
| `Ctrl+K` | Delete to end of line | Everything after cursor |
| `Ctrl+Y` | Paste (yank) last deleted text | Restore deleted content |
| `Ctrl+H` | Delete character before cursor | Same as Backspace |
| `Ctrl+D` | Delete character at cursor | Same as Delete |

**Practice Exercise 2:**
```bash
# Type this command:
$ npm install express react-dom vue angular svelte solid-js qwik

# Tasks:
1. Position cursor after "react-dom"
2. Ctrl+W - Delete "react-dom"
3. Ctrl+A, Alt+F Alt+F - Jump to "express"
4. Alt+D - Delete "express"
5. Ctrl+Y - Paste back "express"

# Result:
$ npm install express vue angular svelte solid-js qwik
```

### 3. Kill Ring (Copy/Paste)

The "kill ring" stores deleted text, allowing you to paste it elsewhere:

```bash
# Original command:
$ git commit -m "feat: add user authentication" --no-verify

# Steps:
1. Ctrl+A - Jump to start
2. Alt+F Alt+F Alt+F - Jump to "feat:"
3. Ctrl+K - Delete to end (stores in kill ring)
4. Type: git push origin feature-auth
5. Press Space
6. Ctrl+Y - Paste the commit message

# Result:
$ git push origin feature-auth --no-verify
```

### 4. History Navigation

| Shortcut | Action | Use Case |
|----------|--------|----------|
| `Ctrl+R` | Reverse search | Find previous command by keyword |
| `Ctrl+S` | Forward search | Search forward (may need `stty -ixon`) |
| `Ctrl+P` or `↑` | Previous command | Navigate history backward |
| `Ctrl+N` or `↓` | Next command | Navigate history forward |
| `Ctrl+G` | Cancel search | Exit Ctrl+R search |
| `Alt+<` | First command in history | Jump to oldest command |
| `Alt+>` | Last command in history | Jump to newest command |

**Practice Exercise 3:**
```bash
# Suppose you ran these commands earlier:
$ npm run build
$ npm run test
$ npm run deploy --env production

# Now you want to run build again:
1. Ctrl+R
2. Type: build
3. Press Enter

# To modify and run:
1. Ctrl+R
2. Type: deploy
3. Press Left Arrow (to edit instead of running)
4. Modify command
5. Press Enter
```

### 5. Advanced History Tricks

**Bang Commands:**
```bash
# Repeat last command
$ npm test
$ !!
# Runs: npm test

# Repeat last command with sudo
$ apt install nodejs
$ sudo !!
# Runs: sudo apt install nodejs

# Use last argument
$ cat /var/log/nginx/access.log
$ vim !$
# Runs: vim /var/log/nginx/access.log

# Use all arguments from previous command
$ git add src/app.js src/utils.js
$ git commit !*
# Runs: git commit src/app.js src/utils.js

# Run command from history by number
$ history | grep docker
# 123  docker ps -a
$ !123
# Runs: docker ps -a

# Search and replace in last command
$ git push origin mian  # Typo!
$ ^mian^main
# Runs: git push origin main
```

### 6. Editing Shortcuts

| Shortcut | Action | Example |
|----------|--------|---------|
| `Alt+T` | Swap current and previous words | Reorder arguments |
| `Ctrl+T` | Swap current and previous characters | Fix typos |
| `Ctrl+_` | Undo last change | Revert accidental deletion |
| `Alt+U` | Uppercase word after cursor | MAKE WORD UPPERCASE |
| `Alt+L` | Lowercase word after cursor | make word lowercase |
| `Alt+C` | Capitalize word after cursor | Make Word Capitalized |

**Practice Exercise 4:**
```bash
# Fix this command using only shortcuts:
$ git commit file.txt -m "update"

# Task: Move file.txt after -m "update"
1. Position cursor on "file.txt"
2. Ctrl+W - Delete "file.txt" (stores in kill ring)
3. Ctrl+E - Jump to end
4. Press Space
5. Ctrl+Y - Paste "file.txt"

# Result:
$ git commit -m "update" file.txt
```

### 7. Screen Control

| Shortcut | Action | Use Case |
|----------|--------|----------|
| `Ctrl+L` | Clear screen | Clean up terminal (keeps current line) |
| `Ctrl+S` | Stop output | Pause scrolling output |
| `Ctrl+Q` | Resume output | Resume after Ctrl+S |

### 8. Platform-Specific Shortcuts

**macOS Terminal:**
```bash
# Word navigation
Option+← - Move backward one word
Option+→ - Move forward one word
Cmd+K - Clear screen
Cmd+T - New tab
```

**Windows PowerShell:**
```powershell
# Most Ctrl shortcuts work
# Alt shortcuts may need configuration
Ctrl+A - Select all (different from readline!)
# Use Set-PSReadLineOption to enable readline shortcuts

# Fix Alt shortcuts in PowerShell:
Set-PSReadLineKeyHandler -Key Alt+F -Function ForwardWord
Set-PSReadLineKeyHandler -Key Alt+B -Function BackwardWord
Set-PSReadLineKeyHandler -Key Alt+D -Function DeleteWord
```

**Windows Terminal:**
```bash
# In Git Bash or WSL, all standard readline shortcuts work
# In PowerShell, add to $PROFILE:

Set-PSReadLineOption -EditMode Emacs
Set-PSReadLineKeyHandler -Key Ctrl+A -Function BeginningOfLine
Set-PSReadLineKeyHandler -Key Ctrl+E -Function EndOfLine
```

### 9. Real-World Scenarios

**Scenario 1: Long Docker Command**
```bash
# Original:
$ docker run -d --name myapp --network bridge -p 8080:8080 -e NODE_ENV=production -v /data:/app myimage:v1.2.3

# Fix: Change port from 8080 to 3000
1. Ctrl+R
2. Type: docker run
3. Press Left Arrow (to edit)
4. Alt+F (5 times) to get to "8080:8080"
5. Ctrl+W - Delete "8080:8080"
6. Type: 3000:3000
7. Press Enter

# Or quicker:
$ ^8080^3000
```

**Scenario 2: Git Command with Long Path**
```bash
# Typo at beginning:
$ gti add src/components/features/authentication/LoginForm.tsx

# Fix:
1. Ctrl+A
2. Ctrl+T - Swap 't' and 'i'
# Result: git add src/components/features/authentication/LoginForm.tsx
```

**Scenario 3: Reusing Arguments**
```bash
# You ran:
$ scp user@server:/path/to/remote/file.txt /local/path/

# Now want to ssh to same server:
$ ssh user@server
# Use Alt+. or !$ won't work here

# Better:
1. Ctrl+R
2. Type: scp
3. Left Arrow
4. Ctrl+A, Ctrl+K - Delete entire line
5. Type: ssh
6. Ctrl+Y - Paste
7. Edit to extract just "user@server"
```

**Scenario 4: Complex npm Command**
```bash
# Add package to long install command:
$ npm install express react vue angular svelte

# Add "typescript" at the beginning:
1. Ctrl+A
2. Alt+F Alt+F - Jump to "express"
3. Type: typescript
4. Press Space

# Result:
$ npm install typescript express react vue angular svelte
```

### 10. Configuration & Customization

**Enhance Readline (~/.inputrc):**
```bash
# Create or edit ~/.inputrc

# Enable case-insensitive completion
set completion-ignore-case on

# Show all completions immediately
set show-all-if-ambiguous on

# Color completion matches
set colored-stats on

# Single tab for completion
set show-all-if-unmodified on

# Append / to completed directories
set mark-directories on

# Enable visible stats
set visible-stats on

# Custom key bindings
"\C-p": history-search-backward
"\C-n": history-search-forward
```

**PowerShell Profile ($PROFILE):**
```powershell
# Enable Emacs editing mode
Set-PSReadLineOption -EditMode Emacs

# Enhanced history search
Set-PSReadLineKeyHandler -Key Ctrl+R -Function ReverseSearchHistory
Set-PSReadLineKeyHandler -Key Ctrl+S -Function ForwardSearchHistory

# Word navigation
Set-PSReadLineKeyHandler -Key Alt+F -Function ForwardWord
Set-PSReadLineKeyHandler -Key Alt+B -Function BackwardWord

# Delete word
Set-PSReadLineKeyHandler -Key Alt+D -Function DeleteWord
Set-PSReadLineKeyHandler -Key Ctrl+W -Function BackwardDeleteWord

# Predictive suggestions
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
```

**Zsh Configuration (~/.zshrc):**
```bash
# Enable Emacs key bindings
bindkey -e

# Better history search
bindkey '^R' history-incremental-search-backward
bindkey '^S' history-incremental-search-forward

# Word navigation
bindkey '^[^[[D' backward-word  # Alt+Left
bindkey '^[^[[C' forward-word   # Alt+Right

# History options
setopt HIST_IGNORE_DUPS
setopt HIST_FIND_NO_DUPS
setopt HIST_REDUCE_BLANKS
```

### 11. Practice Challenges

**Challenge 1: Speed Editing**
```bash
# Time yourself editing this command:
$ git commit -m "feat: add user authentication and authorization system"

# Tasks (under 10 seconds):
1. Change "feat" to "fix"
2. Add "--no-verify" at the end
3. Change "authentication" to "auth"

# Solution:
1. Ctrl+A, Alt+F Alt+F - Jump to "feat"
2. Ctrl+W, type: fix
3. Ctrl+E, type: --no-verify
4. Ctrl+R, type: auth, Left Arrow
5. Alt+F - Jump to "authentication"
6. Ctrl+W, type: auth
```

**Challenge 2: Command Reconstruction**
```bash
# You ran this 20 commands ago:
$ docker exec -it myapp npm run test:e2e -- --headed

# Reconstruct without typing full command:
1. Ctrl+R
2. Type: docker exec
3. Left Arrow
4. Alt+F (until at "test:e2e")
5. Ctrl+K - Delete to end
6. Type: test:unit

# Result:
$ docker exec -it myapp npm run test:unit
```

**Challenge 3: Multi-Edit**
```bash
# Edit this pipeline command:
$ cat file.txt | grep error | awk '{print $1}' | sort | uniq

# Change to:
$ cat access.log | grep 500 | awk '{print $2}' | sort -r | uniq -c

# Steps:
1. Ctrl+R, find command
2. Left Arrow
3. Alt+F - Jump to "file.txt"
4. Ctrl+W, type: access.log
5. Alt+F - Jump to "error"
6. Ctrl+W, type: 500
7. Continue editing each section
```

## Common Mistakes to Avoid

### 1. **Using Arrow Keys for Long Distances**
❌ Holding ← for 10 seconds
✅ Ctrl+A or Alt+B

### 2. **Retyping Instead of Editing**
❌ Clearing line and typing again
✅ Ctrl+R to find, then edit

### 3. **Not Using Kill Ring**
❌ Deleting text then retyping it elsewhere
✅ Ctrl+W then Ctrl+Y to move text

### 4. **Forgetting Ctrl+R**
❌ Scrolling through history with ↑
✅ Ctrl+R and type keyword

### 5. **Not Customizing Terminal**
❌ Using default limited configuration
✅ Configure ~/.inputrc or $PROFILE

## Verification Checklist

- [ ] Can navigate to line start/end without arrow keys
- [ ] Can jump between words using Alt shortcuts
- [ ] Can delete words/sections efficiently with Ctrl+W/K/U
- [ ] Can search command history with Ctrl+R
- [ ] Know how to use !! and !$
- [ ] Can use kill ring (Ctrl+W, Ctrl+Y)
- [ ] Configured custom shortcuts in ~/.inputrc or $PROFILE
- [ ] Completed all practice challenges
- [ ] Can edit complex commands 3x faster

## Time Savings

**Before (using arrow keys and retyping):**
- Navigate long command: 10-15 seconds
- Edit command: 20-30 seconds
- Find previous command: 5-10 seconds
- **Total: ~45 seconds per edit**

**After (using shortcuts):**
- Navigate long command: 1-2 seconds (Ctrl+A/E, Alt+F/B)
- Edit command: 5-10 seconds (Ctrl+W/K, Ctrl+Y)
- Find previous command: 2-3 seconds (Ctrl+R)
- **Total: ~10 seconds per edit**

**Daily Savings:**
- 50 command edits per day
- 35 seconds saved per edit
- **Total: ~30 minutes saved per day**

## Quick Reference Card

```
NAVIGATION          DELETION           HISTORY
Ctrl+A  Start       Ctrl+W  Word←      Ctrl+R  Search
Ctrl+E  End         Alt+D   Word→      Ctrl+P  Previous
Alt+B   Word←       Ctrl+U  ← Line     Ctrl+N  Next
Alt+F   Word→       Ctrl+K  → Line     !!      Repeat
                    Ctrl+Y  Paste      !$      Last arg

EDITING             SCREEN
Alt+T   Swap words  Ctrl+L  Clear
Ctrl+T  Swap chars  Ctrl+S  Stop
Ctrl+_  Undo        Ctrl+Q  Resume
```

Print this and keep it visible until shortcuts become muscle memory!

## Further Reading

- GNU Readline documentation
- Bash manual: Command Line Editing
- Zsh Line Editor (ZLE) documentation
- PowerShell PSReadLine module
- Emacs key bindings reference
