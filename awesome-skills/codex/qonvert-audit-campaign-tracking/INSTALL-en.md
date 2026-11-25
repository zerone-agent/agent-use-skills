# Install Audit Campaign Tracking in Codex

## Prerequisites

Install Codex and open the project where you want to use the skill. The commands use `curl`.

## Installation

1. From the project root, download the canonical skill file.

```bash
mkdir -p .agents/skills/audit-campaign-tracking
curl -fsSL \
  'https://raw.githubusercontent.com/Qonvert-Marketing-AI/qonvert-marketing-skills/main/skills/audit-campaign-tracking/SKILL.md' \
  -o .agents/skills/audit-campaign-tracking/SKILL.md
test -s .agents/skills/audit-campaign-tracking/SKILL.md
```

2. Start a fresh Codex session and ask it to use Audit Campaign Tracking on this fictional URL.

```text
https://example.com/rooms?utm_source=google&utm_medium=cpc
```

## Verify

The agent should find that `utm_campaign` is missing. If you want to check actual redirects or conversion records,
test an approved visit separately.

## Update and support

Repeat the download command to update the copy after reviewing any local edits.
[View the upstream skill][skill] or [report a source issue][issues].

[skill]: https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills/tree/main/skills/audit-campaign-tracking
[issues]: https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills/issues
