#!/usr/bin/env python3
"""
img2excel 图形化界面模块
提供用户友好的图形界面来使用 img2excel 包
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
from pathlib import Path
from PIL import Image, ImageTk
import openpyxl
from .core import ImageToExcel
from .utils import validate_image_path, get_image_dimensions, calculate_cell_count


class Img2ExcelGUI:
    """img2excel 图形化界面主类"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("img2excel - 图片转Excel像素画工具")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # 变量
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.max_width = tk.IntVar(value=100)
        self.max_height = tk.IntVar(value=100)
        self.cell_width = tk.IntVar(value=20)
        self.cell_height = tk.IntVar(value=20)
        self.keep_ratio = tk.BooleanVar(value=True)
        self.sheet_name = tk.StringVar(value="PixelArt")
        
        # 预览图片
        self.preview_image = None
        self.preview_photo = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """设置用户界面"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 标题
        title_label = ttk.Label(main_frame, text="🖼️ img2excel - 图片转Excel像素画工具", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 输入文件选择
        self.create_file_selection_frame(main_frame, 1)
        
        # 图片预览
        self.create_preview_frame(main_frame, 2)
        
        # 参数设置
        self.create_settings_frame(main_frame, 3)
        
        # 输出设置
        self.create_output_frame(main_frame, 4)
        
        # 转换按钮和进度
        self.create_convert_frame(main_frame, 5)
        
        # 日志显示
        self.create_log_frame(main_frame, 6)
        
    def create_file_selection_frame(self, parent, row):
        """创建文件选择框架"""
        frame = ttk.LabelFrame(parent, text="📁 选择输入图片", padding="10")
        frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame.columnconfigure(1, weight=1)
        
        # 输入文件选择
        ttk.Label(frame, text="输入图片:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Entry(frame, textvariable=self.input_path, width=50).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        ttk.Button(frame, text="浏览...", command=self.select_input_file).grid(row=0, column=2)
        
        # 支持格式说明
        format_label = ttk.Label(frame, text="支持格式: JPG, PNG, BMP, GIF, TIFF, WebP", 
                                font=("Arial", 9), foreground="gray")
        format_label.grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=(5, 0))
        
    def create_preview_frame(self, parent, row):
        """创建图片预览框架"""
        frame = ttk.LabelFrame(parent, text="👁️ 图片预览", padding="10")
        frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame.columnconfigure(0, weight=1)
        
        # 预览标签
        self.preview_label = ttk.Label(frame, text="请选择一张图片进行预览", 
                                      font=("Arial", 12), foreground="gray")
        self.preview_label.grid(row=0, column=0, pady=20)
        
        # 图片信息
        self.info_label = ttk.Label(frame, text="", font=("Arial", 9), foreground="blue")
        self.info_label.grid(row=1, column=0, pady=(5, 0))
        
    def create_settings_frame(self, parent, row):
        """创建参数设置框架"""
        frame = ttk.LabelFrame(parent, text="⚙️ 转换参数设置", padding="10")
        frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame.columnconfigure(1, weight=1)
        
        # 第一行：最大尺寸
        ttk.Label(frame, text="最大宽度 (单元格):").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Spinbox(frame, from_=1, to=1000, textvariable=self.max_width, width=10).grid(row=0, column=1, sticky=tk.W, padx=(0, 20))
        
        ttk.Label(frame, text="最大高度 (单元格):").grid(row=0, column=2, sticky=tk.W, padx=(20, 10))
        ttk.Spinbox(frame, from_=1, to=1000, textvariable=self.max_height, width=10).grid(row=0, column=3, sticky=tk.W)
        
        # 第二行：单元格尺寸
        ttk.Label(frame, text="单元格宽度 (像素):").grid(row=1, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        ttk.Spinbox(frame, from_=1, to=100, textvariable=self.cell_width, width=10).grid(row=1, column=1, sticky=tk.W, padx=(0, 20), pady=(10, 0))
        
        ttk.Label(frame, text="单元格高度 (像素):").grid(row=1, column=2, sticky=tk.W, padx=(20, 10), pady=(10, 0))
        ttk.Spinbox(frame, from_=1, to=100, textvariable=self.cell_height, width=10).grid(row=1, column=3, sticky=tk.W, pady=(10, 0))
        
        # 第三行：其他选项
        ttk.Checkbutton(frame, text="保持原图片比例", variable=self.keep_ratio).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))
        
        ttk.Label(frame, text="工作表名称:").grid(row=2, column=2, sticky=tk.W, padx=(20, 10), pady=(10, 0))
        ttk.Entry(frame, textvariable=self.sheet_name, width=15).grid(row=2, column=3, sticky=tk.W, pady=(10, 0))
        
    def create_output_frame(self, parent, row):
        """创建输出设置框架"""
        frame = ttk.LabelFrame(parent, text="💾 输出设置", padding="10")
        frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame.columnconfigure(1, weight=1)
        
        ttk.Label(frame, text="输出文件:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Entry(frame, textvariable=self.output_path, width=50).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        ttk.Button(frame, text="浏览...", command=self.select_output_file).grid(row=0, column=2)
        
    def create_convert_frame(self, parent, row):
        """创建转换控制框架"""
        frame = ttk.LabelFrame(parent, text="🚀 转换控制", padding="10")
        frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame.columnconfigure(1, weight=1)
        
        # 转换按钮
        self.convert_btn = ttk.Button(frame, text="开始转换", command=self.start_conversion, 
                                     style="Accent.TButton")
        self.convert_btn.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # 进度条
        self.progress = ttk.Progressbar(frame, mode='indeterminate')
        self.progress.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # 状态标签
        self.status_label = ttk.Label(frame, text="就绪", font=("Arial", 9), foreground="green")
        self.status_label.grid(row=2, column=0, columnspan=2)
        
    def create_log_frame(self, parent, row):
        """创建日志显示框架"""
        frame = ttk.LabelFrame(parent, text="📋 转换日志", padding="10")
        frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        # 日志文本框
        self.log_text = scrolledtext.ScrolledText(frame, height=8, width=80)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 清空日志按钮
        ttk.Button(frame, text="清空日志", command=self.clear_log).grid(row=1, column=0, pady=(5, 0))
        
    def select_input_file(self):
        """选择输入图片文件"""
        file_path = filedialog.askopenfilename(
            title="选择图片文件",
            filetypes=[
                ("图片文件", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif *.webp"),
                ("所有文件", "*.*")
            ]
        )
        if file_path:
            self.input_path.set(file_path)
            self.output_path.set(self.generate_output_path(file_path))
            self.load_preview(file_path)
            self.log_message(f"已选择输入文件: {file_path}")
            
    def select_output_file(self):
        """选择输出Excel文件"""
        file_path = filedialog.asksaveasfilename(
            title="保存Excel文件",
            defaultextension=".xlsx",
            filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")]
        )
        if file_path:
            self.output_path.set(file_path)
            self.log_message(f"已设置输出文件: {file_path}")
            
    def generate_output_path(self, input_path):
        """根据输入文件路径生成输出文件路径"""
        input_file = Path(input_path)
        output_dir = input_file.parent
        output_name = f"{input_file.stem}_pixel_art.xlsx"
        return str(output_dir / output_name)
        
    def load_preview(self, image_path):
        """加载图片预览"""
        try:
            # 加载图片
            image = Image.open(image_path)
            
            # 获取图片信息
            width, height = image.size
            file_size = os.path.getsize(image_path)
            
            # 计算预览尺寸（最大200x200）
            max_preview_size = 200
            if width > height:
                preview_width = max_preview_size
                preview_height = int(height * max_preview_size / width)
            else:
                preview_height = max_preview_size
                preview_width = int(width * max_preview_size / height)
            
            # 创建预览图片
            preview_image = image.resize((preview_width, preview_height), Image.Resampling.LANCZOS)
            self.preview_photo = ImageTk.PhotoImage(preview_image)
            
            # 更新预览标签
            self.preview_label.configure(image=self.preview_photo, text="")
            
            # 更新信息标签
            info_text = f"图片尺寸: {width} × {height} 像素 | 文件大小: {self.format_file_size(file_size)}"
            self.info_label.configure(text=info_text)
            
            # 自动设置合适的参数
            self.auto_set_parameters(width, height)
            
        except Exception as e:
            self.log_message(f"加载预览失败: {str(e)}")
            self.preview_label.configure(image="", text="预览加载失败")
            
    def auto_set_parameters(self, width, height):
        """根据图片尺寸自动设置合适的参数"""
        # 计算合适的最大尺寸
        max_dimension = max(width, height)
        if max_dimension <= 100:
            suggested_size = max_dimension
        elif max_dimension <= 500:
            suggested_size = 100
        else:
            suggested_size = 200
            
        if width > height:
            self.max_width.set(suggested_size)
            if self.keep_ratio.get():
                self.max_height.set(int(height * suggested_size / width))
        else:
            self.max_height.set(suggested_size)
            if self.keep_ratio.get():
                self.max_width.set(int(width * suggested_size / height))
                
    def start_conversion(self):
        """开始转换"""
        # 验证输入
        if not self.input_path.get():
            messagebox.showerror("错误", "请选择输入图片文件")
            return
            
        if not self.output_path.get():
            messagebox.showerror("错误", "请设置输出文件路径")
            return
            
        # 验证图片文件
        if not validate_image_path(self.input_path.get()):
            messagebox.showerror("错误", "无效的图片文件")
            return
            
        # 开始转换（在新线程中）
        self.convert_btn.configure(state="disabled")
        self.progress.start()
        self.status_label.configure(text="转换中...", foreground="blue")
        
        # 在新线程中执行转换
        thread = threading.Thread(target=self.convert_image)
        thread.daemon = True
        thread.start()
        
    def convert_image(self):
        """执行图片转换"""
        try:
            self.log_message("开始转换图片...")
            
            # 创建转换器
            converter = ImageToExcel(self.input_path.get())
            
            # 执行转换
            output_path = converter.convert_to_excel(
                output_path=self.output_path.get(),
                cell_width=self.cell_width.get(),
                cell_height=self.cell_height.get(),
                max_width=self.max_width.get(),
                max_height=self.max_height.get(),
                keep_ratio=self.keep_ratio.get(),
                sheet_name=self.sheet_name.get()
            )
            
            self.log_message(f"转换完成！输出文件: {output_path}")
            
            # 在主线程中更新UI
            self.root.after(0, self.conversion_completed, output_path)
            
        except Exception as e:
            error_msg = f"转换失败: {str(e)}"
            self.log_message(error_msg)
            self.root.after(0, self.conversion_failed, error_msg)
            
    def conversion_completed(self, output_path):
        """转换完成后的处理"""
        self.progress.stop()
        self.convert_btn.configure(state="normal")
        self.status_label.configure(text="转换完成！", foreground="green")
        
        # 询问是否打开文件
        if messagebox.askyesno("转换完成", f"图片已成功转换为Excel文件！\n\n是否打开文件？"):
            try:
                os.startfile(output_path)
            except:
                messagebox.showinfo("提示", f"文件已保存到:\n{output_path}")
                
    def conversion_failed(self, error_msg):
        """转换失败后的处理"""
        self.progress.stop()
        self.convert_btn.configure(state="normal")
        self.status_label.configure(text="转换失败", foreground="red")
        messagebox.showerror("转换失败", error_msg)
        
    def log_message(self, message):
        """添加日志消息"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # 在主线程中更新UI
        self.root.after(0, self._update_log, log_entry)
        
    def _update_log(self, log_entry):
        """更新日志显示"""
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        
    def clear_log(self):
        """清空日志"""
        self.log_text.delete(1.0, tk.END)
        
    def format_file_size(self, size_bytes):
        """格式化文件大小"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f} MB"


def main():
    """启动图形化界面"""
    root = tk.Tk()
    
    # 设置样式
    style = ttk.Style()
    style.theme_use('clam')
    
    # 创建主应用
    app = Img2ExcelGUI(root)
    
    # 启动主循环
    root.mainloop()


if __name__ == "__main__":
    main()
