# -*- coding: UTF-8 -*-

def walk(name):
    return name,'walk'

def introduce(function,name):
    print 'Hi , ',function(name)

# f就是函数对象 然后把该函数对象作为参数传递给introduce方法
f = lambda name : 'i am '+name
introduce(f,'liming')
introduce(walk,"xiaohong")

# map函数有一个参数是函数对象

re = map((lambda x,y:x+y),[1,2,3],[3,4,5])
re1 = map((lambda x:x+1),[1,2,3])
print re,re1

fi = filter((lambda x:x<5),[2,10,5,6])
print fi

testreduce = reduce((lambda x,y:x*y),[2,4,6,8])
# 相当于 （（2*4）*6）*8
print testreduce