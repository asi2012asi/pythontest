# coding=utf8
'''筛选序列中的元素 有几种做法 第一种是列表推导式 第二种是生成器 第三种是使用filter函数'''
import itertools

mylist = [-1, 3, -4, 5, 6, -7, 8, 9]

# 第一种 列表推导式 筛选出大于0的整数
first = [n for n in mylist if n > 0]
print(first)

# 第二种 生成器
second = (n for n in mylist if n > 0)
print(second)
# print(list(second))
#注意 生成器只可以使用一次 如果上面注释打开了 下面就不会输出数据了
for n in second:
    print(n)

# 第三种 filter函数
third=list(filter(lambda n:n>0,mylist))
print(third)

#如果想把不满足条件的值替换掉 一样可以使用推导式 例如将<0的数替换成0
mylist2=[n if n>0 else 0 for n in mylist]
print(mylist2)

#另一个筛选工具 itertools.compress 可以接受一个可迭代对象和一个布尔值序列 筛选出对应布尔值为true的元素
#compress专门用在把一个序列的筛选结果施加到另一个序列上
names=list('abcdefg')
print(names)
boolresult= [n>0 for n in mylist]
print(boolresult)
result = itertools.compress(names,boolresult)
print(result)
print(list(result))