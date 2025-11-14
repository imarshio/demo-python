from random import random

from tqdm import tqdm
from tqdm.contrib.concurrent import thread_map
import time

# 基本用法
# for i in tqdm(range(100)):
#     # 模拟耗时操作
#     time.sleep(random())


# 并发
"""
leadve: 控制任务完成后进度条是否保留。True 表示任务结束后进度条会留在控制台 / 输出中，False 则会被清除。
dynamic_ncols: 动态调整进度条宽度。根据终端 / 输出窗口的宽度自动适配进度条长度，避免在窄窗口中显示错乱。
"""
thread_map(lambda x: time.sleep(random()), range(100), max_workers=10, desc='模拟下载', unit="item", leave=True, dynamic_ncols=True)