# GitHub README Crafter - Skill

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AlanSong2077/github-readme-crafter-Skill/main/assets/banner-light.svg">
    <img src="https://raw.githubusercontent.com/AlanSong2077/github-readme-crafter-Skill/main/assets/banner.svg" alt="GitHub README Crafter" width="100%">
  </picture>
</p>

<p align="center">
  <strong>AI-powered skill for generating professional GitHub README documents</strong>
</p>

<p align="center">
  [![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
</p>

## Overview

An OpenClaw skill that generates professional README documents matching the quality of top-tier open-source projects like Microsoft Terminal, Vercel Next.js, OpenClaw, and Facebook React.

## Features

- **Project Analysis** — Automatically detects language, framework, and structure
- **Dynamic Banner Generation** — Creates SVG banners with gradient backgrounds
- **Architecture Diagrams** — Generates Mermaid diagrams
- **Bilingual Support** — English and Chinese versions
- **2026 Best Practices** — Dark/Light mode, for-the-badge badges, Star History, Share buttons

## Usage

```bash
# Generate README with banner and diagrams
python3 scripts/create_readme.py /path/to/project

# Bilingual output
python3 scripts/create_readme.py /path/to/project --bilingual --style professional
```

## Project Structure

```
├── SKILL.md                    # OpenClaw skill documentation
├── scripts/
│   ├── create_readme.py        # Main generator
│   ├── analyze_project.py      # Project analyzer
│   ├── generate_banner.py      # SVG banner generator
│   ├── generate_mermaid.py     # Mermaid diagram generator
│   └── generate_advanced_elements.py  # Advanced elements
└── references/
    ├── templates.md            # README templates
    ├── top_projects_analysis.md # GitHub project analysis
    └── mermaid_examples.md     # Diagram examples
```

## Installation

Copy this skill to your OpenClaw skills directory or use with the github-readme-crafter project.

## License

MIT License
