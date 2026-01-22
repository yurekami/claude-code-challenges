# Walkthrough: Handoff Documents

**Difficulty:** Medium | **Time:** 18 minutes | **Category:** Context Management

---

## Overview

Handoff documents are the secret to perfect session continuity. They capture everything needed to resume work seamlessly - whether after a break, in a new session, or when handing off to a colleague. Master this skill for uninterrupted productivity.

## Prerequisites

- [ ] Understanding of context compaction
- [ ] Experience with multi-session projects
- [ ] Basic markdown formatting skills

---

## Step 1: Understand Handoff Documents

A handoff document is a structured summary that enables:
- **Session continuity** - Resume exactly where you left off
- **Context transfer** - Share work state with others
- **Progress tracking** - Document what's done and what remains
- **Decision preservation** - Remember why choices were made

---

## Step 2: The Handoff Document Structure

```markdown
# Handoff Document: [Project/Feature Name]
Generated: [Timestamp]

## Current State
[One sentence describing where things stand]

## Objectives
- Primary: [Main goal]
- Secondary: [Supporting goals]

## Progress Summary
### Completed ✅
- [Item 1]
- [Item 2]

### In Progress 🔄
- [Current work item] - [X]% complete
  - Done: [What's finished]
  - Remaining: [What's left]

### Not Started 📋
- [Future item 1]
- [Future item 2]

## Key Decisions
| Decision | Rationale | Date |
|----------|-----------|------|
| [Choice made] | [Why] | [When] |

## Technical Context
### Architecture
[Brief overview of relevant architecture]

### Key Files
- `path/to/file.ts` - [Purpose]
- `path/to/other.ts` - [Purpose]

### Critical Code
```typescript
// Include only essential snippets
```

## Environment & Configuration
- Node version: X.X
- Database: [Type and setup]
- Key env vars: [List without values]

## Blockers & Issues
- [ ] [Blocker 1]
- [ ] [Issue discovered]

## Next Actions
1. [Immediate next step]
2. [Following step]
3. [Third priority]

## Notes for Future Self
- [Gotcha to remember]
- [Thing that took a while to figure out]
```

---

## Step 3: Generate a Handoff Document

Ask Claude to create one:

```
Create a handoff document for our current session. Include:
- What we've accomplished
- What's in progress
- Key decisions and their rationale
- Any code snippets that are critical
- Exact next steps to continue
```

**Pro Tip:** Be specific about what context matters most for your project.

---

## Step 4: Save and Version Handoffs

### File Naming Convention
```
docs/handoffs/
├── 2024-01-15-auth-implementation.md
├── 2024-01-16-auth-continuation.md
├── 2024-01-17-auth-testing.md
└── latest.md  # Symlink to most recent
```

### Git Integration
```bash
# Save handoff document
claude "Create a handoff document" > docs/handoffs/$(date +%Y-%m-%d)-session.md

# Commit it
git add docs/handoffs/
git commit -m "docs: Add session handoff for [feature]"
```

---

## Step 5: Resume from a Handoff

### Starting a New Session
```
I'm resuming work on the authentication feature. Here's the handoff document from my last session:

[Paste handoff document]

Let's continue from where we left off. The immediate next step is [X].
```

### Quick Resume
```
Resuming from handoff:
- Feature: JWT Authentication
- Progress: 60% complete
- Last completed: Login endpoint
- Next action: Implement refresh token rotation

Continue with the refresh token implementation.
```

---

## Step 6: Handoff Quality Checklist

Before ending a session, verify your handoff includes:

- [ ] **Clear objective** - What are we building?
- [ ] **Progress state** - What's done vs remaining?
- [ ] **Key decisions** - Why did we choose X over Y?
- [ ] **Critical code** - Snippets that show current approach
- [ ] **File locations** - Which files are relevant?
- [ ] **Next actions** - Exactly what to do next?
- [ ] **Blockers** - What might stop progress?
- [ ] **Context notes** - Non-obvious things to remember?

---

## Step 7: Handoff for Different Scenarios

### End of Day Handoff
```markdown
# EOD Handoff - 2024-01-15

## Stopping Point
Middleware complete, starting controller tests

## Time Spent
~3 hours on auth implementation

## For Tomorrow
1. Write controller tests (30 min estimated)
2. Add rate limiting (1 hour)
3. Documentation (30 min)

## Heads Up
- Redis connection is flaky in dev - might need restart
- Found potential security issue in token refresh - see notes
```

### Handoff to Colleague
```markdown
# Handoff: Auth Feature → [Colleague Name]

## Context
I've implemented the core auth, you're taking over for API integration.

## What I Did
- JWT signing/verification utilities
- Login/logout endpoints
- Basic middleware

## What You Need to Do
- Integrate with user service
- Add refresh token rotation
- Write integration tests

## Watch Out For
- Token expiry is 15 min (intentionally short)
- We're using RS256, keys are in /secrets/

## Questions to Ask Me
- Happy to pair on the user service integration
```

---

## Verification Checklist

- [ ] Created at least 3 handoff documents
- [ ] Successfully resumed from a handoff document
- [ ] Handoff includes all essential sections
- [ ] Versioned handoffs in your project
- [ ] Can create handoff in under 5 minutes

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Handoff too long | Keep under 1000 words, focus on essentials |
| Missing key details | Use the checklist every time |
| Outdated information | Generate fresh handoff before saving |
| Lost handoff files | Version control them in docs/handoffs/ |

---

## Pro Tips

1. **Template Files:** Create a handoff template in your project
2. **Auto-Generate:** Set up an alias: `alias handoff='claude "Create handoff document"'`
3. **Daily Practice:** Create handoffs even for short sessions
4. **Include Screenshots:** For UI work, include relevant screenshots

---

## Handoff Automation

Add to your shell config:

```bash
# Generate and save handoff document
save-handoff() {
    local date=$(date +%Y-%m-%d)
    local file="docs/handoffs/${date}-$(git branch --show-current).md"
    echo "Generate a handoff document for this session" | claude > "$file"
    echo "Handoff saved to $file"
    git add "$file"
}

# Quick handoff to clipboard
quick-handoff() {
    echo "Create a brief handoff summary" | claude | pbcopy
    echo "Handoff copied to clipboard!"
}
```

---

## Next Challenge

Continue to **[Session Recovery](./03-session-recovery.md)** to learn how to find and resume any conversation!
