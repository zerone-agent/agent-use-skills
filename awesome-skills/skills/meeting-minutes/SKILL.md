---
name: meeting-minutes
description: 会议录音转会议纪要。将视频(mp4/mkv/webm)或音频(m4a/mp3/wav/flac)文件转录为文字，生成结构化会议纪要。支持生成工作日报。当用户提到会议录音、会议纪要、转录、transcribe meeting 时激活。
---

## 输入

用户提供以下信息：
- 文件路径：视频(.mp4/.mkv/.webm)或音频(.m4a/.mp3/.wav/.flac)文件的绝对路径
- 是否生成日报：可选，额外生成工作日报（只保留关键需求/问题/讨论点）
- 输出目录：可选，指定输出目录，默认与源文件同目录

## 执行步骤

### 第一步：环境检查

1. 确认文件存在，识别文件类型（视频/音频）
2. 确认 ffmpeg 已安装（`which ffmpeg`）
3. 检查 whisper 虚拟环境是否存在：`~/whisper-env/bin/python`
   - 如果不存在，创建并安装依赖：
     ```bash
     python3 -m venv ~/whisper-env
     ~/whisper-env/bin/pip install mlx-whisper
     ```
   - 如果存在，直接复用

### 第二步：提取音频

用 ffmpeg 将源文件转为 WAV（如果已经是 WAV 则跳过）：

```bash
ffmpeg -i "<源文件>" -vn -acodec pcm_s16le -ar 16000 -ac 1 "<输出目录>/audio.wav" -y
```

注意：如果同目录已有 audio.wav，用 `audio_<时间戳>.wav` 避免覆盖。

### 第三步：转录

使用 scripts/transcribe.py 执行转录：

```bash
~/whisper-env/bin/python ~/.kiro/skills/meeting-minutes/scripts/transcribe.py "<音频文件路径>" "<输出目录>"
```

这一步耗时较长（约1-2分钟/10分钟音频），请告知用户需要等待。

### 第四步：读取转录结果

1. 读取 `<输出目录>/transcript_segments.txt`，注意文件可能很大，分批读取
2. **识别并过滤 whisper 幻觉**：静默段落中反复出现的固定短语（如重复的广告词、栏目名）是 whisper 的已知问题，应忽略
3. **修正常见语音识别错误**：技术术语、人名、产品名等需要根据上下文修正

### 第五步：生成会议纪要

基于转录内容，生成结构化的会议纪要 markdown 文件，保存为 `<输出目录>/会议纪要_<主题>.md`。

纪要格式参见 references/output-format.md。

要求：
- 用中文撰写
- 去除口语化表达，提炼核心信息
- 保留具体的数字、时间节点、产品名称
- 区分"已确认结论"和"待确认/待跟进"事项
- 如有明确的 action item，必须列出负责方

### 第六步（可选）：生成工作日报

如果用户要求生成日报，基于会议纪要再生成一份精简的工作日报 `<输出目录>/工作日报_<日期>.md`。

日报要求：
- 去掉所有产品介绍内容，只保留工作视角
- 聚焦：项目现状、需求、关注点、提出的问题、讨论结论
- 包含：项目架构思路、技术选型倾向、决策路径
- 待跟进事项按优先级排列

日报格式参见 references/output-format.md。

## 注意事项

- 如果同一目录下有多个录音文件需要合并生成日报，用户会明确指定
- 输出文件名中不要用空格，用下划线
