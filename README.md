# GitHub README Crafter

<div align="center">

![Banner](assets/banner.svg)

### [English](README.md) | [中文](README.zh-CN.md)

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/AlanSong2077/github-readme-crafter-Skill?style=flat-square" alt="Stars">
</p>

## Overview

`github-readme-crafter` is a **Spec-Driven Development (SDD)** skill that generates **premium, attention-grabbing** GitHub README documents.

**Every README is a first impression.** This skill produces documentation that makes visitors think "this project is professional and well-maintained."

## Features

- 🎨 **Premium Banners** — SVG banners with gradient backgrounds and geometric decorations
- 📊 **Mermaid Diagrams** — Tech stack and architecture visualizations
- 🌐 **Bilingual** — English and Chinese, structurally identical
- 🌓 **Dark/Light Mode** — Theme-aware assets
- ⚡ **TL;DR Quick Start** — One command to immediate productivity
- 📈 **Star History** — Growth tracking visualization
- 👥 **Contributors** — Showcase your community
- 📢 **Share Buttons** — Reddit, Hacker News, Twitter, LinkedIn

## Quick Start

```bash
# Clone the skill
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git
cd github-readme-crafter-Skill

# Generate premium README for your project
python3 scripts/create_readme.py /path/to/project --style professional

# Validate output (REQUIRED)
python3 test.py /path/to/project
```

**Requirements**: Python 3.10+

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Read SPEC.md                                             │
│    - Source of truth for all generation                      │
│    - Premium-only: no minimal mode                          │
├─────────────────────────────────────────────────────────────┤
│ 2. Analyze Project                                          │
│    python3 scripts/analyze_project.py <path>                │
├─────────────────────────────────────────────────────────────┤
│ 3. Generate Assets                                          │
│    - Dark + Light banners (both required)                   │
│    - Tech stack diagram                                     │
│    - Architecture diagram                                   │
├─────────────────────────────────────────────────────────────┤
│ 4. Compose README                                           │
│    - Banner + badges + TL;DR + all required sections       │
│    - Bilingual (English + Chinese)                          │
├─────────────────────────────────────────────────────────────┤
│ 5. Validate (MANDATORY)                                     │
│    python3 test.py <project_path>                           │
│    → 0 errors required for delivery                        │
├─────────────────────────────────────────────────────────────┤
│ 6. Deliver                                                  │
│    - Write files                                           │
│    - Present validation status                             │
└─────────────────────────────────────────────────────────────┘
```

## Project Structure

```
github-readme-crafter-Skill/
├── SKILL.md                           # This skill definition
├── SPEC.md                           # Specification (source of truth)
├── Agent.md                          # Agent operating instructions
├── test.md                           # Validation test definitions
├── test.py                           # Executable validation script
├── scripts/
│   ├── create_readme.py            # Main generator
│   ├── analyze_project.py            # Project analyzer
│   ├── generate_banner.py            # SVG banner generator
│   ├── generate_mermaid.py           # Mermaid diagram generator
│   └── generate_advanced_elements.py  # Badges, charts, etc.
└── references/
    ├── templates.md                  # README templates
    ├── top_projects_analysis.md     # Reference analysis
    └── mermaid_examples.md           # Diagram examples
```

## Required Sections

Every generated README includes:

| Section | Description |
|---------|-------------|
| Banner | Gradient SVG with geometric decorations |
| Language Switcher | English \| 中文 |
| Badges | Max 5, flat-square style |
| TL;DR | One-command quick start |
| Overview | Value proposition |
| Features | 3-5 bullets with emoji |
| Installation | Copy-paste commands |
| Usage | Working code examples |
| Tech Stack | Mermaid diagram |
| Star History | Growth chart |
| Contributors | Showcase |
| Share Buttons | Social sharing |
| Contributing | Guidelines |
| License | MIT |

## Style Tiers

| Style | Description |
|-------|-------------|
| `standard` | All required sections + tech stack diagram |
| `professional` | Standard + sponsors, extended architecture, development channels |

**Both tiers produce premium output.** The difference is depth, not quality.

## Validation

All output MUST pass validation tests:

```bash
python3 test.py /path/to/project
```

### Test Categories

| Category | Description | Failure Action |
|----------|-------------|---------------|
| A - Structural | File existence, dimensions | HARD FAIL |
| B - Content | TL;DR, sections, no placeholders | HARD FAIL |
| C - Badges | Count, style, URLs | HARD FAIL |
| D - Images | URL accessibility | WARN |
| E - Mermaid | Syntax validity | HARD FAIL |
| F - Bilingual | File exists, parity | HARD FAIL |

### Pass Criteria

| Level | Errors | Result |
|-------|--------|--------|
| **PASS** | 0 | Ready for delivery |
| **FAIL** | ≥ 1 | Fix before delivery |

## Design Rules

### Badge Rules
- Maximum 5 badges per row
- Style: `flat-square`
- No emoji in badge text
- shields.io URLs only

### Banner Rules
- SVG format, 1280x320 pixels
- Gradient background (2+ colors)
- Geometric decorations required
- Dark AND light variants (both required)

### Mermaid Rules
- GitHub-compatible syntax only
- Maximum 15 nodes per diagram
- At least 1 diagram required

## Contributing

Contributions follow **Spec-Driven Development**:

1. Read `SPEC.md` before making changes
2. Update `SPEC.md` if adding new requirements
3. Update `test.md` with corresponding validation
4. Update `Agent.md` with new procedures
5. Run `test.py` to verify changes

## License

MIT License
