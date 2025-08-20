"""
命令行接口模块
"""

import argparse
import sys
import os
from pathlib import Path
from .core import ImageToExcel
from .utils import validate_image_path, get_image_dimensions, calculate_cell_count


def main():
    """命令行主函数"""
    parser = argparse.ArgumentParser(
        description="将图片转换为Excel像素画",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  # 基本转换
  img2excel input.jpg output.xlsx
  
  # 指定最大宽度，保持比例
  img2excel input.jpg output.xlsx --max-width 100
  
  # 指定最大高度，保持比例
  img2excel input.jpg output.xlsx --max-height 100
  
  # 指定单元格尺寸
  img2excel input.jpg output.xlsx --cell-width 20 --cell-height 20
  
  # 不保持比例，强制指定尺寸
  img2excel input.jpg output.xlsx --max-width 100 --max-height 50 --no-ratio
  
  # 预览转换后的尺寸
  img2excel input.jpg --preview --max-width 100
        """
    )
    
    # 必需参数
    parser.add_argument(
        "input_image",
        help="输入图片文件路径"
    )
    
    parser.add_argument(
        "output_excel",
        nargs="?",
        help="输出Excel文件路径（可选，用于预览模式）"
    )
    
    # 尺寸控制参数
    parser.add_argument(
        "--max-width",
        type=int,
        help="最大宽度（单元格数量）"
    )
    
    parser.add_argument(
        "--max-height", 
        type=int,
        help="最大高度（单元格数量）"
    )
    
    parser.add_argument(
        "--no-ratio",
        action="store_true",
        help="不保持原图片比例"
    )
    
    # 单元格尺寸参数
    parser.add_argument(
        "--cell-width",
        type=int,
        help="单元格宽度（像素）"
    )
    
    parser.add_argument(
        "--cell-height",
        type=int,
        help="单元格高度（像素）"
    )
    
    # 其他参数
    parser.add_argument(
        "--sheet-name",
        default="PixelArt",
        help="Excel工作表名称（默认: PixelArt）"
    )
    
    parser.add_argument(
        "--preview",
        action="store_true",
        help="预览模式，只显示转换后的尺寸，不生成文件"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="详细输出模式"
    )
    
    args = parser.parse_args()
    
    # 验证输入文件
    if not validate_image_path(args.input_image):
        print(f"错误: 无效的图片文件: {args.input_image}")
        sys.exit(1)
    
    # 预览模式
    if args.preview:
        try:
            # 获取原图片尺寸
            original_width, original_height = get_image_dimensions(args.input_image)
            print(f"原图片尺寸: {original_width} x {original_height}")
            
            # 计算目标尺寸
            keep_ratio = not args.no_ratio
            target_width, target_height = calculate_cell_count(
                original_width, original_height,
                max_cells=10000,  # 默认最大单元格数
                keep_ratio=keep_ratio
            )
            
            if args.max_width:
                target_width = min(target_width, args.max_width)
            if args.max_height:
                target_height = min(target_height, args.max_height)
            
            print(f"转换后尺寸: {target_width} x {target_height}")
            print(f"总单元格数: {target_width * target_height}")
            
            if args.verbose:
                print(f"保持比例: {'是' if keep_ratio else '否'}")
                
        except Exception as e:
            print(f"预览失败: {e}")
            sys.exit(1)
        
        return
    
    # 检查输出文件路径
    if not args.output_excel:
        print("错误: 请指定输出Excel文件路径")
        sys.exit(1)
    
    # 执行转换
    try:
        print(f"开始转换图片: {args.input_image}")
        
        # 创建转换器实例
        converter = ImageToExcel(args.input_image)
        
        # 获取图片信息
        if args.verbose:
            info = converter.get_image_info()
            print(f"图片信息: {info['width']} x {info['height']}, 格式: {info['format']}")
        
        # 执行转换
        output_path = converter.convert_to_excel(
            output_path=args.output_excel,
            cell_width=args.cell_width,
            cell_height=args.cell_height,
            max_width=args.max_width,
            max_height=args.max_height,
            keep_ratio=not args.no_ratio,
            sheet_name=args.sheet_name
        )
        
        print(f"转换完成！输出文件: {output_path}")
        
        # 显示文件信息
        if args.verbose and os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"文件大小: {file_size} 字节")
        
    except Exception as e:
        print(f"转换失败: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
