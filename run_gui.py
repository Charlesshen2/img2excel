#!/usr/bin/env python3
"""
img2excel GUI 启动脚本
运行此脚本启动图形化界面
"""

import sys
import os

# 添加项目路径到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from img2excel.gui import Img2ExcelGUI
    import tkinter as tk
    
    def main():
        """启动GUI主函数"""
        root = tk.Tk()
        app = Img2ExcelGUI(root)
        root.mainloop()
    
    if __name__ == "__main__":
        main()
        
except ImportError as e:
    print(f"错误：无法导入必要的模块 - {e}")
    print("请确保已安装所有依赖：pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"启动失败：{e}")
    sys.exit(1)
