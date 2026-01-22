# Solution: Custom CLAUDE.md Configuration

## Step-by-Step Solution

### Step 1: Decide on Configuration Scope

**Global Configuration** (`~/.claude/CLAUDE.md`):
- Applies to all projects
- General coding preferences
- Universal workflows

**Project-Specific Configuration** (`.claude/CLAUDE.md`):
- Overrides global settings
- Project-specific rules
- Tech stack conventions

**Modular Rules** (`~/.claude/rules/*.md`):
- Organized by topic
- Easy to maintain
- Reusable across projects

### Step 2: Create the Directory Structure

```bash
# For global configuration
mkdir -p ~/.claude/rules

# For project-specific configuration
mkdir -p .claude
```

### Step 3: Start with a Template

Create `~/.claude/CLAUDE.md` with this template:

```markdown
# Claude Code Configuration

## Role and Behavior

You are a senior software engineer with expertise in [your preferred languages/frameworks].
You write clean, maintainable code following industry best practices.

## Coding Style (CRITICAL)

### Immutability
ALWAYS create new objects, NEVER mutate:

```javascript
// WRONG: Mutation
function updateUser(user, name) {
  user.name = name  // MUTATION!
  return user
}

// CORRECT: Immutability
function updateUser(user, name) {
  return { ...user, name }
}
```

### File Organization
- MANY SMALL FILES > FEW LARGE FILES
- High cohesion, low coupling
- 200-400 lines typical, 800 max
- Extract utilities from large components

### Naming Conventions
- Variables: camelCase
- Constants: UPPER_SNAKE_CASE
- Classes: PascalCase
- Files: kebab-case
- Be descriptive, avoid abbreviations

## Testing Requirements (NON-NEGOTIABLE)

### Minimum Coverage: 80%

Test Types (ALL required):
1. **Unit Tests** - Individual functions, components
2. **Integration Tests** - API endpoints, database operations
3. **E2E Tests** - Critical user flows

### TDD Workflow
1. Write test first (RED)
2. Run test - it should FAIL
3. Write minimal implementation (GREEN)
4. Run test - it should PASS
5. Refactor (IMPROVE)
6. Verify coverage

## Git Workflow

### Commit Message Format
```
<type>: <description>

<optional body>
```

Types: feat, fix, refactor, docs, test, chore, perf, ci

### Pull Request Process
1. Analyze full commit history
2. Use `git diff [base-branch]...HEAD` for all changes
3. Draft comprehensive PR summary
4. Include test plan with TODOs
5. Push with `-u` flag if new branch

## Security Guidelines

### Mandatory Security Checks
Before ANY commit:
- [ ] No hardcoded secrets
- [ ] All user inputs validated
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection enabled
- [ ] Authentication/authorization verified
- [ ] Rate limiting on endpoints
- [ ] Error messages don't leak sensitive data

### Secret Management
```typescript
// NEVER: Hardcoded secrets
const apiKey = "sk-proj-xxxxx"

// ALWAYS: Environment variables
const apiKey = process.env.API_KEY
if (!apiKey) throw new Error('API_KEY not configured')
```

## Error Handling

ALWAYS handle errors comprehensively:

```typescript
try {
  const result = await riskyOperation()
  return result
} catch (error) {
  console.error('Operation failed:', error)
  throw new Error('Detailed user-friendly message')
}
```

## Input Validation

ALWAYS validate user input:

```typescript
import { z } from 'zod'

const schema = z.object({
  email: z.string().email(),
  age: z.number().int().min(0).max(150)
})

const validated = schema.parse(input)
```

## Agent Orchestration

### Available Agents
- **planner** - Complex features, refactoring
- **architect** - System design decisions
- **tdd-guide** - Test-driven development
- **code-reviewer** - Code review
- **security-reviewer** - Security analysis

### When to Use Agents
- Complex feature requests → **planner**
- Code just written → **code-reviewer**
- Bug fix or new feature → **tdd-guide**
- Architectural decision → **architect**

## Performance Guidelines

### Model Selection
- **Haiku 4.5** - Lightweight tasks, frequent invocation
- **Sonnet 4.5** - Main development work
- **Opus 4.5** - Complex architectural decisions

### Context Management
- Avoid last 20% of context window for large refactors
- Use smaller contexts for single-file edits
- Extract utilities to reduce file sizes

## Communication Style

- Start immediately, no acknowledgments
- Match user's communication style
- Dense > verbose
- No emojis unless explicitly requested
- Provide code snippets and file paths

## Tool Usage

### TodoWrite Discipline
- 2+ steps → TodoWrite FIRST
- Mark in_progress before starting (ONE at a time)
- Mark completed IMMEDIATELY after each step
- NEVER batch completions

### Verification
Task NOT complete without:
- LSP diagnostics clean
- Build passes
- All todos marked completed

## Code Quality Checklist

Before marking work complete:
- [ ] Code is readable and well-named
- [ ] Functions are small (<50 lines)
- [ ] Files are focused (<800 lines)
- [ ] No deep nesting (>4 levels)
- [ ] Proper error handling
- [ ] No console.log statements
- [ ] No hardcoded values
- [ ] Immutability maintained
```

