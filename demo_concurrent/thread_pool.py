import threading
from enum import Enum
from concurrent.futures import ThreadPoolExecutor


class ThreadPoolExecutorInstance(Enum):
    """线程池执行器实例枚举"""

    # 前缀，核心线程数，最大线程数，线程存活时间（秒）
    UPLOAD_FILE_POOL = ("upload_file", 5, 40, 10 * 60)
    GENERAL_POOL = ("general_", 5, 10, 10 * 60)

    def __init__(
        self, pool_name: str, core_threads: int, max_threads: int, keep_alive: int
    ):
        self.pool_name = pool_name
        self.core_threads = core_threads
        self.max_threads = max_threads
        self.keep_alive = keep_alive
        self._executor = None
        # 保护executor创建和状态的锁
        self._lock = threading.Lock()
        # 引用计数器
        self._ref_count = 0
        self._ref_lock = threading.Lock()
        # 自定义状态：是否已关闭（初始为True，因未创建）
        self._is_shutdown = True

    @property
    def executor(self) -> ThreadPoolExecutor:
        """获取线程池执行器（单例模式）"""
        # 用自定义的_is_shutdown判断状态，而非依赖内部属性
        if self._executor is None or self._is_shutdown:
            with self._lock:
                if self._executor is None or self._is_shutdown:
                    self._executor = ThreadPoolExecutor(
                        max_workers=self.max_threads,
                        thread_name_prefix=self.pool_name,
                    )
                    # 创建后标记为未关闭
                    self._is_shutdown = False
        return self._executor

    def __enter__(self):
        with self._ref_lock:
            self._ref_count += 1
        return self.executor

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self._ref_lock:
            self._ref_count -= 1
            if self._ref_count <= 0:
                self._ref_count = 0
                self.shutdown()

    def shutdown(self):
        """关闭线程池并更新自定义状态"""
        # 先判断是否需要关闭（未关闭且存在executor）
        if not self._is_shutdown and self._executor is not None:
            with self._lock:
                if not self._is_shutdown and self._executor is not None:
                    # 不等待任务完成
                    self._executor.shutdown(wait=True)
                    # 标记为已关闭
                    self._is_shutdown = True
                    # 释放引用
                    self._executor = None
