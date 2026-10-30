# 为 Claude Code 安装 Feishu CLI

## 前提条件

- 已安装 [Claude Code](https://claude.com/claude-code)
- 已安装 Node.js（npm/npx）
- 已有飞书/Lark 账号（应用创建与授权在浏览器中完成）

## 安装步骤

### 1. 安装 lark-cli CLI

```bash
npm install -g @larksuite/cli
```

### 2. 安装 AI Agent Skills

```bash
npx skills add larksuite/cli -y -g
```

安装器会自动探测已安装的 Agent CLI（包括 Claude Code）并注册 lark-* 技能。

### 3. 配置与登录

```bash
lark-cli config init --new
lark-cli auth login --recommend
```

两条命令都会输出授权链接——请在浏览器中完成设置。

### 4. 验证安装

```bash
lark-cli auth status
```

重启 Claude Code 后，尝试询问：

- "帮我看看明天的飞书日程"

如果安装成功，Claude Code 将自动识别并调用 lark-* 技能。

## 更新

```bash
npm update -g @larksuite/cli
npx skills add larksuite/cli -y -g
```

## 卸载

```bash
rm -rf ~/.claude/skills/lark-*
npm uninstall -g @larksuite/cli
```

## 获取帮助

- GitHub: https://github.com/larksuite/cli
- 提交问题: https://github.com/larksuite/cli/issues
