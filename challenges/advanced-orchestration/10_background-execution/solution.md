# Background Execution Solution

## Background Task Examples

### Running Tests in Background
```
"Run the full test suite in the background. Let me know when it completes and if any tests fail."
[Ctrl+B to background]
[Continue other work]
```

### Parallel Analysis
```
Subagent 1: "Analyze security issues in auth module"
Subagent 2: "Check performance of database queries"
Subagent 3: "Review code quality in API handlers"
Main: [Wait for all results, then synthesize]
```

### Build Pipeline
```
Background: "npm run build"
Meanwhile: "Write documentation for new features"
Then: "Check build results and deploy if successful"
```

## Coordination Patterns

### Independent Tasks (Fully Parallel)
```
Task A: Generate API docs
Task B: Update README
Task C: Create changelog
[All can run simultaneously]
```

### Sequential Dependencies
```
Task 1: Install dependencies
Task 2: Run migrations (depends on 1)
Task 3: Start server (depends on 2)
[Must run in order]
```

### Partial Dependencies
```
Task A: Backend tests (independent)
Task B: Frontend tests (independent)
Task C: Integration tests (depends on A + B)
[A and B parallel, then C]
```

## Best Practices

1. **Identify independent tasks** for parallelization
2. **Map dependencies** before starting
3. **Monitor progress** on background tasks
4. **Handle failures** gracefully
5. **Aggregate results** effectively

## Success Indicators

- Reduce overall task completion time
- Manage 3+ parallel workflows
- Handle task dependencies correctly
- Recover from background task failures
