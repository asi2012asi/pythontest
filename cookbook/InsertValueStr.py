#coding=utf8
'''python并不直接支持在字符串中对变量做简单的值替换 但是可以通过format来模拟'''

str1='{name} is {age} years old!'
str2=str1.format(name='yaoming',age='30')
print(str2)

#也可以来自于已经定义的变量 使用format_map() 传入一个map对象即可
name='lilei'
age=29
print(vars()['name'])
str3=str1.format_map(vars())
print(str3)


