# Installing Oil Visual for Claude Code

## Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Git installed
- An image tool reachable from the host (e.g., local Codex CLI installed and signed in — machine-level dependency), or an external image generator for pasting the compiled prompt
- For transparent illustration cutout (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the oil-visual Repository

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.claude/oil-visual
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/oil-visual
ln -s ~/.claude/oil-visual ~/.claude/skills/oil-visual
```

### 3. Verify Installation

Restart Claude Code, then try asking:

- "Use $oil-visual to draw an explainer image"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/oil-visual
git pull
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/oil-visual
```

## Getting Help

- GitHub: https://github.com/oil-oil/oil-visual
- Report issues: https://github.com/oil-oil/oil-visual/issues
