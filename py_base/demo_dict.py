adict = {"a": 1, "b": 2}

print("原始的", adict)

# 获取一个 kv
print(adict.get("a"))
# 获取一个不存在的 kv
print(adict.get("ab"))
# 获取一个不存在的 kv，且带默认值
print(adict.get("ab", False))
# 索引取值
print(adict["a"])
# KeyError: 'ab'
# print(adict["ab"])
print(adict["a"])

# 增加一个 kv
adict["c"] = 3
print("增加一个kv" , adict)
adict.update({"d": 4})
print("增加一个kv" , adict)

# 删除一个 kv
# 删除一个 存在的 kv
print(adict.pop("a"))
print("删除一个kv" , adict)

# 删除一个 不存在的 kv
print(adict.pop("ab", False))
print("删除一个不存在的 kv" , adict)

# 更新一个 kv
adict.update({"b": 5})
print("更新一个kv" , adict)

# 还有哪些常用的 dict 操作
#
print(adict.keys())
print(adict.values())
print(adict.items())
print(adict.get("a"))
print(adict.get("ab", False))
print(adict.clear())
print(adict)
