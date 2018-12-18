#coding=utf8
'''复数运算'''

a=complex(1,2)
print(a.real)
print(a.imag)
print(a.conjugate())

b= 3-5j

#a b两个复数进行运算
print(a+b)
print(a*b)
print(a/b)
print(abs(a))

#要使用sin和cos等函数 可以引入cmath模块
import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))
print(cmath.sqrt(-1))
#使用一般无感知复数的模块 负数求平方根会直接报错 如下
import math
# print(math.sqrt(-1))

#numpy模块 可以直接创建复数数组
import numpy as ny
nyarr=ny.array([1+2j,2+3j,3+4j,4+5j])
print(nyarr)
print(nyarr+2)
print(ny.sin(nyarr))


