# Installing Jev Model Router for Claude Code

## Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Git installed
- Docker with Docker Compose installed (only needed when deploying a new Router instance; managing an existing one is not affected)

## Installation Steps

### 1. Clone the jev-model-router Repository

```bash
git clone https://github.com/zerone-agents/jev-model-router.git ~/.claude/jev-model-router
```

### 2. Symlink the Skill

Create a symlink so Claude Code discovers the jev-router skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/jev-router
ln -s ~/.claude/jev-model-router/skills/jev-router ~/.claude/skills/jev-router
```

### 3. Verify Installation

Restart Claude Code, then try asking:

- "do you have jev-router?"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/jev-model-router
git pull
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/jev-router
```

## Getting Help

- GitHub: https://github.com/zerone-agents/jev-model-router
- Report issues: https://github.com/zerone-agents/jev-model-router/issues
