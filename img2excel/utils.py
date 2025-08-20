"""
工具函数模块
"""

from typing import Tuple
from PIL import Image


def resize_image(image: Image.Image, target_size: Tuple[int, int]) -> Image.Image:
    """
    调整图片尺寸
    
    Args:
        image: PIL图片对象
        target_size: 目标尺寸 (width, height)
        
    Returns:
        调整后的图片对象
    """
    return image.resize(target_size, Image.Resampling.LANCZOS)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    将RGB值转换为十六进制颜色字符串
    
    Args:
        r: 红色值 (0-255)
        g: 绿色值 (0-255)
        b: 蓝色值 (0-255)
        
    Returns:
        十六进制颜色字符串 (如 "#FF0000")
    """
    return f"{r:02X}{g:02X}{b:02X}"


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    将十六进制颜色字符串转换为RGB值
    
    Args:
        hex_color: 十六进制颜色字符串 (如 "#FF0000" 或 "FF0000")
        
    Returns:
        (r, g, b) 元组
    """
    # 移除可能的 # 前缀
    hex_color = hex_color.lstrip('#')
    
    # 解析RGB值
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    return r, g, b


def validate_image_path(image_path: str) -> bool:
    """
    验证图片文件路径是否有效
    
    Args:
        image_path: 图片文件路径
        
    Returns:
        是否有效
    """
    import os
    if not os.path.exists(image_path):
        return False
    
    # 检查文件扩展名
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}
    file_ext = os.path.splitext(image_path)[1].lower()
    
    return file_ext in valid_extensions


def get_image_dimensions(image_path: str) -> Tuple[int, int]:
    """
    获取图片尺寸
    
    Args:
        image_path: 图片文件路径
        
    Returns:
        (宽度, 高度) 元组
    """
    try:
        with Image.open(image_path) as img:
            return img.size
    except Exception as e:
        raise ValueError(f"无法读取图片尺寸: {e}")


def calculate_cell_count(
    image_width: int, 
    image_height: int, 
    max_cells: int = 1000,
    keep_ratio: bool = True
) -> Tuple[int, int]:
    """
    计算适合的单元格数量
    
    Args:
        image_width: 图片宽度
        image_height: 图片高度
        max_cells: 最大单元格数量
        keep_ratio: 是否保持比例
        
    Returns:
        (宽度单元格数, 高度单元格数) 元组
    """
    if keep_ratio:
        # 保持比例，计算缩放因子
        scale = (max_cells / (image_width * image_height)) ** 0.5
        new_width = max(1, int(image_width * scale))
        new_height = max(1, int(image_height * scale))
    else:
        # 不保持比例，平均分配
        total_cells = max_cells
        aspect_ratio = image_width / image_height
        
        new_width = int((total_cells * aspect_ratio) ** 0.5)
        new_height = int(total_cells / new_width)
        
        # 确保至少1x1
        new_width = max(1, new_width)
        new_height = max(1, new_height)
    
    return new_width, new_height


def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小
    
    Args:
        size_bytes: 字节数
        
    Returns:
        格式化的文件大小字符串
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"
