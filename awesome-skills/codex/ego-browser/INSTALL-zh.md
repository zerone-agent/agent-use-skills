# 为 Codex 安装 ego-browser

## 前提条件

- 已安装 [Codex](https://openai.com/codex/)
- 已安装 Node.js（用于 `npx`）
- macOS 系统（官网提供 Windows beta 版）

## 安装步骤

### 1. 安装技能

```bash
npx skills add github:CitroLabs/ego-lite/skills/ego-browser
```

安装器会自动探测已安装的 Agent CLI（包括 Codex）并注册技能。

### 2. 安装 ego lite 浏览器

技能依赖 ego lite 浏览器，并可自行引导安装：

```bash
sh ~/.codex/skills/ego-browser/scripts/install.sh
```

随后在 ego lite 应用中完成首次启动 onboarding：导入浏览器数据，并将 `ego-browser` 命令注册到 PATH（通常位于 `~/.local/bin`）。

如果 Codex 未自动识别技能，可手动创建符号链接：

```bash
mkdir -p ~/.codex/skills
rm -f ~/.codex/skills/ego-browser
ln -s ~/.local/share/ego/ego-skills ~/.codex/skills/ego-browser
```

### 3. 验证安装

```bash
export PATH="$HOME/.local/bin:$PATH"
command -v ego-browser
ego-browser skill
```

重启 Codex 后，尝试询问：

- "do you have ego-browser?"

如果安装成功，Codex 将自动识别并调用该技能。

## 更新

```bash
ego-browser upgrade
```

技能由 ego lite 应用统一管理，符号链接始终指向当前生效版本。

## 卸载

```bash
rm -f ~/.codex/skills/ego-browser
```

如需彻底移除，请从「应用程序」中删除 `ego lite` 应用。

## 获取帮助

- 官网: https://lite.ego.app/
- 文档: https://lite.ego.app/document/en/docs/ego-browser
- GitHub: https://github.com/CitroLabs/ego-lite
- 提交问题: https://github.com/CitroLabs/ego-lite/issues
