# Solution: Copy-Paste Power User Techniques

## Universal Keyboard Shortcuts

### Selection
```
Ctrl+A / Cmd+A     Select all content
Shift+End          Select to end of line
Shift+Home         Select to start of line
Ctrl+Shift+End     Select to end of document
Ctrl+Shift+Home    Select to start of document
Shift+Arrow        Extend selection by character
Shift+Ctrl+Arrow   Extend selection by word (Cmd+Arrow on macOS)
```

### Clipboard
```
Ctrl+C / Cmd+C     Copy
Ctrl+X / Cmd+X     Cut
Ctrl+V / Cmd+V     Paste
Ctrl+Z / Cmd+Z     Undo
Ctrl+Shift+Z       Redo (Cmd+Shift+Z on macOS)
```

### Navigation
```
Ctrl+F / Cmd+F     Find in page
Ctrl+Home          Jump to top
Ctrl+End           Jump to bottom
Page Up/Down       Scroll by page
```

## Web Content Extraction

### Technique 1: Select All Method

**Best for**: Documentation pages, blog posts, articles

```
1. Navigate to page
2. Press Cmd+A (macOS) or Ctrl+A (Windows/Linux)
3. Press Cmd+C / Ctrl+C to copy
4. Paste in Claude Code

Pros:
✓ Fastest method
✓ Gets all content
✓ Keyboard-only workflow

Cons:
✗ Includes some UI elements
✗ May include navigation/footer
```

**Example workflow**:
```
# In browser
1. Open: https://docs.example.com/api-reference
2. Cmd+A (select all)
3. Cmd+C (copy)

# In Claude Code
claude

You: [Paste content]
     "Summarize the key API endpoints and their purposes"
```

### Technique 2: Reader Mode Method

**Best for**: Cluttered websites, blogs, news articles

**Firefox**:
```
1. Press F9 or click Reader View icon
2. Content is cleaned automatically
3. Cmd+A to select all
4. Cmd+C to copy
```

**Safari**:
```
1. Click Reader icon in address bar
2. Or press Shift+Cmd+R
3. Cmd+A to select all
4. Cmd+C to copy
```

**Chrome** (requires extension):
```
1. Install "Reader View" extension
2. Click extension icon
3. Cmd+A to select all
4. Cmd+C to copy
```

**Pros**:
✓ Removes ads, sidebars, headers
✓ Clean, readable content
✓ Better formatting

**Example**:
```
# Reading API tutorial
1. Open tutorial page
2. Enable Reader Mode
3. Select all clean content
4. Paste in Claude:
   "Walk me through implementing this tutorial step by step"
```

### Technique 3: Inspect Element Method

**Best for**: Selecting specific sections, avoiding UI clutter

```
1. Right-click on content section
2. Choose "Inspect" or "Inspect Element"
3. In DevTools, right-click the HTML element
4. Choose "Copy" → "Copy outerHTML" or "Copy element"
5. Paste in text editor to extract text
6. Copy cleaned text to Claude
```

**Alternative - simpler**:
```
1. Right-click content area
2. "Inspect Element"
3. Find the main content div
4. Click to highlight in page
5. Now select just that section normally
```

### Technique 4: Browser Extensions

**Mercury Reader** (Chrome/Firefox):
- Cleans articles automatically
- One-click reading mode
- Exports clean text

**Copyfish** (Chrome):
- OCR for images
- Extract text from screenshots
- Copy from videos

**SingleFile** (Chrome/Firefox):
- Save complete page as single HTML
- Can strip unwanted elements
- Offline archiving

## GitHub Code Extraction

### Method 1: Raw Button

**Best for**: Single files, scripts, configs

```
1. Navigate to file on GitHub
2. Click "Raw" button (top right of file view)
3. Cmd+A to select all
4. Cmd+C to copy
5. Paste in Claude
```

**Example**:
```
URL: https://github.com/user/repo/blob/main/src/auth.ts
1. Click "Raw"
2. URL becomes: .../raw/main/src/auth.ts
3. Cmd+A, Cmd+C
4. Paste in Claude:
   "Review this authentication code for security issues"
```

### Method 2: Clone and Read

**Best for**: Multiple files, entire projects

```bash
# Clone repository
git clone https://github.com/user/repo.git
cd repo

# Launch Claude
claude

# Claude can read files directly
"Review the authentication system in src/auth/"
```

### Method 3: GitHub CLI

**Best for**: Issues, PRs, discussions

```bash
# View PR content
gh pr view 123

# View issue
gh issue view 456

# Can pipe to clipboard or file
gh pr view 123 > pr-context.txt

# Then in Claude:
claude
"Review the PR details in pr-context.txt"
```

### Method 4: Copy Path

**Best for**: Referencing specific files

```
1. On GitHub file view
2. Click "Copy path" button
3. Use in Claude conversation

Example:
"Review the file at src/components/auth/LoginForm.tsx in the repo"
```

## Stack Overflow Extraction

### Clean Extraction Method

