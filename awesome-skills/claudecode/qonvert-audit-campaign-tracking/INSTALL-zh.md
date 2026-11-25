# 在 Claude Code 中安装广告活动追踪审查技能

## 前置条件

安装 Claude Code 并打开要使用该技能的项目。以下命令需要 `curl`。

## 安装

1. 在项目根目录运行以下命令，下载原始技能文件。

```bash
mkdir -p .claude/skills/audit-campaign-tracking
curl -fsSL \
  'https://raw.githubusercontent.com/Qonvert-Marketing-AI/qonvert-marketing-skills/main/skills/audit-campaign-tracking/SKILL.md' \
  -o .claude/skills/audit-campaign-tracking/SKILL.md
test -s .claude/skills/audit-campaign-tracking/SKILL.md
```

2. 新建 Claude Code 会话，让它使用 Audit Campaign Tracking 检查下面的虚构链接。

```text
https://example.com/rooms?utm_source=google&utm_medium=cpc
```

## 验证

助手应指出缺少 `utm_campaign`。如果要检查真实跳转或转化记录，请单独进行一次经过批准的测试访问。

## 更新与支持

在检查本地修改后，可重新下载技能文件以更新副本。
[查看上游技能][skill]或[报告源文件问题][issues]。

[skill]: https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills/tree/main/skills/audit-campaign-tracking
[issues]: https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills/issues
