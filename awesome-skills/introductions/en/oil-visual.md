# Oil Visual (oil-visual)

**Oil Visual** is a manga-ink illustration skill that produces explanatory images and transparent illustration assets in one shared visual language — confident black ink outlines with varied line weight, restrained circular halftone screentone, an optional glasses stick-figure protagonist with a warm-yellow Border Collie, and at most two muted semantic colors per image.

## Tags

🎨 Design & Creativity | 🔍 Pending Verification

## Core Philosophy
- **One visual language**: Characters, line weight, screentone, palette, scene texture, and in-image text all follow a single written spec, so visuals across topics stay stylistically consistent.
- **Two strictly separate modes**: Mode A (explanatory image) delivers a finished off-white scene with every essential title and label generated inside the bitmap; Mode B (transparent illustration) delivers reusable character/object assets on native alpha or chroma-key, cleaned by the bundled cutout script. The two production paths are never mixed.
- **Characters serve the subject, not the style**: The glasses stick figure and the warm-yellow Border Collie are optional subjects — drawn only when requested or when they visibly help explain; object-only artwork carries the style alone.
- **Restrained color semantics**: Black/white/halftone gray base, warm yellow for the dog, plus at most two muted semantic colors (blue = input/content, orange = action/warning, purple = process, green = success).

## Key Features & Workflow

1. **Mode A — explanatory image**: For concepts, mechanisms, workflows, comparisons, and tradeoffs. Workflow: visual brief → label design → prompt build → inspect and retry; relations are made visible through objects, paths, and states, with labels identifying the evidence.
2. **Mode B — transparent illustration**: For hero, document, card, and slide composition. Workflow: subject selection → prompt → source validation → chroma-key removal via `scripts/cutout.py` → transparent-result validation; native alpha is preserved when clean.
3. **Shared visual language**: Varied-weight black ink lines, circular halftone, off-white paper texture, and short accurate sans-serif labels placed directly on the objects (Chinese labels supported).
4. **Quality gate**: Prompt structure, output handling, and acceptance checks are encoded in SKILL.md, keeping output quality stable across hosts.
5. **Generator-agnostic**: Image generation uses the host agent's own image tool (officially designed for Codex); no framework-specific API.

## Skills Library Overview
- **scripts/**: `cutout.py` for chroma-key background removal to transparent PNG (requires Python with Pillow).
- **examples/**: Nine reference images covering explainers and transparent illustration.
- **agents/**: Agent configuration preset.

## Installation & Support
Oil Visual supports the following AI editors and platforms:
- [Claude Code](../../claudecode/oil-visual/INSTALL-en.md)
- [Cursor](../../cursor/oil-visual/INSTALL-en.md)
- [Codex](../../codex/oil-visual/INSTALL-en.md)
- [OpenCode](../../opencode/oil-visual/INSTALL-en.md)
- [OpenClaw](../../openclaw/oil-visual/INSTALL-en.md)
- [Zerone](../../zerone/oil-visual/INSTALL-en.md)
- [Qoder](../../qoder/oil-visual/INSTALL-en.md)

Image generation relies on the host agent's image tool (officially designed for Codex); `scripts/cutout.py` needs Python with Pillow. Non-Codex platforms are pending verification.

---
For more information, visit: [GitHub - oil-oil/oil-visual](https://github.com/oil-oil/oil-visual)
