# Zerone Hub Management - Agent-Ready Certification

**Zerone Hub Management** has officially passed the **Agent-Ready** certification!

Originating from the official `zerone-agents/agent-hub` repository, this skill lets AI agents manage every Zerone Hub resource purely through the `zhub` CLI, covering five resource domains: Agent, Skill, Tool, MCP, and Provider+Model.

## Certification Highlights

- **Officially Built**: Developed and maintained by the Zerone team, evolving in lockstep with the Hub backend API.
- **Full Five-Domain Coverage**: Agents (including deployment lifecycle), Skills (including bundle uploads), Tools, MCPs, and Providers+Models — all through one CLI.
- **Declarative Configuration**: Resources are described as YAML files with clear create/update semantics, making them easy for agents to generate and validate.
- **Explicit Error Semantics**: A standardized exit-code table (0 success / 3 unauthorized / 6 conflict / 9 network error, etc.) lets agents automatically decide whether to retry, re-login, or escalate.

## Why is it Agent-Ready?

Zerone Hub Management successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: Every operation in every resource domain is an independent CLI subcommand with explicit parameters and no hidden side effects, allowing agents to compose calls precisely.
- **Structured Feedback**: The `--output json` convention returns parseable JSON wrapped in `{ data, meta }`, and together with explicit exit codes, the agent always knows the execution state.
- **Security Guardrails**: Credential fields (MCP headers, Provider apiKey) are write-only and automatically masked as `<hidden>` in output; deleting an agent requires an undeploy first, preventing accidental destruction of running instances.
- **Verified Integration**: Built-in pre-flight checks (CLI installation, login status) and a Common Mistakes checklist, validated across major platforms including Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, and Qoder.

---
[View Zerone Hub Management Full Documentation](../../awesome-skills/introductions/en/zhub-management.md)
