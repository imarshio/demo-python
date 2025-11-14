# 元组解构
person = ("Alice", 30, "female")
name, age, gender = person
print(name)   # Alice
print(age)    # 30

# 列表解构
numbers = [10, 20, 30]
number_a, number_b, number_c = numbers
print(number_b)      # 20

# 用下划线 _ 忽略不需要的元素：
data = (1, 2, 3, 4, 5)
first, _, third, _, fifth = data
print(first, third, fifth)  # 1 3 5

# 提取首尾元素，中间元素打包成列表
values = [1, 2, 3, 4, 5]
first, *middle, last = values
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# 只取前两个元素，剩余元素打包
a, b, *rest = [10, 20, 30, 40]
print(rest)     # [30, 40]

user = {"name": "Bob", "age": 25, "city": "New York"}

# 提取键
k1, k2, k3 = user
print(k1, k2, k3)  # name age city

# 提取值
v1, v2, v3 = user.values()
print(v1)  # Bob

# 提取键值对（元组形式）
for k, v in user.items():
    print(f"{k}: {v}")


nested = [(1, 2), (3, 4), (5, 6)]
# 提取第二个元组的两个元素
_, (a, b), _ = nested
print(a, b)  # 3 4

# 更复杂的嵌套
data = [1, (2, 3), [4, 5]]
x, (y, z), [p, q] = data
print(y, q)  # 2 5


# 直接解构函数返回的多个值
def get_user():
    return "Charlie", 35, "male"

name, age, gender = get_user()
print(name)  # Charlie