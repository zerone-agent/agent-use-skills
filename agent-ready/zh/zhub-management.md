# Zerone Hub Management - Agent-Ready 认证

**Zerone Hub Management** 已经正式通过了 **Agent-Ready** 认证！

该技能来自 `zerone-agents/agent-hub` 官方仓库，通过 `zhub` CLI 让 AI Agent 以纯命令行方式管理 Zerone Hub 的全部资源，覆盖 Agent、Skill、Tool、MCP、Provider+Model 五大资源域。

## 认证亮点

- **官方出品**：由 Zerone 团队开发与维护，与 Hub 后端 API 保持同步演进。
- **五域全覆盖**：Agent（含部署生命周期）、Skill（含 Bundle 整包上传）、Tool、MCP、Provider+Model，一个 CLI 全部搞定。
- **声明式配置**：资源以 YAML 文件描述目标状态，create/update 语义清晰，Agent 易于生成与校验。
- **明确的错误语义**：标准化退出码表（0 成功 / 3 未授权 / 6 冲突 / 9 网络错误等），Agent 可据此自动决策重试或降级。

## 为什么它是 Agent-Ready 的？

Zerone Hub Management 成功满足了 Agent-Ready 认证的所有核心标准：

- **原子化动作开放**：每个资源域的每个操作都是独立的 CLI 子命令，参数显式、无副作用隐藏，Agent 可精确组合调用。
- **结构化反馈**：约定 `--output json` 输出 `{ data, meta }` 包装的可解析 JSON，配合明确的退出码，Agent 始终掌握执行状态。
- **安全护栏**：凭证类字段（MCP headers、Provider apiKey）只写不读、输出自动脱敏为 `<hidden>`；删除 Agent 前强制要求先 undeploy，防止误销毁运行中的实例。
- **经过验证的集成**：内置 Pre-flight 检查（CLI 安装、登录状态）与 Common Mistakes 清单，在 Claude Code、Cursor、Codex、OpenCode、OpenClaw、Zerone、Qoder 等主流平台上验证可用。

---
[查看 Zerone Hub Management 完整文档](../../awesome-skills/introductions/zh/zhub-management.md)
