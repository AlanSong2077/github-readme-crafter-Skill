#!/usr/bin/env python3
"""
项目结构分析器 - 提取项目元数据用于README生成
"""
import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional

# 语言到文件扩展名的映射
LANGUAGE_EXTENSIONS = {
    'Python': ['.py'],
    'JavaScript': ['.js', '.jsx', '.mjs'],
    'TypeScript': ['.ts', '.tsx'],
    'Java': ['.java'],
    'Go': ['.go'],
    'Rust': ['.rs'],
    'C++': ['.cpp', '.cc', '.cxx', '.hpp'],
    'C': ['.c', '.h'],
    'Ruby': ['.rb'],
    'PHP': ['.php'],
    'Swift': ['.swift'],
    'Kotlin': ['.kt', '.kts'],
}

# 包管理文件到语言的映射
PACKAGE_FILES = {
    'package.json': 'JavaScript/TypeScript',
    'requirements.txt': 'Python',
    'setup.py': 'Python',
    'pyproject.toml': 'Python',
    'Cargo.toml': 'Rust',
    'go.mod': 'Go',
    'pom.xml': 'Java',
    'build.gradle': 'Java/Kotlin',
    'Gemfile': 'Ruby',
    'composer.json': 'PHP',
    'Package.swift': 'Swift',
}


def detect_language(project_path: str) -> str:
    """检测项目主要语言"""
    path = Path(project_path)
    
    # 优先级：Python项目优先检查requirements.txt/pyproject.toml
    priority_files = ['requirements.txt', 'pyproject.toml', 'setup.py', 'Cargo.toml', 'go.mod']
    for pkg_file in priority_files:
        if (path / pkg_file).exists():
            return PACKAGE_FILES.get(pkg_file, 'Unknown')
    
    # 其他包管理文件
    for pkg_file, lang in PACKAGE_FILES.items():
        if pkg_file in priority_files:
            continue
        if (path / pkg_file).exists():
            return lang
    
    # 基于文件扩展名统计
    ext_counts = {}
    for ext_list in LANGUAGE_EXTENSIONS.values():
        for ext in ext_list:
            ext_counts[ext] = 0
    
    for file in path.rglob('*'):
        if file.is_file() and not any(part.startswith('.') for part in file.parts):
            ext = file.suffix
            if ext in ext_counts:
                ext_counts[ext] += 1
    
    if ext_counts:
        top_ext = max(ext_counts, key=ext_counts.get)
        if ext_counts[top_ext] > 0:
            for lang, exts in LANGUAGE_EXTENSIONS.items():
                if top_ext in exts:
                    return lang
    
    return 'Unknown'


def detect_framework(project_path: str, language: str) -> Optional[str]:
    """检测使用的框架"""
    path = Path(project_path)
    
    framework_indicators = {
        'React': ['react', 'react-dom'],
        'Vue': ['vue'],
        'Next.js': ['next'],
        'Angular': ['@angular/core'],
        'Express': ['express'],
        'FastAPI': ['fastapi'],
        'Django': ['django'],
        'Flask': ['flask'],
        'Spring Boot': ['spring-boot'],
        'Flutter': ['flutter'],
    }
    
    # 检查package.json
    pkg_json = path / 'package.json'
    if pkg_json.exists():
        try:
            with open(pkg_json, 'r') as f:
                data = json.load(f)
            deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
            
            for framework, indicators in framework_indicators.items():
                if any(ind in deps for ind in indicators):
                    return framework
        except:
            pass
    
    # 检查requirements.txt
    req_file = path / 'requirements.txt'
    if req_file.exists():
        content = req_file.read_text()
        for framework, indicators in framework_indicators.items():
            if any(ind in content.lower() for ind in [i.lower() for i in indicators]):
                return framework
    
    return None


