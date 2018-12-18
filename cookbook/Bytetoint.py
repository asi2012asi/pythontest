#coding=utf8
'''将字节串和大整数相互转化'''

#要将一个大整数转化为字节串
x=1234567890987654321
y=x.to_bytes(16,'little')
print(y)

#将一个字节串转化成一个大整数
z=int.from_bytes(y,'little')
print(z)

a=523**23
print(a)
#使用下面这种方式会报错  OverflowError: int too big to convert 因为这个数值太大了 16个字节不能表达
# b=a.to_bytes(16,'little')

# 计算采用多少个字节才合适
nbytes,rem=divmod(a.bit_length(),8)
if rem :nbytes+=1
print(nbytes)
b=a.to_bytes(nbytes,'little')
print(b)

