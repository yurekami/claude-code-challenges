# Manual Exponential Backoff - Solution

## Step-by-Step Solution

### 1. Basic Exponential Backoff

**Simple Implementation (Bash):**
```bash
#!/bin/bash
# poll-job.sh - Basic exponential backoff

JOB_ID=$1
INITIAL_INTERVAL=1
MAX_INTERVAL=60
CURRENT_INTERVAL=$INITIAL_INTERVAL

check_job_status() {
    # Replace with actual job status check
    # Returns 0 if complete, 1 if running, 2 if failed
    curl -s "https://api.example.com/jobs/$JOB_ID/status" | grep -q "completed"
    return $?
}

echo "Polling job: $JOB_ID"

while true; do
    echo "Checking status (interval: ${CURRENT_INTERVAL}s)..."

    if check_job_status; then
        echo "Job completed!"
        exit 0
    fi

    echo "Job still running, waiting ${CURRENT_INTERVAL}s..."
    sleep $CURRENT_INTERVAL

    # Double the interval, cap at MAX_INTERVAL
    CURRENT_INTERVAL=$((CURRENT_INTERVAL * 2))
    if [ $CURRENT_INTERVAL -gt $MAX_INTERVAL ]; then
        CURRENT_INTERVAL=$MAX_INTERVAL
    fi
done
```

**Usage:**
```bash
chmod +x poll-job.sh
./poll-job.sh job-12345
```

### 2. Enhanced Version with Jitter

**Why Jitter?**
- Prevents multiple clients from retrying simultaneously
- Reduces server load spikes
- Improves overall system stability

**Implementation:**
```bash
#!/bin/bash
# poll-job-jitter.sh - Exponential backoff with jitter

JOB_ID=$1
INITIAL_INTERVAL=1
MAX_INTERVAL=60
MAX_RETRIES=20
CURRENT_INTERVAL=$INITIAL_INTERVAL
RETRY_COUNT=0

check_job_status() {
    # Simulate job check (replace with actual check)
    STATUS=$(curl -s "https://api.example.com/jobs/$JOB_ID/status")
    echo "$STATUS" | grep -q "completed"
    return $?
}

add_jitter() {
    local interval=$1
    # Add random jitter: 0-25% of interval
    local jitter=$((RANDOM % (interval / 4)))
    echo $((interval + jitter))
}

echo "Polling job: $JOB_ID"
echo "Max retries: $MAX_RETRIES"

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    RETRY_COUNT=$((RETRY_COUNT + 1))
    echo "[Attempt $RETRY_COUNT/$MAX_RETRIES] Checking status..."

    if check_job_status; then
        echo "✓ Job completed successfully!"
        exit 0
    fi

    if [ $? -eq 2 ]; then
        echo "✗ Job failed!"
        exit 1
    fi

    # Calculate next interval with jitter
    WAIT_TIME=$(add_jitter $CURRENT_INTERVAL)
    echo "Job running, waiting ${WAIT_TIME}s..."
    sleep $WAIT_TIME

    # Exponential backoff
    CURRENT_INTERVAL=$((CURRENT_INTERVAL * 2))
    if [ $CURRENT_INTERVAL -gt $MAX_INTERVAL ]; then
        CURRENT_INTERVAL=$MAX_INTERVAL
    fi
done

echo "✗ Max retries exceeded. Job may still be running."
exit 2
```

### 3. PowerShell Version (Windows)

