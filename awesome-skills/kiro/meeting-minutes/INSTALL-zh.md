# 为 Kiro 安装 meeting-minutes

## 前提条件

- 已安装 [Kiro](https://kiro.dev/)
- macOS Apple Silicon 系统（mlx-whisper 必需）
- 已安装 Python 3.10+
- 已安装 [ffmpeg](https://ffmpeg.org/)（`brew install ffmpeg`）

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.kiro/agent-use-skills
```

### 2. 复制技能到 Kiro 技能目录

Kiro 直接读取 `~/.kiro/skills`，请复制（而非符号链接）技能目录：

```bash
mkdir -p ~/.kiro/skills
rm -rf ~/.kiro/skills/meeting-minutes
cp -R ~/.kiro/agent-use-skills/awesome-skills/skills/meeting-minutes ~/.kiro/skills/meeting-minutes
```

### 3. 验证安装

重启 Kiro 后，尝试询问：

- "对 meeting.m4a 做会议纪要"

首次使用时，技能会自动在 `~/whisper-env` 创建 Python 虚拟环境并安装 mlx-whisper。

## 更新

```bash
cd ~/.kiro/agent-use-skills
git pull
rm -rf ~/.kiro/skills/meeting-minutes
cp -R awesome-skills/skills/meeting-minutes ~/.kiro/skills/meeting-minutes
```

## 卸载

```bash
rm -rf ~/.kiro/skills/meeting-minutes
```

## 获取帮助

- GitHub: https://github.com/aws-samples/sample-for-kiro-meeting-minutes-skill
- 提交问题: https://github.com/aws-samples/sample-for-kiro-meeting-minutes-skill/issues
