# Audit Campaign Tracking

**Audit Campaign Tracking** is an open Qonvert Marketing AI skill for checking the tags in a supplied ad URL.

## Core Philosophy

- Start with a sanitized sample URL and preserve the evidence for each finding.
- Verify real landing-page redirects and conversion recording in separate tests.

## Key Features & Workflow

1. Inspect the three core UTM fields for missing, empty or duplicate values.
2. Identify visible click ID names such as `gclid` and `yclid`.
3. Return a corrected synthetic example and suggest the next attribution test.

## Skills Library Overview

The source contains a single `SKILL.md` for this workflow. The skill needs no provider keys or ad account access.

## Installation & Support

- [Claude Code](../../claudecode/qonvert-audit-campaign-tracking/INSTALL-en.md)
- [Codex](../../codex/qonvert-audit-campaign-tracking/INSTALL-en.md)

[Source and MIT license][repo] · [Optional Qonvert Connect example][check]

[repo]: https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills
[check]: https://qonvert.ai/connect/google-ads?utm_source=agentuse&utm_medium=directory&utm_campaign=google_ads_mcp
