# Container Sandbox

## Difficulty: Hard

## Category: Advanced Orchestration

## Related Tips: 21

## Description

Running Claude Code with `--dangerously-skip-permissions` in a container provides a safe sandbox for risky operations. This enables autonomous execution of potentially destructive commands without risking your main system.

## Objective

Set up and use a containerized Claude Code sandbox:
1. Create a Docker container with Claude Code
2. Mount necessary volumes for work
3. Run with elevated permissions safely
4. Execute autonomous tasks in the sandbox

## Task

Create a sandboxed Claude Code environment for running untrusted code:

1. Write a Dockerfile that includes Claude Code CLI
2. Configure volume mounts for:
   - Work directory (read-write)
   - Credentials (read-only)
3. Run Claude with `--dangerously-skip-permissions`
4. Execute a risky operation (e.g., bulk file modifications)
5. Verify results before applying to main system

## Expected Outcome

- Working Docker container with Claude Code
- Isolated environment for risky operations
- Ability to review changes before committing
- No impact to host system on failure

## Hints

1. Base image: Node.js LTS (Claude Code requires Node)
2. Install Claude Code via npm in the container
3. Use bind mounts for work directories
4. Environment variables pass credentials safely
5. Consider using `--rm` for automatic cleanup

## Constraints

- Container must be truly isolated
- Host system credentials must not be exposed
- Work must be reviewable before applying

## Submission

Submit:
1. Your Dockerfile
2. Docker run command with volume mounts
3. Claude Code command used inside container
4. How you reviewed and applied the results
