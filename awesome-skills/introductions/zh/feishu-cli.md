# Feishu CLI (feishu-cli)

**Feishu CLI** 打包了飞书官方开源的 [Lark/Feishu CLI](https://github.com/larksuite/cli)（`lark-cli`，MIT，larksuite 团队维护）与 26 个 AI Agent Skills：200+ 命令覆盖 18 个业务域，Agent 可以直接读消息、查日历、写文档、建多维表格、发邮件、处理审批，端到端完成飞书内的任务，零额外配置。

## 标签

🛠️ 效率工具 | 🔍 待验证

## 核心理念
- **Agent 原生设计**：每个命令都用真实 Agent 实测，参数精简、默认值智能、输出结构化，最大化调用成功率；技能开箱兼容主流 AI 工具。
- **三层命令体系**：快捷命令（人类与 AI 友好）→ API 命令（与平台同步）→ 原始 API（全量覆盖），Agent 可按任务选择合适的粒度。
- **双身份且边界清晰**：应用身份（Bot）免用户授权即可使用，但无法访问个人数据；用户身份（`lark-cli auth login --recommend`）解锁个人日历、消息与文档——涉及个人数据的操作必须使用用户身份。
- **安全可控**：输入注入防护、终端输出脱敏、操作系统原生钥匙串凭证存储。

## 主要功能与工作流

1. **安装**：`npx @larksuite/cli@latest install` 安装 CLI，再执行 `npx skills add larksuite/cli -y -g` 向已安装的 Agent 注册技能集。
2. **配置与登录**：`lark-cli config init --new`（一次性引导创建应用）与 `lark-cli auth login --recommend`（自动选择常用 scope），用 `lark-cli auth status` 验证。
3. **领域技能**：`lark-shared`（自动加载：配置、认证、scope、安全规则）+ 日历、IM、文档、云空间、Markdown、表格、幻灯片、多维表格、任务、邮箱、通讯录、知识库、实时事件、会议/妙记、画板、考勤、审批、OKR。
4. **工作流与扩展**：内置会议纪要汇总、站会报告工作流；`lark-openapi-explorer` 探索底层 API；`lark-skill-maker` 创建自定义技能。

## 技能库概览
- **核心业务域**：消息、文档、云空间、Markdown、表格、幻灯片、多维表格、任务、知识库、通讯录、邮箱、日历、会议、考勤、审批、OKR、事件订阅、画板。
- **基础设施**：`lark-shared`（所有其他技能自动加载）、`lark-openapi-explorer`、`lark-skill-maker`。
- **工作流**：`lark-workflow-meeting-summary`、`lark-workflow-standup-report`。

## 安装与支持
Feishu CLI 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/feishu-cli/INSTALL-zh.md)
- [Cursor](../../cursor/feishu-cli/INSTALL-zh.md)
- [Codex](../../codex/feishu-cli/INSTALL-zh.md)
- [OpenCode](../../opencode/feishu-cli/INSTALL-zh.md)
- [OpenClaw](../../openclaw/feishu-cli/INSTALL-zh.md)
- [Zerone](../../zerone/feishu-cli/INSTALL-zh.md)
- [Qoder](../../qoder/feishu-cli/INSTALL-zh.md)

技能经官方 `npx skills add` 通道安装（自动探测已安装的 Agent CLI）；`lark-cli` 属机器级依赖，与宿主平台无关。未列出平台为待验证状态。

---
了解更多信息，请访问：[GitHub - larksuite/cli](https://github.com/larksuite/cli)
