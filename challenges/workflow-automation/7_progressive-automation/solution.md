# Progressive Automation - Solution

## Task Analysis Framework

### Step 1: Identify Automation Candidates

**Criteria for Good Automation Targets:**
1. **Frequency**: Done at least weekly
2. **Consistency**: Same steps every time
3. **Time-consuming**: Takes > 5 minutes
4. **Error-prone**: Easy to make mistakes
5. **Boring**: Mindless repetition

**Scoring System:**
```
Score = (Frequency × Time) - (Complexity × 10)

Where:
- Frequency: Times per week (e.g., 5 for daily)
- Time: Minutes per execution
- Complexity: 1-10 (how hard to automate)

Automate if Score > 50
```

### Example Analysis

| Task | Freq/Week | Time (min) | Complexity | Score | Priority |
|------|-----------|------------|------------|-------|----------|
| Database backup | 5 | 10 | 3 | 20 | High |
| Update dependencies | 2 | 15 | 5 | -20 | Low |
| Run tests locally | 10 | 5 | 2 | 30 | Medium |
| Clear log files | 5 | 3 | 1 | 5 | Medium |
| Deploy to staging | 3 | 20 | 7 | -10 | Low |
| Format code | 20 | 2 | 2 | 20 | High |

## Progressive Automation Examples

### Example 1: Database Backup

**V1: Basic Script (10 minutes with Claude Code)**

**Prompt to Claude Code:**
```
Create a simple bash script to backup a PostgreSQL database to a file with timestamp.
```

**Generated Script:**
```bash
#!/bin/bash
# backup-db.sh - V1

DB_NAME="myapp_production"
BACKUP_DIR="/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql"

pg_dump $DB_NAME > $BACKUP_FILE

echo "Backup created: $BACKUP_FILE"
```

**Usage:**
```bash
chmod +x backup-db.sh
./backup-db.sh
```

**Time Saved:** 5 minutes per backup
**Time to Create:** 10 minutes
**ROI:** Positive after 2 backups

---

**V2: Add Error Handling (10 minutes)**

**Prompt to Claude Code:**
```
Enhance the backup script with:
- Error handling
- Check if backup directory exists
- Verify backup was created
```

**Enhanced Script:**
```bash
#!/bin/bash
# backup-db.sh - V2

set -e  # Exit on error

DB_NAME="myapp_production"
BACKUP_DIR="/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql"

# Check if backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Error: Backup directory $BACKUP_DIR does not exist"
    exit 1
fi

# Check if database exists
if ! psql -lqt | cut -d \| -f 1 | grep -qw $DB_NAME; then
    echo "Error: Database $DB_NAME does not exist"
    exit 1
fi

# Perform backup
echo "Starting backup of $DB_NAME..."
if pg_dump $DB_NAME > $BACKUP_FILE; then
    echo "✓ Backup created: $BACKUP_FILE"
    echo "  Size: $(du -h $BACKUP_FILE | cut -f1)"
else
    echo "✗ Backup failed!"
    exit 1
fi
```

---

**V3: Add Configuration & Retention (15 minutes)**

**Prompt to Claude Code:**
```
Add configuration file support and automatic cleanup of old backups (keep last 7 days).
```

**Config File (.backup.conf):**
```bash
# .backup.conf
DB_NAME="myapp_production"
DB_USER="postgres"
BACKUP_DIR="/backups"
RETENTION_DAYS=7
COMPRESSION=true
```

**Enhanced Script:**
```bash
#!/bin/bash
# backup-db.sh - V3

set -e

# Load configuration
CONFIG_FILE=".backup.conf"
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
else
    echo "Error: Config file not found"
    exit 1
fi

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Perform backup
echo "Starting backup of $DB_NAME..."
pg_dump -U $DB_USER $DB_NAME > $BACKUP_FILE

# Compress if enabled
if [ "$COMPRESSION" = true ]; then
    echo "Compressing backup..."
    gzip $BACKUP_FILE
    BACKUP_FILE="${BACKUP_FILE}.gz"
fi

echo "✓ Backup created: $BACKUP_FILE"
echo "  Size: $(du -h $BACKUP_FILE | cut -f1)"

# Clean up old backups
echo "Cleaning up old backups (keeping last $RETENTION_DAYS days)..."
find $BACKUP_DIR -name "${DB_NAME}_*.sql*" -mtime +$RETENTION_DAYS -delete
echo "✓ Cleanup complete"

# List remaining backups
echo ""
echo "Available backups:"
ls -lh $BACKUP_DIR/${DB_NAME}_*.sql* | awk '{print $9, $5}'
```

