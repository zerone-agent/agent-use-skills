# Installing Jev Model Router for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai/) installed
- Git installed
- Docker with Docker Compose installed (only needed when deploying a new Router instance; managing an existing one is not affected)

## Installation Steps

### 1. Clone the jev-model-router Repository

```bash
git clone https://github.com/zerone-agents/jev-model-router.git ~/.config/opencode/jev-model-router
```

### 2. Symlink the Skill

Create a symlink so OpenCode discovers the jev-router skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/jev-router
ln -s ~/.config/opencode/jev-model-router/skills/jev-router ~/.config/opencode/skills/jev-router
```

### 3. Verify Installation

Restart OpenCode, then try asking:

- "do you have jev-router?"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/jev-model-router
git pull
```

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/jev-router
```

## Getting Help

- GitHub: https://github.com/zerone-agents/jev-model-router
- Report issues: https://github.com/zerone-agents/jev-model-router/issues
