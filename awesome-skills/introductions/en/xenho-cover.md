# xenho-cover

**xenho-cover** is a cover-image skill that turns an article, Xiaohongshu note, WeChat official-account post, X post, or a bare topic into finished covers, using a self-built library of 29 style atoms grouped into 6 temperament families. It has two modes: Prompt mode outputs a complete image-generation prompt only; Direct mode compiles the same prompt and generates the image directly via the local Codex CLI GPT Image, no API key needed.

## Tags

🎨 Design & Creativity | 🔍 Pending Verification

## Core Philosophy
- **The prompt is the product**: Every compiled prompt is self-contained — filled-in colors, composition, fonts, an exhaustive text whitelist, and final-check criteria — ready to paste into GPT Image-2 or any compatible generator.
- **Style atoms are immutable**: The 29 styles never overlap; when a request clashes with a style's boundary, the skill explains the conflict and recommends the closest existing style instead of mutating an atom to fit.
- **Ratio before pixels**: Platform mappings (Xiaohongshu 3:4, WeChat 3.35:1 dual-canvas, X 5:2, custom) are strict; if neither platform nor ratio is given, the skill stops and asks rather than guessing — a wrong ratio wastes the whole image.
- **Chinese typography safety**: CJK text only uses standard-ratio 黑体/宋体/圆体 on clean backgrounds, and stylized fonts are reserved for Latin and digits, because hanzi reliably breaks on halftone, sticker overlays, and thermal or dot-matrix fonts.

## Key Features & Workflow

1. **Auto extraction**: Distills a title hierarchy, visual metaphor, mood, and forbidden elements, then recommends 3 candidate styles; naming a style atom skips straight to compilation.
2. **Direct mode**: Generates images via the local Codex CLI GPT Image (no key) or an OpenAI-compatible endpoint, with built-in anti-duplicate generation and at most one image request per canvas.
3. **WeChat dual-canvas**: WeChat 3.35:1 covers are produced as a 2.35:1 landscape and a 1:1 square canvas with matching design decisions, then combined by `scripts/wechat_combine.py` (requires Pillow).
4. **Bilingual prompts**: Chinese prompts by default (better hanzi fidelity), English on request.
5. **Extensible style library**: Adding a style is just a new `styles/{id}/` folder — SKILL.md stays untouched.

## Skills Library Overview
- **styles/**: 29 style atoms across 6 temperament families (from `anthropic-research` to `polish-grain-collage` and `tile-crossword`).
- **references/**: `cover-prompt-blueprint.md` (prompt structure) and `direct-mode.md` (endpoint config, ratio mapping, anti-duplicate rules).
- **scripts/**: `wechat_combine.py` for WeChat cover compositing.

## Installation & Support
xenho-cover supports the following AI editors and platforms:
- [Claude Code](../../claudecode/xenho-cover/INSTALL-en.md)
- [Codex](../../codex/xenho-cover/INSTALL-en.md)

---
For more information, visit: [GitHub - PPory/xenho-cover](https://github.com/PPory/xenho-cover)
