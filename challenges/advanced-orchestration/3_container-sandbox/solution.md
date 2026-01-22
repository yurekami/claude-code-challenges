# Container Sandbox Solution

## Step-by-Step Solution

### Task 1: Create a Safe Testing Environment

**Step 1: Ask Claude to create a basic Dockerfile**
```
"Create a Dockerfile for a safe testing environment based on Ubuntu. I want to test
file system operations without affecting my host machine."
```

**Example Dockerfile:**
```dockerfile
FROM ubuntu:22.04

# Install basic utilities
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    git \
    tree \
    && rm -rf /var/lib/apt/lists/*

# Create a test directory
RUN mkdir -p /workspace/test

# Set working directory
WORKDIR /workspace

# Run bash by default
CMD ["/bin/bash"]
```

**Step 2: Build and run the container**
```bash
# Build the image
docker build -t safe-sandbox .

# Run interactively
docker run -it --rm safe-sandbox

# Inside container, test destructive commands safely
rm -rf /workspace/*
dd if=/dev/zero of=/tmp/largefile bs=1M count=1000
```

**Step 3: Test with volume for results**
```bash
# Create a results directory on host
mkdir results

# Run with mounted volume
docker run -it --rm -v $(pwd)/results:/output safe-sandbox bash -c "
  echo 'Test completed' > /output/results.txt
  ls -la / > /output/filesystem.txt
"
```

### Task 2: Isolate Dependency Testing

**Step 1: Create multi-version testing setup**
```
"Create a docker-compose.yml that lets me test my application against
Python 3.9, 3.10, 3.11, and 3.12 simultaneously."
```

**Example docker-compose.yml:**
```yaml
version: '3.8'

services:
  python39:
    image: python:3.9-slim
    volumes:
      - ./app:/app
      - ./results:/results
    working_dir: /app
    command: bash -c "python --version > /results/py39.txt && python test.py"

  python310:
    image: python:3.10-slim
    volumes:
      - ./app:/app
      - ./results:/results
    working_dir: /app
    command: bash -c "python --version > /results/py310.txt && python test.py"

  python311:
    image: python:3.11-slim
    volumes:
      - ./app:/app
      - ./results:/results
    working_dir: /app
    command: bash -c "python --version > /results/py311.txt && python test.py"

  python312:
    image: python:3.12-slim
    volumes:
      - ./app:/app
      - ./results:/results
    working_dir: /app
    command: bash -c "python --version > /results/py312.txt && python test.py"
```

**Step 2: Run all tests**
```bash
# Run all versions simultaneously
docker-compose up

# Check results
cat results/*.txt

# Clean up
docker-compose down
```

**Step 3: Test database migrations**
```yaml
version: '3.8'

services:
  test-db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: testpass
      POSTGRES_DB: testdb
    tmpfs:
      - /var/lib/postgresql/data  # Ephemeral storage
    ports:
      - "5432:5432"

  migration-test:
    image: node:18
    depends_on:
      - test-db
    volumes:
      - ./migrations:/migrations
    environment:
      DATABASE_URL: postgresql://postgres:testpass@test-db:5432/testdb
    command: |
      bash -c "
        npm install -g db-migrate
        cd /migrations
        db-migrate up
      "
```

### Task 3: Sandbox External Code

**Step 1: Create a restricted container**
```dockerfile
FROM python:3.11-slim

# Run as non-root user
RUN useradd -m -u 1000 sandboxuser

# Install dependencies in a safe location
WORKDIR /home/sandboxuser/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER sandboxuser

# Copy the untrusted code
COPY --chown=sandboxuser:sandboxuser . .

# Set resource limits in docker run command
CMD ["python", "untrusted_script.py"]
```

**Step 2: Run with resource limits**
```bash
# Run with CPU, memory, and network limits
docker run --rm \
  --cpus="1.0" \
  --memory="512m" \
  --memory-swap="512m" \
  --network none \
  --read-only \
  --tmpfs /tmp \
  --security-opt=no-new-privileges \
  untrusted-sandbox
```

**Step 3: Monitor and log**
```bash
# Run with logging
docker run --rm \
  --name sandbox-test \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  untrusted-sandbox

# In another terminal, monitor
docker stats sandbox-test
docker logs -f sandbox-test
```

### Task 4: Disposable Development Environments

**Step 1: Create a quick experiment container**
```bash
# Quick Node.js experiment
docker run -it --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  node:18 \
  bash

# Inside: npm init -y && npm install express
# Test your code
# Exit - everything cleaned up automatically
```

**Step 2: Pre-configured development environment**
```dockerfile
FROM node:18

# Install global tools
RUN npm install -g \
    typescript \
    ts-node \
    nodemon \
    prettier \
    eslint

# Install common development tools
RUN apt-get update && apt-get install -y \
    git \
    vim \
    tmux \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up shell
RUN echo 'alias ll="ls -la"' >> /root/.bashrc

WORKDIR /workspace

CMD ["/bin/bash"]
```

**Step 3: Quick start script**
```bash
#!/bin/bash
# save as dev-env.sh

ENV_NAME=${1:-"dev-experiment"}

docker run -it --rm \
  --name "$ENV_NAME" \
  -v "$(pwd):/workspace" \
  -p 3000:3000 \
  -p 5000:5000 \
  my-dev-env:latest

# Usage: ./dev-env.sh my-test
```

## Example Commands and Techniques

### Testing Installation Scripts

```bash
# Test an installation script safely
docker run -it --rm ubuntu:22.04 bash

# Inside container:
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh  # Test without affecting host
```

### Comparing Different Environments

