# Installing Zerone Hub Management for Claude Code

## Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Git installed
- Node.js installed (for the zhub CLI)

## Installation Steps

### 1. Install the zhub CLI

```bash
npm install -g @zerone-agent/zhub
```

Or with Bun:

```bash
bun add -g @zerone-agent/zhub
```

Log in (the token can be obtained from the control-panel web UI: Settings → CLI Tokens):

```bash
zhub login --url <server-url> --token cli_xxxxxxxxxxxx
```

### 2. Clone the agent-hub Repository

```bash
git clone https://github.com/zerone-agents/agent-hub.git ~/.claude/agent-hub
```

### 3. Symlink the Skill

Create a symlink so Claude Code discovers the zhub-management skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/zhub-management
ln -s ~/.claude/agent-hub/skills/zhub-management ~/.claude/skills/zhub-management
```

### 4. Verify Installation

Restart Claude Code, then try asking:

- "do you have zhub-management?"

If successful, Claude Code will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.claude/agent-hub
git pull
```

## Uninstallation

```bash
rm -rf ~/.claude/skills/zhub-management
```

## Getting Help

- GitHub: https://github.com/zerone-agents/agent-hub
- Report issues: https://github.com/zerone-agents/agent-hub/issues
