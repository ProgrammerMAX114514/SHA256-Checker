# hash checker
# encoding: utf-8
# LICENSE: MIT (See LICENSE file for more information)
from hshchkstdlib import *

# 主程序入口
if __name__ == "__main__":
    try:
        init()
        info(f"Type:{__name__}")
        info("You are running the main program.")
        info(f"----- Hash Checker {version} -----")
        while True:
            choice = ask_op()
            choice_handler(choice)
    except KeyboardInterrupt:
        warning("Program terminated by user.")
        info("Exiting...")
        exit(0)
    except Exception as e:
        error(f"An error occurred while running the program: {e.with_traceback(e.__traceback__)}")
        se(default_title, f"错误：一个错误在运行程序时发生：{e.with_traceback(e.__traceback__)}")
