# 为 Cursor 安装 Oil Visual

## 前提条件

- 已安装 [Cursor](https://cursor.com/)
- 已安装 Git
- 宿主可达的图像工具（如本机已安装并登录的 Codex CLI——机器级依赖），或用于粘贴编译后提示词的外部图像生成器
- 透明插画抠像（可选）：已安装 Python 及 Pillow

## 安装步骤

### 1. 克隆 oil-visual 仓库

```bash
git clone https://github.com/oil-oil/oil-visual.git ~/.cursor/oil-visual
```

### 2. 创建符号链接

仓库根目录即技能目录，将其链接到 Cursor 技能目录：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/oil-visual
ln -s ~/.cursor/oil-visual ~/.cursor/skills/oil-visual
```

### 3. 验证安装

重启 Cursor 后，尝试询问：

- "Use $oil-visual to draw an explainer image"

如果安装成功，Cursor 将自动识别并调用该技能。

## 更新

```bash
cd ~/.cursor/oil-visual
git pull
```

## 卸载

```bash
rm -rf ~/.cursor/skills/oil-visual
```

## 获取帮助

- GitHub: https://github.com/oil-oil/oil-visual
- 提交问题: https://github.com/oil-oil/oil-visual/issues
