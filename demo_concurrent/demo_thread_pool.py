import time
import threading
from demo_concurrent.thread_pool import ThreadPoolExecutorInstance

result = 0

def add():
    global result
    print(f"线程 {threading.current_thread().name} 正在执行")
    time.sleep(0.001)
    result = result + 1

# 100 个线程累加 result
with ThreadPoolExecutorInstance.GENERAL_POOL as executor:
    futures = []
    for i in range(1000):
        """
        支持的参数：
        - fn: 必需参数，要执行的函数/可调用对象
        - *args: 可变位置参数，传递给函数的位置参数
        - *kwargs: 可变关键字参数，传递给函数的关键字参数
        """
        future = executor.submit(add)
        futures.append(future)
    # 等待所有任务完成并累加结果
    for future in futures:
        future.result()

print(result)
