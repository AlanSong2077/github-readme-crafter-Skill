#!/usr/bin/env python3
"""
Mermaid图表生成器 - 为README创建专业的架构图和流程图
"""
import argparse
import json
from pathlib import Path
from typing import List, Dict, Optional


class MermaidGenerator:
    """Mermaid图表生成器"""
    
    @staticmethod
    def architecture_diagram(components: List[Dict], title: str = "System Architecture") -> str:
        """
        生成系统架构图
        
        components: [{"name": "Frontend", "type": "client", "description": "User interface"}, ...]
        types: client, service, database, external
        """
        mermaid = f"```mermaid\nflowchart TB\n    %% {title}\n"
        
        # 定义样式类
        styles = """
    classDef client fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef service fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef database fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef external fill:#fff3e0,stroke:#e65100,stroke-width:2px
"""
        mermaid += styles
        
        # 添加节点
        for comp in components:
            name = comp['name'].replace(' ', '_')
            desc = comp.get('description', comp['name'])
            comp_type = comp.get('type', 'service')
            mermaid += f"    {name}[{desc}]\n"
            mermaid += f"    class {name} {comp_type}\n"
        
        # 添加连接（简单连接，可扩展）
        if len(components) > 1:
            for i in range(len(components) - 1):
                curr = components[i]['name'].replace(' ', '_')
                next_comp = components[i + 1]['name'].replace(' ', '_')
                mermaid += f"    {curr} --> {next_comp}\n"
        
        mermaid += "```"
        return mermaid
    
    @staticmethod
    def workflow_diagram(steps: List[str], title: str = "Workflow") -> str:
        """
        生成工作流程图
        """
        mermaid = f"```mermaid\nflowchart LR\n    %% {title}\n"
        
        for i, step in enumerate(steps):
            step_id = f"S{i}"
            mermaid += f"    {step_id}[{step}]\n"
            if i > 0:
                prev_id = f"S{i-1}"
                mermaid += f"    {prev_id} --> {step_id}\n"
        
        mermaid += "```"
        return mermaid
    
    @staticmethod
    def tech_stack_diagram(frontend: List[str], backend: List[str], 
                          database: List[str], devops: List[str] = None) -> str:
        """
        生成技术栈层次图
        """
        mermaid = "```mermaid\nflowchart TB\n    subgraph Frontend[Frontend Layer]\n"
        
        for tech in frontend:
            mermaid += f"        {tech.replace(' ', '_')}[{tech}]\n"
        mermaid += "    end\n"
        
        mermaid += "    subgraph Backend[Backend Layer]\n"
        for tech in backend:
            mermaid += f"        {tech.replace(' ', '_')}[{tech}]\n"
        mermaid += "    end\n"
        
        mermaid += "    subgraph Data[Data Layer]\n"
        for tech in database:
            mermaid += f"        {tech.replace(' ', '_')}[({tech})]\n"
        mermaid += "    end\n"
        
        if devops:
            mermaid += "    subgraph DevOps[DevOps Layer]\n"
            for tech in devops:
                mermaid += f"        {tech.replace(' ', '_')}[{tech}]\n"
            mermaid += "    end\n"
        
        # 添加连接
        mermaid += "    Frontend --> Backend\n"
        mermaid += "    Backend --> Data\n"
        
        mermaid += "```"
        return mermaid
    
    @staticmethod
    def module_dependency_graph(modules: Dict[str, List[str]]) -> str:
        """
        生成模块依赖图
        
        modules: {"ModuleA": ["ModuleB", "ModuleC"], ...}
        """
        mermaid = "```mermaid\nflowchart TD\n"
        
        # 添加所有节点
        all_modules = set(modules.keys())
        for deps in modules.values():
            all_modules.update(deps)
        
        for mod in all_modules:
            mermaid += f"    {mod.replace('/', '_').replace('.', '_')}[{mod}]\n"
        
        # 添加依赖关系
        for mod, deps in modules.items():
            mod_key = mod.replace('/', '_').replace('.', '_')
            for dep in deps:
                dep_key = dep.replace('/', '_').replace('.', '_')
                mermaid += f"    {mod_key} --> {dep_key}\n"
        
        mermaid += "```"
        return mermaid
    
    @staticmethod
    def timeline_diagram(events: List[Dict]) -> str:
        """
        生成项目时间线图
        
        events: [{"date": "2024-01", "event": "Project started", "milestone": true}, ...]
        """
        mermaid = "```mermaid\ntimeline\n    title Project Timeline\n"
        
        for event in events:
            date = event.get('date', '')
            desc = event.get('event', '')
            if event.get('milestone'):
                desc = f"🎯 {desc}"
            mermaid += f"    {date} : {desc}\n"
        
        mermaid += "```"
        return mermaid


