#coding=utf8
'''将多个词典或映射 合并成一个单独的映射结构'''
from collections import ChainMap

a={'x':1,'y':2}
b={'y':3,'z':4}

mymap=ChainMap(a,b)
print(list(mymap.keys()))
print(list(mymap.values()))
print(mymap['x'])
#使用ChainMap后获取到的是如果在第一个字典中找到 就不去第二个中拿了
print(mymap['y'])
print(mymap)
#修改映射都会作用在第一个字典中
a['w']=5
del mymap['y']
print(mymap)
# 注意下面会出错 因为第一个词典中找不到z这个key
# del mymap['z']

#ChainMap可以创建自己的child
c2=ChainMap()
c2['x']=1
c2=c2.new_child()
c2['x']=2
c2=c2.new_child()
c2['x']=3
print(c2)
#新添加的child在最前面
print(c2['x'])

#对原字典的修改 会影响chainmap后的词典 因为chainmap使用的是原始字典
a['x']=1000
print(mymap)

#另外一种方式 使用update 会创建新的字典 原字典的修改不会影响update后的词典
merged=dict(b)
merged.update(a)
print(merged)
a['y']=-1
print(merged)