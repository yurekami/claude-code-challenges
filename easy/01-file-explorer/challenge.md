# Challenge: File Explorer

**Difficulty:** Easy
**Category:** File Operations
**Points:** 100
**Time Limit:** 10 minutes

## Description

You are given a project directory with a nested file structure. Your task is to use Claude Code's file exploration tools to find specific files and extract information from them.

## Objectives

1. Find all TypeScript files (`.ts`) in the project
2. Locate the file containing the function `calculateTotal`
3. Read the contents of `config/database.json`
4. Count the total number of lines in `src/utils/helpers.ts`

## Constraints

- Use only Claude Code tools (Glob, Read, Grep)
- Do NOT use bash commands like `find`, `cat`, or `wc`
- Complete all objectives in a single Claude Code session

## Input

The `starter/` directory contains a sample project structure.

## Expected Output

Create a file `results.json` with the following format:

```json
{
  "typescript_files": ["path/to/file1.ts", "path/to/file2.ts"],
  "calculateTotal_location": "src/utils/math.ts:42",
  "database_config": { "host": "...", "port": ... },
  "helpers_line_count": 156
}
```

## Examples

### Finding TypeScript Files
```
User: Find all .ts files in the project
Claude: [Uses Glob tool with pattern "**/*.ts"]
```

### Locating a Function
```
User: Find where calculateTotal is defined
Claude: [Uses Grep tool with pattern "function calculateTotal"]
```

## Scoring

| Criteria | Points |
|----------|--------|
| All TypeScript files found | 25 |
| calculateTotal location correct | 25 |
| Database config extracted | 25 |
| Line count accurate | 25 |

## Hints

1. Use `Glob` with `**/*.ts` pattern for recursive TypeScript search
2. Use `Grep` with output_mode "content" to see line numbers
3. The `Read` tool returns line numbers - count them!
4. Parse JSON files with the Read tool - they're text files

## Verification

Run `python tests.py` to check your solution.
