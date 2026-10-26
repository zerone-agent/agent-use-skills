# 为 OpenClaw 安装 Jev Model Router

## 前提条件

- 已安装 [OpenClaw](https://openclaw.ai/)
- 已安装 Git
- 已安装 Docker 及 Docker Compose（仅在部署新 Router 实例时需要；管理已有实例不受影响）

## 安装步骤

### 1. 克隆 jev-model-router 仓库

```bash
git clone https://github.com/zerone-agents/jev-model-router.git ~/.openclaw/jev-model-router
```

### 2. 创建符号链接

创建符号链接，使 OpenClaw 能够发现 jev-router 技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/jev-router
ln -s ~/.openclaw/jev-model-router/skills/jev-router ~/.openclaw/skills/jev-router
```

### 3. 验证安装

重启 OpenClaw 后，尝试询问：

- "do you have jev-router?"

如果安装成功，OpenClaw 将自动识别并调用该技能。

## 更新

```bash
cd ~/.openclaw/jev-model-router
git pull
```

## 卸载

```bash
rm -rf ~/.openclaw/skills/jev-router
```

## 获取帮助

- GitHub: https://github.com/zerone-agents/jev-model-router
- 提交问题: https://github.com/zerone-agents/jev-model-router/issues
