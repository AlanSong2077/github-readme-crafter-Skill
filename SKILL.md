---
name: github-readme-crafter
description: Generate premium, attention-grabbing GitHub README documents using Spec-Driven Development. Every README is visually impressive. No minimal mode. Use when users need professional README files with bilingual support.
---

# GitHub README Crafter

> **Premium README Generation** — Every README is visually impressive. No "minimal" or "simple" mode. All outputs include banner, TL;DR, diagrams, badges, and advanced elements.

## Core Principle

**Every README is a first impression.** This skill generates premium documentation that makes visitors think "this project is professional and well-maintained."

## Quick Reference

| Item | Value |
|------|-------|
| Style Options | `standard`, `professional` |
| Default Style | `standard` (premium minimum) |
| Bilingual | Always (default) |
| Validation | `test.py` script |

**There is NO minimal style. All READMEs include banner, TL;DR, diagrams, and advanced elements.**

## Workflow

```
1. Read SPEC.md (required)
2. Analyze project: python3 scripts/analyze_project.py <path>
3. Generate assets: banner (dark + light), diagrams
4. Compose README with ALL required sections
5. Create bilingual version (mirrored structure)
6. Run validation: python3 test.py <project_path>
7. Fix any HARD FAIL errors
8. Deliver output
```

## Commands

### Generate README
```bash
python3 scripts/create_readme.py <project_path> [options]

Options:
  --style {standard|professional}  # Default: standard
  --bilingual                      # Default: true
```

### Validate Output
```bash
python3 test.py <project_path>

# Exit codes: 0 = PASS, 1 = FAIL
```

### Generate Individual Assets
```bash
# Banner (dark + light required)
python3 scripts/generate_banner.py "Title" --subtitle "Subtitle" --output assets/banner.svg

# Mermaid Diagram
python3 scripts/generate_mermaid.py architecture --project <path> --output diagram.md

# Advanced Elements
python3 scripts/generate_advanced_elements.py {social|star-history|contributors|sponsors|share}
```

## Output Structure

```
project/
├── README.md              # English (required)
├── README.zh-CN.md       # Chinese (required)
└── assets/
    ├── banner.svg        # Dark banner (required)
    └── banner-light.svg  # Light banner (required)
```

## Required Sections

Every README MUST include:

| Section | Description |
|---------|-------------|
| Banner | SVG with gradient + geometric decorations |
| Language Switcher | English \| 中文 |
| Badges | Max 5, flat-square style |
| TL;DR | One-command quick start |
| Overview | 1 paragraph value proposition |
| Features | 3-5 bullets |
| Installation | Copy-paste commands |
| Usage | Working code examples |
| Tech Stack | Mermaid diagram |
| Star History | Growth chart |
| Contributors | Showcase |
| Share Buttons | Social sharing |
| Contributing | Guidelines |
| License | MIT default |

## Style Tiers

| Tier | Description |
|------|-------------|
| `standard` | All required sections + tech stack diagram |
| `professional` | Standard + sponsors, extended architecture, development channels |

Both tiers produce visually premium output. The difference is depth, not quality.

## Validation Checklist

Before delivery:

- [ ] README.md exists, size > 2KB
- [ ] README.zh-CN.md exists, size > 2KB
- [ ] assets/banner.svg exists, valid SVG
- [ ] assets/banner-light.svg exists, valid SVG
- [ ] All badge URLs valid
- [ ] No emoji in badges
- [ ] Mermaid syntax valid
- [ ] TL;DR section present
- [ ] No placeholder text
- [ ] Language switchers in both files
- [ ] Star History present
- [ ] Contributors present
- [ ] Share buttons present

Run: `python3 test.py <project_path>`

## Design Rules

### Badge Rules
- Max 5 badges per row
- Use `flat-square` style
- No emoji in badge text
- shields.io URLs only

### Banner Rules
- SVG format, 1280x320px
- Gradient background (2+ colors)
- Geometric decorations required
- Dark AND light variants (both required)

### Mermaid Rules
- GitHub-compatible syntax only
- Max 15 nodes per diagram
- At least 1 diagram required

## Files

| File | Purpose |
|------|---------|
| `SPEC.md` | Source of truth, hard constraints |
| `Agent.md` | Agent operating instructions |
| `test.md` | Validation test definitions |
| `test.py` | Executable validation script |
| `scripts/create_readme.py` | Main generator |
| `scripts/analyze_project.py` | Project metadata |
| `scripts/generate_banner.py` | SVG banner generation |
| `scripts/generate_mermaid.py` | Mermaid diagram generation |
| `scripts/generate_advanced_elements.py` | Badges, charts, etc. |

## Resources

- [SPEC.md](SPEC.md) — Hard constraints and specifications
- [Agent.md](Agent.md) — Agent operating procedures
- [test.md](test.md) — Validation test definitions
- [references/templates.md](references/templates.md) — README templates
- [references/top_projects_analysis.md](references/top_projects_analysis.md) — Reference analysis
