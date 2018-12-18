#coding=utf8
'''匹配多行的正则表达式'''
import re

comment1='/*I am a comment1. */'
comment2='''/* I am a 
 common2. */'''

content=re.findall(r'/\*(.*?)\*/',comment1)
print(content)

#多行无法直接匹配
content2=re.findall(r'/\*(.*?)\*/',comment2)
print(content2)
#可以加上或使用(?:.|\n)代替. 来匹配任意字符或换行
content3=re.findall(r'/\*((?:.|\n)*?)\*/',comment2)
print(content3)
#使用re.DOTALL可以做的比较优雅
content4=re.findall(r'/\*(.*?)\*/',comment2,re.DOTALL)
print(content4)

