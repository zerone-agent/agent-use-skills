# Installing Zerone Hub Management for Zerone

## Prerequisites

- [Zerone](https://www.zerone.run/) installed
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
git clone https://github.com/zerone-agents/agent-hub.git ~/.agents/agent-hub
```

### 3. Symlink the Skill

Create a symlink so Zerone discovers the zhub-management skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/zhub-management
ln -s ~/.agents/agent-hub/skills/zhub-management ~/.agents/skills/zhub-management
```

### 4. Verify Installation

Restart Zerone, then try asking:

- "do you have zhub-management?"

If successful, Zerone will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.agents/agent-hub
git pull
```

## Uninstallation

```bash
rm -rf ~/.agents/skills/zhub-management
```

## Getting Help

- GitHub: https://github.com/zerone-agents/agent-hub
- Report issues: https://github.com/zerone-agents/agent-hub/issues
