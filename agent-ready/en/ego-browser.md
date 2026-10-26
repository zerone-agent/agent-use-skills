# ego-browser - Agent-Ready Certification

**ego-browser** has officially passed the **Agent-Ready** certification!

From [CitroLabs/ego-lite](https://github.com/CitroLabs/ego-lite), this skill lets any AI agent drive the ego(lite) Chromium browser through the `ego-browser` CLI — reusing your logged-in sessions and running web tasks in isolated Spaces.

## Certification Highlights

- **One Skill, Every Agent**: Installing ego(lite) writes the skill into installed agent CLIs automatically (Claude Code, Codex, Cursor, OpenClaw, OpenCode, and more); one standalone command covers the rest.
- **Code-Based Interface**: Capabilities (snapshot, click, fill, raw CDP) are exposed as pre-injected JavaScript functions, so a single heredoc call executes an entire multi-step web flow.
- **Human–Agent Coexistence**: Tasks run in isolated Spaces with their own tabs — agents never hijack the user's tabs, focus, or mouse, and the user can watch or take over anytime.
- **Local-First Privacy**: ego(lite) runs on the user's machine, stores imported profiles locally, and requires no account or email.

## Why is it Agent-Ready?

ego-browser successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: A single `ego-browser nodejs` call performs a complete multi-step flow with deterministic `@N` snapshot refs as action targets; `ego-browser skill` exposes a version-matched capability guide.
- **Structured Feedback**: Semantic snapshot text (`snapshotText()`), ref-annotated page trees, and `cliLog(...)` output give agents machine-readable state after every step.
- **Security Guardrails**: Space isolation keeps agent work separate from user browsing; `references/clearing-state.md` guards cookie/cache/storage clears that would reach the whole browser profile; profiles stay local.
- **Verified Integration**: Onboarding auto-detects and wires installed agent CLIs; documented and validated across Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, and Qoder.

---
[View ego-browser Full Documentation](../../awesome-skills/introductions/en/ego-browser.md)
