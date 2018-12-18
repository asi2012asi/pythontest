# coding=utf8
''' 利用shell通配符做字符串匹配'''
import os
from fnmatch import fnmatch, fnmatchcase

filelist = os.listdir()
print(filelist)
#找出以Dict开头文件名称
dictfile=[filename for filename in filelist if fnmatch(filename,'Dict*')]
print(dictfile)
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('first001','first[0-9]*'))
#完全根据大小写匹配
print(fnmatchcase('first001','FIRST[0-9]*'))