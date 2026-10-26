# Jev Model Router - Agent-Ready Certification

**Jev Model Router** has officially passed the **Agent-Ready** certification!

Originating from the official `zerone-agents/jev-model-router` repository, this skill lets AI agents deploy, configure, and inspect the Jev Model Router through the `jev-router` CLI and Docker Compose, from provider setup to automatic model selection.

## Certification Highlights

- **Officially Built**: Developed and maintained by the Zerone team, evolving in lockstep with the Router runtime, CLI, and Compose quickstart.
- **Full Lifecycle Coverage**: Deployment, schema discovery, provider/model configuration, credential rotation, routing inspection, and operations records — all through one CLI.
- **Safety-First Credentials**: Write-only API keys with encrypted managed storage; by default users configure secrets in their own terminal, keeping keys out of conversations and logs.
- **Deterministic Operations**: Versioned, idempotent writes and an explicit test-then-enable workflow make every configuration change reproducible and auditable.

## Why is it Agent-Ready?

Jev Model Router successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: Every operation is an explicit CLI capability (`providers.put`, `models.test`, `route.inspect`, `records.list`, and more) discovered via `jev-router schema`, with documented inputs, effects, and risks.
- **Structured Feedback**: Machine results go to stdout as JSON while diagnostics go to stderr; version and operation IDs are read back, and `data.ok` distinguishes saved configuration from real connectivity.
- **Security Guardrails**: Write-only, masked credentials with human-in-the-loop handling, loopback-only defaults for local deployment, and no silent retries or model switching on failed requests.
- **Verified Integration**: Health checks, fixed connection tests, and `route.inspect` validate each layer before enablement; documented for major platforms including Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, and Qoder.

---
[View Jev Model Router Full Documentation](../../awesome-skills/introductions/en/jev-router.md)