---

**V4: Add Logging & Notifications (20 minutes)**

**Prompt to Claude Code:**
```
Add logging to file and Slack notifications for backup status.
```

**Final Script:**
```bash
#!/bin/bash
# backup-db.sh - V4 (Production Ready)

set -e

# Load configuration
CONFIG_FILE=".backup.conf"
source "$CONFIG_FILE"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql"
LOG_FILE="$BACKUP_DIR/backup.log"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Slack notification function
notify_slack() {
    local message=$1
    local status=$2  # success or failure

    if [ -n "$SLACK_WEBHOOK_URL" ]; then
        local color="good"
        [ "$status" = "failure" ] && color="danger"

        curl -X POST "$SLACK_WEBHOOK_URL" \
            -H 'Content-Type: application/json' \
            -d "{\"text\":\"$message\",\"color\":\"$color\"}" \
            2>&1 >> "$LOG_FILE"
    fi
}

# Main backup process
log "Starting backup of $DB_NAME..."

mkdir -p "$BACKUP_DIR"

# Perform backup
if pg_dump -U $DB_USER $DB_NAME > $BACKUP_FILE; then
    # Compress
    if [ "$COMPRESSION" = true ]; then
        gzip $BACKUP_FILE
        BACKUP_FILE="${BACKUP_FILE}.gz"
    fi

    SIZE=$(du -h $BACKUP_FILE | cut -f1)
    log "✓ Backup created: $BACKUP_FILE (Size: $SIZE)"

    # Clean up old backups
    log "Cleaning up old backups..."
    DELETED=$(find $BACKUP_DIR -name "${DB_NAME}_*.sql*" -mtime +$RETENTION_DAYS -delete -print | wc -l)
    log "✓ Deleted $DELETED old backups"

    # Count remaining backups
    COUNT=$(ls $BACKUP_DIR/${DB_NAME}_*.sql* 2>/dev/null | wc -l)
    log "✓ Total backups: $COUNT"

    notify_slack "Database backup successful: $DB_NAME ($SIZE)" "success"
else
    log "✗ Backup failed!"
    notify_slack "Database backup FAILED: $DB_NAME" "failure"
    exit 1
fi
```

**Evolution Summary:**
- V1: 15 lines, basic backup
- V2: 30 lines, + error handling
- V3: 50 lines, + config & retention
- V4: 80 lines, + logging & notifications

**Total Time Invested:** 55 minutes
**Time Saved per Backup:** 5 minutes → 10 minutes (including verification)
**Backups per Week:** 5
**ROI:** Break-even after 2 weeks

### Example 2: Code Formatting Automation

**V1: Simple Pre-commit Hook (5 minutes)**

**Prompt to Claude Code:**
```
Create a git pre-commit hook that runs Prettier on staged files.
```

**Generated: `.git/hooks/pre-commit`**
```bash
#!/bin/bash
# V1: Format staged files

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|ts|jsx|tsx)$')

if [ -n "$FILES" ]; then
    echo "Running Prettier on staged files..."
    npx prettier --write $FILES
    git add $FILES
fi
```

---

**V2: Add Linting (10 minutes)**

```bash
#!/bin/bash
# V2: Format + Lint

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|ts|jsx|tsx)$')

if [ -n "$FILES" ]; then
    echo "Running Prettier..."
    npx prettier --write $FILES

    echo "Running ESLint..."
    npx eslint $FILES --fix

    git add $FILES
fi
```

---

**V3: Add Bypass Option (5 minutes)**

