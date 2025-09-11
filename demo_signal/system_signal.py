import signal
import time

# 处理 Ctrl+C 触发的 SIGINT 信号
# mac 下是 点击 STOP
def handle_int(signum, frame):
    print(f"接收到中断信号{signum}，退出程序, {frame}")
    exit(0)

signal.signal(signal.SIGINT, handle_int)  # 注册信号处理
while True:
    time.sleep(0.1)