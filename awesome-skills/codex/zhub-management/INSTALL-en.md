# Installing Zerone Hub Management for Codex

## Prerequisites

- [Codex](https://openai.com/codex/) installed
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
git clone https://github.com/zerone-agents/agent-hub.git ~/.codex/agent-hub
```

### 3. Symlink the Skill

Create a symlink so Codex discovers the zhub-management skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/zhub-management
ln -s ~/.codex/agent-hub/skills/zhub-management ~/.codex/skills/zhub-management
```

### 4. Verify Installation

Restart Codex, then try asking:

- "do you have zhub-management?"

If successful, Codex will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.codex/agent-hub
git pull
```

## Uninstallation

```bash
rm -rf ~/.codex/skills/zhub-management
```

## Getting Help

- GitHub: https://github.com/zerone-agents/agent-hub
- Report issues: https://github.com/zerone-agents/agent-hub/issues
