try:
    from hashlib import sha256
    from rich.logging import RichHandler
    from rich import traceback, print
    from logging import basicConfig, INFO, info, warning, error, exception
    from tkinter.filedialog import askopenfilename
    from tkinter import Tk, scrolledtext, INSERT, WORD, Button, BOTTOM
    from tkinter.simpledialog import askstring
    from tkinter.messagebox import showinfo as si
    from tkinter.messagebox import showerror as se
    from _tkinter import TclError
    from sys import exit
    from time import sleep as s
except ImportError as e:
    print(f"An error occurred while importing modules: {e.with_traceback(e.__traceback__)}. Have you already installed all the required modules?")
    print("Modules may not be installed:")
    print("tqdm,logging,hashlib")
    print("Do you want to install these modules?(y/n)")
    print("Note: you need to have pip installed and network connection.")
    print("If you are in Great China, you can use tsinghua pip mirror.")
    print("To use tsinghua pip mirror, type 'y1'. To use default pip mirror, type 'y'.")
    install=input("Enter your choice:")
    if install.lower() == "y":
        print("Note: some modules' installation may need a reboot.")
        try:
            import pip
            pip.main(["install", "--upgrade", "pip"])
            pip.main(["install", "--upgrade", "tqdm"])
            pip.main(["install", "--upgrade", "hashlib"])
            pip.main(["install", "--upgrade", "logging"])
            pip.main(["install", "--upgrade","tkinter"])
            print("Installation completed. To apply the changes, restart the program.")
            exit(0)
        except Exception as e:
            print(f"An error occurred while installing modules: {e.with_traceback(e.__traceback__)}")
            exit(1)
    elif install.lower() == "y1":
        print("Note: some modules' installation may need a reboot.")
        try:
            import pip
            pip.main(["install", "--upgrade", "pip", "--index-url=https://mirror.tsinghua.edu.cn/pypi/web/simple"])
            pip.main(["install", "--upgrade", "hashlib", "--index-url=https://mirror.tsinghua.edu.cn/pypi/web/simple"])
            pip.main(["install", "--upgrade", "tkinter", "--index-url=https://mirror.tsinghua.edu.cn/pypi/web/simple"])
            pip.main(["install", "--upgrade", "tqdm", "--index-url=https://mirror.tsinghua.edu.cn/pypi/web/simple"])
            pip.main(["install", "--upgrade", "logging", "--index-url=https://mirror.tsinghua.edu.cn/pypi/web/simple"])
            print("Installation completed. To apply the changes, restart the program.")
            exit(0)
        except Exception as e:
            print(f"An error occurred while installing modules: {e.with_traceback(e.__traceback__)}")
            exit(1)

# 版本
version = "v0.3.0"

