# 🎨 GitHub README Crafter

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
    <img src="assets/banner.svg" alt="GitHub README Crafter" width="100%">
  </picture>
</div>

<div align="center">

### [English](README.md) | 中文

</div>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/AlanSong2077/github-readme-crafter-Skill?style=for-the-badge)
![Build](https://img.shields.io/github/actions/workflow/status/AlanSong2077/github-readme-crafter-Skill/ci.yml?style=for-the-badge)

</p>

> **让您的项目文档从默默无闻到引人注目。**
> AI 驱动的生成器配合规范驱动开发，确保每个 README 都是高端的第一印象。

## ✨ 特性

| 特性 | 描述 |
|------|------|
| 🎨 **动态 Banner** | 带渐变背景和几何装饰的 SVG Banner |
| 📊 **Mermaid 图表** | 自动生成技术栈和架构可视化 |
| 🌐 **双语支持** | 英文和中文，结构完全一致 |
| 🌓 **深色/浅色模式** | 自动适配主题的资源 |
| ⚡ **TL;DR 快速开始** | 一条命令立即上手 |
| 📈 **Star 历史** | 交互式项目增长可视化 |
| 👥 **贡献者展示** | 自动贡献者展示 |
| 📢 **分享按钮** | Reddit、Hacker News、Twitter、LinkedIn |

## 🚀 快速开始

```bash
# 克隆技能仓库
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git
cd github-readme-crafter-Skill

# 生成高端 README
python3 scripts/create_readme.py /path/to/project --style professional

# 验证（必须执行）
python3 test.py /path/to/project
```

**要求**: Python 3.10+

## 🔧 工作原理

```mermaid
flowchart TB
    classDef service fill:#e0e7ff,stroke:#4338ca,stroke-width:2px
    classDef output fill:#d1fae5,stroke:#059669,stroke-width:2px
    
    subgraph Analyze["🔍 分析"]
        A[提取元数据]
    end
    
    subgraph Generate["⚡ 生成"]
        B[创建 Banner]
        C[构建图表]
        D[添加元素]
    end
    
    subgraph Validate["✅ 验证"]
        E[测试输出]
    end
    
    subgraph Deliver["📦 交付"]
        F[高端 README]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    E -->|通过| F
    E -->|失败| B
```

## 📐 技术栈

```mermaid
flowchart TB
    subgraph Frontend["🎨 前端"]
        Python["Python 3.10+"]
    end
    
    subgraph Backend["🔧 后端"]
        StdLib["标准库"]
        Shields["Shields.io API"]
    end
    
    subgraph Storage["💾 存储"]
        FS["文件系统"]
    end
    
    subgraph VCS["📂 版本控制"]
        Git["Git"]
    end
    
    Python --> StdLib
    Python --> Shields
    StdLib --> FS
    Shields --> FS
    Python --> Git
```

## 📁 项目结构

```
github-readme-crafter-Skill/
├── SPEC.md                    # 规范（真实性来源）
├── Agent.md                  # Agent 操作指南
├── test.md                   # 验证测试定义
├── test.py                   # 可执行验证器
├── scripts/
│   ├── create_readme.py      # 主生成器
│   ├── analyze_project.py     # 项目分析器
│   ├── generate_banner.py     # SVG Banner 生成器
│   ├── generate_mermaid.py     # 图表生成器
│   └── generate_advanced_elements.py
└── references/
    ├── templates.md           # README 模板
    ├── top_projects_analysis.md
    └── mermaid_examples.md
```

## 🎯 风格层级

| 层级 | 描述 |
|------|------|
| `standard` | 包含所有高端章节 |
| `professional` | + 赞助商、扩展架构、安全 |

两种风格都产生令人惊艳的文档。每个 README 都是一件艺术品。

## 🛡️ 验证

每个输出都通过 **7 大类硬性验证测试**：

| 类别 | 测试 | 失败处理 |
|------|------|----------|
| A - 结构 | 文件、尺寸 | 硬性失败 |
| B - 内容 | TL;DR、章节 | 硬性失败 |
| C - 徽章 | 数量、样式、URL | 硬性失败 |
| D - 图片 | 可访问性 | 硬性失败 |
| E - Mermaid | 语法有效性 | 硬性失败 |
| F - 双语 | 一致性检查 | 硬性失败 |

```bash
# 验证您的 README
python3 test.py /path/to/project
```

## 📊 Star 历史

[![Star History 图表](https://api.star-history.com/svg?repos=AlanSong2077/github-readme-crafter-Skill&type=Date)](https://www.star-history.com/#AlanSong2077/github-readme-crafter-Skill&type=Date)

## 👥 贡献者

<a href="https://github.com/AlanSong2077/github-readme-crafter-Skill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AlanSong2077/github-readme-crafter-Skill" />
</a>

## 🔗 分享

[![Reddit](https://img.shields.io/badge/Reddit-分享-red?style=for-the-badge&logo=reddit)](https://reddit.com/submit?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&title=GitHub%20README%20Crafter%20-%20AI%20驱动的%20Premium%20文档生成器)
[![Hacker News](https://img.shields.io/badge/Hacker%20News-分享-orange?style=for-the-badge&logo=ycombinator)](https://news.ycombinator.com/submitlink?u=https://github.com/AlanSong2077/github-readme-crafter-Skill)
[![Twitter](https://img.shields.io/badge/Twitter-分享-blue?style=for-the-badge&logo=twitter)](https://twitter.com/share?url=https://github.com/AlanSong2077/github-readme-crafter-Skill&text=GitHub%20README%20Crafter%20-%20AI%20驱动的%20Premium%20文档生成器)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-分享-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/shareArticle?mini=true&url=https://github.com/AlanSong2077/github-readme-crafter-Skill&title=GitHub%20README%20Crafter)

## 🤝 贡献

贡献遵循 **规范驱动开发 (Spec-Driven Development)**：

1. 更改前先阅读 `SPEC.md`
2. 如需添加新要求，更新 `SPEC.md`
3. 在 `test.md` 中添加相应验证
4. 运行 `python3 test.py` 验证

## 📄 许可证

MIT 许可证

---

<p align="center">

**用 ❤️ 由 AlanSong2077 制作**

</p>
