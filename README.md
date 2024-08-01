# 哈希值校验工具 - SHA256 Checker

## 简介
这是一个简单的Python脚本工具，用于检查文件的哈希值（SHA256）是否正确。

## 功能

- **文件对文件哈希值校验**：通过计算文件的哈希值，并比较与提供的哈希值是否一致。
- **文件对文件哈希值校验**：通过计算两个文件的哈希值，并比较它们的哈希值是否一致。
- **哈希值对哈希值校验**：比较两个哈希值是否一致。

## 特性
- **哈希值计算**：通过Python标准库`hashlib`计算文件的哈希值。
- **多格式支持**：支持大小写不同的哈希值校验。
- **GUI界面**：使用`tkinter`模块构建GUI界面，方便用户操作（即使很垃圾，哈哈）。
  
## 依赖
- Python 3.x
- [hashlib](https://docs.python.org/3/library/hashlib.html)：Python标准库，用于计算哈希值。
- [tkinter](https://docs.python.org/3/library/tkinter.html)：Python标准库，用于构建GUI界面。
- [tqdm](https://github.com/tqdm/tqdm)：非官方库，用于显示进度条。
- [logging](https://docs.python.org/3/library/logging.html)：Python标准库，用于记录日志。
- [rich](https://github.com/Textualize/rich)：非官方库，用于美化输出。
- 任意具有Python 3.x的运行环境（注意：该项目只在Windows 11 23H2 x64环境下测试过，不保证对其它系统的兼容性）。

## 安装指南

1. **确保Python 3.x已安装**。可以在[Python官网](https://www.python.org/downloads/)下载安装。
2. 打开命令行工具（Windows用户可以按`Win + R`，输入`cmd`后回车）。
3. 安装依赖库：
   使用`pip`安装依赖库：
   ```shell
   pip install hashlib tqdm rich logging
   ```
   国内用户可以使用镜像源：
   ```shell
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple hashlib tqdm rich logging
   ```

### 使用说明
1. 将本项目克隆到本地：
2. 进入项目目录：
3. 运行脚本：
   ```shell
   git clone https://github.com/ProgrammerMAX114514/SHA256-Checker.git
   cd SHA256-Checker
   python main.py
   ```
4. 按照提示操作即可。
5. 若需要打包，可按照以下步骤：
   1. 安装`pyinstaller`库：
      1.打开命令行工具（Windows用户可以按`Win + R`，输入`cmd`后回车）。
      2.安装`pyinstaller`库：
      ```shell
      pip install pyinstaller
      ```
      国内用户可以使用镜像源：
      ```shell
      pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
      ```
   2. 打包：
      ```shell
      pyinstaller --onefile main.py
      ```
