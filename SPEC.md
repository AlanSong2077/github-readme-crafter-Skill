# SPEC.md — GitHub README Crafter Specification

> **Spec-Driven Development (SDD)** — This specification is the source of truth. All output MUST conform to this document. No deviations permitted without spec update.

---

## 1. Overview

**Project Name**: GitHub README Crafter  
**Type**: AI-Powered Documentation Generation Skill  
**Core Function**: Generate premium, attention-grabbing GitHub README documents  
**Target Users**: Developers, AI agents, technical writers who want professional documentation

---

## 2. Core Principle

**All READMEs MUST be visually premium and attention-grabbing.** There is no "minimal" or "simple" mode. Every generated README should make visitors think "this project is professional and well-maintained."

---

## 3. Required Capabilities

### 3.1 Project Analysis
- **Input**: Project directory path
- **Output**: Structured metadata (language, framework, structure, entry points)
- **Validation**: MUST return valid JSON with required fields

### 3.2 Banner Generation
- **Output**: SVG file with gradient background and geometric decorations
- **Variants**: Dark mode (default), Light mode
- **Dimensions**: 1280x320 pixels
- **Validation**: Valid SVG XML, no broken elements
- **Requirement**: MUST be visually impressive - gradient background, geometric decorations, professional typography

### 3.3 Mermaid Diagrams
- **Types**: Architecture, Tech Stack, Workflow, CI/CD Pipeline
- **Validation**: Valid Mermaid syntax, renders on GitHub
- **Requirement**: At least one diagram required for visual appeal

### 3.4 Advanced Elements
| Element | Format | Required |
|---------|--------|----------|
| Star History | `![Star History](https://api.star-history.com/svg?repos=owner/repo&type=Date)` | Always |
| Contributors | `<a href="..."><img src="https://contrib.rocks/..."/></a>` | Always |
| Share Buttons | Markdown with `style=flat-square` | Always |
| Badges | Shields.io, flat-square style | Always |

### 3.5 Bilingual Support
- **Languages**: English (default), Chinese (zh-CN)
- **Output Files**: `README.md`, `README.zh-CN.md`
- **Validation**: Both files must exist, structurally identical

---

## 4. Output Structure

### 4.1 File Layout
```
project/
├── README.md                    # English version (REQUIRED)
├── README.zh-CN.md             # Chinese version (REQUIRED)
├── assets/
│   ├── banner.svg             # Dark banner (REQUIRED)
│   └── banner-light.svg       # Light banner (REQUIRED)
└── [existing project files]
```

### 4.2 Required Sections (ALL READMEs)

Every generated README MUST include:

1. **Banner** — Visual hero with gradient and decorations
2. **Language Switcher** — English | 中文 (for bilingual)
3. **Badges Row** — Max 5 badges, flat-square style
4. **TL;DR Quick Start** — One-command install + immediate usage
5. **Overview** — 1 paragraph explaining value proposition
6. **Features** — 3-5 bullet points with emoji
7. **Installation** — Copy-paste commands
8. **Usage** — Working code examples
9. **Tech Stack Diagram** — Mermaid flowchart
10. **Architecture Diagram** — Mermaid (if complex project)
11. **Star History** — Growth chart
12. **Contributors** — Showcase
13. **Share Buttons** — Social sharing
14. **Contributing** — Guidelines
15. **License** — MIT (default)

---

## 5. Design Rules (Hard Constraints)

### 5.1 Banner Rules
| Rule | Constraint |
|------|------------|
| Format | SVG only |
| Dimensions | 1280x320 pixels |
| Background | Gradient (2+ colors, visually appealing) |
| Decorations | Geometric shapes REQUIRED |
| Text | Title + subtitle |
| Theme | Dark AND Light variants (both required) |

### 5.2 Badge Rules
| Rule | Constraint | Enforcement |
|------|------------|-------------|
| Max badges | 5 | HARD LIMIT |
| Style | `flat-square` | REQUIRED |
| Emoji in badges | PROHIBITED | REJECT |
| Broken URLs | PROHIBITED | REJECT |

### 5.3 Mermaid Diagram Rules
| Rule | Constraint |
|------|------------|
| Syntax | GitHub-compatible Mermaid |
| Max nodes | 15 per diagram |
| Min diagrams | 1 (Tech Stack) |
| Labels | Meaningful, no generic names |

### 5.4 Content Rules
| Rule | Constraint |
|------|------------|
| Emoji usage | MAX 2 per section |
| Paragraph length | MAX 4 sentences |
| Code examples | Complete, runnable |
| Language | Imperative mood for commands |
| TL;DR | REQUIRED |

---

## 6. Style Tiers

There are TWO style tiers only:

### Standard (Minimum)
All required sections listed in Section 4.

### Professional (Enhanced)
All Standard sections PLUS:
- Sponsors showcase (if available)
- Extended architecture diagram
- Security section
- Development channels explanation

**Note**: Both tiers produce visually premium output. The difference is in depth, not quality.

---

## 7. Validation Checklist

### Pre-Generation
- [ ] Project path exists and is readable
- [ ] Output directory is writable
- [ ] Required scripts are executable

### Post-Generation (ALL MANDATORY)
- [ ] README.md exists, size > 2KB
- [ ] README.zh-CN.md exists, size > 2KB
- [ ] assets/banner.svg exists, valid SVG
- [ ] assets/banner-light.svg exists, valid SVG
- [ ] All badge URLs return HTTP 200
- [ ] All image URLs are accessible
- [ ] Mermaid syntax is valid
- [ ] TL;DR section present
- [ ] No placeholder text
- [ ] Language switchers in both files
- [ ] Star History chart present
- [ ] Contributors section present
- [ ] Share buttons present

---

## 8. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-11 | Initial spec |
| 2.0 | 2026-04-11 | Remove minimal - all READMEs must be premium |

---

**END OF SPEC.md**
