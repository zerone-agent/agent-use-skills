# Installing Jev Model Router for Zerone

## Prerequisites

- [Zerone](https://www.zerone.run/) installed
- Git installed
- Docker with Docker Compose installed (only needed when deploying a new Router instance; managing an existing one is not affected)

## Installation Steps

### 1. Clone the jev-model-router Repository

```bash
git clone https://github.com/zerone-agents/jev-model-router.git ~/.agents/jev-model-router
```

### 2. Symlink the Skill

Create a symlink so Zerone discovers the jev-router skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/jev-router
ln -s ~/.agents/jev-model-router/skills/jev-router ~/.agents/skills/jev-router
```

### 3. Verify Installation

Restart Zerone, then try asking:

- "do you have jev-router?"

If successful, Zerone will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.agents/jev-model-router
git pull
```

## Uninstallation

```bash
rm -rf ~/.agents/skills/jev-router
```

## Getting Help

- GitHub: https://github.com/zerone-agents/jev-model-router
- Report issues: https://github.com/zerone-agents/jev-model-router/issues
