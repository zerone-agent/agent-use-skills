# Installing xenho-cover for Zerone

## Prerequisites

- [Zerone](https://www.zerone.run/) installed
- Git installed
- For Direct mode (optional): Codex CLI installed and signed in on this machine (a machine-level dependency, independent of the host platform), or an OpenAI-compatible image endpoint
- For WeChat cover compositing (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the xenho-cover Repository

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.agents/xenho-cover
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Zerone skills directory:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/xenho-cover
ln -s ~/.agents/xenho-cover ~/.agents/skills/xenho-cover
```

### 3. Verify Installation

Restart Zerone, then try asking:

- "给这篇文章配个封面"

If successful, Zerone will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.agents/xenho-cover
git pull
```

## Uninstallation

```bash
rm -rf ~/.agents/skills/xenho-cover
```

## Getting Help

- GitHub: https://github.com/PPory/xenho-cover
- Report issues: https://github.com/PPory/xenho-cover/issues
