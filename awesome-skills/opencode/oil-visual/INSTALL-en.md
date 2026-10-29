# Installing Oil Visual for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai/) installed
- Git installed
- An image tool reachable from the host (e.g., local Codex CLI installed and signed in — machine-level dependency), or an external image generator for pasting the compiled prompt
- For transparent illustration cutout (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the oil-visual Repository

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.config/opencode/oil-visual
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the OpenCode skills directory:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/oil-visual
ln -s ~/.config/opencode/oil-visual ~/.config/opencode/skills/oil-visual
```

### 3. Verify Installation

Restart OpenCode, then try asking:

- "Use $oil-visual to draw an explainer image"

If successful, OpenCode will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.config/opencode/oil-visual
git pull
```

## Uninstallation

```bash
rm -rf ~/.config/opencode/skills/oil-visual
```

## Getting Help

- GitHub: https://github.com/oil-oil/oil-visual
- Report issues: https://github.com/oil-oil/oil-visual/issues
