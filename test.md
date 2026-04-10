# test.md — GitHub README Crafter Validation Tests

> **Strong Validation**: This document defines hard validation rules. Output MUST pass ALL tests before delivery.

---

## Test Categories

### Category A: Structural Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| A-01 | README.md exists | File exists, size > 1024 bytes | REJECT |
| A-02 | Banner SVG exists | File exists, valid XML, `<svg>` root | REJECT |
| A-03 | Banner dimensions | Width 1280, Height 320 (±10px) | REJECT |
| A-04 | Light banner exists (if bilingual) | File exists, valid XML | REJECT |
| A-05 | Directory structure | All required dirs present | REJECT |

### Category B: Content Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| B-01 | H1 Title present | Exactly one H1 (# Title) | REJECT |
| B-02 | Badges present | 1-5 badges | REJECT if > 5 |
| B-03 | No placeholder text | No "Your Name", "example.com" in user content | REJECT |
| B-04 | TL;DR section | Present for standard/professional | WARN (allow) |
| B-05 | Installation section | Present with code block | WARN (allow) |
| B-06 | Usage section | Present with code example | WARN (allow) |
| B-07 | License section | Present | WARN (allow) |

### Category C: Badge Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| C-01 | Badge count | ≤ 5 badges | REJECT |
| C-02 | Badge style | `flat-square` or `for-the-badge` | REJECT |
| C-03 | Badge URL format | shields.io format valid | REJECT |
| C-04 | No emoji in badges | No unicode emoji in badge text | REJECT |
| C-05 | Badge URL accessibility | HTTP 200 for all badge URLs | REJECT |

### Category D: Image Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| D-01 | Star History URL | Valid star-history.com format | WARN |
| D-02 | Contributors URL | Valid contrib.rocks format | WARN |
| D-03 | Banner URL (in README) | Valid raw.githubusercontent.com URL | REJECT |
| D-04 | Image accessibility | HTTP 200 for all images | WARN |

### Category E: Mermaid Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| E-01 | Mermaid syntax | Valid GitHub-compatible syntax | REJECT |
| E-02 | No unsupported features | No pie charts, timeline, etc. | REJECT |
| E-03 | Node count | ≤ 15 nodes per diagram | WARN |
| E-04 | Subgraph usage | Meaningful subgraph grouping | WARN |

### Category F: Bilingual Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| F-01 | zh-CN file exists | If bilingual=true, file exists | REJECT |
| F-02 | Language switcher | Present in both files | REJECT |
| F-03 | Section parity | Same sections in both languages | WARN |
| F-04 | zh-CN content | Chinese characters present | REJECT if empty |

### Category G: Style Tests (WARN)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| G-01 | Emoji count | ≤ 2 per section | WARN |
| G-02 | Paragraph length | ≤ 4 sentences | WARN |
| G-03 | Code block language | Specified for syntax highlighting | WARN |
| G-04 | Consistent terminology | Same terms used throughout | WARN |

---

## Validation Script

