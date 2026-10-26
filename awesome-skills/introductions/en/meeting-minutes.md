# Meeting Minutes (meeting-minutes)

**Meeting Minutes** is an official AWS Kiro sample skill that transcribes meeting recordings — audio (.m4a/.mp3/.wav/.flac) or video (.mp4/.mkv/.webm) — into structured Chinese meeting minutes using mlx-whisper (whisper-large-v3-turbo), with optional work daily report generation.

## Tags

🗂️ Documents & Office | 🔍 Pending Verification

## Core Philosophy
- **Local transcription**: Audio is transcribed on-device with mlx-whisper (Apple Silicon optimized); recordings never leave your machine.
- **Structured minutes, not raw text**: The transcript is distilled into a decision/action format — separating confirmed conclusions from items pending follow-up, with every action item assigned an owner.
- **Transcript hygiene**: Known whisper hallucinations (repeated fixed phrases in silent passages) are filtered out, and ASR errors in technical terms, names, and product names are corrected from context.
- **Optional daily report**: A follow-up distillation keeps only the work perspective — project status, requirements, concerns, and decisions — with follow-ups ranked by priority.

## Key Features & Workflow

1. **Environment check**: Verify the source file and ffmpeg, and reuse or create the `~/whisper-env` virtual environment (auto-installs mlx-whisper on first use).
2. **Audio extraction**: ffmpeg converts video or audio to 16 kHz mono WAV.
3. **Transcription**: `scripts/transcribe.py` runs mlx-whisper (about 1–2 minutes per 10 minutes of audio) and writes `transcript_segments.txt`.
4. **Minutes generation**: Produces `会议纪要_<主题>.md` per `references/output-format.md` — concrete numbers, timestamps, and product names are preserved.
5. **Optional daily report**: Distills the minutes into `工作日报_<日期>.md`, focused on work status and follow-ups.

## Skills Library Overview
- **scripts/**: `transcribe.py` for local whisper transcription.
- **references/**: `output-format.md` defining the minutes and daily report structure.

## Installation & Support
Meeting Minutes supports the following AI editors and platforms:
- [Kiro](../../kiro/meeting-minutes/INSTALL-en.md)

---
For more information, visit: [GitHub - aws-samples/sample-for-kiro-meeting-minutes-skill](https://github.com/aws-samples/sample-for-kiro-meeting-minutes-skill)
