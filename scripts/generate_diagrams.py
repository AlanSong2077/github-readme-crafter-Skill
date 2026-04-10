#!/usr/bin/env python3
"""
Advanced SVG Diagram Generator - Produces professional, high-quality diagrams
Uses pure Python + SVG for maximum compatibility and visual quality
"""

import xml.etree.ElementTree as ET
from typing import List, Dict, Optional
from pathlib import Path


class SVGBase:
    """Base SVG generator with professional styling"""
    
    def __init__(self, width: int = 1200, height: int = 600):
        self.width = width
        self.height = height
        self.svg = ET.Element('svg', {
            'xmlns': 'http://www.w3.org/2000/svg',
            'width': str(width),
            'height': str(height),
            'viewBox': f'0 0 {width} {height}'
        })
        
        # Professional color palette
        self.colors = {
            'bg': '#0f172a',
            'bg_light': '#1e293b',
            'accent': '#38bdf8',
            'accent2': '#22d3ee',
            'accent3': '#a78bfa',
            'accent4': '#f472b6',
            'text': '#f8fafc',
            'text_dim': '#94a3b8',
            'border': '#334155',
            'gradient_start': '#1e3a5f',
            'gradient_end': '#0f172a',
        }
    
    def add_defs(self):
        """Add SVG definitions (gradients, filters, etc.)"""
        defs = ET.SubElement(self.svg, 'defs')
        
        # Gradient for background
        grad = ET.SubElement(defs, 'linearGradient', {
            'id': 'bgGradient', 'x1': '0%', 'y1': '0%', 'x2': '100%', 'y2': '100%'
        })
        ET.SubElement(grad, 'stop', {'offset': '0%', 'style': f'stop-color:{self.colors["gradient_start"]}'})
        ET.SubElement(grad, 'stop', {'offset': '100%', 'style': f'stop-color:{self.colors["gradient_end"]}'})
        
        # Glow filter for accent elements
        glow = ET.SubElement(defs, 'filter', {'id': 'glow', 'x': '-50%', 'y': '-50%', 'width': '200%', 'height': '200%'})
        ET.SubElement(glow, 'feGaussianBlur', {'stdDeviation': '3', 'result': 'coloredBlur'})
        feMerge = ET.SubElement(glow, 'feMerge')
        ET.SubElement(feMerge, 'feMergeNode', {'in': 'coloredBlur'})
        ET.SubElement(feMerge, 'feMergeNode', {'in': 'SourceGraphic'})
        
        # Drop shadow
        shadow = ET.SubElement(defs, 'filter', {'id': 'shadow', 'x': '-20%', 'y': '-20%', 'width': '140%', 'height': '140%'})
        ET.SubElement(shadow, 'feDropShadow', {'dx': '0', 'dy': '4', 'stdDeviation': '8', 'flood-color': '#000000', 'flood-opacity': '0.3'})
        
        # Node gradient
        node_grad = ET.SubElement(defs, 'linearGradient', {
            'id': 'nodeGradient', 'x1': '0%', 'y1': '0%', 'x2': '0%', 'y2': '100%'
        })
        ET.SubElement(node_grad, 'stop', {'offset': '0%', 'style': 'stop-color:#1e293b'})
        ET.SubElement(node_grad, 'stop', {'offset': '100%', 'style': 'stop-color:#0f172a'})
        
        return defs
    
    def add_background(self):
        """Add background rectangle"""
        rect = ET.SubElement(self.svg, 'rect', {
            'width': str(self.width),
            'height': str(self.height),
            'fill': 'url(#bgGradient)'
        })
        
        # Grid pattern
        defs = self.svg.find('defs')
        grid = ET.SubElement(defs, 'pattern', {
            'id': 'grid', 'width': '40', 'height': '40', 'patternUnits': 'userSpaceOnUse'
        })
        ET.SubElement(grid, 'path', {
            'd': 'M 40 0 L 0 0 0 40', 'fill': 'none', 'stroke': '#1e293b', 'stroke-width': '1'
        })
        
        bg_rect = ET.SubElement(self.svg, 'rect', {
            'width': str(self.width), 'height': str(self.height), 'fill': 'url(#grid)', 'opacity': '0.3'
        })
    
    def draw_arrow(self, x1: int, y1: int, x2: int, y2: int, color: str = None):
        """Draw an arrow between two points"""
        if color is None:
            color = self.colors['accent']
        
        # Calculate angle
        import math
        angle = math.atan2(y2 - y1, x2 - x1)
        arrow_size = 10
        
        # Arrow head points
        ax1 = x2 - arrow_size * math.cos(angle - math.pi/6)
        ay1 = y2 - arrow_size * math.sin(angle - math.pi/6)
        ax2 = x2 - arrow_size * math.cos(angle + math.pi/6)
        ay2 = y2 - arrow_size * math.sin(angle + math.pi/6)
        
        # Line
        line = ET.SubElement(self.svg, 'line', {
            'x1': str(x1), 'y1': str(y1), 'x2': str(x2), 'y2': str(y2),
            'stroke': color, 'stroke-width': '2', 'stroke-dasharray': '5,3'
        })
        
        # Arrow head
        arrow = ET.SubElement(self.svg, 'polygon', {
            'points': f'{x2},{y2} {int(ax1)},{int(ay1)} {int(ax2)},{int(ay2)}',
            'fill': color
        })
    
    def draw_rounded_rect(self, x: int, y: int, w: int, h: int, 
                          fill: str = None, stroke: str = None, 
                          text: str = None, icon: str = None,
                          rx: int = 12, ry: int = 12):
        """Draw a rounded rectangle with optional text and icon"""
        if fill is None:
            fill = 'url(#nodeGradient)'
        if stroke is None:
            stroke = self.colors['border']
        
        # Main rectangle
        rect = ET.SubElement(self.svg, 'rect', {
            'x': str(x), 'y': str(y), 'width': str(w), 'height': str(h),
            'rx': str(rx), 'ry': str(ry),
            'fill': fill, 'stroke': stroke, 'stroke-width': '2',
            'filter': 'url(#shadow)'
        })
        
        # Text
        if text:
            text_el = ET.SubElement(self.svg, 'text', {
                'x': str(x + w//2), 'y': str(y + h//2 + 5),
                'text-anchor': 'middle', 'fill': self.colors['text'],
                'font-family': 'system-ui, -apple-system, sans-serif',
                'font-size': '14', 'font-weight': '600'
            })
            text_el.text = text
        
        return rect
    
    def draw_icon_box(self, x: int, y: int, size: int, icon: str, color: str = None):
        """Draw an icon in a circle"""
        if color is None:
            color = self.colors['accent']
        
        # Circle background
        circle = ET.SubElement(self.svg, 'circle', {
            'cx': str(x + size//2), 'cy': str(y + size//2), 'r': str(size//2),
            'fill': color, 'opacity': '0.2'
        })
        
        # Icon text (emoji)
        icon_el = ET.SubElement(self.svg, 'text', {
            'x': str(x + size//2), 'y': str(y + size//2 + 8),
            'text-anchor': 'middle', 'font-size': '20'
        })
        icon_el.text = icon


class ArchitectureDiagram(SVGBase):
    """Professional Architecture Diagram"""
    
    def __init__(self, width: int = 1200, height: int = 700):
        super().__init__(width, height)
        self.add_defs()
        self.add_background()
        self.node_height = 70
        self.node_width = 180
        self.spacing = 40
    
    def draw_node(self, x: int, y: int, label: str, icon: str, color: str = None, width: int = None):
        """Draw a node with icon and label"""
        if width is None:
            width = self.node_width
        if color is None:
            color = self.colors['accent']
        
        # Icon
        self.draw_icon_box(x, y, 40, icon, color)
        
        # Box
        box_x = x + 45
        self.draw_rounded_rect(box_x, y, width - 45, self.node_height, text=label, stroke=color)
        
        return x + width
    
    def draw_pipeline(self, stages: List[Dict]):
        """Draw a horizontal pipeline"""
        y_start = 100
        x = 50
        
        for i, stage in enumerate(stages):
            # Stage label
            if 'label' in stage:
                label_el = ET.SubElement(self.svg, 'text', {
                    'x': str(x + self.node_width//2), 'y': '60',
                    'text-anchor': 'middle', 'fill': self.colors['accent'],
                    'font-family': 'system-ui', 'font-size': '16', 'font-weight': 'bold'
                })
                label_el.text = stage['label']
            
            # Node
            icon = stage.get('icon', '📦')
            label = stage.get('name', stage.get('label', ''))
            color = stage.get('color', self.colors['accent'])
            
            self.draw_node(x, y_start, label, icon, color)
            
            # Arrow to next
            if i < len(stages) - 1:
                self.draw_arrow(x + self.node_width, y_start + self.node_height//2,
                             x + self.node_width + self.spacing, y_start + self.node_height//2)
            
            x += self.node_width + self.spacing
        
        # Title
        title = ET.SubElement(self.svg, 'text', {
            'x': str(self.width//2), 'y': '30',
            'text-anchor': 'middle', 'fill': self.colors['text'],
            'font-family': 'system-ui', 'font-size': '24', 'font-weight': 'bold'
        })
        title.text = 'Architecture Pipeline'
    
    def to_string(self) -> str:
        """Return SVG as string"""
        return ET.tostring(self.svg, encoding='unicode')


class TechStackDiagram(SVGBase):
    """Professional Tech Stack Diagram"""
    
    def __init__(self, width: int = 1200, height: int = 600):
        super().__init__(width, height)
        self.add_defs()
        self.add_background()
    
    def draw_layer(self, y: int, layer_name: str, items: List[str], colors_list: List[str]):
        """Draw a horizontal layer with items"""
        x_start = 60
        item_width = 200
        spacing = 30
        layer_height = 80
        
        # Layer label
        label = ET.SubElement(self.svg, 'text', {
            'x': '30', 'y': str(y + layer_height//2 + 5),
            'text-anchor': 'start', 'fill': self.colors['text_dim'],
            'font-family': 'system-ui', 'font-size': '12', 'font-weight': 'bold',
            'text-transform': 'uppercase', 'letter-spacing': '2'
        })
        label.text = layer_name
        
        # Items
        for i, (item, color) in enumerate(zip(items, colors_list)):
            x = x_start + i * (item_width + spacing)
            
            # Item box
            rect = ET.SubElement(self.svg, 'rect', {
                'x': str(x), 'y': str(y), 'width': str(item_width), 'height': str(layer_height),
                'rx': '8', 'ry': '8',
                'fill': color, 'opacity': '0.15',
                'stroke': color, 'stroke-width': '2'
            })
            
            # Item text
            text = ET.SubElement(self.svg, 'text', {
                'x': str(x + item_width//2), 'y': str(y + layer_height//2 + 5),
                'text-anchor': 'middle', 'fill': self.colors['text'],
                'font-family': 'system-ui', 'font-size': '14', 'font-weight': '600'
            })
            text.text = item
        
        # Connector line
        line = ET.SubElement(self.svg, 'line', {
            'x1': '20', 'y1': str(y), 'x2': str(self.width - 20), 'y2': str(y),
            'stroke': self.colors['border'], 'stroke-width': '1', 'stroke-dasharray': '4,4'
        })
    
    def draw_connections(self, layers: int):
        """Draw vertical connections between layers"""
        for i in range(layers - 1):
            y1 = 100 + i * 130
            y2 = 100 + (i + 1) * 130
            
            # Draw multiple connection lines
            for j in range(3):
                x = 200 + j * 230
                self.draw_arrow(x, y1 + 80, x, y2)
    
    def to_string(self) -> str:
        """Return SVG as string"""
        return ET.tostring(self.svg, encoding='unicode')


class WorkflowDiagram(SVGBase):
    """Professional Workflow/Process Diagram"""
    
    def __init__(self, width: int = 1000, height: int = 400):
        super().__init__(width, height)
        self.add_defs()
        self.add_background()
    
    def draw_step(self, x: int, y: int, step_num: int, label: str, icon: str = None):
        """Draw a workflow step"""
        size = 60
        
        # Circle
        circle = ET.SubElement(self.svg, 'circle', {
            'cx': str(x + size//2), 'cy': str(y + size//2), 'r': str(size//2),
            'fill': self.colors['accent'], 'opacity': '0.2',
            'stroke': self.colors['accent'], 'stroke-width': '2'
        })
        
        # Number
        num = ET.SubElement(self.svg, 'text', {
            'x': str(x + size//2), 'y': str(y + size//2 + 8),
            'text-anchor': 'middle', 'fill': self.colors['accent'],
            'font-family': 'system-ui', 'font-size': '20', 'font-weight': 'bold'
        })
        num.text = str(step_num)
        
        # Label below
        label_el = ET.SubElement(self.svg, 'text', {
            'x': str(x + size//2), 'y': str(y + size + 25),
            'text-anchor': 'middle', 'fill': self.colors['text'],
            'font-family': 'system-ui', 'font-size': '12', 'font-weight': '500'
        })
        label_el.text = label
        
        return x + size + 40
    
    def draw_horizontal_workflow(self, steps: List[Dict]):
        """Draw a horizontal workflow"""
        y = 100
        x = 50
        
        for i, step in enumerate(steps):
            icon = step.get('icon', '📦')
            label = step.get('label', '')
            
            self.draw_step(x, y, i + 1, label, icon)
            
            # Arrow
            if i < len(steps) - 1:
                self.draw_arrow(x + 60, y + 30, x + 100, y + 30)
                x += 100
            else:
                x += 60
        
        # Title
        title = ET.SubElement(self.svg, 'text', {
            'x': str(self.width//2), 'y': '40',
            'text-anchor': 'middle', 'fill': self.colors['text'],
            'font-family': 'system-ui', 'font-size': '20', 'font-weight': 'bold'
        })
        title.text = 'Workflow'
    
    def to_string(self) -> str:
        """Return SVG as string"""
        return ET.tostring(self.svg, encoding='unicode')


def generate_architecture_svg() -> str:
    """Generate the architecture diagram SVG"""
    diagram = ArchitectureDiagram()
    
    stages = [
        {'label': 'INPUT', 'name': 'Project Path', 'icon': '📁', 'color': '#38bdf8'},
        {'label': 'ANALYZE', 'name': 'Metadata Extract', 'icon': '🔍', 'color': '#22d3ee'},
        {'label': 'GENERATE', 'name': 'Create Assets', 'icon': '⚡', 'color': '#a78bfa'},
        {'label': 'VALIDATE', 'name': 'test.py', 'icon': '🧪', 'color': '#f472b6'},
        {'label': 'OUTPUT', 'name': 'Premium README', 'icon': '✨', 'color': '#22c55e'},
    ]
    
    diagram.draw_pipeline(stages)
    return diagram.to_string()


def generate_techstack_svg() -> str:
    """Generate the tech stack diagram SVG"""
    diagram = TechStackDiagram()
    
    # Draw layers
    diagram.draw_layer(50, 'Frontend', ['Python 3.10+'], ['#38bdf8'])
    diagram.draw_layer(180, 'Services', ['Standard Library', 'Shields.io API'], ['#22d3ee', '#a78bfa'])
    diagram.draw_layer(310, 'Output', ['SVG Banners', 'Mermaid Diagrams'], ['#f472b6', '#22c55e'])
    diagram.draw_layer(440, 'VCS', ['Git'], ['#f97316'])
    
    # Draw connections
    diagram.draw_connections(4)
    
    # Title
    title = ET.SubElement(diagram.svg, 'text', {
        'x': str(diagram.width//2), 'y': '30',
        'text-anchor': 'middle', 'fill': diagram.colors['text'],
        'font-family': 'system-ui', 'font-size': '20', 'font-weight': 'bold'
    })
    title.text = 'Tech Stack'
    
    return diagram.to_string()


def generate_workflow_svg() -> str:
    """Generate the workflow diagram SVG"""
    diagram = WorkflowDiagram()
    
    steps = [
        {'label': 'Analyze', 'icon': '🔍'},
        {'label': 'Generate', 'icon': '⚡'},
        {'label': 'Validate', 'icon': '🧪'},
        {'label': 'Deliver', 'icon': '📦'},
    ]
    
    diagram.draw_horizontal_workflow(steps)
    return diagram.to_string()


if __name__ == '__main__':
    import sys
    
    output_dir = Path('assets')
    output_dir.mkdir(exist_ok=True)
    
    # Generate all diagrams
    arch_svg = generate_architecture_svg()
    (output_dir / 'architecture.svg').write_text(arch_svg)
    print(f"✓ Architecture diagram: {output_dir / 'architecture.svg'}")
    
    tech_svg = generate_techstack_svg()
    (output_dir / 'techstack.svg').write_text(tech_svg)
    print(f"✓ Tech stack diagram: {output_dir / 'techstack.svg'}")
    
    workflow_svg = generate_workflow_svg()
    (output_dir / 'workflow.svg').write_text(workflow_svg)
    print(f"✓ Workflow diagram: {output_dir / 'workflow.svg'}")
