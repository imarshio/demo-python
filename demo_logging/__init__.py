# python import 的行为是：加载被应用的 python 文件并执行
import logging
# 由于 logging 是单例模式，整个程序运行期间只会有一个实例
# 所以如下配置影响的是整个 python 进程，除非子模块有更详细的配置
# logging 的默认日子级别是 Warning
logging.basicConfig(level=logging.INFO)
import self_logger

print("hello world")