```bash
#!/bin/bash
# V3: Add --no-verify bypass option

# Allow bypass with: git commit --no-verify
if [ -n "$SKIP_HOOKS" ]; then
    echo "Skipping pre-commit hooks (SKIP_HOOKS set)"
    exit 0
fi

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|ts|jsx|tsx)$')

if [ -n "$FILES" ]; then
    echo "Running Prettier..."
    npx prettier --write $FILES || exit 1

    echo "Running ESLint..."
    npx eslint $FILES --fix || exit 1

    git add $FILES
fi

echo "✓ Pre-commit checks passed"
```

### Example 3: Dependency Update Automation

**V1: Manual Update Script (10 minutes)**

**Prompt to Claude Code:**
```
Create a script to check for outdated npm packages and update them interactively.
```

```bash
#!/bin/bash
# update-deps.sh - V1

echo "Checking for outdated packages..."
npm outdated

echo ""
read -p "Update all packages? (y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    npm update
    echo "✓ Packages updated"
else
    echo "Update cancelled"
fi
```

---

**V2: Automated with Testing (20 minutes)**

```bash
#!/bin/bash
# update-deps.sh - V2

set -e

echo "Checking for outdated packages..."
OUTDATED=$(npm outdated --json)

if [ "$OUTDATED" = "{}" ]; then
    echo "✓ All packages up to date"
    exit 0
fi

echo "$OUTDATED" | jq -r 'to_entries[] | "\(.key): \(.value.current) → \(.value.latest)"'

echo ""
read -p "Update packages? (y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Creating backup branch..."
    BRANCH_NAME="deps-update-$(date +%Y%m%d-%H%M%S)"
    git checkout -b $BRANCH_NAME

    echo "Updating packages..."
    npm update

    echo "Running tests..."
    if npm test; then
        echo "✓ Tests passed"
        git add package.json package-lock.json
        git commit -m "chore: update dependencies"
        echo ""
        echo "Changes committed to branch: $BRANCH_NAME"
        echo "Review and merge when ready"
    else
        echo "✗ Tests failed, reverting..."
        git checkout main
        git branch -D $BRANCH_NAME
        exit 1
    fi
else
    echo "Update cancelled"
fi
```

---

**V3: Fully Automated with PR Creation (30 minutes)**

```bash
#!/bin/bash
# update-deps.sh - V3 (Automated weekly via cron)

set -e

BRANCH_NAME="deps-update-$(date +%Y%m%d)"
REPO="owner/repo"

echo "Checking for outdated packages..."
OUTDATED=$(npm outdated --json)

if [ "$OUTDATED" = "{}" ]; then
    echo "✓ All packages up to date"
    exit 0
fi

# Create update branch
git checkout main
git pull
git checkout -b $BRANCH_NAME

# Update packages
npm update

# Run tests
if ! npm test; then
    echo "✗ Tests failed, aborting"
    git checkout main
    git branch -D $BRANCH_NAME
    exit 1
fi

# Commit changes
git add package.json package-lock.json
git commit -m "chore: update dependencies"

# Push and create PR
git push -u origin $BRANCH_NAME

# Create PR using GitHub CLI
gh pr create \
    --title "chore: update dependencies" \
    --body "Automated dependency update. Please review changes and test before merging." \
    --label "dependencies" \
    --label "automated"

echo "✓ PR created successfully"
```

**Cron Schedule:**
```bash
# Run every Monday at 9am
0 9 * * 1 cd /path/to/project && ./update-deps.sh >> /var/log/deps-update.log 2>&1
```

## Automation Library

### 1. Log Rotation Script

```bash
#!/bin/bash
# rotate-logs.sh

LOG_DIR="/var/log/myapp"
MAX_SIZE_MB=100
ARCHIVE_DIR="$LOG_DIR/archive"

mkdir -p "$ARCHIVE_DIR"

find "$LOG_DIR" -name "*.log" -size +${MAX_SIZE_MB}M | while read LOG_FILE; do
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    BASENAME=$(basename "$LOG_FILE")
    ARCHIVE_FILE="$ARCHIVE_DIR/${BASENAME%.log}_${TIMESTAMP}.log.gz"

    echo "Rotating $LOG_FILE..."
    gzip -c "$LOG_FILE" > "$ARCHIVE_FILE"
    > "$LOG_FILE"  # Truncate original
    echo "✓ Archived to $ARCHIVE_FILE"
done

# Delete archives older than 30 days
find "$ARCHIVE_DIR" -name "*.log.gz" -mtime +30 -delete
```

