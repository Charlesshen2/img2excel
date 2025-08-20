# 🚀 GitHub 上传指南

## 📋 准备工作

### 1. 创建GitHub仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角 "+" 号，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**: `img2excel`
   - **Description**: `将任意图片转换为Excel像素画的Python工具`
   - **Visibility**: 选择 Public 或 Private
   - **不要**勾选 "Add a README file"（我们已经有了）
   - **不要**勾选 "Add .gitignore"（我们已经有了）
   - **不要**勾选 "Choose a license"（我们已经有了）
4. 点击 "Create repository"

### 2. 获取仓库URL

创建完成后，GitHub会显示仓库URL，类似：
```
https://github.com/yourusername/img2excel.git
```

## 🔗 连接本地仓库到GitHub

### 方法1：使用HTTPS（推荐新手）

```bash
# 添加远程仓库
git remote add origin https://github.com/yourusername/img2excel.git

# 验证远程仓库
git remote -v

# 推送代码到GitHub
git branch -M main
git push -u origin main
```

### 方法2：使用SSH（推荐有经验的用户）

```bash
# 添加SSH远程仓库
git remote add origin git@github.com:yourusername/img2excel.git

# 验证远程仓库
git remote -v

# 推送代码到GitHub
git branch -M main
git push -u origin main
```

## 📤 上传代码

### 首次上传

```bash
# 确保所有文件已提交
git status

# 如果有新文件，添加到暂存区
git add .

# 提交更改
git commit -m "更新项目：优化功能和文档"

# 推送到GitHub
git push origin main
```

### 后续更新

```bash
# 拉取最新更改（如果有协作）
git pull origin main

# 添加更改
git add .

# 提交更改
git commit -m "描述你的更改"

# 推送到GitHub
git push origin main
```

## 🔧 常见问题解决

### 问题1：认证失败

**错误信息**: `fatal: Authentication failed`

**解决方案**:
1. 使用个人访问令牌（推荐）
   - 进入 GitHub Settings → Developer settings → Personal access tokens
   - 生成新令牌，选择 repo 权限
   - 使用令牌作为密码

2. 或配置SSH密钥
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # 将公钥添加到GitHub账户
   ```

### 问题2：推送被拒绝

**错误信息**: `rejected: non-fast-forward`

**解决方案**:
```bash
# 强制推送（谨慎使用）
git push -f origin main

# 或先拉取再推送
git pull origin main
git push origin main
```

### 问题3：大文件上传失败

**解决方案**:
1. 检查 `.gitignore` 文件是否正确配置
2. 删除已提交的大文件：
   ```bash
   git rm --cached large_file.exe
   git commit -m "删除大文件"
   ```

## 📝 仓库设置建议

### 1. 仓库描述
在仓库页面点击 "About" 旁边的编辑按钮，添加：
```
🖼️ 图片转Excel像素画工具 | 支持多种格式，提供GUI和CLI界面
```

### 2. 主题标签
添加相关标签：
- `python`
- `image-processing`
- `excel`
- `pixel-art`
- `gui`
- `cli`

### 3. 仓库网站
如果使用GitHub Pages，可以设置仓库网站。

## 🌟 发布到PyPI（可选）

### 1. 构建包
```bash
# 安装构建工具
pip install build twine

# 构建包
python -m build
```

### 2. 上传到PyPI
```bash
# 测试上传
python -m twine upload --repository testpypi dist/*

# 正式上传
python -m twine upload dist/*
```

## 📚 后续维护

### 1. 定期更新
- 修复bug
- 添加新功能
- 更新依赖
- 改进文档

### 2. 版本管理
```bash
# 创建标签
git tag v1.0.0
git push origin v1.0.0

# 查看所有标签
git tag -l
```

### 3. 分支管理
```bash
# 创建功能分支
git checkout -b feature/new-feature

# 合并到主分支
git checkout main
git merge feature/new-feature
```

## 🎉 完成！

恭喜！您的img2excel项目已经成功上传到GitHub。

### 下一步建议：
1. 在README中添加项目徽章
2. 设置GitHub Actions进行自动化测试
3. 添加贡献指南
4. 创建发布说明
5. 推广您的项目

---

**需要帮助？** 请查看 [GitHub帮助文档](https://help.github.com/) 或提交Issue。
