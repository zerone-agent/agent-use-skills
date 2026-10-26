# Installing meeting-minutes for Kiro

## Prerequisites

- [Kiro](https://kiro.dev/) installed
- macOS with Apple Silicon (required by mlx-whisper)
- Python 3.10+ installed
- [ffmpeg](https://ffmpeg.org/) installed (`brew install ffmpeg`)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.kiro/agent-use-skills
```

### 2. Copy the Skill into the Kiro Skills Directory

Kiro reads `~/.kiro/skills` directly; copy (do not symlink) the skill folder:

```bash
mkdir -p ~/.kiro/skills
rm -rf ~/.kiro/skills/meeting-minutes
cp -R ~/.kiro/agent-use-skills/awesome-skills/skills/meeting-minutes ~/.kiro/skills/meeting-minutes
```

### 3. Verify Installation

Restart Kiro, then try asking:

- "对 meeting.m4a 做会议纪要"

On first use, the skill automatically creates a Python virtual environment at `~/whisper-env` and installs mlx-whisper.

## Updating

```bash
cd ~/.kiro/agent-use-skills
git pull
rm -rf ~/.kiro/skills/meeting-minutes
cp -R awesome-skills/skills/meeting-minutes ~/.kiro/skills/meeting-minutes
```

## Uninstallation

```bash
rm -rf ~/.kiro/skills/meeting-minutes
```

## Getting Help

- GitHub: https://github.com/aws-samples/sample-for-kiro-meeting-minutes-skill
- Report issues: https://github.com/aws-samples/sample-for-kiro-meeting-minutes-skill/issues
