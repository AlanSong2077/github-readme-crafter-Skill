---
name: github-readme-crafter
description: Generate professional GitHub README documents using Spec-Driven Development. Outputs are validated against hard constraints before delivery. Use when users need to create README files, architecture diagrams, or bilingual documentation.
---

# GitHub README Crafter

> **Spec-Driven Development Skill** — Outputs are generated and validated per SPEC.md. Run validation with test.py before delivery.

## Core Principles

1. **SPEC-First**: Read `SPEC.md` before any generation
2. **Harness Engineering**: All output passes validation tests
3. **No Deviation**: Without spec update, no output may differ from spec

## Quick Reference

| Item | Value |
|------|-------|
| Style Options | `minimal`, `standard`, `professional` |
| Default Style | `standard` |
| Bilingual | `--bilingual` flag |
| Validation | `test.py` script |

## Workflow

```
1. Read SPEC.md (required)
2. Analyze project: python3 scripts/analyze_project.py <path>
3. Generate assets: banner, diagrams
4. Compose README per template
5. Run validation: python3 test.py <project_path>
6. Fix any HARD FAIL errors
7. Deliver output
```

## Commands

### Generate README
```bash
python3 scripts/create_readme.py <project_path> [options]

Options:
  --style {minimal|standard|professional}  # Default: standard
  --bilingual                              # Generate zh-CN version
  --banner-theme {dark|both}              # Default: dark
```

### Validate Output
```bash
python3 test.py <project_path>

# Exit codes: 0 = PASS, 1 = FAIL
```

### Generate Individual Assets
```bash
# Banner
python3 scripts/generate_banner.py "Title" --subtitle "Subtitle" --output assets/banner.svg

# Mermaid Diagram
python3 scripts/generate_mermaid.py architecture --project <path> --output diagram.md

# Advanced Elements
python3 scripts/generate_advanced_elements.py {social|star-history|contributors|sponsors|share}
```

## Files

| File | Purpose |
|------|---------|
| `SPEC.md` | Source of truth, hard constraints |
| `Agent.md` | Agent operating instructions |
| `test.md` | Validation test definitions |
| `scripts/create_readme.py` | Main generator |
| `scripts/analyze_project.py` | Project metadata extraction |
| `scripts/generate_banner.py` | SVG banner generation |
| `scripts/generate_mermaid.py` | Mermaid diagram generation |
| `scripts/generate_advanced_elements.py` | Badges, charts, etc. |

## Output Structure

```
project/
├── README.md           # English (required)
├── README.zh-CN.md    # Chinese (if --bilingual)
└── assets/
    ├── banner.svg      # Dark banner (required)
    └── banner-light.svg # Light banner (if bilingual)
```

## Style Sections

| Section | minimal | standard | professional |
|---------|---------|----------|--------------|
| Banner | - | ✓ | ✓ |
| TL;DR | - | ✓ | ✓ |
| Features | - | ✓ | ✓ |
| Installation | ✓ | ✓ | ✓ |
| Usage | ✓ | ✓ | ✓ |
| Tech Stack Diagram | - | ✓ | ✓ |
| Architecture Diagram | - | - | ✓ |
| Star History | - | - | ✓ |
| Contributors | - | - | ✓ |
| Sponsors | - | - | ✓ |
| Share Buttons | - | - | ✓ |
| License | ✓ | ✓ | ✓ |

## Validation Checklist

Before delivery, verify:

- [ ] README.md exists, size > 1KB
- [ ] All badge URLs valid (shields.io format)
- [ ] No emoji in badges
- [ ] Mermaid syntax valid
- [ ] No placeholder text
- [ ] TL;DR present (standard+)
- [ ] Bilingual files structurally match (if applicable)

Run: `python3 test.py <project_path>`

## Design Patterns

### Badge Rules
- Max 5 badges per row
- Use `flat-square` style (default)
- No emoji in badge text
- shields.io URLs only

### Banner Rules
- SVG format, 1280x320px
- Gradient background
- Dark AND light variants for bilingual

### Mermaid Rules
- GitHub-compatible syntax only
- Max 15 nodes per diagram
- Use subgraphs meaningfully

## Resources

- [SPEC.md](SPEC.md) — Hard constraints and specifications
- [Agent.md](Agent.md) — Agent operating procedures
- [test.md](test.md) — Validation test definitions
- [references/templates.md](references/templates.md) — README templates
- [references/top_projects_analysis.md](references/top_projects_analysis.md) — Reference analysis
