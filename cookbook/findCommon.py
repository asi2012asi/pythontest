# coding=utf8
'''查找两个词典中的相同点'''

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 0, 'x': 1, 'y': 2}

# 找到两个词典中都有的key
commonKeys = a.keys() & b.keys()
print(commonKeys)

# 在a中找b不包含的key
otherKeys = a.keys() - b.keys()
print(otherKeys)

# 在ab中找共有的item
commonItems = a.items() & b.items()
print(commonItems)

#创建一个词典 从a中去掉key为z和w的
c = {key: a[key] for key in a.keys() - {'z','w'}}
print(c)

# 下面这种方式会报TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'
# 因为不能保证值是唯一的
# commonValues= a.values() & b.values()
# print(commonValues)
