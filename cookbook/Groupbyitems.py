#coding=utf8

'''根据字段将记录分组显示 使用内建的itertools.groupby比较方便 需要相对groupby的项进行排序'''
from operator import itemgetter

import itertools

items = [{'name': 'xiaoming', 'age': 20, 'scores': 99},
        {'name': 'xiaohua', 'age': 21, 'scores': 95},
        {'name': 'xiaoling', 'age': 20, 'scores': 95},
        {'name': 'xiaozhang', 'age': 18, 'scores': 94}
        ]

sortedItems = sorted(items,key=itemgetter('age'))
print(sortedItems)
groupbyItems =itertools.groupby(sortedItems,key=itemgetter('age'))
print(groupbyItems)
for age,items in groupbyItems:
    print(age)
    for item in items:
        print(' ',item)