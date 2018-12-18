#coding=utf8
'''替换文本 '''

import re

#最简单的方式时 直接调用字符串类型的replace 注意第一个参数不能使用正则
str1="i come from guangzhou !"
str2=str1.replace('guangzhou','guangdong');
print(str2)

#第二种使用 re包的sub函数 第一个参数可以使用正则
str3=re.sub(r'g.*u','guangdong',str1)
print(str3)

#可以包含分组 也可以先预编译
str4='i am born on 09/15/1988 , and now is 12/12/2018, I am 30 years old'
pett=re.compile(r'(\d+)/(\d+)/(\d+)')
#使用\123 来对分组的数字重新分配
str5=pett.sub(r'\3年\1月\2日',str4)
print(str5)

#如果想知道替换了几次 可以使用subn
str6,n =pett.subn(r'\3年\1月\2日',str4)
print(str6)
print(n)