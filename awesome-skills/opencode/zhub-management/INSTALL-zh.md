# 为 OpenCode 安装 Zerone Hub Management

## 前提条件

- 已安装 OpenCode
- 已安装 Git
- 已安装 Node.js（用于安装 zhub CLI）

## 安装步骤

### 1. 安装 zhub CLI

```bash
npm install -g @zerone-agent/zhub
```

或使用 Bun：

```bash
bun add -g @zerone-agent/zhub
```

登录（token 可在 control-panel Web UI 的 Settings → CLI Tokens 获取）：

```bash
zhub login --url <server-url> --token cli_xxxxxxxxxxxx
```

### 2. 克隆 agent-hub 仓库

```bash
git clone https://github.com/zerone-agents/agent-hub.git ~/.config/opencode/agent-hub
```

### 3. 创建符号链接

创建符号链接，使 OpenCode 能够发现 zhub-management 技能：

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/zhub-management
ln -s ~/.config/opencode/agent-hub/skills/zhub-management ~/.config/opencode/skills/zhub-management
```

### 4. 验证安装

重启 OpenCode 后，尝试询问：

- "do you have zhub-management?"

如果安装成功，OpenCode 将自动识别并调用该技能。

## 更新

```bash
cd ~/.config/opencode/agent-hub
git pull
```

## 卸载

```bash
rm -rf ~/.config/opencode/skills/zhub-management
```

## 获取帮助

- GitHub: https://github.com/zerone-agents/agent-hub
- 提交问题: https://github.com/zerone-agents/agent-hub/issues
