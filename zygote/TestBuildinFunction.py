#coding=utf8

# 测试内置函数

#数学运算

print abs(-5)
print round(3.4444)
print cmp(3,4)
print divmod(9,2)
print pow(2,3)
print max((3,1,4))
print min(4,3,2)
print sum((4,3,2),1)


#类型转换
print int("4")
print float(3)
print long(3.4)
print str(23)
print complex(3,9)
print ord('A')
print chr(78)
print unichr(78)
print bool(0)

#将10进制转换成各种进制的字符串
print bin(33)
print hex(33)
print oct(33)

print list((3,4,2))
print tuple([4,3,2])
print slice(3,5,-1)
print dict(a=1,b='a',c="what?",d=4.3)

print all([1,'a',"dada",True])
print any([3,'fff',False])

print sorted([4,3.2,1,6,5])
a = reversed([4,3,1,6,5])
print list(a)






