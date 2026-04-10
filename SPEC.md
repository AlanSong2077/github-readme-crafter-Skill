# SPEC.md — GitHub README Crafter Specification

> **Spec-Driven Development (SDD)** — This specification is the source of truth. All output MUST conform to this document. No deviations permitted without spec update.

---

## 1. Overview

**Project Name**: GitHub README Crafter  
**Type**: AI-Powered Documentation Generation Skill  
**Core Function**: Generate production-ready GitHub README documents from project analysis  
**Target Users**: Developers, AI agents, technical writers

---

## 2. Core Capabilities (Enforced)

### 2.1 Project Analysis
- **Input**: Project directory path
- **Output**: Structured metadata (language, framework, structure, entry points)
- **Validation**: MUST return valid JSON with required fields

### 2.2 Banner Generation
- **Output**: SVG file with gradient background and geometric decorations
- **Variants**: Dark mode (default), Light mode
- **Dimensions**: 1280x320 pixels
- **Validation**: Valid SVG XML, no broken elements

### 2.3 Mermaid Diagrams
- **Types**: Architecture, Tech Stack, Workflow, CI/CD Pipeline
- **Validation**: Valid Mermaid syntax, renders on GitHub

### 2.4 Advanced Elements
| Element | Format | Validation |
|---------|--------|------------|
| Star History | `![Star History](https://api.star-history.com/svg?repos=owner/repo&type=Date)` | URL format check |
| Contributors | `<a href="..."><img src="https://contrib.rocks/..."/></a>` | URL format check |
| Share Buttons | Markdown with `style=flat-square` | Valid shields.io URLs |
| Sponsors | HTML table or badge row | Valid HTML/badge syntax |

### 2.5 Bilingual Support
- **Languages**: English (default), Chinese (zh-CN)
- **Output Files**: `README.md`, `README.zh-CN.md`
- **Validation**: Both files must exist when bilingual=true

---

## 3. Output Structure

### 3.1 File Layout
```
project/
├── README.md                    # English version (REQUIRED)
├── README.zh-CN.md             # Chinese version (if --bilingual)
├── SPEC.md                     # This specification (if applicable)
├── assets/
│   ├── banner.svg             # Dark banner (REQUIRED)
│   ├── banner-light.svg       # Light banner (REQUIRED)
│   └── (other assets)
└── [existing project files]
```

### 3.2 Content Sections (by style)

#### Minimal Style
1. Title (H1)
2. Badges (max 3)
3. One-line description
4. Installation command
5. Usage example
6. License

#### Standard Style
1. Banner (dark/light mode)
2. Language switcher (if bilingual)
3. Badges (max 5)
4. TL;DR Quick Start
5. Overview (1 paragraph)
6. Features (3-5 bullets)
7. Installation
8. Usage examples
9. Tech Stack diagram (Mermaid)
10. Contributing
11. License

#### Professional Style
All Standard sections PLUS:
- Sponsors showcase
- Architecture diagram
- Star History chart
- Contributors showcase
- Development Channels
- Share buttons
- Security section (if applicable)

---

## 4. Design Rules (Hard Constraints)

### 4.1 Badge Rules
| Rule | Constraint | Enforcement |
|------|------------|-------------|
| Max badges | 5 per row | HARD LIMIT |
| Style | `flat-square` (default) or `for-the-badge` | REQUIRED |
| Emoji in badges | PROHIBITED | REJECT |
| Broken URLs | PROHIBITED | REJECT |

### 4.2 Banner Rules
| Rule | Constraint |
|------|------------|
| Format | SVG only |
| Background | Gradient (2+ colors) |
| Decorations | Geometric shapes allowed |
| Text | Title + subtitle required |
| Theme | Dark AND Light variants |

### 4.3 Mermaid Diagram Rules
| Rule | Constraint |
|------|------------|
| Syntax | GitHub-compatible Mermaid |
| Max nodes | 15 per diagram |
| Labels | Meaningful, no generic names |

### 4.4 Content Rules
| Rule | Constraint |
|------|------------|
| Emoji usage | MAX 2 per section |
| Paragraph length | MAX 4 sentences |
| Code examples | Complete, runnable |
| Language | Imperative mood for commands |

---

## 5. Validation Checklist

### Pre-Generation
- [ ] Project path exists and is readable
- [ ] Output directory is writable
- [ ] Required scripts are executable

### Post-Generation
- [ ] README.md exists and non-empty
- [ ] All badge URLs are valid (HTTP 200)
- [ ] All image URLs are valid
- [ ] Mermaid syntax is valid
- [ ] Bilingual files match in structure
- [ ] No prohibited emoji in badges
- [ ] TL;DR section present (standard+)
- [ ] No placeholder text (e.g., "Your Name", "example.com")

---

## 6. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-11 | Initial spec |

---

**END OF SPEC.md**
