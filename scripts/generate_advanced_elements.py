#!/usr/bin/env python3
"""
高级README元素生成器 - 社交图标、统计图表、贡献者信息等 (2026 更新版)
"""
import argparse
from typing import List, Dict, Optional


class AdvancedElementsGenerator:
    """生成顶级开源项目常见的高级README元素"""
    
    @staticmethod
    def social_badges(discord_url: Optional[str] = None,
                      twitter_handle: Optional[str] = None,
                      linkedin_url: Optional[str] = None,
                      website_url: Optional[str] = None) -> str:
        """
        生成社交链接徽章 (2026 for-the-badge 风格)
        参考：OpenClaw, Vercel Next.js 等顶级项目
        """
        badges = []
        
        if discord_url:
            badges.append(f"[![Discord](https://img.shields.io/discord/123456789?label=Discord&logo=discord&logoColor=white&color=5865F2&style=for-the-badge)]({discord_url})")
        if twitter_handle:
            badges.append(f"[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white&style=for-the-badge)](https://twitter.com/{twitter_handle})")
        if linkedin_url:
            badges.append(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white&style=for-the-badge)]({linkedin_url})")
        if website_url:
            badges.append(f"[![Website](https://img.shields.io/badge/Website-4285F4?logo=google-chrome&logoColor=white&style=for-the-badge)]({website_url})")
        
        return " ".join(badges) if badges else ""
    
    @staticmethod
    def star_history_chart(repo_owner: str, repo_name: str) -> str:
        """
        生成Star历史图表链接
        参考：https://star-history.com 被广泛用于展示项目增长趋势
        """
        return f"""## Star History

[![Star History Chart](https://api.star-history.com/svg?repos={repo_owner}/{repo_name}&type=Date)](https://www.star-history.com/#{repo_owner}/{repo_name}&type=Date)

"""
    
    @staticmethod
    def contributors_section(repo_owner: str, repo_name: str) -> str:
        """
        生成贡献者图表
        参考：使用contrib.rocks展示项目贡献者
        """
        return f"""## Contributors

Thanks to all the contributors who have helped make this project better!

<a href="https://github.com/{repo_owner}/{repo_name}/graphs/contributors">
  <img src="https://contrib.rocks/image?repo={repo_owner}/{repo_name}" />
</a>

"""
    
    @staticmethod
    def visitors_badge(repo_owner: str, repo_name: str) -> str:
        """
        生成访问者统计徽章
        注意：这是可选功能，部分用户可能不喜欢
        """
        return f"![Visitors](https://visitor-badge.laobi.icu/badge?page_id={repo_owner}.{repo_name})"
    
    @staticmethod
    def support_section(buy_me_a_coffee: Optional[str] = None,
                       github_sponsors: Optional[str] = None,
                       patreon: Optional[str] = None) -> str:
        """
        生成支持/赞助部分
        参考：许多开源项目在README底部添加赞助链接
        """
        lines = ["## Support", ""]
        
        if buy_me_a_coffee:
            lines.append(f"[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?logo=buy-me-a-coffee&logoColor=black)]({buy_me_a_coffee})")
        if github_sponsors:
            lines.append(f"[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-EA4AAA?logo=github-sponsors&logoColor=white)]({github_sponsors})")
        if patreon:
            lines.append(f"[![Patreon](https://img.shields.io/badge/Patreon-F96854?logo=patreon&logoColor=white)]({patreon})")
        
        lines.append("")
        lines.append("If you find this project helpful, please consider supporting its development!")
        lines.append("")
        
        return '\n'.join(lines) if any([buy_me_a_coffee, github_sponsors, patreon]) else ""
    
    @staticmethod
    def acknowledgments_section(projects: List[Dict[str, str]]) -> str:
        """
        生成致谢部分
        示例：[{"name": "React", "url": "https://react.dev", "description": "UI library"}]
        """
        lines = ["## Acknowledgments", ""]
        lines.append("This project stands on the shoulders of giants. Special thanks to:")
        lines.append("")
        
        for proj in projects:
            name = proj.get('name', '')
            url = proj.get('url', '')
            desc = proj.get('description', '')
            lines.append(f"- [{name}]({url}) - {desc}")
        
        lines.append("")
        return '\n'.join(lines)
    
    @staticmethod
    def changelog_section(releases_url: str) -> str:
        """
        生成变更日志链接部分
        """
        return f"""## Changelog

See [CHANGELOG.md]({releases_url}) or [Releases]({releases_url}) for a detailed history of changes.

"""
    
    @staticmethod
    def security_section(security_file: str = "SECURITY.md") -> str:
        """
        生成安全政策链接
        参考：大型项目通常有专门的安全政策
        """
        return f"""## Security

If you discover any security-related issues, please email security@example.com instead of using the issue tracker. See [{security_file}]({security_file}) for more details.

"""
    
    @staticmethod
    def code_of_conduct_link(coc_file: str = "CODE_OF_CONDUCT.md") -> str:
        """
        生成行为准则链接
        """
        return f"Please read our [Code of Conduct]({coc_file}) before contributing.\n\n"
    
    @staticmethod
    def license_section(license_type: str = "MIT", license_file: str = "LICENSE") -> str:
        """
        生成更详细的许可证部分
        """
        year = "2026"  # Updated for 2026
        return f"""## License

This project is licensed under the {license_type} License - see the [{license_file}]({license_file}) file for details.

Copyright (c) {year} [Your Name or Organization]

"""
    
    @staticmethod
    def generate_toc(sections: List[str]) -> str:
        """
        生成目录，带锚点链接
        """
        lines = ["## Table of Contents", ""]
        
        for section in sections:
            # 将标题转换为锚点格式
            anchor = section.lower().replace(' ', '-').replace('.', '')
            lines.append(f"- [{section}](#{anchor})")
        
        lines.append("")
        return '\n'.join(lines)
    
    @staticmethod
    def demo_section(demo_url: str, screenshot_url: Optional[str] = None) -> str:
        """
        生成演示/截图部分
        参考：许多前端项目在README中展示实际效果
        """
        lines = ["## Demo", ""]
        lines.append(f"**Live Demo:** [{demo_url}]({demo_url})")
        lines.append("")
        
        if screenshot_url:
            lines.append(f"![Screenshot]({screenshot_url})")
            lines.append("")
        
        return '\n'.join(lines)
    
    @staticmethod
    def roadmap_section(items: List[Dict]) -> str:
        """
        生成路线图部分
        
        items: [{"title": "Feature A", "status": "done|in-progress|planned", "description": "..."}]
        """
        lines = ["## Roadmap", ""]
        
        status_icons = {
            'done': '[x]',
            'in-progress': '[~]',
            'planned': '[ ]'
        }
        
        for item in items:
            status = item.get('status', 'planned')
            title = item.get('title', '')
            desc = item.get('description', '')
            icon = status_icons.get(status, '[ ]')
            
            lines.append(f"- {icon} **{title}** - {desc}")
        
        lines.append("")
        return '\n'.join(lines)
    
    @staticmethod
    def sponsors_section(sponsors: List[Dict[str, str]] = None, style: str = "table") -> str:
        """
        生成赞助商展示区 (2026 新功能)
        参考：OpenClaw, sindresorhus/awesome 等项目
        
        sponsors: [{"name": "SponsorName", "url": "https://sponsor.com", "logo": "logo.svg", "description": "Description"}]
        style: "table" (multiple sponsors) or "badge" (few sponsors)
        """
        if not sponsors:
            sponsors = []
        
        if not sponsors:
            return ""
        
        lines = ["## Sponsors", ""]
        
        if style == "table":
            lines.append("<table>")
            lines.append("  <tr>")
            for i, sponsor in enumerate(sponsors):
                if i > 0 and i % 5 == 0:  # 5 columns
                    lines.append("  </tr>")
                    lines.append("  <tr>")
                name = sponsor.get('name', '')
                url = sponsor.get('url', '#')
                logo = sponsor.get('logo', '')
                height = sponsor.get('height', '30')
                lines.append(f'    <td align="center" width="20%">')
                lines.append(f'      <a href="{url}">')
                lines.append(f'        <picture>')
                lines.append(f'          <source media="(prefers-color-scheme: light)" srcset="{logo.replace(".svg", "-light.svg") if logo.endswith(".svg") else logo}">')
                lines.append(f'          <img src="{logo}" alt="{name}" height="{height}">')
                lines.append(f'        </picture>')
                lines.append(f'      </a>')
                lines.append(f'    </td>')
            lines.append("  </tr>")
            lines.append("</table>")
        else:
            # Badge style
            for sponsor in sponsors:
                name = sponsor.get('name', '')
                url = sponsor.get('url', '#')
                color = sponsor.get('color', '181717')
                logo = sponsor.get('logo', 'github')
                lines.append(f"[![{name}](https://img.shields.io/badge/Sponsor-{name.replace(' ', '%20')}-{color}?logo={logo}&style=for-the-badge)]({url})")
        
        lines.append("")
        return '\n'.join(lines)
    
    @staticmethod
    def share_buttons(repo_url: str, title: Optional[str] = None) -> str:
        """
        生成社交分享按钮 (2026 新功能)
        参考：kamranahmedse/developer-roadmap 项目
        """
        title_encoded = title.replace(' ', '%20') if title else 'Check%20out%20this%20project'
        
        return f"""## Share

[![Share on Reddit](https://img.shields.io/badge/share%20on-reddit-red?logo=reddit&style=for-the-badge)](https://reddit.com/submit?url={repo_url}&title={title_encoded})
[![Share on Hacker News](https://img.shields.io/badge/share%20on-hacker%20news-orange?logo=ycombinator&style=for-the-badge)](https://news.ycombinator.com/submitlink?u={repo_url})
[![Share on Twitter](https://img.shields.io/badge/share%20on-twitter-03A9F4?logo=twitter&style=for-the-badge)](https://twitter.com/share?url={repo_url}&text={title_encoded})
[![Share on LinkedIn](https://img.shields.io/badge/share%20on-linkedin-3949AB?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/shareArticle?mini=true&url={repo_url}&title={title_encoded})

"""
    
    @staticmethod
    def development_channels() -> str:
        """
        生成开发频道说明 (2026 新功能)
        参考：OpenClaw 项目
        """
        return """## Development Channels

- **stable**: Tagged releases (`v1.0.0`), npm dist-tag `latest`
- **beta**: Pre-release tags (`v1.0.0-beta.1`), npm dist-tag `beta`
- **dev**: Latest development version, npm dist-tag `dev`

Switch channels: `npm install project@stable|beta|dev`

"""
    
    @staticmethod
    def dark_light_mode_banner(project_name: str, banner_light: str = "./assets/banner-light.svg", 
                               banner_dark: str = "./assets/banner.svg") -> str:
        """
        生成支持暗色/亮色模式切换的 Banner (2026 新功能)
        参考：OpenClaw, sindresorhus/awesome 项目
        """
        return f"""<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="{banner_light}">
    <img src="{banner_dark}" alt="{project_name}" width="100%">
  </picture>
</p>

"""


