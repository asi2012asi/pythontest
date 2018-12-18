#coding=utf8
'''包含对数值的一些处理'''

#对数值进行取整 round是四舍五入运算
from decimal import Decimal

print(round(1.374,2))
print(round(13456,-2))

#另外还有
print(format(1.374,'0.2f'))
print('value is {:0.2f}'.format(1.374))

#精确到小数的运算使用Decimal
a=1.4
b=2.1
print(a+b==3.5)
da=Decimal(a)
db=Decimal(b)
print(da+db==Decimal(3.5))

#可以要求数值输出时对齐
print(format(1.374,'^10.2f'))
#可以要求加上千位分隔符，
print('the value is {:0,.2f}'.format(123455555556.4567))

#也有旧式的使用%处理 这种方法无法添加千位分隔符
print('%10.2f'%1234.6789)

#把一个十进制数转换为二进制 八进制 16进制
x=1234
print(bin(x))
print(oct(x))
print(hex(x))

#将字符串行驶的整数转换为不同的进制
print(int('0xff',16))
print(int('100101',2))