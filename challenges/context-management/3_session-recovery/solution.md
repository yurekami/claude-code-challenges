# Solution: Session Recovery

## Step-by-Step Solution

### Step 1: Locate Conversation History

**On macOS/Linux:**
```bash
cd ~/.claude/projects

# List all projects
ls -la

# Find your specific project
ls -la | grep "your-project-name"

# Navigate to project directory
cd your-project-name

# View conversation files
ls -la conversations/
```

**On Windows:**
```powershell
cd $env:USERPROFILE\.claude\projects

# List all projects
Get-ChildItem

# Navigate to project directory
cd your-project-name

# View conversation files
Get-ChildItem conversations\
```

**Directory Structure:**
```
~/.claude/projects/
└── your-project-name/
    ├── conversations/
    │   ├── conversation-1.json
    │   ├── conversation-2.json
    │   └── conversation-3.json
    ├── metadata.json
    └── settings.json
```

### Step 2: Understanding Conversation File Format

Conversation files typically contain:

```json
{
  "id": "conv_abc123",
  "created_at": "2025-01-20T14:30:00Z",
  "messages": [
    {
      "role": "user",
      "content": "Implement JWT authentication",
      "timestamp": "2025-01-20T14:30:00Z"
    },
    {
      "role": "assistant",
      "content": "I'll implement JWT authentication...",
      "timestamp": "2025-01-20T14:30:15Z"
    }
  ],
  "tool_calls": [...],
  "metadata": {...}
}
```

### Step 3: Search Strategies

#### Strategy A: Simple Text Search (grep)

```bash
# Search for specific keyword across all conversations
grep -r "JWT" ~/.claude/projects/your-project/conversations/

# Search with context (2 lines before and after)
grep -r -B 2 -A 2 "authentication" ~/.claude/projects/your-project/conversations/

# Case-insensitive search
grep -ri "token expiry" ~/.claude/projects/your-project/conversations/

# Search for multiple terms
grep -r "rate limit" ~/.claude/projects/your-project/conversations/ | grep -i "configuration"
```

#### Strategy B: Advanced Search (ripgrep)

```bash
# Install ripgrep if not available
# macOS: brew install ripgrep
# Ubuntu: apt install ripgrep
# Windows: choco install ripgrep

# Search with better formatting
rg "JWT" ~/.claude/projects/your-project/conversations/

# Search JSON specifically
rg -t json "authentication" ~/.claude/projects/your-project/

# Search with line numbers and context
rg -n -C 3 "token expiry" ~/.claude/projects/your-project/

# Search for regex patterns
rg "expir(y|e|ation).*\d+" ~/.claude/projects/your-project/
```

#### Strategy C: Date-Based Search

```bash
# Find conversations from specific date
find ~/.claude/projects/your-project/conversations/ -name "*.json" -newermt "2025-01-20"

# Search within date range
find ~/.claude/projects/your-project/conversations/ -name "*.json" -newermt "2025-01-20" ! -newermt "2025-01-21" -exec grep -l "authentication" {} \;
```

#### Strategy D: Using jq (JSON query tool)

```bash
# Install jq
# macOS: brew install jq
# Ubuntu: apt install jq
# Windows: choco install jq

# Extract all user messages containing "JWT"
jq '.messages[] | select(.role == "user") | select(.content | contains("JWT"))' ~/.claude/projects/your-project/conversations/conversation-1.json

# Get messages from specific date
jq '.messages[] | select(.timestamp | startswith("2025-01-20"))' ~/.claude/projects/your-project/conversations/conversation-1.json

# Extract assistant responses about specific topic
jq '.messages[] | select(.role == "assistant") | select(.content | contains("rate limit"))' ~/.claude/projects/your-project/conversations/conversation-1.json
```

### Step 4: Real-World Recovery Example

**Scenario:** Recover authentication implementation decisions