# 软件开源许可证(MIT License)
MIT_LICENSE = """MIT License

Copyright (c) 2024 ProgrammerMAX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

# 消息提示
default_title = f"哈希值校验工具 {version}"
info_hash_correct = f"哈希值正确。两个文件相同{' '*32}"
info_ask_hash = f"请输入哈希值{' '*128}"
error_file_not_chosen = f"错误：没有选择文件。{' '*32}"
error_hash_not_typed = f"错误：没有输入哈希值。{' '*32}"
error_hash_not_correct = "错误：哈希值错误。两个文件不相同。\n如果该文件来源于Internet下载，你的文件可能在传输过程中被篡改或因网络连接问题而损坏。"
error_type_error = "错误：输入错误，请重新输入。"

def on_agree():
    info("已同意软件开源许可协议。")
    root.quit()

def on_disagree():
    root.withdraw()
    root.quit()
    error("你已拒绝软件开源许可协议。程序即将退出。")
    se("拒绝","你已拒绝软件开源许可协议。程序即将退出。")
    exit(1)

# INIT
def init():
    global MIT_LICENSE, root
    basicConfig(level=INFO, format="%(asctime)s %(message)s", datefmt="[%Y-%m-%d %H:%M:%S]", handlers=[RichHandler()])
    info(f"Starting SHA256 Hash Checker version {version}")
    info("Intializing...")
    if "SNAPSHOT" in version:
        warning("This program is under development. Please do not use it in production environment.")
        warning("This program only supports sha256 hash check.")
        s(3)
    traceback.install(show_locals=True)
    info("Stage: intialize root window")
    root=Tk()
    root.geometry("600x450")
    root.resizable(False, False)
    root.title("软件开源许可协议")
    text_box=scrolledtext.ScrolledText(root, wrap=WORD)
    text_box.insert(INSERT, MIT_LICENSE)
    text_box.configure(state="disabled")
    text_box.pack(padx=10,pady=10)
    disagree_button = Button(root, text="我不同意", command=on_disagree)
    agree_button=Button(root,text="我同意",command=on_agree)
    agree_button.pack(side=BOTTOM, padx=(10, 5))
    disagree_button.pack(side=BOTTOM, padx=(5, 10))
    try:
        root.mainloop()
        info("Stage: hide root window")
        root.withdraw()
    except TclError:
        error("你已拒绝软件开源许可协议。程序即将退出。")
        se("拒绝","你已拒绝软件开源许可协议。程序即将退出。")
        exit(1)
    except Exception as e:
        exception(f"An error occurred while showing the license agreement: {e.with_traceback(e.__traceback__)}")
        se(f"An error occurred while showing the license agreement: {e.with_traceback(e.__traceback__)}")
        exit(-1)
    info("Stage: hide root window")
    root.withdraw()
    s(0.5)
    info("""This program is using the following modules:
    hashlib.
    └──sha256
    rich.
    ├── logging
    │   └── RichHandler
    ├── traceback
    └── print
    logging.
    ├── basicConfig
    ├── INFO
    ├── info
    ├── warning
    ├── exception
    └── error
    tkinter.
    ├── filedialog
    ├── Tk
    ├── INSERT
    ├── WORD
    ├── LEFT
    ├── Button
    ├── scrolledtext
    ├── simpledialog.
    │   └── askstring
    └── messagebox.
        ├── showinfo -> si
        └── showerror -> se
    _tkinter
    └── TclError 
    sys.
    └── exit
    time.
    └── sleep -> s""")
    s(3)
    info("Program started.")
    info("Initiation completed.")
    s(1)
    
# 获取选择
def ask_op():
    info("Asking for operation...")
    text = f"""请选择校验方式：
