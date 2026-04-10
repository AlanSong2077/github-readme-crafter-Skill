#!/usr/bin/env python3
"""
README生成器主入口 - 整合所有组件生成专业README
"""
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional

from analyze_project import analyze_project
from generate_banner import generate_svg_banner, banner_to_base64_svg
from generate_mermaid import MermaidGenerator, detect_tech_stack


def get_shield_badges(project_info: Dict) -> str:
    """生成Shields.io风格的徽章"""
    badges = []
    
    # 语言徽章
    if project_info.get('language'):
        lang = project_info['language'].replace('/', '%2F')
        badges.append(f"![Language](https://img.shields.io/badge/Language-{lang}-blue)")
    
    # 框架徽章
    if project_info.get('framework'):
        fw = project_info['framework'].replace(' ', '%20')
        badges.append(f"![Framework](https://img.shields.io/badge/Framework-{fw}-green)")
    
    # 许可证徽章
    if project_info.get('has_license'):
        badges.append("![License](https://img.shields.io/badge/License-MIT-yellow)")
    
    return " ".join(badges) if badges else ""


def generate_features_section(language: str, framework: Optional[str]) -> str:
    """生成特性列表，基于项目类型"""
    
    common_features = [
        "Modern architecture with clean code principles",
        "Comprehensive documentation and examples",
        "Production-ready with best practices",
    ]
    
    lang_features = {
        'Python': [
            "Type hints support for better IDE experience",
            "Async/await support for high performance",
            "Extensive test coverage with pytest",
        ],
        'JavaScript': [
            "ES6+ modern JavaScript syntax",
            "Hot module replacement for development",
            "Tree-shaking for optimized bundles",
        ],
        'TypeScript': [
            "Full TypeScript support with strict types",
            "Intelligent code completion",
            "Compile-time error detection",
        ],
        'Go': [
            "High performance with minimal memory footprint",
            "Built-in concurrency with goroutines",
            "Static binary compilation",
        ],
        'Rust': [
            "Memory safety without garbage collector",
            "Zero-cost abstractions",
            "Fearless concurrency",
        ],
    }
    
    features = common_features + lang_features.get(language, [])
    
    lines = ["## Features", ""]
    for feat in features[:5]:
        lines.append(f"- {feat}")
    lines.append("")
    
    return '\n'.join(lines)


def generate_installation_section(project_info: Dict) -> str:
    """生成安装说明"""
    language = project_info.get('language', '')
    name = project_info.get('name', 'project')
    
    sections = ["## Installation", ""]
    
    if 'Python' in language:
        sections.extend([
            "### Using pip",
            "",
            f"```bash\npip install {name.lower().replace('-', '_')}\n```",
            "",
            "### From source",
            "",
            "```bash\ngit clone https://github.com/username/" + name + ".git\ncd " + name + "\npip install -e .\n```",
            "",
        ])
    elif 'JavaScript' in language or 'TypeScript' in language:
        sections.extend([
            "### Using npm",
            "",
            f"```bash\nnpm install {name}\n```",
            "",
            "### Using yarn",
            "",
            f"```bash\nyarn add {name}\n```",
            "",
            "### Using pnpm",
            "",
            f"```bash\npnpm add {name}\n```",
            "",
        ])
    elif language == 'Go':
        sections.extend([
            "```bash\ngo get github.com/username/" + name + "\n```",
            "",
        ])
    elif language == 'Rust':
        sections.extend([
            f"Add to your `Cargo.toml`:",
            "",
            f"```toml\n[dependencies]\n{name.lower().replace('-', '_')} = \"0.1.0\"\n```",
            "",
        ])
    else:
        sections.extend([
            "```bash\ngit clone https://github.com/username/" + name + ".git\ncd " + name + "\n# Follow project-specific instructions\n```",
            "",
        ])
    
    return '\n'.join(sections)


