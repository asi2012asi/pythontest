#coding=utf8
'''在序列中找出出现次数最多的元素'''
from collections import Counter

items=[1,2,1,1,2,3]
#对每个元素数数
wordsCount =Counter(items)
print(wordsCount)
#输出一个列表 每个item是一个元组 输出最多的两组
print(wordsCount.most_common(2))
#或者直接输出某一个元素的数量
print(wordsCount[1])
items2=[1,2,3]
#追加数量 再添加一些数据纳入统计
wordsCount.update(items2)
print(wordsCount[1])
#counter类型还可以直接进行数学运算 可相加或相减
wordsCount2=Counter(items2)
print(wordsCount+wordsCount2)
print(wordsCount-wordsCount2)
