# Jev Model Router (jev-router)

**Jev Model Router** 是一个用于部署、配置和检查 Jev Model Router 的运维技能，通过 `jev-router` CLI 覆盖 Docker Compose 部署、Provider、模型卡片、路由偏好、连接测试以及自动/显式模型选择。

## 标签

💻 开发与测试 | ✅ 已验证

## 核心理念
- **Schema 先行发现**：操作前先对目标实例运行 `jev-router schema`，在运行时发现每个能力的输入、副作用、角色与风险，而不是凭空假设。
- **安全幂等写入**：配置变更使用完整替换资源，并携带 `--expected-version` 与 `--idempotency-key`，重试不会重复或破坏状态。
- **凭证默认安全**：API Key 只写不读，采用加密托管存储；默认由用户在自己的终端执行凭证配置，密钥绝不进入对话、Shell 参数或日志。
- **验证而非假设**：配置已保存、连接成功、生成成功是三种不同状态——分别通过 `models.test`、`route.inspect` 和健康字段逐一证实。

## 主要功能与工作流

1. **部署**：Docker Compose 快速启动，配置独立的 settings/inference 令牌与加密主密钥；任何配置之前，容器健康检查以及 `schema`、`status.get` 必须先通过。
2. **发现**：`jev-router schema <capability>` 展示目标实例各能力的输入、副作用、角色、示例与风险，使操作始终与实际运行时版本对齐。
3. **配置与验证**：先创建 Provider 和禁用态模型卡片，运行 `models.test` 后再启用；为多候选自动路由配置 `decision.put`，并在真实流量前用 `route.inspect` 检查选择结果。
4. **托管凭证**：只写 `api_key` 或服务端解析的 `secret_ref`，读取回显脱敏，轮换无需重启，Provider 与 decision 引用严格隔离、不可互换。
5. **路由运维**：自动（`auto`）或显式模型选择、推理控制、Anthropic Messages 兼容、人类管理面板、含 decision 用量的路由记录，以及 Auto fallback 检查。

## 技能库概览
- **部署与发现**：Compose 快速启动、CLI schema 发现与实例状态检查。
- **配置与凭证**：带版本的资源写入、加密托管密钥与连接测试。
- **路由与可观测**：自动/显式选择、推理控制、健康恢复、路由记录与 decision 成本核算。

## 安装与支持
Jev Model Router 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/jev-router/INSTALL-zh.md)
- [Cursor](../../cursor/jev-router/INSTALL-zh.md)
- [Codex](../../codex/jev-router/INSTALL-zh.md)
- [OpenCode](../../opencode/jev-router/INSTALL-zh.md)
- [OpenClaw](../../openclaw/jev-router/INSTALL-zh.md)
- [Zerone](../../zerone/jev-router/INSTALL-zh.md)
- [Qoder](../../qoder/jev-router/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - zerone-agents/jev-model-router](https://github.com/zerone-agents/jev-model-router/tree/main/skills/jev-router)
