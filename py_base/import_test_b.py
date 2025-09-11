
class Demo:
    def __init__(self):
        # 如果是其他文件 import 当前文件则输出文件名：import_test_b
        # 如果是直接执行当前文件则输出文件名：__main__
        print(__name__)
        print("this is b class Demo")


demo = Demo()

if __name__ == '__main__':
    print(__name__)
    print("this is b")