# Solution: Command Audit and Permission Management

## Overview

This solution demonstrates how to audit and manage Claude's command permissions effectively, balancing security with productivity.

## Step-by-Step Solution

### Step 1: Locate Settings File

```bash
# On macOS/Linux
cat ~/.claude/settings.json

# On Windows
type %USERPROFILE%\.claude\settings.json

# Or use Claude to show it
# "Show me my .claude/settings.json file"
```

### Step 2: Understand Settings Structure

```json
{
  "approvedCommands": [
    "git status",
    "npm test",
    "ls -la"
  ],
  "allowedTools": [
    "Read",
    "Write",
    "Bash"
  ],
  "autoApprove": false,
  "modelPreferences": {
    "default": "claude-sonnet-4.5"
  }
}
```

Key sections:
- `approvedCommands`: Commands that run without prompting
- `allowedTools`: Which tools Claude can use
- `autoApprove`: Dangerous flag that auto-approves all commands

### Step 3: Create Audit Script

```bash
# Create audit-permissions.sh
cat > audit-permissions.sh << 'EOF'
#!/bin/bash

SETTINGS_FILE="$HOME/.claude/settings.json"
REPORT_FILE="permission-audit-$(date +%Y%m%d).md"

echo "# Claude Command Permission Audit" > "$REPORT_FILE"
echo "Date: $(date)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Extract approved commands
echo "## Approved Commands" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

commands=$(jq -r '.approvedCommands[]' "$SETTINGS_FILE" 2>/dev/null)

if [ -z "$commands" ]; then
  echo "No approved commands found." >> "$REPORT_FILE"
  exit 0
fi

# Categorize by risk
echo "### High Risk Commands" >> "$REPORT_FILE"
echo "$commands" | grep -E "(rm -rf|sudo|curl.*bash|wget.*sh|dd if|mkfs|fdisk)" >> "$REPORT_FILE" || echo "None found" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "### Medium Risk Commands" >> "$REPORT_FILE"
echo "$commands" | grep -E "(npm install|pip install|docker|git push|git \*|mv|cp -r)" >> "$REPORT_FILE" || echo "None found" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "### Low Risk Commands" >> "$REPORT_FILE"
echo "$commands" | grep -E "(ls|cat|grep|git status|git log|git diff|npm test)" >> "$REPORT_FILE" || echo "None found" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Check for wildcards
echo "### Commands with Wildcards (Review Carefully)" >> "$REPORT_FILE"
echo "$commands" | grep "\*" >> "$REPORT_FILE" || echo "None found" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Check autoApprove flag
echo "### Auto-Approve Status" >> "$REPORT_FILE"
auto_approve=$(jq -r '.autoApprove' "$SETTINGS_FILE" 2>/dev/null)
if [ "$auto_approve" = "true" ]; then
  echo "⚠️  WARNING: autoApprove is enabled (DANGEROUS)" >> "$REPORT_FILE"
else
  echo "✓ autoApprove is disabled (SAFE)" >> "$REPORT_FILE"
fi
echo "" >> "$REPORT_FILE"

echo "## Recommendations" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "1. Review all High Risk commands" >> "$REPORT_FILE"
echo "2. Replace wildcard patterns with specific commands" >> "$REPORT_FILE"
echo "3. Remove unused permissions" >> "$REPORT_FILE"
echo "4. Consider project-specific permissions" >> "$REPORT_FILE"

echo "Audit report generated: $REPORT_FILE"
cat "$REPORT_FILE"
EOF

chmod +x audit-permissions.sh
./audit-permissions.sh
```

### Step 4: Manual Audit Process

#### Example Settings to Audit

```json
{
  "approvedCommands": [
    "git *",
    "npm install",
    "npm test",
    "rm -rf node_modules",
    "docker build -t myapp .",
    "curl https://example.com/api",
    "cat src/**/*.ts",
    "ls -la",
    "pytest",
    "tsc --noEmit"
  ]
}
```

#### Audit Analysis

| Command | Risk Level | Issue | Recommendation |
|---------|-----------|-------|----------------|
| `git *` | HIGH | Too broad, includes `git push --force` | Replace with specific: `git status`, `git log`, `git diff` |
| `npm install` | MEDIUM | Can install malicious packages | Keep but review package.json first |
| `npm test` | LOW | Safe in most contexts | Keep |
| `rm -rf node_modules` | MEDIUM | Destructive but scoped | Consider: `rm -rf node_modules` (exact match) |
| `docker build -t myapp .` | MEDIUM | Executes Dockerfile | Keep if you control Dockerfiles |
| `curl https://example.com/api` | MEDIUM | Network access | Acceptable if trusted domain |
| `cat src/**/*.ts` | LOW | Read-only | Keep |
| `ls -la` | LOW | Read-only | Keep |
| `pytest` | LOW | Test execution | Keep |
| `tsc --noEmit` | LOW | Type checking | Keep |

### Step 5: Improved Settings

