#!/usr/bin/env python3
"""会议录音转录脚本 - 使用 mlx-whisper 进行语音识别"""

import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: transcribe.py <audio_file> <output_dir>")
        sys.exit(1)

    audio_file = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(audio_file):
        print(f"Error: Audio file not found: {audio_file}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    import mlx_whisper

    print(f"Transcribing: {audio_file}")
    result = mlx_whisper.transcribe(
        audio_file,
        path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
        language="zh",
        word_timestamps=False,
    )

    # 保存完整文本
    transcript_path = os.path.join(output_dir, "transcript.txt")
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    # 保存分段文本
    segments_path = os.path.join(output_dir, "transcript_segments.txt")
    with open(segments_path, "w", encoding="utf-8") as f:
        for seg in result["segments"]:
            start = seg["start"]
            end = seg["end"]
            text = seg["text"].strip()
            if text:
                f.write(f"[{start:.1f}s - {end:.1f}s] {text}\n")

    print(f"Total segments: {len(result['segments'])}")
    print(f"Text length: {len(result['text'])} chars")
    print(f"Output: {transcript_path}")
    print(f"Segments: {segments_path}")
    print("Done!")


if __name__ == "__main__":
    main()