```powershell
# poll-job.ps1 - Exponential backoff in PowerShell

param(
    [string]$JobId,
    [int]$InitialInterval = 1,
    [int]$MaxInterval = 60,
    [int]$MaxRetries = 20
)

function Check-JobStatus {
    param([string]$Id)

    try {
        $response = Invoke-RestMethod -Uri "https://api.example.com/jobs/$Id/status"
        return $response.status -eq "completed"
    }
    catch {
        Write-Host "Error checking job status: $_"
        return $false
    }
}

function Get-Jitter {
    param([int]$Interval)
    $jitter = Get-Random -Minimum 0 -Maximum ($Interval / 4)
    return $Interval + $jitter
}

$currentInterval = $InitialInterval
$retryCount = 0

Write-Host "Polling job: $JobId"
Write-Host "Max retries: $MaxRetries"

while ($retryCount -lt $MaxRetries) {
    $retryCount++
    Write-Host "[Attempt $retryCount/$MaxRetries] Checking status..."

    if (Check-JobStatus -Id $JobId) {
        Write-Host "✓ Job completed successfully!" -ForegroundColor Green
        exit 0
    }

    $waitTime = Get-Jitter -Interval $currentInterval
    Write-Host "Job running, waiting $($waitTime)s..." -ForegroundColor Yellow
    Start-Sleep -Seconds $waitTime

    # Exponential backoff
    $currentInterval = $currentInterval * 2
    if ($currentInterval -gt $MaxInterval) {
        $currentInterval = $MaxInterval
    }
}

Write-Host "✗ Max retries exceeded." -ForegroundColor Red
exit 2
```

**Usage:**
```powershell
.\poll-job.ps1 -JobId "job-12345"
```

### 4. Python Version (More Features)

```python
#!/usr/bin/env python3
# poll_job.py - Feature-rich exponential backoff

import time
import random
import sys
import requests
from datetime import datetime

class ExponentialBackoff:
    def __init__(self, initial=1, maximum=60, max_retries=20):
        self.initial = initial
        self.maximum = maximum
        self.max_retries = max_retries
        self.current = initial
        self.retries = 0

    def wait(self):
        """Wait with exponential backoff and jitter"""
        if self.retries >= self.max_retries:
            raise Exception(f"Max retries ({self.max_retries}) exceeded")

        # Add jitter (0-25% of interval)
        jitter = random.uniform(0, self.current * 0.25)
        wait_time = self.current + jitter

        print(f"⏳ Waiting {wait_time:.1f}s... (retry {self.retries + 1}/{self.max_retries})")
        time.sleep(wait_time)

        # Exponential backoff
        self.current = min(self.current * 2, self.maximum)
        self.retries += 1

    def reset(self):
        """Reset backoff to initial state"""
        self.current = self.initial
        self.retries = 0

def check_job_status(job_id):
    """Check job status via API"""
    try:
        response = requests.get(f"https://api.example.com/jobs/{job_id}/status")
        response.raise_for_status()
        data = response.json()
        return data.get("status")
    except requests.RequestException as e:
        print(f"⚠️  Error checking status: {e}")
        return None

def poll_job(job_id, initial=1, maximum=60, max_retries=20):
    """Poll job with exponential backoff"""
    backoff = ExponentialBackoff(initial, maximum, max_retries)
    start_time = datetime.now()

    print(f"🔍 Polling job: {job_id}")
    print(f"📊 Config: initial={initial}s, max={maximum}s, retries={max_retries}")
    print()

    while True:
        status = check_job_status(job_id)

        if status == "completed":
            elapsed = (datetime.now() - start_time).total_seconds()
            print(f"✅ Job completed! (took {elapsed:.1f}s, {backoff.retries} checks)")
            return 0
        elif status == "failed":
            print("❌ Job failed!")
            return 1
        elif status == "running":
            print(f"🔄 Job running...")
            try:
                backoff.wait()
            except Exception as e:
                print(f"❌ {e}")
                return 2
        else:
            print(f"⚠️  Unknown status: {status}")
            try:
                backoff.wait()
            except Exception as e:
                print(f"❌ {e}")
                return 2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: poll_job.py <job-id>")
        sys.exit(1)

    job_id = sys.argv[1]
    sys.exit(poll_job(job_id))
```

**Usage:**
```bash
python poll_job.py job-12345
```

### 5. Real-World Examples

