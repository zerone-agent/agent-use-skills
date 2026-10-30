# Feishu CLI (feishu-cli)

**Feishu CLI** bundles the official [Lark/Feishu CLI](https://github.com/larksuite/cli) (`lark-cli`, MIT, maintained by the larksuite team) with 26 AI Agent Skills: 200+ commands across 18 business domains let agents read messages, check calendars, write docs, build Base tables, send mail, and manage approvals — operating Feishu end-to-end with zero extra setup.

## Tags

🛠️ Productivity Tools | ✅ Verified

## Core Philosophy
- **Agent-native design**: Every command is tested with real agents, featuring concise parameters, smart defaults, and structured output to maximize call success rates; the skills work with popular AI tools out of the box.
- **Three-layer command system**: Shortcuts (human & AI friendly) → API commands (platform-synced) → raw API (full coverage), so agents can pick the right granularity for each task.
- **Dual identity with clear boundaries**: Bot identity works without user authorization but cannot access personal data; User identity (`lark-cli auth login --recommend`) unlocks personal calendars, messages, and docs — personal-data operations must use User identity.
- **Secure & controllable**: Input injection protection, terminal output sanitization, and OS-native keychain credential storage.

## Key Features & Workflow

1. **Install**: `npx @larksuite/cli@latest install` for the CLI, then `npx skills add larksuite/cli -y -g` to register the skill set with installed agents.
2. **Configure and log in**: `lark-cli config init --new` (one-time guided app creation) and `lark-cli auth login --recommend` (auto-selects common scopes); verify with `lark-cli auth status`.
3. **Domain skills**: `lark-shared` (auto-loaded: config, auth, scope, security) plus calendar, IM, docs, drive, Markdown, sheets, slides, Base, tasks, mail, contacts, wiki, real-time events, meetings/Minutes, whiteboard, attendance, approval, and OKR.
4. **Workflows & extensibility**: Ready-made meeting-summary and standup-report workflows, `lark-openapi-explorer` for underlying APIs, and `lark-skill-maker` for custom skill creation.

## Skills Library Overview
- **Core domains**: Messenger, Docs, Drive, Markdown, Sheets, Slides, Base, Tasks, Wiki, Contact, Mail, Calendar, Meetings, Attendance, Approval, OKR, Event subscriptions, Whiteboard.
- **Infrastructure**: `lark-shared` (auto-loaded by all other skills), `lark-openapi-explorer`, `lark-skill-maker`.
- **Workflows**: `lark-workflow-meeting-summary`, `lark-workflow-standup-report`.

## Installation & Support
Feishu CLI supports the following AI editors and platforms:
- [Claude Code](../../claudecode/feishu-cli/INSTALL-en.md)
- [Cursor](../../cursor/feishu-cli/INSTALL-en.md)
- [Codex](../../codex/feishu-cli/INSTALL-en.md)
- [OpenCode](../../opencode/feishu-cli/INSTALL-en.md)
- [OpenClaw](../../openclaw/feishu-cli/INSTALL-en.md)
- [Zerone](../../zerone/feishu-cli/INSTALL-en.md)
- [Qoder](../../qoder/feishu-cli/INSTALL-en.md)

Skills are installed through the official `npx skills add` channel, which detects installed agent CLIs; `lark-cli` is a machine-level dependency independent of the host platform. All seven listed platforms are verified.

---
For more information, visit: [GitHub - larksuite/cli](https://github.com/larksuite/cli)
