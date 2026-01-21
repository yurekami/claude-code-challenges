# Challenge: Refactor Safely

**Difficulty:** Medium
**Category:** File Operations + Git Mastery
**Points:** 150
**Time Limit:** 20 minutes

## Description

Refactoring across multiple files requires careful coordination. This challenge tests your ability to make consistent changes while maintaining git safety.

## Objectives

1. Rename a function across the entire codebase
2. Update all imports and references
3. Ensure no broken references remain
4. Create atomic commits for the changes

## The Refactoring Task

Rename the function `getUserData` to `fetchUserProfile` across the codebase.

This function is:
- Defined in `src/api/users.ts`
- Imported in 5 other files
- Called 12 times total
- Has TypeScript types referencing it

## Constraints

- Use Claude Code tools (Edit, Grep, Glob)
- Do NOT manually rewrite files
- All changes must be atomic (work together or not at all)
- Must verify no broken references after refactoring
- Create a meaningful commit

## Refactoring Steps

1. **Find all occurrences**
   - Use Grep to find all `getUserData` references
   - Document file:line for each

2. **Rename the definition**
   - Edit the function declaration in users.ts
   - Update the export statement

3. **Update all imports**
   - Edit each file that imports the function
   - Use `replace_all: true` where safe

4. **Update all call sites**
   - Edit each function call
   - Verify parameter names unchanged

5. **Verify completeness**
   - Grep for any remaining `getUserData`
   - Should return 0 results

## Expected Output

1. All files updated with new function name
2. `refactor_report.md` documenting:
   - Files changed
   - Number of replacements per file
   - Verification results
3. Git commit with changes

## Example Edit for Rename

```
file_path: "src/api/users.ts"
old_string: "export async function getUserData(userId: string)"
new_string: "export async function fetchUserProfile(userId: string)"
```

## Scoring

| Criteria | Points |
|----------|--------|
| Definition renamed | 20 |
| All imports updated | 25 |
| All call sites updated | 25 |
| No broken references | 30 |
| Atomic git commit | 25 |
| Report complete | 25 |

## Common Pitfalls

1. **Missing occurrences**: Some files use dynamic imports
2. **Partial renames**: Function renamed but type not updated
3. **String references**: Function name in strings/comments
4. **Test files**: Often forgotten in refactoring

## Verification Checklist

- [ ] `grep "getUserData"` returns 0 results
- [ ] `grep "fetchUserProfile"` finds the definition
- [ ] TypeScript compiles without errors
- [ ] All tests pass (if applicable)

## Hints

1. Use Grep with `output_mode: "content"` to see context
2. The `-n` flag shows line numbers
3. Check `.test.ts` and `.spec.ts` files too
4. Types might reference the function name

## Verification

Run `python tests.py` to check your refactoring.
