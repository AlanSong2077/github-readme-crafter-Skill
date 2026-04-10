# 🎨 GitHub README Crafter

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
    <img src="assets/banner.svg" alt="GitHub README Crafter" width="100%">
  </picture>
</div>

<div align="center">

### English | [中文](README.zh-CN.md)

</div>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge)
![Build](https://img.shields.io/github/actions/workflow/status/AlanSong2077/github-readme-crafter-Skill/ci.yml?style=for-the-badge)

</p>

> **Transform your project documentation from invisible to irresistible.**
> AI-powered generation with Spec-Driven Development ensures every README is a premium first impression.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Dynamic Banners** | SVG banners with gradient backgrounds and geometric decorations |
| 📊 **Mermaid Diagrams** | Auto-generated tech stack and architecture visualizations |
| 🌐 **Bilingual** | English and Chinese, structurally identical |
| 🌓 **Dark/Light Mode** | Theme-aware assets that adapt automatically |
| ⚡ **TL;DR Quick Start** | One command to immediate productivity |
| 📈 **Star History** | Interactive project growth visualization |
| 👥 **Contributors** | Automatic contributor showcase |
| 📢 **Share Buttons** | Reddit, Hacker News, Twitter, LinkedIn |

## 🚀 Quick Start

```bash
# Clone the skill
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git
cd github-readme-crafter-Skill

# Generate premium README
python3 scripts/create_readme.py /path/to/project --style professional

# Validate (REQUIRED)
python3 test.py /path/to/project
```

**Requirements**: Python 3.10+

## 🔧 How It Works

```mermaid
flowchart TB
    classDef service fill:#e0e7ff,stroke:#4338ca,stroke-width:2px
    classDef output fill:#d1fae5,stroke:#059669,stroke-width:2px
    
    subgraph Analyze["🔍 Analyze"]
        A[Extract Metadata]
    end
    
    subgraph Generate["⚡ Generate"]
        B[Create Banner]
        C[Build Diagrams]
        D[Add Elements]
    end
    
    subgraph Validate["✅ Validate"]
        E[Test Output]
    end
    
    subgraph Deliver["📦 Deliver"]
        F[Premium README]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    E -->|Pass| F
    E -->|Fail| B
```

## 📐 Tech Stack

```mermaid
flowchart TB
    subgraph Frontend["🎨 Frontend"]
        Python["Python 3.10+"]
    end
    
    subgraph Backend["🔧 Backend"]
        StdLib["Standard Library"]
        Shields["Shields.io API"]
    end
    
    subgraph Storage["💾 Storage"]
        FS["File System"]
    end
    
    subgraph VCS["📂 VCS"]
        Git["Git"]
    end
    
    Python --> StdLib
    Python --> Shields
    StdLib --> FS
    Shields --> FS
    Python --> Git
```

## 📁 Project Structure

```
github-readme-crafter-Skill/
├── SPEC.md                    # Specification (source of truth)
├── Agent.md                  # Agent operating instructions
├── test.md                   # Validation test definitions
├── test.py                   # Executable validator
├── scripts/
│   ├── create_readme.py      # Main generator
│   ├── analyze_project.py     # Project analyzer
│   ├── generate_banner.py     # SVG banner generator
│   ├── generate_mermaid.py     # Diagram generator
│   └── generate_advanced_elements.py
└── references/
    ├── templates.md           # README templates
    ├── top_projects_analysis.md
    └── mermaid_examples.md
```

## 🎯 Style Tiers

| Tier | Description |
|------|-------------|
| `standard` | All premium sections included |
| `professional` | + Sponsors, extended architecture, security |

Both tiers produce visually stunning documentation. Every README is a masterpiece.

## 🛡️ Validation

Every output passes **7 categories of hard validation tests**:

| Category | Tests | Failure |
|----------|-------|---------|
| A - Structural | Files, dimensions | HARD |
| B - Content | TL;DR, sections | HARD |
| C - Badges | Count, style, URLs | HARD |
| D - Images | Accessibility | HARD |
| E - Mermaid | Syntax validity | HARD |
| F - Bilingual | Parity check | HARD |

```bash
# Validate your README
python3 test.py /path/to/project
```

## 📊 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AlanSong2077/github-readme-crafter-Skill&type=Date)](https://www.star-history.com/#AlanSong2077/github-readme-crafter-Skill&type=Date)

## 👥 Contributors

<a href="https://github.com/AlanSong2077/github-readme-crafter-Skill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AlanSong2077/github-readme-crafter-Skill" />
</a>

## 🔗 Share

[![Reddit](https://img.shields.io/badge/Reddit-Share-red?style=for-the-badge&logo=reddit)](https://reddit.com/submit?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&title=GitHub%20README%20Crafter%20-%20AI-Powered%20Premium%20Documentation)
[![Hacker News](https://img.shields.io/badge/Hacker%20News-Share-orange?style=for-the-badge&logo=ycombinator)](https://news.ycombinator.com/submitlink?u=https://github.com/AlanSong2077/github-readme-crafter-Skill)
[![Twitter](https://img.shields.io/badge/Twitter-Share-blue?style=for-the-badge&logo=twitter)](https://twitter.com/share?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&text=GitHub%20README%20Crafter%20-%20AI-Powered%20Premium%20Documentation)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Share-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/shareArticle?mini=true&url=https://github.com/AlanSong2077/github-readme-crafter-Skill&title=GitHub%20README%20Crafter)

## 🤝 Contributing

Contributions follow **Spec-Driven Development**:

1. Read `SPEC.md` before making changes
2. Update `SPEC.md` if adding new requirements
3. Update `test.md` with corresponding validation
4. Run `python3 test.py` to verify

## 📄 License

MIT License

---

<p align="center">

**Made with ❤️ by AlanSong2077**

</p>