def extract_project_name(project_path: str) -> str:
    """提取项目名称"""
    path = Path(project_path)
    
    # 从package.json
    pkg_json = path / 'package.json'
    if pkg_json.exists():
        try:
            with open(pkg_json, 'r') as f:
                data = json.load(f)
            return data.get('name', path.name)
        except:
            pass
    
    # 从pyproject.toml
    pyproject = path / 'pyproject.toml'
    if pyproject.exists():
        content = pyproject.read_text()
        match = re.search(r'^name\s*=\s*["\'](.+?)["\']', content, re.M)
        if match:
            return match.group(1)
    
    # 从Cargo.toml
    cargo = path / 'Cargo.toml'
    if cargo.exists():
        content = cargo.read_text()
        match = re.search(r'^name\s*=\s*["\'](.+?)["\']', content, re.M)
        if match:
            return match.group(1)
    
    return path.name


def extract_description(project_path: str) -> Optional[str]:
    """提取项目描述"""
    path = Path(project_path)
    
    # 从package.json
    pkg_json = path / 'package.json'
    if pkg_json.exists():
        try:
            with open(pkg_json, 'r') as f:
                data = json.load(f)
            return data.get('description')
        except:
            pass
    
    # 从pyproject.toml
    pyproject = path / 'pyproject.toml'
    if pyproject.exists():
        content = pyproject.read_text()
        match = re.search(r'^description\s*=\s*["\'](.+?)["\']', content, re.M)
        if match:
            return match.group(1)
    
    return None


def detect_entry_points(project_path: str, language: str) -> List[str]:
    """检测项目入口文件"""
    path = Path(project_path)
    entry_points = []
    
    common_entries = {
        'Python': ['main.py', 'app.py', 'manage.py', '__main__.py'],
        'JavaScript': ['index.js', 'app.js', 'server.js', 'main.js'],
        'TypeScript': ['index.ts', 'app.ts', 'server.ts', 'main.ts'],
        'Java': ['Main.java', 'Application.java'],
        'Go': ['main.go'],
        'Rust': ['main.rs', 'lib.rs'],
    }
    
    for entry in common_entries.get(language, []):
        for file in path.rglob(entry):
            if file.is_file():
                entry_points.append(str(file.relative_to(path)))
                if len(entry_points) >= 3:
                    break
    
    return entry_points


def get_directory_structure(project_path: str, max_depth: int = 3) -> str:
    """生成目录结构文本"""
    path = Path(project_path)
    lines = []
    
    ignore_patterns = {'.git', 'node_modules', '__pycache__', '.pytest_cache', 
                       'dist', 'build', '.next', '.nuxt', 'target', 'vendor'}
    
    def tree(dir_path: Path, prefix: str = "", depth: int = 0):
        if depth > max_depth:
            return
        
        try:
            entries = sorted([e for e in dir_path.iterdir() 
                            if e.name not in ignore_patterns and not e.name.startswith('.')],
                           key=lambda e: (e.is_file(), e.name.lower()))
        except PermissionError:
            return
        
        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{entry.name}")
            
            if entry.is_dir():
                extension = "    " if is_last else "│   "
                tree(entry, prefix + extension, depth + 1)
    
    lines.append(path.name + "/")
    tree(path)
    return '\n'.join(lines)


def analyze_project(project_path: str) -> Dict:
    """完整分析项目，返回所有元数据"""
    path = Path(project_path)
    
    if not path.exists():
        raise ValueError(f"项目路径不存在: {project_path}")
    
    language = detect_language(project_path)
    framework = detect_framework(project_path, language)
    name = extract_project_name(project_path)
    description = extract_description(project_path)
    entry_points = detect_entry_points(project_path, language)
    structure = get_directory_structure(project_path)
    
    # 检测许可证
    license_file = None
    for lic in ['LICENSE', 'LICENSE.md', 'LICENSE.txt', 'COPYING']:
        if (path / lic).exists():
            license_file = lic
            break
    
    return {
        'name': name,
        'language': language,
        'framework': framework,
        'description': description,
        'entry_points': entry_points,
        'directory_structure': structure,
        'has_license': license_file is not None,
        'license_file': license_file,
    }


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_project.py <project_path>", file=sys.stderr)
        sys.exit(1)
    
    project_path = sys.argv[1]
    result = analyze_project(project_path)
    print(json.dumps(result, indent=2, ensure_ascii=False))
