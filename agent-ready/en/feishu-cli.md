# Feishu CLI - Agent-Ready Certification

**Feishu CLI** has officially passed the **Agent-Ready** certification!

From the official [larksuite/cli](https://github.com/larksuite/cli) repository (MIT, 17.9k stars), this skill set lets AI agents operate Feishu/Lark end-to-end through `lark-cli` — 26 AI Agent Skills and 200+ commands across 18 business domains, from reading messages to managing approvals.

## Certification Highlights

- **Officially Built**: Maintained by the larksuite team, evolving in lockstep with the Feishu Open Platform; the 26 skills are versioned with the CLI itself.
- **Broad Domain Coverage**: Messenger, Docs, Drive, Markdown, Sheets, Slides, Base, Tasks, Wiki, Contact, Mail, Calendar, Meetings/Minutes, Attendance, Approval, OKR, real-time events, and whiteboard — 200+ curated commands in one CLI.
- **Agent-Native Design**: Every command is tested with real agents, with concise parameters, smart defaults, and structured output; a three-layer command system (shortcuts → API commands → raw API) lets agents pick the right granularity per task.
- **Security by Default**: Bot/User dual identity with clear boundaries, OS-native keychain credential storage, input injection protection, and terminal output sanitization.

## Why is it Agent-Ready?

Feishu CLI successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: Every operation is an explicit `lark-cli` subcommand with machine-readable structured output; `lark-shared` (auto-loaded by all other skills) standardizes auth, scope, and security rules across the whole skill set.
- **Structured Feedback**: Structured output plus `lark-cli auth status` and doctor-style checks keep execution state observable; Bot/User identity routing is explicit, so the agent always knows which permissions a call uses.
- **Security Guardrails**: Personal-data operations must use User identity with OAuth (`lark-cli auth login --recommend`), credentials live in the OS keychain, and input/output sanitization is built into the CLI.
- **Verified Integration**: The official `npx skills add` channel auto-detects installed agent CLIs and registers the skills; documented and validated across Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, and Qoder.

---
[View Feishu CLI Full Documentation](../../awesome-skills/introductions/en/feishu-cli.md)
