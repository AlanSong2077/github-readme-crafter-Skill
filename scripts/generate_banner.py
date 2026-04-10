#!/usr/bin/env python3
"""
专业Banner生成器 - 创建顶级开源项目风格的README横幅
支持渐变背景、现代排版、SVG输出
"""
import argparse
import base64
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False


def create_gradient(width: int, height: int, color_start: tuple, color_end: tuple) -> Image.Image:
    """创建渐变背景"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    for y in range(height):
        ratio = y / height
        r = int(color_start[0] * (1 - ratio) + color_end[0] * ratio)
        g = int(color_start[1] * (1 - ratio) + color_end[1] * ratio)
        b = int(color_start[2] * (1 - ratio) + color_end[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return image


def generate_svg_banner(text: str, subtitle: str = "", 
                        primary_color: str = "#1a1a2e",
                        secondary_color: str = "#16213e",
                        accent_color: str = "#e94560") -> str:
    """
    生成SVG格式的专业Banner - 无需外部依赖
    """
    width = 1280
    height = 320
    
    # 计算字体大小
    title_size = min(72, max(48, 800 // len(text))) if text else 64
    subtitle_size = max(24, title_size // 2)
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  
  <!-- 背景 -->
  <rect width="{width}" height="{height}" fill="url(#grad)"/>
  
  <!-- 装饰几何图形 -->
  <circle cx="1100" cy="80" r="120" fill="{accent_color}" opacity="0.1"/>
  <circle cx="100" cy="240" r="80" fill="{accent_color}" opacity="0.08"/>
  <rect x="850" y="200" width="60" height="60" fill="{accent_color}" opacity="0.15" transform="rotate(45 880 230)"/>
  
  <!-- 标题 -->
  <text x="{width//2}" y="{height//2 - 10}" 
        font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
        font-size="{title_size}" font-weight="700" fill="#ffffff" text-anchor="middle">
    {text}
  </text>
  
  <!-- 副标题 -->
  {'<text x="' + str(width//2) + '" y="' + str(height//2 + 50) + '" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-size="' + str(subtitle_size) + '" fill="#cccccc" text-anchor="middle">' + subtitle + '</text>' if subtitle else ''}
  
  <!-- 底部装饰线 -->
  <rect x="{width//2 - 60}" y="{height - 40}" width="120" height="3" fill="{accent_color}"/>
</svg>'''
    
    return svg


def generate_png_banner(text: str, subtitle: str = "",
                        output_path: str = "banner.png",
                        color_scheme: str = "dark") -> str:
    """
    生成PNG格式的Banner - 需要Pillow
    """
    if not HAS_PILLOW:
        print("Warning: Pillow not installed. Generating SVG instead.")
        return generate_svg_banner(text, subtitle)
    
    width, height = 1280, 320
    
    # 颜色方案
    schemes = {
        'dark': ((26, 26, 46), (22, 33, 62), (233, 69, 96)),
        'blue': ((0, 82, 147), (0, 150, 199), (72, 202, 228)),
        'purple': ((69, 25, 82), (60, 9, 108), (158, 71, 132)),
        'green': ((20, 60, 40), (30, 80, 60), (80, 200, 120)),
    }
    
    c_start, c_end, accent = schemes.get(color_scheme, schemes['dark'])
    
    # 创建渐变背景
    img = create_gradient(width, height, c_start, c_end)
    draw = ImageDraw.Draw(img)
    
    # 尝试加载字体，否则使用默认字体
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 64)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    
    # 绘制文字
    bbox = draw.textbbox((0, 0), text, font=font_title)
    text_width = bbox[2] - bbox[0]
    title_x = (width - text_width) // 2
    title_y = height // 2 - 40
    
    draw.text((title_x, title_y), text, fill=(255, 255, 255), font=font_title)
    
    if subtitle:
        bbox_sub = draw.textbbox((0, 0), subtitle, font=font_sub)
        sub_width = bbox_sub[2] - bbox_sub[0]
        sub_x = (width - sub_width) // 2
        sub_y = title_y + 70
        draw.text((sub_x, sub_y), subtitle, fill=(200, 200, 200), font=font_sub)
    
    # 保存
    img.save(output_path, 'PNG')
    return output_path


def banner_to_base64_svg(svg_content: str) -> str:
    """将SVG转换为base64，可用于Markdown内嵌"""
    encoded = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{encoded}"


def main():
    parser = argparse.ArgumentParser(description='Generate professional README banners')
    parser.add_argument('text', help='Main banner text (project name)')
    parser.add_argument('--subtitle', '-s', help='Subtitle text')
    parser.add_argument('--output', '-o', default='banner.svg', help='Output file path')
    parser.add_argument('--format', '-f', choices=['svg', 'png'], default='svg', help='Output format')
    parser.add_argument('--scheme', '-c', choices=['dark', 'blue', 'purple', 'green'], 
                        default='dark', help='Color scheme (PNG only)')
    
    args = parser.parse_args()
    
    if args.format == 'svg':
        svg = generate_svg_banner(args.text, args.subtitle)
        Path(args.output).write_text(svg)
        print(f"SVG banner saved to: {args.output}")
    else:
        path = generate_png_banner(args.text, args.subtitle, args.output, args.scheme)
        print(f"PNG banner saved to: {path}")


if __name__ == '__main__':
    main()
