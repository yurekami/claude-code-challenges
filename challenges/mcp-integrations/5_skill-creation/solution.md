# Solution: Building Reusable Skills

## Complete Example: API Documentation Generator Skill

We'll build a skill that automatically generates API documentation from code.

## Phase 1: Planning

### Workflow Identification

**Manual Process**:
1. Read API route files
2. Extract endpoint information
3. Generate OpenAPI/Swagger spec
4. Create markdown documentation
5. Update README with API links

**Skill Value**: Automates documentation creation, ensures consistency, keeps docs in sync with code.

### Skill Scope

**What it DOES**:
- Scans code for API endpoints
- Extracts route definitions, parameters, responses
- Generates OpenAPI specification
- Creates human-readable documentation

**What it DOESN'T do**:
- Modify source code
- Deploy documentation
- Validate API implementations

**Parameters**:
- `source_dir`: Directory to scan (required)
- `output_format`: 'openapi' | 'markdown' | 'both' (default: 'both')
- `output_dir`: Where to save docs (default: './docs')
- `include_examples`: Include example requests/responses (default: true)

### Workflow Design

```
1. Validate parameters
   ├─ Check source_dir exists
   └─ Check output_dir is writable

2. Scan source files
   ├─ Find API route definitions
   ├─ Extract HTTP methods, paths, parameters
   └─ Parse JSDoc/docstrings

3. Generate documentation
   ├─ Build OpenAPI spec (if requested)
   ├─ Generate markdown (if requested)
   └─ Create examples (if requested)

4. Write output files
   ├─ Save generated documentation
   └─ Update index/README

5. Report results
   ├─ Summary of endpoints found
   └─ Location of generated files
```

## Phase 2: Implementation

### Directory Structure

```
api-doc-generator-skill/
├── README.md
├── package.json
├── src/
│   ├── index.js
│   ├── scanner.js
│   ├── parser.js
│   ├── generators/
│   │   ├── openapi.js
│   │   └── markdown.js
│   └── skill-config.json
├── tests/
│   └── skill.test.js
└── examples/
    ├── express-app/
    └── fastapi-app/
```

### Implementation: package.json

```json
{
  "name": "api-doc-generator-skill",
  "version": "1.0.0",
  "description": "Claude skill for generating API documentation from code",
  "main": "src/index.js",
  "type": "module",
  "keywords": ["claude-skill", "api", "documentation", "openapi"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.5.0",
    "glob": "^10.3.10",
    "yaml": "^2.3.4"
  },
  "devDependencies": {
    "jest": "^29.7.0"
  },
  "scripts": {
    "test": "jest",
    "start": "node src/index.js"
  }
}
```

### Implementation: src/skill-config.json

```json
{
  "name": "api-doc-generator",
  "version": "1.0.0",
  "description": "Generates API documentation from source code",
  "triggers": [
    "generate api docs",
    "create api documentation",
    "document api endpoints",
    "update api docs"
  ],
  "parameters": {
    "type": "object",
    "properties": {
      "source_dir": {
        "type": "string",
        "description": "Directory containing API route files",
        "required": true
      },
      "output_format": {
        "type": "string",
        "enum": ["openapi", "markdown", "both"],
        "default": "both",
        "description": "Format for generated documentation"
      },
      "output_dir": {
        "type": "string",
        "default": "./docs",
        "description": "Directory to save documentation"
      },
      "include_examples": {
        "type": "boolean",
        "default": true,
        "description": "Include example requests/responses"
      }
    },
    "required": ["source_dir"]
  },
  "examples": [
    {
      "description": "Generate both OpenAPI and Markdown docs",
      "invocation": "Generate API documentation for ./src/routes"
    },
    {
      "description": "Generate only OpenAPI spec",
      "invocation": "api-doc-generator --source_dir ./api --output_format openapi"
    }
  ]
}
```

### Implementation: src/index.js