```json
{
  "approvedCommands": [
    // Safe git operations (specific, not wildcard)
    "git status",
    "git log",
    "git log --oneline",
    "git diff",
    "git diff --staged",
    "git show",
    "git branch",

    // Safe read operations
    "ls",
    "ls -la",
    "cat src/**/*.ts",
    "cat package.json",
    "grep -r",

    // Build and test (safe in trusted projects)
    "npm test",
    "npm run test:unit",
    "npm run lint",
    "tsc --noEmit",
    "pytest",

    // Specific safe operations
    "rm -rf node_modules",  // Exact match, not wildcard
    "npm run build"
  ],

  // NEVER enable this
  "autoApprove": false
}
```

### Step 6: Project-Specific Permissions

Create `.claude/settings.json` in project root for project-specific overrides:

```json
// Project: web-app/.claude/settings.json
{
  "approvedCommands": [
    // Add project-specific commands
    "npm run dev",
    "npm run build",
    "npm run test:e2e",

    // Inherit global safe commands
    "@extend": "~/.claude/settings.json"
  ]
}
```

### Step 7: Permission Patterns

#### Safe Pattern: Specific Commands

```json
{
  "approvedCommands": [
    "npm test",              // Exact command
    "git status",            // Exact command
    "ls -la"                 // Exact command with flag
  ]
}
```

#### Unsafe Pattern: Wildcards

```json
{
  "approvedCommands": [
    "git *",                 // BAD: Includes git push --force
    "npm *",                 // BAD: Includes npm install malicious-pkg
    "rm *",                  // BAD: Can delete anything
    "*"                      // TERRIBLE: Allows everything
  ]
}
```

#### Safe Pattern: Scoped Wildcards

```json
{
  "approvedCommands": [
    "cat src/**/*.ts",       // OK: Read-only, scoped to src/
    "grep -r . src/",        // OK: Read-only, scoped
    "ls -la tests/"          // OK: Read-only, scoped
  ]
}
```

### Step 8: Dangerous Commands to Never Approve

```json
{
  "approvedCommands": [
    // NEVER APPROVE THESE:
    "rm -rf /",
    "rm -rf /*",
    "rm -rf *",
    "sudo *",
    "curl * | bash",
    "wget * | sh",
    "chmod 777 *",
    "eval *",
    "python -c *",
    "node -e *",
    ":(){:|:&};:",           // Fork bomb
    "dd if=/dev/zero of=/dev/sda",
    "mkfs.*",
    "fdisk *"
  ]
}
```

### Step 9: Regular Audit Workflow

```bash
# Create audit workflow script
cat > quarterly-audit.sh << 'EOF'
#!/bin/bash

echo "=== Claude Permission Quarterly Audit ==="
echo ""

# 1. Generate audit report
./audit-permissions.sh

# 2. Review commands
echo ""
echo "Review Questions:"
echo "1. Are all commands still needed?"
echo "2. Can any wildcards be made more specific?"
echo "3. Are there new risky commands?"
echo "4. Have project requirements changed?"

# 3. Backup current settings
cp ~/.claude/settings.json ~/.claude/settings.json.backup-$(date +%Y%m%d)

# 4. Interactive review
echo ""
echo "Open settings file for editing? (y/n)"
read -r response
if [ "$response" = "y" ]; then
  ${EDITOR:-nano} ~/.claude/settings.json
fi

echo ""
echo "Audit complete. Backup saved to ~/.claude/settings.json.backup-$(date +%Y%m%d)"
EOF

chmod +x quarterly-audit.sh
```

### Step 10: Create Permission Request Template

```bash
# When Claude needs a new permission
cat > permission-request-template.md << 'EOF'
# Permission Request

## Command
`[exact command here]`

## Purpose
[Why is this command needed?]

## Risk Assessment
- **Risk Level**: [Low/Medium/High]
- **Destructive**: [Yes/No]
- **Network Access**: [Yes/No]
- **Privilege Escalation**: [Yes/No]

## Scope
- **Global** or **Project-Specific**
- **Temporary** or **Permanent**

## Alternatives Considered
1. [Alternative 1]
2. [Alternative 2]

## Approval Decision
- [ ] Approved
- [ ] Denied
- [ ] Needs modification

## Notes
[Additional context or conditions]
EOF
```

## Common Audit Findings

### Finding 1: Overly Broad Git Permissions

```json
// Before
{
  "approvedCommands": ["git *"]
}

// After
{
  "approvedCommands": [
    "git status",
    "git log",
    "git log --oneline",
    "git diff",
    "git show"
  ]
}
```

### Finding 2: Unnecessary Historical Permissions

```json
// Before
{
  "approvedCommands": [
    "npm test",
    "npm run old-project-task",  // Project no longer exists
    "python manage.py runserver",  // Switched to Node.js
    "rake db:migrate"  // Old Ruby project
  ]
}

// After
{
  "approvedCommands": [
    "npm test"
  ]
}
```

### Finding 3: Dangerous Wildcards

