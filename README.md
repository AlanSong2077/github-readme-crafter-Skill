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

`github-readme-crafter` is a **Spec-Driven Development (SDD)** skill that generates production-ready GitHub README documents using AI.

The skill follows **Harness Engineering** principles: specifications drive generation, and all outputs are validated against hard constraints before delivery.

## Features

- 📋 **Spec-First Development** — All output conforms to `SPEC.md`
- ✅ **Strong Validation** — Hard constraints enforced via `test.py`
- 🎨 **Dynamic Banner Generation** — SVG banners with gradient backgrounds
- 📊 **Mermaid Diagrams** — Architecture, tech stack, workflow diagrams
- 🌐 **Bilingual Support** — English and Chinese versions
- 🌓 **Dark/Light Mode** — Theme-aware assets
- ⚡ **TL;DR Sections** — Quick start for busy readers

## Quick Start

```bash
# Clone the skill
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git
cd github-readme-crafter-Skill

# Generate README for your project
python3 scripts/create_readme.py /path/to/project --style professional --bilingual

# Validate output (REQUIRED before delivery)
python3 test.py /path/to/project
```

**Requirements**: Python 3.10+

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Read SPEC.md                                             │
│    - Source of truth for all generation                      │
│    - Hard constraints, section requirements                  │
├─────────────────────────────────────────────────────────────┤
│ 2. Analyze Project                                          │
│    python3 scripts/analyze_project.py <path>                │
│    → Returns: language, framework, structure metadata        │
├─────────────────────────────────────────────────────────────┤
│ 3. Generate Assets                                          │
│    - Banner (dark + light variants)                         │
│    - Mermaid diagrams (if applicable)                       │
│    - Advanced elements (badges, charts)                     │
├─────────────────────────────────────────────────────────────┤
│ 4. Compose README                                           │
│    - Select template per style (minimal/standard/pro)       │
│    - Insert generated assets                                │
│    - Insert metadata from analysis                          │
├─────────────────────────────────────────────────────────────┤
│ 5. Validate (HARD REQUIREMENT)                              │
│    python3 test.py <project_path>                           │
│    → MUST PASS all Category A-E tests before delivery       │
├─────────────────────────────────────────────────────────────┤
│ 6. Deliver                                                  │
│    - Write files to project directory                        │
│    - Present validation status                              │
└─────────────────────────────────────────────────────────────┘
```

## Project Structure

```
github-readme-crafter-Skill/
├── SKILL.md                           # This skill definition
├── SPEC.md                           # Specification (source of truth)
├── Agent.md                          # Agent operating instructions
├── test.md                           # Validation test definitions
├── scripts/
│   ├── create_readme.py             # Main generator
│   ├── analyze_project.py             # Project analyzer
│   ├── generate_banner.py            # SVG banner generator
│   ├── generate_mermaid.py           # Mermaid diagram generator
│   └── generate_advanced_elements.py  # Badges, charts, etc.
└── references/
    ├── templates.md                  # README templates
    ├── top_projects_analysis.md     # Reference analysis
    └── mermaid_examples.md           # Diagram examples
```

## Style Options

| Style | Use Case | Sections |
|-------|----------|----------|
| `minimal` | Small libraries | Title, badges, install, usage, license |
| `standard` | Medium projects | Banner, TL;DR, features, diagrams, install, usage |
| `professional` | Large frameworks | All sections + star history, contributors, sponsors |

## Validation

All output MUST pass validation tests:

```bash
python3 test.py /path/to/project
```

### Test Categories

| Category | Description | Failure Action |
|----------|-------------|----------------|
| A - Structural | File existence, dimensions | HARD FAIL |
| B - Content | Sections present, no placeholders | HARD FAIL |
| C - Badges | Count, style, URLs | HARD FAIL |
| D - Images | URL accessibility | WARN |
| E - Mermaid | Syntax validity | HARD FAIL |
| F - Bilingual | File exists, parity | HARD FAIL |
| G - Style | Emoji count, paragraph length | WARN |

### Pass Criteria

| Level | Errors | Warnings |
|-------|--------|----------|
| **PASS** | 0 | Any |
| **FAIL** | ≥ 1 | - |

## Design Rules (Hard Constraints)

### Badge Rules
- Maximum 5 badges per row
- Style: `flat-square` (default) or `for-the-badge`
- No emoji in badge text
- shields.io URLs only

### Banner Rules
- SVG format, 1280x320 pixels
- Gradient background (2+ colors)
- Dark AND light variants required for bilingual

### Mermaid Rules
- GitHub-compatible syntax only
- Maximum 15 nodes per diagram
- No unsupported features (pie, timeline, gantt)

## Contributing

Contributions follow **Spec-Driven Development**:

1. Read `SPEC.md` before making changes
2. Update `SPEC.md` if adding new requirements
3. Update `test.md` with corresponding validation
4. Update `Agent.md` with new procedures
5. Run `test.py` to verify changes

## License

MIT License