**Example 1: CI/CD Pipeline Polling**
```bash
#!/bin/bash
# poll-github-actions.sh

REPO="owner/repo"
RUN_ID=$1
GITHUB_TOKEN=$2

check_workflow_status() {
    local status=$(curl -s \
        -H "Authorization: token $GITHUB_TOKEN" \
        "https://api.github.com/repos/$REPO/actions/runs/$RUN_ID" \
        | jq -r '.status')

    echo "$status"
}

INTERVAL=2
MAX_INTERVAL=60
MAX_TIME=3600  # 1 hour timeout
ELAPSED=0

while [ $ELAPSED -lt $MAX_TIME ]; do
    STATUS=$(check_workflow_status)

    case "$STATUS" in
        "completed")
            echo "✓ Workflow completed!"
            exit 0
            ;;
        "in_progress"|"queued")
            echo "⏳ Workflow status: $STATUS (waited ${ELAPSED}s)"
            sleep $INTERVAL
            ELAPSED=$((ELAPSED + INTERVAL))
            INTERVAL=$((INTERVAL * 2))
            [ $INTERVAL -gt $MAX_INTERVAL ] && INTERVAL=$MAX_INTERVAL
            ;;
        *)
            echo "✗ Unexpected status: $STATUS"
            exit 1
            ;;
    esac
done

echo "✗ Timeout after ${MAX_TIME}s"
exit 2
```

**Example 2: Database Migration Polling**
```bash
#!/bin/bash
# poll-migration.sh

DB_HOST="localhost"
DB_NAME="myapp"
MIGRATION_ID=$1

check_migration() {
    psql -h "$DB_HOST" -d "$DB_NAME" -t -c \
        "SELECT status FROM migrations WHERE id='$MIGRATION_ID';" \
        | xargs
}

echo "Checking migration: $MIGRATION_ID"

INTERVAL=1
while true; do
    STATUS=$(check_migration)

    case "$STATUS" in
        "completed")
            echo "✓ Migration completed!"
            exit 0
            ;;
        "running")
            echo "⏳ Migration running... (checking again in ${INTERVAL}s)"
            sleep $INTERVAL
            INTERVAL=$((INTERVAL * 2))
            [ $INTERVAL -gt 120 ] && INTERVAL=120
            ;;
        "failed")
            echo "✗ Migration failed!"
            exit 1
            ;;
        *)
            echo "⚠️  Unknown status: $STATUS"
            sleep $INTERVAL
            ;;
    esac
done
```

**Example 3: AWS Job Polling**
```bash
#!/bin/bash
# poll-aws-job.sh

JOB_ID=$1
AWS_PROFILE="default"

check_job() {
    aws batch describe-jobs \
        --jobs "$JOB_ID" \
        --profile "$AWS_PROFILE" \
        --query 'jobs[0].status' \
        --output text
}

INTERVAL=5
MAX_INTERVAL=300

while true; do
    STATUS=$(check_job)

    case "$STATUS" in
        "SUCCEEDED")
            echo "✓ Job succeeded!"
            exit 0
            ;;
        "FAILED")
            echo "✗ Job failed!"
            exit 1
            ;;
        "RUNNING"|"PENDING"|"RUNNABLE")
            echo "⏳ Job status: $STATUS (next check in ${INTERVAL}s)"
            sleep $INTERVAL
            INTERVAL=$((INTERVAL * 2))
            [ $INTERVAL -gt $MAX_INTERVAL ] && INTERVAL=$MAX_INTERVAL
            ;;
        *)
            echo "⚠️  Unknown status: $STATUS"
            sleep $INTERVAL
            ;;
    esac
done
```

### 6. Comparison: Linear vs Exponential

**Linear Polling (every 5s for 10 minutes):**
```
Checks: 120
Total wait time: 600s
Server requests: 120
```

**Exponential Backoff (1s → 60s max):**
```
Checks: ~15
Total wait time: 600s
Server requests: 15
Reduction: 87.5%
```

**Simulation Script:**
```bash
#!/bin/bash
# compare-strategies.sh

JOB_DURATION=300  # 5 minutes

echo "Simulating linear polling (every 5s)..."
LINEAR_CHECKS=$((JOB_DURATION / 5))
echo "Total checks: $LINEAR_CHECKS"

echo ""
echo "Simulating exponential backoff (1s → 60s)..."
INTERVAL=1
ELAPSED=0
EXPO_CHECKS=0

while [ $ELAPSED -lt $JOB_DURATION ]; do
    EXPO_CHECKS=$((EXPO_CHECKS + 1))
    ELAPSED=$((ELAPSED + INTERVAL))
    INTERVAL=$((INTERVAL * 2))
    [ $INTERVAL -gt 60 ] && INTERVAL=60
done

echo "Total checks: $EXPO_CHECKS"
echo ""
echo "Reduction: $(((LINEAR_CHECKS - EXPO_CHECKS) * 100 / LINEAR_CHECKS))%"
```

