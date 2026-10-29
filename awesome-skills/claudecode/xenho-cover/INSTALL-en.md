# Installing xenho-cover for Claude Code

## Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Git installed
- For Direct mode (optional): Codex CLI installed locally, or an OpenAI-compatible image endpoint
- For WeChat cover compositing (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the xenho-cover Repository

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.claude/xenho-cover
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/xenho-cover
ln -s ~/.claude/xenho-cover ~/.claude/skills/xenho-cover
```

### 3. Verify Installation

Restart Claude Code, then try asking:

- "给这篇文章配个封面"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/xenho-cover
git pull
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/xenho-cover
```

## Getting Help

- GitHub: https://github.com/PPory/xenho-cover
- Report issues: https://github.com/PPory/xenho-cover/issues