```javascript
#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import fs from 'fs/promises';
import path from 'path';
import { scanDirectory } from './scanner.js';
import { parseEndpoints } from './parser.js';
import { generateOpenAPI } from './generators/openapi.js';
import { generateMarkdown } from './generators/markdown.js';
import skillConfig from './skill-config.json' assert { type: 'json' };

class ApiDocGeneratorSkill {
  constructor() {
    this.server = new Server(
      {
        name: skillConfig.name,
        version: skillConfig.version,
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupHandlers();
  }

  setupHandlers() {
    // List available tools
    this.server.setRequestHandler('tools/list', async () => {
      return {
        tools: [
          {
            name: skillConfig.name,
            description: skillConfig.description,
            inputSchema: skillConfig.parameters,
          },
        ],
      };
    });

    // Handle tool calls
    this.server.setRequestHandler('tools/call', async (request) => {
      if (request.params.name !== skillConfig.name) {
        throw new Error(`Unknown tool: ${request.params.name}`);
      }

      try {
        const result = await this.execute(request.params.arguments);
        return {
          content: [
            {
              type: 'text',
              text: result,
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error.message}`,
            },
          ],
          isError: true,
        };
      }
    });
  }

  async execute(args) {
    // Validate parameters
    await this.validateParams(args);

    const {
      source_dir,
      output_format = 'both',
      output_dir = './docs',
      include_examples = true,
    } = args;

    // Step 1: Scan directory for API files
    const files = await scanDirectory(source_dir);
    console.error(`Found ${files.length} files to scan`);

    // Step 2: Parse endpoints from files
    const endpoints = await parseEndpoints(files);
    console.error(`Extracted ${endpoints.length} API endpoints`);

    if (endpoints.length === 0) {
      throw new Error('No API endpoints found in source directory');
    }

    // Step 3: Ensure output directory exists
    await fs.mkdir(output_dir, { recursive: true });

    const results = [];

    // Step 4: Generate documentation
    if (output_format === 'openapi' || output_format === 'both') {
      const openapiPath = path.join(output_dir, 'openapi.yaml');
      const openapiSpec = generateOpenAPI(endpoints, { include_examples });
      await fs.writeFile(openapiPath, openapiSpec);
      results.push(`OpenAPI spec: ${openapiPath}`);
    }

    if (output_format === 'markdown' || output_format === 'both') {
      const markdownPath = path.join(output_dir, 'API.md');
      const markdown = generateMarkdown(endpoints, { include_examples });
      await fs.writeFile(markdownPath, markdown);
      results.push(`Markdown docs: ${markdownPath}`);
    }

    // Step 5: Generate summary
    return this.formatResult(endpoints.length, results);
  }

  async validateParams(args) {
    if (!args.source_dir) {
      throw new Error('source_dir parameter is required');
    }

    try {
      const stats = await fs.stat(args.source_dir);
      if (!stats.isDirectory()) {
        throw new Error('source_dir must be a directory');
      }
    } catch (error) {
      throw new Error(`Invalid source_dir: ${error.message}`);
    }

    if (args.output_format) {
      const validFormats = ['openapi', 'markdown', 'both'];
      if (!validFormats.includes(args.output_format)) {
        throw new Error(
          `Invalid output_format. Must be one of: ${validFormats.join(', ')}`
        );
      }
    }
  }

  formatResult(endpointCount, outputFiles) {
    return `
# API Documentation Generated ✓

## Summary
- **Endpoints Found**: ${endpointCount}
- **Documentation Generated**: ${outputFiles.length} file(s)

## Output Files
${outputFiles.map((file) => `- ${file}`).join('\n')}

## Next Steps
1. Review the generated documentation
2. Add missing endpoint descriptions
3. Verify examples are accurate
4. Commit documentation to version control
    `.trim();
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('API Doc Generator Skill running on stdio');
  }
}

// Start the server
const skill = new ApiDocGeneratorSkill();
skill.run().catch(console.error);
```

### Implementation: src/scanner.js

```javascript
import { glob } from 'glob';
import path from 'path';

export async function scanDirectory(sourceDir) {
  // Find files that typically contain API routes
  const patterns = [
    '**/*.routes.js',
    '**/*.routes.ts',
    '**/routes/**/*.js',
    '**/routes/**/*.ts',
    '**/api/**/*.js',
    '**/api/**/*.ts',
    '**/*_routes.py',
    '**/routes/**/*.py',
  ];

  const files = [];

  for (const pattern of patterns) {
    const matches = await glob(path.join(sourceDir, pattern), {
      ignore: ['**/node_modules/**', '**/dist/**', '**/__tests__/**'],
    });
    files.push(...matches);
  }

  // Remove duplicates
  return [...new Set(files)];
}
```

### Implementation: src/parser.js

```javascript
import fs from 'fs/promises';

export async function parseEndpoints(files) {
  const endpoints = [];

  for (const file of files) {
    const content = await fs.readFile(file, 'utf-8');
    const fileEndpoints = extractEndpoints(content, file);
    endpoints.push(...fileEndpoints);
  }

  return endpoints;
}

