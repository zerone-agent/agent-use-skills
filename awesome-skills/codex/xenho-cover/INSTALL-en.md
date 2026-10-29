# Installing xenho-cover for Codex

## Prerequisites

- [Codex](https://openai.com/codex/) installed
- Git installed
- For Direct mode (optional): Codex CLI signed in locally (default image path, no API key), or an OpenAI-compatible image endpoint
- For WeChat cover compositing (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the xenho-cover Repository

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.codex/xenho-cover
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Codex skills directory:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/xenho-cover
ln -s ~/.codex/xenho-cover ~/.codex/skills/xenho-cover
```

### 3. Verify Installation

Restart Codex, then try asking:

- "给这篇文章配个封面"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/xenho-cover
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/xenho-cover
```

## Getting Help

- GitHub: https://github.com/PPory/xenho-cover
- Report issues: https://github.com/PPory/xenho-cover/issues
