# Walkthrough: Universal Interface

**Difficulty:** Hard | **Time:** 35 minutes | **Category:** Advanced Orchestration

---

## Overview

Claude Code can serve as a universal interface to any system - databases, APIs, cloud services, CLI tools, and more. Instead of remembering dozens of different syntaxes, you interact with everything through natural language.

## Prerequisites

- [ ] Multiple tools/systems to integrate
- [ ] API keys or credentials configured
- [ ] Understanding of the systems you want to interface with

---

## Step 1: The Universal Interface Concept

### Traditional Approach
```
Query database → Learn SQL syntax
Deploy to AWS → Learn AWS CLI
Search logs → Learn grep/awk
Manage K8s → Learn kubectl
```

### Universal Interface Approach
```
┌─────────────────────────────────────┐
│          Natural Language           │
│     "Show me failing pods"          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│          Claude Code                │
│    (Translates to appropriate       │
│     tool and syntax)                │
└──────────────┬──────────────────────┘
               │
     ┌─────────┼─────────┐
     ▼         ▼         ▼
  kubectl    docker    aws cli
```

---

## Step 2: Database Interface

### Natural Language Queries
```
"Show me users who signed up last week"
→ Claude generates: SELECT * FROM users WHERE created_at > NOW() - INTERVAL '7 days'

"What's our most popular product?"
→ Claude generates: SELECT product_id, COUNT(*) FROM orders GROUP BY product_id ORDER BY COUNT(*) DESC LIMIT 1

"Update all inactive users to archived status"
→ Claude generates: UPDATE users SET status = 'archived' WHERE last_login < NOW() - INTERVAL '90 days'
```

### Setup Pattern
```
I'm working with a PostgreSQL database. The schema is:
- users (id, email, created_at, last_login, status)
- orders (id, user_id, product_id, amount, created_at)
- products (id, name, price, category)

When I ask questions about data, translate to SQL and run against the database.
```

---

## Step 3: Cloud Service Interface

### AWS Examples
```
"Show me all running EC2 instances"
→ aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"

"What's in my S3 bucket photos?"
→ aws s3 ls s3://photos/

"Create a new Lambda function from this code"
→ [Claude creates deployment package and runs aws lambda create-function]
```

### Kubernetes Examples
```
"Why is my deployment failing?"
→ kubectl describe deployment myapp
→ kubectl get events --sort-by=.lastTimestamp
→ kubectl logs deployment/myapp

"Scale the API to 5 replicas"
→ kubectl scale deployment api --replicas=5

"Show resource usage across pods"
→ kubectl top pods
```

---

## Step 4: Multi-System Workflows

### Coordinated Actions
```
"Deploy the latest code to staging"

Claude orchestrates:
1. git pull origin main
2. npm run build
3. docker build -t myapp:staging .
4. docker push myapp:staging
5. kubectl set image deployment/myapp myapp=myapp:staging
6. kubectl rollout status deployment/myapp
```

### Cross-System Queries
```
"Compare production database size with staging"

Claude:
1. Queries production DB for size
2. Queries staging DB for size
3. Presents comparison table
```

---

## Step 5: API Interface

### REST APIs
```
"Create a new GitHub issue for this bug"
→ gh issue create --title "Bug: ..." --body "..."

"What's the weather in Tokyo?"
→ curl 'https://api.weather.com/...'

"Send a Slack message to #deployments"
→ curl -X POST -H 'Content-type: application/json' --data '{"text":"..."}' $SLACK_WEBHOOK
```

### GraphQL APIs
```
"Get all open pull requests with their reviews"
→ Claude constructs appropriate GraphQL query
→ Runs via gh api graphql
```

---

## Step 6: Building Your Interface

### Define Your Context
```
I work with these systems daily:
- PostgreSQL database (connection: DATABASE_URL)
- AWS (profile: mycompany)
- Kubernetes cluster (context: production)
- GitHub (repo: org/myapp)

When I ask questions, use the appropriate tool.
Explain what you're doing before running commands.
Summarize results in human-readable format.
```

### Create Aliases
```
Common operations I do:
- "deploy" = build, push, and roll out to Kubernetes
- "check health" = query all monitoring endpoints
- "db backup" = pg_dump to S3
- "logs" = get last 100 lines from all pods

Map these shortcuts to full workflows.
```

---

## Step 7: Safety and Verification

### Confirmation for Dangerous Operations
```
Before running:
- DELETE queries → Ask for confirmation
- Production deployments → Show what will change
- Destructive commands → Explain consequences

Claude should:
1. Show the command it will run
2. Explain what it does
3. Wait for approval on sensitive operations
```

### Audit Trail
```
Log all commands executed:
- What was requested
- What command was run
- What the result was
- Timestamp

Store in: ~/.claude/command-history.log
```

---

## Verification Checklist

- [ ] Queried a database using natural language
- [ ] Ran cloud CLI commands through Claude
- [ ] Created a multi-system workflow
- [ ] Set up confirmation for dangerous operations
- [ ] Built personalized shortcuts

---

## Universal Interface Patterns

| System | Example Command | Natural Language |
|--------|-----------------|------------------|
| Database | `SELECT...` | "Show me..." |
| Kubernetes | `kubectl get pods` | "List pods" |
| Docker | `docker ps` | "Running containers" |
| AWS | `aws s3 ls` | "What's in S3?" |
| Git | `git log --oneline` | "Recent commits" |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Credentials not configured | Set up env vars or config files first |
| Wrong context (prod vs staging) | Always specify environment |
| Dangerous commands running | Set up confirmation prompts |
| Complex results overwhelming | Ask Claude to summarize |

---

## Pro Tips

1. **Context Is Key:** Tell Claude about your systems upfront
2. **Start Safe:** Test with read-only commands first
3. **Build Incrementally:** Add systems one at a time
4. **Log Everything:** Keep audit trail of actions
5. **Confirm Destructive:** Always verify before mutating

---

## Next Challenge

Continue to **[Abstraction Levels](./08-abstraction-levels.md)** for working at the right level of detail!
