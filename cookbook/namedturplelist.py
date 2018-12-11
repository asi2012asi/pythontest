# coding=utf8
'''元组的一般访问方式是使用下标 可以通过名称的方式来访问这些元素'''
from collections import namedtuple

scoreTuple = (('xiaoming', 21, 95), ('xiaolong', 20, 90), ('xiaohong', 18, 92))

# c3班的成绩单 将数据元组命名为c3class
c3class = namedtuple('c3class', ['name', 'age', 'scoreNum'])
tongxue1 = c3class('xiaoming', 21, 95)
print(tongxue1)
print(tongxue1.name)
# tongxue1看起来像个类实例 他与普通元组是可以互换的 而且支持所有元组支持的操作如索引和分解
stuname, stuage, stuscore = tongxue1
print(stuage)

# 命名元组与词典很相似 但是前者的存储空间更少

totalscore=0
for stu in scoreTuple:
    tongxue = c3class(*stu)
    totalscore += tongxue.scoreNum
print(totalscore)

#命名元组有个_replace方法用来修改元组内某些元素 创建一个新的元组
#将某个人的成绩改为100
tongxue1=tongxue1._replace(scoreNum=100)
print(tongxue1)