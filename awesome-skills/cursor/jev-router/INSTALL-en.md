# Installing Jev Model Router for Cursor

## Prerequisites

- [Cursor](https://cursor.com/) installed
- Git installed
- Docker with Docker Compose installed (only needed when deploying a new Router instance; managing an existing one is not affected)

## Installation Steps

### 1. Clone the jev-model-router Repository

```bash
git clone https://github.com/zerone-agents/jev-model-router.git ~/.cursor/jev-model-router
```

### 2. Symlink the Skill

Create a symlink so Cursor discovers the jev-router skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/jev-router
ln -s ~/.cursor/jev-model-router/skills/jev-router ~/.cursor/skills/jev-router
```

### 3. Verify Installation

Restart Cursor, then try asking:

- "do you have jev-router?"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/jev-model-router
git pull
```

## Uninstallation

```bash
rm -rf ~/.cursor/skills/jev-router
```

## Getting Help

- GitHub: https://github.com/zerone-agents/jev-model-router
- Report issues: https://github.com/zerone-agents/jev-model-router/issues
