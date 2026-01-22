# Challenge: Command Audit and Permission Management

**Related Tip**: Tip 33 - Audit approved commands in .claude/settings.json

## Description

Learn to audit and manage Claude's approved commands in `.claude/settings.json`. Understanding the permission system helps maintain security while enabling Claude to work efficiently. This challenge teaches you to review, understand, and configure command permissions appropriately.

## Objective

Master the command approval system in Claude Code:
- Understand how permissions are stored and managed
- Audit existing approved commands for security risks
- Configure appropriate permissions for different projects
- Balance convenience with security
- Recognize dangerous permission patterns

## Background

Claude Code uses a permission system to control which commands can run without prompting the user. Commands are stored in `.claude/settings.json` in the `approvedCommands` array. While auto-approval speeds up workflows, it's important to regularly audit these permissions to ensure:

1. No dangerous commands are auto-approved
2. Permissions are scoped appropriately
3. Unnecessary permissions are removed
4. Security risks are minimized

## Permission Risks

### High Risk
- `rm -rf` (file deletion)
- `sudo` commands (elevated privileges)
- `curl | bash` (remote code execution)
- Database modification commands
- Network configuration changes
- System service control

### Medium Risk
- Build commands that run arbitrary code
- Package installations (`npm install`, `pip install`)
- File writes to system directories
- Git push/force operations

### Low Risk
- Read-only operations (`ls`, `cat`, `grep`)
- Git read operations (`git status`, `git log`)
- Test execution (in sandboxed environments)

## Steps to Complete

1. **Locate your settings file**:
   - Find `.claude/settings.json` in your home directory
   - Understand the structure of the settings file
   - Identify the `approvedCommands` section

2. **Audit existing permissions**:
   - Review all approved commands
   - Categorize by risk level
   - Identify overly broad permissions (wildcards)
   - Find unused or outdated permissions

3. **Create an audit report**:
   - List all approved commands
   - Flag security concerns
   - Recommend removals or restrictions
   - Document safe alternatives

4. **Optimize permissions**:
   - Remove unnecessary permissions
   - Replace broad permissions with specific ones
   - Use command patterns safely
   - Configure project-specific permissions

5. **Establish audit practices**:
   - Set up regular audit schedule (monthly/quarterly)
   - Create approval criteria for new commands
   - Document permission decisions
   - Test changes don't break workflows

## Success Criteria

- [ ] Located and read `.claude/settings.json`
- [ ] Listed all approved commands
- [ ] Categorized commands by risk level
- [ ] Identified at least 3 potential security issues
- [ ] Created a permission audit report
- [ ] Removed or restricted risky permissions
- [ ] Tested that critical workflows still function
- [ ] Documented permission policies for future reference
- [ ] Understand when to approve vs. deny commands

## Example Audit

```json
// Current approvedCommands (example)
{
  "approvedCommands": [
    "git *",              // RISKY: Too broad, includes git push --force
    "npm install *",      // MEDIUM: Can install malicious packages
    "rm -rf *",           // DANGEROUS: Can delete anything
    "curl *",             // RISKY: Can fetch/execute remote content
    "docker *",           // RISKY: Container operations
    "cat *",              // SAFE: Read-only
    "ls *",               // SAFE: Read-only
    "npm test"            // SAFE: Specific test command
  ]
}
```

## Bonus Challenges

1. Create a script to automatically audit permissions
2. Set up permission profiles for different project types
3. Implement a permission request/approval workflow
4. Create documentation for team members on permission policies
5. Build a tool to analyze command patterns in Claude logs

## Common Pitfalls

- Approving commands with wildcards (`*`) too broadly
- Not reviewing permissions after project completion
- Approving dangerous commands for convenience
- Using global permissions when project-specific would work
- Not testing permission changes before committing
- Forgetting about approved commands from old projects

## Permission Audit Checklist

```markdown
## Command Audit Checklist

### For Each Approved Command:

- [ ] Is this command still needed?
- [ ] Is the permission scope minimal?
- [ ] Could it be more specific?
- [ ] Does it include dangerous operations?
- [ ] Is there a safer alternative?
- [ ] Should it be project-specific instead of global?
- [ ] Has the project context changed?
- [ ] Would I approve this again today?

### Red Flags:

- [ ] Commands with `rm -rf`
- [ ] Commands with `sudo`
- [ ] Commands with `curl | bash` or `wget | sh`
- [ ] Wildcards in dangerous commands (`git *`, `docker *`)
- [ ] Commands that modify system files
- [ ] Commands that access network without validation
- [ ] Commands that run arbitrary code
```

## Security Guidelines

### DO Approve:
- Read-only operations (`cat`, `ls`, `grep`)
- Specific test commands (`npm test`, `pytest`)
- Safe git operations (`git status`, `git log`, `git diff`)
- Build commands in trusted projects
- Linters and formatters

### DON'T Approve:
- Commands with `rm -rf`
- Commands with `sudo`
- Wildcard git operations (`git *`)
- Package installation without review
- Database modification commands
- System configuration changes
- Arbitrary script execution

### CONDITIONAL Approve:
- `npm install` (only for trusted projects)
- `git push` (only to specific remotes)
- `docker build` (only for reviewed Dockerfiles)
- Test execution (only in isolated environments)

## Related Concepts

- Principle of Least Privilege
- Security Auditing
- Permission Models
- Command Injection Prevention
- Sandbox Security
- Access Control Lists
