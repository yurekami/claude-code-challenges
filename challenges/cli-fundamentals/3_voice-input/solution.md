# Solution: Voice Input Configuration

## Step-by-Step Setup

### Step 1: Obtain OpenAI API Key

1. Visit https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Name it "Claude Code Voice" (for tracking)
5. Copy the key (starts with `sk-proj-...`)
6. Store it securely (you won't see it again)

**Cost Note**: Whisper API is very affordable (~$0.006 per minute of audio)

### Step 2: Configure API Key in Claude Code

**Method 1: Environment Variable (Recommended)**

```bash
# Linux/macOS - Add to ~/.bashrc or ~/.zshrc
export OPENAI_API_KEY="sk-proj-your-key-here"

# Windows - PowerShell
$env:OPENAI_API_KEY="sk-proj-your-key-here"

# Windows - Command Prompt
set OPENAI_API_KEY=sk-proj-your-key-here

# Reload shell
source ~/.bashrc  # or restart terminal
```

**Method 2: Claude Code Settings File**

```bash
# Create/edit settings file
# Linux/macOS: ~/.claude/settings.json
# Windows: %USERPROFILE%\.claude\settings.json

{
  "openai_api_key": "sk-proj-your-key-here",
  "voice_enabled": true,
  "voice_shortcut": "Ctrl+Shift+V"  // or "Cmd+Shift+V" on macOS
}
```

**Method 3: In-Session Configuration**

```bash
# In Claude Code session
/settings

# Set OpenAI API key
openai_api_key: sk-proj-your-key-here
```

### Step 3: Set Up Keyboard Shortcut

**Default Shortcuts:**
- **macOS**: `Cmd + Shift + V`
- **Windows**: `Ctrl + Shift + V`
- **Linux**: `Ctrl + Shift + V`

**Custom Shortcut Configuration:**

```json
// ~/.claude/settings.json
{
  "voice": {
    "enabled": true,
    "shortcut": "Ctrl+Alt+Space",  // Your preferred shortcut
    "language": "en",               // Language code
    "model": "whisper-1"            // Whisper model
  }
}
```

### Step 4: Test Voice Transcription

```bash
# 1. Launch Claude Code
claude

# 2. Press voice input shortcut (Ctrl+Shift+V or Cmd+Shift+V)

# 3. Speak clearly:
"Hello Claude, can you hear me? Please respond with a greeting."

# 4. Release the key when done speaking

# 5. Claude will transcribe and respond
```

**Expected Workflow:**
1. Hold shortcut key
2. Red/recording indicator appears
3. Speak your message
4. Release key
5. Transcription appears in chat
6. Claude processes and responds

### Step 5: Practice Complex Dictation

**Example 1: Code Review**

```
[Hold voice key and speak]

"I'm reviewing the authenticate user function in auth.ts.
I see several issues:

First, the password is being logged in plain text on line 23,
which is a security vulnerability.

Second, there's no rate limiting on failed login attempts,
making the system vulnerable to brute force attacks.

Third, the JWT token expiration is set to 365 days,
which is way too long and violates security best practices.

Can you help me fix these issues?"
```

**Example 2: Feature Request**

```
[Hold voice key and speak]

"I need to implement a notification system with three main features:

One: Real-time notifications using WebSockets for instant delivery.

Two: A notification center UI component showing unread count
and last 50 notifications with infinite scroll.

Three: Email fallback for users who are offline,
batched and sent every hour.

Please create an implementation plan breaking this down into phases."
```

**Example 3: Bug Report**

```
[Hold voice key and speak]

"I'm encountering a bug in the checkout flow.

Steps to reproduce:
1. Add three items to cart
2. Navigate to checkout
3. Enter payment details
4. Click submit

Expected: Order confirmation page
Actual: 500 error and cart is cleared

The error appears to happen when the payment gateway times out.
Can you help me debug this?"
```

## Voice Input Best Practices

### Do's ✓

1. **Speak clearly and at moderate pace**
   - Not too fast, not too slow
   - Clear pronunciation
   - Pause between sentences

2. **Use natural language**
   - Speak conversationally
   - Don't try to dictate syntax
   - Explain the intent, not the exact code

3. **Structure your speech**
   - "First... Second... Third..."
   - "There are three issues..."
   - "Let me explain the problem..."

4. **Spell out ambiguous terms**
   - "JWT, spelled J-W-T"
   - "API key, spelled A-P-I"
   - "PostgreSQL, that's P-O-S-T-G-R-E-S-Q-L"

5. **Use punctuation cues**
   - "period" for .
   - "comma" for ,
   - "new paragraph" for breaks
   - "question mark" for ?

### Don'ts ✗

1. **Don't dictate code directly**
   - ✗ "const user equals curly brace name colon..."
   - ✓ "Create a user object with name and email properties"

2. **Don't use in noisy environments**
   - Background noise reduces accuracy
   - Find a quiet space for best results

3. **Don't rush**
   - Speaking too fast causes errors
   - Pause to gather thoughts

4. **Don't mumble**
   - Clear enunciation is critical
   - Speak with confidence

5. **Don't use for precise formatting**
   - Markdown tables are hard to dictate
   - Code blocks are better typed
   - Use for descriptions, type for structure

## Advanced Voice Techniques

### Technique 1: Hybrid Voice + Typing

```
Voice: "I need to implement a rate limiter for the API"

Type: "Use Redis for distributed rate limiting"

Voice: "The limiter should allow 100 requests per minute per user,
with a burst capacity of 150. It should return 429 status
when the limit is exceeded."

Type: "Show me the implementation"
```

### Technique 2: Voice for Context, Type for Precision

```
Voice: "I'm working on the user authentication system.
We need to add two-factor authentication using TOTP.
Users should be able to enable it in their settings,
and it should be required for admin accounts."

Type: "Generate the database migration for TOTP secrets"

Voice: "Now let's implement the QR code generation
for enrolling users in the 2FA system."

Type: "Use the speakeasy library"
```

### Technique 3: Voice Brainstorming

```
Voice: "Let me think through this architecture problem.

We have a microservices system with five services.
The payment service needs to notify the order service
when payment completes.

Option one: Direct HTTP call. Pros: simple. Cons: coupling.

Option two: Message queue. Pros: decoupled. Cons: complexity.

Option three: Event sourcing. Pros: audit trail. Cons: learning curve.

What are your thoughts on these approaches?"
```

### Technique 4: Structured Problem Description

```
Voice: "Problem statement:
The application becomes unresponsive after 10,000 concurrent users.

Current architecture:
Single Node.js server, PostgreSQL database,
no caching layer, no load balancing.

Constraints:
Budget is limited, team is small,
need solution within 2 weeks.

Question:
What's the most effective way to scale
without a complete rewrite?"
```

## Troubleshooting

### Issue 1: Voice Input Not Working

**Symptoms**: Shortcut key doesn't start recording

**Solutions**:
```bash
# 1. Check API key is set
echo $OPENAI_API_KEY  # Should show your key

# 2. Verify microphone permissions
# macOS: System Preferences → Security → Microphone
# Windows: Settings → Privacy → Microphone
# Linux: Check PulseAudio/ALSA settings

# 3. Test with Claude Code debug mode
claude --debug

# 4. Check settings file
cat ~/.claude/settings.json
```

### Issue 2: Poor Transcription Accuracy

**Symptoms**: Text doesn't match what you said

**Solutions**:
- Speak more slowly and clearly
- Reduce background noise
- Use a better microphone
- Speak in shorter segments
- Specify language if not English: `"language": "es"` for Spanish

### Issue 3: Shortcut Key Conflict

**Symptoms**: Shortcut triggers other application

**Solutions**:
```json
// Change shortcut in settings
{
  "voice": {
    "shortcut": "Ctrl+Alt+V"  // Different combo
  }
}
```

### Issue 4: API Costs Concern

**Symptoms**: Worried about Whisper API costs

**Solutions**:
- Monitor usage at platform.openai.com/usage
- Set up billing alerts
- Use voice strategically (not for every message)
- Average cost: $0.006/minute (very affordable)

## Verification Tasks

### Task 1: Basic Transcription

```bash
# Start Claude Code
claude

# Press voice shortcut and say:
"Hello Claude, this is a test of voice transcription.
Can you confirm you received this message?"

# Verify: Text appears correctly in chat
```

### Task 2: Technical Vocabulary

```bash
# Press voice shortcut and say:
"I need help with PostgreSQL database optimization,
specifically around query performance and index strategies
for a React application using TypeScript and GraphQL."

# Verify: Technical terms transcribed correctly
```

### Task 3: Complex Explanation

```bash
# Press voice shortcut and say:
"I'm implementing a feature that requires three steps.
First, validate the user input using Zod schema validation.
Second, store the data in the database using Prisma ORM.
Third, emit a webhook notification to external systems.
Can you help me architect this?"

# Verify: Structure preserved, details accurate
```

### Task 4: Speed Test

```bash
# Time yourself typing this:
"I need to implement authentication with JWT tokens,
refresh token rotation, role-based access control,
and password reset functionality via email."

# Now time yourself speaking it via voice input

# Compare: Voice should be 2-3x faster
```

## Common Mistakes to Avoid

### Mistake 1: Dictating Code Syntax
```
❌ "const user equals curly brace name colon quote John quote comma"
✓ "Create a user object with name property set to John"
```

### Mistake 2: Speaking Too Fast
```
❌ "IneedtoimplementafeaturethatdoesXYZandABC"
✓ [Pause] "I need to implement a feature" [Pause] "that does X Y Z and A B C"
```

### Mistake 3: Not Spelling Ambiguous Terms
```
❌ "Use the sequel database"  → Transcribes as "use the sequel database"
✓ "Use the S-Q-L database" or "Use the SQL, that's S-Q-L, database"
```

### Mistake 4: Using Voice for Everything
```
❌ Voice for typing commands, code, and explanations
✓ Voice for explanations, typing for code and commands
```

## Best Practices Summary

1. **Setup**: Environment variable for API key (most secure)
2. **Usage**: Voice for explanations, typing for code
3. **Quality**: Quiet environment, clear speech, moderate pace
4. **Structure**: Organize thoughts before speaking
5. **Hybrid**: Combine voice and typing for optimal workflow
6. **Cost**: Monitor usage, but don't overthink it (very cheap)

## Quick Reference

```
Setup Steps:
1. Get OpenAI API key
2. Set OPENAI_API_KEY environment variable
3. Configure voice shortcut in settings
4. Test with simple phrase

Best Use Cases:
✓ Code reviews
✓ Bug descriptions
✓ Feature explanations
✓ Brainstorming
✓ Complex requirements

Avoid For:
✗ Dictating code
✗ Typing commands
✗ Precise formatting
✗ Noisy environments

Shortcuts:
- macOS: Cmd + Shift + V
- Windows/Linux: Ctrl + Shift + V
- Custom: Configure in ~/.claude/settings.json
```

## Success Indicators

You've mastered voice input when you:
- Naturally reach for voice shortcut for explanations
- Can dictate complex technical descriptions clearly
- Know when to use voice vs typing
- Achieve 95%+ transcription accuracy
- Save significant time on communication
- Seamlessly switch between voice and keyboard
