# Walkthrough: Exponential Backoff

**Difficulty:** Medium | **Time:** 15 minutes | **Category:** Workflow Automation

---

## Overview

Long-running jobs need monitoring. Exponential backoff is a smart polling strategy - check frequently at first, then less often as time passes. This saves resources while still catching completion quickly.

## Prerequisites

- [ ] Understanding of async operations
- [ ] Experience with long-running commands
- [ ] Basic scripting knowledge

---

## Step 1: Understanding Exponential Backoff

### The Pattern
```
Time     Check  Wait Until Next
───────────────────────────────
0s       ✓      1s
1s       ✓      2s
3s       ✓      4s
7s       ✓      8s
15s      ✓      16s
31s      ✓      32s
...      ...    (max cap)
```

### Benefits
- Quick detection of fast jobs
- Resource-efficient for slow jobs
- No constant polling overhead

---

## Step 2: Basic Implementation

### Bash Script
```bash
#!/bin/bash
# exponential_poll.sh

wait_time=1
max_wait=60

while true; do
    # Check if job is complete
    if check_job_status; then
        echo "Job complete!"
        exit 0
    fi

    echo "Not ready, waiting ${wait_time}s..."
    sleep $wait_time

    # Exponential increase with cap
    wait_time=$((wait_time * 2))
    if [ $wait_time -gt $max_wait ]; then
        wait_time=$max_wait
    fi
done
```

### JavaScript
```javascript
async function pollWithBackoff(checkFn, maxWait = 60000) {
  let waitTime = 1000;

  while (true) {
    if (await checkFn()) {
      return true;
    }

    await sleep(waitTime);
    waitTime = Math.min(waitTime * 2, maxWait);
  }
}
```

---

## Step 3: Use with Claude

### For CI/CD Monitoring
```
Monitor this GitHub Actions run using exponential backoff:
- Start checking every 5 seconds
- Double wait time each check
- Cap at 60 seconds
- Alert me when complete or failed
```

### For Build Processes
```
I started a long build. Poll for completion:
- Check build status with: npm run build:status
- Use exponential backoff starting at 2 seconds
- Report result when done
```

---

## Step 4: Practical Applications

### Monitoring Deploy
```bash
#!/bin/bash
# monitor_deploy.sh

url="https://myapp.com/health"
wait=5
max=120

while true; do
    if curl -s "$url" | grep -q "healthy"; then
        echo "✅ Deploy complete and healthy!"
        exit 0
    fi

    echo "⏳ Waiting ${wait}s..."
    sleep $wait
    wait=$((wait * 2 > max ? max : wait * 2))
done
```

### Waiting for Database
```bash
#!/bin/bash
# wait_for_db.sh

wait=1
max=30

while ! pg_isready -h localhost -p 5432; do
    echo "Waiting for database... (${wait}s)"
    sleep $wait
    wait=$((wait * 2 > max ? max : wait * 2))
done

echo "Database ready!"
```

---

## Step 5: With Jitter (Advanced)

### Add Randomness
Prevents thundering herd when multiple clients poll:

```javascript
function getBackoffWithJitter(attempt, baseDelay = 1000, maxDelay = 60000) {
  const exponentialDelay = baseDelay * Math.pow(2, attempt);
  const cappedDelay = Math.min(exponentialDelay, maxDelay);

  // Add ±25% jitter
  const jitter = cappedDelay * 0.25 * (Math.random() * 2 - 1);

  return cappedDelay + jitter;
}
```

---

## Step 6: Timeout Handling

### With Maximum Attempts
```bash
#!/bin/bash
max_attempts=10
attempt=0
wait=5

while [ $attempt -lt $max_attempts ]; do
    if check_status; then
        echo "Success!"
        exit 0
    fi

    attempt=$((attempt + 1))
    echo "Attempt $attempt/$max_attempts, waiting ${wait}s..."
    sleep $wait
    wait=$((wait * 2))
done

echo "Timeout after $max_attempts attempts"
exit 1
```

---

## Verification Checklist

- [ ] Understand exponential backoff concept
- [ ] Implemented basic backoff script
- [ ] Used with a real long-running process
- [ ] Added maximum wait cap
- [ ] Added timeout/max attempts

---

## Backoff Patterns

| Pattern | Use Case |
|---------|----------|
| Simple exponential | General polling |
| With cap | Prevent excessive waits |
| With jitter | Multiple concurrent pollers |
| With timeout | Prevent infinite loops |
| With notification | Alert on completion |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| No maximum cap | Always cap wait time |
| Infinite loop | Add max attempts |
| Too aggressive start | Start at reasonable interval |
| Missing timeout | Always have an exit condition |

---

## Pro Tips

1. **Start Small:** Begin with 1-5 second intervals
2. **Cap Appropriately:** 60-120 seconds is usually good max
3. **Add Jitter:** For distributed systems
4. **Log Progress:** Show wait times for debugging

---

## Next Challenge

Continue to **[CI/CD Integration](./04-cicd-integration.md)** to debug GitHub Actions!