```bash
# Step 1: Search for authentication-related conversations
rg -l "authentication" ~/.claude/projects/ecommerce/conversations/

# Output:
# conversation-2025-01-20.json
# conversation-2025-01-21.json

# Step 2: Search for specific decisions
rg -B 5 -A 5 "JWT vs" ~/.claude/projects/ecommerce/conversations/

# Output might show:
# "We need to choose between JWT and sessions for authentication"
# "I recommend JWT because..."
# "Token expiry set to 15 minutes for access tokens"

# Step 3: Extract token configuration
rg -n "token.*expir" ~/.claude/projects/ecommerce/conversations/

# Step 4: Find rate limiting details
rg -C 3 "rate limit" ~/.claude/projects/ecommerce/conversations/

# Step 5: Combine findings into recovery doc
```

### Step 5: Create Context Recovery Document

Based on searches, create a structured document:

```markdown
# Context Recovery: Authentication System
*Recovered from conversations: 2025-01-20 to 2025-01-21*

## Recovered Decisions

### JWT vs Sessions (2025-01-20 14:30)
**Decision:** JWT tokens
**Rationale:**
- Need stateless authentication for mobile app
- Microservices architecture benefits from stateless auth
- Team has JWT experience

**Source:** conversation-2025-01-20.json, line 245

### Token Configuration (2025-01-20 15:15)
**Access Token:** 15 minutes expiry
**Refresh Token:** 7 days expiry
**Rationale:** Balance between security and UX

**Source:** conversation-2025-01-20.json, line 389

### Rate Limiting (2025-01-20 16:00)
**Configuration:**
- 5 login attempts per 15 minutes per IP
- 100 requests per hour per authenticated user
- 429 status code on limit exceeded

**Rationale:** Prevent brute force attacks while allowing legitimate use

**Source:** conversation-2025-01-20.json, line 512

## Recovered Code Snippets

### Token Generation
```typescript
// From conversation-2025-01-20.json, line 421
function generateTokens(userId: string) {
  const accessToken = jwt.sign(
    { userId, type: 'access' },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );

  const refreshToken = jwt.sign(
    { userId, type: 'refresh' },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );

  return { accessToken, refreshToken };
}
```

## Open Questions from Previous Session
- [ ] How to handle refresh token rotation?
- [ ] Need to implement token revocation list?
- [ ] What happens to active sessions when user changes password?

**Source:** conversation-2025-01-21.json, line 102
```

### Step 6: Automation Script

Create a helper script for common searches:

```bash
#!/bin/bash
# save as ~/.claude/scripts/search-history.sh

PROJECT_DIR="$HOME/.claude/projects/$1"
SEARCH_TERM="$2"

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: search-history.sh <project-name> <search-term>"
    exit 1
fi

echo "Searching for '$SEARCH_TERM' in project '$1'..."
echo ""

# Search conversations
rg -C 3 --color always "$SEARCH_TERM" "$PROJECT_DIR/conversations/"

# Count occurrences
echo ""
echo "Total occurrences:"
rg -c "$SEARCH_TERM" "$PROJECT_DIR/conversations/" | awk -F: '{sum+=$2} END {print sum}'
```

Usage:
```bash
chmod +x ~/.claude/scripts/search-history.sh
~/.claude/scripts/search-history.sh ecommerce "JWT"
```

### Step 7: Advanced Recovery Techniques

#### Technique 1: Timeline Reconstruction

```bash
# Extract all messages with timestamps, sorted
jq -r '.messages[] | "\(.timestamp) [\(.role)]: \(.content[:100])..."' \
  ~/.claude/projects/ecommerce/conversations/*.json | sort

# Output:
# 2025-01-20T14:30:00Z [user]: Implement JWT authentication
# 2025-01-20T14:30:15Z [assistant]: I'll implement JWT authentication...
# 2025-01-20T15:15:00Z [user]: What should the token expiry be?
# 2025-01-20T15:15:10Z [assistant]: I recommend 15 minutes for access tokens...
```

#### Technique 2: Decision Mining

```bash
# Extract all instances where decisions were made
rg -i "decision:|chose|selected|decided" ~/.claude/projects/ecommerce/conversations/ -B 2 -A 5

# Extract rationale statements
rg -i "because|rationale|reason" ~/.claude/projects/ecommerce/conversations/ -B 1 -A 3
```