def main():
    parser = argparse.ArgumentParser(description='Generate advanced README elements (2026 Updated)')
    parser.add_argument('type', choices=['social', 'star-history', 'contributors', 
                                         'support', 'roadmap', 'toc', 'sponsors', 
                                         'share', 'development', 'banner-dl'],
                        help='Type of element to generate')
    parser.add_argument('--repo-owner', help='GitHub repository owner')
    parser.add_argument('--repo-name', help='GitHub repository name')
    parser.add_argument('--repo-url', help='GitHub repository URL (for share buttons)')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    gen = AdvancedElementsGenerator()
    result = ""
    
    if args.type == 'social':
        result = gen.social_badges(
            discord_url="https://discord.gg/example",
            twitter_handle="example"
        )
    elif args.type == 'star-history':
        if not args.repo_owner or not args.repo_name:
            print("Error: --repo-owner and --repo-name required for star-history")
            return
        result = gen.star_history_chart(args.repo_owner, args.repo_name)
    elif args.type == 'contributors':
        if not args.repo_owner or not args.repo_name:
            print("Error: --repo-owner and --repo-name required for contributors")
            return
        result = gen.contributors_section(args.repo_owner, args.repo_name)
    elif args.type == 'roadmap':
        items = [
            {"title": "Core Features", "status": "done", "description": "Basic functionality"},
            {"title": "Advanced API", "status": "in-progress", "description": "Extended capabilities"},
            {"title": "Mobile Support", "status": "planned", "description": "iOS and Android apps"},
        ]
        result = gen.roadmap_section(items)
    elif args.type == 'toc':
        sections = ["Features", "Installation", "Usage", "API Reference", "Contributing", "License"]
        result = gen.generate_toc(sections)
    elif args.type == 'sponsors':
        sponsors = [
            {"name": "Sponsor1", "url": "https://sponsor1.com", "logo": "./sponsor1.svg", "height": "30"},
            {"name": "Sponsor2", "url": "https://sponsor2.com", "logo": "./sponsor2.svg", "height": "30"},
        ]
        result = gen.sponsors_section(sponsors)
    elif args.type == 'share':
        if not args.repo_url:
            print("Error: --repo-url required for share buttons")
            return
        result = gen.share_buttons(args.repo_url, "My Awesome Project")
    elif args.type == 'development':
        result = gen.development_channels()
    elif args.type == 'banner-dl':
        result = gen.dark_light_mode_banner("ProjectName")
    
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(result)
        print(f"Generated: {args.output}")
    else:
        print(result)


if __name__ == '__main__':
    main()
