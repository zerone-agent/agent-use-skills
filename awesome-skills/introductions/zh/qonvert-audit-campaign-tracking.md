# 广告活动追踪审查

**Audit Campaign Tracking** 是 Qonvert Marketing AI 的开源技能，用于检查所提供广告链接中的追踪参数。

## 核心理念

- 从已去除敏感信息的示例链接开始，为每个发现保留证据。
- 分别验证真实落地页的跳转过程和转化事件记录。

## 主要功能与流程

1. 检查三个核心 UTM 参数是否缺失、为空或重复。
2. 识别链接中可见的点击标识参数，例如 `gclid` 和 `yclid`。
3. 给出修正后的虚构示例，并建议下一步归因验证。

## 技能概览

此流程由一个 `SKILL.md` 文件定义。它无需广告平台密钥，也无需访问广告账户。

## 安装与支持

- [Claude Code](../../claudecode/qonvert-audit-campaign-tracking/INSTALL-zh.md)
- [Codex](../../codex/qonvert-audit-campaign-tracking/INSTALL-zh.md)

[源文件和 MIT 许可][repo] · [可选的 Qonvert Connect 示例][check]

[repo]: https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills
[check]: https://qonvert.ai/connect/google-ads?utm_source=agentuse&utm_medium=directory&utm_campaign=google_ads_mcp
