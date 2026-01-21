# Challenge: Simple Edit

**Difficulty:** Easy
**Category:** File Operations
**Points:** 100
**Time Limit:** 10 minutes

## Description

Master Claude Code's Edit tool for making precise, targeted changes to files. The Edit tool uses exact string matching to replace content - understanding this is key to efficient code modification.

## Objectives

1. Fix a typo in a variable name
2. Update a function's return type
3. Add a new parameter to a function
4. Change an import statement

## The Edit Tool

```
Edit tool parameters:
- file_path: Absolute path to the file
- old_string: Exact text to replace (must be unique)
- new_string: Replacement text
- replace_all: Replace all occurrences (default: false)
```

## Constraints

- Use ONLY the Edit tool (not Write)
- The `old_string` must be EXACTLY as it appears in the file
- Do NOT rewrite entire files
- Each edit should be minimal and targeted

## Input

The `starter/app.ts` file contains several issues that need fixing:

1. Variable `usrName` should be `userName`
2. Function `getData()` returns `any`, should return `Promise<Data>`
3. Function `processItem(item)` needs a type: `processItem(item: Item)`
4. Import `import { helper }` should be `import { helper, utils }`

## Expected Output

The corrected `app.ts` file with all four issues fixed.

## Examples

### Fixing a Typo
```
old_string: "const usrName = "
new_string: "const userName = "
```

### Updating Return Type
```
old_string: "function getData(): any {"
new_string: "function getData(): Promise<Data> {"
```

## Common Mistakes

1. **Not matching exactly**: Whitespace matters!
   ```
   WRONG: "function getData()"
   RIGHT: "function getData(): any {"
   ```

2. **Changing too much**: Be minimal
   ```
   WRONG: Rewriting the entire function
   RIGHT: Just changing the return type
   ```

3. **Non-unique matches**: Include surrounding context
   ```
   WRONG: "item"  (appears many times)
   RIGHT: "function processItem(item)"
   ```

## Scoring

| Criteria | Points |
|----------|--------|
| Variable name fixed | 25 |
| Return type updated | 25 |
| Parameter type added | 25 |
| Import statement fixed | 25 |

## Hints

1. Read the file first to see exact content
2. Include enough context for unique matches
3. Preserve indentation and formatting
4. Test by reading the file after each edit

## Verification

Run `python tests.py` to check your edits.
