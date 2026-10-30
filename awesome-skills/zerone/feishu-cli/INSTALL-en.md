# Installing Feishu CLI for Zerone

## Prerequisites

- [Zerone](https://www.zerone.run/) installed
- Node.js (npm/npx) installed
- A Feishu/Lark account (app creation and authorization happen in the browser)

## Installation Steps

### 1. Install the lark-cli CLI

```bash
npm install -g @larksuite/cli
```

### 2. Install the AI Agent Skills

```bash
npx skills add larksuite/cli -y -g
```

The installer detects installed agent CLIs, including Zerone, and registers the lark-* skills.

### 3. Configure and Log In

```bash
lark-cli config init --new
lark-cli auth login --recommend
```

Both commands print an authorization URL — complete the setup in the browser.

### 4. Verify Installation

```bash
lark-cli auth status
```

Restart Zerone, then try asking:

- "帮我看看明天的飞书日程"

If successful, Zerone will automatically recognize and invoke the lark-* skills.

## Updating

```bash
npm update -g @larksuite/cli
npx skills add larksuite/cli -y -g
```

## Uninstallation

```bash
rm -rf ~/.agents/skills/lark-*
npm uninstall -g @larksuite/cli
```

## Getting Help

- GitHub: https://github.com/larksuite/cli
- Report issues: https://github.com/larksuite/cli/issues
