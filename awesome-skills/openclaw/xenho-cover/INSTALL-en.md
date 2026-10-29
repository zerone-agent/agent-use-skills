# Installing xenho-cover for OpenClaw

## Prerequisites

- [OpenClaw](https://openclaw.ai/) installed
- Git installed
- For Direct mode (optional): Codex CLI installed and signed in on this machine (a machine-level dependency, independent of the host platform), or an OpenAI-compatible image endpoint
- For WeChat cover compositing (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the xenho-cover Repository

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.openclaw/xenho-cover
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the OpenClaw skills directory:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/xenho-cover
ln -s ~/.openclaw/xenho-cover ~/.openclaw/skills/xenho-cover
```

### 3. Verify Installation

Restart OpenClaw, then try asking:

- "给这篇文章配个封面"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/xenho-cover
git pull
```

## Uninstallation

```bash
rm -rf ~/.openclaw/skills/xenho-cover
```

## Getting Help

- GitHub: https://github.com/PPory/xenho-cover
- Report issues: https://github.com/PPory/xenho-cover/issues
