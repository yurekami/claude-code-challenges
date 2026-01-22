# Walkthrough: Output Extraction

**Difficulty:** Easy | **Time:** 12 minutes | **Category:** CLI Fundamentals

---

## Overview

Claude generates valuable outputs: code, configurations, documentation, and data. This challenge teaches you to efficiently extract and use these outputs - copying code, exporting files, and integrating Claude's work into your projects.

## Prerequisites

- [ ] Claude Code CLI operational
- [ ] Understanding of file operations
- [ ] Clipboard access in your terminal

---

## Step 1: Direct Code Generation to Files

Instead of copying/pasting, have Claude write directly:

**Approach 1: Explicit File Writing**
```
Create a utility file at src/utils/format.ts with functions for:
- formatCurrency
- formatDate
- formatPhoneNumber
```

**Claude uses the Write tool to create the file directly.**

**Approach 2: Specific Path Request**
```
Write the following to ./config/database.json:
{
  "host": "localhost",
  "port": 5432
}
```

---

## Step 2: Extract Code Blocks

When Claude shows code in the conversation, extract it:

**Method 1: Direct Request**
```
Take the formatCurrency function you just showed and add it to src/utils/money.ts
```

**Method 2: Reference by Description**
```
Save that last code block to a new file called helpers.ts
```

---

## Step 3: Batch Extraction

Extract multiple outputs at once:

```
From our conversation, extract and save:
1. The API types to src/types/api.ts
2. The validation schema to src/schemas/user.ts
3. The test cases to tests/user.test.ts
```

Claude will create all three files with the relevant content.

---

## Step 4: Structured Data Export

Export data in specific formats:

### JSON Export
```
Export the user schema we discussed as a JSON file at schemas/user.json
```

### CSV Export
```
Take the test results and export them as CSV to reports/test-results.csv
```

### Markdown Export
```
Create a markdown document summarizing our API design at docs/api-design.md
```

---

## Step 5: Selective Extraction

Extract specific portions:

```
From the component we built, extract only:
- The TypeScript interfaces (save to types.ts)
- The utility functions (save to utils.ts)
- Keep the React component in component.tsx
```

---

## Step 6: Template Extraction

Create reusable templates:

```
Take this component and create a template at templates/component.tsx.template
that I can use to generate similar components
```

**Result:**
```typescript
// templates/component.tsx.template
import React from 'react';

interface {{ComponentName}}Props {
  {{props}}
}

export function {{ComponentName}}({ {{destructuredProps}} }: {{ComponentName}}Props) {
  return (
    <div className="{{className}}">
      {{content}}
    </div>
  );
}
```

---

## Step 7: Documentation Extraction

Generate documentation from conversation:

```
Based on our discussion about the auth module, create:
1. README.md with usage instructions
2. CHANGELOG.md with version history
3. API.md with endpoint documentation
```

---

## Verification Checklist

- [ ] Had Claude write code directly to a file
- [ ] Extracted a code block from conversation to a file
- [ ] Performed batch extraction (3+ files)
- [ ] Exported data in a specific format (JSON/CSV/MD)
- [ ] Created a reusable template

---

## Common Patterns

### Extract and Organize
```
Organize the code from this session:
- Types → src/types/
- Utils → src/utils/
- Components → src/components/
- Tests → tests/
```

### Extract with Modifications
```
Take the UserService class and:
1. Save it to src/services/user.ts
2. Add error handling to each method
3. Add JSDoc comments
```

### Extract and Test
```
Save the validation function to src/validate.ts and create a test file
at tests/validate.test.ts with comprehensive test cases
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Code extracted to wrong location | Be explicit about paths: "save to ./src/utils/file.ts" |
| Partial extraction | Request "the complete function including imports" |
| Formatting lost | Specify format: "preserve TypeScript formatting" |
| File overwritten accidentally | Ask Claude to check if file exists first |

---

## Pro Tips

1. **Incremental Saving:** Save code as you develop rather than at the end
2. **Path Conventions:** Establish patterns: "always use src/ for source files"
3. **Verify Extraction:** Ask Claude to read back the file after saving
4. **Bulk Operations:** Group related extractions in single requests

---

## Advanced Extraction

### Extract with Transformations
```
Take the JavaScript module and save it as TypeScript to src/utils/helpers.ts,
adding proper type annotations
```

### Extract to Multiple Formats
```
Save the API documentation as:
- OpenAPI spec at api/openapi.yaml
- Markdown at docs/API.md
- TypeScript types at src/types/api.ts
```

### Extract with Version Control
```
Save the updated config to config/app.json and commit with message
"chore: Update application configuration"
```

---

## Output Types Reference

| Output Type | Best Extraction Method |
|-------------|----------------------|
| Code files | Direct Write tool |
| Configuration | JSON export |
| Documentation | Markdown files |
| Data/Reports | CSV or JSON |
| Templates | Template files with placeholders |
| Schemas | Dedicated schema files |

---

## Next Challenge

Continue to **[Terminal Aliases](./08-terminal-aliases.md)** to speed up your daily commands!
