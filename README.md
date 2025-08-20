# 🖼️ img2excel - 图片转Excel像素画工具

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-img2excel-blue.svg)](https://pypi.org/project/img2excel/)

一个功能强大的Python工具，可以将任意图片转换为Excel像素画，支持多种图片格式和自定义参数设置。无论是创建像素艺术、制作Excel图表背景，还是进行图片分析，这个工具都能满足您的需求。

## ✨ 主要特性

- 🖼️ **多格式支持** - 支持JPG、PNG、BMP、GIF、TIFF、WebP等主流图片格式
- 📏 **智能尺寸控制** - 自动保持原图片比例，支持自定义最大尺寸
- 🎨 **像素级渲染** - 通过改变Excel单元格颜色精确还原图片
- 🖥️ **图形化界面** - 直观易用的GUI界面，支持实时预览
- 💻 **命令行工具** - 强大的CLI工具，支持批量处理和脚本自动化
- 🐍 **Python API** - 完整的编程接口，易于集成到其他项目中
- ⚡ **高性能** - 优化的算法，快速处理大尺寸图片
- 🔧 **高度可定制** - 支持自定义单元格尺寸、工作表名称等参数

## 🚀 快速开始

### 安装

#### 从PyPI安装（推荐）

```bash
pip install img2excel
```

#### 从源码安装

```bash
git clone https://github.com/yourusername/img2excel.git
cd img2excel
pip install -e .
```

### 图形化界面使用（推荐新手）

```bash
# 方法1：直接运行
python -m img2excel.gui

# 方法2：安装后使用
img2excel-gui
```

### 命令行使用

```bash
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
```

### Python API使用

```python
from img2excel import ImageToExcel

# 创建转换器
converter = ImageToExcel("input.jpg")

# 基本转换，保持原比例，最大宽度100个单元格
output_path = converter.convert_to_excel(
    output_path="output.xlsx",
    max_width=100,
    keep_ratio=True
)

# 自定义单元格尺寸
output_path = converter.convert_to_excel(
    output_path="output_custom.xlsx",
    max_width=50,
    cell_width=20,  # 20像素宽
    cell_height=20,  # 20像素高
    keep_ratio=True
)

# 强制指定尺寸，不保持比例
output_path = converter.convert_to_excel(
    output_path="output_forced.xlsx",
    max_width=80,
    max_height=60,
    keep_ratio=False
)
```

## 📖 详细使用说明

### 图形化界面功能

图形化界面提供以下功能：

- **图片选择和预览** - 支持拖拽操作，实时显示图片信息
- **参数设置面板** - 直观的参数调整界面
- **实时预览** - 显示转换后的尺寸和单元格数量
- **进度显示** - 实时转换进度和状态提示
- **日志记录** - 详细的转换过程记录
- **智能建议** - 根据图片尺寸自动推荐参数

### 命令行参数详解

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `input_file` | 输入图片文件路径 | 必需 | `photo.jpg` |
| `output_file` | 输出Excel文件路径 | 必需 | `output.xlsx` |
| `--max-width` | 最大宽度（单元格数量） | 100 | `--max-width 150` |
| `--max-height` | 最大高度（单元格数量） | 100 | `--max-height 80` |
| `--cell-width` | 单元格宽度（像素） | 20 | `--cell-width 30` |
| `--cell-height` | 单元格高度（像素） | 20 | `--cell-height 30` |
| `--no-ratio` | 不保持原图片比例 | False | `--no-ratio` |
| `--sheet-name` | Excel工作表名称 | "PixelArt" | `--sheet-name "MyArt"` |
| `--preview` | 仅预览，不生成文件 | False | `--preview` |

### Python API参数说明

#### ImageToExcel类

**初始化参数：**
- `image_path` (str): 图片文件路径

**convert_to_excel方法参数：**
- `output_path` (str): 输出Excel文件路径
- `cell_width` (int, 可选): 单元格宽度（像素），默认20
- `cell_height` (int, 可选): 单元格高度（像素），默认20
- `max_width` (int, 可选): 最大宽度（单元格数量）
- `max_height` (int, 可选): 最大高度（单元格数量）
- `keep_ratio` (bool): 是否保持原图片比例，默认True
- `sheet_name` (str): Excel工作表名称，默认"PixelArt"

## 🎯 使用场景

### 1. 像素艺术创作
- 将手绘图片转换为像素风格
- 创建复古游戏风格的图像
- 制作像素画模板

### 2. Excel美化
- 为Excel表格添加背景图片
- 创建独特的图表背景
- 制作个性化的Excel模板

### 3. 图片分析
- 分析图片的颜色分布
- 研究图片的像素结构
- 进行图片质量评估

### 4. 教育和演示
- 教学图片处理原理
- 演示像素化效果
- 展示图像压缩概念

## 📊 尺寸计算逻辑

### 保持比例模式（默认）

1. **只指定宽度**：高度按原图片比例自动计算
2. **只指定高度**：宽度按原图片比例自动计算
3. **同时指定宽高**：选择较小的缩放比例，确保不超出限制

### 不保持比例模式

- 直接使用指定的尺寸
- 可能导致图片变形
- 适用于需要特定尺寸的场景

### 单元格尺寸设置

- `cell_width` 和 `cell_height` 控制每个单元格的物理尺寸
- 单位：像素
- 影响最终Excel文件的大小和显示效果

## 🔧 高级用法

### 批量处理

```python
import os
from img2excel import ImageToExcel

def batch_convert(input_dir, output_dir, max_width=100):
    """批量转换图片"""
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.png', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.xlsx")
            
            try:
                converter = ImageToExcel(input_path)
                converter.convert_to_excel(output_path, max_width=max_width)
                print(f"✓ {filename} 转换成功")
            except Exception as e:
                print(f"✗ {filename} 转换失败: {e}")

# 使用示例
batch_convert("input_images/", "output_excel/", max_width=80)
```

### 自定义颜色映射

```python
from img2excel import ImageToExcel
from img2excel.utils import rgb_to_hex

class CustomImageToExcel(ImageToExcel):
    def _render_image_to_excel(self, image):
        """自定义渲染逻辑"""
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixel = image.getpixel((x, y))
                # 自定义颜色处理逻辑
                hex_color = self._custom_color_mapping(pixel)
                cell = self.worksheet.cell(row=y+1, column=x+1)
                cell.fill = PatternFill(start_color=hex_color, end_color=hex_color, fill_type="solid")
    
    def _custom_color_mapping(self, pixel):
        """自定义颜色映射"""
        r, g, b = pixel
        # 例如：增强对比度
        r = min(255, int(r * 1.2))
        g = min(255, int(g * 1.2))
        b = min(255, int(b * 1.2))
        return rgb_to_hex(r, g, b)
```

## 📋 系统要求

- **Python版本**: 3.7 或更高版本
- **操作系统**: Windows、macOS、Linux
- **内存**: 建议至少512MB可用内存
- **存储**: 根据图片大小，建议至少100MB可用空间

## 📦 依赖包

- **Pillow (PIL)** >= 8.0.0 - 图片处理核心库
- **openpyxl** >= 3.0.0 - Excel文件操作库

### 可选依赖

- **tkinter** - GUI界面（Python标准库，通常已预装）
- **pytest** - 测试框架（开发时使用）

## 🚀 性能优化建议

### 1. 图片尺寸控制
- 对于大图片，建议设置合理的`max_width`和`max_height`
- 通常100x100的单元格数量已经足够清晰

### 2. 单元格尺寸优化
- 较小的单元格尺寸（如10x10像素）适合精细效果
- 较大的单元格尺寸（如30x30像素）适合快速预览

### 3. 批量处理
- 使用Python API进行批量处理，避免重复启动程序
- 考虑使用多线程处理大量图片

## 🐛 常见问题

### Q: 转换后的Excel文件很大怎么办？
**A**: 可以通过以下方式减小文件大小：
- 减少`max_width`和`max_height`的值
- 增加`cell_width`和`cell_height`的值
- 使用压缩的图片格式（如JPG）

### Q: 如何保持图片清晰度？
**A**: 提高清晰度的方法：
- 增加`max_width`和`max_height`的值
- 减小`cell_width`和`cell_height`的值
- 使用高质量的源图片

### Q: 支持批量转换吗？
**A**: 是的！可以通过以下方式实现：
- 使用Python API编写批量处理脚本
- 使用命令行工具配合批处理脚本
- 在GUI中逐个处理多张图片

### Q: 可以转换透明背景的图片吗？
**A**: 透明背景会被转换为白色背景，因为Excel不支持透明度。如果需要保持透明效果，建议：
- 使用白色或浅色背景的图片
- 在转换前处理透明区域

### Q: 转换速度慢怎么办？
**A**: 提高转换速度的方法：
- 减少目标尺寸（`max_width`和`max_height`）
- 增加单元格尺寸（`cell_width`和`cell_height`）
- 使用SSD存储设备
- 确保有足够的内存

## 🤝 贡献指南

我们欢迎所有形式的贡献！如果您想为项目做出贡献，请：

1. **Fork** 这个仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 **Pull Request**

### 贡献类型

- 🐛 **Bug报告** - 提交Issue描述问题
- 💡 **功能建议** - 提出新功能想法
- 📝 **文档改进** - 改进README、注释等
- 🔧 **代码优化** - 性能优化、代码重构
- 🧪 **测试用例** - 添加测试、提高覆盖率

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- **项目地址**: https://github.com/yourusername/img2excel
- **问题反馈**: https://github.com/yourusername/img2excel/issues
- **邮箱**: your.email@example.com

## 🙏 致谢

感谢以下开源项目：
- [Pillow](https://python-pillow.org/) - 强大的图像处理库
- [openpyxl](https://openpyxl.readthedocs.io/) - Excel文件操作库
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Python标准GUI库

---

**⭐ 如果这个项目对您有帮助，请给我们一个星标！**

**🔄 项目持续更新中，欢迎关注最新版本！**
