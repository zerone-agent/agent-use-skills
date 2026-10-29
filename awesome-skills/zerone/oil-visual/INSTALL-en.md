# Installing Oil Visual for Zerone

## Prerequisites

- [Zerone](https://www.zerone.run/) installed
- Git installed
- An image tool reachable from the host (e.g., local Codex CLI installed and signed in — machine-level dependency), or an external image generator for pasting the compiled prompt
- For transparent illustration cutout (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the oil-visual Repository

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.agents/oil-visual
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Zerone skills directory:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/oil-visual
ln -s ~/.agents/oil-visual ~/.agents/skills/oil-visual
```

### 3. Verify Installation

Restart Zerone, then try asking:

- "Use $oil-visual to draw an explainer image"

If successful, Zerone will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.agents/oil-visual
git pull
```

## Uninstallation

```bash
rm -rf ~/.agents/skills/oil-visual
```

## Getting Help

- GitHub: https://github.com/oil-oil/oil-visual
- Report issues: https://github.com/oil-oil/oil-visual/issues
