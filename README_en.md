英语(美国)/en_US
*Warning: This documentation is originally written in Simplified Chinese (Mainland China) and has been machinically translated. We cannot guarantee 100% accuracy of the translation.*
*警告：本文档原来是以简体中文（中国大陆）编写的，并经过机器翻译。我们无法保证翻译的100%准确性。*

# SHA256 Checker

This project provides both English and Chinese documentation. You can choose a language by clicking the language following button.
这个项目提供了英语和中文说明文档文档。你可以通过点击下面的语言按钮选择语言。

- [英语(美国)/en_US](README_en.md)
- [简体中文(中国大陆)/Simplified Chinese (Mainland China)](README.md)

## Introduction

This is a simple Python script tool that checks the hash values (SHA256) of files.

## Functions

- **File to file hash value verification**: Calculate the hash value of a file and compare it with the provided hash value.
- **File to file hash value verification**: Calculate the hash value of two files and compare their hash values.
- **Hash value to hash value verification**: Compare two hash values.
  
## Features

- **Hash value calculation**: Calculate the hash value of a file using the Python standard library `hashlib`.
- **Multi-format support**: Support case-insensitive hash value verification.
- **GUI interface**: Use the `tkinter` module to build a GUI interface, which is easy to use (even very bad, haha).

## Dependencies
- Python 3.x
- [hashlib](https://docs.python.org/3/library/hashlib.html): Python standard library, used to calculate hash values.
- [tkinter](https://docs.python.org/3/library/tkinter.html): Python standard library, used to build GUI interface.
- [tqdm](https://github.com/tqdm/tqdm): Non-official library, used to display progress bars.
- [logging](https://docs.python.org/3/library/logging.html): Python standard library, used to record logs.
- [rich](https://github.com/Textualize/rich): Non-official library, used to beautify output.
- Any Python 3.x environment **(Note: This project has only been tested on Windows 11 23H2 x64, and it is not guaranteed to be compatible with other systems).**

## Installation Guide

1. **Ensure Python 3.x is installed**. You can download and install it from [Python official website](https://www.python.org/downloads/).
2. Open the command line tool (Windows users can press `Win + R`, type `cmd` and press Enter).
3. Install the dependency libraries:
   Install the dependency libraries using pip:
   ```shell
   pip install hashlib tqdm rich logging
   ```
   For users in China, you can use the mirror source:
   ```shell
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple hashlib tqdm rich logging
   ```

### Usage Instructions
1. Clone this project to your local machine:
2. Enter the project directory:
3. Run the script:
   ```shell
   git clone https://github.com/ProgrammerMAX114514/SHA256-Checker.git
   cd SHA256-Checker
   python main.py
   ```
4. Follow the prompts to operate.
5. If you need to package, you can follow the following steps:
  1. Install the `pyinstaller` library:
      - Open the command line tool (Windows users can press `Win + R`, type `cmd` and press Enter).
      - Install the `pyinstaller` library:
        ```shell
        pip install pyinstaller
        ```
        - For users in China, you can use the mirror source:
        - ```shell
        pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
        ```
      - Note: You may need administrator privileges to install the `pyinstaller` library. The actual situation is different, please operate according to your actual situation.
  2. Package:
    ```shell
    pyinstaller --onefile main.py
    ```