## Common Mistakes to Avoid

### 1. **No Maximum Interval**
❌ Interval keeps doubling forever
```bash
# After 10 iterations: 1024s wait (17 minutes!)
```

✅ Cap at reasonable maximum
```bash
[ $INTERVAL -gt $MAX_INTERVAL ] && INTERVAL=$MAX_INTERVAL
```

### 2. **No Jitter**
❌ All clients retry at same time
```bash
# 100 clients all retry at t=1, t=2, t=4, t=8...
# Server gets hammered
```

✅ Add randomness
```bash
JITTER=$((RANDOM % (INTERVAL / 4)))
sleep $((INTERVAL + JITTER))
```

### 3. **No Timeout**
❌ Script runs forever
```bash
while true; do
    # Never exits if job hangs
done
```

✅ Add retry limit or time limit
```bash
MAX_RETRIES=20
RETRY_COUNT=0
while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    # ...
done
```

### 4. **Ignoring Error States**
❌ Only checks for success
```bash
if job_completed; then
    exit 0
fi
# What if job failed?
```

✅ Handle all states
```bash
case "$status" in
    "completed") exit 0 ;;
    "failed") exit 1 ;;
    "running") continue ;;
    *) echo "Unknown: $status" ;;
esac
```

### 5. **Starting Too Slow**
❌ Initial interval too long
```bash
INITIAL_INTERVAL=30  # Misses fast jobs
```

✅ Start fast, slow down gradually
```bash
INITIAL_INTERVAL=1  # Catches fast completions
```

## Pro Tips

### 1. **Adaptive Backoff**
```python
# Adjust backoff based on job type
if job_type == "fast":
    backoff = ExponentialBackoff(initial=0.5, maximum=10)
elif job_type == "slow":
    backoff = ExponentialBackoff(initial=5, maximum=300)
```

### 2. **Progress Indicators**
```bash
# Show progress bar
echo -n "Polling: "
for i in {1..5}; do
    echo -n "."
    sleep $((INTERVAL / 5))
done
echo " done"
```

### 3. **Logging**
```bash
# Log all checks for debugging
LOG_FILE="poll_${JOB_ID}_$(date +%s).log"
echo "[$(date)] Check $RETRY_COUNT: $STATUS" >> "$LOG_FILE"
```

### 4. **Notifications**
```bash
# Notify on completion
if check_job_status; then
    notify-send "Job Complete" "$JOB_ID finished"
    # or
    curl -X POST "$SLACK_WEBHOOK" -d "{\"text\":\"Job $JOB_ID done\"}"
fi
```

## Verification Checklist

- [ ] Implemented exponential backoff with interval doubling
- [ ] Added maximum interval cap
- [ ] Included jitter to prevent synchronization
- [ ] Added timeout/retry limits
- [ ] Handled all job states (success, failure, running)
- [ ] Tested with simulated or real job
- [ ] Compared efficiency vs linear polling
- [ ] Added logging or progress indicators

## Time Savings

**Scenario:** Monitoring 10 CI/CD pipelines per day (avg 5 min each)

**Linear polling (every 5s):**
- 120 checks × 10 jobs = 1,200 API calls/day
- Server load: High
- API rate limit risk: High

**Exponential backoff:**
- 15 checks × 10 jobs = 150 API calls/day
- Server load: Low
- API rate limit risk: Minimal
- **Reduction: 87.5% fewer API calls**

## Further Reading

- AWS SDK retry strategies
- Google Cloud exponential backoff guidelines
- HTTP 429 (Too Many Requests) handling
- Circuit breaker pattern (related concept)