### 2. Environment Setup Script

```bash
#!/bin/bash
# setup-dev-env.sh

echo "Setting up development environment..."

# Install dependencies
echo "1. Installing dependencies..."
npm ci

# Setup database
echo "2. Setting up database..."
if ! psql -lqt | cut -d \| -f 1 | grep -qw myapp_dev; then
    createdb myapp_dev
    psql myapp_dev < schema.sql
    echo "✓ Database created"
else
    echo "✓ Database already exists"
fi

# Copy env file
echo "3. Setting up environment variables..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file (please update values)"
else
    echo "✓ .env already exists"
fi

# Generate secrets
echo "4. Generating secrets..."
if ! grep -q "JWT_SECRET=" .env || grep -q "JWT_SECRET=changeme" .env; then
    JWT_SECRET=$(openssl rand -base64 32)
    sed -i "s/JWT_SECRET=.*/JWT_SECRET=$JWT_SECRET/" .env
    echo "✓ JWT secret generated"
fi

echo ""
echo "✓ Development environment ready!"
echo "Run 'npm start' to start the server"
```

### 3. Test Reporter Script

```bash
#!/bin/bash
# test-report.sh

REPORT_DIR="test-reports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
REPORT_FILE="$REPORT_DIR/test-report-$TIMESTAMP.html"

mkdir -p "$REPORT_DIR"

echo "Running tests with coverage..."
npm test -- --coverage --coverageReporters=html

# Generate HTML report
echo "Generating report..."
cp -r coverage/lcov-report/* "$REPORT_DIR/"

# Calculate summary
COVERAGE=$(cat coverage/lcov-report/index.html | grep -oP '\d+\.\d+(?=%</span>)' | head -1)

echo ""
echo "✓ Test report generated: $REPORT_FILE"
echo "  Coverage: $COVERAGE%"

# Open in browser
if [ "$OPEN_BROWSER" = true ]; then
    open "$REPORT_FILE"
fi

# Send to Slack
if [ -n "$SLACK_WEBHOOK_URL" ]; then
    curl -X POST "$SLACK_WEBHOOK_URL" \
        -H 'Content-Type: application/json' \
        -d "{\"text\":\"Test coverage: $COVERAGE%\",\"color\":\"good\"}"
fi
```

### 4. API Health Check

```bash
#!/bin/bash
# health-check.sh

ENDPOINTS=(
    "https://api.example.com/health"
    "https://api.example.com/db/health"
    "https://api.example.com/cache/health"
)

FAILURES=0

for ENDPOINT in "${ENDPOINTS[@]}"; do
    echo -n "Checking $ENDPOINT... "

    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$ENDPOINT")

    if [ "$HTTP_CODE" = "200" ]; then
        echo "✓ OK"
    else
        echo "✗ FAILED (HTTP $HTTP_CODE)"
        FAILURES=$((FAILURES + 1))
    fi
done

echo ""
if [ $FAILURES -eq 0 ]; then
    echo "✓ All health checks passed"
    exit 0
else
    echo "✗ $FAILURES health check(s) failed"
    exit 1
fi
```

### 5. Deployment Smoke Test

```bash
#!/bin/bash
# smoke-test.sh

ENVIRONMENT=$1
BASE_URL=""

case "$ENVIRONMENT" in
    staging)
        BASE_URL="https://staging.example.com"
        ;;
    production)
        BASE_URL="https://example.com"
        ;;
    *)
        echo "Usage: $0 {staging|production}"
        exit 1
        ;;
esac

echo "Running smoke tests on $ENVIRONMENT..."

# Test 1: Homepage loads
echo -n "Test 1: Homepage... "
if curl -sf "$BASE_URL" > /dev/null; then
    echo "✓"
else
    echo "✗"
    exit 1
fi

# Test 2: API responds
echo -n "Test 2: API... "
if curl -sf "$BASE_URL/api/health" | grep -q "ok"; then
    echo "✓"
else
    echo "✗"
    exit 1
fi

# Test 3: Database connectivity
echo -n "Test 3: Database... "
if curl -sf "$BASE_URL/api/db/health" | grep -q "connected"; then
    echo "✓"
else
    echo "✗"
    exit 1
fi

echo ""
echo "✓ All smoke tests passed on $ENVIRONMENT"
```