```
1. Find relevant question/answer
2. Scroll to answer section
3. Click and drag to select:
   - Question title
   - Question body
   - Relevant answer(s)
4. Copy to clipboard
5. Paste in text editor first
6. Clean up:
   - Remove vote counts
   - Remove user avatars/names (if not relevant)
   - Remove comments (unless important)
7. Copy cleaned content to Claude
```

### Better Method: Code Blocks Only

```
1. Find answer with code
2. Click "Copy" button on code block (if available)
3. Or select just the code block
4. Paste in Claude with context:

"I found this solution on Stack Overflow:

[paste code]

How does this work and how can I adapt it for my use case?"
```

### Using SO Links Directly

```
# Sometimes easier to just share the link
You: "Explain the accepted answer here:
     https://stackoverflow.com/questions/123456/..."

Claude: [Can fetch and read the page]
```

## Documentation Sites

### Method 1: Section-by-Section

**Best for**: Long documentation pages

```
1. Navigate to docs
2. Find relevant section
3. Triple-click to select paragraph
4. Or click and drag section heading to end of section
5. Copy
6. Paste in Claude with context
```

**Example**:
```
# React Docs
1. Go to "useState" documentation
2. Select the "useState" section only
3. Copy
4. In Claude:
   "Explain this documentation about useState and give me examples"
```

### Method 2: Multiple Tabs

**Best for**: Compiling from multiple pages

```
1. Open relevant doc pages in tabs
2. Tab 1: Select and copy
3. Paste in text editor with label:
   "--- From: Authentication Guide ---"
   [content]

4. Tab 2: Select and copy
5. Paste in text editor:
   "--- From: API Reference ---"
   [content]

6. Copy entire compiled content to Claude:
   "Based on these docs, help me implement authentication"
```

### Method 3: Table of Contents Navigation

```
1. Open documentation page
2. Use table of contents to navigate
3. For each relevant section:
   - Click section in TOC
   - Page scrolls to section
   - Select just that section
   - Copy and compile
```

## PDF Text Extraction

### Method 1: Direct Selection

**Best for**: Text-based PDFs (not scanned)

```
1. Open PDF in viewer
2. Click and drag to select text
3. Copy to clipboard
4. Paste in text editor first (formatting may be messy)
5. Clean up formatting
6. Copy to Claude
```

**Tips**:
- Select column by column for multi-column PDFs
- Copy tables as-is, Claude can interpret
- Preserve code block structure

### Method 2: PDF to Text Tools

**macOS**:
```bash
# Using Preview's built-in OCR
# Just select and copy text

# Or command line:
pdftotext document.pdf output.txt
cat output.txt | pbcopy
```

**Linux**:
```bash
# Install pdftotext
sudo apt-get install poppler-utils

# Convert
pdftotext document.pdf output.txt

# Copy to clipboard
xclip -selection clipboard < output.txt
```

**Windows**:
```powershell
# Use Adobe Reader to select and copy

# Or online tools:
# - pdf2go.com
# - ilovepdf.com
# - smallpdf.com
```

### Method 3: OCR for Scanned PDFs

**Online Tools**:
- ocr.space
- onlineocr.net
- Adobe Acrobat Online

**Desktop Tools**:
- Adobe Acrobat (paid)
- ABBYY FineReader (paid)
- Tesseract (free, command line)

```bash
# Tesseract OCR (open source)
# macOS
brew install tesseract

# Linux
sudo apt-get install tesseract-ocr

# Convert PDF to image, then OCR
pdftoppm document.pdf page -png
tesseract page-1.png output
cat output.txt
```

## Error Messages and Logs

### Terminal Error Messages

```bash
# Method 1: Select in terminal
1. Click before error
2. Shift+Click after error
3. Cmd+C / Ctrl+C

# Method 2: Pipe to clipboard
command 2>&1 | pbcopy  # macOS
command 2>&1 | xclip -selection clipboard  # Linux

# Method 3: Redirect to file
command > output.txt 2>&1
claude
"Debug this error in output.txt"
```

### Browser Console Errors

```
1. Open DevTools (F12)
2. Go to Console tab
3. Right-click on error
4. Choose "Copy message" or "Copy stack trace"
5. Or select all with Cmd+A and copy

Paste in Claude:
"Explain this JavaScript error and how to fix it"
```

### Application Logs

```bash
# View logs
tail -f /var/log/app.log

# When error appears:
Ctrl+C to stop tail

# Copy recent errors
tail -100 /var/log/app.log | pbcopy  # macOS
tail -100 /var/log/app.log | xclip -selection clipboard  # Linux

# Paste in Claude
claude
"Analyze these application errors"
```

## Multi-Source Compilation

### Workflow: Research Mode

```
1. Open all relevant tabs/windows

2. Create compilation document:
   # research-notes.md

3. For each source:
   ---
   Source: [URL or description]
   Relevant excerpt:
   [paste content]
   ---

4. Save compilation

5. In Claude:
   claude
   "I've compiled research on [topic] in research-notes.md.
    Help me synthesize this into [deliverable]"
```

### Browser Window Management

