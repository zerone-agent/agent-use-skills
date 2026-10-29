# Oil Visual (oil-visual)

**Oil Visual** 是一个漫画墨线插画技能：用同一套视觉语言产出解释图与透明插画素材——粗细分明的黑色墨线、克制的圆形半调网点、可选的圆框眼镜线条小人配暖黄色边牧，每图最多两种低饱和语义色。

## 标签

🎨 设计与创意 | 🔍 待验证

## 核心理念
- **统一视觉语言**：角色、线条粗细、网点、配色、场景质感与图内文字全部遵循同一份书面规范，让不同主题的图保持同一种视觉风格。
- **两种模式严格分离**：Mode A（解释图）交付米白成品场景，所有关键标题与标签直接生成在位图内；Mode B（透明插画）交付可复用的角色/物件素材（原生透明或抠像），由自带脚本清理背景。两条生产路径绝不混用。
- **角色服务于主题而非风格**：眼镜小人与暖黄色边牧是可选主体——仅在用户要求或确有助于解释时绘制；纯物件作品独自承载风格。
- **克制的色彩语义**：黑白 + 半调灰为基底，暖黄留给边牧，每图最多再加两种低饱和语义色（蓝 = 输入/内容、橙 = 动作/警示、紫 = 流程、绿 = 成功结果）。

## 主要功能与工作流

1. **Mode A —— 解释图**：用于概念、机制、流程、对比与权衡。工作流：视觉简报 → 标签设计 → 提示词构建 → 检查重试；关系靠物件、路径、状态呈现，标签只做证据标注。
2. **Mode B —— 透明插画**：用于 hero、文档、卡片、幻灯片合成。工作流：主体选择 → 提示词 → 源图校验 → `scripts/cutout.py` 抠像 → 透明结果校验；源图原生透明且干净时直接保留。
3. **共享视觉语言**：粗细变化的黑色墨线、圆形半调、米白纸张质感、短而准确的无衬线标签直接放在对应物体上（支持中文标签）。
4. **质量门**：提示词结构、输出处理与验收检查全部写入 SKILL.md，跨宿主保持稳定产出质量。
5. **生成器无关**：图像生成使用宿主 Agent 自带的图像工具（官方为 Codex 设计），无框架专属 API。

## 技能库概览
- **scripts/**：`cutout.py`，chroma-key 抠像转透明 PNG（需 Python + Pillow）。
- **examples/**：九张参考图，覆盖解释图与透明插画。
- **agents/**：Agent 配置预设。

## 安装与支持
Oil Visual 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/oil-visual/INSTALL-zh.md)
- [Cursor](../../cursor/oil-visual/INSTALL-zh.md)
- [Codex](../../codex/oil-visual/INSTALL-zh.md)
- [OpenCode](../../opencode/oil-visual/INSTALL-zh.md)
- [OpenClaw](../../openclaw/oil-visual/INSTALL-zh.md)
- [Zerone](../../zerone/oil-visual/INSTALL-zh.md)
- [Qoder](../../qoder/oil-visual/INSTALL-zh.md)

图像生成依赖宿主 Agent 的图像工具（官方为 Codex 设计）；`scripts/cutout.py` 需 Python + Pillow。非 Codex 平台为待验证状态。

---
了解更多信息，请访问：[GitHub - oil-oil/oil-visual](https://github.com/oil-oil/oil-visual)