## When NOT to Automate

### Don't Automate If:

1. **One-Time Tasks**
   - Project setup (done once)
   - One-off data migration
   - Temporary fixes

2. **Rarely Done**
   - Annual reports
   - Infrequent audits
   - Rare scenarios

3. **Highly Variable**
   - Creative work
   - Exploratory debugging
   - Custom client requests

4. **Learning Opportunity**
   - New technology exploration
   - Skill development
   - Understanding system behavior

5. **Too Complex**
   - Automation takes 10x longer than manual
   - Maintenance cost > benefit
   - Brittle/fragile automation

### Decision Formula

```
Automate if:
(Time Saved per Execution × Frequency per Year) > (Time to Build + Annual Maintenance)

Example:
- Task: 10 min
- Frequency: Daily (365/year)
- Time Saved: 3650 min/year (60 hours)
- Time to Build: 2 hours
- Maintenance: 30 min/year

60 hours > 2.5 hours → AUTOMATE!
```

## Common Mistakes to Avoid

### 1. **Over-Engineering V1**
❌ Adding every feature to first version
✅ Start minimal, iterate based on usage

### 2. **Not Tracking ROI**
❌ Automating without measuring impact
✅ Track time saved vs time invested

### 3. **Automating Before Standardizing**
❌ Automating inconsistent process
✅ Standardize first, then automate

### 4. **No Documentation**
❌ Scripts without usage instructions
✅ Document what it does and how to run it

### 5. **Ignoring Edge Cases in Production**
❌ V1 script with no error handling in production
✅ Add error handling before deploying to production

## Verification Checklist

- [ ] Identified 5+ recurring tasks
- [ ] Calculated ROI for each task
- [ ] Built V1 automation in < 15 minutes
- [ ] Used automation for 1+ week
- [ ] Tracked actual time savings
- [ ] Iterated based on real pain points
- [ ] Created reusable automation library
- [ ] Documented all scripts
- [ ] Shared with team
- [ ] Can explain when NOT to automate

## Progressive Automation Workflow

```
Week 1: Identify & Build
├─ Analyze recurring tasks
├─ Build V1 (simple script)
└─ Use daily, track pain points

Week 2: Iterate
├─ Add error handling
├─ Add logging
└─ Measure time savings

Week 3: Polish
├─ Add configuration
├─ Add notifications
└─ Document usage

Week 4: Share
├─ Share with team
├─ Gather feedback
└─ Standardize approach
```

## Time Savings Examples

### Case Study 1: Database Backups

**Manual Process:**
- SSH to server: 30s
- Run pg_dump: 2 min
- Compress: 1 min
- Download to local: 2 min
- Verify: 1 min
- **Total: 6.5 min per backup**

**Automated (V4):**
- Runs automatically: 0s human time
- Sends notification: 0s human time
- **Total: 0 min per backup**

**ROI:**
- Time to build: 55 min
- Backups per week: 5
- Time saved per week: 32.5 min
- **Break-even: 2 weeks**
- **Annual savings: 28 hours**

### Case Study 2: Code Formatting

**Manual:**
- Remember to format: 10s (often forgotten)
- Run Prettier: 5s
- Run ESLint: 10s
- Fix lint errors: 2 min
- **Total: 2.5 min per commit**

**Automated Pre-commit Hook:**
- Automatic: 0s human time
- Never forgotten: 0s debugging time
- **Total: 0 min per commit**

**ROI:**
- Time to build: 20 min
- Commits per day: 10
- Time saved per day: 25 min
- **Break-even: 1 day**
- **Annual savings: 100+ hours**

## Further Reading

- XKCD: "Is It Worth the Time?" (classic automation chart)
- "The Pragmatic Programmer" - Automation chapter
- Bash scripting best practices
- CI/CD automation patterns
- Infrastructure as Code (Terraform, Ansible)
