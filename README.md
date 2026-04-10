# 🎨 GitHub README Crafter

<p align="center">
  <a href="https://github.com/AlanSong2077/github-readme-crafter-Skill">
    <img src="assets/banner.svg" alt="GitHub README Crafter" width="100%">
  </a>
</p>

<p align="center">
  <a href="https://github.com/AlanSong2077/github-readme-crafter-Skill/stargazers">
    <img src="https://img.shields.io/github/stars/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge&logo=github&color=38bdf8" alt="Stars">
  </a>
  <a href="https://github.com/AlanSong2077/github-readme-crafter-Skill/forks">
    <img src="https://img.shields.io/github/forks/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge&logo=github&color=38bdf8" alt="Forks">
  </a>
  <img src="https://img.shields.io/github/languages/code-size/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge&color=38bdf8" alt="Code Size">
  <img src="https://img.shields.io/github/repo-size/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge&color=38bdf8" alt="Repo Size">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-38bdf8?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-38bdf8?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/actions/workflow/status/AlanSong2077/github-readme-crafter-Skill/ci.yml?style=for-the-badge&branch=main" alt="Build">
  <img src="https://img.shields.io/badge/Standard-SDD-38bdf8?style=for-the-badge&logo=spec" alt="Spec-Driven">
</p>

<p align="center">
  <a href="https://github.com/AlanSong2077/github-readme-crafter-Skill/releases/latest">
    <img src="https://img.shields.io/github/v/release/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge&color=38bdf8" alt="Latest Release">
  </a>
  <img src="https://img.shields.io/github/release-date/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge&color=38bdf8" alt="Release Date">
  <img src="https://img.shields.io/github/last-commit/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge&color=38bdf8" alt="Last Commit">
</p>

<div align="center">

### English | [中文](README.zh-CN.md)

</div>

---

## ✨ What is This?

<p align="center">
  <em>"Every README is a first impression. Make yours unforgettable."</em>
</p>

`github-readme-crafter` transforms ordinary project documentation into **premium, attention-grabbing** README documents using **Spec-Driven Development (SDD)** and **Harness Engineering**.

| Metric | Value |
|--------|-------|
| 📦 Scripts | 5 core generators |
| 📋 Sections | 14 premium sections |
| ✅ Validation | 7 test categories |
| 🌐 Languages | EN + 中文 |
| 🎨 Styles | 2 premium tiers |

---

## 🚀 Quick Start

```bash
# One-liner to glory
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git \
  && cd github-readme-crafter-Skill \
  && python3 scripts/create_readme.py /path/to/project --style professional
```

```bash
# Full validation (REQUIRED before delivery)
python3 test.py /path/to/project
```

**Requires**: Python 3.10+

---

## ⚡ Features

| | Feature | Description |
|---|---------|-------------|
| 🎨 | **Dynamic Banners** | SVG with gradient + geometric decorations, dark/light mode |
| 📊 | **Mermaid Diagrams** | Tech stack, architecture, workflow — auto-generated |
| 🌓 | **Theme-Aware** | Automatic dark/light mode adaptation |
| ⚡ | **TL;DR Sections** | One-command quick start for busy readers |
| 📈 | **Star History** | Interactive project growth visualization |
| 🧪 | **Strong Validation** | 7 categories of HARD constraints, zero tolerance |
| 🌐 | **Bilingual** | English + Chinese, structurally identical |
| 🔒 | **Spec-First** | Specification-driven, no deviation allowed |

---

## 🔬 Architecture

```mermaid
flowchart TB
    classDef process fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc
    classDef output fill:#1e293b,stroke:#22d3ee,stroke-width:2px,color:#f8fafc
    classDef quality fill:#1e293b,stroke:#a78bfa,stroke-width:2px,color:#f8fafc

    subgraph IN[📥 INPUT]
        direction LR
        P[/path/to/project\]
    end

    subgraph ANALYZE[🔍 ANALYZE]
        A[Metadata Extraction]
        L[Language Detection]
        S[Structure Analysis]
    end

    subgraph GENERATE[⚡ GENERATE]
        B[Banner Generator]
        D[Mermaid Diagrams]
        E[Advanced Elements]
    end

    subgraph VALIDATE[🧪 VALIDATE]
        V[test.py]
        H[HARD Constraints]
    end

    subgraph OUT[📤 OUTPUT]
        R[README.md]
        C[README.zh-CN.md]
        A[assets/]
    end

    P --> ANALYZE
    ANALYZE --> GENERATE
    GENERATE --> VALIDATE
    VALIDATE -->|PASS| OUT
    VALIDATE -->|FAIL| GENERATE
    OUT --> R
    OUT --> C
    OUT --> A

    style IN fill:#1e293b,stroke:#38bdf8,color:#f8fafc
    style ANALYZE fill:#0f172a,stroke:#38bdf8,color:#f8fafc
    style GENERATE fill:#0f172a,stroke:#22d3ee,color:#f8fafc
    style VALIDATE fill:#1e293b,stroke:#a78bfa,color:#f8fafc
    style OUT fill:#0f172a,stroke:#22d3ee,color:#f8fafc
```

