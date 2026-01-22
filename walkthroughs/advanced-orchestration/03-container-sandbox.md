# Walkthrough: Container Sandbox

**Difficulty:** Hard | **Time:** 30 minutes | **Category:** Advanced Orchestration

---

## Overview

Running untrusted code or experimenting with system changes can be risky. Container sandboxes provide isolated environments for safe execution. This challenge teaches you to use Docker containers as sandboxes with Claude.

## Prerequisites

- [ ] Docker installed and running
- [ ] Basic container knowledge
- [ ] Understanding of isolation concepts

---

## Step 1: Why Sandbox?

### Use Cases
```
- Running untrusted code snippets
- Experimenting with system configurations
- Testing destructive operations
- Reproducing bugs in clean environments
- Trying new tools without polluting your system
```

### Safety Benefits
```
Sandboxed:           Your System:
┌──────────────┐     ┌──────────────┐
│  Untrusted   │     │    Safe      │
│    Code      │ ──X─│   Always     │
│  rm -rf /    │     │              │
└──────────────┘     └──────────────┘
     Isolated            Protected
```

---

## Step 2: Quick Sandbox Setup

### One-Liner Sandbox
```bash
# Temporary container, auto-removed
docker run --rm -it ubuntu:22.04 bash
```

### Node.js Sandbox
```bash
docker run --rm -it node:20 bash
```

### Python Sandbox
```bash
docker run --rm -it python:3.11 bash
```

---

## Step 3: Project Sandbox

### Mount Your Code (Read-Only)
```bash
docker run --rm -it \
  -v $(pwd):/app:ro \
  -w /app \
  node:20 bash
```

### Mount with Write Access
```bash
docker run --rm -it \
  -v $(pwd):/app \
  -w /app \
  node:20 bash
```

---

## Step 4: Custom Sandbox Dockerfile

### Create a Development Sandbox
```dockerfile
# Dockerfile.sandbox
FROM ubuntu:22.04

# Install common tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    nodejs \
    npm \
    python3 \
    python3-pip

# Create non-root user
RUN useradd -m developer
USER developer
WORKDIR /home/developer

CMD ["bash"]
```

### Build and Run
```bash
docker build -f Dockerfile.sandbox -t my-sandbox .
docker run --rm -it -v $(pwd):/work my-sandbox
```

---

## Step 5: Sandbox with Claude

### Ask Claude to Use Sandbox
```
Run this potentially risky code in a Docker sandbox:
[paste code]

Use a temporary container that's removed after execution.
Show me the output without affecting my system.
```

### Test in Clean Environment
```
Create a Docker sandbox to test if our app works on a fresh machine:
1. Start from a clean Ubuntu image
2. Install only documented dependencies
3. Clone our repo
4. Run the setup and tests
5. Report any missing dependencies
```

---

## Step 6: Advanced Sandboxing

### Network Isolation
```bash
# No network access
docker run --rm -it --network none ubuntu:22.04 bash
```

### Memory Limits
```bash
# Limit to 512MB RAM
docker run --rm -it --memory=512m ubuntu:22.04 bash
```

### CPU Limits
```bash
# Limit to 1 CPU
docker run --rm -it --cpus=1 ubuntu:22.04 bash
```

### Combined Security
```bash
docker run --rm -it \
  --network none \
  --memory=512m \
  --cpus=1 \
  --read-only \
  ubuntu:22.04 bash
```

---

## Step 7: Sandbox Patterns

### Pattern A: Experiment Sandbox
```bash
#!/bin/bash
# experiment.sh - Run experiments safely
docker run --rm -it \
  -v $(pwd)/experiments:/experiments \
  -w /experiments \
  python:3.11 bash
```

### Pattern B: Build Sandbox
```bash
#!/bin/bash
# clean-build.sh - Build in clean environment
docker run --rm \
  -v $(pwd):/app \
  -w /app \
  node:20 \
  sh -c "npm ci && npm run build && npm test"
```

### Pattern C: Debug Sandbox
```bash
#!/bin/bash
# debug.sh - Debug with full access
docker run --rm -it \
  -v $(pwd):/app \
  -w /app \
  --cap-add=SYS_PTRACE \
  node:20 bash
```

---

## Verification Checklist

- [ ] Ran a command in a temporary container
- [ ] Mounted project files in a sandbox
- [ ] Created a custom sandbox Dockerfile
- [ ] Used network/resource isolation
- [ ] Had Claude execute code in a sandbox

---

## Sandbox Commands Reference

| Purpose | Command |
|---------|---------|
| Temporary shell | `docker run --rm -it <image> bash` |
| Mount current dir | `-v $(pwd):/app` |
| Read-only mount | `-v $(pwd):/app:ro` |
| No network | `--network none` |
| Memory limit | `--memory=512m` |
| CPU limit | `--cpus=1` |
| Read-only filesystem | `--read-only` |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Container can't write | Check mount permissions |
| Network needed | Remove `--network none` |
| Files owned by root | Use `--user $(id -u)` |
| Container exits immediately | Use `-it` for interactive |

---

## Pro Tips

1. **Always --rm:** Don't leave orphan containers
2. **Named Images:** Build custom sandboxes for frequent use
3. **Resource Limits:** Prevent runaway processes
4. **Non-Root:** Run as non-root user inside container

---

## Next Challenge

Continue to **[Learning by Doing](./04-learning-by-doing.md)** for practice-based learning!
