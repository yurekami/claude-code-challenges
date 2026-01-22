# Terminal Cascade - Solution

## Step-by-Step Solution

### 1. Terminal Setup

**For Windows Terminal:**
```
Ctrl+Shift+T - New tab
Ctrl+Tab - Next tab
Ctrl+Shift+Tab - Previous tab
Ctrl+Alt+1-9 - Jump to specific tab
```

**For iTerm2 (macOS):**
```
Cmd+T - New tab
Cmd+Shift+] - Next tab
Cmd+Shift+[ - Previous tab
Cmd+1-9 - Jump to specific tab
```

**For tmux:**
```bash
Ctrl+B C - Create new window
Ctrl+B N - Next window
Ctrl+B P - Previous window
Ctrl+B 0-9 - Jump to window number
```

### 2. Example Cascade Setup

**Tab 1: Development Server**
```bash
# Navigate to project
cd C:\Users\creat\CCC\my-project

# Start dev server
npm run dev
# or
python manage.py runserver
# or
cargo watch -x run
```

**Tab 2: Log Monitoring**
```bash
# Tail application logs
tail -f logs/app.log

# Or monitor multiple logs
tail -f logs/*.log

# On Windows (PowerShell)
Get-Content logs\app.log -Wait -Tail 50
```

**Tab 3: Git Operations**
```bash
# Keep this tab clean for git work
cd C:\Users\creat\CCC\my-project
git status

# Use for commits, branches, etc.
```

**Tab 4: Claude Code / General**
```bash
# Available for ad-hoc commands
cd C:\Users\creat\CCC\my-project

# Run tests
npm test

# Build project
npm run build

# Use Claude Code
claude "refactor this component"
```

### 3. Advanced Cascade Patterns

**Frontend + Backend + Database**
```
Tab 1: Frontend (npm run dev)
Tab 2: Backend API (python app.py)
Tab 3: Database logs (docker logs -f postgres)
Tab 4: General commands
```

**Microservices Development**
```
Tab 1: Service A (npm run dev:service-a)
Tab 2: Service B (npm run dev:service-b)
Tab 3: Service C (npm run dev:service-c)
Tab 4: API Gateway (npm run dev:gateway)
Tab 5: Logs aggregator (tail -f logs/*.log)
Tab 6: General commands
```

### 4. Workflow Example

**Complete Development Cycle:**

1. **Tab 4 (General)**: Edit file with Claude Code
   ```bash
   claude "add error handling to user login"
   ```

2. **Tab 1 (Dev)**: Monitor automatic rebuild
   ```
   [watch] build finished, watching for changes...
   ```

3. **Tab 2 (Logs)**: Check for errors
   ```
   [INFO] Server reloaded
   [WARN] No errors detected
   ```

4. **Tab 3 (Git)**: Commit changes
   ```bash
   git add src/auth/login.ts
   git commit -m "feat: add error handling to user login"
   ```

5. **Tab 4 (General)**: Run tests
   ```bash
   npm test -- login.test.ts
   ```

### 5. Pro Tips

**Naming Tabs:**
- Windows Terminal: Right-click tab → Rename
- iTerm2: Cmd+I → Tab → Title
- tmux: `Ctrl+B ,` then type name

**Session Management:**
```bash
# Save tmux session
tmux new -s dev-session

# Detach and reattach later
Ctrl+B D
tmux attach -t dev-session

# List all sessions
tmux ls
```

**Color-Coding (tmux):**
```bash
# In .tmux.conf
set -g window-status-format "#[fg=white]#I:#W"
set -g window-status-current-format "#[fg=green,bold]#I:#W"
```

## Common Mistakes to Avoid

### 1. **Too Many Tabs**
❌ Opening 10+ tabs and losing track
✅ Limit to 4-6 focused tabs per workflow

### 2. **Not Using Keyboard Shortcuts**
❌ Using mouse to click between tabs
✅ Learn and use Ctrl+Tab or equivalent

### 3. **Forgetting Running Processes**
❌ Starting duplicate servers because you forgot which tab
✅ Name tabs clearly and check before starting

### 4. **No Session Persistence**
❌ Losing all tabs when terminal crashes
✅ Use tmux or terminal's session saving feature

### 5. **Not Monitoring Logs**
❌ Making changes without checking server output
✅ Keep log tab visible or use split panes

## Advanced Techniques

### Split Panes + Tabs
```bash
# tmux: Split current pane
Ctrl+B % # Vertical split
Ctrl+B " # Horizontal split

# View logs + commands in same tab
```

### Automated Startup Script
```bash
#!/bin/bash
# start-dev.sh

tmux new-session -d -s dev 'cd ~/project && npm run dev'
tmux split-window -v 'cd ~/project && tail -f logs/app.log'
tmux new-window 'cd ~/project'
tmux attach -t dev
```

### Process Monitoring Dashboard
```bash
# Use htop in one tab to monitor resource usage
htop

# Or use watch for continuous monitoring
watch -n 1 'ps aux | grep node'
```

## Verification Checklist

- [ ] Can switch between tabs using only keyboard
- [ ] All 4 tabs serve distinct purposes
- [ ] Tabs are named/labeled clearly
- [ ] Can complete edit-build-test cycle without closing tabs
- [ ] Understand how to save and restore session
- [ ] Can monitor multiple processes simultaneously

## Time Savings

- **Before**: 2-3 minutes per context switch (close, restart, wait)
- **After**: 0.5 seconds per tab switch
- **Daily savings**: 30-45 minutes on 20+ context switches