### Step 4: Create Modular Rule Files

Create `~/.claude/rules/coding-style.md`:

```markdown
# Coding Style

## Immutability (CRITICAL)

ALWAYS create new objects, NEVER mutate:

```javascript
// WRONG: Mutation
function updateUser(user, name) {
  user.name = name
  return user
}

// CORRECT: Immutability
function updateUser(user, name) {
  return { ...user, name }
}
```

## File Organization

- MANY SMALL FILES > FEW LARGE FILES
- High cohesion, low coupling
- 200-400 lines typical, 800 max
- Extract utilities from large components
- Organize by feature/domain, not by type

## Code Quality Checklist

- [ ] Code is readable and well-named
- [ ] Functions are small (<50 lines)
- [ ] Files are focused (<800 lines)
- [ ] No deep nesting (>4 levels)
- [ ] Proper error handling
- [ ] No console.log statements
- [ ] No hardcoded values
- [ ] Immutability maintained
```

Create `~/.claude/rules/testing.md`:

```markdown
# Testing Requirements

## Minimum Test Coverage: 80%

Test Types (ALL required):
1. **Unit Tests** - Individual functions, components
2. **Integration Tests** - API endpoints, database operations
3. **E2E Tests** - Critical user flows

## TDD Workflow (MANDATORY)

1. Write test first (RED)
2. Run test - it should FAIL
3. Write minimal implementation (GREEN)
4. Run test - it should PASS
5. Refactor (IMPROVE)
6. Verify coverage (80%+)

## Agent Support

- **tdd-guide** - Use PROACTIVELY for new features
- **e2e-runner** - Playwright E2E testing specialist
```

### Step 5: Create Project-Specific Configuration

For a React project, create `.claude/CLAUDE.md`:

```markdown
# Project: MyApp - React Application

## Tech Stack

- **Frontend**: React 18, TypeScript, Tailwind CSS
- **State Management**: Zustand
- **Data Fetching**: React Query
- **Testing**: Jest, React Testing Library, Playwright
- **Build**: Vite

## Architecture

- Feature-based folder structure
- Hooks in `src/hooks/`
- Components in `src/components/`
- Pages in `src/pages/`
- Utils in `src/utils/`

## React-Specific Rules

### Component Structure
```typescript
// Functional components only, no class components
export function MyComponent({ prop1, prop2 }: Props) {
  // 1. Hooks
  const [state, setState] = useState()
  const data = useQuery()

  // 2. Derived values
  const computed = useMemo(() => ..., [])

  // 3. Effects
  useEffect(() => { ... }, [])

  // 4. Event handlers
  const handleClick = useCallback(() => { ... }, [])

  // 5. Render
  return <div>...</div>
}
```

### State Management
- Use Zustand for global state
- Use React Query for server state
- Use local state for UI-only state
- NEVER mutate state directly

### Performance
- Use React.memo for expensive components
- Use useMemo for expensive computations
- Use useCallback for stable function references
- Lazy load routes with React.lazy

## Project Commands

```bash
# Development
npm run dev

# Testing
npm run test
npm run test:e2e
npm run test:coverage

# Build
npm run build
npm run preview

# Linting
npm run lint
npm run format
```

## Common Patterns

### API Response Handling
```typescript
interface ApiResponse<T> {
  success: boolean
  data?: T
  error?: string
  meta?: {
    total: number
    page: number
    limit: number
  }
}
```

### Custom Hooks Pattern
```typescript
export function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value)

  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay)
    return () => clearTimeout(handler)
  }, [value, delay])

  return debouncedValue
}
```

## Known Issues

- Avoid using `any` type - use `unknown` and type guards instead
- Don't use `useEffect` for data fetching - use React Query
- Don't store derived values in state - use `useMemo`

## Review Checklist

Before PR:
- [ ] All components have proper TypeScript types
- [ ] No `any` types used
- [ ] Tests written and passing (80%+ coverage)
- [ ] E2E tests for critical flows
- [ ] No console.log statements
- [ ] Accessibility attributes added (aria-*)
- [ ] Loading and error states handled
- [ ] Responsive design verified
```

