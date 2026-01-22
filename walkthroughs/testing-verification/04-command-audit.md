# Walkthrough: Command Audit

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** Testing & Verification

---

## Overview

Claude executes commands on your behalf - but are they safe? This challenge teaches you to audit and review commands before they run, ensuring you maintain control over what happens on your system.

## Prerequisites

- [ ] Understanding of shell commands
- [ ] Awareness of dangerous operations
- [ ] Claude Code with command confirmation enabled

---

## Step 1: Understand Command Risk

### Risk Levels
```
🟢 Safe: Read-only operations
   ls, cat, git status, npm list

🟡 Moderate: Modifications within project
   npm install, git commit, file edits

🟠 High: System changes
   npm install -g, sudo commands, system configs

🔴 Critical: Destructive operations
   rm -rf, git push --force, DROP TABLE
```

---

## Step 2: Enable Command Review

### Claude Settings
Ensure you're reviewing commands before execution:

```json
{
  "permissions": {
    "autoApprove": false,
    "confirmAll": true
  }
}
```

### Review Prompt
When Claude wants to run a command, you'll see:
```
Claude wants to run:
  npm install lodash

[Allow] [Deny] [Edit]
```

---

## Step 3: Audit Checklist

### Before Approving Any Command

```
□ Do I understand what this command does?
□ Is the target correct (right file/directory)?
□ Are the flags/options expected?
□ Could this have unintended side effects?
□ Is this reversible if something goes wrong?
```

---

## Step 4: Common Dangerous Commands

### File Operations
```bash
# DANGEROUS - Recursive delete
rm -rf some_directory
# ASK: Is this the right directory?

# DANGEROUS - Wildcard delete
rm *.js
# ASK: Am I in the right directory?

# SAFER - Interactive delete
rm -i file.txt
```

### Git Operations
```bash
# DANGEROUS - Force push
git push --force
# ASK: Will this affect others?

# DANGEROUS - Hard reset
git reset --hard HEAD~3
# ASK: Will I lose uncommitted work?

# SAFER - Soft reset
git reset --soft HEAD~1
```

### System Operations
```bash
# DANGEROUS - Global install
sudo npm install -g package
# ASK: Do I need global install?

# DANGEROUS - Permission change
chmod -R 777 /path
# ASK: Is this too permissive?
```

---

## Step 5: Safe Alternatives

### Instead of Destructive Commands
```bash
# Instead of: rm -rf node_modules
# Use: mv node_modules node_modules.bak
# Then delete later after confirming

# Instead of: git push --force
# Use: git push --force-with-lease
# Safer force push

# Instead of: npm install unknown-pkg
# First: npm info unknown-pkg
# Check what you're installing
```

---

## Step 6: Create Command Whitelist

### In CLAUDE.md
```markdown
## Approved Commands
- git status, git diff, git log
- npm test, npm run build
- ls, cat, grep, find

## Requires Confirmation
- git commit, git push
- npm install, npm update
- File writes

## Never Auto-Approve
- rm (any form)
- git push --force
- sudo anything
- curl | bash
```

---

## Step 7: Audit Session Commands

### Review Command History
```
What commands have you executed this session?
```

Claude should provide:
```
Commands executed:
1. git status - Check repo state
2. npm test - Run tests
3. Read src/index.ts - View file
4. Edit src/index.ts - Modified function
```

### Check for Concerns
```
Were any of the commands you ran potentially destructive?
List them with risk levels.
```

---

## Verification Checklist

- [ ] Enabled command confirmation
- [ ] Denied at least one risky command
- [ ] Requested safer alternative
- [ ] Reviewed session command history
- [ ] Created command whitelist

---

## Red Flags to Watch For

| Pattern | Concern |
|---------|---------|
| `rm -rf` | Permanent deletion |
| `curl \| bash` | Unreviewed remote code |
| `--force` flags | Overrides safety checks |
| `sudo` or `admin` | Elevated privileges |
| Unfamiliar packages | Supply chain risk |
| `chmod 777` | Security weakening |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Approved dangerous command | Check for backups, revert if possible |
| Too many confirmations | Create appropriate whitelist |
| Don't understand command | Ask Claude to explain first |
| Need to run risky command | Use safer alternatives |

---

## Pro Tips

1. **Explain First:** Ask Claude to explain commands before running
2. **Dry Run:** Use `--dry-run` flags when available
3. **Backup First:** Ensure backups before destructive operations
4. **Scope Down:** Ask for less privileged alternatives

---

## Command Explanation Request

Before approving, ask:
```
Before I approve "npm install package --save-dev":
1. What does this package do?
2. Is it from a trusted source?
3. What are its dependencies?
4. Any known vulnerabilities?
```

---

## Next Challenge

Continue to **[TDD Workflow](./05-tdd-workflow.md)** for test-first development!