---

## 📐 Tech Stack

```mermaid
flowchart LR
    subgraph Core["🧠 Core"]
        Py["Python 3.10+"]
        SL["Standard Library"]
    end

    subgraph Services["🌐 Services"]
        SH["Shields.io API"]
        ST["Star-History API"]
        CR["Contrib.rocks"]
    end

    subgraph Output["📦 Output"]
        SVG["SVG Banners"]
        MD["Markdown README"]
        DM["Mermaid Diagrams"]
    end

    Py --> SL
    Py --> SH
    Py --> ST
    Py --> CR
    SH --> SVG
    ST --> MD
    CR --> MD
    SL --> SVG
    SL --> DM
```

---

## 📂 Project Structure

```
github-readme-crafter-Skill/
├── SPEC.md                    # 📜 Specification (source of truth)
├── Agent.md                  # 🤖 Agent instructions
├── test.md                   # 🧪 Test definitions
├── test.py                   # ⚡ Executable validator
│
├── scripts/
│   ├── create_readme.py      # 🚀 Main generator
│   ├── analyze_project.py     # 🔍 Project analyzer
│   ├── generate_banner.py     # 🎨 Banner generator
│   ├── generate_mermaid.py    # 📊 Diagram generator
│   └── generate_advanced_elements.py  # ✨ Badges & more
│
└── references/
    ├── templates.md           # 📋 README templates
    ├── top_projects_analysis.md  # 🏆 Top repo analysis
    └── mermaid_examples.md   # 📈 Diagram examples
```

---

## 🎯 Style Tiers

| Tier | Description | Use Case |
|------|-------------|----------|
| `standard` | All 14 premium sections | Medium projects |
| `professional` | Extended + sponsors, security | Large frameworks |

**Both tiers produce museum-quality documentation.**

---

## 🧪 Validation Pipeline

Every output must pass **ALL 7 categories**:

| Category | Checks | Enforcement |
|----------|--------|-------------|
| **A** | File existence, SVG validity, dimensions | HARD FAIL |
| **B** | TL;DR required, sections complete | HARD FAIL |
| **C** | ≤5 badges, flat-square, no emoji | HARD FAIL |
| **D** | URLs accessible (HTTP 200) | HARD FAIL |
| **E** | Valid Mermaid, ≤15 nodes | HARD FAIL |
| **F** | Bilingual parity, Chinese content | HARD FAIL |

```bash
# Validate your README
python3 test.py /path/to/project

# Exit code 0 = PASS, Exit code 1 = FAIL
```

---

## 📊 Project Stats

| Stat | Badge |
|------|-------|
| Stars | ![Stars](https://img.shields.io/github/stars/AlanSong2077/github-readme-crafter-Skill?style=flat-square) |
| Forks | ![Forks](https://img.shields.io/github/forks/AlanSong2077/github-readme-crafter-Skill?style=flat-square) |
| Size | ![Size](https://img.shields.io/github/repo-size/AlanSong2077/github-readme-crafter-Skill?style=flat-square) |

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AlanSong2077/github-readme-crafter-Skill&type=Date)](https://www.star-history.com/#AlanSong2077/github-readme-crafter-Skill&type=Date)

---

## 👥 Contributors

<a href="https://github.com/AlanSong2077/github-readme-crafter-Skill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AlanSong2077/github-readme-crafter-Skill&max=5" />
</a>

---

## 🔗 Share the Love

<a href="https://github.com/AlanSong2077/github-readme-crafter-Skill">
  <img src="https://img.shields.io/badge/Share%20on-GitHub-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>
<a href="https://reddit.com/submit?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&title=GitHub%20README%20Crafter%20-%20Spec-Driven%20AI%20Documentation">
  <img src="https://img.shields.io/badge/Share%20on-Reddit-ff4500?style=for-the-badge&logo=reddit" alt="Reddit">
</a>
<a href="https://twitter.com/intent/tweet?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&text=GitHub%20README%20Crafter%20-%20Spec-Driven%20AI%20Documentation%20Generator">
  <img src="https://img.shields.io/badge/Share%20on-Twitter-1da1f2?style=for-the-badge&logo=twitter" alt="Twitter">
</a>
<a href="https://news.ycombinator.com/submitlink?u=https://github.com/AlanSong2077/github-readme-crafter-Skill">
  <img src="https://img.shields.io/badge/Share%20on-Hacker%20News-ff6600?style=for-the-badge&logo=ycombinator" alt="Hacker News">
</a>

---

## 🤝 Contributing

We follow **Spec-Driven Development**:

1. Read `SPEC.md` — source of truth
2. Make changes
3. Update `test.py` if needed
4. Run `python3 test.py` to verify
5. Submit PR

---

## 📜 License

MIT License

---

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-38bdf8?style=for-the-badge&logo=python&logoColor=white" alt="Made with Python">
  <img src="https://img.shields.io/badge/Powered%20by-Spec%20Driven%20Development-38bdf8?style=for-the-badge&logo=spec" alt="Spec-Driven">
</p>

<p align="center">
  <a href="https://github.com/AlanSong2077">@AlanSong2077</a> • 2026
</p>
