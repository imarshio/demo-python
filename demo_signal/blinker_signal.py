import time

from blinker import signal

# 声明一个信号
demo_signal = signal('demo')


# @demo_signal.connect
def demo_handler(sender, **kwargs):
    """
    函数名 随意
    :param sender:
    :param kwargs:
    :return:
    """
    print('demo_handler:', sender, kwargs)

print("注册 signal")
demo_signal.connect(demo_handler)

time.sleep(1)
demo_signal.send('demo_signal')