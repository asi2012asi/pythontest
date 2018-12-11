# coding=utf8
'''同时对数据进行转换和换算 先看几个例子'''

nums = [1, 2, 3, 4, 5, 6]

all = sum(x * x for x in nums)
print(all)
allstr=','.join(str(x) for x in nums)
print(allstr)
#以上都是尝试了将生成器表达式直接作为参数放进换算函数里 可以去掉里面的括号
all2=sum((x * x for x in nums))
#all和all2的效果是一样的
print(all2)