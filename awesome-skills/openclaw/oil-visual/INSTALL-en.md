# Installing Oil Visual for OpenClaw

## Prerequisites

- [OpenClaw](https://openclaw.ai/) installed
- Git installed
- An image tool reachable from the host (e.g., local Codex CLI installed and signed in — machine-level dependency), or an external image generator for pasting the compiled prompt
- For transparent illustration cutout (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the oil-visual Repository

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.openclaw/oil-visual
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the OpenClaw skills directory:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/oil-visual
ln -s ~/.openclaw/oil-visual ~/.openclaw/skills/oil-visual
```

### 3. Verify Installation

Restart OpenClaw, then try asking:

- "Use $oil-visual to draw an explainer image"

If successful, OpenClaw will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.openclaw/oil-visual
git pull
```

## Uninstallation

```bash
rm -rf ~/.openclaw/skills/oil-visual
```

## Getting Help

- GitHub: https://github.com/oil-oil/oil-visual
- Report issues: https://github.com/oil-oil/oil-visual/issues
