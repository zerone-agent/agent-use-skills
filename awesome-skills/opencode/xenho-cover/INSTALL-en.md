# Installing xenho-cover for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai/) installed
- Git installed
- For Direct mode (optional): Codex CLI installed and signed in on this machine (a machine-level dependency, independent of the host platform), or an OpenAI-compatible image endpoint
- For WeChat cover compositing (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the xenho-cover Repository

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.config/opencode/xenho-cover
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the OpenCode skills directory:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/xenho-cover
ln -s ~/.config/opencode/xenho-cover ~/.config/opencode/skills/xenho-cover
```

### 3. Verify Installation

Restart OpenCode, then try asking:

- "给这篇文章配个封面"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/xenho-cover
git pull
```

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/xenho-cover
```

## Getting Help

- GitHub: https://github.com/PPory/xenho-cover
- Report issues: https://github.com/PPory/xenho-cover/issues
