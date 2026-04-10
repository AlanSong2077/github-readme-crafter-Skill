# test.md — GitHub README Crafter Validation Tests

> **Strong Validation**: This document defines hard validation rules. ALL tests must pass. There is NO "minimal" mode — every README must be premium.

---

## Core Principle

**Every README must be visually premium and attention-grabbing.** There is no minimal or simple mode. Every output includes banner, TL;DR, diagrams, and advanced elements.

---

## Test Categories

### Category A: Structural Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| A-01 | README.md exists | File exists, size > 2KB | REJECT |
| A-02 | Banner SVG exists | File exists, valid XML, `<svg>` root | REJECT |
| A-03 | Banner dimensions | Width 1280, Height 320 (±10px) | REJECT |
| A-04 | Light banner exists | File exists, valid XML | REJECT |
| A-05 | zh-CN exists | File exists, size > 2KB | REJECT |

### Category B: Content Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| B-01 | H1 Title present | Exactly one H1 | REJECT |
| B-02 | Badges present | 1-5 badges, flat-square | REJECT if > 5 |
| B-03 | No placeholder text | No "Your Name", generic placeholders | REJECT |
| B-04 | TL;DR section | REQUIRED - all READMEs must have quick start | REJECT |
| B-05 | Installation section | Present with code block | REJECT |
| B-06 | Usage section | Present with code example | REJECT |
| B-07 | License section | Present | REJECT |

### Category C: Badge Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| C-01 | Badge count | ≤ 5 badges | REJECT |
| C-02 | Badge style | `flat-square` | REJECT |
| C-03 | Badge URL format | shields.io format valid | REJECT |
| C-04 | No emoji in badges | No unicode emoji in badge text | REJECT |
| C-05 | Badge URL accessible | HTTP 200 for all | REJECT |

### Category D: Image Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| D-01 | Star History URL | Valid star-history.com format | REJECT |
| D-02 | Contributors URL | Valid contrib.rocks format | REJECT |
| D-03 | Banner URL | Valid raw.githubusercontent.com URL | REJECT |
| D-04 | Image accessible | HTTP 200 for all images | REJECT |

### Category E: Mermaid Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| E-01 | Mermaid syntax | Valid GitHub-compatible syntax | REJECT |
| E-02 | No unsupported | No pie, timeline, gantt | REJECT |
| E-03 | Node count | ≤ 15 nodes per diagram | WARN |
| E-04 | Min 1 diagram | At least tech stack diagram | REJECT |

### Category F: Bilingual Tests (HARD FAIL)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| F-01 | zh-CN file exists | File exists, size > 2KB | REJECT |
| F-02 | Language switcher | Present in both files | REJECT |
| F-03 | Section parity | Same sections in both languages | WARN |
| F-04 | Chinese content | Chinese characters present | REJECT |

### Category G: Style Tests (WARN)

| Test ID | Description | Expected | Fail Action |
|---------|-------------|----------|-------------|
| G-01 | Emoji count | ≤ 2 per section | WARN |
| G-02 | Paragraph length | ≤ 4 sentences | WARN |
| G-03 | Code language | Specified for syntax highlighting | WARN |

---

## Style Tiers

| Style | Description | Requirements |
|-------|-------------|---------------|
| `standard` | Premium minimum | All required sections |
| `professional` | Extended depth | Standard + sponsors, architecture, channels |

**Both tiers are premium. There is NO minimal mode.**

---

## Pass Criteria

| Level | Errors | Warnings | Result |
|-------|--------|----------|--------|
| **PASS** | 0 | Any | Ready for delivery |
| **FAIL** | ≥ 1 | - | Fix before delivery |

---

**END OF test.md**