```yaml
version: '3.8'

services:
  ubuntu:
    image: ubuntu:22.04
    volumes:
      - ./test-script.sh:/test.sh
    command: bash /test.sh

  alpine:
    image: alpine:3.18
    volumes:
      - ./test-script.sh:/test.sh
    command: sh /test.sh

  debian:
    image: debian:12
    volumes:
      - ./test-script.sh:/test.sh
    command: bash /test.sh
```

### Network Isolation Testing

```bash
# Create isolated network
docker network create isolated-net

# Run container on isolated network
docker run -it --rm \
  --network isolated-net \
  --name test1 \
  alpine sh

# In another terminal, run second container
docker run -it --rm \
  --network isolated-net \
  --name test2 \
  alpine sh

# They can communicate with each other
# From test1: ping test2
# But not with outside world
```

### Data Persistence Patterns

```bash
# Named volume for persistence
docker volume create mydata
docker run -it --rm -v mydata:/data alpine sh

# Bind mount for development
docker run -it --rm \
  -v "$(pwd)/src:/app/src" \
  -v "$(pwd)/tests:/app/tests" \
  my-dev-env

# Temporary filesystem for security
docker run -it --rm \
  --tmpfs /tmp:rw,noexec,nosuid,size=100m \
  alpine sh
```

## Common Mistakes to Avoid

### 1. Not Using --rm Flag
**Wrong:**
```bash
docker run -it ubuntu bash
# Leaves stopped container
```

**Right:**
```bash
docker run -it --rm ubuntu bash
# Auto-cleanup on exit
```

### 2. Running as Root Unnecessarily
**Wrong:**
```dockerfile
# No USER directive - runs as root
CMD ["python", "app.py"]
```

**Right:**
```dockerfile
RUN useradd -m appuser
USER appuser
CMD ["python", "app.py"]
```

### 3. No Resource Limits
**Wrong:**
```bash
docker run my-container
# Can consume all host resources
```

**Right:**
```bash
docker run --cpus="2" --memory="1g" my-container
```

### 4. Mounting Sensitive Directories
**Wrong:**
```bash
docker run -v /:/host alpine
# Entire filesystem exposed
```

**Right:**
```bash
docker run -v $(pwd)/data:/data alpine
# Only necessary directory
```

### 5. Not Cleaning Up
**Wrong:**
Never removing old containers, images, or volumes.

**Right:**
```bash
# Regular cleanup
docker system prune -a --volumes

# Remove specific items
docker container prune
docker image prune -a
docker volume prune
```

## Best Practices

### 1. Security Layers

```bash
# Combine multiple security measures
docker run -it --rm \
  --read-only \
  --tmpfs /tmp \
  --security-opt=no-new-privileges \
  --cap-drop=ALL \
  --cap-add=NET_BIND_SERVICE \
  --user 1000:1000 \
  --network none \
  my-secure-container
```

### 2. Multi-Stage Builds

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Runtime stage
FROM node:18-slim
RUN useradd -m appuser
USER appuser
WORKDIR /app
COPY --from=builder --chown=appuser:appuser /app/node_modules ./node_modules
COPY --chown=appuser:appuser . .
CMD ["node", "server.js"]
```

### 3. Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

### 4. Environment-Specific Configurations

```yaml
version: '3.8'

services:
  app:
    image: my-app
    environment:
      - NODE_ENV=${NODE_ENV:-development}
    env_file:
      - .env.${NODE_ENV:-development}
```

### 5. Efficient Caching

```dockerfile
# Copy dependency files first
COPY package*.json ./
RUN npm install

# Then copy source code
COPY . .

# Changes to source don't invalidate npm install cache
```

## Advanced Techniques

### Using Docker as Claude Workspace

```
"Create a Docker container where I can safely let you execute commands to test
this database migration script. Include PostgreSQL and all necessary tools."
```

### Automated Testing Pipeline

```yaml
version: '3.8'

services:
  unit-tests:
    build: .
    command: npm test
    environment:
      - NODE_ENV=test

  integration-tests:
    build: .
    depends_on:
      - test-db
    command: npm run test:integration
    environment:
      - DATABASE_URL=postgresql://test-db/testdb

  test-db:
    image: postgres:15
    tmpfs:
      - /var/lib/postgresql/data
```

### Cross-Platform Testing

```bash
# Test on different architectures
docker buildx build --platform linux/amd64,linux/arm64 -t my-app .

# Run on specific platform
docker run --platform linux/arm64 my-app
```

### Development with Live Reload

```yaml
version: '3.8'

services:
  dev:
    build:
      context: .
      target: development
    volumes:
      - ./src:/app/src:ro  # Read-only source
      - /app/node_modules   # Preserve node_modules
    ports:
      - "3000:3000"
    command: npm run dev
```

### Interactive Debugging

```bash
# Run container with debugging tools
docker run -it --rm \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  -v $(pwd):/app \
  my-debug-image \
  bash

# Inside: use strace, gdb, etc.
```

## Working with Claude

**Ask for complete environments:**
```
"Create a docker-compose setup for testing a microservices application with:
- Node.js API service
- Python ML service
- PostgreSQL database
- Redis cache
- Nginx reverse proxy
Include health checks and proper networking."
```

**Ask for security review:**
```
"Review this Dockerfile for security issues and suggest improvements:
[paste Dockerfile]"
```

**Ask for optimization:**
```
"This Docker build takes 10 minutes. Can you optimize the Dockerfile to use
better layer caching and reduce build time?"
```

## Success Indicators

You've mastered this challenge when you can:
- Safely execute risky operations in isolated containers
- Create reproducible test environments on demand
- Properly secure containers with resource limits and restrictions
- Efficiently manage container lifecycle and cleanup
- Use containers for development without affecting host system
- Leverage Claude to generate and optimize container configurations
