# Walkthrough: Abstraction Levels

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** Advanced Orchestration

---

## Overview

Effective communication with Claude requires choosing the right level of abstraction. Too high-level and you get generic solutions; too detailed and you waste time on obvious steps. This challenge teaches you to work at the appropriate level for each task.

## Prerequisites

- [ ] Task to accomplish
- [ ] Understanding of your codebase
- [ ] Awareness of what you know vs. need help with

---

## Step 1: Understanding Abstraction Levels

### The Spectrum
```
High Level (Strategic)
│   "Make the app faster"
│   "Add authentication"
│   "Improve user experience"
│
├── Mid Level (Tactical)
│   "Add Redis caching for API responses"
│   "Implement JWT token refresh"
│   "Add loading states to forms"
│
└── Low Level (Operational)
    "Add cache.get() call on line 45"
    "Set token expiry to 15 minutes"
    "Add spinner component to Submit button"
```

---

## Step 2: Choosing Your Level

### Use High Level When
```
- Starting a new feature
- Exploring options
- You don't know the best approach
- You want Claude to make architectural decisions

Example:
"I need to add real-time notifications to my app.
What are my options and what would you recommend?"
```

### Use Mid Level When
```
- You know what you want, not how to implement
- You want guidance but have preferences
- Collaborating on design decisions

Example:
"Add WebSocket-based notifications using Socket.io.
The backend is Express, frontend is React.
Show me the architecture before implementing."
```

### Use Low Level When
```
- You know exactly what you need
- Making small, specific changes
- Fixing a known bug

Example:
"In src/socket.ts line 23, change the reconnection
attempts from 3 to 5 and add exponential backoff."
```

---

## Step 3: Level Mismatch Problems

### Too High for Simple Tasks
```
Bad: "Help me with authentication"
     → Long discussion about auth strategies
     → Wastes time when you just need a fix

Better: "The JWT token isn't being included in API requests.
        Check src/api/client.ts"
```

### Too Low for Complex Tasks
```
Bad: "Add useState hook on line 15 of UserForm.tsx"
     → Misses the bigger picture
     → May create inconsistencies

Better: "Add form state management to UserForm.
        It should validate on submit and show errors."
```

---

## Step 4: Dynamic Level Shifting

### Start High, Drill Down
```
Round 1: "I need to improve API performance"
Claude: "Here are the main approaches..."

Round 2: "Let's focus on caching. What options?"
Claude: "Redis, in-memory, CDN..."

Round 3: "Implement Redis caching for the /products endpoint"
Claude: [Implements specific solution]
```

### Start Low, Zoom Out
```
Round 1: "This function is slow"
Claude: [Identifies bottleneck]

Round 2: "This seems like a deeper architectural issue"
Claude: [Discusses broader patterns]

Round 3: "Let's refactor this whole module"
Claude: [Comprehensive solution]
```

---

## Step 5: Level-Appropriate Prompts

### Strategic Prompts (High)
```
"Design a system for..."
"What's the best approach to..."
"Evaluate options for..."
"Architect a solution that..."
"What are the tradeoffs between..."
```

### Tactical Prompts (Mid)
```
"Implement X using Y approach"
"Add feature X to component Y"
"Refactor X to use pattern Y"
"Create a service that does X"
"Write tests for the X functionality"
```

### Operational Prompts (Low)
```
"Change X to Y in file Z"
"Add parameter X to function Y"
"Fix the bug where X happens"
"Update the import on line X"
"Rename variable X to Y"
```

---

## Step 6: Abstraction Indicators

### Signs You Need to Go Higher
```
- You keep fixing symptoms, not causes
- Changes create new problems elsewhere
- You don't understand why something works
- Claude's solutions feel band-aid-like
```

### Signs You Need to Go Lower
```
- Discussions feel abstract and theoretical
- No concrete progress after several exchanges
- Claude keeps asking clarifying questions
- You know what you want but aren't getting it
```

---

## Step 7: Practical Examples

### Feature Addition
```
High: "Add user preferences to the app"

Mid: "Add a preferences page where users can set:
      - Theme (light/dark)
      - Notification settings
      - Language
      Store in the database, sync to frontend."

Low: "Add a 'theme' column to the users table,
      create an API endpoint at PATCH /users/preferences,
      add a toggle switch in SettingsPage.tsx"
```

### Bug Fix
```
High: "The app crashes sometimes"

Mid: "Users report crashes when loading large lists.
      Investigate the ProductList component and
      the /api/products endpoint."

Low: "In ProductList.tsx line 45, the map function
      throws when products is undefined. Add null check."
```

---

## Verification Checklist

- [ ] Identified a task and chose appropriate abstraction level
- [ ] Practiced shifting between levels
- [ ] Recognized when to zoom in or out
- [ ] Completed a task using level-appropriate prompts

---

## Abstraction Level Cheat Sheet

| Situation | Start Level | Shift To |
|-----------|-------------|----------|
| New feature | High | Mid → Low |
| Known bug | Low | Mid if needed |
| Refactoring | Mid | Low for changes |
| Learning | High | Mid for details |
| Quick fix | Low | Stay low |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Getting stuck in theory | Shift to mid-level, ask for implementation |
| Missing forest for trees | Zoom out, describe the goal |
| Generic solutions | Add specific constraints and context |
| Overly specific requests | Describe the problem, not just the symptom |

---

## Pro Tips

1. **Match Expertise:** High level for unfamiliar territory, low level for your domain
2. **State Your Level:** "Give me a high-level overview" or "Specific implementation please"
3. **Iterate:** Start somewhere, adjust based on responses
4. **Context Matters:** Same task, different levels based on situation

---

## Next Challenge

Continue to **[Iterative Problem Solving](./09-iterative-problem-solving.md)** for systematic debugging!