def detect_tech_stack(project_path: str) -> Dict[str, List[str]]:
    """
    从项目路径自动检测技术栈
    """
    path = Path(project_path)
    stack = {
        'frontend': [],
        'backend': [],
        'database': [],
        'devops': []
    }
    
    # 检测前端技术
    if (path / 'package.json').exists():
        try:
            pkg = json.loads((path / 'package.json').read_text())
            deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}
            
            if 'react' in deps:
                stack['frontend'].append('React')
            if 'vue' in deps:
                stack['frontend'].append('Vue')
            if 'next' in deps:
                stack['frontend'].append('Next.js')
            if 'typescript' in deps or '@types/node' in deps:
                stack['frontend'].append('TypeScript')
            if 'tailwindcss' in deps:
                stack['frontend'].append('Tailwind CSS')
            if 'webpack' in deps or 'vite' in deps:
                stack['frontend'].append(deps.get('vite') and 'Vite' or 'Webpack')
        except:
            pass
    
    # 检测后端技术
    if (path / 'requirements.txt').exists() or (path / 'pyproject.toml').exists():
        stack['backend'].append('Python')
        
        req_content = ''
        if (path / 'requirements.txt').exists():
            req_content = (path / 'requirements.txt').read_text()
        
        if 'fastapi' in req_content.lower():
            stack['backend'].append('FastAPI')
        elif 'flask' in req_content.lower():
            stack['backend'].append('Flask')
        elif 'django' in req_content.lower():
            stack['backend'].append('Django')
    
    if (path / 'Cargo.toml').exists():
        stack['backend'].append('Rust')
    
    if (path / 'go.mod').exists():
        stack['backend'].append('Go')
    
    # 检测数据库
    db_files = list(path.glob('**/*.sql'))
    if db_files or 'prisma' in (path / 'package.json').read_text() if (path / 'package.json').exists() else False:
        stack['database'].append('PostgreSQL/MySQL')
    
    if (path / 'docker-compose.yml').exists() or (path / 'Dockerfile').exists():
        stack['devops'].append('Docker')
    
    return stack


def main():
    parser = argparse.ArgumentParser(description='Generate Mermaid diagrams for README')
    parser.add_argument('type', choices=['architecture', 'workflow', 'techstack', 'modules'],
                        help='Type of diagram to generate')
    parser.add_argument('--project', '-p', help='Project path for auto-detection')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    gen = MermaidGenerator()
    result = ""
    
    if args.type == 'techstack' and args.project:
        stack = detect_tech_stack(args.project)
        result = gen.tech_stack_diagram(
            stack.get('frontend', ['-']),
            stack.get('backend', ['-']),
            stack.get('database', ['-']),
            stack.get('devops', [])
        )
    elif args.type == 'architecture':
        # 示例架构
        components = [
            {"name": "Web Client", "type": "client", "description": "Browser App"},
            {"name": "API Gateway", "type": "service", "description": "API Gateway"},
            {"name": "Core Service", "type": "service", "description": "Core Service"},
            {"name": "Database", "type": "database", "description": "PostgreSQL"},
        ]
        result = gen.architecture_diagram(components)
    elif args.type == 'workflow':
        steps = ["Clone", "Install", "Configure", "Run", "Deploy"]
        result = gen.workflow_diagram(steps)
    elif args.type == 'modules':
        modules = {"App": ["Utils", "Components"], "Components": ["Utils"]}
        result = gen.module_dependency_graph(modules)
    
    if args.output:
        Path(args.output).write_text(result)
        print(f"Diagram saved to: {args.output}")
    else:
        print(result)


if __name__ == '__main__':
    main()
