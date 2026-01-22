# Walkthrough: Learning by Doing

**Difficulty:** Easy | **Time:** 15 minutes | **Category:** Advanced Orchestration

---

## Overview

The best way to learn is by doing. Claude can guide you through hands-on exercises, explain concepts as you encounter them, and help you build understanding through practice.

## Prerequisites

- [ ] Curiosity about a new topic
- [ ] Willingness to experiment
- [ ] Time for hands-on practice

---

## Step 1: The Learning Loop

```
┌─────────────────────────────────────┐
│          Learning Loop              │
├─────────────────────────────────────┤
│   Try Something                     │
│        ↓                            │
│   Encounter Problem/Question        │
│        ↓                            │
│   Ask Claude for Explanation        │
│        ↓                            │
│   Understand Concept                │
│        ↓                            │
│   Apply Understanding               │
│        ↓                            │
│   ← Repeat                          │
└─────────────────────────────────────┘
```

---

## Step 2: Start with a Goal

### Bad: Abstract Learning
```
"Teach me about Docker"
→ Long lecture, passive reading
```

### Good: Project-Based Learning
```
"Help me containerize my Node.js app.
I know nothing about Docker.
Explain each step as we go."
→ Learn by doing, concepts in context
```

---

## Step 3: Ask "Why" and "How"

### During Implementation
```
You: "Why did we use COPY instead of ADD?"
Claude: [Explains the difference in context]

You: "How does this port mapping work?"
Claude: [Explains with your specific example]
```

### Build Understanding Incrementally
```
Step 1: Basic container (just makes it work)
Step 2: Add environment variables (explain why)
Step 3: Add volumes (explain the concept)
Step 4: Multi-stage build (explain optimization)
```

---

## Step 4: Learn Through Errors

### Embrace Errors
```
You: "I got this error: [error message]"
Claude: "This error means... Here's what's happening..."
→ Error becomes teaching moment
```

### Debug Together
```
You: "It's not working as expected"
Claude: "Let's debug step by step:
1. First, let's check...
2. Can you run this command?
3. Ah, I see the issue..."
→ Learn debugging process
```

---

## Step 5: Learning Prompts

### For New Concepts
```
I want to learn [topic] by building [project].
I'm a complete beginner.
Walk me through it step by step.
Explain each new concept when we encounter it.
```

### For Deepening Knowledge
```
I know the basics of [topic].
Help me understand [advanced concept] by implementing [feature].
Challenge my understanding with questions.
```

### For Practical Skills
```
I need to [practical task] but never done it before.
Guide me through it like a pair programming session.
Explain the "why" behind each decision.
```

---

## Step 6: Active Learning Techniques

### Explain Back
```
You: "Let me explain what I understand: [your explanation]"
Claude: "That's correct, except... [clarification]"
```

### Predict Then Verify
```
You: "I think running this will produce [prediction]"
Claude: "Let's try it... [result]. Your prediction was [correct/incorrect] because..."
```

### Teach It Back
```
You: "How would I explain Docker volumes to someone else?"
Claude: "Good summary! You might also mention..."
```

---

## Step 7: Learning Workflows

### New Technology
```
1. "What's the simplest thing I can do with [tech]?"
2. Build that simple thing
3. "Now how do I add [feature]?"
4. Repeat, increasing complexity
```

### New Language
```
1. "Help me write Hello World in [language]"
2. "Now help me read a file"
3. "How do I handle errors?"
4. Build small, increasing complexity
```

### New Framework
```
1. "Create minimal [framework] project"
2. "Add a basic [feature]"
3. "How does [concept] work here?"
4. Gradually add framework features
```

---

## Verification Checklist

- [ ] Started a hands-on learning project
- [ ] Asked "why" questions during implementation
- [ ] Learned from at least one error
- [ ] Explained a concept back to Claude
- [ ] Completed something that works

---

## Learning Mindsets

| Instead of | Try |
|------------|-----|
| "Teach me X" | "Help me build Y using X" |
| "I don't understand" | "Let me try to explain what I think..." |
| "Just give me the code" | "Walk me through the solution" |
| "This is too hard" | "What's the smallest step I can take?" |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Passive reading | Actively type and try code |
| Skipping the "why" | Always ask why decisions are made |
| Moving too fast | Understand before progressing |
| Fear of errors | Errors are learning opportunities |

---

## Pro Tips

1. **Start Small:** Smallest possible working example
2. **One Thing at a Time:** Learn concepts incrementally
3. **Real Projects:** Learn in service of a goal
4. **Struggle a Little:** Don't ask for help too quickly

---

## Next Challenge

Continue to **[Interactive PR Reviews](./05-interactive-pr-reviews.md)** for conversational code review!
