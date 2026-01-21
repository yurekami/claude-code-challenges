# Challenge: Search Master

**Difficulty:** Easy
**Category:** File Operations
**Points:** 100
**Time Limit:** 10 minutes

## Description

Efficient codebase navigation requires mastering Claude Code's search tools. Learn to use Grep and Glob to find code patterns across large codebases quickly.

## Objectives

1. Find all files containing `TODO` comments
2. Find all function definitions that are `async`
3. Find all imports from `@/utils`
4. Count occurrences of `console.log` in the codebase

## The Search Tools

### Grep Tool
```
pattern: Regex pattern to search
path: Directory to search in
output_mode: "files_with_matches" | "content" | "count"
type: File type filter (js, ts, py, etc.)
```

### Glob Tool
```
pattern: Glob pattern like "**/*.ts"
path: Starting directory
```

## Constraints

- Use Grep for content searching
- Use Glob for file pattern matching
- Do NOT use bash `grep`, `find`, or `rg` commands
- Report results accurately

## Input

The `starter/` directory contains a sample codebase with various files.

## Expected Output

Create `search_results.json`:

```json
{
  "todo_files": ["path/to/file1.ts", "path/to/file2.ts"],
  "async_functions": [
    {"file": "src/api.ts", "line": 15, "content": "async function fetchData()"},
    {"file": "src/db.ts", "line": 8, "content": "async function connect()"}
  ],
  "util_imports": [
    {"file": "src/index.ts", "line": 3, "content": "import { helper } from '@/utils'"}
  ],
  "console_log_count": 12
}
```

## Examples

### Finding TODOs
```
Grep pattern: "TODO"
output_mode: "files_with_matches"
```

### Finding Async Functions
```
Grep pattern: "async function"
output_mode: "content"
-n: true (show line numbers)
```

### Counting Occurrences
```
Grep pattern: "console\\.log"
output_mode: "count"
```

## Grep Output Modes

| Mode | Returns | Use Case |
|------|---------|----------|
| `files_with_matches` | File paths only | Finding which files contain X |
| `content` | Matching lines | Seeing actual matches |
| `count` | Match counts per file | Statistics |

## Scoring

| Criteria | Points |
|----------|--------|
| TODO files found correctly | 25 |
| Async functions with line numbers | 25 |
| Util imports found | 25 |
| Console.log count accurate | 25 |

## Hints

1. Use `-n: true` to include line numbers in content mode
2. Escape special regex characters (`.` becomes `\\.`)
3. Use `type: "ts"` to filter to TypeScript files
4. Glob is faster for file finding, Grep for content

## Verification

Run `python tests.py` to check your search results.
