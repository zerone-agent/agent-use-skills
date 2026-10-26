# ego-browser - Agent-Ready 认证

**ego-browser** 已经正式通过了 **Agent-Ready** 认证！

该技能来自 [CitroLabs/ego-lite](https://github.com/CitroLabs/ego-lite)，让任意 AI Agent 通过 `ego-browser` CLI 驱动 ego(lite) Chromium 浏览器——复用你的已登录会话，在隔离的 Space 中执行网页任务。

## 认证亮点

- **一个技能，连接所有 Agent**：安装 ego(lite) 时自动将技能写入已安装的 Agent CLI（Claude Code、Codex、Cursor、OpenClaw、OpenCode 等）；其余场景一条独立命令即可完成安装。
- **代码化接口**：能力（快照、点击、填表、原生 CDP）以预注入的 JavaScript 函数形式开放，一段 heredoc 调用即可执行完整的多步网页流程。
- **人机共存**：任务在带独立标签页的隔离 Space 中运行——Agent 不会劫持用户的标签页、焦点或鼠标，用户可随时旁观或接管。
- **本地优先隐私**：ego(lite) 在用户本机运行，导入的 Profile 本地存储，无需注册账号或邮箱。

## 为什么它是 Agent-Ready 的？

ego-browser 成功满足了 Agent-Ready 认证的所有核心标准：

- **原子化动作开放**：单次 `ego-browser nodejs` 调用即可执行完整多步流程，以确定性的 `@N` 快照引用作为操作目标；`ego-browser skill` 输出与版本匹配的能力指南。
- **结构化反馈**：语义快照文本（`snapshotText()`）、带引用标注的页面树与 `cliLog(...)` 输出，让每一步之后 Agent 都能拿到机器可读的状态。
- **安全护栏**：Space 隔离将 Agent 工作与用户浏览互不干扰；`references/clearing-state.md` 为会波及整个浏览器 Profile 的 Cookie/缓存/存储清理提供护栏；Profile 仅存本地。
- **经过验证的集成**：Onboarding 自动探测并接入已安装的 Agent CLI；已在 Claude Code、Cursor、Codex、OpenCode、OpenClaw、Zerone、Qoder 等主流平台上完成文档验证。

---
[查看 ego-browser 完整文档](../../awesome-skills/introductions/zh/ego-browser.md)
