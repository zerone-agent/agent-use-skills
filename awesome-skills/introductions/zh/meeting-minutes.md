# Meeting Minutes (meeting-minutes)

**Meeting Minutes** 是 AWS 官方 Kiro 示例技能：将会议录音（音频 .m4a/.mp3/.wav/.flac / 视频 .mp4/.mkv/.webm）通过 mlx-whisper（whisper-large-v3-turbo）转录为结构化中文会议纪要，并可选生成工作日报。

## 标签

🗂️ 文档与办公 | 🔍 待验证

## 核心理念
- **本地转录**：使用 mlx-whisper（Apple Silicon 优化）在本地设备完成转录，录音文件不出本机。
- **结构化纪要而非原始文本**：将转录内容提炼为决策/行动格式——区分「已确认结论」与「待确认/待跟进」事项，每个 action item 标注负责方。
- **转录文本治理**：过滤 whisper 已知幻觉（静默段落中反复出现的固定短语），并根据上下文修正术语、人名、产品名等语音识别错误。
- **可选工作日报**：在纪要基础上二次提炼，只保留工作视角——项目现状、需求、关注点与决策结论，待跟进事项按优先级排列。

## 主要功能与工作流

1. **环境检查**：确认源文件与 ffmpeg，复用或创建 `~/whisper-env` 虚拟环境（首次使用自动安装 mlx-whisper）。
2. **音频提取**：ffmpeg 将视频/音频转为 16 kHz 单声道 WAV。
3. **转录**：`scripts/transcribe.py` 运行 mlx-whisper（约每 10 分钟音频耗时 1–2 分钟），输出 `transcript_segments.txt`。
4. **纪要生成**：按 `references/output-format.md` 生成 `会议纪要_<主题>.md`——保留具体数字、时间节点与产品名称。
5. **可选日报**：将纪要提炼为 `工作日报_<日期>.md`，聚焦工作现状与待跟进事项。

## 技能库概览
- **scripts/**：`transcribe.py`，本地 whisper 转录脚本。
- **references/**：`output-format.md`，定义纪要与日报的输出结构。

## 安装与支持
Meeting Minutes 支持以下 AI 编辑器和平台：
- [Kiro](../../kiro/meeting-minutes/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - aws-samples/sample-for-kiro-meeting-minutes-skill](https://github.com/aws-samples/sample-for-kiro-meeting-minutes-skill)
