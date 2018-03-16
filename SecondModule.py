# import FirstModule
import FirstModule as F
# from ThirdModule import doSomething
from ThirdModule import *


F.laugh()
doSomething()
watchSomething()
saySomething()
# print sumNumber(1,2,3,4)
# print sumNumber(2,4)
a = [1,2,3,4]
b = (4,5,6)
print sumNumber(*a)
print sumNumber(*b)

print sumRange(10)
# printScore(xiaoming=90,xiaohuang=80,xiaoli = 100)
di = {'zhangming':98,"jiaoshou":99,'chengzi':100}
# printScore(**di)
# printScore2(a) # we can't put dict in this container
# printNum2(*a)
c = zip(a,b)
# print c
# decompose
d, e = zip(*c)
print d,e

a = 5
b = a
a = a + 2
print a,b

L1 = [1,2,3]
L2 = L1
L1 = 1
print L1,L2

L1 = [1,2,3]
L2 = L1
L1[0] = 10
print L2

