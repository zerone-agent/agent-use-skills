# Jev Model Router - Agent-Ready 认证

**Jev Model Router** 已经正式通过了 **Agent-Ready** 认证！

该技能来自 `zerone-agents/jev-model-router` 官方仓库，通过 `jev-router` CLI 与 Docker Compose，让 AI Agent 完成 Jev Model Router 的部署、配置与检查，覆盖从 Provider 接入到自动模型选择的完整流程。

## 认证亮点

- **官方出品**：由 Zerone 团队开发与维护，与 Router 运行时、CLI 及 Compose 快速启动保持同步演进。
- **全生命周期覆盖**：部署、schema 发现、Provider/模型配置、凭证轮换、路由检查与运维记录，一个 CLI 全部完成。
- **凭证安全优先**：API Key 只写不读、加密托管存储；默认由用户在自己的终端配置密钥，密钥不进入对话与日志。
- **确定性运维**：带版本的幂等写入与明确的“先测试后启用”工作流，让每次配置变更可复现、可审计。

## 为什么它是 Agent-Ready 的？

Jev Model Router 成功满足了 Agent-Ready 认证的所有核心标准：

- **原子化动作开放**：每个操作都是显式的 CLI 能力（`providers.put`、`models.test`、`route.inspect`、`records.list` 等），通过 `jev-router schema` 发现，输入、副作用与风险均有文档说明。
- **结构化反馈**：机器结果以 JSON 输出到 stdout，诊断信息输出到 stderr；版本与操作 ID 可回读，`data.ok` 区分“配置已保存”与“真实连接成功”。
- **安全护栏**：凭证只写并脱敏、人工在环处理，本地部署默认仅回环绑定，请求失败不做静默重试或模型切换。
- **经过验证的集成**：健康检查、固定连接测试与 `route.inspect` 在启用前逐层验证；文档覆盖 Claude Code、Cursor、Codex、OpenCode、OpenClaw、Zerone、Qoder 等主流平台。

---
[查看 Jev Model Router 完整文档](../../awesome-skills/introductions/zh/jev-router.md)