### Python Validation Script
```python
#!/usr/bin/env python3
"""README Validation Script - Run before delivery"""

import os
import re
import sys
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

class READMEValidator:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.errors = []
        self.warnings = []
        self.passed = []
    
    def validate_all(self) -> bool:
        """Run all validation tests"""
        self.validate_structure()
        self.validate_content()
        self.validate_badges()
        self.validate_images()
        self.validate_mermaid()
        self.validate_bilingual()
        return len(self.errors) == 0
    
    def validate_structure(self):
        """Category A tests"""
        # A-01: README exists
        readme = self.project_path / "README.md"
        if not readme.exists():
            self.errors.append("A-01: README.md does not exist")
        elif readme.stat().st_size < 1024:
            self.errors.append("A-01: README.md too small (< 1KB)")
        else:
            self.passed.append("A-01")
        
        # A-02, A-03: Banner validation
        banner = self.project_path / "assets" / "banner.svg"
        if not banner.exists():
            self.errors.append("A-02: banner.svg does not exist")
        else:
            content = banner.read_text()
            if "<svg" not in content:
                self.errors.append("A-02: Invalid SVG (no <svg> root)")
            elif "1280" not in content or "320" not in content:
                self.warnings.append("A-03: Banner dimensions may not be 1280x320")
            else:
                self.passed.append("A-02, A-03")
    
    def validate_badges(self):
        """Category C tests"""
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # Count badges
        badge_pattern = r'!\[.*?\]\(https://img\.shields\.io/.*?\)'
        badges = re.findall(badge_pattern, content)
        
        if len(badges) > 5:
            self.errors.append(f"C-01: Too many badges ({len(badges)} > 5)")
        elif len(badges) > 0:
            self.passed.append(f"C-01: {len(badges)} badges")
        
        # Check style
        for badge in badges:
            if "style=flat-square" not in badge and "style=for-the-badge" not in badge:
                self.warnings.append(f"C-02: Badge without recommended style: {badge[:50]}")
            if any(ord(c) > 127 and c not in "中文简体繁体日本語한국어" for c in badge):
                self.errors.append(f"C-04: Emoji/problematic char in badge: {badge[:50]}")
        
        # Validate URLs
        for badge in badges:
            url_match = re.search(r'\((https://.*?)\)', badge)
            if url_match:
                url = url_match.group(1)
                if not self._check_url(url):
                    self.errors.append(f"C-05: Badge URL failed: {url[:50]}")
    
    def validate_content(self):
        """Category B tests"""
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # B-01: Exactly one H1
        h1_count = len(re.findall(r'^# [^#]', content, re.MULTILINE))
        if h1_count == 0:
            self.errors.append("B-01: No H1 title found")
        elif h1_count > 1:
            self.warnings.append(f"B-01: Multiple H1 titles ({h1_count})")
        else:
            self.passed.append("B-01")
        
        # B-03: No placeholder text
        placeholders = ["Your Name", "example.com", "your-", "Your "]
        for p in placeholders:
            if p in content and "example.com" not in content:
                self.warnings.append(f"B-03: Possible placeholder: {p}")
        
        # B-04: TL;DR section
        if "TL;DR" in content or "Quick Start" in content:
            self.passed.append("B-04")
        else:
            self.warnings.append("B-04: No TL;DR or Quick Start section")
    
    def validate_mermaid(self):
        """Category E tests"""
        readme = self.project_path / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        
        # Find mermaid blocks
        mermaid_pattern = r'```mermaid\s*(.*?)\s*```'
        diagrams = re.findall(mermaid_pattern, content, re.DOTALL)
        
        for diagram in diagrams:
            # E-01: Basic syntax check
            if "flowchart" not in diagram and "graph" not in diagram:
                self.warnings.append("E-01: Possible non-flowchart diagram")
            
            # E-02: Check for unsupported features
            unsupported = ["pie", "timeline", "gantt"]
            for u in unsupported:
                if u in diagram.lower():
                    self.warnings.append(f"E-02: Unsupported Mermaid feature: {u}")
            
            # E-03: Node count
            nodes = re.findall(r'\b[A-Za-z0-9_]+\[', diagram)
            if len(nodes) > 15:
                self.warnings.append(f"E-03: Many nodes ({len(nodes)} > 15)")
            
            self.passed.append("E-01 to E-04")
    
    def validate_bilingual(self):
        """Category F tests"""
        zh_cn = self.project_path / "README.zh-CN.md"
        
        if zh_cn.exists():
            content_zh = zh_cn.read_text()
            content_en = (self.project_path / "README.md").read_text()
            
            # F-01: File exists
            self.passed.append("F-01")
            
            # F-02: Language switcher
            if "[English]" in content_zh and "[中文]" in content_en:
                self.passed.append("F-02")
            else:
                self.errors.append("F-02: Missing language switcher")
            
            # F-04: Chinese content
            chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content_zh))
            if chinese_chars < 50:
                self.errors.append("F-04: Insufficient Chinese content")
            else:
                self.passed.append(f"F-04: {chinese_chars} Chinese characters")
    
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
        
        if self.passed:
            print(f"\n✅ PASSED ({len(self.passed)})")
            for p in self.passed:
                print(f"  ✓ {p}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)})")
            for w in self.warnings:
                print(f"  ! {w}")
        
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 test.py /path/to/project")
        sys.exit(1)
    
    validator = READMEValidator(sys.argv[1])
    success = validator.validate_all()
    validator.report()
    sys.exit(0 if success else 1)
```

---

## Test Execution

### Run All Tests
```bash
python3 test.py /path/to/project
```

### Run Specific Category
```bash
python3 -c "
from test import READMEValidator
v = READMEValidator('/path/to/project')
v.validate_badges()
v.report()
"
```

---

## Pass Criteria

| Level | Requirements |
|-------|-------------|
| **PASS** | 0 errors, all hard constraints met |
| **WARN** | 0 errors, ≤ 5 warnings |
| **FAIL** | ≥ 1 error |

---

**END OF test.md**