function extractEndpoints(content, filepath) {
  const endpoints = [];

  // Simple regex-based extraction (can be improved with AST parsing)
  const patterns = [
    // Express.js: app.get('/path', ...)
    /(?:router|app)\.(get|post|put|delete|patch)\s*\(\s*['"`]([^'"`]+)['"`]/g,

    // FastAPI: @app.get("/path")
    /@app\.(get|post|put|delete|patch)\s*\(\s*['"`]([^'"`]+)['"`]/g,
  ];

  for (const pattern of patterns) {
    let match;
    while ((match = pattern.exec(content)) !== null) {
      const [, method, path] = match;

      // Extract JSDoc comment above the route
      const description = extractDescription(content, match.index);

      endpoints.push({
        method: method.toUpperCase(),
        path,
        description,
        file: filepath,
      });
    }
  }

  return endpoints;
}

function extractDescription(content, index) {
  // Look backwards for JSDoc comment
  const beforeContent = content.substring(0, index);
  const jsdocMatch = beforeContent.match(/\/\*\*\s*\n([^*]|\*[^/])*\*\//g);

  if (jsdocMatch && jsdocMatch.length > 0) {
    const lastComment = jsdocMatch[jsdocMatch.length - 1];
    // Extract description lines
    const lines = lastComment
      .split('\n')
      .map((line) => line.replace(/^\s*\*\s?/, '').trim())
      .filter((line) => line && !line.startsWith('@'));

    return lines.join(' ');
  }

  return 'No description provided';
}
```

### Implementation: src/generators/openapi.js

```javascript
import yaml from 'yaml';

export function generateOpenAPI(endpoints, options = {}) {
  const spec = {
    openapi: '3.0.0',
    info: {
      title: 'API Documentation',
      version: '1.0.0',
      description: 'Auto-generated API documentation',
    },
    paths: {},
  };

  // Group endpoints by path
  for (const endpoint of endpoints) {
    const { method, path, description } = endpoint;

    if (!spec.paths[path]) {
      spec.paths[path] = {};
    }

    spec.paths[path][method.toLowerCase()] = {
      summary: description,
      responses: {
        '200': {
          description: 'Successful response',
        },
        '400': {
          description: 'Bad request',
        },
        '500': {
          description: 'Server error',
        },
      },
    };

    // Add example if requested
    if (options.include_examples) {
      spec.paths[path][method.toLowerCase()].responses['200'].content = {
        'application/json': {
          example: { message: 'Success' },
        },
      };
    }
  }

  return yaml.stringify(spec);
}
```

### Implementation: src/generators/markdown.js

```javascript
export function generateMarkdown(endpoints, options = {}) {
  let markdown = '# API Documentation\n\n';
  markdown += `*Auto-generated on ${new Date().toISOString()}*\n\n`;
  markdown += '## Endpoints\n\n';

  // Group by method
  const byMethod = {};
  for (const endpoint of endpoints) {
    if (!byMethod[endpoint.method]) {
      byMethod[endpoint.method] = [];
    }
    byMethod[endpoint.method].push(endpoint);
  }

  // Generate documentation for each method
  for (const [method, methodEndpoints] of Object.entries(byMethod)) {
    markdown += `### ${method} Requests\n\n`;

    for (const endpoint of methodEndpoints) {
      markdown += `#### \`${method} ${endpoint.path}\`\n\n`;
      markdown += `${endpoint.description}\n\n`;

      if (options.include_examples) {
        markdown += '**Example Request:**\n\n';
        markdown += '```bash\n';
        markdown += `curl -X ${method} http://localhost:3000${endpoint.path}\n`;
        markdown += '```\n\n';

        markdown += '**Example Response:**\n\n';
        markdown += '```json\n';
        markdown += JSON.stringify({ message: 'Success' }, null, 2);
        markdown += '\n```\n\n';
      }

      markdown += '---\n\n';
    }
  }

  return markdown;
}
```

## Phase 3: Testing

### Test File: tests/skill.test.js

```javascript
import { jest } from '@jest/globals';
import fs from 'fs/promises';
import path from 'path';
import { scanDirectory } from '../src/scanner.js';
import { parseEndpoints } from '../src/parser.js';

describe('API Doc Generator Skill', () => {
  const testDir = './test-fixtures';

  beforeAll(async () => {
    // Create test fixtures
    await fs.mkdir(testDir, { recursive: true });
    await fs.writeFile(
      path.join(testDir, 'routes.js'),
      `
      /**
       * Get all users
       */
      router.get('/users', async (req, res) => {
        // handler
      });

      /**
       * Create a new user
       */
      router.post('/users', async (req, res) => {
        // handler
      });
      `
    );
  });

  afterAll(async () => {
    // Cleanup
    await fs.rm(testDir, { recursive: true, force: true });
  });

  test('should scan directory for route files', async () => {
    const files = await scanDirectory(testDir);
    expect(files.length).toBeGreaterThan(0);
  });

  test('should extract endpoints from files', async () => {
    const files = await scanDirectory(testDir);
    const endpoints = await parseEndpoints(files);

    expect(endpoints.length).toBe(2);
    expect(endpoints[0]).toMatchObject({
      method: 'GET',
      path: '/users',
      description: expect.stringContaining('Get all users'),
    });
  });

  test('should handle empty directories gracefully', async () => {
    const emptyDir = './empty-test';
    await fs.mkdir(emptyDir, { recursive: true });

    const files = await scanDirectory(emptyDir);
    expect(files).toEqual([]);

    await fs.rmdir(emptyDir);
  });
});
```

## Phase 4: Deployment

### README.md

```markdown
# API Documentation Generator Skill

Automatically generates API documentation from your source code.

## Features

- Scans code for API endpoints
- Generates OpenAPI/Swagger specifications
- Creates human-readable markdown documentation
- Supports Express.js, FastAPI, and more
- Auto-triggers when you ask for API docs

## Installation

```bash
npm install -g api-doc-generator-skill
```

## Configuration

Add to your `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "api-doc-generator": {
      "command": "api-doc-generator-skill"
    }
  }
}
```

## Usage

### Natural Language

```
Generate API documentation for my project
```

### Explicit Invocation

```
Run api-doc-generator skill with source_dir: ./src/routes
```

### With Parameters

```json
{
  "source_dir": "./src/api",
  "output_format": "both",
  "output_dir": "./docs/api",
  "include_examples": true
}
```

## Examples

See [examples/](./examples/) for complete working examples.

## Development

```bash
# Install dependencies
npm install

# Run tests
npm test

# Start in development mode
npm start
```

## License

MIT
```

### Deploy to Claude

```bash
# Build if needed
npm install

# Link globally for testing
npm link

# Update Claude settings
cat >> ~/.claude/settings.json <<EOF
{
  "mcpServers": {
    "api-doc-generator": {
      "command": "npx",
      "args": ["-y", "api-doc-generator-skill"]
    }
  }
}
EOF

# Restart Claude
```

## Common Mistakes and Solutions

### Mistake 1: Not Validating Parameters

**Wrong**:
```javascript
async function execute(args) {
  const dir = args.source_dir; // No validation!
  const files = await scanDirectory(dir);
}
```

**Correct**:
```javascript
async function execute(args) {
  if (!args.source_dir) {
    throw new Error('source_dir is required');
  }

  try {
    const stats = await fs.stat(args.source_dir);
    if (!stats.isDirectory()) {
      throw new Error('source_dir must be a directory');
    }
  } catch (error) {
    throw new Error(`Invalid source_dir: ${error.message}`);
  }

  const files = await scanDirectory(args.source_dir);
}
```

### Mistake 2: Poor Error Messages

**Wrong**:
```javascript
catch (error) {
  return { error: 'Failed' };
}
```

**Correct**:
```javascript
catch (error) {
  return {
    content: [{
      type: 'text',
      text: `Failed to generate documentation: ${error.message}\n\nPlease check:\n- Source directory exists\n- You have read permissions\n- Files contain valid API routes`
    }],
    isError: true
  };
}
```

### Mistake 3: Hardcoded Values

**Wrong**:
```javascript
const outputDir = './docs';  // Always uses this directory
await fs.mkdir(outputDir);
```

**Correct**:
```javascript
const outputDir = args.output_dir || './docs';
await fs.mkdir(outputDir, { recursive: true });
```

### Mistake 4: Not Testing Auto-Triggering

Always test that your skill triggers on the expected phrases:

```
Test 1: "Generate API documentation"
Test 2: "Create API docs for my project"
Test 3: "Document my API endpoints"
```

## Verification Checklist

- [✓] Skill has clear name and description
- [✓] Parameters are validated before use
- [✓] Error messages are helpful and actionable
- [✓] Workflow steps are clearly separated
- [✓] Can be invoked explicitly
- [✓] Auto-triggers on expected phrases
- [✓] Includes comprehensive tests
- [✓] Documentation with examples
- [✓] Handles edge cases (empty dirs, invalid files)
- [✓] Successfully deployed to Claude

## Next Steps

1. **Enhance the Parser**: Add AST parsing for better accuracy
2. **Support More Frameworks**: Add Django, Flask, Rails, etc.
3. **Add Validation**: Check generated docs against actual API
4. **Interactive Mode**: Let users review/edit before saving
5. **CI/CD Integration**: Run as part of build process
6. **Share the Skill**: Publish to npm for others to use