#### Technique 3: Code Evolution Tracking

```bash
# Find all code snippets related to auth
rg -A 20 "```typescript" ~/.claude/projects/ecommerce/conversations/ | grep -A 20 "auth"

# Track changes to specific function
rg -B 2 -A 15 "generateTokens" ~/.claude/projects/ecommerce/conversations/
```

## Common Mistakes to Avoid

### Mistake 1: Searching Too Broadly
❌ **Wrong:**
```bash
grep "token" ~/.claude/projects/ecommerce/conversations/
# Returns thousands of matches
```

✅ **Correct:**
```bash
rg "token expiry|token expiration|expiresIn" ~/.claude/projects/ecommerce/conversations/
# More specific, better results
```

### Mistake 2: Ignoring Context
❌ **Wrong:** Copy first match without understanding context.

✅ **Correct:** Use `-B` and `-A` flags to see surrounding conversation:
```bash
rg -B 5 -A 5 "JWT" ~/.claude/projects/ecommerce/conversations/
```

### Mistake 3: Not Verifying Currency
❌ **Wrong:** Using old decisions that were later changed.

✅ **Correct:** Check timestamps and look for updates:
```bash
# Search chronologically
jq '.messages[] | select(.content | contains("JWT")) | {timestamp, content}' \
  ~/.claude/projects/ecommerce/conversations/*.json | sort
```

### Mistake 4: Manual Search Only
❌ **Wrong:** Manually opening and reading each file.

✅ **Correct:** Use command-line tools for efficient searching.

## Tool Recommendations

### Essential Tools

1. **ripgrep (rg)** - Fastest search
   ```bash
   brew install ripgrep  # macOS
   apt install ripgrep   # Ubuntu
   choco install ripgrep # Windows
   ```

2. **jq** - JSON querying
   ```bash
   brew install jq  # macOS
   apt install jq   # Ubuntu
   choco install jq # Windows
   ```

3. **fzf** - Fuzzy finder (optional but helpful)
   ```bash
   brew install fzf  # macOS
   apt install fzf   # Ubuntu
   choco install fzf # Windows
   ```

### Helper Aliases

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Search Claude conversations
alias claude-search='rg --color always -C 3'
alias claude-find='rg -l'

# Quick project navigation
alias claude-projects='cd ~/.claude/projects'

# JSON query helper
alias claude-jq='jq ".messages[] | select(.content | contains(\$term))"'
```

## Measuring Success

Successful session recovery means:
- ✅ Found relevant information in <5 minutes
- ✅ Recovered key decisions with rationale
- ✅ Retrieved working code snippets
- ✅ Understood timeline of changes
- ✅ No need to ask Claude what was previously discussed

## Edge Cases

### Case 1: Very Large Conversation Files
If files are >10MB:

```bash
# Use streaming search instead of loading entire file
rg --mmap "search term" large-conversation.json

# Or split search
split -l 10000 large-conversation.json chunk_
grep "search term" chunk_*
```

### Case 2: Compressed Conversation History
Some installations compress old conversations:

```bash
# Search in gzipped files
zgrep "search term" ~/.claude/projects/ecommerce/conversations/*.gz

# Decompress temporarily
gunzip -c conversation.json.gz | rg "search term"
```

### Case 3: Multiple Projects with Similar Context
```bash
# Search across all projects
rg "authentication" ~/.claude/projects/*/conversations/

# See which project each match is from
rg "authentication" ~/.claude/projects/*/conversations/ --heading
```

## Best Practices

1. **Search specific before broad** - Start with exact terms, then expand
2. **Use context flags** - Always use `-B` and `-A` for surrounding context
3. **Verify timestamps** - Ensure information is current
4. **Cross-reference** - Check multiple mentions of same topic
5. **Document findings** - Create recovery document immediately
6. **Automate common searches** - Create scripts for frequent tasks
7. **Regular backups** - Keep backups of important conversations
8. **Clean old conversations** - Archive or delete very old, irrelevant conversations
