#coding=utf8
'''定义最短匹配的正则表达式 一般的表达式都是贪婪模式'''
import re

str='I am a "good" student,also a "bad" boy!'
matchstr=re.findall(r'"(.*)"',str)
print(matchstr)

#要最短匹配 主要在匹配时 后面加个?即可最短匹配
match2=re.findall(r'"(.*?)"',str)
print(match2)