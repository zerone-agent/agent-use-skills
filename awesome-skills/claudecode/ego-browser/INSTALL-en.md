# Installing ego-browser for Claude Code

## Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Node.js installed (for `npx`)
- macOS (a Windows beta is available on the official site)

## Installation Steps

### 1. Install the Skill

```bash
npx skills add github:CitroLabs/ego-lite/skills/ego-browser
```

The installer detects installed agent CLIs, including Claude Code, and registers the skill.

### 2. Install the ego lite Browser

The skill depends on the ego lite browser and can bootstrap it:

```bash
sh ~/.claude/skills/ego-browser/scripts/install.sh
```

Then complete the first-run onboarding in the ego lite app: it imports your browser data and registers the `ego-browser` command on the PATH (usually `~/.local/bin`).

If Claude Code has not picked up the skill automatically, symlink it manually:

```bash
mkdir -p ~/.claude/skills
rm -f ~/.claude/skills/ego-browser
ln -s ~/.local/share/ego/ego-skills ~/.claude/skills/ego-browser
```

### 3. Verify Installation

```bash
export PATH="$HOME/.local/bin:$PATH"
command -v ego-browser
ego-browser skill
```

Restart Claude Code, then try asking:

- "do you have ego-browser?"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
ego-browser upgrade
```

The skill is managed by the ego lite app; the symlink always points at the active version.

## Uninstallation

```bash
rm -f ~/.claude/skills/ego-browser
```

To fully remove, delete the `ego lite` app from /Applications.

## Getting Help

- Website: https://lite.ego.app/
- Docs: https://lite.ego.app/document/en/docs/ego-browser
- GitHub: https://github.com/CitroLabs/ego-lite
- Report issues: https://github.com/CitroLabs/ego-lite/issues
