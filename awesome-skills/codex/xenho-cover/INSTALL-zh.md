# 为 Codex 安装 xenho-cover

## 前提条件

- 已安装 [Codex](https://openai.com/codex/)
- 已安装 Git
- Direct 模式（可选）：本机 Codex CLI 已登录（默认出图通道，无需 API key），或有 OpenAI 兼容的图像接口
- 公众号封面拼合（可选）：已安装 Python 及 Pillow

## 安装步骤

### 1. 克隆 xenho-cover 仓库

```bash
git clone https://github.com/PPory/xenho-cover.git ~/.codex/xenho-cover
```

### 2. 创建符号链接

仓库根目录即技能目录，将其链接到 Codex 技能目录：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/xenho-cover
ln -s ~/.codex/xenho-cover ~/.codex/skills/xenho-cover
```

### 3. 验证安装

重启 Codex 后，尝试询问：

- "给这篇文章配个封面"

如果安装成功，Codex 将自动识别并调用该技能。

## 更新

```bash
cd ~/.codex/xenho-cover
git pull
```

## 卸载

```bash
rm -rf ~/.codex/skills/xenho-cover
```

## 获取帮助

- GitHub: https://github.com/PPory/xenho-cover
- 提交问题: https://github.com/PPory/xenho-cover/issues
