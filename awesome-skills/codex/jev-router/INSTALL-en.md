# Installing Jev Model Router for Codex

## Prerequisites

- [Codex](https://openai.com/codex/) installed
- Git installed
- Docker with Docker Compose installed (only needed when deploying a new Router instance; managing an existing one is not affected)

## Installation Steps

### 1. Clone the jev-model-router Repository

```bash
git clone https://github.com/zerone-agents/jev-model-router.git ~/.codex/jev-model-router
```

### 2. Symlink the Skill

Create a symlink so Codex discovers the jev-router skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/jev-router
ln -s ~/.codex/jev-model-router/skills/jev-router ~/.codex/skills/jev-router
```

### 3. Verify Installation

Restart Codex, then try asking:

- "do you have jev-router?"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/jev-model-router
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/jev-router
```

## Getting Help

- GitHub: https://github.com/zerone-agents/jev-model-router
- Report issues: https://github.com/zerone-agents/jev-model-router/issues
