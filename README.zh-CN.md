# GitHub README Crafter

<div align="center">

![Banner](assets/banner.svg)

### [English](README.md) | 中文

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/AlanSong2077/github-readme-crafter-Skill?style=flat-square" alt="Stars">
</p>

## 简介

`github-readme-crafter` 是一款基于 **规范驱动开发 (Spec-Driven Development)** 的技能，可生成**高端、吸引眼球**的 GitHub README 文档。

**每个 README 都是第一印象。** 此技能生成的文档让访问者觉得"这个项目非常专业且维护良好"。

## 特性

- 🎨 **高端 Banner** — 带渐变背景和几何装饰的 SVG Banner
- 📊 **Mermaid 图表** — 技术栈和架构可视化
- 🌐 **双语支持** — 英文和中文，结构一致
- 🌓 **深色/浅色模式** — 主题感知资源
- ⚡ **TL;DR 快速开始** — 一条命令立即上手
- 📈 **Star 历史** — 增长追踪可视化
- 👥 **贡献者** — 展示你的社区
- 📢 **分享按钮** — Reddit、Hacker News、Twitter、LinkedIn

## 快速开始

```bash
# 克隆技能仓库
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git
cd github-readme-crafter-Skill

# 为您的项目生成高端 README
python3 scripts/create_readme.py /path/to/project --style professional

# 验证输出（必须执行）
python3 test.py /path/to/project
```

**要求**: Python 3.10+

## 工作流程

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 阅读 SPEC.md                                             │
│    - 所有生成的真实性来源                                     │
│    - 高端优先：无 minimal 模式                              │
├─────────────────────────────────────────────────────────────┤
│ 2. 分析项目                                                 │
│    python3 scripts/analyze_project.py <路径>                │
├─────────────────────────────────────────────────────────────┤
│ 3. 生成资源                                                 │
│    - 深色 + 浅色 Banner（两者都必须）                        │
│    - 技术栈图表                                             │
│    - 架构图表（如适用）                                     │
├─────────────────────────────────────────────────────────────┤
│ 4. 编写 README                                              │
│    - Banner + 徽章 + TL;DR + 所有必需章节                    │
│    - 双语（英文 + 中文）                                    │
├─────────────────────────────────────────────────────────────┤
│ 5. 验证（必须执行）                                         │
│    python3 test.py <项目路径>                               │
│    → 0 个错误才能交付                                       │
├─────────────────────────────────────────────────────────────┤
│ 6. 交付                                                     │
│    - 写入文件                                               │
│    - 展示验证状态                                           │
└─────────────────────────────────────────────────────────────┘
```

## 项目结构

```
github-readme-crafter-Skill/
├── SKILL.md                           # 技能定义
├── SPEC.md                           # 规范（真实性来源）
├── Agent.md                          # Agent 操作指南
├── test.md                           # 验证测试定义
├── test.py                           # 可执行验证脚本
├── scripts/
│   ├── create_readme.py            # 主生成器
│   ├── analyze_project.py            # 项目分析器
│   ├── generate_banner.py            # SVG Banner 生成器
│   ├── generate_mermaid.py           # Mermaid 图表生成器
│   └── generate_advanced_elements.py  # 徽章、图表等
└── references/
    ├── templates.md                  # README 模板
    ├── top_projects_analysis.md     # 参考分析
    └── mermaid_examples.md           # 图表示例
```

## 必需章节

每个 README 必须包含：

| 章节 | 描述 |
|------|------|
| Banner | 带几何装饰的渐变 SVG |
| 语言切换 | English \| 中文 |
| 徽章 | 最多 5 个，flat-square 样式 |
| TL;DR | 一条命令快速开始 |
| 简介 | 价值主张 |
| 特性 | 3-5 个要点，带 emoji |
| 安装 | 可复制命令 |
| 使用 | 可运行代码示例 |
| 技术栈 | Mermaid 图表 |
| Star 历史 | 增长图表 |
| 贡献者 | 展示 |
| 分享按钮 | 社交分享 |
| 贡献指南 | 指南 |
| 许可证 | MIT |

## 风格层级

| 风格 | 描述 |
|------|------|
| `standard` | 所有必需章节 + 技术栈图表 |
| `professional` | Standard + 赞助商、扩展架构、开发频道 |

**两种风格都产生高端输出。** 区别在于深度，而非质量。

## 验证

所有输出必须通过验证测试：

```bash
python3 test.py /path/to/project
```

### 测试类别

| 类别 | 描述 | 失败操作 |
|------|------|----------|
| A - 结构 | 文件存在、尺寸 | 硬性失败 |
| B - 内容 | TL;DR、章节、无占位符 | 硬性失败 |
| C - 徽章 | 数量、样式、URL | 硬性失败 |
| D - 图片 | URL 可访问性 | 警告 |
| E - Mermaid | 语法有效性 | 硬性失败 |
| F - 双语 | 文件存在、结构一致性 | 硬性失败 |

### 通过标准

| 等级 | 错误数 | 结果 |
|------|--------|------|
| **通过** | 0 | 可交付 |
| **失败** | ≥ 1 | 修复后再交付 |

## 设计规则

### 徽章规则
- 每行最多 5 个徽章
- 样式：`flat-square`
- 徽章文本中禁止使用 Emoji
- 仅限 shields.io URL

### Banner 规则
- SVG 格式，1280x320 像素
- 渐变背景（2 种以上颜色）
- 必须有几何装饰
- 深色和浅色变体（两者都必须）

### Mermaid 规则
- 仅限 GitHub 兼容语法
- 每个图表最多 15 个节点
- 至少 1 个图表

## 如何贡献

贡献遵循 **规范驱动开发**：

1. 更改前先阅读 `SPEC.md`
2. 如需添加新要求，更新 `SPEC.md`
3. 在 `test.md` 中添加相应验证
4. 在 `Agent.md` 中添加新操作程序
5. 运行 `test.py` 验证更改

## 许可证

MIT 许可证
