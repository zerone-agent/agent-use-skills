# ego-browser

**ego-browser** is the browser automation skill for [ego(lite)](https://lite.ego.app/), a Chromium browser built for humans and AI agents. Agents drive the browser through the `ego-browser` CLI to open websites, fill forms, click buttons, take screenshots, extract page data, reuse logged-in sessions, and run web app tests — all inside an isolated Space that never hijacks your own tabs.

## Tags

🛠️ Productivity Tools | ✅ Verified

## Core Philosophy
- **Code-first control**: The agent writes one Node.js script per task and `ego-browser` executes the whole flow in a single call — fewer model turns, fewer tokens, and multi-step tasks finish 20–50% faster than per-action CLI loops.
- **Space isolation**: Every task runs in its own Space (isolated workspace) inside ego(lite). The agent never switches your tabs, steals keyboard focus, or takes over your mouse; you can watch or take over anytime.
- **Reuse real logins**: Built on Chromium, ego(lite) imports your Chrome profile in one click, so the agent inherits signed-in state for Gmail, Notion, LinkedIn, and internal tools without re-authenticating.
- **Semantic snapshots**: A custom Chromium engine produces page snapshots that reach cross-origin iframes, shadow DOM, and embedded widgets (Stripe, Salesforce, Intercom), where plain fetches and injected scripts usually fail.
- **Self-bootstrapping**: The skill installs and upgrades the browser it depends on, and prints a version-matched usage guide so agents always follow current capabilities.

## Key Features & Workflow

1. **Bootstrap**: Run `ego-browser skill` before any browser task — it prints the usage guide matching the installed ego lite version; `references/install.md` handles a missing browser or unknown command.
2. **Core loop**: In a single heredoc, reuse or create a Task Space, open a tab, read the semantic snapshot (`snapshotText()`), act on `@N` refs or CSS selectors, and report results with `cliLog(...)`.
3. **Logged-in automation**: Sign in once in the browser, then let every agent reuse the session for daily web work — research, form filling, data collection, QA, and dogfooding.
4. **Site learnings**: Ships accumulating per-site recipes (GitHub, Google, X) under `learnings/`, with reusable browser-tools scripts and notes.
5. **Safe maintenance**: `references/clearing-state.md` guards cookie/cache/storage clearing (some clears reach the whole browser profile); `ego-browser upgrade` keeps the runtime and guide in sync.

## Skills Library Overview
- **References**: install/upgrade guide and state-clearing guardrails.
- **Scripts**: `scripts/install.sh` for one-command macOS installation of ego lite.
- **Learnings**: per-site browser-tools and notes (github, google, x-com) for common automation targets.

## Installation & Support
ego-browser supports the following AI editors and platforms:
- [Claude Code](../../claudecode/ego-browser/INSTALL-en.md)
- [Cursor](../../cursor/ego-browser/INSTALL-en.md)
- [Codex](../../codex/ego-browser/INSTALL-en.md)
- [OpenCode](../../opencode/ego-browser/INSTALL-en.md)
- [OpenClaw](../../openclaw/ego-browser/INSTALL-en.md)
- [Zerone](../../zerone/ego-browser/INSTALL-en.md)
- [Qoder](../../qoder/ego-browser/INSTALL-en.md)

---
For more information, visit: [ego(lite) Official Site](https://lite.ego.app/) | [GitHub - CitroLabs/ego-lite](https://github.com/CitroLabs/ego-lite)
