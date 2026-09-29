# Zerone Hub Management (zhub-management)

**Zerone Hub Management** 是一个通过 `zhub` CLI 管理 Zerone Hub 资源的技能，覆盖 Agent、Skill、Tool、MCP、Provider+Model 五大资源域的完整增删改查与部署生命周期。

## 标签

🛠️ 效率工具 | ✅ 已验证

## 核心理念
Zerone Hub Management 的设计哲学体现在以下几点：
- **CLI 即接口**：所有 Hub 资源操作统一收敛到 `zhub` 命令行，AI Agent 通过 bash 即可完成全部管理动作，无需触碰 Web UI。
- **安全前置**：每次进入技能先做 Pre-flight 检查（CLI 是否安装、是否登录），凭证类字段（MCP headers、Provider apiKey）只写不读，输出自动脱敏。
- **机器可解析**：约定需要程序化处理时一律使用 `--output json`，避免解析面向人类的表格输出。
- **声明式配置**：Agent、Tool、MCP、Provider 均通过 YAML 文件描述目标状态，create/update 语义清晰。

## 主要功能与工作流

1. **Agent 管理（14 个命令）**：
   - 通过 `agent.yaml` 声明式创建/更新 Agent（含本地化标题、描述、模型、系统提示词）。
   - 关联管理使用专用命令：`set-subagents`、`set-tools`、`set-mcps`、`set-skills`（避免 `update` 全量覆盖）。
   - 完整部署生命周期：`deploy` → `status` → `stop` / `start` → `undeploy`（支持 `--purge` 彻底删除）。

2. **Skill 上传与管理（6 个命令）**：
   - `skill create --from-dir` 打包上传单个技能；`--name` 必填，标题/描述元数据需显式传递（无 frontmatter 回退）。
   - 支持 Bundle（组合技能）整包上传：一个目录含多个嵌套 SKILL.md 即作为一个条目上传，运行时自动注册所有子技能。
   - 自动排除 `.git`、`node_modules`、`dist` 等目录，50MB 体积上限。

3. **Tool 与 MCP 管理**：
   - Tool：名称、标题、描述、`isDefault` 标志的增删改查。
   - MCP：支持 `sse` / `http` 传输，创建前自动 probe 验证配置；headers 在输出中始终以 `<hidden>` 脱敏。

4. **Provider + Model 管理（6 个命令）**：
   - Provider 增删改查与模型列表查看。
   - `provider probe` 支持两种模式：探测已存 Provider，或直接测试一组未保存的配置（base-url + api-key + protocol）。

5. **错误恢复约定**：
   - 明确的退出码表（0 成功 / 3 未授权 / 6 冲突 / 9 网络错误等），Agent 可据此自动决定重试、重新登录或报告用户。

## 技能库概览
- **资源域**：Agent、Skill、Tool、MCP、Provider+Model 五域全覆盖。
- **参考资料**：`references/agent.yaml` 提供 Agent 配置的完整示例（含嵌套 config 与兼容扁平两种形态）。
- **常见陷阱清单**：内置 Common Mistakes 章节，覆盖凭证只写不读、删除前需先 undeploy、技能名全局唯一等关键约束。

## 安装与支持
Zerone Hub Management 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/zhub-management/INSTALL-zh.md)
- [Cursor](../../cursor/zhub-management/INSTALL-zh.md)
- [Codex](../../codex/zhub-management/INSTALL-zh.md)
- [OpenCode](../../opencode/zhub-management/INSTALL-zh.md)
- [OpenClaw](../../openclaw/zhub-management/INSTALL-zh.md)
- [Zerone](../../zerone/zhub-management/INSTALL-zh.md)
- [Qoder](../../qoder/zhub-management/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - zerone-agents/agent-hub](https://github.com/zerone-agents/agent-hub/tree/main/skills/zhub-management)
