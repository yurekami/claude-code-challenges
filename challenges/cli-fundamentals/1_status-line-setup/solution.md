# Solution: Status Line Setup

## Step-by-Step Solution

### Step 1: Launch Claude Code in a Git Repository

```bash
cd your-project-directory
claude
```

The status line will automatically appear at the bottom of your terminal.

### Step 2: Understanding the Status Line Components

The status line typically displays information in this format:

```
[Model: Sonnet 4.5] [Branch: main] [Tokens: 5,234/200,000 (2.6%)]
```

**Components:**
1. **Model**: Current AI model (Sonnet 4.5, Haiku 4.5, or Opus 4.5)
2. **Branch**: Active Git branch
3. **Tokens**: Used tokens / Total tokens (percentage)

### Step 3: Model Selection

To switch models during a session:

1. Look for the model selector in your Claude Code interface
2. Common model choices:
   - **Haiku 4.5**: Fast, cost-effective, 90% of Sonnet capability
   - **Sonnet 4.5**: Best coding model, balanced performance
   - **Opus 4.5**: Deepest reasoning, highest cost

### Step 4: Monitoring Token Usage

**Token Usage Guidelines:**
- **0-60%**: Safe zone for any task
- **60-80%**: Start planning to wrap up or start new conversation
- **80%+**: Avoid complex refactoring or multi-file operations
- **90%+**: Consider starting a new conversation

**When to start fresh:**
- Approaching 80% on complex tasks
- Context has drifted from original goal
- Too many failed attempts or corrections
- Switching to a completely different task

### Step 5: Git Branch Awareness

The status line automatically reflects your current Git branch:

```bash
# Create and switch to a new branch
git checkout -b feature/status-line-practice

# Status line will update to show: [Branch: feature/status-line-practice]
```

### Step 6: Practical Example

```bash
# 1. Navigate to a project
cd ~/projects/my-app

# 2. Create a feature branch
git checkout -b feature/add-logging

# 3. Launch Claude Code
claude

# 4. Observe status line shows:
#    Model: Sonnet 4.5
#    Branch: feature/add-logging
#    Tokens: 0/200,000 (0%)

# 5. Start a conversation
# "Help me add structured logging to this application"

# 6. Watch token usage increase as conversation progresses
```

## Common Mistakes to Avoid

### Mistake 1: Ignoring Token Usage
**Problem**: Continuing complex work when at 90% token usage
**Solution**: Start a new conversation when reaching 80% for complex tasks

### Mistake 2: Wrong Model for the Task
**Problem**: Using Opus for simple code generation (expensive)
**Solution**: Use Haiku for lightweight tasks, Sonnet for most work, Opus only for complex reasoning

### Mistake 3: Not Checking Git Branch
**Problem**: Making changes on the wrong branch
**Solution**: Always verify the branch name in the status line before starting work

### Mistake 4: Context Window Mismanagement
**Problem**: Starting a large refactor at 70% token usage
**Solution**: Plan ahead - start big tasks with fresh context

## Best Practices

1. **Model Selection Strategy**:
   - Default to Sonnet 4.5 for most coding tasks
   - Use Haiku 4.5 for simple edits, quick questions, or frequent agent invocations
   - Reserve Opus 4.5 for architectural decisions or complex debugging

2. **Token Budget Management**:
   - Check token usage before starting multi-step tasks
   - Leave 20% buffer for complex operations
   - Start new conversations when switching focus areas

3. **Git Workflow**:
   - Always verify branch before coding
   - Use feature branches (not main) for development
   - Status line prevents accidental commits to main

4. **Session Planning**:
   - Estimate token needs for your task
   - Group related work in single conversations
   - Split unrelated work across conversations

## Advanced Tips

### Tip 1: Model Switching Strategy
Switch models mid-conversation when:
- Started with Haiku but need deeper reasoning → switch to Sonnet
- Complex architecture question → switch to Opus
- Back to simple edits → switch back to Haiku

### Tip 2: Token Usage Patterns
- Simple questions: ~500-1,000 tokens
- Code review: ~2,000-5,000 tokens
- Feature implementation: ~10,000-30,000 tokens
- Large refactoring: ~30,000-100,000+ tokens

### Tip 3: Status Line as Decision Tool
Use the status line to decide:
- "Can I start this feature implementation?" (check token budget)
- "Am I on the right branch?" (verify before coding)
- "Should I switch models?" (task complexity vs model capability)

## Verification

To verify you've mastered status line setup:

```bash
# 1. Create a test branch
git checkout -b test/status-line-mastery

# 2. Launch Claude Code
claude

# 3. Verify you can answer:
# - What model am I using?
# - What branch am I on?
# - How many tokens have I used?
# - What percentage of context is remaining?

# 4. Have a short conversation (ask Claude a question)

# 5. Observe token usage increase

# 6. Switch models and note the change in status line
```

## Success Indicators

You've mastered status line setup when you:
- Glance at the status line before starting any task
- Choose the appropriate model for your work
- Never accidentally work on the wrong Git branch
- Proactively manage token usage
- Know when to start fresh conversations
