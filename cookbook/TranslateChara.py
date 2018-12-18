#coding=utf8
'''文本过滤和清理 仅需要一个替换map 告诉文本将什么替换成什么'''
import re

str="i\tam\fa\rbig\nboss! "
remap={ord('\t'):" ",ord('\r'):" ",ord('\f'):" ",ord('\n'):" "}
#只需要传入一个map
str2=str.translate(remap)
print(str2)

