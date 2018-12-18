#coding=utf8
'''文本模式的匹配和查找'''

#匹配简单的文字 直接采用str自带的math
import re

print('first001.txt'.endswith('.txt'))
#稍微复杂的可以采用re包的match 如果能符合就反馈match对象 如果不能匹配会反馈None 所以经常配合if使用
if re.match(r'.*[0-9]+.*','first001.txt') :
    print('match result')

#如果是需要匹配多次的 可以先预编译
pett= re.compile(r'.*[0-9]+.*')
print('match' if pett.match('first001.txt') else 'not match')
print('match' if pett.match('second.txt') else 'not match')

#如果想找到所有的匹配项 返回一个列表 可以使用findall
str1='I am a student fom guangdong university of technology! Good evening every body!'
pett2=re.compile(r'[a-z]+!')
print(pett2.findall(str1))

#使用group 分组
datepet=re.compile(r'(\d+)/(\d+)/(\d+)')
m=datepet.match('12/11/2018')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

#上面展示的使用findall的方式返回列表 可以使用finditer的方式返回迭代器