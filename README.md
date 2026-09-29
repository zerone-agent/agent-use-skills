<p align="center">
  <a href="https://github.com/zerone-agent/agent-use-skills">
    <img alt="AgentUse Skills" src="resources/agent-use.jpg"/>
  </a>
</p>

# AgentUse Skills - Curated AI Skills Library

English | [中文](README-zh.md)

[![Last Updated](https://img.shields.io/badge/updated-Mar%202026-blue.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **AgentUse Skills** provide a set of **reusable and standardized procedural knowledge** for AI Agents.

We have deeply organized existing AI Skills, provided the most convenient installation tutorials, further enhanced and verified compatibility for mainstream Agent frameworks (e.g., Claude Code, Cursor, OpenCode), ensuring that every skill is "ready-to-use" out of the box.

### ✨ Key Advantages

- **Deep Curation**: More than just a collection; we've standardized the functions, prompts, and scripts for each skill.
- **Convenient Installation**: One-click scripts and detailed docs to significantly lower the barrier to entry.
- **Framework Optimization**: Specialized tuning for different Agent frameworks, verified by rigorous automated testing.
- **Progressive Loading**: Efficient metadata discovery ensures support for massive skill libraries without overwhelming the context window.
- **[Agent-Ready Certification](agent-ready/README.md)**: A specialized program for software vendors to bridge traditional applications with the AI Agent ecosystem through standardized APIs and verified integrations.

## 🚀 Getting Started

### Supported Frameworks

AgentUse Skills supports the following AI Agent frameworks:

- **Claude Code**
- **Codex**
- **Cursor**
- **OpenCode**
- **OpenClaw**
- **Qoder**
- **Zerone**

Each framework provides its own skill loading mechanism. Please refer to the installation guides in each skill directory for framework-specific instructions.

## 👑 Agent-Ready SKILLs

> [Agent-Ready](agent-ready/README.md) is a certification program ensuring skills and software work seamlessly with AI Agent platforms.

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[skill-market](agent-ready/en/skill-market.md)** | Automated discovery and installation of specialized agent skills from the Zerone Skill Market. | 👑 Certified |
| **[zhub-management](agent-ready/en/zhub-management.md)** | Manage Zerone Hub resources (Agent, Skill, Tool, MCP, Provider+Model) via the `zhub` CLI, with full CRUD and deployment lifecycle. | 👑 Certified |
| **[Obsidian](agent-ready/en/obsidian-cli.md)** | Knowledge management app with an official CLI (v1.12+) supporting semantic search, graph queries, and vault management — up to 70,000x fewer tokens than traditional MCP approaches. | 👑 Certified |
| **[OfficeCLI](agent-ready/en/officecli.md)** | The world's first Office suite purpose-built for AI agents — create, read, edit, and render Word, Excel, and PowerPoint documents with a single command. | 👑 Certified |
| **[OpenCLI](agent-ready/en/opencli.md)** | CLI tool library that turns websites and apps into deterministic interfaces with 87+ adapters, direct browser control, and zero LLM runtime cost. | 👑 Certified |

## 🎯 SKILL List

> The skill library is being rapidly organized, and more high-quality skills will be available soon!

### Documents & Office

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[minimax-skills](awesome-skills/introductions/en/minimax-skills.md)** | A comprehensive skill library covering frontend, fullstack, mobile, shader programming, and document processing (PDF, PPTX, XLSX, DOCX). | ✅ Verified |
| **[agent-browser](awesome-skills/introductions/en/agent-browser.md)** | A fast Rust-based headless browser automation CLI with Node.js fallback. Enables Agent navigation, interaction, and snapshots. | 🔍 Pending Verification |
| **[github](awesome-skills/introductions/en/github.md)** | Official GitHub CLI integration for managing Issues, PRs, and monitoring CI/CD Action runs. | 🔍 Pending Verification |
| **[content-research-writer](awesome-skills/introductions/en/content-research-writer.md)** | A collaborative writing partner that helps research, outline, draft, and refine content with proper citations while preserving your voice. | ✅ Verified |
| **[deep-research](awesome-skills/introductions/en/deep-research.md)** | Autonomous multi-step deep research skill powered by Gemini Deep Research Agent for market analysis, literature reviews, due diligence, and more — producing detailed, cited reports. | ✅ Verified |
| **[humanizer](awesome-skills/introductions/en/humanizer.md)** | Remove signs of AI-generated writing from text to make it sound more natural and human-written. | ✅ Verified |

### Design & Creativity

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[ui-ux-pro-max-skill](awesome-skills/introductions/en/ui-ux-pro-max-skill.md)** | AI-powered design intelligence with 67 UI styles, 96 color palettes, and 100 industry-specific reasoning rules. | ✅ Verified |
| **[baoyu-skills](awesome-skills/introductions/en/baoyu-skills.md)** | A practical skill collection for AI coding agents covering content creation, image generation, social media publishing, and document processing. | ✅ Verified |
| **[slidev](awesome-skills/introductions/en/slidev.md)** | A presentation slides maker tailored for developers, built on Vite, Vue, and Markdown. | ✅ Verified |

### Dev & Testing

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[agentuse-share](awesome-skills/introductions/en/agentuse-share.md)** | A standardized workflow for contributing new skills to this repository, including research, documentation, and installation guide generation. | ✅ Verified |
| **[superpowers](awesome-skills/introductions/en/superpowers.md)** | Battle-tested 20+ core skills including TDD, debugging, and collaboration patterns. | ✅ Verified |
| **[playwright-skill](awesome-skills/introductions/en/playwright-skill.md)** | Complete browser automation with Playwright. Auto-detects dev servers, performs testing, screenshots, and UX validation. | 🔍 Pending Verification |
| **[prompt-engineering](awesome-skills/introductions/en/prompt-engineering.md)** | Advanced prompt engineering techniques including Few-Shot, CoT, and persuasion principles to maximize Agent performance. | 🔍 Pending Verification |
| **[self-improving-agent](awesome-skills/introductions/en/self-improving-agent.md)** | Captures learnings, errors, and corrections to enable continuous improvement. Promotes learnings to project memory. | 🔍 Pending Verification |
| **[proactive-agent](awesome-skills/introductions/en/proactive-agent.md)** | Transform AI agents into proactive partners that anticipate needs and survive context loss using WAL and Working Buffer protocols. | 🔍 Pending Verification |

### System Automation

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[skill-market](awesome-skills/introductions/en/skill-market.md)** | Automated discovery and installation of specialized agent skills from the Zerone Skill Market. | ✅ Verified |
| **[zhub-management](awesome-skills/introductions/en/zhub-management.md)** | Manage Zerone Hub resources (Agent, Skill, Tool, MCP, Provider+Model) via the `zhub` CLI, with full CRUD and deployment lifecycle. | ✅ Verified |
| **[openclaw-config-guard](awesome-skills/introductions/en/openclaw-config-guard.md)** | A safety-first maintenance skill for auditing and repairing OpenClaw configuration with deterministic validation, backups, rollback, and change reporting. | ✅ Verified |

### Productivity Tools

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[obsidian-cli](awesome-skills/introductions/en/obsidian-cli.md)** | The official Obsidian CLI (v1.12+) that enables AI Agents to control the Obsidian desktop app directly from the terminal, providing full vault manipulation capabilities. | ✅ Verified |
| **[skill-creator](awesome-skills/introductions/en/skill-creator.md)** | Anthropic's official skill creation and iterative optimization tool for creating, testing, evaluating, and improving AI programming skills. | ✅ Verified |
| **[anti-distill](awesome-skills/introductions/en/anti-distill.md)** | A tool to clean your forced-to-write employee AI Skills, keeping core knowledge assets strictly to yourself. | 🔍 Pending Verification |
| **[colleague-skill](awesome-skills/introductions/en/colleague-skill.md)** | A tool that distills a colleague into an AI Skill by automatically collecting Feishu/DingTalk data. | 🔍 Pending Verification |

## 🛠️ Skill Development & Contribution

If you'd like to contribute new skills or improve existing ones:

1. **Structural Specification**: Each skill must follow the `SKILL.md` standard and include necessary `scripts/` and `resources/`.
2. **Verification Flow**: Ensure the skill passed verification in at least one mainstream framework.
3. **Submit PR**: We welcome your contributions via Pull Requests!

## 📖 Core Concept: Why Skills?

| Feature | Skills (This Repo) | Prompts | Project Context |
| :--- | :--- | :--- | :--- |
| **Reusability** | Extremely High; cross-session/project | Low; usually requires rewriting | Medium; workspace-specific |
| **Efficiency** | Progressive loading; saves tokens | Low; grows with conversation | Medium; depends on indexing |
| **Extensibility** | Supports complex scripts/resources | Pure text instructions only | Depends on file mounts |
| **Maintainability** | Centralized version management | Scattered distribution | Fragmented |

## 💡 How to Contribute

We advocate for an **AI-native contribution workflow**. You can use AI Agents along with our `agentuse-share` skill to automate the process of adding new skills.

- **Fast-Track**: Simply provide a GitHub URL to your AI Agent and ask it to use the `agentuse-share` skill.
- **Manual**: Follow our contribution guidelines for structure and bilingual requirements.

For detailed instructions, please see our **[Contributing Guide](CONTRIBUTING.md)**.

## 🔒 Security & Best Practices

⚠️ **Important Notice**: Skills may execute code in your environment. Please ensure you:
- Only install skills from trusted sources (like this repo).
- Read the instructions in `SKILL.md` carefully before production deployment.
- Follow the principle of least privilege, granting only necessary permissions to the Agent.

## 🤝 Acknowledgments & Contributors

A huge thanks to all developers contributing to the AI ecosystem! Special thanks to the following open-source communities for their inspiration and contributions to the field of AI skills:

- [ClawHub](https://clawhub.ai/) — An open skill dock for AI agents, enabling versioned distribution and one-click installation of agent skills.
- [LobeHub](https://lobehub.com/) — An open-source collaborative agent platform for finding, building, and evolving AI agent teammates.
- [ai-skills](https://github.com/sanjay3290/ai-skills) — A collection of ready-to-use AI skills for coding assistants.
- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — A curated list of community-contributed skills for Claude Code.

---
© 2026 AgentUse Team. Released under the GPL-3.0 License.
