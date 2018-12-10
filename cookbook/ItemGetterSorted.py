# coding=utf8
'''通过公共键对字典列表排序 主要是利用operator里的itemgetter进行排序'''
from operator import itemgetter

rows = [{'name': 'xiaoming', 'age': 20, 'scores': 99},
        {'name': 'xiaohua', 'age': 21, 'scores': 95},
        {'name': 'xiaoling', 'age': 19, 'scores': 95},
        {'name': 'xiaozhang', 'age': 18, 'scores': 94}
        ]

# 对age或者scores进行排序 运用sorted 传递一个可迭代对象和一个名为key的callable
# 可以使用lambda的方式
newrows = sorted(rows, key=lambda item: item['scores'])
print(newrows)
# 或者可以使用operator里的itemgetter进行排序 运行更快
newrows2 = sorted(rows, key=itemgetter('scores'))
print(newrows2)
# 对两个数值进行排序
newrows3 = sorted(rows, key=itemgetter('scores', 'age'))
print(newrows3)

#同样不单只sorted适用 min和max也适用
print(max(rows,key=itemgetter('age')))
print(min(rows,key=itemgetter('scores')))