### Step 6: Test Your Configuration

Start Claude and test if it follows your rules:

```
Can you create a new React component for a user profile card?
```

Claude should now:
- Use functional components
- Follow your naming conventions
- Include TypeScript types
- Write tests first (TDD)
- Handle errors properly
- Use immutable patterns

### Step 7: Iterate and Refine

Monitor Claude's behavior and update your CLAUDE.md:

```markdown
## Learnings (Update Regularly)

### 2024-01-15
- Added rule about avoiding `any` type
- Clarified when to use React.memo
- Added custom hooks pattern

### 2024-01-10
- Fixed testing workflow description
- Added project commands section
- Improved error handling examples
```

## Common Mistakes to Avoid

### 1. Too Vague Instructions

**Wrong**:
```markdown
## Coding Style
- Write good code
- Follow best practices
```

**Correct**:
```markdown
## Coding Style
- Use camelCase for variables
- Maximum 50 lines per function
- Extract magic numbers to constants

Example:
```javascript
// Wrong
function calc(x) { return x * 1.1 }

// Correct
const TAX_RATE = 1.1
function calculateWithTax(amount: number) {
  return amount * TAX_RATE
}
```
```

### 2. Conflicting Instructions

**Wrong**:
```markdown
## Style
- Use verbose variable names for clarity
...
## Performance
- Keep code concise and minimal
```

Make sure instructions don't contradict each other.

### 3. Not Using Examples

**Wrong**:
```markdown
- Handle errors properly
```

**Correct**:
```markdown
- Handle errors properly

Example:
```typescript
try {
  const result = await riskyOperation()
  return result
} catch (error) {
  console.error('Operation failed:', error)
  throw new Error('User-friendly message')
}
```
```

### 4. Overloading One File

Instead of a massive CLAUDE.md:
```
~/.claude/
  CLAUDE.md          # Main configuration
  rules/
    coding-style.md  # Style rules
    testing.md       # Test requirements
    security.md      # Security guidelines
    git-workflow.md  # Git processes
```

### 5. Not Testing Changes

Always verify:
```
Ask Claude to perform a task that should follow new rules
Observe if the rules are followed
Iterate if needed
```

## Advanced Patterns

### Conditional Rules

```markdown
## Project Type Detection

If working on a React project:
- Use functional components only
- Implement hooks pattern
- Use React Query for data fetching

If working on a Node.js API:
- Use Express.js patterns
- Implement repository pattern
- Use Prisma for database

If working on a Python project:
- Follow PEP 8
- Use type hints
- Implement pytest for testing
```

### Dynamic Context

```markdown
## Context-Aware Responses

When implementing a new feature:
1. Use **planner** agent first
2. Then use **tdd-guide** for implementation
3. Finally use **code-reviewer** for review

When fixing a bug:
1. Write a failing test first
2. Fix the bug
3. Verify test passes
4. Use **code-reviewer** to check for issues

When refactoring:
1. Ensure test coverage exists
2. Use **refactor-cleaner** agent
3. Verify all tests still pass
```

### Project Templates

```markdown
## Starting New Projects

When creating a new [React/Node/Python] project:
1. Copy template from ~/.templates/[project-type]
2. Update package.json with project details
3. Initialize git repository
4. Set up pre-commit hooks
5. Configure CI/CD pipeline
6. Create initial test suite
```

## Verification Checklist

- [ ] CLAUDE.md created in appropriate location
- [ ] Contains clear section headings
- [ ] Includes specific, actionable instructions
- [ ] Has code examples for clarity
- [ ] Defines testing requirements
- [ ] Establishes git workflow
- [ ] Includes security guidelines
- [ ] Specifies error handling patterns
- [ ] Claude follows instructions consistently
- [ ] Instructions reduce repetitive prompting
- [ ] File is maintainable and organized

## Next Steps

1. **Monitor Effectiveness**: Track how often Claude follows your rules
2. **Collect Feedback**: Note when instructions are unclear
3. **Update Regularly**: Add learnings and new patterns
4. **Share Templates**: Create reusable templates for common project types
5. **Version Control**: Commit CLAUDE.md changes to track evolution
6. **Team Collaboration**: Share effective patterns with your team