def generate_usage_section(project_info: Dict) -> str:
    """生成使用示例"""
    language = project_info.get('language', '')
    name = project_info.get('name', 'project')
    
    sections = ["## Quick Start", ""]
    
    if 'Python' in language:
        sections.extend([
            "```python",
            f"import {name.lower().replace('-', '_')}",
            "",
            "# Initialize the client",
            f"client = {name.lower().replace('-', '_')}.Client()",
            "",
            "# Use the API",
            "result = client.process()",
            "print(result)",
            "```",
            "",
        ])
    elif 'JavaScript' in language or 'TypeScript' in language:
        sections.extend([
            "```javascript",
            f"import {{ {name.replace('-', '').title()} }} from '{name}';",
            "",
            "// Initialize",
            f"const app = new {name.replace('-', '').title()}();",
            "",
            "// Use the API",
            "const result = await app.process();",
            "console.log(result);",
            "```",
            "",
        ])
    elif language == 'Go':
        sections.extend([
            "```go",
            f"package main\n",
            f"import \"{name}\"",
            "",
            "func main() {",
            f"    client := {name}.NewClient()",
            "    result := client.Process()",
            "}",
            "```",
            "",
        ])
    else:
        sections.extend([
            "Please refer to the documentation for detailed usage instructions.",
            "",
        ])
    
    return '\n'.join(sections)


def generate_chinese_version(project_info: Dict, english_readme: str) -> str:
    """生成中文版本README（保持技术术语英文）"""
    
    translations = {
        '## Features': '## 特性',
        '## Installation': '## 安装',
        '## Quick Start': '## 快速开始',
        '## Usage': '## 使用说明',
        '## Documentation': '## 文档',
        '## Contributing': '## 贡献指南',
        '## License': '## 许可证',
        '## System Architecture': '## 系统架构',
        '## Project Structure': '## 项目结构',
        '## Tech Stack': '## 技术栈',
        '## Overview': '## 项目概述',
        '## Table of Contents': '## 目录',
        # 内容翻译
        'Modern architecture with clean code principles': '采用简洁代码原则的现代架构设计',
        'Comprehensive documentation and examples': '完善的文档和示例代码',
        'Production-ready with best practices': '生产就绪，遵循最佳实践',
        'Type hints support for better IDE experience': '支持类型提示，提供更好的IDE体验',
        'Async/await support for high performance': '支持Async/await，实现高性能',
        'Extensive test coverage with pytest': '使用pytest实现全面的测试覆盖',
        'Contributions are welcome': '欢迎贡献代码',
        'Please feel free to submit a Pull Request': '请随时提交Pull Request',
        'For major changes, please open an issue first': '对于重大变更，请先提交issue讨论',
        'This project is licensed under the MIT License': '本项目采用MIT许可证',
        'see the [LICENSE](LICENSE) file for details': '详情请查看[LICENSE](LICENSE)文件',
        # 安装说明
        '### Using pip': '### 使用 pip',
        '### Using npm': '### 使用 npm',
        '### Using yarn': '### 使用 yarn',
        '### Using pnpm': '### 使用 pnpm',
        '### From source': '### 从源码安装',
        # 其他
        'Fork the repository': 'Fork本仓库',
        'Create your feature branch': '创建特性分支',
        'Commit your changes': '提交变更',
        'Push to the branch': '推送到分支',
        'Open a Pull Request': '创建Pull Request',
    }
    
    chinese = english_readme
    for en, cn in translations.items():
        chinese = chinese.replace(en, cn)
    
    # 添加语言切换链接
    lang_switch = """<div align="right">

[English](README.md) | [中文](README.zh-CN.md)

</div>

"""
    
    return lang_switch + chinese


