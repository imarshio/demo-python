import importlib

# 当引入另外一个 py 文件时，相当于把另外一个文件的代码放到这里，然后运行
import import_test_b

if __name__ == '__main__':
    print(__name__)
    # __main__ 这段代码只有在直接运行该文件时才会执行
    print("this is a")
    importlib.import_module("import_test_b")