# Installing Oil Visual for Codex

## Prerequisites

- [Codex](https://openai.com/codex/) installed and signed in (image generation uses its built-in GPT Image)
- Git installed
- For transparent illustration cutout (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the oil-visual Repository

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.codex/skills/oil-visual
```

### 2. Verify Installation

The skill is cloned directly into the Codex skills directory. Restart Codex, then try asking:

- "Use $oil-visual to draw an explainer image"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/skills/oil-visual
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/oil-visual
```

## Getting Help

- GitHub: https://github.com/oil-oil/oil-visual
- Report issues: https://github.com/oil-oil/oil-visual/issues
