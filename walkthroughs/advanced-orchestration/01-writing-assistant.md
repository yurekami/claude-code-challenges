# Walkthrough: Writing Assistant

**Difficulty:** Medium | **Time:** 20 minutes | **Category:** Advanced Orchestration

---

## Overview

Claude Code isn't just for programming. It's a powerful writing collaborator for documentation, blog posts, and technical content. This challenge teaches you to use Claude as an effective writing partner.

## Prerequisites

- [ ] Topic to write about
- [ ] Basic writing skills
- [ ] Understanding of your audience

---

## Step 1: Start with Structure

### Ask for an Outline
```
I want to write a blog post about [topic].

Create an outline with:
- Compelling title options (3)
- Hook/intro approach
- 5-7 main sections
- Key points for each section
- Call to action for conclusion
```

### Example Output
```markdown
# Title Options
1. "5 Lessons from Building CLI Tools Nobody Tells You"
2. "Why Your CLI Tool Fails (And How to Fix It)"
3. "The Art of Command-Line User Experience"

## Outline
1. Hook: A frustrating CLI experience everyone relates to
2. Problem: Why CLIs often have poor UX
3. Lesson 1: Error messages matter
4. Lesson 2: Defaults should be smart
5. Lesson 3: Progressive disclosure of complexity
6. Lesson 4: Consistency with conventions
7. Lesson 5: Documentation as first-class citizen
8. Conclusion: CTA to improve your own CLI
```

---

## Step 2: Draft Sections Collaboratively

### Section by Section
```
Write the first section "Hook: A frustrating CLI experience"

Style guide:
- Conversational but professional
- Short paragraphs (2-3 sentences)
- One clear example
- ~150 words
```

### Iterate
```
This is good, but:
- Make it more personal
- Add a touch of humor
- End with a question to engage readers
```

---

## Step 3: Technical Documentation

### API Documentation
```
Document this API endpoint:

POST /api/users
Body: { email, password, name }
Returns: User object with token

Include:
- Description
- Parameters table
- Example request/response
- Error codes
- Rate limits
```

### README Writing
```
Create a README for this project:

Name: TaskRunner
Purpose: CLI tool for running tasks defined in YAML
Main features: Parallel execution, dependency tracking, dry-run mode

Include:
- Badges (build, npm, license)
- Quick start (3 steps)
- Features list
- Installation options
- Basic usage examples
- Configuration reference
- Contributing section
```

---

## Step 4: Refine and Polish

### Ask for Review
```
Review this draft for:
- Clarity: Is anything confusing?
- Flow: Does it read smoothly?
- Engagement: Will readers stay interested?
- Accuracy: Any technical errors?
- Tone: Does it match our audience (developers)?
```

### Specific Improvements
```
This paragraph is too long and dense:
[paste paragraph]

Rewrite it to be:
- Shorter (2-3 sentences max)
- Clearer (one idea per sentence)
- More engaging (add an example)
```

---

## Step 5: Content Adaptation

### Different Audiences
```
I have this technical explanation:
[paste content]

Rewrite it for:
1. A beginner developer (explain all jargon)
2. A senior engineer (skip basics, focus on edge cases)
3. A non-technical manager (focus on benefits, not how)
```

### Different Formats
```
Transform this blog post into:
1. A Twitter thread (10 tweets)
2. A LinkedIn post (professional tone)
3. A Hacker News comment (technical, concise)
4. An email newsletter (personal, scannable)
```

---

## Step 6: Writing Workflows

### Blog Post Workflow
```
1. Brainstorm: "Give me 10 blog ideas about [topic]"
2. Outline: "Create outline for idea #3"
3. Draft: "Write section 1 in conversational style"
4. Review: "Review and suggest improvements"
5. Polish: "Check for typos, improve clarity"
6. Meta: "Write SEO description and social preview"
```

### Documentation Workflow
```
1. Structure: "Outline docs for [feature]"
2. Content: "Write installation section"
3. Examples: "Add code examples for each section"
4. Review: "Check technical accuracy"
5. Links: "Add cross-references and links"
```

---

## Verification Checklist

- [ ] Created an outline for content
- [ ] Drafted at least one section collaboratively
- [ ] Refined content based on Claude's feedback
- [ ] Adapted content for different audiences
- [ ] Completed a full writing workflow

---

## Writing Prompts Reference

| Task | Prompt Start |
|------|--------------|
| Brainstorm | "Give me 10 ideas for..." |
| Outline | "Create an outline for..." |
| Draft | "Write a draft of... in [style]" |
| Review | "Review this for clarity and..." |
| Refine | "Rewrite this to be more..." |
| Adapt | "Rewrite this for [audience]" |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Content too generic | Be specific about audience and style |
| Lost your voice | Provide examples of your preferred style |
| Too verbose | Set word limits |
| Inaccurate | Always verify technical claims |

---

## Pro Tips

1. **Your Voice:** Share examples of writing you like
2. **Iterate:** Multiple passes beat single drafts
3. **Verify:** Always fact-check Claude's technical claims
4. **Mix Modes:** Outline with Claude, draft yourself, refine with Claude

---

## Next Challenge

Continue to **[Markdown Mastery](./02-markdown-mastery.md)** for the universal format!
