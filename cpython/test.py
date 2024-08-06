# import sys
# # 原列表
# lst = []
# print(f"Dilatation list capacity: {sys.getsizeof(lst)} bytes")
# for i in range(100):
#     lst.append(i)
#
# # 扩容操作
# print(f"Original list capacity: {sys.getsizeof(lst)} bytes")
# # 缩容操作
# # 缩容操作
# lst = lst[:10]
# print(f"Shrunk list capacity: {sys.getsizeof(lst)} bytes")

import sys

d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}
d = {
        'name': 'abc', 'age': 1, 'c': 'c', '0': '0', '1': '1',
        # '2': '2',
        # '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
    }
d = {
        '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
}
# d = {}
print(len(d))
print(d.__sizeof__())
print(sys.getsizeof(d))

print({}.__sizeof__())

import sys

# 示例字典
d = {
    '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
}

# 计算字典对象的基础内存大小
dict_size = d.__sizeof__()
sys.getsizeof()
# 计算每个键值对的内存大小
key_value_sizes = [key.__sizeof__() + value.__sizeof__() for key, value in d.items()]

# 键值对总大小
total_key_value_size = sum(key_value_sizes)

# 总大小
total_size = dict_size + total_key_value_size

print(f"字典对象的基础大小: {dict_size} bytes")
print(f"键值对总大小: {total_key_value_size} bytes")
print(f"总内存使用量: {total_size} bytes")