1.已知哈希值对文件/文件夹
2.已知哈希值对已知哈希值
3.文件对文件
9.退出
注意：该程序仍处于开发阶段，目前仅支持sha256校验。{' '*15}"""
    try:
        op = askstring(default_title, f"{text}\n请输入数字选择校验方式：{' '*15}")
    except Exception as e:
        exception(f"An error occurred while asking user's operation choice: {e.with_traceback(e.__traceback__)}")
        return None
    if op == "":
        op = "<empty>"
    info(f'GET OP: "{op}"')
    return op

# 打开文件
def open_file():
    info("Asking for file...")
    file_path = askopenfilename(title=f"{default_title} - 选择文件", filetypes=[("All Files", "*.*")])
    if file_path == "":
        file_path = "<empty>"
    info(f'GET FILE: "{file_path}"')
    return file_path

# 验证SHA256值有效性
def is_sha256(sha256):
    info("Checking SHA256...")
    if type(sha256) != str:
        return False
    if len(sha256) != 64:
        return False
    for char in sha256:
        if char not in "0123456789abcdefABCDEF":
            return False
    return True

# 检查SHA256值（文件对文件）
def check_sha256_f2f(file_1, file_2):
    info("Checking SHA256...(f2f)")
    try:
        with open(file_1, "rb") as f1, open(file_2, "rb") as f2:
            sha256_1 = sha256(f1.read()).hexdigest()
            if not is_sha256(sha256_1):
                info(f'Invalid SHA256 value "{sha256_1}". Please provide a correct SHA256 value.')
                se(default_title, "错误：无效的SHA256值。请提供正确的SHA256值。")
                return -1
            info(f'GET SHA2561: "{sha256_1}"')
            sha256_2 = sha256(f2.read()).hexdigest()
            if not is_sha256(sha256_2):
                info(f'Invalid SHA256 value "{sha256_2}". Please provide a correct SHA256 value.')
                se(default_title, "错误：无效的SHA256值。请提供正确的SHA256值。")
                return -1
            info(f'GET SHA2562: "{sha256_2}"')
            return sha256_1 == sha256_2
    except FileNotFoundError:
        error(f"File not found: {file_1} or {file_2}")
        se(default_title, f"错误：没有找到文件 {file_1} 或 {file_2}")
        return -1
    except PermissionError:
        error("Permission denied while accessing files.")
        se(default_title, "错误：文件拒绝访问。")
        return -1
    except IsADirectoryError:
        error("Invalid file path. Please provide a correct file path.")
        se(default_title, "错误：无效的文件路径。请提供正确的文件路径。")
        return -1
    except Exception as e:
        exception(f"An error occurred while checking the SHA256 value: {e.with_traceback(e.__traceback__)}")
        se(default_title, f"错误：一个错误在检查SHA256值时发生：{e.with_traceback(e.__traceback__)}")
        return -1
# 检查SHA256值（文件对已知哈希值）
def check_sha256_f2h(file, hash):
    try:
        info("Checking SHA256...(f2h)")
        with open(file, "rb") as f:
            _hash = sha256(f.read()).hexdigest()
            info(f'GET SHA256 from file "{f}": "{sha256}"')
            return _hash == hash
    except FileNotFoundError:
        error(f'File not found: "{file}"')
        se(default_title, f'错误：没有找到文件 "{file}"')
        return -1
    except PermissionError:
        error("Permission denied while accessing files.")
        se(default_title, "错误：文件拒绝访问。")
        return False
    except IsADirectoryError:
        error("Invalid file path. Please provide a correct file path.")
        se(default_title, "错误：无效的文件路径。请提供正确的文件路径。")
        return False
    except Exception as e:
        exception(f'An error occurred while checking the SHA256 value: "{e.with_traceback(e.__traceback__)}"')
        se(default_title, f'错误：一个错误在检查SHA256值时发生："{e.with_traceback(e.__traceback__)}"')
        return False
# 检查SHA256值（已知哈希值对已知哈希值）
def check_sha256_h2h(hash_1, hash_2):
    try:
        info("Checking SHA256...(h2h)")
        return hash_1.lower() == hash_2.lower()
    except Exception as e:
        exception(f"An error occurred while checking the SHA256 value: {e.with_traceback(e.__traceback__)}")
        se(default_title, f"错误：一个错误在检查SHA256值时发生：{e.with_traceback(e.__traceback__)}")
        return False
# choice=1
def choice_1():
    file_path = open_file()
    if file_path == "<empty>":
        warning("GET file path: <empty>")
        warning("File path is empty. Skipped sha256 check.")
        se(default_title, error_file_not_chosen)
        return
    info(f"GET file path: {file_path}")
    hash_value = askstring(default_title, info_ask_hash)
    if not is_sha256(hash_value):
        info(f'Invalid SHA256 value "{hash_value}". Please provide a correct SHA256 value.')
        se(default_title, "错误：无效的SHA256值。请提供正确的SHA256值。")
        return
    if hash_value == "" or hash_value is None:
        warning("GET hash value: <empty>")
        warning("Hash value is empty. Skipped sha256 check.")
        se(default_title, error_hash_not_typed)
        return
    info(f"GET hash value: {hash_value}")
    if check_sha256_f2h(file_path, hash_value) == -1:
        return
    elif check_sha256_f2h(file_path, hash_value):
        info("Hash value is correct. Two files are same.")
        si(default_title, info_hash_correct)
    else:
        info("Hash value is incorrect. Two files are not same.")
        se(default_title, error_hash_not_correct)

# choice=2
def choice_2():
    hash_1 = askstring(default_title, f"请输入第一个文件的哈希值：{' '*128}")
    if hash_1 == "" or hash_1 is None:
        warning("GET hash 1: <empty>")
        warning("Hash 1 is empty. Skipped sha256 check.")
        se(default_title, error_hash_not_typed)
        return
    info(f"GET hash 1 = {hash_1}")
    hash_2 = askstring(default_title, f"请输入第二个文件的哈希值：{' '*128}")
    if hash_2 == "" or hash_2 is None:
        warning("GET hash 2: <empty>")
        warning("Hash 2 is empty. Skipped sha256 check.")
        se(default_title, error_hash_not_typed)
        return
    info(f"GET hash 2 = {hash_2}")
    if check_sha256_h2h(hash_1, hash_2):
        info("Hash value is correct. Two files are same.")
        si(default_title, info_hash_correct)
    else:
        info("Hash value is incorrect. Two files are not same.")
        se(default_title, error_hash_not_correct)

# choice_3
def choice_3():
    file_1 = askopenfilename(title=f"{default_title} - 选择第一个文件", filetypes=[("All Files", "*.*")])
    if file_1 == "":
        warning("GET file 1: <empty>")
        warning("File 1 is empty. Skipped sha256 check.")
        se(default_title, error_file_not_chosen)
        return
    info(f"GET FILE 1: {file_1}")
    file_2 = askopenfilename(title=f"{default_title} - 选择第二个文件", filetypes=[("All Files", "*.*")])
    if file_2 == "":
        warning("GET file 2: <empty>")
        warning("File 2 is empty. Skipped sha256 check.")
        se(default_title, error_file_not_chosen)
        return
    info(f"GET FILE 2: {file_2}")
    if check_sha256_f2h(file_1, hash) == -1:
        return
    elif check_sha256_f2f(file_1, file_2):
        info("Hash value is correct. Two files are same.")
        si(default_title,info_hash_correct)
    else:
        info("Hash value is incorrect. Two files are not same.")
        se(default_title, error_hash_not_correct)

# 处理用户选择
def choice_handler(choice):
    try:
        if choice == "1":
            choice_1()
        elif choice == "2":
            choice_2()
        elif choice == "3":
            choice_3()
        elif choice == "9" or choice == None:
            info("Exiting...")
            exit(0)
        else:
            info(f"Input error:{choice}")
            se(default_title, error_type_error)
    except Exception as e:
        exception(f"An error occurred while handling the user's choice {choice}: {e.with_traceback(e.__traceback__)}")
        se(default_title, f"错误：一个错误发生在处理用户的请求 {choice} 时发生: {e.with_traceback(e.__traceback__)}")

def demo():
    choice=ask_op()
    choice_handler(choice)

if __name__ == "__main__":
    try:
        init()
        info(f"Type:{__name__}")
        warning("You are running the Hash Checker Standard Library.")
        info(f"----- Hash Checker (hskchkstdlib.py) {version} -----")
        warning("This file CAN NOT be executed directly.")
        warning("But you still executed it. Would you like to watch a demo ?(y/n)")
        if (input()).lower() == "y":
            info("Launching demo...")
            demo()
            info("Exiting...")
            exit(0)
        else:
            info("Exiting...")
            exit(1)
    except KeyboardInterrupt as e:
        warning("Program terminated by user.")
        info("Exiting...")
        exit(0)
    except Exception as e:
        exception(f"An error occurred while running the program: {e.with_traceback(e.__traceback__)}")
        se(default_title, f"An error occurred while running tge program: {e.with_traceback(e.__traceback__)}")        
