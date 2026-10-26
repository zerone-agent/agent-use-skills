# Jev Model Router (jev-router)

**Jev Model Router** is an operations skill for deploying, configuring, and inspecting the Jev Model Router through the `jev-router` CLI, covering Docker Compose deployment, providers, model cards, routing preferences, connection tests, and automatic or explicit model selection.

## Tags

💻 Dev & Testing | ✅ Verified

## Core Philosophy
- **Schema-first discovery**: Run `jev-router schema` against the target instance before operating; every capability's input, effects, role, and risk are discovered at runtime instead of assumed.
- **Safe, idempotent writes**: Configuration changes use complete replacement resources with `--expected-version` and `--idempotency-key`, so retries never duplicate or corrupt state.
- **Credential safety by default**: API keys are write-only with encrypted managed storage; by default the user runs credential configuration in their own terminal, and keys never enter conversations, shell arguments, or logs.
- **Verify, don't assume**: Saved configuration, successful connectivity, and successful generation are distinct states — `models.test`, `route.inspect`, and health fields are used to prove each one.

## Key Features & Workflow

1. **Deploy**: Docker Compose quickstart with distinct settings/inference tokens and an encryption master key; container health plus `schema` and `status.get` checks must pass before any configuration.
2. **Discover**: `jev-router schema <capability>` exposes inputs, effects, roles, examples, and risks for the target instance, keeping operations aligned with the actual runtime version.
3. **Configure and verify**: Create providers and disabled model cards, run `models.test`, then enable; configure `decision.put` for multi-candidate automatic routing and inspect selection with `route.inspect` before real traffic.
4. **Managed credentials**: Write-only `api_key` or server-resolved `secret_ref`, masked read-back, rotation without restart, and strict ownership boundaries between provider and decision references.
5. **Routing operations**: Automatic (`auto`) or explicit model selection, reasoning controls, Anthropic Messages compatibility, a human dashboard, routing records with decision usage, and Auto fallback inspection.

## Skills Library Overview
- **Deployment & discovery**: Compose quickstart, CLI schema discovery, and instance status checks.
- **Configuration & credentials**: Versioned resource writes, encrypted managed keys, and connection testing.
- **Routing & observability**: Auto/explicit selection, reasoning controls, health recovery, routing records, and decision-cost accounting.

## Installation & Support
Jev Model Router supports the following AI editors and platforms:
- [Claude Code](../../claudecode/jev-router/INSTALL-en.md)
- [Cursor](../../cursor/jev-router/INSTALL-en.md)
- [Codex](../../codex/jev-router/INSTALL-en.md)
- [OpenCode](../../opencode/jev-router/INSTALL-en.md)
- [OpenClaw](../../openclaw/jev-router/INSTALL-en.md)
- [Zerone](../../zerone/jev-router/INSTALL-en.md)
- [Qoder](../../qoder/jev-router/INSTALL-en.md)

---
For more information, visit: [GitHub - zerone-agents/jev-model-router](https://github.com/zerone-agents/jev-model-router/tree/main/skills/jev-router)
