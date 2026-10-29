# xenho-cover

**xenho-cover** 是一个封面图技能：把一篇文章、一条小红书笔记、一篇公众号推文、一条 X 帖子或一个主题变成成品封面。风格来自自建风格库——29 个风格原子、分 6 个气质家族。提供两种模式：Prompt 模式只产出完整图像生成提示词；Direct 模式编译同一份提示词后直接出图，默认经本机 Codex CLI 的 GPT Image，无需 API key。

## 标签

🎨 设计与创意 | 🔍 待验证

## 核心理念
- **提示词即产品**：编译出的每份提示词都自包含——色值、构图、字体、穷举的文字白名单与终检标准全部填实，可直接粘贴到 GPT Image-2 或任意兼容生成器。
- **风格原子不可变**：29 个风格互不重叠；当需求撞上风格边界时，技能会说明冲突、推荐最接近的现有风格，而不是临时改造风格原子去凑。
- **比例先于像素**：平台比例映射（小红书 3:4、公众号 3.35:1 双画幅、X 5:2、自定义）严格执行；未给平台也未给比例时会先停下来问，绝不猜——比例错了整张图作废。
- **汉字排版安全**：中文只用标准比例的黑体/宋体/圆体且笔画下方保持干净底色，风格特殊字体只给西文和数字——汉字压在网点、贴纸、热敏/点阵字体上必错。

## 主要功能与工作流

1. **自动提炼**：提炼标题三层、视觉隐喻、情绪与禁用元素，推荐 3 个候选风格；直接点名风格原子则跳过推荐直接编译。
2. **Direct 模式**：经本机 Codex CLI GPT Image（无需 key）或 OpenAI 兼容接口直接出图，内置防重复出图，且每个画幅最多发一次出图请求。
3. **公众号双画幅**：公众号 3.35:1 封面按横版 2.35:1 + 方版 1:1 两张画幅分别生成（设计决定逐字一致），再由 `scripts/wechat_combine.py` 拼合成上传图（需 Pillow）。
4. **中英双语提示词**：默认输出中文提示词（汉字还原更好），可要求英文版。
5. **风格库可扩展**：新增风格只需添加 `styles/{id}/` 文件夹，无需修改 SKILL.md。

## 技能库概览
- **styles/**：29 个风格原子，分属 6 个气质家族（从 `anthropic-research` 到 `polish-grain-collage`、`tile-crossword`）。
- **references/**：`cover-prompt-blueprint.md`（提示词结构）与 `direct-mode.md`（端点配置、比例映射、防重复规则）。
- **scripts/**：`wechat_combine.py`，公众号封面拼合脚本。

## 安装与支持
xenho-cover 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/xenho-cover/INSTALL-zh.md)
- [Cursor](../../cursor/xenho-cover/INSTALL-zh.md)
- [Codex](../../codex/xenho-cover/INSTALL-zh.md)
- [OpenCode](../../opencode/xenho-cover/INSTALL-zh.md)
- [OpenClaw](../../openclaw/xenho-cover/INSTALL-zh.md)
- [Zerone](../../zerone/xenho-cover/INSTALL-zh.md)
- [Qoder](../../qoder/xenho-cover/INSTALL-zh.md)

Prompt 模式在任何可加载 SKILL.md 的 Agent 上可用；Direct 模式需本机 Codex CLI（已登录）或 OpenAI 兼容图像接口——属机器级依赖，与宿主平台无关。

---
了解更多信息，请访问：[GitHub - PPory/xenho-cover](https://github.com/PPory/xenho-cover)
