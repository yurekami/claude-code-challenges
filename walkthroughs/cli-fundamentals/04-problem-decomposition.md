# Walkthrough: Problem Decomposition

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** CLI Fundamentals

---

## Overview

Large, complex problems overwhelm both humans and AI. This challenge teaches you to break down big tasks into smaller, manageable pieces that Claude can handle effectively. This is a core skill for productive AI-assisted development.

## Prerequisites

- [ ] Completed basic CLI challenges
- [ ] Understanding of software development concepts
- [ ] A complex task or feature to practice with

---

## Step 1: Recognize When to Decompose

**Signs your task needs decomposition:**
- Claude gives incomplete or confused responses
- The task description is more than 3-4 sentences
- Multiple files or systems are involved
- You can't clearly define "done"
- The response would need 500+ lines of code

**Example of a task that needs decomposition:**
```
"Build a user authentication system with login, registration,
password reset, OAuth integration, session management,
and role-based access control"
```

---

## Step 2: The Decomposition Framework

Use this framework to break down any complex task:

### WHAT → WHY → HOW → VERIFY

```
┌──────────────────────────────────────────────────────┐
│  WHAT: Define the end goal clearly                   │
│    ↓                                                 │
│  WHY: Understand the purpose (guides decisions)      │
│    ↓                                                 │
│  HOW: Break into independent subtasks                │
│    ↓                                                 │
│  VERIFY: Define success criteria for each            │
└──────────────────────────────────────────────────────┘
```

---

## Step 3: Apply to Our Example

Let's decompose the authentication system:

### Level 1: Major Components
```
Authentication System
├── 1. User Registration
├── 2. User Login
├── 3. Password Reset
├── 4. Session Management
├── 5. OAuth Integration
└── 6. Role-Based Access Control
```

### Level 2: Subtasks for Each Component
```
1. User Registration
   ├── 1.1 Create registration form UI
   ├── 1.2 Implement form validation
   ├── 1.3 Create API endpoint
   ├── 1.4 Add database schema
   ├── 1.5 Send verification email
   └── 1.6 Handle verification link
```

---

## Step 4: Work with Claude Using Subtasks

**Instead of this (too vague):**
```
Build user registration
```

**Do this (specific subtask):**
```
Create the registration form component in React with fields for:
- Email (with validation)
- Password (with strength indicator)
- Confirm password
- Terms acceptance checkbox

Use our existing Button and Input components from src/components/ui
```

---

## Step 5: Sequential vs Parallel Tasks

Identify dependencies to optimize your workflow:

```
Can be done in PARALLEL:
├── Form UI design
├── Database schema design
└── Email template design

Must be done SEQUENTIALLY:
1. Database schema → 2. API endpoint → 3. Frontend integration
```

**Parallel Strategy:** Ask Claude to work on independent tasks in separate conversations.

---

## Step 6: The Todo List Approach

Use Claude's TodoWrite capability for complex tasks:

```
Create a todo list for implementing user registration:

1. [ ] Design database schema for users table
2. [ ] Create registration API endpoint
3. [ ] Build registration form component
4. [ ] Add form validation logic
5. [ ] Implement password hashing
6. [ ] Set up email verification
7. [ ] Write integration tests
8. [ ] Add error handling
```

Then work through each item systematically.

---

## Step 7: Practice Decomposition

### Exercise: Decompose This Task

**Original Task:**
```
"Add a shopping cart feature to our e-commerce site"
```

**Your Decomposition:**
```
Shopping Cart Feature
├── Data Layer
│   ├── Cart database schema
│   ├── Cart item model
│   └── Cart service/repository
├── Backend API
│   ├── Add to cart endpoint
│   ├── Remove from cart endpoint
│   ├── Update quantity endpoint
│   └── Get cart endpoint
├── Frontend UI
│   ├── Add to cart button
│   ├── Cart icon with count
│   ├── Cart dropdown/sidebar
│   └── Cart page
├── Business Logic
│   ├── Price calculation
│   ├── Inventory check
│   └── Guest vs logged-in cart
└── Testing
    ├── Unit tests
    ├── Integration tests
    └── E2E tests
```

---

## Step 8: Communicate Progress

After each subtask, summarize for context:

```
Status Update:
✅ Completed: Database schema, API endpoints
🔄 In Progress: Frontend cart component
📋 Next: Price calculation logic
🚫 Blocked: Waiting for payment gateway decision
```

---

## Verification Checklist

- [ ] Can identify when a task needs decomposition
- [ ] Apply the WHAT → WHY → HOW → VERIFY framework
- [ ] Break a complex feature into 5+ subtasks
- [ ] Identify parallel vs sequential dependencies
- [ ] Use todo lists to track progress
- [ ] Communicate status effectively to Claude

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Subtasks still too large | Keep decomposing until each is <30 min work |
| Lost context between subtasks | Start each with a brief summary of what's done |
| Forgot dependencies | Map out dependencies before starting |
| Over-decomposed | If subtask is <5 min, combine with related tasks |

---

## Decomposition Templates

### For Bug Fixes:
```
1. Reproduce the bug reliably
2. Identify the root cause
3. Write a failing test
4. Implement the fix
5. Verify the test passes
6. Check for regressions
```

### For New Features:
```
1. Define requirements and scope
2. Design the interface/API
3. Implement data layer
4. Implement business logic
5. Build UI components
6. Integrate and test
7. Document
```

### For Refactoring:
```
1. Write tests for current behavior
2. Identify code to change
3. Make incremental changes
4. Verify tests still pass
5. Update documentation
```

---

## Pro Tips

1. **Start Small:** If unsure, pick the smallest subtask first to build momentum
2. **Define Done:** Each subtask should have a clear completion criteria
3. **Context Windows:** New conversations for major component boundaries
4. **Document Decisions:** When Claude makes design choices, note them for consistency

---

## Next Challenge

Continue to **[Git Integration](./05-git-integration.md)** to master version control workflows with Claude!
