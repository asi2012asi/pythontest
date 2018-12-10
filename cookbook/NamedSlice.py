#coding=utf8
'''对切片命名 对弈切片的索引值从硬编码改为命名的'''

items=[1,2,3,4,5]
#对整个切片进行重命名
a=slice(2,3,1)
selected=items[a]
print(selected)
#删除切片元素
del items[a]
print(items)
print(a.start,a.stop,a.step)