class Counter:
    # 静态变量
    """
    python 严格意义上来说是没有静态变量这个概念的
    """
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Counter.count)
Counter.increment()
print(Counter.count)
Counter.increment()
print(Counter.count)
