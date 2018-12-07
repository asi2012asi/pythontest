# -*- coding: utf-8 -*-

'任何模块代码的第一个字符串都被视为模块的文档注释'
from operator import itemgetter

students = [("Bob",75),("Adam",92),("Lisa",88)]
print (type(students))
print (sorted(students,key=itemgetter(0)))
print (sorted(students,key=itemgetter(0),reverse=True))
print (sorted(students,key=itemgetter(1)))
print (sorted(students,key=lambda t:t[1])) #t[1]表示匿名函数只返回第一个数
mydict = dict(students)
print (type(mydict),mydict)
print (__doc__)