# Installing xenho-cover for Qoder

## Prerequisites

- [Qoder](https://qoder.com/) installed
- Git installed
- For Direct mode (optional): Codex CLI installed and signed in on this machine (a machine-level dependency, independent of the host platform), or an OpenAI-compatible image endpoint
- For WeChat cover compositing (optional): Python with Pillow installed

## Installation Steps

### 1. Clone the xenho-cover Repository

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.qoder/xenho-cover
```

### 2. Symlink the Skill

The repository root is the skill folder; symlink it into the Qoder skills directory:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/xenho-cover
ln -s ~/.qoder/xenho-cover ~/.qoder/skills/xenho-cover
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "给这篇文章配个封面"

If successful, Qoder will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.qoder/xenho-cover
git pull
```

## Uninstallation

```bash
rm -rf ~/.qoder/skills/xenho-cover
```

## Getting Help

- GitHub: https://github.com/PPory/xenho-cover
- Report issues: https://github.com/PPory/xenho-cover/issues
