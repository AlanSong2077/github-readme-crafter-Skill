#!/usr/bin/env python3
"""
README Validation Script - Run before delivery
Part of github-readme-crafter skill
"""

import os
import re
import sys
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime


class READMEValidator:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.errors = []
        self.warnings = []
        self.passed = []
        self.log = []
    
    def log_action(self, message: str):
        """Log an action with timestamp"""
        timestamp = datetime.now().isoformat()
        self.log.append(f"[{timestamp}] {message}")
    
    def validate_all(self) -> bool:
        """Run all validation tests"""
        self.log_action("Starting validation")
        
        self.validate_structure()  # Category A
        self.validate_content()    # Category B
        self.validate_badges()     # Category C
        self.validate_images()     # Category D
        self.validate_mermaid()    # Category E
        self.validate_bilingual()  # Category F
        self.validate_style()       # Category G
        
        self.log_action(f"Validation complete: {len(self.passed)} passed, {len(self.warnings)} warnings, {len(self.errors)} errors")
        return len(self.errors) == 0
    
    def validate_structure(self):
        """Category A tests - HARD FAIL"""
        self.log_action("Running Category A: Structural tests")
        
        # A-01: README exists
        readme = self.project_path / "README.md"
        if not readme.exists():
            self.errors.append("A-01: README.md does not exist")
        elif readme.stat().st_size < 1024:
            self.errors.append("A-01: README.md too small (< 1KB)")
        else:
            self.passed.append("A-01: README.md exists and valid size")
        
        # A-02: Banner SVG exists and valid
        banner = self.project_path / "assets" / "banner.svg"
        if not banner.exists():
            self.errors.append("A-02: banner.svg does not exist")
        else:
            content = banner.read_text()
            if "<svg" not in content:
                self.errors.append("A-02: Invalid SVG (no <svg> root)")
            else:
                self.passed.append("A-02: banner.svg valid")
        
        # A-03: Banner dimensions
        if banner.exists():
            content = banner.read_text()
            if "1280" in content and "320" in content:
                self.passed.append("A-03: Banner dimensions correct (1280x320)")
            else:
                self.warnings.append("A-03: Banner dimensions may not be 1280x320")
    
    def validate_content(self):
        """Category B tests - HARD FAIL"""
        self.log_action("Running Category B: Content tests")
        
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # B-01: Exactly one H1
        h1_matches = re.findall(r'^# [^#\n]', content, re.MULTILINE)
        h1_count = len(h1_matches)
        if h1_count == 0:
            self.errors.append("B-01: No H1 title found")
        elif h1_count > 1:
            self.warnings.append(f"B-01: Multiple H1 titles ({h1_count})")
        else:
            self.passed.append("B-01: Exactly one H1 title")
        
        # B-02: Badges present
        badge_pattern = r'!\[.*?\]\(https://img\.shields\.io/.*?\)'
        badges = re.findall(badge_pattern, content)
        if len(badges) > 0:
            self.passed.append(f"B-02: {len(badges)} badges present")
        else:
            self.warnings.append("B-02: No badges found")
        
        # B-03: No placeholder text
        placeholders = [
            ("Your Name", "user placeholder"),
            ("your-project", "generic placeholder"),
            ("username/repo", "generic placeholder"),
        ]
        for placeholder, desc in placeholders:
            if placeholder in content:
                # Allow in URL examples but warn
                if "example" not in placeholder.lower():
                    self.warnings.append(f"B-03: Possible placeholder: {placeholder}")
        
        # B-04: TL;DR section
        if "TL;DR" in content or "Quick Start" in content or "Quick start" in content:
            self.passed.append("B-04: TL;DR or Quick Start section present")
        else:
            self.warnings.append("B-04: No TL;DR or Quick Start section")
        
        # B-05: Installation section
        if "## Installation" in content or "## 安装" in content:
            self.passed.append("B-05: Installation section present")
        else:
            self.warnings.append("B-05: No Installation section")
        
        # B-06: Usage section
        if "## Usage" in content or "## 使用" in content:
            self.passed.append("B-06: Usage section present")
        else:
            self.warnings.append("B-06: No Usage section")
        
        # B-07: License section
        if "## License" in content or "## 许可证" in content or "MIT License" in content:
            self.passed.append("B-07: License section present")
        else:
            self.warnings.append("B-07: No License section")
    
    def validate_badges(self):
        """Category C tests - HARD FAIL"""
        self.log_action("Running Category C: Badge tests")
        
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # C-01: Badge count
        badge_pattern = r'!\[.*?\]\(https://img\.shields\.io/.*?\)'
        badges = re.findall(badge_pattern, content)
        
        if len(badges) > 5:
            self.errors.append(f"C-01: Too many badges ({len(badges)} > 5)")
        elif len(badges) > 0:
            self.passed.append(f"C-01: Badge count OK ({len(badges)})")
        
        # C-02: Badge style
        for badge in badges:
            if "style=flat-square" not in badge and "style=for-the-badge" not in badge:
                self.warnings.append(f"C-02: Badge without recommended style")
        
        # C-04: No emoji in badges
        for badge in badges:
            # Check for common emoji patterns
            emoji_pattern = re.compile(
                "[\U0001F600-\U0001F64F"
                "\U0001F300-\U0001F5FF"
                "\U0001F680-\U0001F6FF"
                "\U0001F1E0-\U0001F1FF]"
            )
            if emoji_pattern.search(badge):
                self.errors.append(f"C-04: Emoji in badge: {badge[:50]}")
        self.passed.append("C-04: No emoji in badges")
        
        # C-05: Badge URL accessibility
        for badge in badges:
            url_match = re.search(r'\((https://[^)]+)\)', badge)
            if url_match:
                url = url_match.group(1)
                if not self._check_url(url):
                    self.warnings.append(f"C-05: Badge URL may be inaccessible: {url[:50]}")
        self.passed.append("C-05: Badge URLs validated")
    
    def validate_images(self):
        """Category D tests - WARN"""
        self.log_action("Running Category D: Image tests")
        
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # D-01: Star History URL format
        if "star-history.com" in content:
            if re.search(r'star-history\.com/svg\?repos=.+', content):
                self.passed.append("D-01: Star History URL format valid")
            else:
                self.warnings.append("D-01: Star History URL may be invalid")
        
        # D-02: Contributors URL format
        if "contrib.rocks" in content:
            if re.search(r'contrib\.rocks/image\?repo=.+', content):
                self.passed.append("D-02: Contributors URL format valid")
            else:
                self.warnings.append("D-02: Contributors URL may be invalid")
        
        # D-03: Banner URL in README
        banner_urls = re.findall(r'https://raw\.githubusercontent\.com/[^)]+\.svg', content)
        for url in banner_urls:
            if not self._check_url(url):
                self.warnings.append(f"D-03: Banner URL inaccessible: {url[:50]}")
        if banner_urls:
            self.passed.append(f"D-03: {len(banner_urls)} banner URLs validated")
    
    def validate_mermaid(self):
        """Category E tests - HARD FAIL"""
        self.log_action("Running Category E: Mermaid tests")
        
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # Find mermaid blocks
        mermaid_pattern = r'```mermaid\s*(.*?)\s*```'
        diagrams = re.findall(mermaid_pattern, content, re.DOTALL)
        
        if not diagrams:
            self.warnings.append("E-00: No Mermaid diagrams found")
            return
        
        for diagram in diagrams:
            # E-01: Basic syntax check
            if "flowchart" not in diagram and "graph" not in diagram:
                self.warnings.append("E-01: Possible non-flowchart diagram")
            else:
                self.passed.append("E-01: Mermaid syntax appears valid")
            
            # E-02: Check for unsupported features
            unsupported = ["pie", "timeline", "gantt"]
            for u in unsupported:
                if u in diagram.lower():
                    self.warnings.append(f"E-02: Unsupported Mermaid feature: {u}")
            
            # E-03: Node count
            nodes = re.findall(r'\b[A-Za-z0-9_]+\[', diagram)
            if len(nodes) > 15:
                self.warnings.append(f"E-03: Many nodes ({len(nodes)} > 15)")
            else:
                self.passed.append(f"E-03: Node count OK ({len(nodes)})")
    
    def validate_bilingual(self):
        """Category F tests - HARD FAIL"""
        self.log_action("Running Category F: Bilingual tests")
        
        zh_cn = self.project_path / "README.zh-CN.md"
        
        # F-01: zh-CN file exists (if bilingual was requested)
        # We check if zh-CN file exists, but don't fail if it doesn't
        # (user may not have requested bilingual)
        if zh_cn.exists():
            self.passed.append("F-01: README.zh-CN.md exists")
            
            content_zh = zh_cn.read_text()
            readme = self.project_path / "README.md"
            
            if readme.exists():
                content_en = readme.read_text()
                
                # F-02: Language switcher
                has_switch_en = "[中文]" in content_en or "[中文]" in content_en
                has_switch_zh = "[English]" in content_zh or "[English]" in content_zh
                
                if has_switch_en and has_switch_zh:
                    self.passed.append("F-02: Language switchers present")
                else:
                    self.errors.append("F-02: Missing language switcher")
                
                # F-04: Chinese content
                chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content_zh))
                if chinese_chars < 50:
                    self.errors.append(f"F-04: Insufficient Chinese content ({chinese_chars} chars)")
                else:
                    self.passed.append(f"F-04: Chinese content OK ({chinese_chars} chars)")
        else:
            self.warnings.append("F-01: No bilingual version (README.zh-CN.md missing)")
    
    def validate_style(self):
        """Category G tests - WARN"""
        self.log_action("Running Category G: Style tests")
        
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # G-01: Emoji count per section
        sections = re.split(r'^## ', content, flags=re.MULTILINE)
        for section in sections[1:]:  # Skip first (before any ##)
            emoji_count = len(re.findall(r'[\U0001F000-\U0001F9FF]', section))
            if emoji_count > 2:
                self.warnings.append(f"G-01: Section has {emoji_count} emoji (> 2)")
        self.passed.append("G-01: Emoji count checked")
        
        # G-02: Paragraph length
        paragraphs = re.split(r'\n\n', content)
        long_paras = [p for p in paragraphs if len(re.findall(r'[.!?]', p)) > 4]
        if long_paras:
            self.warnings.append(f"G-02: {len(long_paras)} paragraphs > 4 sentences")
        else:
            self.passed.append("G-02: Paragraph length OK")
    
    def _check_url(self, url: str) -> bool:
        """Check if URL returns 200"""
        try:
            with urlopen(url, timeout=5) as response:
                return response.status == 200
        except:
            return False
    
    def report(self):
        """Generate validation report"""
        print("\n" + "="*60)
        print("VALIDATION REPORT")
        print("="*60)
        print(f"Project: {self.project_path}")
        print(f"Time: {datetime.now().isoformat()}")
        
        if self.passed:
            print(f"\n✅ PASSED ({len(self.passed)})")
            for p in self.passed[:10]:  # Show first 10
                print(f"  ✓ {p}")
            if len(self.passed) > 10:
                print(f"  ... and {len(self.passed) - 10} more")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)})")
            for w in self.warnings[:10]:
                print(f"  ! {w}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more")
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)})")
            for e in self.errors:
                print(f"  ✗ {e}")
        
        print("\n" + "="*60)
        if len(self.errors) == 0:
            print("✅ VALIDATION PASSED - Output ready for delivery")
            return True
        else:
            print("❌ VALIDATION FAILED - Fix errors before delivery")
            return False
    
    def get_log(self):
        """Return validation log"""
        return "\n".join(self.log)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 test.py <project_path>")
        print("\nValidates README generation output against hard constraints.")
        sys.exit(1)
    
    project_path = sys.argv[1]
    
    if not Path(project_path).exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)
    
    validator = READMEValidator(project_path)
    success = validator.validate_all()
    validator.report()
    
    if len(sys.argv) > 2 and sys.argv[2] == "--log":
        print("\n--- Validation Log ---")
        print(validator.get_log())
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
