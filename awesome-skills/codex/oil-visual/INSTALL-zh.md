# 为 Codex 安装 Oil Visual

## 前提条件

- 已安装并登录 [Codex](https://openai.com/codex/)（图像生成使用其内置 GPT Image）
- 已安装 Git
- 透明插画抠像（可选）：已安装 Python 及 Pillow

## 安装步骤

### 1. 克隆 oil-visual 仓库

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.codex/skills/oil-visual
```

### 2. 验证安装

技能直接克隆进 Codex 技能目录。重启 Codex 后，尝试询问：

- "Use $oil-visual to draw an explainer image"

如果安装成功，Codex 将自动识别并调用该技能。

## 更新

```bash
cd ~/.codex/skills/oil-visual
git pull
```

## 卸载

```bash
rm -rf ~/.codex/skills/oil-visual
```

## 获取帮助

- GitHub: https://github.com/oil-oil/oil-visual
- 提交问题: https://github.com/oil-oil/oil-visual/issues
