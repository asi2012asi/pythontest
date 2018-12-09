# -*- coding: UTF-8 -*-

# 读取一个文件 按要求输出一些结果

f = open('record.txt','r')
content = f.readlines()

class Student(object):
    name = ""
    age = 0
    score = 0

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score



studentlist = list()
for line in content:
    if line.startswith('#'):continue
    elif line.startswith('\n'):continue
    else:
        stuArray = line.split(',')
        stu = Student(stuArray[0],stuArray[1],stuArray[2])
        studentlist.append(stu)

print studentlist

# 得分少于60的人有谁
for item in studentlist:
    if  int(item.score) < 60 :
        print item.name+" 's score is  < 60"

# 谁的名字以L开头
for item in studentlist:
    if str(item.name).startswith('L'):
        print item.name+" 's name is start with L"


# 所有人的总分是多少
allScore = 0
for item in studentlist:
    allScore = allScore+int(item.score)
print "all score is "+str(allScore)








