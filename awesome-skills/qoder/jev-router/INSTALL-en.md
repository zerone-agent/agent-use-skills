# Installing Jev Model Router for Qoder

## Prerequisites

- [Qoder](https://qoder.com/) installed
- Git installed
- Docker with Docker Compose installed (only needed when deploying a new Router instance; managing an existing one is not affected)

## Installation Steps

### 1. Clone the jev-model-router Repository

```bash
git clone https://github.com/zerone-agents/jev-model-router.git ~/.qoder/jev-model-router
```

### 2. Symlink the Skill

Create a symlink so Qoder discovers the jev-router skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/jev-router
ln -s ~/.qoder/jev-model-router/skills/jev-router ~/.qoder/skills/jev-router
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "do you have jev-router?"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/jev-model-router
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/jev-router
```

## Getting Help

- GitHub: https://github.com/zerone-agents/jev-model-router
- Report issues: https://github.com/zerone-agents/jev-model-router/issues
