# CI/CD Integration with Claude Code - Solution

## Step-by-Step Solution

### 1. Generate Basic GitHub Actions Pipeline

**Prompt to Claude Code:**
```
Create a GitHub Actions workflow for a Node.js application that:
- Runs on PRs and main branch
- Uses Node.js 20
- Installs dependencies
- Runs linting and tests
- Builds the application
- Caches node_modules
```

**Generated: `.github/workflows/ci.yml`**
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run tests
        run: npm test

      - name: Build application
        run: npm run build

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/
          retention-days: 7
```

### 2. Add Matrix Builds

**Prompt to Claude Code:**
```
Enhance the workflow to test against Node.js 18, 20, and 22.
Also test on ubuntu-latest, windows-latest, and macos-latest.
```

**Enhanced Workflow:**
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ${{ matrix.os }}

    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [18, 20, 22]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

  build:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/
```

### 3. Add Code Coverage

**Prompt to Claude Code:**
```
Add code coverage reporting using codecov.
Generate coverage report and upload to codecov.io.
Add coverage badge to README.
```

**Coverage Job:**
```yaml
  coverage:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests with coverage
        run: npm run test:coverage

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage/lcov.info
          fail_ci_if_error: true
```

### 4. Add Security Scanning

**Prompt to Claude Code:**
```
Add security scanning with:
1. npm audit for dependency vulnerabilities
2. CodeQL for static analysis
3. Snyk for container scanning
```

**Security Jobs:**
```yaml
  security:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Run npm audit
        run: npm audit --audit-level=moderate

      - name: Run Snyk scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  codeql:
    runs-on: ubuntu-latest

    permissions:
      security-events: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: javascript

      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
```

### 5. Deployment Pipeline

**Prompt to Claude Code:**
```
Create a deployment workflow that:
1. Deploys to staging automatically on main branch
2. Requires manual approval for production
3. Uses environment secrets
4. Supports rollback
```

**Deployment Workflow: `.github/workflows/deploy.yml`**
```yaml
name: Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy to'
        required: true
        type: choice
        options:
          - staging
          - production

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    environment:
      name: staging
      url: https://staging.example.com

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build
        env:
          NODE_ENV: staging
          API_URL: ${{ secrets.STAGING_API_URL }}

      - name: Deploy to staging
        run: |
          echo "Deploying to staging..."
          # Replace with actual deployment command
          npm run deploy:staging
        env:
          DEPLOY_TOKEN: ${{ secrets.STAGING_DEPLOY_TOKEN }}

      - name: Run smoke tests
        run: npm run test:smoke
        env:
          TEST_URL: https://staging.example.com

  deploy-production:
    runs-on: ubuntu-latest
    if: github.event_name == 'workflow_dispatch' && github.event.inputs.environment == 'production'
    environment:
      name: production
      url: https://example.com

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build
        env:
          NODE_ENV: production
          API_URL: ${{ secrets.PROD_API_URL }}

      - name: Create deployment
        id: deployment
        uses: actions/github-script@v7
        with:
          script: |
            const deployment = await github.rest.repos.createDeployment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              ref: context.sha,
              environment: 'production',
              required_contexts: []
            });
            return deployment.data.id;

      - name: Deploy to production
        run: |
          echo "Deploying to production..."
          npm run deploy:production
        env:
          DEPLOY_TOKEN: ${{ secrets.PROD_DEPLOY_TOKEN }}

      - name: Update deployment status
        if: always()
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.repos.createDeploymentStatus({
              owner: context.repo.owner,
              repo: context.repo.repo,
              deployment_id: ${{ steps.deployment.outputs.result }},
              state: '${{ job.status }}' === 'success' ? 'success' : 'failure',
              environment_url: 'https://example.com'
            });

      - name: Run smoke tests
        run: npm run test:smoke
        env:
          TEST_URL: https://example.com
```

### 6. Performance Optimization

**Before Optimization:**
```
Total pipeline time: 12 minutes
- Setup: 1 min
- Dependencies: 4 min
- Lint: 1 min
- Tests: 3 min
- Build: 3 min
```

**Prompt to Claude Code:**
```
Optimize this pipeline to run in under 5 minutes using:
1. Better caching
2. Parallel jobs
3. Incremental builds
4. Conditional steps
```

**Optimized Workflow:**
```yaml
name: CI (Optimized)

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  # Run lint and tests in parallel
  lint:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --prefer-offline --no-audit

      - name: Run linter
        run: npm run lint

  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Cache test results
        uses: actions/cache@v4
        with:
          path: .test-cache
          key: test-${{ hashFiles('src/**') }}

      - name: Install dependencies
        run: npm ci --prefer-offline --no-audit

      - name: Run tests
        run: npm test -- --cache --cacheDirectory=.test-cache

  build:
    runs-on: ubuntu-latest
    needs: [lint, test]

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Cache build
        uses: actions/cache@v4
        with:
          path: |
            dist
            .next/cache
          key: build-${{ hashFiles('src/**') }}-${{ hashFiles('package-lock.json') }}

      - name: Install dependencies
        run: npm ci --prefer-offline --no-audit

      - name: Build
        run: npm run build

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/
```

**After Optimization:**
```
Total pipeline time: 4 minutes
- Setup: 30s (cached)
- Dependencies: 1 min (cached, --prefer-offline)
- Lint + Tests: 2 min (parallel)
- Build: 1.5 min (cached)
Improvement: 67% faster
```

### 7. GitLab CI Example

**Prompt to Claude Code:**
```
Convert the GitHub Actions workflow to GitLab CI/CD.
Use stages, caching, and artifacts properly.
```

