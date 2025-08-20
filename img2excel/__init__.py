"""
img2excel - 图片转Excel像素画工具

一个功能强大的Python工具，可以将任意图片转换为Excel像素画，
支持多种图片格式和自定义参数设置。

主要模块:
- core: 核心转换功能
- utils: 工具函数
- cli: 命令行接口
- gui: 图形化界面
"""

from .core import ImageToExcel
from .utils import resize_image, rgb_to_hex, validate_image_path, get_image_dimensions

__version__ = "1.0.0"
__author__ = "Charlesshen2"
__email__ = "463674542@qq.com"

__all__ = [
    "ImageToExcel",
    "resize_image", 
    "rgb_to_hex",
    "validate_image_path",
    "get_image_dimensions"
]