def create_readme(project_path: str, 
                  style: str = 'professional',
                  include_banner: bool = True,
                  include_diagrams: bool = True,
                  include_advanced: bool = True,
                  bilingual: bool = False,
                  repo_owner: Optional[str] = None,
                  repo_name: Optional[str] = None) -> Dict[str, str]:
    """
    创建完整README文档
    
    Args:
        project_path: 项目路径
        style: 'minimal', 'professional', 'detailed'
        include_banner: 是否包含横幅
        include_diagrams: 是否包含架构图
        include_advanced: 是否包含高级元素(contributors, roadmap等)
        bilingual: 是否生成中文版本
        repo_owner: GitHub仓库所有者（用于高级元素）
        repo_name: GitHub仓库名称（用于高级元素）
    
    Returns: {'en': english_content, 'zh': chinese_content (if bilingual)}
    """
    from generate_advanced_elements import AdvancedElementsGenerator
    
    # 分析项目
    project_info = analyze_project(project_path)
    
    # 生成Banner
    banner_section = ""
    if include_banner:
        banner_svg = generate_svg_banner(
            project_info['name'],
            project_info.get('description', '')
        )
        # 使用GitHub作为图片托管的替代方案：保存到assets
        banner_path = Path(project_path) / 'assets' / 'banner.svg'
        banner_path.parent.mkdir(exist_ok=True)
        banner_path.write_text(banner_svg)
        
        banner_section = f"<div align=\"center\">\n\n![Banner](./assets/banner.svg)\n\n</div>\n\n"
    
    # 生成徽章
    badges = get_shield_badges(project_info)
    badge_section = f"<div align=\"center\">\n\n{badges}\n\n</div>\n\n" if badges else ""
    
    # 描述
    description = project_info.get('description', f"A {project_info['language']} project.")
    desc_section = f"## Overview\n\n{description}\n\n"
    
    # 目录（可选）
    toc = """## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

"""
    
    # 特性
    features = generate_features_section(project_info['language'], project_info.get('framework'))
    
    # 安装
    installation = generate_installation_section(project_info)
    
    # 快速开始
    usage = generate_usage_section(project_info)
    
    # 架构图
    diagram_section = ""
    if include_diagrams:
        gen = MermaidGenerator()
        stack = detect_tech_stack(project_path)
        if any(stack.values()):
            diagram = gen.tech_stack_diagram(
                stack.get('frontend', ['-']),
                stack.get('backend', ['-']),
                stack.get('database', ['-']),
                stack.get('devops', [])
            )
            diagram_section = f"## Tech Stack\n\n{diagram}\n\n"
    
    # 项目结构
    structure_section = f"## Project Structure\n\n```\n{project_info['directory_structure']}\n```\n\n"
    
    # 贡献和许可证
    contributing_section = """## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

"""
    
    license_section = """## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

"""
    
    # 高级元素（仅在detailed样式或明确启用时）
    advanced_sections = []
    if include_advanced and style in ('professional', 'detailed'):
        adv_gen = AdvancedElementsGenerator()
        
        # Roadmap
        if style == 'detailed':
            roadmap_items = [
                {"title": "Core Features", "status": "done", "description": "Basic functionality"},
                {"title": "Advanced API", "status": "in-progress", "description": "Extended capabilities"},
                {"title": "Documentation", "status": "in-progress", "description": "Complete guides"},
            ]
            advanced_sections.append(adv_gen.roadmap_section(roadmap_items))
        
        # Contributors (需要repo信息)
        if repo_owner and repo_name:
            advanced_sections.append(adv_gen.contributors_section(repo_owner, repo_name))
    
    # 组装英文README - 根据样式选择包含的章节
    readme_parts = [banner_section, badge_section, desc_section]
    
    if style != 'minimal':
        readme_parts.append(toc)
    
    readme_parts.extend([features, installation, usage])
    
    if include_diagrams and style != 'minimal':
        readme_parts.append(diagram_section)
    
    if style == 'detailed':
        readme_parts.append(structure_section)
    
    readme_parts.extend(advanced_sections)
    readme_parts.extend([contributing_section, license_section])
    
    english_readme = '\n'.join(readme_parts)
    
    result = {'en': english_readme}
    
    if bilingual:
        result['zh'] = generate_chinese_version(project_info, english_readme)
    
    return result


def main():
    parser = argparse.ArgumentParser(description='Generate professional README for GitHub projects')
    parser.add_argument('project_path', help='Path to the project directory')
    parser.add_argument('--style', '-s', choices=['minimal', 'professional', 'detailed'],
                        default='professional', help='README style')
    parser.add_argument('--no-banner', action='store_true', help='Skip banner generation')
    parser.add_argument('--no-diagrams', action='store_true', help='Skip diagram generation')
    parser.add_argument('--no-advanced', action='store_true', help='Skip advanced elements')
    parser.add_argument('--bilingual', '-b', action='store_true', help='Generate Chinese version')
    parser.add_argument('--repo-owner', help='GitHub repository owner for advanced features')
    parser.add_argument('--repo-name', help='GitHub repository name for advanced features')
    parser.add_argument('--output', '-o', default='README.md', help='Output file name')
    
    args = parser.parse_args()
    
    readmes = create_readme(
        args.project_path,
        style=args.style,
        include_banner=not args.no_banner,
        include_diagrams=not args.no_diagrams,
        include_advanced=not args.no_advanced,
        bilingual=args.bilingual,
        repo_owner=args.repo_owner,
        repo_name=args.repo_name
    )
    
    # 写入文件
    project_path = Path(args.project_path)
    
    en_path = project_path / args.output
    en_path.write_text(readmes['en'])
    print(f"Generated: {en_path}")
    
    if args.bilingual and 'zh' in readmes:
        zh_path = project_path / args.output.replace('.md', '.zh-CN.md')
        zh_path.write_text(readmes['zh'])
        print(f"Generated: {zh_path}")


if __name__ == '__main__':
    main()