```json
// Before
{
  "approvedCommands": [
    "rm -rf *"  // DANGEROUS
  ]
}

// After
{
  "approvedCommands": [
    "rm -rf node_modules",
    "rm -rf dist",
    "rm -rf .cache"
  ]
}
```

## Best Practices

### 1. Principle of Least Privilege

```json
// Apply minimal necessary permissions
{
  "approvedCommands": [
    // Only what's needed, nothing more
    "npm test",
    "git status"
  ]
}
```

### 2. Specific Over General

```json
// Prefer specific commands
{
  "approvedCommands": [
    "npm run test:unit",     // Specific
    "npm run test:integration"  // Specific
    // NOT: "npm run *"       // Too general
  ]
}
```

### 3. Regular Review Schedule

```bash
# Set calendar reminder
# - Monthly: Quick scan for new risks
# - Quarterly: Full audit with documentation
# - Annually: Complete review and cleanup
```

### 4. Documentation

```markdown
## Permission Decisions Log

### 2026-01-21
- Added: `npm test` - Reason: Needed for TDD workflow
- Removed: `git *` - Reason: Too broad, replaced with specific commands
- Modified: `rm -rf *` → `rm -rf node_modules` - Reason: Scoped to safe directory

### 2026-01-15
- Added: `tsc --noEmit` - Reason: Type checking for TypeScript project
```

### 5. Separation by Environment

```json
// Development settings (more permissive)
// ~/.claude/settings.dev.json
{
  "approvedCommands": [
    "npm test",
    "npm run dev",
    "npm run build"
  ]
}

// Production settings (restrictive)
// ~/.claude/settings.prod.json
{
  "approvedCommands": [
    "git status",
    "ls -la"
  ]
}
```

## Security Checklist

```markdown
### Before Approving a Command:

- [ ] Is it read-only? (Safest)
- [ ] Does it modify files? (Review scope)
- [ ] Does it access network? (Review destination)
- [ ] Does it require elevated privileges? (Deny)
- [ ] Does it execute arbitrary code? (Review carefully)
- [ ] Can it be more specific? (Avoid wildcards)
- [ ] Is there a safer alternative? (Use that instead)
- [ ] Do I trust the project context? (Essential)

### Red Flags (Auto-Deny):

- [ ] Contains `rm -rf /`
- [ ] Contains `sudo`
- [ ] Contains `curl | bash` or `wget | sh`
- [ ] Modifies system files
- [ ] Uses `eval` or similar
- [ ] Accesses `/dev/` devices
- [ ] Format/partition commands
```

## Integration with Claude Workflow

When Claude requests a new permission:

```markdown
1. **Claude Requests**: "I need to run `git push` to deploy"

2. **User Reviews**:
   - Is this necessary? (Yes, for deployment)
   - Is it safe? (Yes, if I trust the remote)
   - Should it be global? (No, project-specific)

3. **User Decision**:
   - Add to project-specific settings: `.claude/settings.json`
   - Not global: `~/.claude/settings.json`
   - Grant permission: `git push origin main` (specific branch)

4. **Documentation**:
   - Record in permission log
   - Set review reminder
   - Note any conditions
```

## Tools and Scripts

### Permission Analyzer

```python
#!/usr/bin/env python3
import json
import re

def analyze_permission(cmd):
    """Analyze command for security risks."""

    risks = []

    # Check for dangerous patterns
    if re.search(r'rm\s+-rf', cmd):
        risks.append("DESTRUCTIVE: Recursive force delete")
    if 'sudo' in cmd:
        risks.append("PRIVILEGED: Requires elevated access")
    if re.search(r'\|\s*(bash|sh)', cmd):
        risks.append("INJECTION: Pipes to shell")
    if '*' in cmd and not re.search(r'(cat|grep|ls)', cmd):
        risks.append("WILDCARD: Broad scope")

    # Risk score
    score = len(risks)
    level = "HIGH" if score >= 2 else "MEDIUM" if score == 1 else "LOW"

    return {
        "command": cmd,
        "risk_level": level,
        "risks": risks
    }

# Read settings
with open('settings.json') as f:
    settings = json.load(f)

# Analyze each command
print("Permission Analysis Report")
print("=" * 50)

for cmd in settings.get('approvedCommands', []):
    result = analyze_permission(cmd)
    print(f"\nCommand: {result['command']}")
    print(f"Risk: {result['risk_level']}")
    if result['risks']:
        print("Issues:")
        for risk in result['risks']:
            print(f"  - {risk}")
```

## Summary

Effective permission management requires:

1. **Regular Audits**: Monthly quick scans, quarterly deep reviews
2. **Minimal Permissions**: Only approve what's necessary
3. **Specific Commands**: Avoid wildcards when possible
4. **Risk Assessment**: Evaluate each command's potential impact
5. **Documentation**: Record decisions and rationale
6. **Separation**: Project-specific vs. global permissions
7. **Review Process**: Formal approval for new permissions

Security is ongoing. Stay vigilant.