**Generated: `.gitlab-ci.yml`**
```yaml
stages:
  - test
  - build
  - deploy

variables:
  NODE_VERSION: "20"
  CACHE_KEY: "$CI_COMMIT_REF_SLUG"

# Cache template
.node_cache:
  cache:
    key: $CACHE_KEY
    paths:
      - node_modules/
      - .npm/

# Lint job
lint:
  stage: test
  image: node:$NODE_VERSION
  extends: .node_cache
  script:
    - npm ci --cache .npm --prefer-offline
    - npm run lint

# Test job
test:
  stage: test
  image: node:$NODE_VERSION
  extends: .node_cache
  script:
    - npm ci --cache .npm --prefer-offline
    - npm test
  coverage: '/Statements\s+:\s+(\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

# Build job
build:
  stage: build
  image: node:$NODE_VERSION
  extends: .node_cache
  needs: [lint, test]
  script:
    - npm ci --cache .npm --prefer-offline
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 week

# Deploy staging
deploy:staging:
  stage: deploy
  image: node:$NODE_VERSION
  needs: [build]
  only:
    - main
  environment:
    name: staging
    url: https://staging.example.com
  script:
    - npm run deploy:staging
  variables:
    API_URL: $STAGING_API_URL
    DEPLOY_TOKEN: $STAGING_DEPLOY_TOKEN

# Deploy production (manual)
deploy:production:
  stage: deploy
  image: node:$NODE_VERSION
  needs: [build]
  only:
    - main
  when: manual
  environment:
    name: production
    url: https://example.com
  script:
    - npm run deploy:production
  variables:
    API_URL: $PROD_API_URL
    DEPLOY_TOKEN: $PROD_DEPLOY_TOKEN
```

### 8. Debugging Failed Pipelines

**Prompt to Claude Code:**
```
My GitHub Actions pipeline is failing with this error:
[paste error log]

Help me debug and fix it.
```

**Example Debugging Session:**

**Error:**
```
Error: Cannot find module 'typescript'
```

**Claude Code Response:**
```bash
# The issue is that TypeScript is not installed in CI.
# Add it to dependencies or devDependencies:

npm install --save-dev typescript

# Or ensure npm ci is running (not npm install)
# Check package-lock.json is committed
```

**Error:**
```
Error: EACCES: permission denied
```

**Claude Code Response:**
```yaml
# Fix permission issues in workflow:

- name: Fix permissions
  run: |
    chmod +x ./scripts/deploy.sh
    # or
    sudo chown -R $USER:$USER ./dist
```

### 9. Advanced Techniques

**Conditional Deployments:**
```yaml
deploy:
  if: |
    github.event_name == 'push' &&
    github.ref == 'refs/heads/main' &&
    !contains(github.event.head_commit.message, '[skip deploy]')
```

**Dynamic Environment URLs:**
```yaml
environment:
  name: preview-${{ github.event.number }}
  url: https://pr-${{ github.event.number }}.preview.example.com
```

**Slack Notifications:**
```yaml
- name: Notify Slack
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
    text: 'Deployment to production: ${{ job.status }}'
```

**Rollback Capability:**
```yaml
rollback:
  runs-on: ubuntu-latest
  if: github.event_name == 'workflow_dispatch'
  steps:
    - name: Rollback to previous version
      run: |
        echo "Rolling back to previous deployment"
        # Use version from git tag or artifact
        npm run deploy:rollback -- --version=${{ github.event.inputs.version }}
```

## Common Mistakes to Avoid

### 1. **Not Caching Dependencies**
❌ Installing dependencies fresh every time
```yaml
- run: npm install  # Slow, no cache
```

✅ Use caching
```yaml
- uses: actions/setup-node@v4
  with:
    cache: 'npm'
- run: npm ci
```

### 2. **Secrets in Code**
❌ Hardcoding credentials
```yaml
env:
  API_KEY: "sk-1234567890"  # EXPOSED!
```

✅ Use GitHub Secrets
```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

### 3. **No Job Dependencies**
❌ Deploying without testing
```yaml
jobs:
  test: ...
  deploy: ...  # Runs in parallel!
```

✅ Use needs
```yaml
jobs:
  test: ...
  deploy:
    needs: test  # Waits for test to pass
```

### 4. **Ignoring Failed Tests**
❌ Deploying despite failures
```yaml
- run: npm test || true  # Ignores failures!
```

✅ Let failures stop pipeline
```yaml
- run: npm test  # Fails on error
```

### 5. **No Production Gates**
❌ Auto-deploying to production
```yaml
deploy:
  if: github.ref == 'refs/heads/main'  # Auto-deploys!
```

✅ Require manual approval
```yaml
deploy:
  environment:
    name: production  # Requires approval in settings
```

## Verification Checklist

- [ ] Pipeline runs automatically on PR and main push
- [ ] All jobs use appropriate caching
- [ ] Dependencies installed with `npm ci` (not `npm install`)
- [ ] Tests must pass before deployment
- [ ] Secrets managed via environment variables
- [ ] Production deployments require manual approval
- [ ] Build artifacts uploaded and available
- [ ] Pipeline completes in under 5 minutes
- [ ] Error handling and notifications configured
- [ ] Rollback strategy implemented

## Time Savings

**Manual Deployment:**
- SSH into server: 1 min
- Pull latest code: 1 min
- Install dependencies: 3 min
- Run tests: 2 min
- Build: 2 min
- Restart services: 1 min
- **Total: 10 min per deployment**

**With CI/CD:**
- Git push: 10s
- Pipeline runs automatically
- **Total: 10s of human time**
- **Savings: 99% of manual effort**

## Further Reading

- GitHub Actions documentation
- GitLab CI/CD best practices
- CircleCI optimization guide
- Deployment strategies (blue-green, canary)
- Infrastructure as Code (Terraform, Pulumi)
