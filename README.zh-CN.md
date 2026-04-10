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

### [English](README.md) | 中文

</div>

---

## ✨ 这是什么?

<p align="center">
  <em>"每个 README 都是第一印象。让你的令人难忘。"</em>
</p>

`github-readme-crafter` 使用 **规范驱动开发 (SDD)** 和 **Harness Engineering** 将普通项目文档转化为**高端、引人注目**的 README 文档。

| 指标 | 数值 |
|------|------|
| 📦 脚本 | 5 个核心生成器 |
| 📋 章节 | 14 个高端章节 |
| ✅ 验证 | 7 大测试类别 |
| 🌐 语言 | EN + 中文 |
| 🎨 风格 | 2 种高端层级 |

---

## 🚀 快速开始

```bash
# 一行命令搞定
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git \
  && cd github-readme-crafter-Skill \
  && python3 scripts/create_readme.py /path/to/project --style professional
```

```bash
# 完整验证（交付前必须执行）
python3 test.py /path/to/project
```

**要求**: Python 3.10+

---

## ⚡ 特性

| | 特性 | 描述 |
|---|------|------|
| 🎨 | **动态 Banner** | SVG 渐变 + 几何装饰，深色/浅色模式 |
| 📊 | **Mermaid 图表** | 技术栈、架构、工作流 — 自动生成 |
| 🌓 | **主题适配** | 自动深色/浅色模式切换 |
| ⚡ | **TL;DR 区块** | 一命令快速开始 |
| 📈 | **Star 历史** | 交互式项目增长可视化 |
| 🧪 | **强验证** | 7 类别 HARD 约束，零容忍 |
| 🌐 | **双语支持** | 英文 + 中文，结构完全一致 |
| 🔒 | **规范优先** | 规范驱动，不允许偏差 |

---

## 🔬 架构

```mermaid
flowchart TB
    classDef process fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc
    classDef output fill:#1e293b,stroke:#22d3ee,stroke-width:2px,color:#f8fafc
    classDef quality fill:#1e293b,stroke:#a78bfa,stroke-width:2px,color:#f8fafc

    subgraph IN[📥 输入]
        direction LR
        P[/path/to/project\]
    end

    subgraph ANALYZE[🔍 分析]
        A[元数据提取]
        L[语言检测]
        S[结构分析]
    end

    subgraph GENERATE[⚡ 生成]
        B[Banner 生成器]
        D[Mermaid 图表]
        E[高级元素]
    end

    subgraph VALIDATE[🧪 验证]
        V[test.py]
        H[HARD 约束]
    end

    subgraph OUT[📤 输出]
        R[README.md]
        C[README.zh-CN.md]
        A[assets/]
    end

    P --> ANALYZE
    ANALYZE --> GENERATE
    GENERATE --> VALIDATE
    VALIDATE -->|通过| OUT
    VALIDATE -->|失败| GENERATE
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

## 📐 技术栈

```mermaid
flowchart LR
    subgraph Core["🧠 核心"]
        Py["Python 3.10+"]
        SL["标准库"]
    end

    subgraph Services["🌐 服务"]
        SH["Shields.io API"]
        ST["Star-History API"]
        CR["Contrib.rocks"]
    end

    subgraph Output["📦 输出"]
        SVG["SVG Banner"]
        MD["Markdown README"]
        DM["Mermaid 图表"]
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

## 📂 项目结构

```
github-readme-crafter-Skill/
├── SPEC.md                    # 📜 规范（真实性来源）
├── Agent.md                  # 🤖 Agent 指令
├── test.md                   # 🧪 测试定义
├── test.py                   # ⚡ 可执行验证器
│
├── scripts/
│   ├── create_readme.py      # 🚀 主生成器
│   ├── analyze_project.py     # 🔍 项目分析器
│   ├── generate_banner.py    # 🎨 Banner 生成器
│   ├── generate_mermaid.py   # 📊 图表生成器
│   └── generate_advanced_elements.py  # ✨ 徽章等
│
└── references/
    ├── templates.md           # 📋 README 模板
    ├── top_projects_analysis.md  # 🏆 顶级仓库分析
    └── mermaid_examples.md    # 📈 图表示例
```

