# Feishu CLI - Agent-Ready 认证

**Feishu CLI** 已经正式通过了 **Agent-Ready** 认证！

该技能集来自飞书官方 [larksuite/cli](https://github.com/larksuite/cli) 仓库（MIT，17.9k stars），通过 `lark-cli` 让 AI Agent 端到端操作飞书/Lark——26 个 AI Agent Skills、200+ 命令覆盖 18 个业务域，从读消息到批审批全部完成。

## 认证亮点

- **官方出品**：由 larksuite 团队维护，与飞书开放平台同步演进；26 个技能随 CLI 版本严格配套。
- **业务域全覆盖**：消息、文档、云空间、Markdown、表格、幻灯片、多维表格、任务、知识库、通讯录、邮箱、日历、会议/妙记、考勤、审批、OKR、实时事件、画板——200+ 精选命令集于一身。
- **Agent 原生设计**：每个命令均经真实 Agent 实测，参数精简、默认值智能、输出结构化；三层命令体系（快捷命令 → API 命令 → 原始 API）让 Agent 按任务选择合适粒度。
- **默认安全**：Bot/User 双身份边界清晰，凭证存于操作系统原生钥匙串，内置输入注入防护与终端输出脱敏。

## 为什么它是 Agent-Ready 的？

Feishu CLI 成功满足了 Agent-Ready 认证的所有核心标准：

- **原子化动作开放**：每个操作都是显式的 `lark-cli` 子命令，输出机器可读的结构化数据；`lark-shared`（所有技能自动加载）统一认证、scope 与安全规则。
- **结构化反馈**：结构化输出配合 `lark-cli auth status` 与 doctor 式体检，执行状态始终可观测；Bot/User 身份路由显式明确，Agent 始终清楚每次调用使用的权限。
- **安全护栏**：涉及个人数据的操作必须走用户身份 + OAuth（`lark-cli auth login --recommend`），凭证仅存操作系统钥匙串，输入/输出脱敏内置于 CLI。
- **经过验证的集成**：官方 `npx skills add` 通道自动探测已安装的 Agent CLI 并注册技能；已在 Claude Code、Cursor、Codex、OpenCode、OpenClaw、Zerone、Qoder 等主流平台完成文档验证。

---
[查看 Feishu CLI 完整文档](../../awesome-skills/introductions/zh/feishu-cli.md)
