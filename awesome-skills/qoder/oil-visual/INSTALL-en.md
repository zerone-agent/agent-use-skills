# Installing Oil Visual for Qoder

## Prerequisites

- [Qoder](https://qoder.com/) installed
- Git installed
- An image tool reachable from the host (e.g., local Codex CLI installed and signed in — machine-level dependency), or an external image generator for pasting the compiled prompt
- For transparent illustration cutout (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the oil-visual Repository

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.qoder/oil-visual
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Qoder skills directory:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/oil-visual
ln -s ~/.qoder/oil-visual ~/.qoder/skills/oil-visual
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "Use $oil-visual to draw an explainer image"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/oil-visual
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/oil-visual
```

## Getting Help

- GitHub: https://github.com/oil-oil/oil-visual
- Report issues: https://github.com/oil-oil/oil-visual/issues