---

## 🎯 风格层级

| 层级 | 描述 | 适用场景 |
|------|------|----------|
| `standard` | 全部 14 个高端章节 | 中型项目 |
| `professional` | 扩展 + 赞助商、安全 | 大型框架 |

**两种风格都产出博物馆级文档。**

---

## 🧪 验证流水线

每个输出必须通过 **全部 7 类别**：

| 类别 | 检查项 | 执行方式 |
|------|--------|----------|
| **A** | 文件存在、SVG 有效性、尺寸 | HARD FAIL |
| **B** | TL;DR 必须有、章节完整 | HARD FAIL |
| **C** | ≤5 徽章、flat-square、无 emoji | HARD FAIL |
| **D** | URL 可访问 (HTTP 200) | HARD FAIL |
| **E** | 有效 Mermaid、≤15 节点 | HARD FAIL |
| **F** | 双语一致性、中文内容 | HARD FAIL |

```bash
# 验证你的 README
python3 test.py /path/to/project

# 退出码 0 = 通过, 退出码 1 = 失败
```

---

## 📊 项目统计

| 统计 | 徽章 |
|------|-------|
| Stars | ![Stars](https://img.shields.io/github/stars/AlanSong2077/github-readme-crafter-Skill?style=flat-square) |
| Forks | ![Forks](https://img.shields.io/github/forks/AlanSong2077/github-readme-crafter-Skill?style=flat-square) |
| Size | ![Size](https://img.shields.io/github/repo-size/AlanSong2077/github-readme-crafter-Skill?style=flat-square) |

---

## 📈 Star 历史

[![Star History 图表](https://api.star-history.com/svg?repos=AlanSong2077/github-readme-crafter-Skill&type=Date)](https://www.star-history.com/#AlanSong2077/github-readme-crafter-Skill&type=Date)

---

## 👥 贡献者

<a href="https://github.com/AlanSong2077/github-readme-crafter-Skill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AlanSong2077/github-readme-crafter-Skill&max=5" />
</a>

---

## 🔗 分享

<a href="https://github.com/AlanSong2077/github-readme-crafter-Skill">
  <img src="https://img.shields.io/badge/分享-GitHub-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>
<a href="https://reddit.com/submit?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&title=GitHub%20README%20Crafter%20-%20Spec-Driven%20AI%20Documentation">
  <img src="https://img.shields.io/badge/分享-Reddit-ff4500?style=for-the-badge&logo=reddit" alt="Reddit">
</a>
<a href="https://twitter.com/intent/tweet?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&text=GitHub%20README%20Crafter%20-%20Spec-Driven%20AI%20Documentation%20Generator">
  <img src="https://img.shields.io/badge/分享-Twitter-1da1f2?style=for-the-badge&logo=twitter" alt="Twitter">
</a>
<a href="https://news.ycombinator.com/submitlink?u=https://github.com/AlanSong2077/github-readme-crafter-Skill">
  <img src="https://img.shields.io/badge/分享-Hacker%20News-ff6600?style=for-the-badge&logo=ycombinator" alt="Hacker News">
</a>

---

## 🤝 贡献

我们遵循 **规范驱动开发**：

1. 阅读 `SPEC.md` — 真实性来源
2. 进行更改
3. 如需更新 `test.py`
4. 运行 `python3 test.py` 验证
5. 提交 PR

---

## 📜 许可证

MIT 许可证

---

<p align="center">
  <img src="https://img.shields.io/badge/用-Python-38bdf8?style=for-the-badge&logo=python&logoColor=white" alt="用 Python 制作">
  <img src="https://img.shields.io/badge/驱动-规范-38bdf8?style=for-the-badge&logo=spec" alt="Spec-Driven">
</p>

<p align="center">
  <a href="https://github.com/AlanSong2077">@AlanSong2077</a> • 2026
</p>