```
# Split screen for efficiency
# Left: Browser with sources
# Right: Text editor for compilation

Workflow:
1. Read in browser
2. Select relevant text
3. Cmd+C
4. Click text editor
5. Cmd+V with label
6. Back to browser (Cmd+Tab)
7. Repeat

Final step:
Copy entire compilation to Claude
```

## Screenshot + OCR Workflow

### When to Use Screenshots

Use when:
- Content can't be selected (image-based)
- Diagram or visual is important
- UI context matters
- Copy protection prevents text selection

### Taking Screenshots

**macOS**:
```
Cmd+Shift+3       Full screen
Cmd+Shift+4       Selection
Cmd+Shift+4+Space Window capture
Cmd+Shift+5       Screenshot menu (with options)
```

**Windows**:
```
Win+Shift+S       Snipping Tool
PrtScn            Full screen
Alt+PrtScn        Active window
```

**Linux**:
```
PrtScn            Full screen
Shift+PrtScn      Selection
# Or use GNOME Screenshot, Spectacle, etc.
```

### Using Screenshots in Claude

```
# Claude Code supports image input

claude

You: [Paste or drag screenshot]
     "What does this error message mean?"

Claude: [Reads image via OCR and responds]
```

### Screenshot Best Practices

```
✓ Capture relevant context
✓ Include enough surrounding UI for clarity
✓ Use high resolution
✓ Crop out unnecessary parts
✓ Annotate if needed (arrows, highlights)

✗ Too much content (unreadable)
✗ Too little context (unclear)
✗ Low resolution (can't read text)
✗ Includes sensitive information
```

## Advanced Techniques

### Technique 1: Bookmarklet for Clean Copy

Create a bookmarklet that cleans and copies content:

```javascript
javascript:(function(){
    var content = document.body.innerText;
    navigator.clipboard.writeText(content);
    alert('Content copied!');
})();
```

Save as bookmark, click to copy page text.

### Technique 2: Command Line Fetch

```bash
# Fetch and copy page content
curl -s https://example.com/docs | pbcopy

# Or save to file
curl -s https://example.com/docs > docs.txt

# Then in Claude:
claude
"Summarize the documentation in docs.txt"
```

### Technique 3: Browser Automation

```javascript
// JavaScript console snippet to extract content
const content = document.querySelector('main').innerText;
copy(content); // Copies to clipboard
```

### Technique 4: Markdown Conversion

```bash
# Convert HTML to Markdown for cleaner input
# Using pandoc
curl -s https://example.com | pandoc -f html -t markdown

# Or using online service
# markdownify.com
```

## Best Practices

### 1. Clean Before Pasting

```
❌ Direct paste with formatting issues:
"Here's some content [weird spacing] (ad) [navigation menu]..."

✅ Paste in text editor first, clean, then copy to Claude:
"Here's the relevant documentation about authentication..."
```

### 2. Provide Context

```
❌ Just pasting code:
[paste mysterious code snippet]

✅ Paste with context:
"I found this authentication implementation on GitHub.
Can you explain how it works and if it's secure?

[paste code]"
```

### 3. Be Selective

```
❌ Copy entire 50-page documentation:
[Ctrl+A on massive docs site]

✅ Copy relevant sections:
"I'm specifically interested in the WebSocket authentication section:
[paste relevant 2-3 paragraphs]"
```

### 4. Preserve Code Formatting

```
❌ Pasting code that lost indentation:
function example() {
console.log('broken')
}

✅ Use code blocks or preserve formatting:
\`\`\`typescript
function example() {
    console.log('formatted correctly')
}
\`\`\`
```

## Quick Reference

### Speed Shortcuts

```
Task                          Shortcut
----                          --------
Select all page              Cmd/Ctrl + A
Copy                         Cmd/Ctrl + C
Paste                        Cmd/Ctrl + V
Find in page                 Cmd/Ctrl + F
Reader mode (Firefox)        F9
Reader mode (Safari)         Shift+Cmd+R
Screenshot (macOS)           Cmd+Shift+4
Screenshot (Windows)         Win+Shift+S
New tab                      Cmd/Ctrl + T
Close tab                    Cmd/Ctrl + W
Switch tab                   Cmd/Ctrl + Tab
```

### Decision Matrix

```
Content Type          Best Method
------------          -----------
Documentation         Select All or Reader Mode
GitHub code           Raw button
Stack Overflow        Code blocks only
PDF text              Direct selection
Scanned PDF           OCR tool
Error message         Terminal selection
Browser error         Console copy
Multiple sources      Compile in text editor
Visual content        Screenshot
Protected content     Screenshot + OCR
```

## Success Indicators

You've mastered copy-paste power techniques when you:

- Use keyboard shortcuts exclusively (no mouse)
- Clean content before pasting to Claude
- Extract code blocks without extra formatting
- Compile multi-source content efficiently
- Know when to use screenshots vs text
- Navigate documentation quickly
- Copy errors and logs precisely
- Provide context with pastes
- Never paste raw HTML or UI clutter
- Can extract from any source confidently
