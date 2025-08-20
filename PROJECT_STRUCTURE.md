# 📁 img2excel 项目结构说明

## 🗂️ 目录结构

```
img2excel/
├── README.md                    # 项目主要说明文档
├── LICENSE                      # MIT许可证文件
├── requirements.txt             # 项目依赖包列表
├── run_gui.py                  # GUI启动脚本
├── PROJECT_STRUCTURE.md        # 项目结构说明（本文档）
├── img2excel/                  # 核心Python包
│   ├── __init__.py            # 包初始化文件
│   ├── core.py                # 图片转换核心逻辑
│   ├── utils.py               # 工具函数和辅助方法
│   ├── gui.py                 # 图形界面主模块
│   ├── cli.py                 # 命令行界面
│   └── pyproject.toml         # 现代Python项目配置
└── img2excel_gui/             # 已废弃的GUI文件夹（可删除）
    └── ...                    # 旧版本文件
```

## 🚀 核心文件说明

### 主要脚本
- **`run_gui.py`** - GUI启动脚本，推荐使用
- **`img2excel/__init__.py`** - 包初始化文件

### 核心模块
- **`img2excel/core.py`** - 图片转换核心逻辑
- **`img2excel/utils.py`** - 工具函数库
- **`img2excel/gui.py`** - 图形界面主模块
- **`img2excel/cli.py`** - 命令行接口

### 配置文件
- **`pyproject.toml`** - 现代Python项目配置
- **`requirements.txt`** - 依赖包列表

## 🔧 使用方法

### 运行图形界面
```bash
# 方法1：直接运行启动脚本
python run_gui.py

# 方法2：作为模块运行
python -m img2excel.gui
```

### 安装为Python包
```bash
# 开发模式安装
pip install -e .

# 从PyPI安装
pip install img2excel
```

### 命令行使用
```bash
# 安装后使用
img2excel input.jpg output.xlsx

# 或作为模块运行
python -m img2excel.cli input.jpg output.xlsx
```

## 📚 项目特点

- **模块化设计** - 核心功能、GUI、CLI分离
- **易于维护** - 清晰的代码结构和文档
- **跨平台支持** - Windows、macOS、Linux
- **多种使用方式** - GUI、CLI、Python API

## 🔄 更新说明

本项目已重新整理，主要变化：
1. 删除了冗余的演示和测试文件
2. 简化了配置文件
3. 整合了GUI相关代码
4. 优化了项目结构
5. 完善了中文文档

---

**注意**：`img2excel_gui` 文件夹中的文件已废弃，建议删除。
