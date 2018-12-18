#coding=utf8
'''处理无穷大和Nan 我们需要对浮点数的无穷大 负无穷大 NaN(not a number)进行判断和处理'''

a=float('inf')
b=float('-inf')
c=float('nan')

print(a,b,c)

#判断一个数是否属于这些值 使用math模块
import math
print(math.isinf(a),math.isinf(b),math.isnan(c))

#无穷大会在数学计算中进行传播
print(a+45,a*3,10/a)

#某些特定的操作会导致未定义的行为产生nan的结果
print(a/a,a+b)

#nan会通过所有的操作进行传播
print(c+45,c/2,math.sqrt(c))

#nan在进行比较时 使用==是不会相等的
d=float('nan')
print(c,d,c==d,c is d)
#只能 使用math.isnan来比较
print(math.isnan(d)&math.isnan(c))


