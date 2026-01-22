# Container Sandbox Challenge

**Related Tip:** Tip 21 - Run risky tasks in Docker containers for safety

## Description

Some tasks are risky to run directly on your development machine: testing destructive operations, experimenting with system configurations, or running untrusted code. Docker containers provide isolated sandboxes where you can safely experiment without affecting your host system.

## Objective

Learn to use Docker containers as safe sandboxes for risky operations, testing, and experimentation, leveraging Claude Code to set up and manage containerized environments.

## Challenge Tasks

1. **Create a Safe Testing Environment**
   - Build a Docker container for testing file system operations
   - Test potentially destructive commands safely
   - Experiment with configuration changes without risk

2. **Isolate Dependency Testing**
   - Test different versions of languages/frameworks in containers
   - Run multiple incompatible versions simultaneously
   - Test migration scripts in isolated environments

3. **Sandbox External Code**
   - Run untrusted or third-party code in a container
   - Limit resource usage (CPU, memory, network)
   - Monitor and log container behavior

4. **Disposable Development Environments**
   - Create ephemeral containers for quick experiments
   - Set up pre-configured development environments
   - Test installation scripts without polluting your system

## Success Criteria

- Successfully execute risky operations in containers without host impact
- Demonstrate ability to create isolated, reproducible environments
- Show proper resource limitation and security practices
- Effectively use containers for testing and experimentation
- Leverage Claude to generate Dockerfiles and docker-compose configurations

## Key Skills to Practice

- Writing effective Dockerfiles
- Using docker-compose for multi-container setups
- Container resource management
- Volume mounting for data persistence
- Network isolation and security
- Container cleanup and maintenance

## Bonus Challenges

- Create a library of reusable development containers
- Set up automated testing pipelines in containers
- Use Docker for cross-platform compatibility testing
- Implement container-based CI/CD workflows
- Use Docker networks to test distributed systems
