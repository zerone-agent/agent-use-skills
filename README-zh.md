<p align="center">
  <a href="https://github.com/zerone-agent/agent-use-skills">
    <img alt="AgentUse Skills" src="resources/agent-use.jpg"/>
  </a>
</p>

# AgentUse Skills - 精选 AI 技能库

[English](README.md) | 中文

[![Last Updated](https://img.shields.io/badge/updated-Mar%202026-blue.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING-zh.md)

> **AgentUse Skills** 为 AI Agent 提供了一套**可复用、可标准化的程序化知识**。

我们对现有的 AI Skill 进行了深度整理，提供了最为便捷的安装教程，并针对主流的 Agent 框架（如 Claude Code, Cursor, OpenCode 等）进行了性能增强与兼容性验证，确保每个技能都能“开箱即用”。

### ✨ 核心优势

- **深度精选与整理**：不仅仅是收集，我们对每个技能的功能、提示词和脚本进行了标准化重构。
- **便捷安装体验**：提供一键式安装脚本与详细的配置文档，大幅降低使用门槛。
- **框架增强与验证**：针对不同的 Agent 框架进行了针对调优，并经过严格的自动化测试验证其稳定性。
- **渐进式加载架构**：采用高效的元数据发现机制，确保在拥有海量技能的同时，不浪费 Agent 的上下文窗口。
- **[Agent-Ready 认证计划](agent-ready/README-zh.md)**：专门为软件厂商提供的认证计划，通过标准化 API 与验证集成，填补传统软件与 AI Agent 生态系统之间的鸿沟。

## 🚀 快速开始

### 支持的框架

AgentUse Skills 支持以下 AI Agent 框架：

- **Claude Code**
- **Codex**
- **Cursor**
- **OpenCode**
- **OpenClaw**
- **Qoder**

每个框架都有其独立的技能加载机制。请参考各技能目录下的安装指南获取具体框架的操作说明。

## 👑 Agent-Ready SKILLs

> [Agent-Ready](agent-ready/README-zh.md) 是一项认证计划，确保技能和软件能够与 AI Agent 平台无缝协作。

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[skill-market](agent-ready/zh/skill-market.md)** | 从 Zerone Skill Market 自动发现并安装专业 Agent 技能。 | 👑 已认证 |
| **[zhub-management](agent-ready/zh/zhub-management.md)** | 通过 `zhub` CLI 管理 Zerone Hub 资源（Agent、Skill、Tool、MCP、Provider+Model），覆盖完整增删改查与部署生命周期。 | 👑 已认证 |
| **[Obsidian](agent-ready/zh/obsidian.md)** | 知识库管理软件，Obsidian 1.12 引入官方 CLI，支持语义搜索、图谱查询与日志管理，Token 消耗减少高达 70,000 倍。 | 👑 已认证 |
| **[OpenCLI](agent-ready/zh/opencli.md)** | CLI 工具库，将网站和应用转化为确定性接口，包含 87+ 适配器、浏览器直控能力，运行时零 LLM 成本。 | 👑 已认证 |

## 🎯 SKILL 列表

> 技能库正在加速整理中，更多高质量技能即将上线！

### 文档与办公

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[minimax-skills](awesome-skills/introductions/zh/minimax-skills.md)** | 综合技能库，覆盖前端、全栈、移动端、着色器开发及文档处理（PDF、PPTX、XLSX、DOCX）。 | ✅ 已验证 |
| **[agent-browser](awesome-skills/introductions/zh/agent-browser.md)** | 基于 Rust 的高性能无头浏览器自动化 CLI。支持 Agent 导航、交互及快照获取。 | 🔍 待验证 |
| **[github](awesome-skills/introductions/zh/github.md)** | GitHub 官方 CLI 集成，支持管理 Issue、PR 及监控 CI/CD 流水线运行详情。 | 🔍 待验证 |
| **[content-research-writer](awesome-skills/introductions/zh/content-research-writer.md)** | 内容写作协作技能，帮助调研、构建大纲、撰写草稿并优化内容，支持引用管理，同时保持你独特的写作风格。 | ✅ 已验证 |
| **[deep-research](awesome-skills/introductions/zh/deep-research.md)** | 自主多步骤深度研究技能，利用 Gemini Deep Research Agent 进行市场分析、文献综述、尽职调查等，生成带引用的详细报告。 | ✅ 已验证 |
| **[humanizer](awesome-skills/introductions/zh/humanizer.md)** | 识别并消除文本中的 AI 写作痕迹，使文字听起来更自然、更具人情味。 | ✅ 已验证 |

### 设计与创意

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[ui-ux-pro-max-skill](awesome-skills/introductions/zh/ui-ux-pro-max-skill.md)** | AI 驱动的设计智能体，提供 67 种 UI 风格、96 种配色方案和 100 条行业特定推理规则。 | ✅ 已验证 |
| **[imagen](awesome-skills/introductions/zh/imagen.md)** | 利用 Google Gemini 的图像生成能力，在 AI 编码会话期间直接生成图像。纯 Python 实现，零依赖。 | 🔍 待验证 |
| **[baoyu-skills](awesome-skills/introductions/zh/baoyu-skills.md)** | 宝玉分享的效率提升技能集，涵盖内容创作、图像生成、社交媒体发布和文档处理等多个维度。 | ✅ 已验证 |
| **[slidev](awesome-skills/introductions/zh/slidev.md)** | 基于 Vite、Vue 和 Markdown 构建的面向开发者的幻灯片制作和演示工具。 | ✅ 已验证 |

### 开发与测试

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[agentuse-share](awesome-skills/introductions/zh/agentuse-share.md)** | 标准化 Skill 贡献工作流，涵盖调研、文档撰写及多平台安装指南生成。 | ✅ 已验证 |
| **[superpowers](awesome-skills/introductions/zh/superpowers.md)** | 20+ 核心技能，涵盖 TDD、调试和协作模式。 | ✅ 已验证 |
| **[playwright-skill](awesome-skills/introductions/zh/playwright-skill.md)** | 基于 Playwright 的全功能浏览器自动化技能，支持自动探测服务器、网页测试、截图及 UX 验证。 | 🔍 待验证 |
| **[prompt-engineering](awesome-skills/introductions/zh/prompt-engineering.md)** | 高级提示词工程模式，涵盖少样本学习、思维链及说服原则，旨在最大化 Agent 执行效率。 | 🔍 待验证 |
| **[self-improving-agent](awesome-skills/introductions/zh/self-improving-agent.md)** | 捕获学习经验、错误和修正建议，实现持续改进。支持将学习成果晋升为项目内存。 | 🔍 待验证 |
| **[proactive-agent](awesome-skills/introductions/zh/proactive-agent.md)** | 将 AI 智能体转变为主动合作伙伴，通过 WAL 和工作缓冲区协议预判需求并应对上下文丢失。 | 🔍 待验证 |

### 系统自动化

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[skill-market](awesome-skills/introductions/zh/skill-market.md)** | 从 Zerone Skill Market 自动发现并安装专业 Agent 技能。 | ✅ 已验证 |
| **[zhub-management](awesome-skills/introductions/zh/zhub-management.md)** | 通过 `zhub` CLI 管理 Zerone Hub 资源（Agent、Skill、Tool、MCP、Provider+Model），覆盖完整增删改查与部署生命周期。 | ✅ 已验证 |
| **[openclaw-config-guard](awesome-skills/introductions/zh/openclaw-config-guard.md)** | 一个以安全为优先的配置维护技能，用于对 OpenClaw 配置进行审计与修复，并提供确定性校验、备份、回滚和变更报告能力。 | ✅ 已验证 |

### 效率工具

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[obsidian](awesome-skills/introductions/zh/obsidian.md)** | 专为 Obsidian 知识管理工具设计的 Agent Skills，兼容 Claude Code、Codex CLI 等 AI 编码助手。 | ✅ 已验证 |
| **[skill-creator](awesome-skills/introductions/zh/skill-creator.md)** | Anthropic 官方技能创建与迭代优化工具，实现从构思到部署的完整工作流。 | ✅ 已验证 |
| **[anti-distill](awesome-skills/introductions/zh/anti-distill.md)** | 专为保护员工核心知识资产设计的工具，"清洗"被迫写出的工作 Skill，核心经验留给自己。 | 🔍 待验证 |
| **[colleague-skill](awesome-skills/introductions/zh/colleague-skill.md)** | 将同事"蒸馏"为 AI Skill，通过自动采集飞书/钉钉数据生成数字化同事。 | 🔍 待验证 |

## 🛠️ 技能开发与贡献

如果您想贡献新的技能或改进现有技能：

1. **结构规范**：每个技能需遵循 `SKILL.md` 标准，并包含必要的 `scripts/` 与 `resources/`。
2. **验证流程**：确保技能在至少一个主流框架中通过验证。
3. **提交 PR**：欢迎通过 Pull Request 的形式提交您的贡献。

## 📖 核心概念：为什么选择 Skills？

| 特性 | Skills (本仓库) | 提示词 (Prompts) | 项目上下文 (Projects) |
| :--- | :--- | :--- | :--- |
| **复用性** | 极高，跨会话、跨项目通用 | 低，通常需要重写 | 中，局限于特定工作区 |
| **效率** | 渐进式加载，节省 Token | 低，随对话增长消耗 | 中，依赖索引 |
| **扩展性** | 支持携带复杂脚本与资源 | 仅限文本指令 | 依赖文件挂载 |
| **维护性** | 集中版本化管理 | 零散分布 | 碎片化 |

## 💡 如何贡献

我们倡导 **AI 原生（AI-native）的贡献流程**。你可以配合 AI Agent 使用我们内置的 `agentuse-share` 技能来自动化新增技能的过程。

- **快速通道**：只需向你的 AI Agent 提供一个 GitHub 链接，并让它调用 `agentuse-share` 技能。
- **手动贡献**：遵循我们的目录结构规范与双语要求进行提交。

详细指南请阅读我们的 **[贡献指南](CONTRIBUTING-zh.md)**。

## 🔒 安全与最佳实践

⚠️ **重要提示**：技能可能会在您的环境中执行代码。请务必：
- 仅安装来自受信任来源（如本仓库）的技能。
- 在生产环境部署前，仔细阅读 `SKILL.md` 中的指令。
- 遵循最小权限原则，仅授予 Agent 必要的操作权限。

## 🤝 鸣谢与贡献者

非常感谢所有为 AI 生态做出贡献的开发者！特别感谢以下开源社区为 AI 技能领域提供的灵感与贡献：

- [ClawHub](https://clawhub.ai/) — 面向 AI Agent 的开放式技能平台，支持技能的版本化分发与一键安装。
- [LobeHub](https://lobehub.com/) — 开源协作式 Agent 平台，用于发现、构建和进化 AI Agent 队友。
- [ai-skills](https://github.com/sanjay3290/ai-skills) — 面向编码助手的即用型 AI 技能合集。
- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — 社区贡献的 Claude Code 技能精选列表。

---
© 2026 AgentUse Team. Released under the GPL-3.0 License.
