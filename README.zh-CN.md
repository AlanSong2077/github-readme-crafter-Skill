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

`github-readme-crafter` 是一款基于 **规范驱动开发 (Spec-Driven Development)** 的技能，可使用 AI 生成生产级别的 GitHub README 文档。

该技能遵循 **Harness Engineering** 原则：规范驱动生成，所有输出在交付前必须通过硬约束验证。

## 特性

- 📋 **规范优先开发** — 所有输出均符合 `SPEC.md` 规范
- ✅ **强验证** — 通过 `test.py` 强制执行硬约束
- 🎨 **动态 Banner 生成** — 渐变背景 SVG Banner
- 📊 **Mermaid 图表** — 架构图、技术栈图、工作流图
- 🌐 **双语支持** — 英文和中文版本
- 🌓 **深色/浅色模式** — 主题感知资源
- ⚡ **TL;DR 区块** — 为忙碌的读者提供快速开始

## 快速开始

```bash
# 克隆技能仓库
git clone https://github.com/AlanSong2077/github-readme-crafter-Skill.git
cd github-readme-crafter-Skill

# 为您的项目生成 README
python3 scripts/create_readme.py /path/to/project --style professional --bilingual

# 验证输出（交付前必须执行）
python3 test.py /path/to/project
```

**要求**: Python 3.10+

## 工作流程

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 阅读 SPEC.md                                             │
│    - 所有生成的真实性来源                                     │
│    - 硬约束、章节要求                                       │
├─────────────────────────────────────────────────────────────┤
│ 2. 分析项目                                                 │
│    python3 scripts/analyze_project.py <路径>                │
│    → 返回：语言、框架、结构元数据                            │
├─────────────────────────────────────────────────────────────┤
│ 3. 生成资源                                                 │
│    - Banner（深色 + 浅色变体）                               │
│    - Mermaid 图表（如适用）                                  │
│    - 高级元素（徽章、图表）                                  │
├─────────────────────────────────────────────────────────────┤
│ 4. 编写 README                                              │
│    - 根据风格选择模板（minimal/standard/pro）                │
│    - 插入生成的资源                                          │
│    - 插入分析元数据                                          │
├─────────────────────────────────────────────────────────────┤
│ 5. 验证（硬性要求）                                          │
│    python3 test.py <项目路径>                                │
│    → 交付前必须通过所有 A-E 类测试                           │
├─────────────────────────────────────────────────────────────┤
│ 6. 交付                                                     │
│    - 将文件写入项目目录                                      │
│    - 展示验证状态                                            │
└─────────────────────────────────────────────────────────────┘
```

## 项目结构

```
github-readme-crafter-Skill/
├── SKILL.md                           # 技能定义
├── SPEC.md                           # 规范（真实性来源）
├── Agent.md                          # Agent 操作指南
├── test.md                           # 验证测试定义
├── scripts/
│   ├── create_readme.py             # 主生成器
│   ├── analyze_project.py            # 项目分析器
│   ├── generate_banner.py            # SVG Banner 生成器
│   ├── generate_mermaid.py           # Mermaid 图表生成器
│   └── generate_advanced_elements.py  # 徽章、图表等
└── references/
    ├── templates.md                  # README 模板
    ├── top_projects_analysis.md     # 参考分析
    └── mermaid_examples.md           # 图表示例
```

## 风格选项

| 风格 | 适用场景 | 包含章节 |
|------|----------|----------|
| `minimal` | 小型库 | 标题、徽章、安装、使用、许可证 |
| `standard` | 中型项目 | Banner、TL;DR、特性、图表、安装、使用 |
| `professional` | 大型框架 | 全部章节 + Star 历史、贡献者、赞助商 |

## 验证

所有输出必须通过验证测试：

```bash
python3 test.py /path/to/project
```

### 测试类别

| 类别 | 描述 | 失败操作 |
|------|------|----------|
| A - 结构 | 文件存在性、尺寸 | 硬性失败 |
| B - 内容 | 章节存在、无占位符 | 硬性失败 |
| C - 徽章 | 数量、样式、URL | 硬性失败 |
| D - 图片 | URL 可访问性 | 警告 |
| E - Mermaid | 语法有效性 | 硬性失败 |
| F - 双语 | 文件存在、结构一致性 | 硬性失败 |
| G - 风格 | Emoji 数量、段落长度 | 警告 |

### 通过标准

| 等级 | 错误数 | 警告数 |
|------|--------|--------|
| **通过** | 0 | 任意 |
| **失败** | ≥ 1 | - |

## 设计规则（硬性约束）

### 徽章规则
- 每行最多 5 个徽章
- 样式：`flat-square`（默认）或 `for-the-badge`
- 徽章文本中禁止使用 Emoji
- 仅限 shields.io URL

### Banner 规则
- SVG 格式，1280x320 像素
- 渐变背景（2 种以上颜色）
- 双语项目必须同时提供深色和浅色变体

### Mermaid 规则
- 仅限 GitHub 兼容语法
- 每个图表最多 15 个节点
- 不支持饼图、时间线、甘特图

## 如何贡献

贡献遵循 **规范驱动开发**：

1. 更改前先阅读 `SPEC.md`
2. 如需添加新要求，更新 `SPEC.md`
3. 在 `test.md` 中添加相应验证
4. 在 `Agent.md` 中添加新操作程序
5. 运行 `test.py` 验证更改

## 许可证

MIT 许可证
