# ego-browser

**ego-browser** 是 [ego(lite)](https://lite.ego.app/) 的浏览器自动化技能。ego(lite) 是一款为人与 AI Agent 共同设计的 Chromium 浏览器，Agent 通过 `ego-browser` CLI 驱动浏览器：打开网站、填写表单、点击按钮、截图、提取页面数据、复用已登录会话、执行 Web 应用测试——全部在隔离的 Space 中进行，绝不会劫持你自己的标签页。

## 标签

🛠️ 效率工具 | ✅ 已验证

## 核心理念
- **代码优先控制**：Agent 每个任务只写一段 Node.js 脚本，`ego-browser` 一次调用执行完整流程——更少的模型轮次与 Token 消耗，多步任务比逐动作 CLI 循环快 20–50%。
- **Space 隔离**：每个任务在 ego(lite) 内的独立 Space（隔离工作区）中运行。Agent 不会切换你的标签页、抢占键盘焦点或接管鼠标；你可随时旁观或接管。
- **复用真实登录态**：基于 Chromium 构建，ego(lite) 一键导入 Chrome 配置，Agent 直接继承 Gmail、Notion、LinkedIn 及内部工具的登录状态，无需重复认证。
- **语义化快照**：自研 Chromium 引擎生成页面快照，可深入跨域 iframe、Shadow DOM 与嵌入式组件（Stripe、Salesforce、Intercom），而普通 fetch 或注入脚本通常无法触达。
- **自举式安装**：技能负责安装与升级其依赖的浏览器，并打印与已装版本匹配的使用指南，确保 Agent 始终按当前能力执行。

## 主要功能与工作流

1. **引导启动**：任何浏览器任务前先运行 `ego-browser skill`——输出与已装 ego lite 版本匹配的使用指南；浏览器缺失或命令未知时由 `references/install.md` 兜底处理。
2. **核心循环**：单个 heredoc 内完成——复用或创建 Task Space、打开标签页、读取语义快照（`snapshotText()`）、按 `@N` 引用或 CSS 选择器操作页面、用 `cliLog(...)` 汇报结果。
3. **登录态自动化**：在浏览器中登录一次，所有 Agent 即可复用会话完成日常网页工作——调研、填表、数据采集、QA 与 dogfooding。
4. **站点经验积累**：内置按站点沉淀的配方（GitHub、Google、X），位于 `learnings/` 目录，含可复用的 browser-tools 脚本与笔记。
5. **安全维护**：`references/clearing-state.md` 为清理 Cookie/缓存/存储提供护栏（部分清理会波及整个浏览器 Profile）；`ego-browser upgrade` 保持运行时与指南同步。

## 技能库概览
- **参考资料**：安装升级指南与状态清理护栏。
- **脚本**：`scripts/install.sh` 提供一条命令完成 macOS 端 ego lite 安装。
- **站点经验**：github、google、x-com 的 browser-tools 脚本与笔记，覆盖常见自动化目标。

## 安装与支持
ego-browser 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/ego-browser/INSTALL-zh.md)
- [Cursor](../../cursor/ego-browser/INSTALL-zh.md)
- [Codex](../../codex/ego-browser/INSTALL-zh.md)
- [OpenCode](../../opencode/ego-browser/INSTALL-zh.md)
- [OpenClaw](../../openclaw/ego-browser/INSTALL-zh.md)
- [Zerone](../../zerone/ego-browser/INSTALL-zh.md)
- [Qoder](../../qoder/ego-browser/INSTALL-zh.md)

---
了解更多信息，请访问：[ego(lite) 官网](https://lite.ego.app/) | [GitHub - CitroLabs/ego-lite](https://github.com/CitroLabs/ego-lite)
