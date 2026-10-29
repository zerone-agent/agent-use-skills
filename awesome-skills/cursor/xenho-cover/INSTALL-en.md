# Installing xenho-cover for Cursor

## Prerequisites

- [Cursor](https://cursor.com/) installed
- Git installed
- For Direct mode (optional): Codex CLI installed and signed in on this machine (a machine-level dependency, independent of the host platform), or an OpenAI-compatible image endpoint
- For WeChat cover compositing (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the xenho-cover Repository

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.cursor/xenho-cover
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Cursor skills directory:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/xenho-cover
ln -s ~/.cursor/xenho-cover ~/.cursor/skills/xenho-cover
```

### 3. Verify Installation

Restart Cursor, then try asking:

- "给这篇文章配个封面"

If successful, Cursor will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.cursor/xenho-cover
git pull
```

## Uninstallation

```bash
rm -rf ~/.cursor/skills/xenho-cover
```

## Getting Help

- GitHub: https://github.com/PPory/xenho-cover
- Report issues: https://github.com/PPory/xenho-cover/issues
