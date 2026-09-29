# Zerone Hub Management (zhub-management)

**Zerone Hub Management** is a skill for managing Zerone Hub resources via the `zhub` CLI, covering full CRUD and deployment lifecycles across five resource domains: Agent, Skill, Tool, MCP, and Provider+Model.

## Tags

🛠️ Productivity Tools | ✅ Verified

## Core Philosophy
The design philosophy of Zerone Hub Management:
- **CLI as the interface**: All Hub resource operations are unified under the `zhub` command line, so AI agents can perform every management action through bash without touching the web UI.
- **Safety first**: A pre-flight check runs on every entry (CLI installed? logged in?). Credential fields (MCP headers, Provider apiKey) are write-only and masked in output.
- **Machine-parseable**: `--output json` is the convention whenever output needs programmatic processing, avoiding fragile parsing of human-oriented tables.
- **Declarative configuration**: Agents, Tools, MCPs, and Providers are described as YAML files with clear create/update semantics.

## Key Features & Workflow

1. **Agent management (14 commands)**:
   - Declarative create/update via `agent.yaml` (localized titles, descriptions, model, system prompt).
   - Associations managed through dedicated commands: `set-subagents`, `set-tools`, `set-mcps`, `set-skills` (avoiding full-config overwrite by `update`).
   - Full deployment lifecycle: `deploy` → `status` → `stop` / `start` → `undeploy` (with `--purge` for permanent deletion).

2. **Skill upload & management (6 commands)**:
   - `skill create --from-dir` packs and uploads a single skill; `--name` is required and metadata flags must be passed explicitly (no frontmatter fallback).
   - Bundle (composite skill) uploads: a directory containing multiple nested SKILL.md files is packed as one entry, with all sub-skills auto-registered at runtime.
   - `.git`, `node_modules`, `dist`, etc. are automatically excluded; 50MB size cap.

3. **Tool & MCP management**:
   - Tools: CRUD over name, title, description, and the `isDefault` flag.
   - MCPs: `sse` / `http` transports with automatic probe before create; headers are always masked as `<hidden>` in output.

4. **Provider + Model management (6 commands)**:
   - Provider CRUD and model listing.
   - `provider probe` supports two modes: probe a stored provider, or test an unsaved config directly (base-url + api-key + protocol).

5. **Error recovery conventions**:
   - An explicit exit-code table (0 success / 3 unauthorized / 6 conflict / 9 network error, etc.) lets agents decide automatically whether to retry, re-login, or report to the user.

## Skills Library Overview
- **Resource domains**: Full coverage of Agent, Skill, Tool, MCP, and Provider+Model.
- **References**: `references/agent.yaml` provides a complete agent configuration example (both nested `config` and compatible flat shapes).
- **Common mistakes list**: A built-in Common Mistakes section covers key constraints such as write-only credentials, undeploy-before-delete, and globally unique skill names.

## Installation & Support
Zerone Hub Management supports the following AI editors and platforms:
- [Claude Code](../../claudecode/zhub-management/INSTALL-en.md)
- [Cursor](../../cursor/zhub-management/INSTALL-en.md)
- [Codex](../../codex/zhub-management/INSTALL-en.md)
- [OpenCode](../../opencode/zhub-management/INSTALL-en.md)
- [OpenClaw](../../openclaw/zhub-management/INSTALL-en.md)
- [Zerone](../../zerone/zhub-management/INSTALL-en.md)
- [Qoder](../../qoder/zhub-management/INSTALL-en.md)

---
For more information, visit: [GitHub - zerone-agents/agent-hub](https://github.com/zerone-agents/agent-hub/tree/main/skills/zhub-management)
