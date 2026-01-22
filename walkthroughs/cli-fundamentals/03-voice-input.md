# Walkthrough: Voice Input

**Difficulty:** Easy | **Time:** 15 minutes | **Category:** CLI Fundamentals

---

## Overview

Voice input transforms how you interact with Claude Code. Instead of typing, simply speak your requests. This is especially useful for dictating long explanations, describing bugs, or when your hands are busy.

## Prerequisites

- [ ] Claude Code CLI installed
- [ ] Microphone connected and working
- [ ] Quiet environment for best recognition

---

## Step 1: Check Voice Input Availability

Verify voice input is available on your system:

```
/help voice
```

Or look for the microphone indicator in Claude Code's interface.

**Supported Platforms:**
- macOS: Built-in support via system APIs
- Windows: Requires specific audio setup
- Linux: May require additional packages

---

## Step 2: Enable Voice Mode

Activate voice input mode:

**Method 1: Keyboard Shortcut**
```
Press: Ctrl+Shift+V (or Cmd+Shift+V on Mac)
```

**Method 2: Slash Command**
```
/voice
```

**Expected Indicator:**
```
🎤 Voice mode active - speak when ready...
```

---

## Step 3: Speak Your First Command

With voice mode active, speak clearly:

```
"Create a function called calculate sum that takes an array of numbers and returns their total"
```

**Expected Result:**
Claude interprets your speech and generates:
```javascript
function calculateSum(numbers) {
  return numbers.reduce((sum, num) => sum + num, 0);
}
```

---

## Step 4: Practice Voice Commands

Try these voice commands to get comfortable:

### Simple Commands
| Say This | Claude Does |
|----------|-------------|
| "Show me the package.json file" | Reads package.json |
| "What does this function do?" | Explains selected code |
| "Fix the syntax error" | Corrects code issues |

### Complex Commands
| Say This | Claude Does |
|----------|-------------|
| "Add error handling to this function with try catch" | Wraps code in try-catch |
| "Refactor this to use async await instead of promises" | Modernizes async code |
| "Write unit tests for the user service" | Generates test file |

---

## Step 5: Voice + Context Combination

Use voice with file context for powerful workflows:

1. **Load a file first:**
   ```
   Read src/api/users.ts
   ```

2. **Then use voice:**
   ```
   "Add a new method called delete user that takes a user ID and removes them from the database"
   ```

**Pro Tip:** Voice works best when Claude already has context about what you're working on.

---

## Step 6: Dictate Documentation

Voice is excellent for documentation:

```
"Add JSDoc comments to this function explaining that it handles user authentication, takes an email and password, and returns a session token or throws an authentication error"
```

**Result:**
```javascript
/**
 * Handles user authentication
 * @param {string} email - User's email address
 * @param {string} password - User's password
 * @returns {string} Session token on successful authentication
 * @throws {AuthenticationError} When credentials are invalid
 */
function authenticate(email, password) {
  // implementation
}
```

---

## Step 7: Voice for Bug Description

Describe bugs naturally:

```
"When I click the submit button nothing happens. The form data should be sent to the API but I see no network request in dev tools. The button's onClick handler is connected but the async function might not be awaited"
```

Claude will analyze and likely respond with debugging steps or fixes.

---

## Verification Checklist

- [ ] Can enable voice mode via shortcut or command
- [ ] Successfully dictated a simple coding request
- [ ] Used voice with file context
- [ ] Dictated documentation for a function
- [ ] Described a bug using voice

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Voice not recognized | Check microphone permissions in system settings |
| Poor transcription | Speak slower, reduce background noise |
| Wrong words interpreted | Use the text correction feature after transcription |
| Voice mode not available | Update Claude Code to latest version |

---

## Voice Best Practices

### DO:
- Speak in complete sentences
- Pause briefly between distinct instructions
- Use technical terms - Claude understands them
- Describe the "why" not just the "what"

### DON'T:
- Rush through complex instructions
- Assume Claude heard perfectly - verify transcription
- Use voice in noisy environments
- Forget punctuation hints ("new line", "open bracket")

---

## Advanced Voice Techniques

### Punctuation Commands
| Say | Inserts |
|-----|---------|
| "period" | `.` |
| "comma" | `,` |
| "new line" | Line break |
| "open paren" | `(` |
| "close curly brace" | `}` |

### Code Dictation
```
"function greet open paren name close paren open curly brace new line return template string Hello comma space dollar sign open curly brace name close curly brace exclamation point close template string new line close curly brace"
```

---

## Pro Tips

1. **Hybrid Approach:** Start with voice for the idea, then type for precision
2. **Review Before Accept:** Always read the transcription before sending
3. **Context First:** Load relevant files before starting voice mode
4. **Natural Language:** Speak as if explaining to a colleague, not dictating code

---

## Next Challenge

Move on to **[Problem Decomposition](./04-problem-decomposition.md)** to learn how to break complex tasks into manageable pieces!
